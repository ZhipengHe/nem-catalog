# Curated Patterns

Human-authored overlays on top of the machine-generated `patterns/auto/` catalog.

## What goes here

**Net-new human judgment only**, not a re-encoding of extractor output:

- `anomaly_note` — human-readable explanation for edge cases the extractor flags but can't fully describe.
- `retention_hint_unverified_days` — derived from mirror observation, confirmed by a human.
- `schema_source` — URLs to authoritative AEMO schema documentation.
- `query_shape` — per-record user affordance (what inputs does THIS dataset take).
- Deprecation markers for datasets AEMO is retiring.

## What does NOT go here

- `path_template`, `filename_template`, `filename_regex`, `observed_range` — these are the extractor's job. If the extractor is wrong, fix the extractor.
- Regenerated pattern rows from URL-CONVENTIONS.md — that file is already a build artifact.

## Merge semantics

See `scripts/merge_catalog.py` and `docs/architecture.md`:

1. Field overlap with auto → curated wins, build warns with both values.
2. Curated-only field → accept unconditionally.
3. Auto-only field → pass through.
4. Orphan curated key (not in auto) → warn on first occurrence, fail on 2 consecutive weekly runs.
5. Auto-only key → flow through to catalog.

## File format

One YAML file per repo. Top-level keys are dataset identifiers in `Repo:intra_repo_id` form.
