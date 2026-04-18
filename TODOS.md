# TODOS — nem-catalog

Parking lot for items deferred past v0.1 or surfaced during design / engineering review. Each entry has: what, why, when, depends-on.

## v0.1.1 ergonomics

*(`count()` helper was promoted into v0.1 during /gstack-plan-devex-review — Codex finding 6 pointed out it's a first-use safety rail, not polish.)*

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
