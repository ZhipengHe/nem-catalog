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

- First clean `policy-audit.yml` run post-DUPLICATE-fix. Policy-audit is the monthly first-Monday 02:00 UTC cron; next natural fire is **2026-05-04**. Do not cut the v0.2 tag until that run is clean — it confirms the walk-filter change introduced no regressions that the audit catches.

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

### v0.2 candidate — `list_urls()` for non-temporal keys

- **What:** New SDK method that enumerates candidate URLs for dataset keys containing `{aemo_id}`, `{nn}`, `{d2}` (file-sequence placeholders). Current `resolve()` raises `NonResolvableTemplateError` on ~84% of keys.
- **Why:** v0.1.0's CHANGELOG explicitly flagged this as the v0.2 focus: _"v0.2 will add `list_urls()` to handle these."_ Closes the biggest known usability gap.
- **v0.1.0 caveat this addresses:** "Resolve coverage: ~16% of 362 keys resolve cleanly."

### v0.2 candidate — observed-range retention

- **What:** Replace `retention_hint_unverified_days: int` with `retention_hint_observed_days: {min, max, confidence}`. Derive the range and confidence from accumulated weekly-crawl observations.
- **Why:** v0.1.0's single-snapshot value is fake precision. v0.1.0 TODOS.md queued this exact item.
- **v0.1.0 caveat this addresses:** "`retention_hint_unverified_days` is derived from a single 2026-04-18 mirror snapshot. v0.2 replaces with confidence range."
- **Depends on:** Weekly workflow reliably green for ≥6 weeks.

*(MMSDM column-level schema embedding moved out of v0.2 candidates — it's on the mid-term roadmap at `/ROADMAP.md` "Mid-term (v0.3 – v0.5 candidates)". 33K-row source data exists (`reference/MMSDM-DDL-COLUMNS.csv`) but graduation needs user-demand signal or ecosystem gap. Re-enter v0.2/v0.3 scope only when a real consumer asks.)*

### v0.2 candidate — `write_json` multi-row collapse fix (28 victims, subsumes T5T6-I3)

- **What:** Redesign how `write_json()` emits multiple `(dataset, tier)` rows. Currently the per-row `datasets[key]["tiers"][tier_name] = tier_record` assignment inside `write_json()` in `scripts/extract_patterns.py` overwrites — the last row in sort order wins; all earlier rows for the same (dataset, tier) vanish. As a result, 28 (dataset, tier) combos surface only ONE of their N path_templates in the published catalog.
- **Why:** Each collapsed row represents a real dataset the consumer cannot reach via `catalog.resolve()`. Scope of silent data loss:
  - **15 `/DUPLICATE/`-related collapses.** The DUPLICATE `_LEGACY.zip` walk-filter shipped in PR #10 only fixes 2 of 17. The remaining 15 catalog tiers still point into `/DUPLICATE/` (e.g. `Reports:Dispatch_SCADA` CURRENT = `/Reports/CURRENT/Dispatch_SCADA/DUPLICATE/` — wrong primary path).
  - **13 legit-multi-subdir collapses (formerly tracked as T5T6-I3 "deep-subdir dataset schema").** 7 distinct parent streams have genuine sub-partitions under CURRENT and/or ARCHIVE: `GSH` (13 sub-datasets in both tiers), `Operational_Demand` (9 CURRENT / 6 ARCHIVE), `ROOFTOP_PV` (4 each), `Operational_Demand_Less_SNSG` (3 CURRENT / 2 ARCHIVE), `MMSDataModelReport` (3 CURRENT-only), `ECGS` (1 CURRENT-only + 3-level `Attachments/` nesting), `STTM` (2 CURRENT-only). Plus 2 taxonomy-root AUX rows (MMSDM OTHER/UNKNOWN, NEMDE ROOT_AUX/ROOT_AUX). Example: `Reports:GSH` has 13 sub-datasets (GSH_Participants, GSH_Daily_Trans_Summary, GSH_Benchmark_Price, …) but the catalog surfaces only **1**. The other 12 are invisible to every downstream consumer.
- **Fix shape (options — design in plan):**
  1. `tiers[tier]` becomes a **list** of tier_records. `resolve()` iterates. Schema-breaking (1.0.0 → 2.0.0).
  2. Promote each sub-dataset to its own `{repo}:{parent}/{sub}` dataset key (e.g. `Reports:GSH/GSH_Participants`). Consumer enumeration API changes. Tracks closer to how AEMO's own manifests classify.
  3. Add `alt_paths: list[str]` field to tier_record. Backwards-compat (additive), but ambiguous semantics for multi-path streams — which path is canonical?
  4. Hybrid: parent-preferred path_template + `partitions[]` sidecar listing for multi-subdir case. Preserves resolvable primary while exposing partitions.
- **Why design work (not inline fix):** Schema-touching. Affects every downstream consumer. Also needs `catalog.resolve()` contract update — today it assumes one path_template per (dataset, tier). Multi-path datasets mean multi-URL resolution.
- **v0.1.0 caveat this addresses:** *not listed* in v0.1.0's explicit known-issues. Latent since v0.1.0, surfaced during the DUPLICATE filter implementation on master (PR #10, 2026-04-21). T5T6-I3 tracked a subset (the 13 legit-multi-subdir cases from Issue #5 secondary finding 2026-04-20) but under-counted — the full blast radius is 28 combos once DUPLICATE is included.
- **Evidence:** the overwriting assignment in `write_json()` (search for `datasets[key]["tiers"][tier_name] = tier_record`) + `python -c "…"` audit of `reference/URL-CONVENTIONS.csv` against `patterns/auto/catalog.json` shows 28 (dataset, tier) combos with >1 distinct path_template but only 1 surviving in JSON.
- **Source:** PR #10 verification 2026-04-20; Issue #5 secondary finding 2026-04-20 (T5T6-I3).

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
