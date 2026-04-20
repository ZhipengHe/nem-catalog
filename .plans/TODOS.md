# TODOS — nem-catalog

Parking lot for items deferred past v0.1 or surfaced during design / engineering review. Each entry has: what, why, when, depends-on. Closed items live in §Closed at the bottom for historical record.

---

## v0.1.2 — DUPLICATE-fix small patch (next release)

The 2026-04-20 morning PR #9 incident plus its post-mortem recon (committed `abb29d2` / `96e7d47` / `05db3ea`) made one thing obvious: the catalog has a real DUPLICATE-handling bug AND a few small tactical fixes worth bundling. v0.1.2 keeps to that scope — bigger ideas surfaced by the recon roll forward to v0.1.3+ / v0.2.

**Acceptance gate:** D2 — first observed clean `policy-audit.yml` run (natural fire ~2026-05-04, 12 calendar days post-v0.1.1 ship).

### v0.1.2-T0. Author fresh PR-1 plan

- **What:** Write `.plans/v0.1.2-pr1-duplicate-filter.md` (the prior one was deleted in commit `7611928` as superseded). Anchor the plan to `reference/NEMWEB-STRUCTURE.md §2.1.1` and the decisions recorded in v0.1.2-T1 below. Follow the superpowers `writing-plans` skill; quote load-bearing decisions inline (the §2.1.1 3-class table; the path_template + test-coverage decisions).
- **Why:** The old plan's binary-filter approach would reintroduce the PR #9 regression. A fresh plan prevents anyone picking up this work from re-shipping the same bug for a third time.
- **When:** First task in v0.1.2.
- **Source:** /gstack-plan-ceo-review 2026-04-20 (recurring-problem architectural smell).

### v0.1.2-T1. Rewrite DUPLICATE filter using the 3-class semantic model

- **What:** Replace the morning's binary "skip everything under `/DUPLICATE/`" filter (PR #9, closed) with the principled 3-class model from `reference/NEMWEB-STRUCTURE.md §2.1.1`:
  | Class | Detect by | Action | path_template |
  |---|---|---|---|
  | Single-file `_LEGACY` placeholders (12 dataset dirs) | filename matches `*_LEGACY.zip` AND parent contains `/DUPLICATE/` | **skip** — AEMO dedup artifact | (N/A, skipped) |
  | Multi-file non-LEGACY stragglers (5 subtrees: MCCDispatch, Next_Day_Intermittent_DS, Next_Day_PreDispatch, PredispatchIS_Reports, Trading_Cumulative_Price) | parent contains `/DUPLICATE/` AND no `_LEGACY` filename suffix | **keep** — real data | **points at the actual data path including `/DUPLICATE/`** (catalog tells users where bytes actually are; parent dir does not contain the files) |
  | GBB rolling timestamped archive (617 files) | parent path matches `Gas/GBB/.../DUPLICATE/` | **keep** — real data | **points at the actual data path including `/DUPLICATE/`** |
- **Why:** The old T5T6-I2 fix as written (`if "/DUPLICATE/" in parent_path: continue`) is exactly the unconditional filter that broke as PR #9 — it would lose 622 real files (5 stragglers + 617 GBB). Filename-discriminator approach is the safe form.
- **Fix sketch:** in `scripts/extract_patterns.py:477` (the `for idx in sorted(MIRROR.rglob("index.html"))` loop), classify each file by filename rather than parent dir. Cross-reference `reference/NEMWEB-STRUCTURE.md §2.1.1` table for the full enumeration. Filter acts only on class-(a) `_LEGACY`-suffixed filenames under `/DUPLICATE/`; leaves class-(b) and class-(c) entries untouched so their real data remains indexed at their actual path.
- **Regression test (required):** `tests/test_extract_patterns_json.py::test_main_handles_all_duplicate_classes` exercising three synthetic-mirror fixtures:
  1. **class-a skip:** `Dispatch_Reports` with a single `PUBLIC_*_LEGACY.zip` under `/DUPLICATE/` — assert the dataset's `path_template` resolves to the parent `/Reports/CURRENT/Dispatch_Reports/` (NOT the DUPLICATE subpath), classifies as `rolling` under curated policy.
  2. **class-b keep:** `MCCDispatch` (or any straggler) with multi-file non-LEGACY filenames under `/DUPLICATE/` — assert both the dataset is present AND its `path_template` includes `/DUPLICATE/` (real data lives there).
  3. **class-c keep:** GBB with 5+ timestamped files under `Gas/GBB/{stream}/DUPLICATE/` — assert all files visible in the catalog; file count must match fixture. This is the PR #9 regression pin.
  End-to-end diff against the real 2863-listing mirror is retained as supplementary sanity check, not as the primary fence.
