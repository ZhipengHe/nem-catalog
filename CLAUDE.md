# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

`nem-catalog` is a **JSON URL catalog + JSON Schema** for AEMO NEMWEB, with a thin Python SDK on top. The catalog artifact (`catalog.json`, CC0) is the primary deliverable; the SDK (MIT, stdlib only) is a thin convenience layer. Non-Python consumers (R, Julia, shell) use the JSON directly.

- Versioning: SemVer for the SDK, CalVer (`YYYY.MM.DD`) for `catalog.json`.
- Stability: v0.1 is experimental. Only ~16% of 362 dataset keys resolve cleanly via `resolve()` — the rest raise `NonResolvableTemplateError`. `list_urls()` for non-temporal keys is v0.2 scope (issue #15).
- Runtime deps: **none**. Dev deps pinned in `pyproject.toml [project.optional-dependencies].dev`.

## Common commands

Use `uv`, not `pip` (project standard; `uv.lock` is committed).

```bash
uv sync --extra dev                 # one-time setup
uv run pre-commit install           # local hook install
uv run pytest                       # all tests
uv run pytest tests/test_resolve.py::test_name  # single test
uv run pytest --cov=nem_catalog --cov-fail-under=90  # mirrors CI gate
uv run ruff check . && uv run ruff format --check .
uv run mypy --strict                # files = ["src"] per pyproject
bash tests/readme_examples.sh       # shell README examples (CI runs this)
```

Pipeline scripts (module-mode invocation; runs under CI weekly):

```bash
uv run python scripts/nemweb_download.py --policy patterns/curated/freshness-policy.yaml 10000
uv run python -m scripts.extract_patterns --policy patterns/curated/freshness-policy.yaml
uv run python scripts/merge_catalog.py --auto patterns/auto/catalog.json --curated patterns/curated/ --out catalog.json
```

## Architecture — pipeline + SDK

Two layers, glued by `catalog.json`.

**Build pipeline** (weekly GHA `weekly-refresh.yml`, Mon 03:00 UTC):

1. `scripts/nemweb_download.py` mirrors NEMWEB directory listings into `nemweb-mirror/` (1 req/s, byte-exact HREFs, content-aware `save_listing()` to suppress IIS template drift). Policy-driven: `patterns/curated/freshness-policy.yaml` classifies paths as `rolling | append_only | static | parent_index` — static paths are skipped.
2. `scripts/extract_patterns.py` walks the mirror and emits `patterns/auto/catalog.json` (gitignored; regenerated every run). This file is the source of truth for `path_template`, `filename_template`, `filename_regex`, `observed_range`.
3. `scripts/merge_catalog.py` overlays `patterns/curated/*.yaml` onto the auto output and writes top-level `catalog.json`. Merge rules live in `docs/architecture.md §Merge semantics` — curated wins on overlap (warns), curated keys without `curated_only: true` that are missing from auto **fail the build** (suspected AEMO deletion).
4. On diff, the workflow opens a PR; on failure (`PolicyLoadError`, `HREFExtractionShiftError`, WAF >5% non-200), opens a P0/P1 issue and keeps serving the last-good artifact.

Separate monthly `policy-audit.yml` (1st of month 00:00 UTC) force-refetches into a side directory, diffs HREF sets vs. policy classifications, and opens a drift issue or a clean-audit bump PR. Shares concurrency group `nemweb-mirror-refresh` with `weekly-refresh.yml`.

**Python SDK** (`src/nem_catalog/`):

- `loader.py` — `load(path_or_url)` (deterministic, library-pure) and `fetch_latest()` (ETag cache + last-good fallback).
- `catalog.py` — immutable `Catalog` class. `resolve(key, from_, to_, view=None)` expands `(dataset, date range) → list[URL]`. Raises `NonResolvableTemplateError` when a selected tier's template contains a non-temporal token (`{aemo_id}`, `{nn}`, `{d2}`). `_TEMPORAL_TOKENS` must stay in sync with the extractor's token vocabulary — see the warning comment around line 32 of `catalog.py`.
- `errors.py` — error hierarchy rooted at `NemCatalogError`.

**Taxonomy** (per `reference/NEMWEB-STRUCTURE.md`):

- Exactly four repos: `Reports`, `MMSDM`, `NEMDE`, `FCAS_Causer_Pays`.
- Dataset identity = `(repo, intra_repo_id)`. **Cross-repo keys are default-separate.** `Reports:DispatchIS_Reports` and `MMSDM:DISPATCHIS` are distinct until proven identical per the §4 evidence bar (AEMO doc, column-schema match, or internal cross-reference). Do not merge on name similarity.

## Repo-specific discipline (non-obvious, load-bearing)

- **Case-sensitive by design.** AEMO enforced case sensitivity on 2026-04-21. Catalog entries record tier-specific casing byte-exact (§3.1 lists three split-casing streams). Reject any `.casefold()` / `.lower()` suggestion from reviewers; the byte-exact contract is the discipline.
- **Protected paths — never let formatters touch them.** `.pre-commit-config.yaml` excludes `nemweb-mirror/`, `reference/`, `catalog.json`, `patterns/auto/`, `uv.lock` globally. These are byte-preserved captures or build artifacts. Whitespace/EOF hooks would break the "exactly what AEMO served" contract `extract_patterns.py` depends on.
- **Ground-truth first — don't invent example values.** When writing tests/examples/docs that reference URLs, regexes, filenames: `grep` `reference/URL-CONVENTIONS.md|csv` or the mirror first. Never hand-write a template from memory. `extract_patterns.py` output wins over hand-written docs.
- **Fix the code, not the cached captures.** If a script misbehaves against `nemweb-mirror/`, add a `--force` / `--refresh` flag. Do **not** `rm -rf nemweb-mirror/` as a workaround — that destroys source-of-truth data.
- **sdist allowlist is explicit** in `pyproject.toml [tool.hatch.build.targets.sdist]`. The repo carries ~58 MB of research artifacts (`nemweb-mirror/`, `.plans/`, `reference/`) that must NOT ship to PyPI. If you add a new top-level directory that should ship, update the `include` list.
- **Curated overlay boundary.** `patterns/curated/` = human judgment only (`anomaly_note`, `schema_source`, `query_shape`, `curated_only: true` placeholders). If the extractor is wrong, fix the extractor — do not paper over it with a curated override. See `patterns/curated/README.md`.
- **SHA-pin GitHub Actions to commit, not tag-object.** When updating action pins: check `.object.type` from the GitHub API and follow through if `"tag"` — annotated tags resolve to tag-object SHAs, not commit SHAs.

## Scope + release cadence

Where to look, in order of specificity:

- `.plans/TODOS.md` — **active scope**. Committed, in-flight, and un-tagged master work, grouped by release. This is the source of truth for "what's next".
- `.plans/<version>-*.md` — **per-release / per-PR implementation plans** (e.g. `v0.1.2-pr1-duplicate-filter.md`). Authored before the PR, kept after merge for archaeology.
- `ROADMAP.md` — **aspirational candidates**. Items graduate to TODOS.md only on user-demand / ecosystem-gap / maintainer-tedium signal.
- `CHANGELOG.md` — shipped work, Keep-a-Changelog format.

Issue tracking lives on GitHub. Most TODOS.md subsections cite their issue number inline (e.g. `list_urls` = #15, observed-range retention = #16, extractor classifier gap = #21, `write_json` schema collapse = #22, v0.2 pre-tag gate = #14). When working on a listed item, check the linked issue first — scope often sharpens there. User-reported 404s use `.github/ISSUE_TEMPLATE/catalog-url-404.md`.

Release rules:

- Patch releases (`.x.x.PATCH`) are bug-fix-only and tagged **only** when a downstream consumer needs a pinned release. Otherwise fixes roll into the next minor. **Features dressed as patches are forbidden** — v0.1.1 accidentally shipped a feature as a patch; do not repeat that.
- Commit convention: Conventional Commits. Types: `feat`, `fix`, `docs`, `chore`, `test`, `refactor`, `perf`, `style`. Scopes: `data`, `model`, `utils`, `workflow`, `config`, `docs`.

## Reference layer

`reference/` holds ground-truth docs and CSVs derived from primary-source captures. Treated like build artifacts — byte-preserved, excluded from formatting, regenerable from the mirror.

- `NEMWEB-STRUCTURE.md` — authoritative layout + anomaly list. Cite section numbers when making structural claims.
- `URL-CONVENTIONS.md` / `.csv` — build artifact, not source. Do not hand-edit.
- `MMSDM-*` files — DDL/timeline/rename data for future mid-term schema-embedding work (v0.3–v0.5 roadmap).
- `aemo-mmsdm-docs/` and `aemo-catalog/` are gitignored captures; `INVENTORY.md` / `FETCH-MANIFEST.md` are the committed provenance manifests.
