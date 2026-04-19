# Changelog

All notable changes to nem-catalog are tracked here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). SemVer for the SDK; CalVer for the `catalog.json` artifact.

## [Unreleased]

## [0.1.1] — 2026-04-20

### Added
- Policy-driven refresh: `patterns/curated/freshness-policy.yaml` classifies 2863 mirror listings as `rolling | append_only | static | parent_index`. Weekly crawler refetches rolling/append_only/parent_index paths and skips static paths.
- `scripts/policy.py` — `Policy.load` + `Policy.class_for` with ant-style glob patterns, longest-match-wins precedence.
- `--policy <yaml-path>` flag on `scripts/nemweb_download.py`.
- Content-aware write in `save_listing()`: skips writes when extracted HREF set matches cached file. Suppresses ~82% of AEMO IIS 8.5 template drift (server renders filesystem mtimes into directory listings).
- Template-shift guard `HREFExtractionShiftError`: raised when HREF extraction drops ≥50% vs. cached or to zero. Forensic bytes written before raise.
- Catalog-level `last_crawl_attempted_at` and `last_crawl_completed_at` sourced from CI env vars at crawl-step boundaries. Partial-crawl catalogs never shipped.
- Per-dataset `freshness_class` (from policy classification) and `last_observed_change_at` (from `git log -1 --format=%aI` on the mirror index, NOT filesystem mtime).
- Schema additions: 4 new optional fields in `schemas/catalog.schema.json`. `schema_version` unchanged at `1.0.0`.
- `scripts/audit_policy.py` — stateless monthly audit. Compares fresh-refetch HREF-diffs against policy classification and emits `reclassify_up | reclassify_down | new_path` findings.
- `.github/workflows/policy-audit.yml` — first-Monday-of-month cron. Force-refetches into a side directory and opens a P1 issue on drift or a chore PR on clean.

### Changed
- `.github/workflows/weekly-refresh.yml`: replaced the non-functional day-of-month gaps/full mode gate with a single policy-driven crawl. Added concurrency group `nemweb-mirror-refresh` (shared with policy-audit). Crawl failure opens a P0 issue; all publish steps gated on crawl success.
- `scripts/extract_patterns.py` CLI now uses module-mode invocation (`python -m scripts.extract_patterns --policy ...`).

### Fixed
- Weekly cron actually refreshes the mirror. Root cause: the walker short-circuited on cached files regardless of mode (`--gaps` and `--full` were both no-ops once the mirror had any content).

Refs: #3

## [0.1.0] — 2026-04-19

### Added

- JSON Schema v1.0.0 for the catalog artifact.
- Python SDK (pure stdlib):
  - `nem_catalog.load(path_or_url)` — deterministic loader.
  - `nem_catalog.fetch_latest(cache_dir=, catalog_version=)` — opt-in live fetch with ETag cache and last-good fallback.
  - `Catalog.resolve(key, from_, to_, view=None)` — URL expansion + tier routing.
  - `Catalog.count(key, from_, to_, view=None)` — preview cardinality.
  - `Catalog.list_datasets(filter=, include_raw=False)` — discovery.
  - Error types: `KeyError` (difflib-suggested), `ValueError`, `IncompatibleCatalogError`, `NemCatalogFetchError`, `UnresolvableDatasetError`.
- Weekly GitHub Actions workflow: crawl → extract → merge → validate → PR.
- `patterns/auto/` (generated) + `patterns/curated/` (human) hybrid source.
- Catalog JSON shape: `placeholders`, `dataset_keys` (curated), `raw_keys` (full), per-record `query_shape` and `resolvable`.
- Docs: architecture, cookbook, api-tour, aemo-coordination, troubleshooting.
- CI-tested README examples (doctest + shell).

### Caveats

- v0.1 is **experimental**. API may change before v1.0.
- **Resolve coverage:** ~16% of the 362 dataset keys (mostly `Reports:*` ARCHIVE) resolve cleanly via `resolve()`. The remaining ~84% raise `NonResolvableTemplateError` — almost all of `MMSDM:*` (file-sequence `{d2}`/`{nn}`) and every live CURRENT tier (`{aemo_id}`). v0.2 will add `list_urls()`. See [`docs/troubleshooting.md#non-resolvable-template`](docs/troubleshooting.md#non-resolvable-template).
- Schema source for MMSDM tables is the portal root only. Per-table anchors deferred to v0.2.
- `retention_hint_unverified_days` is derived from a single 2026-04-18 mirror snapshot. v0.2 replaces with confidence range.
- No CLI in v0.1. Use the JSON directly from shell or R/Julia via the cookbook.
