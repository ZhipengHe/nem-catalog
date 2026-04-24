# TODOS — nem-catalog

Active scope only. Aspirational features live in `/ROADMAP.md`.

## Scope discipline — lesson from v0.1.1

v0.1.1 was tagged a patch (`.1`) but actually shipped a new freshness-policy feature layer. That expanded surface then had bugs (the DUPLICATE regression) which forced a narrow follow-up fix. We shipped that fix to master but **intentionally did not cut a v0.1.2 tag** — patch-inflation for a bug already landed on master, right before v0.2 feature work, is pure tag noise. The fix rolls up into v0.2.

Going forward:

- **`.x.x.PATCH`** = bug fix only. No new feature surface. Single-concern. Land on master. **Tag only when a downstream consumer needs a pinned release** (security, breakage, stability anchor). Otherwise roll into the next minor.
- **`.x.MINOR.x`** = coherent feature release. Always tagged.
- **Features dressed as patches** = forbidden. If it adds capability, it's a minor, even if small.

Items below follow this rule.

---

## Between v0.1.1 and v0.2 — on master or about to land (un-tagged, rolls into v0.2)

Three classes of work live here. None of them gets an independent tag — everything rolls into v0.2 when it's cut.

1. **Shipped to master.** Already merged, awaiting the v0.2 pre-tag acceptance gate.
2. **Workflow + action hygiene (pre-v0.2 polish pass).** One batched `chore(workflow)` / `ci:` PR before v0.2 feature work starts. Keeps v0.2's feature PRs topically focused.
3. **Design work.** Real items but each needs a design decision before implementation. Graduate into a minor scope (v0.2 or v0.3) with a short design note first.

### Shipped to master — DUPLICATE 3-class filter

**DUPLICATE 3-class filter** merged 2026-04-20 as PR #10 / squash commit `45392b2`. Narrow walk-filter fix: the 3-class model skips only class-(a) `_LEGACY.zip` placeholders (2 dirs on the current mirror — `Dispatch_Reports/DUPLICATE/`, `Predispatch_Reports/DUPLICATE/`). Class-(b) non-LEGACY stragglers (15 dirs, 33 files) and class-(c) GBB rolling archive (617 files) stay indexed.

Primary-source verification during implementation resolved only 2 of the 17 originally-flagged "broken path_template" datasets. The remaining 15 DUPLICATE-related collapses and 13 legit-multi-subdir collapses are the same `write_json` row-overwrite bug — consolidated as a v0.2 candidate below (subsumes T5T6-I3).

Co-shipped: `reference/NEMWEB-STRUCTURE.md §2.1.1` primary-source correction (2 class-(a), not 12; prose arithmetic "9 CURRENT and 4 ARCHIVE" legit-nested).

#### v0.2 pre-tag acceptance gate

Tracked on GitHub: issue #14.

- First clean `policy-audit.yml` run post-DUPLICATE-fix. Cron is `"0 0 1 * *"` (1st of month 00:00 UTC = 10:00 AEST); next natural fire **2026-05-01**. Workflow also supports `workflow_dispatch` for earlier manual evaluation once v0.2 feature work lands. Do not cut the v0.2 tag until the run (scheduled or manual) is clean — it confirms the walk-filter change introduced no regressions that the audit catches.

### Workflow + action hygiene (pre-v0.2 polish pass)

Tracked on GitHub: issue #11 (all 13 items checklisted there).

Everything below touches CI/action/audit machinery rather than user-facing SDK surface. Items accumulated from v0.1.1 plan review + post-PR code review + monthly audit. Individually small (1-15 lines each). **Ship as one batched `chore(workflow)` / `ci:` PR before v0.2 feature work starts.** Do NOT ship any of these as an independent patch — that repeats the feature-as-patch mistake.

#### Audit + policy loader

- **POL-1.** `Policy.load` version compatibility guard. One-line add: raise `PolicyLoadError` on `version != 1`. Caught by `policy-audit.yml` when it loads a future policy version. (was v0.1.1 T2-I2)
- **POL-2.** `append_only` / `parent_index` coverage in `audit_policy.run_audit`. Currently only `unclassified` / `static` / `rolling` surface findings — audit pipeline is silent on the other two classes. (was T10-I1)
- **POL-3.** `_load_fresh` root-level `index.html` produces `/./` URL instead of `/`. One-line fix. Functional bug but symptom shows up in audit output. (was T10-M1)

