# TODOS — nem-catalog

Active scope only. Aspirational features live in `/ROADMAP.md`.

## Scope discipline — lesson from v0.1.1 + v0.1.2

v0.1.1 was tagged a patch (`.1`) but actually shipped a new freshness-policy feature layer. That expanded surface then had bugs (the DUPLICATE regression) which forced v0.1.2 to patch the patch. **Patch-on-patch spirals waste budget.** Going forward:

- **`.x.x.PATCH`** = bug fix only. No new feature surface. Single-concern.
- **`.x.MINOR.x`** = coherent feature release. Batched, reviewed, numbered honestly.
- **Features dressed as patches** = forbidden. If it adds capability, it's a minor, even if small.

Items below follow this rule.

---

## v0.1.2 — DUPLICATE bug fix (patch, narrow)

Single concern: the DUPLICATE-filter regression that broke 17 market-report datasets' `path_template`. No other items ride in this release.

### v0.1.2-T0. Author a fresh PR-1 plan

- **What:** Write `.plans/v0.1.2-pr1-duplicate-filter.md` (the prior plan was deleted as superseded). Anchor to the 3-class model in `reference/NEMWEB-STRUCTURE.md §2.1.1` and the decisions recorded in v0.1.2-T1 below.
- **Why:** The old plan proposed a binary `/DUPLICATE/` filter — the same shape that shipped as PR #9 and was closed for losing 640 real files. A fresh plan prevents a third recurrence.
- **When:** First task in v0.1.2.

### v0.1.2-T1. Rewrite DUPLICATE filter using the 3-class semantic model

- **What:** Classify each file by filename rather than parent dir. Skip only listings where every file matches `_LEGACY.zip` under `/DUPLICATE/`. Per `reference/NEMWEB-STRUCTURE.md §2.1.1`:
  | Class | Filter action | path_template |
  |---|---|---|
  | (a) `_LEGACY.zip` placeholders (12 dataset dirs) | **skip** | parent path (real data lives there) |
  | (b) multi-file non-LEGACY stragglers (5 subtrees, 23 files) | **keep** | actual path including `/DUPLICATE/` |
  | (c) GBB rolling timestamped archive (617 files) | **keep** | actual path including `/DUPLICATE/` |
- **Fix sketch:** in `scripts/extract_patterns.py:477` mirror-walk loop, after `parse_listing()`, skip when `"/DUPLICATE/" in parent_path and all(f.endswith("_LEGACY.zip") for f in files)`.
- **Regression test (required):** `tests/test_extract_patterns_json.py::test_main_handles_all_duplicate_classes` with three synthetic-mirror fixtures exercising class-(a) skip, class-(b) keep, class-(c) keep. Class-(c) assertion pins the PR #9 regression (assert GBB files remain indexed).
- **Observability:** log `Skipped N _LEGACY files under /DUPLICATE/` after the walk.
- **Maintenance note:** code comment cites `reference/NEMWEB-STRUCTURE.md §2.1.1` as authority for the `_LEGACY`-suffix convention.
- **Side effects to verify:** 12 class-(a) datasets' `path_template` now resolves to parent. Class-(b) and class-(c) entries remain in catalog with their `/DUPLICATE/`-including paths. Re-run extractor against real mirror; confirm observability log count + GBB stays visible.
- **Source:** Issue #5 root-cause 2026-04-20; `reference/NEMWEB-STRUCTURE.md §2.1.1` (commit `abb29d2`); CEO review decisions captured 2026-04-20 (commit `c41be25`).

### v0.1.2 acceptance gate

- First observed clean `policy-audit.yml` run (natural fire ~2026-05-04, 12 days post-v0.1.1 ship).

**NOT in v0.1.2:** `Policy.load` version guard, argv bounds check, unused-output cleanup, `gh release create` step, additional test coverage. All legitimate but each adds surface area and belongs in v0.2 hygiene bundle.

---

## v0.2 — coherent next release (planned, not yet scoped)

v0.2 addresses v0.1.0's explicit known-issues list. Keep the scope small and focused. Pick 2–4 items from the candidate pool below; don't ship all of them.

### v0.2 candidate — `list_urls()` for non-temporal keys

