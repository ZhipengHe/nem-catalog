"""Merge patterns/auto/catalog.json with patterns/curated/*.yaml overlays.

Merge semantics (see docs/architecture.md):

1. Curated entry with `curated_only: true` → INSERT into the catalog as-is.
   Derives `repo` and `intra_repo_id` from the `{repo}:{intra_repo_id}` key.
   Requires `tiers` in the YAML (schema validation catches omissions).
   If the key also exists in auto, warn and overwrite with the curated
   record.
2. Curated entry without `curated_only` (override):
   a. Field overlap with auto: curated wins; emit WARNING with both values.
   b. Curated-only field: accept unconditionally.
   c. Key absent from auto: FAIL immediately (suspected AEMO deletion).
3. Auto-only dataset key: pass through unchanged.

v2.0.0 array-shape contract: dataset.tiers[T] is a list of tier records, not
a single dict. Curated YAML files continue to write one tier dict per tier
name (e.g. ``tiers: {CURRENT: {field: value}}``); merge wraps each as a
1-element list to match the v2.0.0 array shape, and broadcasts curated
fields across all records in an existing auto tier list.

Usage:
    python scripts/merge_catalog.py --auto patterns/auto/catalog.json \\
        --curated patterns/curated/ --out catalog.json
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import sys
from pathlib import Path
from typing import Any

import jsonschema  # type: ignore[import-untyped]
import yaml  # type: ignore[import-untyped]

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "catalog.schema.json"

# YAML filename stem -> repo enum value in the schema.
_REPO_STEM_MAP = {
    "reports": "Reports",
    "mmsdm": "MMSDM",
    "nemde": "NEMDE",
    "fcas_causer_pays": "FCAS_Causer_Pays",
}


def load_auto(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = json.loads(path.read_text())
    return data


def load_curated(
    curated_dir: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Return (per_key_overlays, per_repo_defaults).

    per_repo_defaults[repo] is the '__default__' block from <repo>.yaml if present.
    Raises SystemExit on duplicate keys across files (identifying both file paths).
    """
    overlays: dict[str, dict[str, Any]] = {}
    overlay_sources: dict[str, Path] = {}
    defaults: dict[str, dict[str, Any]] = {}
    for yml in sorted(curated_dir.glob("*.yaml")):
        # freshness-policy.yaml is a curated artifact but not a dataset overlay;
        # it's consumed by scripts/policy.py + scripts/audit_policy.py, not here.
        if yml.name == "freshness-policy.yaml":
            continue
        repo_name = yml.stem
        raw = yaml.safe_load(yml.read_text())
        content: dict[str, Any] = raw or {}
        if "__default__" in content:
            defaults[_title_case_repo(repo_name)] = content.pop("__default__")
        for key, overlay in content.items():
            if key in overlays:
                prior = overlay_sources[key]
                raise SystemExit(
                    f"FAIL: duplicate curated key {key!r} across YAML files: "
                    f"{prior.name} and {yml.name}"
                )
            overlays[key] = overlay
            overlay_sources[key] = yml
    return overlays, defaults


def _title_case_repo(stem: str) -> str:
    """Map YAML filename stem to repo enum value."""
    return _REPO_STEM_MAP.get(stem.lower(), stem)


