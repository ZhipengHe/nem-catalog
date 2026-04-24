# Issue #17 scope correction — findings from codex review 2026-04-24

Codex review against `reference/URL-CONVENTIONS.csv` + `patterns/auto/catalog.json`. Counts independently reproduced.

## Corrected counts

| Metric | Issue body | Actual |
|---|---|---|
| Collapsing (key, tier) groups | 28 | **67** |
| Rows overwritten by `write_json` | 76 | **1166** |

The original count grouped rows by `(repo, tier, intra_repo_id, path_template)` — path-level multiplicity only. It did not count filename-family multiplicity within the same path.

## Filename-family collapse within the same path

Examples confirmed against the flat CSV:

| Dataset | Tier | Distinct (path, filename) tuples | Distinct paths | Distinct filenames |
|---|---|---|---|---|
| `Reports:VicGas` | CURRENT | 91 | 1 | 91 |
| `Reports:STTM` | CURRENT | 94 | multi | multi |
| `Reports:GBB` | CURRENT | 85 | 4 | multi |
| `Reports:FPPDAILY` | ARCHIVE | 3 | 1 | 3 |
| `Reports:FPPDAILY` | CURRENT | 3 | 1 | 3 |
| `Reports:ROOFTOP_PV/ACTUAL` | child | ≥2 | 1 | ≥2 (measurement + satellite families) |

Reproducer:

```python
import csv
from collections import defaultdict
rows = list(csv.DictReader(open("reference/URL-CONVENTIONS.csv")))
by_key = defaultdict(set)
for r in rows:
    key = (r["repo"], r["retention_tier"], r["intra_repo_id"])
    by_key[key].add((r["path_template"], r.get("filename_template", "")))
multi = {k: v for k, v in by_key.items() if len(v) > 1}
print(len(multi), sum(len(v) for v in multi.values()) - len(multi))  # 67 1166
```

## Codex structural findings (verbatim)

- **Shape 2c (sub-dataset key promotion) only handles subdirectories.** The overwrite at `scripts/extract_patterns.py:896` also loses multiple filename families in the same directory because upstream aggregation preserves `(path_template, skeleton)` at `scripts/extract_patterns.py:469`.
- **Keeping `$defs.Tier` unchanged is the central flaw.** A single tier has one `path_template` and one `filename_template`; the data has many valid templates per logical (dataset, tier).
- **`write_json()` detection logic for "parent with only subdirectory children" cannot work from current inputs.** Empty parent listings are discarded at `scripts/extract_patterns.py:499`. `write_json()` receives no "parent path has no data files" evidence.
- **"Did you mean" on parent keys is false as stated.** `resolve("Reports:GSH")` finds an existing record and raises `UnresolvableDatasetError` at `src/nem_catalog/catalog.py:100`. The `difflib` suggestion only runs for unknown keys at `catalog.py:215`.
- **DUPLICATE class-(b) skip reverses a pinned regression test.** `tests/test_extract_patterns_json.py:340` pins class-(b) non-LEGACY DUPLICATE rows as KEPT.
- **Class-(b) heuristic is brittle.** "Older than parent" describes legitimate stragglers/archives. "Fewer files than parent" is not semantic evidence. Will drift with crawl date.
- **GBB is not solved by path-only split.** `Reports:GBB` has 85 CURRENT rows across root, `DUPLICATE`, `ForecastUtilisation`, and `GBB_PIPELINE_CONNECTION_FLOW`. Even after filtering DUPLICATE rows, root GBB still has dozens of same-path filename families.
- **`_files/` directories are not all assets.** Some contain `.htm` report fragments. Blanket skip is a product decision, not obvious walker garbage.
- **Schema-key "pattern extension" is imaginary.** `dataset_keys` and `raw_keys` items are `"type": "string"` in `schemas/catalog.schema.json:65`; `datasets` has unconstrained `additionalProperties`. No pattern exists to extend.
- **Minor-version framing understates the change.** Consumers may treat `intra_repo_id` as a single Reports stream segment; promoting `Reports:GSH/GSH_Participants` changes that field's meaning.
- **Freshness policy coverage drops.** Promoted subkeys' `path_template`s are not enumerated in `patterns/curated/freshness-policy.yaml`; they classify as `unclassified`.
- **Success criteria weak.** "14 parents exact N-counts" passes while same-directory filename collisions remain broken. Stronger invariant needed: every extractor CSV row must map to a distinct emitted representation or be explicitly filtered with a reason.