- **What:** New SDK method that enumerates candidate URLs for dataset keys containing `{aemo_id}`, `{nn}`, `{d2}` (file-sequence placeholders). Current `resolve()` raises `NonResolvableTemplateError` on ~84% of keys.
- **Why:** v0.1.0's CHANGELOG explicitly flagged this as the v0.2 focus: _"v0.2 will add `list_urls()` to handle these."_ Closes the biggest known usability gap.
- **v0.1.0 caveat this addresses:** "Resolve coverage: ~16% of 362 keys resolve cleanly."

### v0.2 candidate — observed-range retention

- **What:** Replace `retention_hint_unverified_days: int` with `retention_hint_observed_days: {min, max, confidence}`. Derive the range and confidence from accumulated weekly-crawl observations.
- **Why:** v0.1.0's single-snapshot value is fake precision. v0.1.0 TODOS.md queued this exact item.
- **v0.1.0 caveat this addresses:** "`retention_hint_unverified_days` is derived from a single 2026-04-18 mirror snapshot. v0.2 replaces with confidence range."
- **Depends on:** Weekly workflow reliably green for ≥6 weeks.

### v0.2 candidate — MMSDM schema embedding (reframes v0.1.0's schema-pointer item)

- **What:** Embed per-table-per-version column metadata in MMSDM dataset records. Source: `reference/MMSDM-DDL-COLUMNS.csv` (33,162 rows, v5.2-v5.6). Schema-level detail beyond just a portal-root URL.
- **Why:** v0.1.0 imagined anchor URLs into AEMO's HTML portal. Today's recon produced the actual column data — strictly better. Users querying an MMSDM table get the schema directly, no URL chase.
- **v0.1.0 caveat this addresses:** "Schema source for MMSDM tables is the portal root only. Per-table anchors deferred to v0.2."
- **Scope decision:** pick ONE of inline-in-catalog vs sidecar-JSON-file per record. 33K rows is non-trivial catalog size.

---

## v0.1.x — tactical hygiene (bundle for a future minor, not ship as patches)

These accumulated from v0.1.1 plan review + post-PR code review + monthly audit. Individually small (1-15 lines each). Bundling them into a future minor release (v0.2 or v0.3) is cleaner than shipping a patch parade. Do NOT ship any of these as a v0.1.x patch — that repeats the feature-as-patch mistake.

### Policy + loader

- **POL-1.** `Policy.load` version compatibility guard. One-line add: raise `PolicyLoadError` on `version != 1`. (was v0.1.1 T2-I2)
- **POL-2.** `append_only` / `parent_index` coverage in `audit_policy.run_audit`. Currently only `unclassified` / `static` / `rolling` surface findings. (was T10-I1)
- **POL-3.** `_load_fresh` root-level `index.html` produces `/./` URL instead of `/`. One-line fix. (was T10-M1)

### Extractor + CLI

- **EXT-1.** `--policy` / `--threads` argv bounds check. (was v0.1.1 T4-I1)
- **EXT-2.** `--policy` documented in module docstring. (was T4-I3)
- **EXT-3.** Walker closure emits `fetch_noop` vs `fetch` distinction. Observability debt, not correctness. (was T4-I2)
- **EXT-4.** `save_listing` `idx.read_bytes()` guarded against `OSError`. Defensive hygiene. (was T3-I2)

### Tests

- **TEST-1.** Rename `test_template_shift_raises_when_new_empty` → `test_template_shift_triggers_at_50pct_via_lowercase_href`. Add a truly-zero-HREF companion test. (was T3-I1)
- **TEST-2.** `main()` failure-mode red tests (exit 2 on `PolicyLoadError` and `HREFExtractionShiftError`). (was D4)
- **TEST-3.** `format_report` output coverage — empty findings + multi-kind findings. (was T10-M2)

### Workflows + release

- **WF-1.** Drop unused `crawl_attempted.outputs.ts` from `weekly-refresh.yml`. (was T9-M3)
- **WF-2.** `release.yml` adds `gh release create` step so the GitHub Releases page auto-populates. (was T-release-M1)

### Catalog schema

- **CAT-1.** `catalog.policy_version` field at catalog root if any consumer asks. Currently derivable from `catalog_version` + git history. (was D1)

---

## v0.1.x design work (not patch-shippable, needs design pass)

These are real items but each needs a design decision before implementation. Not shippable in a patch. Graduate into a minor release scope with a short design note first.

### Classify ~57 unclassified CURRENT paths