- **Observability:** after the mirror walk, log `Skipped N _LEGACY files under /DUPLICATE/` so filter behaviour is visible from run logs alone (no catalog-diff required to confirm correct operation).
- **Maintenance note:** the filter assumes AEMO's `_LEGACY.zip` naming convention for dedup placeholders. If AEMO ever ships a dedup placeholder WITHOUT the suffix, the filter misses it and the PR #9 regression pattern silently returns. The regression test's class-a fixture pins the convention; cite `reference/NEMWEB-STRUCTURE.md §2.1.1` in the code comment next to the filter as the authority.
- **Source:** Issue #5 root-cause investigation 2026-04-20 (primary); confirmed by today's recon (`reference/NEMWEB-STRUCTURE.md §2.1.1`); path_template + test-coverage decisions captured via /gstack-plan-ceo-review 2026-04-20.

### v0.1.2-T2. `Policy.load` version compatibility guard

- **What:** `Policy.load` parses and stores `version` but never validates it. A future `version: 2` policy with different schema loads silently.
- **Fix:** `if int(raw.get("version", 0)) != 1: raise PolicyLoadError("unsupported policy version ...")` after the `rules` key check.
- **Source:** v0.1.1 plan review (T2-I2).

### v0.1.2-T3. `--policy` / `--threads` argv bounds check

- **What:** `argv[i + 1]` accessed without bounds check when these flags are the final argv element. CI passes fixed strings; developer-only crash.
- **Fix:**
  ```python
  elif a == "--policy":
      if i + 1 >= len(argv):
          raise SystemExit("--policy requires a path argument")
      policy_path = argv[i + 1]
      i += 1
  ```
  Same guard for `--threads`.
- **Source:** v0.1.1 plan review (T4-I1).

### v0.1.2-T4. Drop unused `crawl_attempted.outputs.ts`

- **What:** `weekly-refresh.yml` line 49 writes `ts=$TS` to `$GITHUB_OUTPUT`; no downstream step references it. Consumed path is the env var `LAST_CRAWL_ATTEMPTED_AT`.
- **Fix:** Remove the unused `echo "ts=$TS" >> $GITHUB_OUTPUT` line.
- **Source:** v0.1.1 plan review (T9-M3).

### v0.1.2-T5. `release.yml` creates GitHub Release page

- **What:** v0.1.0 + v0.1.1 needed manual `gh release create vX.Y.Z --notes-from-tag` post-workflow; PyPI publishes but the GitHub Release tab is empty until done by hand.
- **Fix:** Add step after `Publish to PyPI` and before `Open issue on failure`:
  ```yaml
  - name: Create GitHub Release
    env:
      GH_TOKEN: ${{ github.token }}
    run: |
      gh release create "${{ github.ref_name }}" \
        --title "${{ github.ref_name }}" \
        --notes-from-tag \
        --verify-tag
  ```
- **When:** Land before pushing the v0.1.2 tag so the workflow self-creates the Release page.
- **Source:** v0.1.1 release postmortem (T-release-M1).

---

## Reference docs — recon follow-ups (continues today's ground-truth pass)