def merge(
    auto: dict[str, Any],
    overlays: dict[str, dict[str, Any]],
    defaults: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Apply curated overlays to the auto catalog. Returns merged catalog.

    Curated YAML entries are one of two kinds:

    - Override (no curated_only flag): merges fields into an existing auto
      entry. If the auto entry is missing, that means AEMO deleted a dataset
      we used to describe. Fail immediately — the curator should either
      restore the entry in AEMO or remove the YAML line.
    - Placeholder (curated_only: true): inserts into the catalog as-is.
      Requires a complete record shape (tiers in particular). Never
      orphan. If the key ALSO exists in auto, the curated record wins and
      a warning is emitted so the collision is visible.
    """
    merged: dict[str, Any] = copy.deepcopy(auto)
    datasets: dict[str, Any] = merged["datasets"]
    warnings: list[str] = []
    missing_auto_orphans: list[str] = []

    for key, overlay in overlays.items():
        if overlay.get("curated_only") is True:
            _insert_curated_only(key, overlay, merged, warnings)
            continue
        # Override path
        if key not in datasets:
            missing_auto_orphans.append(key)
            continue
        _merge_record(key, datasets[key], overlay, warnings)

    # Apply per-repo defaults only where the field is currently None/absent.
    for ds in datasets.values():
        repo = ds["repo"]
        default = defaults.get(repo, {})
        for field, value in default.items():
            if ds.get(field) is None:
                ds[field] = value

    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)

    if missing_auto_orphans:
        for key in missing_auto_orphans:
            print(
                f"ORPHAN CURATED KEY: {key} (override has no matching auto entry "
                f"— suspected AEMO deletion)",
                file=sys.stderr,
            )
        raise SystemExit(1)

    # Inject catalog-level crawl timestamps from workflow env vars.
    # Present only when the workflow explicitly exports them (i.e. real
    # weekly/audit runs, not local development merges).
    attempted = os.environ.get("LAST_CRAWL_ATTEMPTED_AT")
    completed = os.environ.get("LAST_CRAWL_COMPLETED_AT")
    if attempted:
        merged["last_crawl_attempted_at"] = attempted
    if completed:
        merged["last_crawl_completed_at"] = completed

    return merged


def _insert_curated_only(
    key: str,
    overlay: dict[str, Any],
    merged: dict[str, Any],
    warnings: list[str],
) -> None:
    """Insert a curated_only entry into the catalog. Derive ONLY repo and
    intra_repo_id from the key; all other fields come from the YAML overlay
    as-is. Missing required fields (resolvable, tiers) are caught by schema
    validate() after merge completes — intentionally, so malformed YAML
    surfaces as a validation error instead of being silently backfilled.

    Also appends the key to merged["raw_keys"] so placeholder entries are
    discoverable via list_datasets(include_raw=True). Without this, a user
    searching for "NEXT_DAY_OFFER" variants would not see the anomaly
    entry even though it's in datasets.
    """
    datasets: dict[str, Any] = merged["datasets"]
    if key in datasets:
        warnings.append(
            f"curated_only: {key} shadows an auto entry (curated record wins, auto entry discarded)"
        )
    if ":" not in key:
        raise SystemExit(f"FAIL: curated_only key {key!r} is not in 'Repo:intra_repo_id' form")
    repo, intra_repo_id = key.split(":", 1)
    record = {k: v for k, v in overlay.items() if k != "curated_only"}
    if "tiers" in record:
        record["tiers"] = {
            tier_name: ([tier_dict] if isinstance(tier_dict, dict) else tier_dict)
            for tier_name, tier_dict in record["tiers"].items()
        }
    # repo + intra_repo_id are derived from the key. If the YAML also sets
    # them, the values MUST match — accepting a divergent YAML value would
    # silently produce an inconsistent record (key says one thing, fields
    # say another). Validate, then overwrite unconditionally so the key
    # is the single source of truth.
    for field, expected in (("repo", repo), ("intra_repo_id", intra_repo_id)):
        if field in record and record[field] != expected:
            raise SystemExit(
                f"FAIL: curated_only key {key!r} has conflicting "
                f"{field}={record[field]!r}; expected {expected!r} (derived from key)"
            )
    record["repo"] = repo
    record["intra_repo_id"] = intra_repo_id
    datasets[key] = record
    # Make the placeholder discoverable via list_datasets(include_raw=True).
    # dataset_keys is the curated user-facing subset; raw_keys is "everything
    # the catalog knows about." Placeholders belong in raw_keys.
    raw_keys: list[str] = merged["raw_keys"]
    if key not in raw_keys:
        raw_keys.append(key)
        raw_keys.sort()


def _merge_record(
    key: str, ds: dict[str, Any], overlay: dict[str, Any], warnings: list[str]
) -> None:
    for field, curated_value in overlay.items():
        if field == "tiers":
            _merge_tiers(key, ds, curated_value, warnings)
            continue
        auto_value = ds.get(field)
        if auto_value is not None and auto_value != curated_value:
            warnings.append(f"{key}.{field}: auto={auto_value!r} vs curated={curated_value!r}")
        ds[field] = curated_value


def _merge_tiers(
    key: str, ds: dict[str, Any], curated_tiers: dict[str, Any], warnings: list[str]
) -> None:
    for tier_name, tier_overlay in curated_tiers.items():
        if isinstance(tier_overlay, list):
            raise SystemExit(
                f"FAIL: curated YAML for {key!r} provides list-shape "
                f"tiers.{tier_name} — this shape is reserved for the auto "
                f"catalog only; curated YAML must use a single tier dict "
                f"per tier name (the merge layer wraps it as a 1-element list)."
            )
        if tier_name not in ds["tiers"]:
            warnings.append(f"{key}.tiers.{tier_name}: curated-only tier (auto has no such tier)")
            ds["tiers"][tier_name] = [tier_overlay]  # wrap as 1-element list
            continue
        # auto tier is now a list of records — broadcast curated fields to each
        for record in ds["tiers"][tier_name]:
            for field, curated_value in tier_overlay.items():
                auto_value = record.get(field)
                if auto_value is not None and auto_value != curated_value:
                    warnings.append(
                        f"{key}.tiers.{tier_name}[*].{field}: "
                        f"auto={auto_value!r} vs curated={curated_value!r}"
                    )
                record[field] = curated_value


def validate(catalog: dict[str, Any]) -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    jsonschema.validate(instance=catalog, schema=schema)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", required=True, type=Path)
    parser.add_argument("--curated", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    auto = load_auto(args.auto)
    overlays, defaults = load_curated(args.curated)
    merged = merge(auto, overlays, defaults)

    if not merged.get("datasets"):
        print("WARNING: empty catalog — auto catalog contained zero datasets")

    try:
        validate(merged)
    except jsonschema.ValidationError as e:
        print(f"FAIL: merged catalog does not validate: {e.message}", file=sys.stderr)
        return 1
    print("schema validation: OK")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
