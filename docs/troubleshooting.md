# Troubleshooting

<a id="unresolvable-dataset"></a>
## #unresolvable-dataset

`UnresolvableDatasetError` means the dataset key exists in the catalog but the record has `resolvable: false` — typically a directory-level anomaly (e.g., `NEXT_DAY_OFFER_ENERGY)SPARSE`) where AEMO published a directory with zero files.

**Fix:** check the `anomaly_note` field on the record for details. If you believe it should be resolvable, open an issue with a concrete example URL you expected.

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