These extend the recon foundation built today (`reference/NEMWEB-STRUCTURE.md`, `reference/MMSDM-TABLE-LIFECYCLE.{md,csv}`, `reference/MMSDM-DDL-COLUMNS.csv`, etc.). They are NOT catalog-feature work — they expand the reference/ ground-truth layer that catalog features will later draw from. Tracked here so they're not lost; nominally feed v0.1.3+ and v0.2.

### REF-T3. Reconstruct v5.2+ Table↔File↔Report mapping

- **What:** AEMO published `Table_File_Report_Relationships.xlsx` for v4.26 → v5.1 (7 versions, captured as `reference/aemo-mmsdm-docs/v{X.Y}/table-file-report-mapping.csv`) and stopped. Reconstruct the equivalent mapping for v5.2 → v5.6 (5 versions) using:
  - v5.1 baseline mapping (carry-forward).
  - Per-version DDL deltas from `reference/MMSDM-DDL-COLUMNS.csv` (33,162 rows).
  - Per-version Upgrade Report change-lists from `reference/MMSDM-UPGRADE-TABLES.csv` (354 rows, indexed by package).
  - For new tables added in each version: column-schema heuristics (e.g., a new table with `SETTLEMENTDATE + DUID + BIDTYPE` columns belongs to the BID file group).
- **Why:** Cross-boundary `MMSDM ↔ Reports` identity (per `NEMWEB-STRUCTURE.md §4`) is currently broken at v5.2+ — consumers parsing 2024-08+ filenames have no canonical mapping back to AEMO's logical Report category. Without this, several catalog v0.2 features (rename metadata, schema attachment, per-table provenance links) can't fully cite Reports/MMSDM unification.
- **Output:** `reference/MMSDM-TABLE-FILE-REPORT-MAPPING-v5.2-plus.csv` in same shape as AEMO's xlsx (`table_name, file_name, report_id, report_name, transaction_type, version`). Include a `confidence` column per row: `direct-from-DDL` / `inferred-from-rename` / `inferred-from-column-shape` / `unknown`.
- **When:** v0.1.3 reference-doc pass. Already in-flight (Task 3 of 2026-04-20 session).
- **Depends on:** Today's MMSDM-DDL-COLUMNS + MMSDM-UPGRADE-TABLES outputs (committed `96e7d47`).
- **Source:** 2026-04-20 recon session, deferred from same-day Task 1+2 batch.

### REF-T4. Pre-2015 MMSDM mirror walk extension

- **What:** AEMO's catalog (`reference/aemo-catalog/datasets/mms-data-model-definition.yaml`) claims MMSDM data exists 2009-07 onwards (201 months); current mirror walk only covers 2015-01 onwards (135 months). Year-level dirs exist on the mirror at `https://nemweb.com.au/Data_Archive/Wholesale_Electricity/MMSDM/{2009..2014}/` but month-level listings have not been walked. Walk the 66 missing months (2009-07 → 2014-12), record HTTP status + href set per dir.
- **Why:** Tables present only before 2015-01 are invisible to current `MMSDM-TABLE-LIFECYCLE.csv`. Several rename hypotheses in §6 reference pre-2015 predecessors that we currently can't verify. Pre-2015 coverage closes this gap.
- **Critical timing:** **Must run after AEMO's 2026-04-21 case-sensitivity enforcement goes live.** Walking today (2026-04-20) risks recording URLs that work today and 404 tomorrow (same gotcha as the 6 already-documented Reports/ARCHIVE URLs in `NEMWEB-STRUCTURE.md §6`). Single clean walk against post-enforcement state = cleaner ground truth.
- **Output:** Extend `reference/MMSDM-TABLE-LIFECYCLE.csv` with rows for any pre-2015-only tables. Update `NEMWEB-STRUCTURE.md §2.2` and `MMSDM-TABLE-LIFECYCLE.md §7.2` with findings (close the "Pre-2015 coverage gap" open question).
- **When:** v0.1.3 reference-doc pass, after 2026-04-21. Already deferred (Task 4 of 2026-04-20 session).
- **Depends on:** AEMO case-sensitivity enforcement going live (external timing).
- **Source:** 2026-04-20 recon session.

