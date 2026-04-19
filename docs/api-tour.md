# nem-catalog API tour (1 page, 3 use cases)

## 1. Python researcher: get URLs for a date range

```python
import nem_catalog

catalog = nem_catalog.load("catalog.json")   # or fetch_latest() for live
urls = catalog.resolve(
    "Reports:DispatchIS_Reports",
    from_="2025-04-01",
    to_="2025-04-30",
)
# 30 URLs (daily rollups)
```

**v0.1 limit:** `resolve()` only returns URLs when the tier's filename can be
built from a date range alone. Rolling CURRENT filenames that embed a
participant ID (`{aemo_id}`) or file sequence (`{nn}`) raise
`NonResolvableTemplateError` — see [`troubleshooting.md#non-resolvable-template`](troubleshooting.md#non-resolvable-template).
Workaround for v0.1: query an ARCHIVE-covered date range, or inspect the raw
template via `catalog.datasets[key]['tiers']` and build URLs yourself.

## 2. Non-Python shell user: grep for datasets, expand template

```bash
# Find all Dispatch-named datasets
curl -s https://zhipenghe.github.io/nem-catalog/catalog.json \
  | jq -r '.dataset_keys[] | select(startswith("Reports:Dispatch"))'

# Get one template, expand it
curl -s https://zhipenghe.github.io/nem-catalog/catalog.json \
  | jq -r '.datasets["Reports:DispatchIS_Reports"].tiers.ARCHIVE'
```

## 3. Tool-builder: consume catalog as a metadata dependency

```python
from nem_catalog import load

class MyDownloader:
    def __init__(self, catalog_path: str):
        self.catalog = load(catalog_path)  # deterministic, no I/O defaults

    def list_all_aux(self) -> list[str]:
        # Full 367+ including AUX and utility entries
        return self.catalog.raw_keys()

    def urls_for(self, key: str, from_: str, to_: str) -> list[str]:
        return self.catalog.resolve(key, from_=from_, to_=to_)
```

See the full public API in `src/nem_catalog/catalog.py`.