#### CLI ergonomics (scripts invoked from workflows)

- **EXT-1.** `--policy` / `--threads` argv bounds check. Workflows pass these values; bad input should fail fast. (was v0.1.1 T4-I1)
- **EXT-2.** `--policy` documented in module docstring. (was T4-I3)
- **EXT-3.** Walker closure emits `fetch_noop` vs `fetch` distinction. Observability debt for weekly-refresh logs, not correctness. (was T4-I2)
- **EXT-4.** `save_listing` `idx.read_bytes()` guarded against `OSError`. Defensive hygiene for CI-runner filesystem hiccups. (was T3-I2)

#### Test coverage

- **TEST-1.** Rename `test_template_shift_raises_when_new_empty` → `test_template_shift_triggers_at_50pct_via_lowercase_href`. Add a truly-zero-HREF companion test. (was T3-I1)
- **TEST-2.** `main()` failure-mode red tests (exit 2 on `PolicyLoadError` and `HREFExtractionShiftError`). Pins CI-visible failure modes. (was D4)
- **TEST-3.** `format_report` output coverage — empty findings + multi-kind findings. (was T10-M2)

#### GitHub Actions + release

- **WF-1.** Drop unused `crawl_attempted.outputs.ts` from `weekly-refresh.yml`. (was T9-M3)
- **WF-2.** `release.yml` adds `gh release create` step so the GitHub Releases page auto-populates on tag push. Prerequisite for automating v0.2.0+ releases. (was T-release-M1)

#### Catalog schema (CI metadata leak)

- **CAT-1.** `catalog.policy_version` field at catalog root if any consumer asks. Currently derivable from `catalog_version` + git history — lands only on explicit user-demand signal. (was D1)

### Policy + audit workflow refinement (needs design pass before shipping)

Same class of work as the polish pass above — both touch `patterns/curated/freshness-policy.yaml` and surface through `policy-audit.yml` — but each item needs a design pass before implementation, so they don't batch into the quick `chore(workflow)` PR. Each ships as its own `chore(policy)` / `data(policy)` PR after the design discussion converges.

Tracked on GitHub: issue #12 (classify 57 paths), issue #13 (ARCHIVE retention).

#### Classify ~57 unclassified CURRENT paths

