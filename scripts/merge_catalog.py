"""Merge patterns/auto/catalog.json with patterns/curated/*.yaml overlays.

Merge semantics (see docs/architecture.md):

1. Field overlap (same field in auto + curated for same dataset key):
   curated wins; emit WARNING with both values.
2. Curated-only field: accept unconditionally, no warning.
3. Auto-only field: pass through untouched.
4. Orphan curated dataset key (key in curated but absent from auto):
   warn on first occurrence, fail on 2 consecutive weekly runs.
5. Auto-only dataset key: flows through to catalog.

Usage:
    python scripts/merge_catalog.py --auto patterns/auto/catalog.json \\
        --curated patterns/curated/ --out catalog.json [--prior-fail-count N]

--prior-fail-count is the count of previous consecutive orphan-key failures for
this curated key. The weekly workflow tracks this and passes it in.
"""

from __future__ import annotations

import argparse
import copy
import json
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
    prior_fail_count: int,
) -> dict[str, Any]:
    """Apply curated overlays to the auto catalog. Returns merged catalog."""
    merged: dict[str, Any] = copy.deepcopy(auto)
    datasets: dict[str, Any] = merged["datasets"]
    warnings: list[str] = []
    orphans: list[str] = []

    # Rule 1 + 2 + 3: apply per-key overlays (curated wins on overlap, warn).
    # Rule 4: track orphan curated keys.
    for key, overlay in overlays.items():
        if key not in datasets:
            orphans.append(key)
            continue
        _merge_record(key, datasets[key], overlay, warnings)

    # Apply per-repo defaults only where the field is currently None/absent.
    for ds in datasets.values():
        repo = ds["repo"]
        default = defaults.get(repo, {})
        for field, value in default.items():
            if ds.get(field) is None:
                ds[field] = value

    # Rule 5 is implicit: auto-only dataset keys are already in `datasets`.

    for w in warnings:
        print(f"WARNING: field overlap: {w}", file=sys.stderr)

    if orphans:
        for key in orphans:
            print(f"ORPHAN CURATED KEY: {key} (not in auto catalog)", file=sys.stderr)
        if prior_fail_count >= 1:
            print(
                f"FAIL: {len(orphans)} orphan curated key(s) for 2 consecutive runs.",
                file=sys.stderr,
            )
            raise SystemExit(1)

    return merged


def _merge_record(
    key: str, ds: dict[str, Any], overlay: dict[str, Any], warnings: list[str]
) -> None:
    for field, curated_value in overlay.items():
        if field == "tiers":
            _merge_tiers(key, ds, curated_value, warnings)
            continue
        auto_value = ds.get(field)
        if auto_value is not None and auto_value != curated_value:
            warnings.append(
                f"{key}.{field}: auto={auto_value!r} vs curated={curated_value!r}"
            )
        ds[field] = curated_value


def _merge_tiers(
    key: str, ds: dict[str, Any], curated_tiers: dict[str, Any], warnings: list[str]
) -> None:
    for tier_name, tier_overlay in curated_tiers.items():
        if tier_name not in ds["tiers"]:
            warnings.append(
                f"{key}.tiers.{tier_name}: curated-only tier (auto has no such tier)"
            )
            ds["tiers"][tier_name] = tier_overlay
            continue
        auto_tier = ds["tiers"][tier_name]
        for field, curated_value in tier_overlay.items():
            auto_value = auto_tier.get(field)
            if auto_value is not None and auto_value != curated_value:
                warnings.append(
                    f"{key}.tiers.{tier_name}.{field}: "
                    f"auto={auto_value!r} vs curated={curated_value!r}"
                )
            auto_tier[field] = curated_value


def validate(catalog: dict[str, Any]) -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    jsonschema.validate(instance=catalog, schema=schema)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", required=True, type=Path)
    parser.add_argument("--curated", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument(
        "--prior-fail-count",
        type=int,
        default=0,
        help="consecutive orphan-key failures in prior runs",
    )
    args = parser.parse_args()

    auto = load_auto(args.auto)
    overlays, defaults = load_curated(args.curated)
    merged = merge(auto, overlays, defaults, args.prior_fail_count)

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
