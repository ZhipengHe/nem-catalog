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

**D3. Residual force-refetch mirror noise in `Reports/ARCHIVE/**` and `Data_Archive/**`**
- **What:** ~34 + ~461 files touched during 2026-04-20 investigation still sit in working tree.
- **Why deferred:** Content-aware write in `save_listing()` (T3) absorbs silently on the first policy-driven crawl post-merge.
- **When:** Auto-resolves on first weekly cron.

**D4. `main()` failure-mode red test**
- **What:** Explicit unit test that `main()` returns exit 2 on `PolicyLoadError` and `HREFExtractionShiftError`.
- **Why deferred:** Green paths verified; red-path test is ~5 min but not in verbatim spec. Both exit-2 paths reviewed and correct by inspection.
- **When:** v0.1.2 test-coverage PR.

### T2 — `scripts/policy.py`

**T2-I1. `/Data_Archive/` classified as `static`, should be `parent_index`** [important, cross-file fix]
- **What:** `/Data_Archive/**` in the policy YAML matches the bare `/Data_Archive/` (compiled regex `^/Data_Archive/.*$` matches empty tail). Longest-match (16 > 14) gives `static`, so the walker skips the bare index and can't discover a hypothetical new top-level Data_Archive sibling of `Wholesale_Electricity/`.
- **Why deferred:** Only affects the bare `/Data_Archive/` path; `Wholesale_Electricity/` (the sole existing child) still classifies correctly. Monthly `policy-audit.yml` force-refetches everything and surfaces new siblings within ~30 days. AEMO has not added a top-level Data_Archive category in years.
- **Fix:** Change `/Data_Archive/**` → `/Data_Archive/*/**` in `patterns/curated/freshness-policy.yaml`. Add pin-test: `class_for("/Data_Archive/") == "parent_index"` when both rules coexist.
- **When:** v0.1.2, combined with T2-I2.

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

**T5T6-I1. `from scripts.policy import Policy` in `__main__` fails on direct script invocation** [important, addressed in T9]
- **What:** Line 1073 of `scripts/extract_patterns.py` uses a package-relative import inside `if __name__ == "__main__":`. Running `python scripts/extract_patterns.py --policy ...` raises `ModuleNotFoundError: No module named 'scripts'`. Requires `python -m scripts.extract_patterns ...` (or `PYTHONPATH=.` prefix).
- **Status:** T9's `weekly-refresh.yml` update now uses `python -m scripts.extract_patterns --policy ...`. Same pattern expected for T11 (audit workflow).
- **Fix (v0.1.2):** Either keep the module-invocation-only contract (document it in the script's docstring) OR add a `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))` guard inside the `__main__` block so direct-script invocation also works. No urgency.

### T9 — `weekly-refresh.yml`

**T9-M1. Redundant `set -e` in the crawl step's shell block** [minor, cosmetic]
- **What:** GitHub Actions bash runs with `-eo pipefail` by default on ubuntu; the explicit `set -e` is a no-op.
- **Fix:** Remove or replace with a comment: `# GHA default shell is -eo pipefail`.
- **When:** v0.1.2 or whenever the workflow is next touched.

**T9-M2. `crawl-failure` GitHub label may not exist on the repo** [minor, ops]
- **What:** The P0-issue step creates an issue with labels `weekly-refresh,crawl-failure,p0`. If `crawl-failure` doesn't exist, `gh issue create` will fail with a confusing error that masks the underlying crawl failure.
- **Fix:** Create the label via `gh label create crawl-failure --color c04000 --description "weekly-refresh crawl step exited non-zero"` before the next cron fires. Same exposure pre-existed for the `merge,p0` label combo.
- **When:** Pre-ship checklist (before merging v0.1.1).

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
