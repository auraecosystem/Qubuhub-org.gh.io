import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.assets = []
        self.tags = set()
        self.title_text = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.add(tag)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("href"):
            self.assets.append(attrs["href"])
        if tag == "script" and attrs.get("src"):
            self.assets.append(attrs["src"])
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)


class CorporateSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = INDEX.read_text(encoding="utf-8")
        cls.parser = SiteParser()
        cls.parser.feed(cls.html)
        cls.parser.close()

    def test_homepage_is_a_standalone_html_document(self):
        self.assertIn("<!doctype html>", self.html.lower())
        self.assertIn("<html lang=\"en\">", self.html)
        self.assertIn("qubuhuborg", " ".join(self.parser.title_text).lower())
        self.assertNotRegex(self.html, re.compile(r"\{\{|\{%"))

    def test_required_semantic_regions_exist(self):
        for tag in ("header", "nav", "main", "section", "footer"):
            self.assertIn(tag, self.parser.tags)

    def test_navigation_fragments_resolve(self):
        fragments = [urlsplit(link).fragment for link in self.parser.links if urlsplit(link).fragment]
        self.assertTrue(fragments)
        for fragment in fragments:
            self.assertIn(fragment, self.parser.ids, f"Missing target for #{fragment}")

    def test_local_assets_exist(self):
        for asset in self.parser.assets:
            parsed = urlsplit(asset)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            self.assertTrue((ROOT / parsed.path).is_file(), f"Missing local asset: {asset}")

    def test_mobile_navigation_has_accessible_controls(self):
        self.assertIn('aria-label="Main navigation"', self.html)
        self.assertIn('aria-expanded="false"', self.html)
        self.assertIn("data-menu-toggle", self.html)

    def test_company_name_and_service_content_are_present(self):
        for phrase in ("qubuhuborg", "AI &amp; Machine Learning", "Web4 Applications",
                       "Blockchain Solutions", "Custom Software", "Digital Platforms",
                       "Innovation Lab"):
            self.assertIn(phrase, self.html)


if __name__ == "__main__":
    unittest.main()