- **What:** `patterns/curated/freshness-policy.yaml` enumerates 29 of ~92 CURRENT dataset paths; ~57 fall through to `unclassified` via the no-catchall design.
- **New path:** `reference/aemo-catalog/manifests/` ships 97 AEMO-authored dataset manifests (today's recon). Cross-referencing those against the 57 unclassified paths is a fast path to authoritative classification — no 4-week observation window required.
- **Why design work:** 57 paths × classification-convention design × tooling work is non-trivial. Separate spike, not inline with other work.
- **When:** v0.2 or v0.3.
- **Source:** Issue #5 tertiary finding (was T1-I2).

#### `/Reports/ARCHIVE/**` retention classification refinement

- **What:** Current policy classifies ARCHIVE as `append_only`. Reality is ~1-year rolling window. Either introduce a new class (`bounded_rolling`) or document `append_only` with a retention caveat.
- **Why design work:** Needs per-stream retention measurement across ~40 ARCHIVE streams.
- **When:** v0.2 or v0.3.
- **Source:** v0.1.1 plan review (was T1-I1).

*(T5T6-I3 "Deep-subdir dataset schema" moved into the v0.2 `write_json` candidate below — it's the same bug with a higher-resolution victim count. See that entry.)*

---

## v0.2 — coherent next release (planned, not yet scoped)

v0.2 addresses v0.1.0's explicit known-issues list. Keep the scope small and focused. Pick 2–4 items from the candidate pool below; don't ship all of them.

Tracked on GitHub: issue #12 (unclassified CURRENT paths), #13 (ARCHIVE retention class), #14 (pre-tag gate), #15 (list_urls), #16 (observed-range), #21 (extractor classifier gap), #22 (write_json schema collapse). Issue #17 was split into #21 + #22 on 2026-04-25 after Codex adversarial review separated a 5-line classifier fix from a schema-breaking emission-shape redesign; see #17 close comment for rationale.

### Priority ordering (2026-04-25)

Correctness bugs outrank features; schema-shape changes gate features that depend on them; patchable items ship ahead of design-heavy ones.

| Tier | Issue | Gate reason |
|---|---|---|
| **P0a — correctness, ship first** | #21 extractor classifier gap | 552 rows mis-attributed to fake placeholder datasets; no schema touch, ~5-line regex extension + 4 AUX bucket audits. Patch-safe, independent. |
| **P0b — correctness, schema-breaking** | #22 `write_json` collapse | 614 rows silently lost across 56 legitimate groups. Gates #15 and the schema bump for #16. Needs design pass on fix-shape #1 vs alternatives. |
| **P1a — SDK promise from v0.1.0** | #15 `list_urls()` | CHANGELOG promised this as v0.2 focus. Depends on #22 landing so it can enumerate recovered multi-record tiers. |
| **P1b — schema add, dependency likely unmet** | #16 observed-range retention | Acceptance requires "≥6 weeks weekly workflow green"; weekly stabilized 2026-04-21 (4 days ago). **Slip to v0.2.1 unless dependency is overridden.** Batch schema bump with #22 if it does land in v0.2. |
| **P2 — release gate, auto-fires** | #14 pre-tag gate | Cron `"0 0 1 * *"` — fires 2026-05-01 00:00 UTC. Zero work. |
| **P3a — audit hygiene (stretch)** | #13 `/Reports/ARCHIVE/**` rolling retention | Policy currently says `append_only`, reality is ~1yr rolling — consumer-facing lie. Small scope, has 3 candidate shapes to choose. |
| **P3b — audit hygiene (stretch)** | #12 classify ~57 unclassified CURRENT paths | Recurring `policy-audit.yml` noise. Defer-safe; no catalog correctness impact. |

**Recommended v0.2 shapes:**

- **Minimum viable (strict correctness):** #21 + #22. Recovers all 1166 silently-lost rows; catalog becomes structurally honest. Schema bump 1.0.0 → 2.0.0.
- **Coherent scope (honors v0.1.0 promise):** #21 + #22 + #15. Adds the SDK feature v0.1.0 promised. 3 items, within the 2-4 guideline.
- **Stretch (4 items):** add #13 — small-scope policy correctness fix, independent of the schema work.

**Deferred to v0.2.1 or v0.3:** #12, #16 (both contingent on weekly-workflow stability that won't clear in the v0.2 window). #20 metadata enrichment stays parked for v0.3-v0.5 per ROADMAP.md graduation criteria.

Candidate detail sections below are ordered to match this priority — P0a first, P3b last.

### [P0a] v0.2 candidate — MMSDM/NEMDE classifier gaps (#21) (552 rows mis-bucketed, no schema touch)

- **What:** `extract_mmsdm_table()` at `scripts/extract_patterns.py:328-340` only parses `#`-delimited SQLLoader filenames (`PUBLIC_ARCHIVE#<TABLE>#FILE#<date>.<ext>`) and misses the actual `_`-delimited format `PUBLIC_DVD_<TABLE>_<yearmonth>.<ext>`. Function returns `None` → line 306 substitutes `"UNPARSED"` → 505 distinct MMSDM tables × 3 views (CTL / DATA / BCP_FMT) collapse into 3 placeholder buckets. Plus 4 secondary AUX buckets (`NEMDE:ROOT_AUX`, `MMSDM:UNKNOWN [OTHER]`, `MMSDM:DOCUMENTATION_AUX`, `MMSDM:MTPASA_DATA_EXPORT`) that need row-by-row audit to decide classifier-fix vs. legit-aux.
- **Why:** 11 placeholder-bucket groups hold 563 rows in the flat CSV; `write_json` then collapses them to 11 single-tier records — silently losing 552 rows. These are NOT real datasets; fixing `write_json` alone would leave 552 rows mis-attributed to fake `UNPARSED`/`UNKNOWN` keys. Fix is upstream.
- **Fix shape:** extend `extract_mmsdm_table()` to parse `PUBLIC_DVD_*` filenames (byte-exact, no `.casefold()` — §3.1 case-sensitivity discipline). Audit 4 secondary AUX buckets. Add regression test pinning the distinct `(repo, intra_repo_id, retention_tier)` tuple set.
- **Schema impact:** NONE. Extractor-only. Patchable, can ship ahead of #22.
- **Evidence:** measured 2026-04-25 primary-source audit, Codex-reviewed 2026-04-25. Reproducer and full AUX breakdown on #21.
- **Source:** 2026-04-25 audit, supersedes the extractor-gap portion of the old #17.

### [P0b] v0.2 candidate — `write_json` multi-record collapse fix (#22) (56 legitimate groups / 614 rows lost, schema-breaking)

- **What:** Redesign how `write_json()` emits multiple records for the same `(repo, intra_repo_id, retention_tier)` key. The per-row `datasets[key]["tiers"][tier_name] = tier_record` assignment at `scripts/extract_patterns.py:896` overwrites last-write-wins. 56 legitimate multi-record groups (`intra_repo_id` is a real dataset, not an AUX placeholder) surface only ONE of their N tier records in the published catalog.
- **Why:** Every collapsed row is a real dataset path + filename family the consumer cannot reach via `catalog.resolve()`. Four structural sub-patterns (measured 2026-04-25):
  - **`SAME_PATH_MULTI_FILE`** (30 groups / 281 rows lost): one path, N filename families (e.g. `Reports:VicGas [CURRENT]` = 1 path × 91 filenames; 13 `MMSDM:MMS_DATA_MODEL_v* [DOCUMENTATION]` groups at 141 rows).
  - **`MIXED`** (7 / 293): parent dir with both sub-streams and same-path filename families (`Reports:STTM`, `Reports:GBB`, `Reports:MMSDataModelReport`).
  - **`DUPLICATE_STRADDLE`** (14 / 14): parent + `/DUPLICATE/` sibling pairs. PR #10's walk-filter did NOT solve this — 14 pairs remain.
  - **`MULTI_SUBDIR`** (5 / 26): N distinct path+filename pairs, no DUPLICATE (e.g. `Reports:GSH [ARCHIVE]` = 13 streams).
- **Fix shape options (design on #22):**
  1. `tiers[tier]` becomes a **list** of tier_records — closes all four sub-patterns. Schema-breaking (1.0.0 → 2.0.0). Recommended.
  2. Sub-dataset key promotion by (path, filename-family) — technically closes all four but produces generated subkeys per filename family (e.g. `Reports:VicGas/{91-keys}`); consumer API-breaking and namespace-polluting.
  3. `alt_paths: list[str]` additive — leaves `filename_template` single-valued, cannot close `SAME_PATH_MULTI_FILE` (30 groups / 281 rows). Insufficient.
  4. Parent `path_template` + `partitions[]` sidecar — same flaw as #3.
  Shapes #3 and #4 cannot close `SAME_PATH_MULTI_FILE` without listifying `filename_template`, at which point they collapse into #1.
- **Why design work (not inline fix):** Schema-touching. Affects every downstream consumer. Also needs `catalog.resolve()` contract update — today it assumes one path_template per (dataset, tier). Multi-record tiers mean multi-URL resolution.
- **v0.1.0 caveat this addresses:** *not listed* in v0.1.0's explicit known-issues. Latent since v0.1.0, surfaced during the DUPLICATE filter implementation on master (PR #10, 2026-04-21). T5T6-I3 tracked a subset.
- **Evidence:** measured 2026-04-25, Codex-reviewed. Reproducer and sub-pattern breakdown on #22.
- **Source:** 2026-04-25 audit, supersedes the emission-shape portion of the old #17.

### [P1a] v0.2 candidate — `list_urls()` for non-temporal keys (#15)

- **What:** New SDK method that enumerates candidate URLs for dataset keys containing `{aemo_id}`, `{nn}`, `{d2}` (file-sequence placeholders). Current `resolve()` raises `NonResolvableTemplateError` on ~84% of keys.
- **Why:** v0.1.0's CHANGELOG explicitly flagged this as the v0.2 focus: _"v0.2 will add `list_urls()` to handle these."_ Closes the biggest known usability gap.
- **v0.1.0 caveat this addresses:** "Resolve coverage: ~16% of 362 keys resolve cleanly."
- **Depends on:** #22 landing — `list_urls()` cannot enumerate URLs for collapsed multi-record groups until the emission shape is fixed.

### [P1b] v0.2 candidate — observed-range retention (#16) (likely defer to v0.2.1)

- **What:** Replace `retention_hint_unverified_days: int` with `retention_hint_observed_days: {min, max, confidence}`. Derive the range and confidence from accumulated weekly-crawl observations.
- **Why:** v0.1.0's single-snapshot value is fake precision. v0.1.0 TODOS.md queued this exact item.
- **v0.1.0 caveat this addresses:** "`retention_hint_unverified_days` is derived from a single 2026-04-18 mirror snapshot. v0.2 replaces with confidence range."
- **Depends on:** Weekly workflow reliably green for ≥6 weeks. Weekly stabilized on 2026-04-21 (PR #10); earliest ready date is ~2026-06-02. **Likely misses v0.2 unless dependency is overridden.** If overridden, batch schema bump with #22's 2.0.0 bump to avoid a double break.

*(MMSDM column-level schema embedding moved out of v0.2 candidates — it's on the mid-term roadmap at `/ROADMAP.md` "Mid-term (v0.3 – v0.5 candidates)". 33K-row source data exists (`reference/MMSDM-DDL-COLUMNS.csv`) but graduation needs user-demand signal or ecosystem gap. Re-enter v0.2/v0.3 scope only when a real consumer asks.)*

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

### Post-v0.1.1 fixes on master (un-tagged, rolling into v0.2)

- **T5T6-I1** [2026-04-20, commit `491bce3`] `from scripts.policy import Policy` import promoted to module top-level + sys.path bootstrap for direct-script invocation. Root cause of Monday 2026-04-20 03:00 UTC silent canary crash.
- **Superseded PR-1 plan** [2026-04-20, commit `7611928`] Original `.plans/2026-04-20-v0.1.2-pr1-duplicate-filter.md` deleted because it proposed a binary `/DUPLICATE/` filter — the same shape that shipped as PR #9 (closed for losing 640 files). Replaced by the fresh plan anchored to `NEMWEB-STRUCTURE.md §2.1.1`.
- **DUPLICATE-T0** [2026-04-20, PR #10 / squash commit `45392b2`] Fresh 117-line PR-1 plan authored at `.plans/v0.1.2-pr1-duplicate-filter.md` (filename retained for git-history archaeology; the "v0.1.2" prefix is a historical artifact — no v0.1.2 tag was cut). Shipped as the branch's first commit so it rides inside the PR.
- **DUPLICATE-T1** [2026-04-20, PR #10 / squash commit `45392b2`] 3-class DUPLICATE filter shipped. Walk-layer guard skips only listings where every file ends in `_LEGACY.zip` under `/DUPLICATE/`. Real-mirror effect: 2 class-(a) dirs skipped (`Dispatch_Reports/DUPLICATE/` + `Predispatch_Reports/DUPLICATE/`); 15 class-(b) non-LEGACY stragglers + 617 class-(c) GBB files stay indexed. Co-shipped §2.1.1 primary-source correction (12→2 class-(a), 5→15 class-(b), prose "8 CURRENT/5 ARCHIVE" → "9/4"). Closes issue #5. Full 17-of-17 fix deferred to v0.2 `write_json` collapse work (see above) — that's 28 victims total, broader than the walk-filter scope shipped here.

### Notes (not deferrals)

- **T10-N1** Ruff auto-removed unused `import json` and `AuditFinding` imports in tests. Genuinely unused.
- **T10-N2** Unicode minus `−` replaced with ASCII `-` in `format_report`.