---

## v0.1.x — deferred for later patches

Items that don't fit the v0.1.2 small-patch scope but should land before v0.2. Promote into a v0.1.3 / v0.1.4 patch as scope solidifies.

### v0.1.x design — `/Reports/ARCHIVE/**` retention classification

- **What:** Current policy classifies `/Reports/ARCHIVE/**` as `append_only`, implying pure growth. Reality is closer to "long-rolling" (~365-day window) — items appended at head AND drop off tail.
- **Why deferred from v0.1.2:** Requires per-stream empirical retention measurement; ~40 ARCHIVE streams to measure. Out of scope for a small patch.
- **Investigation scope:**
  1. For each ARCHIVE stream: measure oldest vs newest listing date; record observed retention window.
  2. Decide: introduce new class (`rolling_long` / `retention_window` / `bounded_rolling`) OR keep `append_only` with documented caveat.
  3. If new class: update `Policy.VALID_CLASSES`, `audit_policy.py` finding logic (currently doesn't cover `append_only` at all — see v0.1.x-T10I1 below), JSON Schema enum.
  4. Update `freshness-policy.yaml` for `/Reports/ARCHIVE/**`.
  5. Document `retention_window_days` as a new dataset-level field.
- **When:** v0.1.3 or v0.1.4 policy-accuracy pass.
- **Source:** v0.1.1 plan review (T1-I1).

### v0.1.x design — Classify the ~57 unclassified CURRENT paths

- **What:** `freshness-policy.yaml` enumerates 29 of ~92 CURRENT dataset paths. After v0.1.2 lands, ~57 remain unclassified by design (catchall comment lines 113-116).
- **NEW path forward (today's recon enables this):** `reference/aemo-catalog/manifests/` ships 97 AEMO-authored dataset manifests. Cross-referencing these against the 57 unclassified paths gives an authoritative classification source TODAY — no need to wait 4 weekly cron runs for observation data. Two-source approach:
  - **Primary:** AEMO catalog manifests (immediate, authoritative).
  - **Secondary:** Observed churn from weekly cron (validation; promotes `confidence` field).
- **Why deferred from v0.1.2:** Still substantial design work — 57 paths × manifest cross-reference + classification convention design + per-class fixture tests.
- **Scope:**
  1. Build `scripts/match_unclassified_against_aemo_catalog.py` — cross-reference unclassified paths in `freshness-policy.yaml` against AEMO catalog manifest entries.
  2. Assign each matched path a class based on AEMO's documented cadence + retention.
  3. For unmatched paths (AEMO catalog doesn't cover): keep in catchall, surface via `policy-audit.yml`.
  4. Batch-add rules to `freshness-policy.yaml` grouped by retention bucket.
- **When:** v0.1.3.
- **Depends on:** v0.1.2-T1 (DUPLICATE filter) landing first so the 17 market reports get correct path_template.
- **Source:** Issue #5 root-cause investigation 2026-04-20 + 2026-04-20 recon session (AEMO catalog availability).

### v0.1.x design — `extract_patterns.py` deep-subdir handling (T5T6-I3)

- **What:** After v0.1.2-T1 lands, 9 datasets still misrecord their CURRENT `path_template` as a sub-partition: `Reports:ROOFTOP_PV` (FORECAST_AREA / ACTUAL / etc.), `Reports:Operational_Demand` (FORECAST_HH_AREA / ...), `Reports:STTM` (MOS%20Estimates / ...), plus `GSH`, `ECGS`, `GBB`, `MMSDataModelReport`, `Operational_Demand_Less_SNSG`. Same overwrite mechanic, but the winning path is genuine data not a dedup artifact.
- **Why this is a design call:** Sub-partitions are real data partitions. Losing them by picking the parent drops information; keeping the last-sorted is arbitrary. Options:
  - (a) Record each sub-partition as its own dataset (`Reports:ROOFTOP_PV.ACTUAL`, …).
  - (b) Record only the parent `path_template`; lose per-sub-partition `filename_regex` / `observed_range` granularity.
  - (c) Record parent as canonical; enumerate sub-partitions in a new `partitions[]` field per tier.
  - (d) Prefer shortest `path_template` when merging into `tiers[X]` — partial fix.
- **Why deferred:** Schema-touching design. Needs downstream-consumer input on how sub-partitioned data should be addressed.
- **When:** v0.1.3 design spike → implementation in v0.1.4 or v0.2.
- **Source:** Issue #5 root-cause investigation 2026-04-20, secondary finding (T5T6-I3).

### v0.1.x tactical bundle — minor fixes worth batching together

Single-PR-able tactical work, no individual blocker. Land as a single v0.1.3 hygiene PR.

- **D1.** `catalog.policy_version` field at catalog root if any consumer surfaces. Currently derivable from `catalog_version` + git history of `freshness-policy.yaml`.
- **D4.** `main()` failure-mode red test — explicit unit test that `main()` returns exit 2 on `PolicyLoadError` and `HREFExtractionShiftError`. ~5 min, both paths reviewed and correct by inspection.
- **T3-I1.** Rename `test_template_shift_raises_when_new_empty` to `test_template_shift_triggers_at_50pct_via_lowercase_href` (lowercase HREF actually matches `re.IGNORECASE`, hits 50% threshold not zero-extraction). Add `test_template_shift_raises_when_new_truly_empty` using markup with no HREFs.
- **T3-I2.** `save_listing` `idx.read_bytes()` `OSError` guard (3 lines, treats unreadable cache as cache miss).
- **T4-I2.** Walker can emit `"fetch_noop"` (mtime capture inside walker closure; per-wave counter for `fetch_noop`).
- **T4-I3.** `nemweb_download.py` module docstring lists `--policy` with usage example.
- **T10-I1.** Extend `audit_policy.py run_audit` with `reclassify_down` arm for `append_only` with zero churn (interim minimum: add fall-through comment marking the gap).
- **T10-M1.** `_load_fresh` `/./` URL bug at root-level `index.html` — change guard to `if rel != "." else "/"`.
- **T10-M2.** `format_report` test coverage — 1 test for empty findings (clean-audit string), 1 test for multi-kind findings (all 3 section headers).

---

## v0.2 — catalog data refinements

Today's recon unlocked several catalog value-adds that move v0.2 from "format polish" to "richer data layer." Existing v0.2 items reframed; new items added.

### v0.2-NEW. AEMO Visibility annotation per catalog entry

- **What:** Surface AEMO's per-table Visibility classification (4-value taxonomy from upgrade reports v5.4+: `Public` / `Private` / `Private, Public Next-Day` / `Private & Public`) as a dataset-level field in catalog records. Source: `reference/MMSDM-UPGRADE-TABLES.csv` for v5.4+, `PUBLIC_PDR_CONFIG_*_FULL.CSV` (in `reference/aemo-mmsdm-docs/v{X.Y}/MMS_Data_Model_pdrLoader_Configuration_*.zip`) for older versions.
- **Why:** Operationalizes "is this data public or do I need participant access?" — currently a hand-wave / read-AEMO-PDFs question for users. Direct user value for academic, BESS, market-participant downstream consumers.
- **Considerations:**
  - Visibility is a per-table (MMSDM) attribute, not per-NEMWEB-file. Need a join model.
  - PDR_CONFIG CSV format differs across versions; old form is nested `PUBLIC_PDR_CONFIG_*_FULL.zip` inside the pdrLoader zip. Need a small loader.
  - Visibility can change across versions (rare but possible). Use the latest version's tag as canonical; flag if a table changed Visibility category.
- **When:** v0.2.
- **Depends on:** REF-T3 (Table↔File↔Report mapping for v5.2+) for joining Visibility (per-table) to NEMWEB files (per-Report).
- **Source:** 2026-04-20 recon session.

### v0.2-NEW. Rename predecessor/successor metadata

- **What:** For each table that had a verified rename event (per `reference/MMSDM-RENAMES-VERIFICATION.md`), surface bidirectional `succeeded_by` / `successor_of` fields at the dataset level. Cover all 3 verdict classes:
  - **CONFIRMED** (1: BIDOFFERPERIOD ← BIDPEROFFER1+2): hard-deprecated alias, both names map to canonical successor.
  - **DATA-FLOW-REPLACEMENT** (7): both names remain valid identifiers; consumer treats as paired streams with switch-month annotation.
  - **PRE-DDL-CAPTURED** (4): predecessor → successor strict mapping (predecessor is gone from current schema).
- **Why:** Consumers querying historical NEMWEB filenames currently can't resolve `BIDPEROFFER_D` to `BIDOFFERPERIOD`, `MTPASA_CONSTRAINTSOLUTION` to `MTPASA_CONSTRAINTRESULT + MTPASA_CONSTRAINTSUMMARY`, `TRADINGLOAD` to its 5MS-era successor `DISPATCHLOAD`, etc. Catalog should bridge.
- **When:** v0.2.
- **Depends on:** Today's `MMSDM-RENAMES-VERIFICATION.md` (committed `96e7d47`) + REF-T3 for Reports-side rename impact.
- **Source:** 2026-04-20 recon session.

### v0.2-REFRAMED. MMSDM column-level schema in catalog records

(Replaces the older "Per-table MMSDM schema pointers" item — that proposed anchor-URLs into AEMO's portal; today's recon shipped the actual column data, so we no longer need URL-stability HEAD checks.)

- **What:** Fold `reference/MMSDM-DDL-COLUMNS.csv` (33,162 rows) into MMSDM dataset records as a structured per-version column inventory: `columns: [{name, type, nullable, is_pk, first_version, last_version}]`.
- **Why:** Higher-fidelity "what's in this dataset" answer than today's `schema_source: <portal_url>`. Removes the need for downstream tools to re-parse DDL.
- **Considerations:**
  - 33K rows × catalog overhead. Decide: inline per-record vs separate `mmsdm-columns.json` sidecar referenced by URL.
  - Column lifecycle (added in v5.3, removed in v5.5) needs per-version tracking — already structured in source CSV.
- **When:** v0.2.
- **Depends on:** REF-T3 (mapping reconstruction) for tying columns back to Reports-side files.
- **Source:** 2026-04-20 recon session, reframes pre-v0.1 idea.

### v0.2-NEW. AEMO catalog cross-reference for completeness validation

- **What:** Use `reference/aemo-catalog/datasets/mms-data-model-definition.yaml` (AEMO's own master catalog, 97 manifests) as a periodic completeness check: every dataset AEMO claims to publish should appear in `nem-catalog`. Surface discrepancies in `policy-audit.yml`.
- **Why:** AEMO's catalog is internally inconsistent (`monthList` claims 201 months, manifests cover 135) but it's still the most authoritative completeness reference we have. Any dataset listed there but absent from our catalog is either (a) coverage gap on our side or (b) AEMO catalog drift — both worth flagging.
- **When:** v0.2.
- **Depends on:** Stable AEMO catalog capture cadence (re-fetch monthly to detect AEMO additions).
- **Source:** 2026-04-20 recon session.

### v0.2-NEW. Per-version MMSDM table timeline as catalog-queryable surface

- **What:** Surface `reference/MMSDM-TABLE-TIMELINE.csv` (447 rows: per-(table, version) action with ADDED / MODIFIED / RENAMED_FROM / RENAMED_TO) as a top-level catalog field or sidecar JSON. Enables queries like "what tables changed between v5.2 and v5.3?", "when was DISPATCHLOAD last modified?", "which tables added in 2024-08?".
- **Why:** No existing public artifact answers these questions structurally — currently requires reading 13 PDFs.
- **When:** v0.2.
- **Depends on:** Schema decision on whether catalog stays per-NEMWEB-file or grows a parallel per-MMSDM-table view.
- **Source:** 2026-04-20 recon session.

### v0.2-EXISTING. Retention hint → observed range with confidence

- **What:** Replace `retention_hint_unverified_days: int` with `retention_hint_observed_days: {min, max, confidence}` object. Confidence derived from number of weekly re-crawls that observed the window.
- **Why:** Single-snapshot retention is fake precision (outside-voice finding #9). After ≥2 additional weekly crawls land, the catalog has enough data to publish an honest range.
- **NEW:** AEMO catalog manifests (today's capture) may also expose retention metadata directly — investigate before designing the observed-range structure. If AEMO publishes retention, prefer that over derived observation.
- **When:** After 4 consecutive green weekly runs + 2 more weeks of observation.
- **Depends on:** Weekly workflow being reliably green for ≥6 weeks.

### v0.2-EXISTING. Schema coverage for Reports streams

- **What:** v0.1 ships Reports records with `schema_source: null`. v0.2 explores schema extraction from sample file parsing (Reports doesn't have AEMO docs for schemas).
- **Why:** Schema is the missing ecosystem piece for Reports; currently every downstream tool reverse-engineers it.
- **NEW context:** Today's REF-T3 (Table↔File↔Report mapping reconstruction) will partially close this — for Reports tables that DO appear in the MMSDM model, the MMSDM column metadata transfers. For Reports tables that don't (e.g. Bidmove_Complete CSV columns), sample parsing is still needed.
- **When:** Post-v0.1, scoped after understanding real consumer demand.
- **Depends on:** v0.1 adoption signals + REF-T3 completion.

---

## Strategic evaluations (v0.2++ / v1.0)

### Alternative distribution: per-language codegen

- **What:** Evaluate generating per-language SDK packages (Python, R, Julia) from the JSON Schema instead of shipping one Python SDK and expecting other languages to roll their own.
- **Why:** Outside-voice finding #17 — a universal JSON catalog does not eliminate tier-routing, view-selection, and fetch-policy logic in consumer languages. Codegen would actually deliver the "language-agnostic" promise.
- **When:** Consider in a v1.0 architecture review after v0.1 has 3+ months of usage data.
- **Depends on:** Tooling choice (e.g., `datamodel-code-generator` for Python, `rquickjson-bindgen` style for others), and willingness to maintain N language ports.

### Crawl budget at scale

- **What:** Revisit `--gaps` vs full-recrawl strategy when the mirror reaches ~5000 listings.
- **Why:** At 1 req/s, full recrawl is ~48 min today, ~96 min at 5000 listings, ~3 hours at 10000. Still under GHA free-tier 6-hour limit, but worth reconsidering parallelization (matrix jobs respecting aggregate 1 req/s) before the limit becomes tight.
- **When:** Trigger: mirror listing count hits 5000 (currently 2863). Roughly 5 years at observed growth.
- **Depends on:** Mirror size monitoring in the weekly workflow.

### AEMO coordination

- **What:** Publish `docs/aemo-coordination.md` with User-Agent contact, GHA IP disclosure, purpose statement, and a request-for-allowlist email template.
- **Why:** Outside-voice finding #18 — AEMO permission tolerance is currently an unstated assumption. **Strengthened by today's recon:** AEMO ships `mms-data-model-definition.yaml` and 97 dataset manifests under a `/datasets/` path that's clearly intended for programmatic consumption. They've published machine-readable metadata for tools like ours; coordination is more "introduce ourselves" than "ask for permission."
- **When:** v0.1 stretch; v0.1.x hard commit if bumped.
- **Depends on:** Nothing.

### v1.0 — catalog as semantic bridge

- **What:** Re-evaluate the project framing once v0.2 ships. Position `nem-catalog` not as "list of NEMWEB files" but as "rigorous bridge between NEMWEB filenames, AEMO MMSDM schema, and AEMO Reports semantic structure — verified against primary source." Today's recon makes this framing defensible; v0.2's deliverables make it shipped.
- **Why:** Differentiates `nem-catalog` from anyone who just runs `wget -r` against nemweb. The differentiator IS the verification + cross-source synthesis layer.
- **When:** v1.0 README / project positioning revision after v0.2 ships and 6 months of usage data exist.
- **Depends on:** v0.2 catalog refinements landing (AEMO Visibility, rename metadata, schema embedding).

---

## Sibling project (tracked here for visibility, not scoped)

### `nem-downloader` sibling repo

- **What:** A separate project that depends on `nem-catalog` (via PyPI or vendoring, decided at the time) to provide the actual byte-downloading + decompression + caching layer users want.
- **Why:** Design premise 6 — nem-catalog is catalog-only; the downloader is user's own future work, first-party dogfooder for P0 success criterion.
- **When:** After v0.1 of nem-catalog ships and stabilizes.
- **Depends on:** nem-catalog v0.1 stable release on PyPI. Single vs two-repo decision deferred to that point per outside-voice finding #14.

---

## Closed (historical record)

Resolved or no-longer-applicable items. Kept here so future archaeology of "why is X the way it is" finds the answer.

### v0.1.1 cycle — pre-ship convergence

- **D3** [2026-04-20] Residual force-refetch mirror noise in `/Reports/ARCHIVE/**` and `/Data_Archive/**`. Content-aware `save_listing()` absorbed the drift as designed. PR #7 (first fully-green weekly-refresh run) committed 123 real HREF-change listings, zero template drift. Mechanism validated end-to-end.
- **T2-I1** [2026-04-20, commit `21fce89`] `/Data_Archive/` classified as `static`, should be `parent_index`. Closed during pre-landing review convergence (codex + gstack both HIGH). Policy catchall changed `/Data_Archive/**` → `/Data_Archive/*/**` and pinned by `test_data_archive_bare_path_is_parent_index_not_static`.
- **T9-M1** [2026-04-20, commit `1fc5151`] Redundant `set -e` in the crawl step's shell block — original premise was wrong. The crawl step declares `shell: /usr/bin/bash -e {0}` (no `pipefail`); Monday 2026-04-20 cron silently swallowed a Python crash through `tee`. Changed to `set -eo pipefail`. Lesson logged: gstack adversarial review C1 finding flagged this and was closed as false positive — textbook "reviewer shared sources with author" miss (ground-truth discipline §4).
- **T9-M2** [2026-04-20] All labels referenced by `weekly-refresh.yml` and `policy-audit.yml` created on the repo: `crawl-failure`, `p0`, `p1`, `policy-audit`, `weekly-refresh`, `chore`, `aemo-coordination`, `robots-halt`, `merge`, `data-catalog`. Verified via `gh label list`.

### v0.1.2 cycle — pre-PR convergence

- **T5T6-I1** [2026-04-20, commit `491bce3`] `from scripts.policy import Policy` in `__main__` failed on direct script invocation. Promoted imports to module top-level in both `nemweb_download.py` and `extract_patterns.py`. Added `if __package__ is None:` sys.path bootstrap so `python scripts/X.py` and `python -m scripts.X` both resolve. Reverted the workflow's `-m` workaround (was patching the symptom). Root cause of Monday 2026-04-20 03:00 UTC silent canary crash.

### Notes (not deferrals)

- **T10-N1** Ruff auto-removed unused `import json` and `AuditFinding` imports in `tests/test_audit_policy.py`. Imports were genuinely unused.
- **T10-N2** Unicode minus `−` (U+2212) replaced with ASCII `-` in `format_report` display string. No test assertion references the character.
