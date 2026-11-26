# qubuhuborg

Corporate website and organization resources for **qubuhuborg** — engineering intelligence and building the future.

## Website

The production website is a lightweight, responsive static site deployed with GitHub Pages.

- `index.html` — semantic homepage and SEO metadata.
- `assets/css/site.css` — responsive design system and visual styling.
- `assets/js/site.js` — accessible mobile navigation and dynamic copyright year.
- `assets/favicon.svg` — vector brand mark.
- `.github/workflows/static.yml` — the single production Pages deployment workflow.
- `.github/workflows/jekyll-gh-pages.yml` — legacy Jekyll build validation only; it does not deploy.

## Technology focus

- AI and machine learning
- Web4 applications
- Blockchain solutions
- Custom software
- Digital platforms
- Innovation and research

## Repository maintenance

The repository also retains its organization profile, notebooks, documentation history and Python profile updater. Website changes are isolated from those existing assets.

## Local validation

Requires Python 3.10 or later. No third-party packages are required for the test suite.

```sh
python -m unittest discover -s tests -v
```

To refresh the organization profile timestamp:

```sh
python scripts/update_readme.py
```

Recent blog posts are optional. Configure the repository variable `BLOG_FEED_URL` with a canonical HTTPS RSS or Atom feed URL. When unset, the updater makes no network request and leaves the blog section unchanged.

## Deployment

Pushes to `main` run the repository test suite, stage only the website files, and publish the resulting artifact to GitHub Pages. The Jekyll workflow is validation-only to prevent competing production deployments.
