# gh.io

A small collection of documentation and reference files, primarily covering GitHub Copilot CLI and text markup. This repository does **not** contain the Copilot CLI implementation or a complete, runnable application.

## Contents

| Path | Description |
| --- | --- |
| `profile/index.md` | Copilot CLI overview, installation and usage notes, and links to official documentation. |
| `changelog.md` | Versioned Copilot CLI release notes, with entries dating from September to November 2025. |
| `Page/_index.rSt.md` | Reference text about reStructuredText and Markdown syntax. |
| `packages/rsc/README.md` | Another reStructuredText and Markdown reference document. |
| `__ docs/README.mdown` | A README-style overview of a separate Aura repository; its paths and setup instructions do not describe this repository’s contents. |
| `package/webview.dart` | An incomplete Flutter WebView example loading `https://flutter.dev`. |
| `input.pdf` | A PDF file. |
| `LICENSE.md` | Copyright and license terms for this repository. |

The repository also has empty or placeholder files, including `lib/main.dart`, `pubspec.yaml`, `src/page.web4.py`, and `notebook/Notebook.ipynb`. They do not currently provide runnable Flutter, Python, or notebook projects.

## GitHub Copilot CLI

The CLI information in `profile/index.md` is documentation, not executable code. It describes installing the CLI separately with npm:

```bash
npm install -g @github/copilot
copilot
```

That document lists Node.js 22 or later, npm 10 or later, and an active Copilot subscription as prerequisites. CLI features and requirements can change; consult the [official Copilot CLI documentation](https://docs.github.com/copilot/concepts/agents/about-copilot-cli) for current instructions.

## Development

There is no complete application or root build configuration to run. The root `pubspec.yaml` is empty, and the repository does not include a populated Flutter entry point or Python utility.

## License

`LICENSE.md` states that the contents are Copyright © GitHub 2025 and that use is subject to [GitHub’s Pre-release License Terms](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products#github-copilot-pre-release-license-terms). Review those terms before using or redistributing repository contents.
