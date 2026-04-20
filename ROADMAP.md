# Roadmap — nem-catalog

Feature-level forecast for what nem-catalog MIGHT grow into, beyond the near-term release plan. Aspirational, periodically reviewed, NOT commitment-grade. Active in-flight work and committed scope live in [`.plans/TODOS.md`](.plans/TODOS.md).

## Principle

nem-catalog is a **URL catalog**. It maps `(NEMWEB dataset key, time range) → candidate URLs`. Everything on this roadmap is a candidate extension. Items graduate into `.plans/TODOS.md` with a specific version tag only when (a) real user demand surfaces, (b) ecosystem evidence shows the work is load-bearing, or (c) maintainer pain points force the issue.

Items are grouped by horizon and intentionally brief. Detail is deferred until graduation.

## Near-term (v0.2 candidates)

See `.plans/TODOS.md §v0.2` for the small committed set. Other items listed here compete for v0.2 scope only if they beat the current committed items on user value.

- **Reports schema coverage via sample parsing** — Reports don't have AEMO-published schemas. Derive column shapes from sample file parsing. Known as "big scope"; only graduate if real Reports consumers ask.
- **`retention_hint` → observed-range object** with confidence derived from weekly-crawl accumulation.

## Mid-term (v0.3 – v0.5 candidates)

- **AEMO Visibility annotation per catalog entry** — 4-value taxonomy (Public / Private / Private, Public Next-Day / Private & Public) sourced from MMSDM Upgrade Reports + PDR_CONFIG CSVs. Answers "do I need participant access to fetch this?"
- **Rename predecessor/successor metadata** — 3-class verdict model (CONFIRMED / DATA-FLOW-REPLACEMENT / PRE-DDL-CAPTURED) from `reference/MMSDM-RENAMES-VERIFICATION.md`. Lets consumers resolve historical names (e.g., `BIDPEROFFER_D` → `BIDOFFERPERIOD`).
- **MMSDM column-level schema embedding** — inline column metadata per table per version from `reference/MMSDM-DDL-COLUMNS.csv` (33K rows, v5.2-v5.6). Supersedes the anchor-URL approach originally imagined in v0.1.0's TODOS. Design decision at graduation: inline-in-catalog.json (fattens the primary artifact) vs sidecar JSON-per-table (keeps catalog.json lean). 33K rows is non-trivial payload either way.
- **Per-version MMSDM table timeline** — per-(table, version, action) surface from `reference/MMSDM-TABLE-TIMELINE.csv`. Answers "what changed between v5.2 and v5.3?"
- **AEMO catalog cross-reference** — periodic completeness check against `reference/aemo-catalog/datasets/mms-data-model-definition.yaml` (AEMO's own manifest). Surfaces coverage gaps via `policy-audit.yml`.
- **AEMO coordination doc** — publish User-Agent contact, GHA IP disclosure, purpose statement, request-for-allowlist template. De-risks the maintenance story.

## Long-term (v1.0+ candidates)

- **Per-language codegen** — generate R, Julia (and other) SDK packages from the JSON Schema rather than shipping one Python SDK. Delivers on the "language-agnostic" promise properly.
- **Crawl-budget-at-scale** — parallelisation strategy when mirror listings pass ~5000. Currently 2863; roughly 5 years out at observed growth.
- **Catalog-as-semantic-bridge positioning** — if mid-term items land and adoption follows, reframe the project's public story around "bridge between NEMWEB filenames, AEMO MMSDM schema, and Reports structure." Only meaningful if the underlying features exist and are used.

## Explicitly out of scope (separate projects)

- **`nem-downloader` sibling repo** — byte-downloading + decompression + caching layer. Depends on nem-catalog via PyPI; never merges in. Triggered after v0.1 stabilises on PyPI.

## Graduation criteria

An item moves from this roadmap to `.plans/TODOS.md` with a specific version tag when at least one is true:

1. **User-demand signal** — an actual consumer (GitHub issue, email, downstream repo depending on nem-catalog) asks for it.
2. **Ecosystem gap** — a reasonable downstream use of nem-catalog is blocked without it.
3. **Maintainer tedium** — the absence of the feature creates repeated manual work during routine catalog maintenance.

Absent all three, items stay here. The roadmap is allowed to grow faster than releases; that's its job.

## Review cadence

Revisit after each minor release (v0.2, v0.3, ...) and when a major ecosystem event changes the landscape (AEMO platform change, new NEM data source, etc.). Not after every patch.
