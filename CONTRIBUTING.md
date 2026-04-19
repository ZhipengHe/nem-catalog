# Contributing to nem-catalog

Most contribution scope for v0.1 falls into two categories.

## 1. Report a wrong URL

If a URL from `resolve()` 404s or returns unexpected content:

1. Open an issue using the `.github/ISSUE_TEMPLATE/catalog-url-404.md` template.
2. Include the dataset key, date range, and one concrete URL that failed.

## 2. Add a curated entry for a new anomaly

If you find a NEMWEB dataset the extractor describes incorrectly (wrong casing, missing retention hint, misleading `filename_template`):

1. Fork the repo.
2. Add or update the relevant YAML in `patterns/curated/<repo>.yaml`.
3. Include: `anomaly_note` describing the issue, `query_shape` if you know the right inputs.
4. Run `pytest tests/test_merge_catalog.py` to confirm your YAML parses.
5. Submit a PR.

**What does NOT go in `patterns/curated/`:**
- Regenerated pattern rows. Those are the extractor's job.
- Entire URL schemas for Reports streams (v0.2 concern).

## Development setup

```bash
uv sync --extra dev
uv run pytest
uv run pre-commit install
```

All PRs must pass `ruff check`, `ruff format --check`, `mypy --strict`, and `pytest`.

## Commit convention

[Conventional Commits](https://www.conventionalcommits.org/). Types: `feat`, `fix`, `docs`, `chore`, `test`, `refactor`. Scopes: `data`, `model`, `utils`, `workflow`, `config`, `docs`.

Example: `feat(data): add curated entry for Reports:DispatchIS_FCAS_Fix`.
