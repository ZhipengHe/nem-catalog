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

## Between v0.1.1 and v0.2 — un-tagged work that rolls into v0.2

Items here either gate the v0.2 acceptance check or need a design pass before batching with v0.2 feature work. Nothing here gets an independent tag.

### v0.2 pre-tag acceptance gate

Tracked on GitHub: issue #14.

- First clean `policy-audit.yml` run post-DUPLICATE-fix. Cron is `"0 0 1 * *"` (1st of month 00:00 UTC = 10:00 AEST); next natural fire **2026-05-01**. Workflow also supports `workflow_dispatch` for earlier manual evaluation once v0.2 feature work lands. Do not cut the v0.2 tag until the run (scheduled or manual) is clean — it confirms the walk-filter change introduced no regressions that the audit catches.

### Policy + audit workflow refinement (needs design pass before shipping)

Both items below touch `patterns/curated/freshness-policy.yaml` and surface through `policy-audit.yml`, but each needs a design pass before implementation. Each ships as its own `chore(policy)` / `data(policy)` PR after the design discussion converges.

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

---

## v0.2 — coherent next release (planned, not yet scoped)

v0.2 addresses v0.1.0's explicit known-issues list. Keep the scope small and focused. Pick 2–4 items from the candidate pool below; don't ship all of them.

Tracked on GitHub: issue #12 (unclassified CURRENT paths), #13 (ARCHIVE retention class), #14 (pre-tag gate), #15 (list_urls), #16 (observed-range), #22 (write_json schema collapse). Issue #17 was split into #21 + #22 on 2026-04-25 after Codex adversarial review separated a 5-line classifier fix from a schema-breaking emission-shape redesign; see #17 close comment for rationale.

### Priority ordering (2026-04-25)

Correctness bugs outrank features; schema-shape changes gate features that depend on them; patchable items ship ahead of design-heavy ones.

| Tier | Issue | Gate reason |
|---|---|---|
| **P0b — correctness, schema-breaking** | #22 `write_json` collapse | 614 rows silently lost across 56 legitimate groups. Gates #15 and the schema bump for #16. Needs design pass on fix-shape #1 vs alternatives. Now the top unshipped item. |
| **P1a — SDK promise from v0.1.0** | #15 `list_urls()` | CHANGELOG promised this as v0.2 focus. Depends on #22 landing so it can enumerate recovered multi-record tiers. |
| **P1b — schema add, dependency likely unmet** | #16 observed-range retention | Acceptance requires "≥6 weeks weekly workflow green"; weekly stabilized 2026-04-21. **Slip to v0.2.1 unless dependency is overridden.** Batch schema bump with #22 if it does land in v0.2. |
| **P2 — release gate, auto-fires** | #14 pre-tag gate | Cron `"0 0 1 * *"` — fires 2026-05-01 00:00 UTC. Zero work. |
| **P3a — audit hygiene (stretch)** | #13 `/Reports/ARCHIVE/**` rolling retention | Policy currently says `append_only`, reality is ~1yr rolling — consumer-facing lie. Small scope, has 3 candidate shapes to choose. |
| **P3b — audit hygiene (stretch)** | #12 classify ~57 unclassified CURRENT paths | Recurring `policy-audit.yml` noise. Defer-safe; no catalog correctness impact. |

**Recommended v0.2 shapes:**

- **Minimum viable (strict correctness):** #22. Recovers the remaining 614 silently-lost rows in legitimate multi-record groups; catalog becomes structurally honest. Schema bump 1.0.0 → 2.0.0.
- **Coherent scope (honors v0.1.0 promise):** #22 + #15. Adds the SDK feature v0.1.0 promised.
- **Stretch (3 items):** add #13 — small-scope policy correctness fix, independent of the schema work.

**Deferred to v0.2.1 or v0.3:** #12, #16 (both contingent on weekly-workflow stability that won't clear in the v0.2 window). #20 metadata enrichment stays parked for v0.3-v0.5 per ROADMAP.md graduation criteria.

Candidate detail sections below are ordered to match this priority — P0b first, P3b last.

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
- **v0.1.0 caveat this addresses:** *not listed* in v0.1.0's explicit known-issues. Latent since v0.1.0, surfaced during the DUPLICATE filter implementation on master (PR #10, 2026-04-21).
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
