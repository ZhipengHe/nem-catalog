# Changelog

All notable changes to nem-catalog are tracked here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). SemVer for the SDK; CalVer for the `catalog.json` artifact.

## [Unreleased]

## [0.1.0] — TBD

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
- Schema source for MMSDM tables is the portal root only. Per-table anchors deferred to v0.2.
- `retention_hint_unverified_days` is derived from a single 2026-04-18 mirror snapshot. v0.2 replaces with confidence range.
- No CLI in v0.1. Use the JSON directly from shell or R/Julia via the cookbook.
