# Curated Patterns

Human-authored overlays on top of the machine-generated `patterns/auto/` catalog.

## What goes here

**Net-new human judgment only**, not a re-encoding of extractor output:

- `anomaly_note` — human-readable explanation for edge cases the extractor flags but can't fully describe.
- `retention_hint_unverified_days` — derived from mirror observation, confirmed by a human.
- `schema_source` — URLs to authoritative AEMO schema documentation.
- `query_shape` — per-record user affordance (what inputs does THIS dataset take).
- Deprecation markers for datasets AEMO is retiring.
- Placeholder entries (`curated_only: true`) for datasets AEMO publishes without crawlable files — directory exists, zero content. Requires full tiers block.

## What does NOT go here

- `path_template`, `filename_template`, `filename_regex`, `observed_range` — these are the extractor's job. If the extractor is wrong, fix the extractor.
- Regenerated pattern rows from URL-CONVENTIONS.md — that file is already a build artifact.

## Merge semantics

See `scripts/merge_catalog.py` and `docs/architecture.md`:

1. **Placeholder entry** (`curated_only: true`): insert into the catalog as-is.
   Requires full record shape (tiers in particular). Warns and overwrites if
   the key also exists in auto. Use for AEMO directories that exist but have
   zero files (e.g., directory-level anomalies, one-off corrections).
2. **Override entry** (no `curated_only` flag):
   - Field overlap with auto: curated wins, build warns with both values.
   - Curated-only field: accept unconditionally.
   - Auto-only field: pass through.
   - Key missing from auto: FAIL immediately (suspected AEMO deletion —
     investigate the cause, then either restore the curated field or remove
     the YAML entry).
3. Auto-only key: flows through to catalog unchanged.

## File format

One YAML file per repo. Top-level keys are dataset identifiers in `Repo:intra_repo_id` form.
