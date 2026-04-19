# Troubleshooting

<a id="unresolvable-dataset"></a>
## #unresolvable-dataset

`UnresolvableDatasetError` means the dataset key exists in the catalog but the record has `resolvable: false` — typically a directory-level anomaly (e.g., `NEXT_DAY_OFFER_ENERGY)SPARSE`) where AEMO published a directory with zero files.

**Fix:** check the `anomaly_note` field on the record for details. If you believe it should be resolvable, open an issue with a concrete example URL you expected.

<a id="non-resolvable-template"></a>
## #non-resolvable-template

`NonResolvableTemplateError` means one of the tiers selected by `resolve()` has a filename or path template containing a placeholder the v0.1 SDK cannot compute from a date range — typically `{aemo_id}` (per-participant), `{nn}` (file sequence), or `{d2}` (MMSDM end-of-range day marker).

Rather than return a URL with unsubstituted `{token}` literals (which would 404), `resolve()` raises. The error includes:

- `.dataset_key` — the key you passed
- `.tier` — the specific tier (e.g., `"CURRENT"`) that can't be built
- `.tokens` — the placeholder names missing values (e.g., `frozenset({"aemo_id"})`)

**Fix options:**

1. **Pin to an older date range** that only hits a pure-temporal tier (e.g., ARCHIVE tiers of `Reports:*` use `{date}` alone).
2. **Inspect the raw template** via `catalog.datasets[key]['tiers'][tier]` and build the URL with your own participant ID or by listing the directory.
3. **Wait for v0.2** — an enumeration API (`list_urls(key, from_, to_, **overrides)`) is planned.

**Background:** AEMO's rolling CURRENT filenames frequently embed a 16-digit participant ID like `PUBLIC_DISPATCHIS_202604160445_0000000513144978.zip`. There's no way to enumerate those IDs from a date range alone; you have to list the directory on NEMWEB and filter.

<a id="incompatible-catalog"></a>
## #incompatible-catalog

`IncompatibleCatalogError` means the catalog's `schema_version` MAJOR is not supported by your SDK version. SDK 0.1.x supports schema `1.x`.

**Fix:** upgrade the SDK (`pip install -U nem-catalog`) or pin an older catalog version.

<a id="fetch-failed"></a>
## #fetch-failed

`NemCatalogFetchError` means the live fetch failed AND no cache was available.

**Fix:** check network connectivity; manually download the catalog from the Releases page and pass it to `nem_catalog.load()` directly.

## Empty result from resolve() with a warning

The requested date range is entirely outside the dataset's `observed_range`. No error — empty list + `warnings.warn`. Check the catalog record's `observed_range` for each tier; pick a range that overlaps.

## Key typo — KeyError suggestion

`KeyError` includes a `Did you mean` suggestion via `difflib`. Use the suggested spelling or browse `catalog.dataset_keys()`.

## curl + jq returns `null`

Your dataset key is wrong. List valid keys:

```bash
curl -s https://zhipenghe.github.io/nem-catalog/catalog.json \
  | jq '.dataset_keys[]' | grep -i YOUR_SEARCH
```
