# Troubleshooting

<a id="unresolvable-dataset"></a>
## #unresolvable-dataset

`UnresolvableDatasetError` means the dataset key exists in the catalog but the record has `resolvable: false` — typically a directory-level anomaly (e.g., `NEXT_DAY_OFFER_ENERGY)SPARSE`) where AEMO published a directory with zero files.

**Fix:** check the `anomaly_note` field on the record for details. If you believe it should be resolvable, open an issue with a concrete example URL you expected.

<a id="non-resolvable-template"></a>
## #non-resolvable-template

`NonResolvableTemplateError` means every tier `resolve()` would have expanded for your date range has a filename or path template containing a placeholder the v0.1 SDK cannot compute from a date range — typically `{aemo_id}` (per-participant), `{nn}` (file sequence), or `{d2}` (MMSDM per-file enumeration).

**Temporal tokens the v0.1 SDK knows:** `{date}`, `{yyyymmdd}`, `{timestamp}`, `{yyyymmddHHMM}`, `{yyyymmddhhmm}`, `{datetime}` (14-digit), `{yyyymmddhh}`, `{yearmonth}`, `{yyyymm}`, `{year}`, `{yyyy}`, `{month}`. Everything else is treated as non-temporal.

**Partial success:** If your query straddles multiple tiers and SOME of them are pure-temporal, `resolve()` returns URLs from the resolvable tiers and emits a `UserWarning` naming each tier it skipped. `NonResolvableTemplateError` only fires when ZERO candidate tiers could resolve.

The error includes:

- `.dataset_key` — the key you passed
- `.tier` — the tier (the first skipped one) that can't be built
- `.tokens` — the non-temporal placeholder names (e.g., `frozenset({"aemo_id"})`)

**Fix options:**

1. **Pin to an older date range** that only hits a pure-temporal ARCHIVE tier.
2. **Use `view=` to force a specific tier.** For MMSDM datasets with multiple views, pick one that's pure-temporal (rarely available — most use `{nn}`/`{d2}`).
3. **Inspect the raw template** via `catalog.datasets[key]['tiers'][tier][0]` (v2.0.0: each tier is a list of records; `[0]` selects the first) and build the URL with your own participant ID or by listing the directory on NEMWEB.
4. **Wait for v0.2** — an enumeration API (`list_urls(key, from_, to_, **overrides)`) is planned.

**Background:** AEMO's rolling CURRENT filenames frequently embed a 16-digit participant ID like `PUBLIC_DISPATCHIS_202604160445_0000000513144978.zip`. MMSDM SQLLoader files use a 1- or 2-digit FILE sequence number per month. There's no way to enumerate those values from a date range alone; you have to list the directory on NEMWEB and filter.

<a id="incompatible-catalog"></a>
## #incompatible-catalog

`IncompatibleCatalogError` means the catalog's `schema_version` MAJOR is not supported by your SDK version. SDK 0.1.x (post-#22) supports schema `2.x`.

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
curl -s https://zhipenghe.me/nem-catalog/catalog.json \
  | jq '.dataset_keys[]' | grep -i YOUR_SEARCH
```
