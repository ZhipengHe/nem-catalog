# nem-catalog — Machine-readable URL catalog for AEMO NEMWEB

[![Catalog](https://img.shields.io/badge/catalog-live-blue)](https://zhipenghe.github.io/nem-catalog/catalog.json)
[![Schema](https://img.shields.io/badge/schema-v1.0.0-green)](https://zhipenghe.github.io/nem-catalog/catalog.schema.json)
[![PyPI](https://img.shields.io/pypi/v/nem-catalog)](https://pypi.org/project/nem-catalog/)
[![License: MIT](https://img.shields.io/badge/license-MIT%20%2B%20CC0-brightgreen)](LICENSE)
[![Last successful crawl](https://img.shields.io/badge/last%20crawl-TBD-lightgrey)](https://github.com/ZhipengHe/nem-catalog/actions/workflows/weekly-refresh.yml)

A versioned JSON catalog + JSON Schema that maps `(NEMWEB dataset key, time range) → candidate URLs`, covering all four NEMWEB repositories (`Reports`, `MMSDM`, `NEMDE`, `FCAS_Causer_Pays`). Released under MIT (code) and CC0 (catalog data).

## Quick start — no install required

```bash
curl -s https://zhipenghe.github.io/nem-catalog/catalog.json \
  | jq '.datasets["Reports:DispatchIS_Reports"].tiers.ARCHIVE'
```

Output:

```json
{
  "path_template": "/Reports/ARCHIVE/DispatchIS_Reports/",
  "filename_template": "PUBLIC_DISPATCHIS_{date}.zip",
  "filename_regex": "^PUBLIC_DISPATCHIS_\\d{8}\\.zip$",
  "example": "PUBLIC_DISPATCHIS_20250407.zip",
  "cadence": "daily_rollup"
}
```

Build the full URL: `https://nemweb.com.au` + `path_template` + `filename_template` (with `{date}` substituted as `yyyymmdd`). Placeholder vocabulary is in the catalog's top-level `placeholders` field.

## Stability

v0.1 is **experimental**. API may change before v1.0. For reproducible research, pin the catalog version:

```python
catalog = nem_catalog.fetch_latest(catalog_version="2026.04.18")
```

## Python usage

```bash
pip install nem-catalog
```

```python
import nem_catalog

# Primary (library-pure, deterministic):
catalog = nem_catalog.load("catalog.json")

urls = catalog.resolve(
    "Reports:DispatchIS_Reports",
    from_="2025-04-01",
    to_="2025-04-02",
)
# → list of candidate URLs. Caller is responsible for reachability.

# Convenience (live fetch + cache + fallback):
catalog = nem_catalog.fetch_latest()

# Preview cardinality before materializing:
n = catalog.count("MMSDM:DISPATCHPRICE", from_="2024-01-01", to_="2024-12-31")
```

## Not for you if...

- You want a **pandas DataFrame** of NEMWEB data → use [NEMOSIS](https://github.com/UNSW-CEEM/NEMOSIS). It's the production-grade Python pipeline for researchers.
- You want **forecast data** (pre-dispatch, PASA) → use [NEMSEER](https://github.com/UNSW-CEEM/NEMSEER).
- You want **emissions data** → use [NEMED](https://github.com/UNSW-CEEM/NEMED).

`nem-catalog` serves the layer *below* these tools: a shared metadata + canonical JSON shape describing NEMWEB's URL grammar. Non-Python consumers (R, Julia, shell) can use the JSON directly without installing anything.

## Shell cookbook (R/Julia/shell users)

See [`docs/cookbook.md`](docs/cookbook.md) for recipes including URL expansion, date iteration, and parallel download with `xargs`.

## How it's built

See [`docs/architecture.md`](docs/architecture.md). Briefly: `extract_patterns.py` mirrors NEMWEB directory listings weekly, derives URL patterns, and a hybrid auto+curated merge produces `catalog.json`. Weekly GitHub Actions runs the whole pipeline and opens a PR on diffs.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

- Code: MIT. See [`LICENSE`](LICENSE).
- Catalog JSON: CC0 (public domain).
