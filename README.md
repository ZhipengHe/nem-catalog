# nem-catalog — Machine-readable URL catalog for AEMO NEMWEB

[![Catalog](https://img.shields.io/badge/catalog-live-blue)](https://zhipenghe.me/nem-catalog/catalog.json)
[![Schema](https://img.shields.io/badge/schema-v1.0.0-green)](https://zhipenghe.me/nem-catalog/catalog.schema.json)
[![PyPI](https://img.shields.io/pypi/v/nem-catalog)](https://pypi.org/project/nem-catalog/)
[![License: MIT](https://img.shields.io/badge/license-MIT%20%2B%20CC0-brightgreen)](LICENSE)
[![Last successful crawl](https://img.shields.io/badge/last%20crawl-TBD-lightgrey)](https://github.com/ZhipengHe/nem-catalog/actions/workflows/weekly-refresh.yml)

A versioned JSON catalog + JSON Schema that maps `(NEMWEB dataset key, time range) → candidate URLs`, covering all four NEMWEB repositories (`Reports`, `MMSDM`, `NEMDE`, `FCAS_Causer_Pays`). Released under MIT (code) and CC0 (catalog data).

## Quick start — no install required

```bash
curl -s https://zhipenghe.me/nem-catalog/catalog.json \
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
n = catalog.count("Reports:DispatchIS_Reports", from_="2024-01-01", to_="2024-12-31")
```

> **Expected `UserWarning`:** `Reports:*` datasets with both an ARCHIVE and a
> rolling CURRENT tier emit a one-line warning when you query historical
> (ARCHIVE-era) dates. The SDK is telling you the live tier has no data that
> old, so it routed to ARCHIVE. The returned URLs are correct.

### Not every dataset resolves to concrete URLs in v0.1

> **Coverage in v0.1:** roughly **1 in 6** of the 362 dataset keys resolve
> cleanly today (~16%, mostly `Reports:*` ARCHIVE tiers). The remaining ~84%
> raise `NonResolvableTemplateError` — including almost all `MMSDM:*` tables
> (file-sequence suffix `{d2}`/`{nn}`) and every live CURRENT tier (16-digit
> publish ID `{aemo_id}`).
>
> Per repo: `Reports` 53/96 (55%), `MMSDM` 4/259 (~2%), `NEMDE` 2/6,
> `FCAS_Causer_Pays` 0/1. v0.2 will add `list_urls()` for the non-temporal
> cases by reading NEMWEB directory listings.

`resolve()` only returns URLs when the tier's filename template can be built
from a date range alone. AEMO filenames in rolling CURRENT tiers often embed a
participant ID (e.g. `{aemo_id}`) or a file-sequence suffix (e.g. `{nn}`) that
the SDK cannot compute without extra input. For those, `resolve()` raises
`NonResolvableTemplateError` rather than return a broken URL string.

```python
# Raises NonResolvableTemplateError — CURRENT filename has {aemo_id}
catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-17", to_="2026-04-18")

# Works — ARCHIVE filename is pure temporal
catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-01", to_="2025-04-02")
```

Inspect the raw template for any dataset via `catalog.datasets[key]['tiers']`
and build the URL yourself, or pin the query to an ARCHIVE-covered date range.
A future release will add an enumeration API for these datasets.

## Not for you if...

- You want a **pandas DataFrame** of NEMWEB data → use [NEMOSIS](https://github.com/UNSW-CEEM/NEMOSIS). It's the production-grade Python pipeline for researchers.
- You want **forecast data** (pre-dispatch, PASA) → use [NEMSEER](https://github.com/UNSW-CEEM/NEMSEER).
- You want **emissions data** → use [NEMED](https://github.com/UNSW-CEEM/NEMED).

`nem-catalog` serves the layer *below* these tools: a shared metadata + canonical JSON shape describing NEMWEB's URL grammar. Non-Python consumers (R, Julia, shell) can use the JSON directly without installing anything.

## Shell cookbook (R/Julia/shell users)

See [`docs/cookbook.md`](docs/cookbook.md) for recipes including URL expansion, date iteration, and parallel download with `xargs`.

## Freshness metadata (v0.1.1+)

The catalog carries optional freshness fields populated by CI at crawl time.

**Catalog-level** (top-level keys in `catalog.json`):

| Field | Type | Description |
|---|---|---|
| `last_crawl_attempted_at` | ISO 8601 | When the weekly crawl step started |
| `last_crawl_completed_at` | ISO 8601 | When the crawl step finished (absent means partial crawl — not published) |

**Per-dataset** (inside each `datasets[key]` entry):

| Field | Type | Description |
|---|---|---|
| `freshness_class` | `rolling \| append_only \| static \| parent_index` | Policy classification for crawl frequency |
| `last_observed_change_at` | ISO 8601 | Last time the mirror index for this dataset changed (from `git log`, not filesystem mtime) |

These fields are absent in catalog snapshots built before v0.1.1 and in the static catalog committed to this repo (which is built offline). They are present in every catalog artifact published by the weekly CI workflow.

## How it's built

See [`docs/architecture.md`](docs/architecture.md). Briefly: `nemweb_download.py --policy freshness-policy.yaml` mirrors NEMWEB directory listings weekly (skipping paths classified as `static`), `extract_patterns.py` derives URL patterns, and a hybrid auto+curated merge produces `catalog.json`. Weekly GitHub Actions runs the whole pipeline and opens a PR on diffs.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

- Code: MIT. See [`LICENSE`](LICENSE).
- Catalog JSON: CC0 (public domain).
