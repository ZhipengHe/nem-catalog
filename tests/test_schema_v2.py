"""Tests for schema v2.0.0 (tier-as-array) shape per issue #22."""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from scripts import extract_patterns as ep  # noqa: E402

SCHEMA = json.loads((REPO_ROOT / "schemas" / "catalog.schema.json").read_text())


def test_schema_version_is_2_0_0(tmp_path):
    """RED: write_json() should emit schema_version 2.0.0 for tier-as-array support.

    Currently emits 1.0.0; this test fails until the extractor is patched.
    """
    rows = [
        {
            "repo": "Reports",
            "retention_tier": "CURRENT",
            "intra_repo_id": "DispatchIS_Reports",
            "path_template": "/Reports/CURRENT/DispatchIS_Reports/",
            "filename_template": "PUBLIC_DISPATCHIS_{timestamp}_{aemo_id}.zip",
            "filename_regex": "^PUBLIC_DISPATCHIS_\\d{12}_\\d{16}\\.zip$",
            "skeleton": "skel-1",
            "sample_filename": "PUBLIC_DISPATCHIS_202604160445_0000000513144978.zip",
            "anomaly_flag": "",
            "files_count": 578,
            "first_seen_snapshot": "2026-04-16",
            "last_seen_snapshot": "2026-04-18",
        }
    ]
    out = tmp_path / "catalog.json"
    ep.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.25",
        as_of="2026-04-25T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    catalog = json.loads(out.read_text())
    assert catalog["schema_version"] == "2.0.0"


def test_dataset_tiers_is_array():
    """RED: schema should define tiers.additionalProperties as array type.

    Currently additionalProperties is {"$ref": "#/$defs/Tier"} (single object).
    After fix, should be {"type": "array", "items": {"$ref": "#/$defs/Tier"}}.
    """
    dataset_def = SCHEMA["$defs"]["Dataset"]
    tiers_prop = dataset_def["properties"]["tiers"]
    additional_props = tiers_prop["additionalProperties"]

    # This should be an array type after the fix
    assert additional_props.get("type") == "array", (
        f"tiers.additionalProperties should have type='array', got {additional_props}"
    )

    # The array items should reference the Tier definition
    items = additional_props.get("items")
    assert items is not None, "tiers.additionalProperties.items must exist"
    assert items.get("$ref") == "#/$defs/Tier", (
        f"tiers.additionalProperties.items should reference Tier, got {items}"
    )


def test_writejson_emits_list_for_collision_fixture(tmp_path):
    """RED: write_json() should emit tiers[T] as a list when multiple rows
    share (repo, intra_repo_id, retention_tier) but differ in filename_template.

    Currently overwrites with last-write-wins (issue #22); after fix,
    should collect into an array.
    """
    # Two rows: same dataset and tier, different filename templates (collision)
    rows = [
        {
            "repo": "Reports",
            "retention_tier": "CURRENT",
            "intra_repo_id": "Test_Dataset",
            "path_template": "/Reports/CURRENT/Test_Dataset/",
            "filename_template": "FILE_A_{timestamp}.zip",
            "filename_regex": "^FILE_A_\\d{12}\\.zip$",
            "skeleton": "skel-1",
            "sample_filename": "FILE_A_202604160445.zip",
            "anomaly_flag": "",
            "files_count": 100,
            "first_seen_snapshot": "2026-04-16",
            "last_seen_snapshot": "2026-04-18",
        },
        {
            "repo": "Reports",
            "retention_tier": "CURRENT",
            "intra_repo_id": "Test_Dataset",
            "path_template": "/Reports/CURRENT/Test_Dataset/",
            "filename_template": "FILE_B_{timestamp}.zip",
            "filename_regex": "^FILE_B_\\d{12}\\.zip$",
            "skeleton": "skel-2",
            "sample_filename": "FILE_B_202604160445.zip",
            "anomaly_flag": "",
            "files_count": 50,
            "first_seen_snapshot": "2026-04-16",
            "last_seen_snapshot": "2026-04-18",
        },
    ]
    out = tmp_path / "catalog.json"
    ep.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.25",
        as_of="2026-04-25T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    catalog = json.loads(out.read_text())

    # Access the dataset and tier
    dataset_key = "Reports:Test_Dataset"
    assert dataset_key in catalog["datasets"], f"Expected dataset {dataset_key} in catalog"
    ds = catalog["datasets"][dataset_key]
    assert "CURRENT" in ds["tiers"], "Expected CURRENT tier in dataset"

    # After fix: tiers["CURRENT"] should be a list of 2 Tier records
    tier_data = ds["tiers"]["CURRENT"]
    assert isinstance(tier_data, list), (
        f"tiers['CURRENT'] should be a list (schema v2), got {type(tier_data).__name__}"
    )
    assert len(tier_data) == 2, (
        f"Expected 2 tier records in the collision fixture, got {len(tier_data)}"
    )
