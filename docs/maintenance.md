# Repository maintenance and audit

## Website implementation

The root homepage is now a standalone, responsive HTML website for qubuhuborg. It no longer contains the unrelated Jinja/Sphinx Python documentation template.

- `index.html` provides semantic page structure, metadata, Organization JSON-LD and accessible navigation.
- `assets/css/site.css` contains the responsive design system and uses system fonts to avoid a runtime font-provider dependency.
- `assets/js/site.js` provides progressive mobile navigation and the current footer year.
- `assets/favicon.svg` provides the vector Q brand mark.
- `tests/test_site.py` checks document structure, navigation targets, local asset references and required brand content.

## Deployment architecture

- `.github/workflows/static.yml` is the only production deployment workflow.
- The production workflow runs the Python test suite and stages only `index.html` and `assets/` into the Pages artifact. Source notebooks, documentation and repository tooling are not copied into the published site artifact.
- `.github/workflows/jekyll-gh-pages.yml` is retained as a pull-request/manual build-validation workflow. It has no Pages deployment permissions and does not publish.
- `.github/workflows/validate-and-update.yml` runs tests on pushes and pull requests. Write permission is scoped to the scheduled/manual profile-update job.

## Existing functionality retained

The implementation leaves the following areas intact:

- `.github/profile/README.md` and the organization profile updater.
- `scripts/update_readme.py` and its existing unit tests.
- Jupyter notebooks under `Notebook/`.
- Documentation and changelog history.
- The legacy notebook executor and package-specific material.

## Audit findings and follow-up

- The previous root `index.html` was a Python documentation template and could not function as a standalone corporate homepage.
- Two workflows previously attempted production Pages deployment on pushes to `main`, creating competing deployments. Production deployment is now assigned to `static.yml` alone.
- The former root `bash` file was not a coherent portable shell script; its content is documented in `docs/legacy-build-notes.md`. Do not execute it as Bash.
- `scripts/notebook_executor.py` is legacy Beam interactive-test code with optional third-party dependencies. It was preserved rather than rewritten without its original runtime and compatibility matrix. It should receive a dedicated dependency and security review before being used with untrusted notebooks.
- The organization profile's separate `index.md` and unusual legacy documentation paths were not deleted because their intended ownership and use have not been established.

## Local validation

Run the standard-library test suite from the repository root:

```sh
python -m unittest discover -s tests -v
```