- **What:** `patterns/curated/freshness-policy.yaml` enumerates 29 of ~92 CURRENT dataset paths; ~57 fall through to `unclassified` via the no-catchall design.
- **New path:** `reference/aemo-catalog/manifests/` ships 97 AEMO-authored dataset manifests (today's recon). Cross-referencing those against the 57 unclassified paths is a fast path to authoritative classification — no 4-week observation window required.
- **Why design work:** 57 paths × classification-convention design × tooling work is non-trivial. Separate spike, not inline with other work.
- **When:** v0.2 or v0.3.
- **Source:** Issue #5 tertiary finding (was T1-I2).

### `/Reports/ARCHIVE/**` retention classification refinement

- **What:** Current policy classifies ARCHIVE as `append_only`. Reality is ~1-year rolling window. Either introduce a new class (`bounded_rolling`) or document `append_only` with a retention caveat.
- **Why design work:** Needs per-stream retention measurement across ~40 ARCHIVE streams.
- **When:** v0.2 or v0.3.
- **Source:** v0.1.1 plan review (was T1-I1).

### Deep-subdir dataset schema (T5T6-I3)

- **What:** 9 datasets (ROOFTOP_PV, Operational_Demand, STTM, GSH, ECGS, GBB, MMSDataModelReport, Operational_Demand_Less_SNSG) have genuine sub-partitions under CURRENT. Current sort-order-wins merge picks arbitrarily. Options: separate datasets per partition, parent-only path_template, or a new `partitions[]` schema field.
- **Why design work:** Schema-touching. Affects every downstream consumer.
- **When:** v0.3+ after v0.2 ships and adoption signals come in.
- **Source:** Issue #5 secondary finding 2026-04-20.

---

## Reference docs — recon follow-ups

Continue today's ground-truth pass on the AEMO documentation layer. These are NOT catalog features — they expand the `reference/` docs that v0.2 schema-embedding will draw from. Graduate into a version scope when their outputs feed a shippable feature.

### REF-T3. Reconstruct v5.2+ Table↔File↔Report mapping

- **What:** AEMO published `Table_File_Report_Relationships.xlsx` for v4.26–v5.1 and stopped. Reconstruct for v5.2–v5.6 using DDL + Upgrade Report deltas + v5.1 baseline.
- **Output:** `reference/MMSDM-TABLE-FILE-REPORT-MAPPING-v5.2-plus.csv` with confidence column (direct-from-DDL / inferred-from-rename / inferred-from-column-shape).
- **Source:** 2026-04-20 recon session, Task 3 carried over.

### REF-T4. Pre-2015 MMSDM mirror walk extension

- **What:** Walk 66 pre-2015 months (2009-07 → 2014-12) against post-case-sensitivity-enforcement AEMO.
- **Timing:** After 2026-04-21 case-sensitivity enforcement goes live. Not before.
- **Source:** 2026-04-20 recon session, Task 4 deferred.

---

## Closed (historical record)

Resolved items. Kept for "why is X the way it is" archaeology.

### v0.1.1 cycle

- **D3** [2026-04-20] Force-refetch mirror noise absorbed by content-aware `save_listing()`. PR #7 validated end-to-end.
- **T2-I1** [2026-04-20, commit `21fce89`] `/Data_Archive/` reclassified `static` → `parent_index`.
- **T9-M1** [2026-04-20, commit `1fc5151`] `set -eo pipefail` added to crawl step shell override. Fixed Monday 2026-04-20 silent canary crash. Lesson: gstack adversarial review C1 finding was closed as false positive based on memory of GHA defaults, not the actual `shell:` override — "reviewer shared sources with author" miss per ground-truth discipline §4.
- **T9-M2** [2026-04-20] All workflow labels created on the repo.

### v0.1.2 cycle

- **T5T6-I1** [2026-04-20, commit `491bce3`] `from scripts.policy import Policy` import promoted to module top-level + sys.path bootstrap for direct-script invocation. Root cause of Monday 2026-04-20 03:00 UTC silent canary crash.
- **Superseded PR-1 plan** [2026-04-20, commit `7611928`] Original `.plans/2026-04-20-v0.1.2-pr1-duplicate-filter.md` deleted because it proposed a binary `/DUPLICATE/` filter — the same shape that shipped as PR #9 (closed for losing 640 files). See v0.1.2-T0 for the fresh plan anchored to `NEMWEB-STRUCTURE.md §2.1.1`.

### Notes (not deferrals)

- **T10-N1** Ruff auto-removed unused `import json` and `AuditFinding` imports in tests. Genuinely unused.
- **T10-N2** Unicode minus `−` replaced with ASCII `-` in `format_report`.
