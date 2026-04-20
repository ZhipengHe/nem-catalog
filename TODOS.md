# TODOS — nem-catalog

Parking lot for items deferred past v0.1 or surfaced during design / engineering review. Each entry has: what, why, when, depends-on.

## v0.1.2 follow-ups (deferred during v0.1.1-refresh-fix execution)

*(Prior `v0.1.1 ergonomics` section retired: `count()` helper was promoted into v0.1 during /gstack-plan-devex-review — Codex finding 6 pointed out it's a first-use safety rail, not polish. v0.1.1 now ships the refresh-fix; deferred ergonomics items roll forward here.)*


Items surfaced during v0.1.1 plan review or per-task code review that were intentionally deferred to keep v0.1.1 shippable before the Monday 2026-04-20 03:00 UTC cron. Each entry names the source (design phase, task ID, or review phase).

### Design-phase deferrals (agreed at plan approval)

**D1. `catalog.policy_version` field**
- **What:** Expose active policy file's `version:` at catalog root.
- **Why deferred:** Derivable from `catalog_version` + `patterns/curated/freshness-policy.yaml` git history when a consumer actually asks. No identified consumer.
- **When:** v0.1.2 if surfaced; else cut.

**D2. First observed clean `policy-audit.yml` run**
- **What:** Confirm monthly audit executes end-to-end (chore PR on clean, P1 issue on drift).
- **Why deferred:** Requires ~12 calendar days — natural first fire ~2026-05-04, outside reasonable v0.1.1 acceptance window.
- **When:** v0.1.2 acceptance gate.

**D3. ~~Residual force-refetch mirror noise in `Reports/ARCHIVE/**` and `Data_Archive/**`~~** [RESOLVED 2026-04-20 on first successful canary PR #7]
- Content-aware `save_listing()` absorbed the drift as designed. PR #7 (the first fully-green weekly-refresh run) committed 123 real HREF-change listings, zero template drift. Mechanism validated end-to-end.

**D4. `main()` failure-mode red test**
- **What:** Explicit unit test that `main()` returns exit 2 on `PolicyLoadError` and `HREFExtractionShiftError`.
- **Why deferred:** Green paths verified; red-path test is ~5 min but not in verbatim spec. Both exit-2 paths reviewed and correct by inspection.
- **When:** v0.1.2 test-coverage PR.

### T1 — `patterns/curated/freshness-policy.yaml`

**T1-I1. `/Reports/ARCHIVE/**` classification is too loose — AEMO retains ~1 year of data, items roll off** [important, classification accuracy]
- **What:** The current policy classifies `/Reports/ARCHIVE/**` as `append_only`, implying pure growth (items only added, never removed). In reality, AEMO's ARCHIVE directory has a ~1-year retention window — weekly rollups are appended at the head AND older items drop off the tail. The correct semantic is closer to "long-rolling" (365-day window) than "append_only".
- **Why this matters:** `append_only` tells downstream consumers (and the audit logic) that older references are stable. If a consumer bookmarks an ARCHIVE URL from 14 months ago expecting it to still resolve, they'll hit a 404. The audit's `reclassify_down` logic (fires only for `rolling` with zero change) also won't catch misclassification drift on ARCHIVE.
- **Why deferred:** Fixing requires empirical measurement of the actual retention window per ARCHIVE stream — probably 1 year on average but variance likely exists (e.g., Billing vs. DISPATCHFCST). Not in scope for the v0.1.1 critical fix (weekly crawler works, signals exposed).
- **Investigation scope (v0.1.2):**
  1. For each of the ~40 `/Reports/ARCHIVE/*/` streams: measure oldest vs. newest listing date; record the observed retention window.
  2. Decide: introduce a new class (e.g., `rolling_long`, `retention_window`, `bounded_rolling`) OR keep `append_only` with a documented caveat that "append-only within a retention window".
  3. If a new class is introduced: update `Policy.VALID_CLASSES`, `scripts/audit_policy.py` finding logic (the current 3-branch check doesn't cover append_only/parent_index at all — see T10-I1), and JSON Schema's `freshness_class` enum.
  4. Update `patterns/curated/freshness-policy.yaml` classification for `/Reports/ARCHIVE/**` accordingly.
  5. Document the retention window as a separate dataset-level field (e.g., `retention_window_days`) so catalog consumers know how far back to expect data.
- **When:** v0.1.2 policy-accuracy pass.

**T1-I2. Policy YAML enumerates only 29 of ~92 CURRENT dataset paths (~57 fall through to `unclassified`)** [important, data coverage, issue #5 tertiary]
- **What:** `patterns/curated/freshness-policy.yaml` was derived from a 23-hour observation window (policy header: snapshot `2026-04-19T22:20Z` → `2026-04-20T00:04Z`). 29 CURRENT paths were enumerated by hand from what churned during that window; real AEMO CURRENT has ~92 datasets. ~57 are unlisted and fall through to `unclassified` by design (the "no `/Reports/CURRENT/**` catchall" comment at policy lines 113-116 — unknown paths conservative-refetch + surface via monthly audit). After T5T6-I2's DUPLICATE fix lands, 17 of the 83 currently-unclassified datasets classify correctly against existing policy rules; the remaining ~57 still need per-dataset rules.
- **Missing examples:** `Adjusted_Prices_Reports`, `Bidmove_Complete`, `Billing`, `Daily_Reports`, `Weekly_Bulletin`, `Market_Notice`, `HistDemand`, `PD7Day`, `PDPASA`, `SEVENDAYOUTLOOK_PEAK`, `Regional_Summary_Report`, `Settlements`, `CSC_CSP_Settlements`, `Mktsusp_Pricing`, ~40 more.
- **Why this is careful work (not a quick YAML expansion):** Per the `observe-before-design` session memory: "measure full population before proposing taxonomies." Assigning each missing path a classification from a single snapshot is exactly the shortcut that shipped broken in v0.1.1. Each dataset needs AEMO cadence knowledge + ideally multi-week observed churn data from the catalog's own `last_observed_change_at` timestamps, which only accumulate across weekly runs.
- **Scope to do this right:**
  1. Land T5T6-I2 (DUPLICATE filter) so the 17 market-report datasets get correct classification + fresh `observed_range.to` first.
  2. Wait for ≥4 consecutive green weekly cron runs (gives ~4 weeks of per-dataset churn data across the shipped 92 CURRENT datasets).
  3. Build a per-dataset churn table from the mirror's git log against each dataset's `path_template/index.html`.
  4. Assign each missing path a class based on observed churn + AEMO's documented cadence conventions.
  5. Batch-add rules to `freshness-policy.yaml` grouped by retention bucket.
- **Interim signal:** The monthly `policy-audit.yml` already surfaces unclassified paths as `new_path` findings (that's how issue #5 was found). The design catches this gap — it just doesn't auto-resolve it.
- **When:** v0.1.3 or v0.2 — NOT v0.1.2. Requires observation window that doesn't exist yet.
- **Source:** Issue #5 root-cause investigation 2026-04-20, tertiary finding.

### T2 — `scripts/policy.py`

**T2-I1. ~~`/Data_Archive/` classified as `static`, should be `parent_index`~~** [FIXED in v0.1.1, commit `21fce89`]
- Closed during pre-landing review convergence (codex + gstack both HIGH). Policy catchall changed `/Data_Archive/**` → `/Data_Archive/*/**` and pinned by `test_data_archive_bare_path_is_parent_index_not_static`. Left in this section only as a historical record of what the reviewers found.

**T2-I2. No `version` compatibility guard in `Policy.load`** [important]
- **What:** `Policy.load` parses and stores `version` but never validates it. A future `version: 2` policy with different schema loads silently.
- **Why deferred:** No v2 schema exists yet. One-line add, unrequested by verbatim spec.
- **Fix:** `if int(raw.get("version", 0)) != 1: raise PolicyLoadError("unsupported policy version ...")` after the `rules` key check.
- **When:** v0.1.2.

### T3 — `save_listing()` guard

**T3-I1. Misnamed test + missing coverage for zero-HREF case** [important, test hygiene]
- **What:** `HREF_RE` has `re.IGNORECASE`; the test named `test_template_shift_raises_when_new_empty` uses a lowercase `<a href=` fixture that actually matches and extracts 1 HREF. The test hits the 50% threshold path (1*2 ≤ 2), not the zero-extraction (`not new`) branch. The truly-empty HREF branch has no dedicated test.
- **Why deferred:** Guard logic is correct; only test naming/coverage is misleading. Functional behavior verified by the other six tests.
- **Fix:** Rename to `test_template_shift_triggers_at_50pct_via_lowercase_href`. Add `test_template_shift_raises_when_new_truly_empty` using bytes with no `<A HREF=...>` markup (e.g. `b'<html>403 Forbidden</html>'`).
- **When:** v0.1.2.
- **Re-flagged by:** Copilot PR #4 review (confirms the superpowers reviewer's finding).

**T3-I2. `save_listing` does not guard `idx.read_bytes()` against `OSError`** [minor, defensive]
- **What:** When a cached `index.html` exists, `save_listing` calls `idx.read_bytes()` without a try/except. If the cached file is unreadable (permission issue, transient IO error, partial write from a prior crashed run), the crawler crashes instead of treating it as a cache miss and overwriting.
- **Why deferred:** Probability is near-zero in practice. The file is one the same process wrote earlier, on an ephemeral GHA runner with no concurrent writers. A permission error here would indicate something much worse is broken. But the fix is 3 lines and closes a real failure mode — good hygiene for v0.1.2.
- **Fix:**
  ```python
  if idx.is_file():
      try:
          old = frozenset(m.group(1) for m in HREF_RE.finditer(idx.read_bytes()))
      except OSError:
          old = None  # treat as cache miss — write unconditionally below
      if old is not None:
          new = frozenset(m.group(1) for m in HREF_RE.finditer(data))
          ...
  ```
- **When:** v0.1.2.
- **Source:** Copilot PR #4 review.

### T4 — `nemweb_download.py` `--policy` flag + walker

**T4-I1. `--policy` without argument raises `IndexError`** [important]
- **What:** `argv[i + 1]` accessed without bounds check when `--policy` is the final argv element. Same pre-existing bug for `--threads`.
- **Why deferred:** CI passes `--policy patterns/curated/freshness-policy.yaml` (fixed string); the crash path is unreachable in production. Developer-only exposure.
- **Fix:** Add bounds check:
  ```python
  elif a == "--policy":
      if i + 1 >= len(argv):
          raise SystemExit("--policy requires a path argument")
      policy_path = argv[i + 1]
      i += 1
  ```
  Apply same guard to `--threads`.
- **When:** v0.1.2.

**T4-I2. Walker closure can't emit `"fetch_noop"`** [observability debt]
- **What:** Only `_process_one_for_test` distinguishes `"fetch"` from `"fetch_noop"` via mtime comparison. Production closure always reports `"fetch"` after `save_listing`, so the wave-level `fetched=N` counter conflates real writes with content-noop re-fetches.
- **Why deferred:** Accounting debt, not correctness. v0.1.1 acceptance criteria don't require the distinction.
- **Fix:** Mirror `_process_one_for_test`'s mtime capture inside the walker closure; break out a separate per-wave counter for `fetch_noop`.
- **When:** v0.1.2 or later — depends on whether catalog consumers want per-dataset fetch-vs-noop breakdown.

**T4-I3. Module docstring does not list `--policy`** [minor]
- **What:** `scripts/nemweb_download.py` docstring lists `--gaps`, `--force`, `--threads` with usage examples; `--policy` is absent.
- **Fix:** Add a "Policy-driven refresh" block with the canonical invocation.
- **When:** v0.1.2 (batch with other housekeeping).

### T5+T6 — `extract_patterns.py` freshness fields

**T5T6-I1. ~~`from scripts.policy import Policy` in `__main__` fails on direct script invocation~~** [FIXED 2026-04-20, commit `491bce3`]
- Promoted `from scripts.policy import ...` to module top-level in both `scripts/nemweb_download.py` and `scripts/extract_patterns.py`. Added an `if __package__ is None:` sys.path bootstrap so `python scripts/X.py` and `python -m scripts.X` both resolve imports. Reverted the workflow's `-m` workaround (that was patching the symptom, not the cause). Root cause of Monday 2026-04-20 03:00 UTC silent canary crash — full analysis in issue #5 comment. Also closed T5T6 source gap: the v0.1.1 plan fixed this for `extract_patterns.py`'s invocation but never audited `nemweb_download.py`, which acquired `from scripts.policy` imports in T5/T6 after T9 had moved on.

**T5T6-I2. DUPLICATE-subdir path overwrites canonical `path_template` for 17 core market reports** [important, issue #5 primary]
- **What:** `scripts/extract_patterns.py:568-576` sorts rows by `path_template`; `write_json` at line 837 assigns `datasets[key]["tiers"][tier_name]` with last-row-wins semantics. When a dataset has files in both `/Reports/CURRENT/X/` (real data) AND `/Reports/CURRENT/X/DUPLICATE/` (AEMO dedup-placeholder, 1 stale file), they classify to the same `(repo, tier, intra_id)` and the DUPLICATE path wins because it sorts after the parent lexicographically. The catalog records the 1-file placeholder path instead of the 577-file real-data path. `Policy.class_for()` at `scripts/policy.py:84` uses `re.fullmatch`, so the policy's `/Reports/CURRENT/X/ → rolling` rule can't match the DUPLICATE-suffixed path and classification returns `unclassified`.
- **Why it matters:** 17 core AEMO market reports affected, all should be `rolling`: `Dispatch_Reports`, `Dispatch_SCADA`, `MCCDispatch`, `P5MINFCST`, `TradingIS_Reports`, `Predispatch_Reports`, `PredispatchIS_Reports`, `Dispatch_IRSR`, `Dispatchprices_PRE_AP`, `DISPATCH_NEGATIVE_RESIDUE`, `Trading_Cumulative_Price`, `Predispatch_Sensitivities`, `SEVENDAYOUTLOOK_FULL`, `P5_Reports`, `Yesterdays_Bids_Reports`, `Next_Day_Intermittent_DS`, `Next_Day_PreDispatch`. Secondary effect: `observed_range.to` and `last_observed_change_at` are computed against the stale placeholder for these 17 datasets — partial regression of issue #3 (today's canary passed on `Bidmove_Complete`, which has no DUPLICATE subdir; the 17 market reports are still stale).
- **Fix (~2 lines):** Skip DUPLICATE directories during extraction at `scripts/extract_patterns.py:477`:
  ```python
  for idx in sorted(MIRROR.rglob("index.html")):
      parent_path = url_path_from_local(idx)
      if "/DUPLICATE/" in parent_path:
          continue
      ...
  ```
- **When:** v0.1.2 — highest-leverage issue #5 remediation. Land first in the v0.1.2 PR.
- **Source:** Issue #5 root-cause investigation 2026-04-20.

**T5T6-I3. Same sort-order overwrite hits 9 deep-subdir datasets (ROOFTOP_PV, Operational_Demand, STTM, …)** [important, design call]
- **What:** After the T5T6-I2 DUPLICATE filter lands, 9 datasets still misrecord their CURRENT `path_template` as a genuine AEMO sub-partition (not a dedup artifact). Same overwrite mechanic (sort order + last-row-wins) but the winning path is a real sub-directory. Examples: `Reports:ROOFTOP_PV` → `/Reports/CURRENT/ROOFTOP_PV/FORECAST_AREA/` (last-sorted among ACTUAL, ACTUAL_AREA, FORECAST, FORECAST_AREA); `Reports:Operational_Demand` → `/Reports/CURRENT/Operational_Demand/FORECAST_HH_AREA/`; `Reports:STTM` → `/Reports/CURRENT/STTM/MOS%20Estimates/`. Also: `GSH`, `ECGS`, `GBB`, `MMSDataModelReport`, `Operational_Demand_Less_SNSG`.
- **Why it's not a simple fix:** Unlike DUPLICATE, these sub-directories are real data partitions. Losing them by picking the parent drops useful information. Keeping the last-sorted one is arbitrary. Design options:
  - (a) Record each sub-partition as its own dataset (e.g. `Reports:ROOFTOP_PV.ACTUAL`, `Reports:ROOFTOP_PV.FORECAST`).
  - (b) Record only the parent `path_template`; lose per-sub-partition `filename_regex` / `observed_range` granularity.
  - (c) Record parent as canonical `path_template`; enumerate sub-partitions in a new `partitions[]` field per tier.
  - (d) Prefer shortest `path_template` when merging into `tiers[X]` — partial fix, picks parent when it has direct files; falls back to arbitrary-but-shortest-subdir otherwise.
- **Why deferred:** Design call touching catalog schema. Needs downstream-consumer input on how sub-partitioned data should be addressed.
- **When:** v0.1.2 design spike → implementation in v0.1.3 or v0.2 depending on schema impact.
- **Source:** Issue #5 root-cause investigation 2026-04-20, secondary finding.

### T9 — `weekly-refresh.yml`

**T9-M1. ~~Redundant `set -e` in the crawl step's shell block~~** [FIXED 2026-04-20, commit `1fc5151` — the original TODO premise was wrong]
- Original claim: "GHA default shell is `-eo pipefail`, so `set -e` is redundant." **That was wrong.** The crawl step declares `shell: /usr/bin/bash -e {0}` — an explicit override that does NOT inherit GHA's default `pipefail`. Monday 2026-04-20 cron ran `uv run python scripts/nemweb_download.py ... 2>&1 | tee ...` through a Python crash; `tee` exited 0, pipe swallowed the non-zero, step marked `success`, downstream steps ran against a stale mirror, PR #6 opened claiming "0.0% change" over a silent regression. Changed to `set -eo pipefail`. The gstack adversarial review during v0.1.1 convergence (C1 finding) flagged this exact risk and was closed as a false positive based on memory of GHA defaults, without reading the actual `shell:` override — a textbook "reviewer shared sources with author" miss (ground-truth discipline §4). Lesson logged.

**T9-M2. ~~`crawl-failure` GitHub label may not exist on the repo~~** [DONE — pre-ship checklist closed 2026-04-20]
- All labels referenced by `weekly-refresh.yml` and `policy-audit.yml` are now created on the repo: `crawl-failure`, `p0`, `p1`, `policy-audit`, `weekly-refresh`, `chore`, `aemo-coordination`, `robots-halt`, `merge`, `data-catalog`. `bug` pre-existed. Verified via `gh label list`.

**T9-M3. `crawl_attempted.outputs.ts` is set but never read** [minor]
- **What:** Line 49 writes `ts=$TS` to `$GITHUB_OUTPUT`; no downstream step references `steps.crawl_attempted.outputs.ts`. The consumed path is the env var `LAST_CRAWL_ATTEMPTED_AT`.
- **Fix:** Remove the unused `echo "ts=$TS" >> $GITHUB_OUTPUT` line.
- **When:** v0.1.2.

### T10 — `scripts/audit_policy.py` monthly audit

**T10-N1. Ruff auto-removed unused `import json` and `AuditFinding` imports in tests** [note, not a deferral]
- **What:** `tests/test_audit_policy.py` imported `AuditFinding` but didn't reference the type by name (assertions use attribute access on returned list items). Ruff F401 auto-removed both it and an unused `import json`. Tests still pass.
- **Action:** None required — the imports were genuinely unused.

**T10-N2. Unicode minus `−` (U+2212) replaced with ASCII `-` in `format_report` display string** [note, not a deferral]
- **What:** Ruff RUF001 flagged the typographic minus sign. Implementer replaced with ASCII hyphen. Affects only the rendered audit report's display of HREF-removed counts — no test assertion references the character.
- **Action:** None required.

**T10-I1. `append_only` and `parent_index` paths silently swallowed by `run_audit`** [important, spec-level gap]
- **What:** `scripts/audit_policy.py` fires findings only for `unclassified` (→ `new_path`), `static` with change (→ `reclassify_up`), and `rolling` with zero change (→ `reclassify_down`). Paths classified `append_only` or `parent_index` fall through all three branches — no finding, no signal. A stale `append_only` path (zero churn for weeks) would never surface.
- **Why deferred:** The plan and verbatim spec only require these three branches. Functional for v0.1.1 — the classes that matter most (`rolling`, `static`) are covered.
- **Fix:** Extend `run_audit` with a `reclassify_down` arm for `append_only` paths with zero churn (same logic as `rolling`). Add coverage for `parent_index` if needed. Minimum interim: add a fall-through comment marking the gap.
- **When:** v0.1.2 audit-coverage pass.

**T10-M1. `_load_fresh` builds `/./` URL when fresh_dir itself contains `index.html`** [minor, edge case]
- **What:** `rel = idx.parent.relative_to(fresh_dir).as_posix()` returns `"."` (truthy) for a root-level `index.html`, so `url = "/" + "." + "/"` = `"/./"` instead of the intended `"/"`.
- **Fix:** Change guard to `if rel != "." else "/"`.
- **When:** v0.1.2. No test currently exercises this path; T11's workflow places crawler output in a nested tree so the bug is latent.

**T10-M2. No test for `format_report` output structure** [minor, test coverage]
- **What:** All 4 tests exercise `run_audit` only. `format_report`'s grouping, section headers, and the clean-audit return string have no direct coverage.
- **Fix:** Add 2 tests — one for empty findings (asserts "# Policy Audit — clean" in output), one for multi-kind findings (asserts all 3 section headers present).
- **When:** v0.1.2.

### T-release — `release.yml`

**T-release-M1. Workflow doesn't create a GitHub Release page** [minor, release ergonomics]
- **What:** `release.yml` has `permissions: contents: write` but no `gh release create` step — only the PyPI publish step runs. v0.1.1 needed a manual `gh release create v0.1.1 --notes-from-tag` after the workflow finished to populate https://github.com/ZhipengHe/nem-catalog/releases/tag/v0.1.1.
- **Fix:** Add a step after `Publish to PyPI` (and before `Open issue on failure`):
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
  Use `--notes-from-tag` to reuse the annotated tag message (which already exists per v0.1.0 + v0.1.1 release discipline). Falls back to `--generate-notes` if a tag is ever pushed without an annotation.
- **Why deferred:** Discovered post-tag during v0.1.1 release. Cosmetic for users (PyPI install works), but the GitHub side looks unfinished without it. Manual workaround is one command per release.
- **When:** v0.1.2 — fix before pushing v0.1.2 tag so the workflow self-creates the Release page.

## v0.2 catalog refinements

### Retention hint → observed range with confidence
- **What:** Replace `retention_hint_unverified_days: int` with `retention_hint_observed_days: {min, max, confidence}` object. Confidence derived from number of weekly re-crawls that observed the window.
- **Why:** Single-snapshot retention is fake precision (outside-voice finding #9). After ≥2 additional weekly crawls land, the catalog has enough data to publish an honest range.
- **When:** After P0.1 (4 consecutive green weekly runs) plus 2 more weeks of observation.
- **Depends on:** Weekly workflow being reliably green for ≥6 weeks.

### Per-table MMSDM schema pointers
- **What:** Extend `schema_source` on MMSDM records from generic portal root to per-table anchor URLs (e.g., `.../TSP_EMMSDM57_May2026/tables/DISPATCHPRICE.htm`).
- **Why:** Users querying a specific MMSDM table want to jump directly to the AEMO spec for that table, not the portal root. Higher-value UX for researchers.
- **When:** Post-v0.1. First verify URL-anchor stability (the old "Step 0" from original plan — moved here since v0.1 does not ship per-table schema).
- **Depends on:** AEMO's tech-specs portal maintaining stable per-version, per-table URLs. Verify by HEAD-checking 10 random tables at both `TSP_EMMSDM56_Nov2025/` and `TSP_EMMSDM57_May2026/` anchors; require ≥7/10 success for promotion.

### Schema coverage for Reports streams
- **What:** v0.1 ships Reports records with `schema_source: null`. v0.2 explores schema extraction from sample file parsing (Reports doesn't have AEMO docs for schemas).
- **Why:** Schema is the missing ecosystem piece for Reports; currently every downstream tool reverse-engineers it.
- **When:** Post-v0.1, scoped after understanding real consumer demand.
- **Depends on:** v0.1 adoption signals, volunteer capacity (this is a big scope).

## Strategic evaluations (v0.2+)

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
- **What:** Publish `docs/aemo-coordination.md` with User-Agent contact, GHA IP disclosure, purpose statement, and a request-for-allowlist email template. Ship in v0.1 stretch scope if time allows; else early v0.1.1.
- **Why:** Outside-voice finding #18 — AEMO permission tolerance is currently an unstated assumption. Respectful crawling posture de-risks the whole maintenance story.
- **When:** v0.1 stretch; v0.1.1 hard commit if bumped.
- **Depends on:** Nothing.

## Sibling project (tracked here for visibility, not scoped)

### `nem-downloader` sibling repo
- **What:** A separate project that depends on `nem-catalog` (via PyPI or vendoring, decided at the time) to provide the actual byte-downloading + decompression + caching layer users want.
- **Why:** Design premise 6 — nem-catalog is catalog-only; the downloader is user's own future work, first-party dogfooder for P0 success criterion.
- **When:** After v0.1 of nem-catalog ships and stabilizes.
- **Depends on:** nem-catalog v0.1 stable release on PyPI. Single vs two-repo decision deferred to that point per outside-voice finding #14.
