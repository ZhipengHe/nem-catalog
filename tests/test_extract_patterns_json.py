"""Tests for the write_json() emitter in scripts/extract_patterns.py."""

import json
import sys
from pathlib import Path

import jsonschema
import pytest

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import extract_patterns  # noqa: E402

SCHEMA = json.loads((REPO_ROOT / "schemas" / "catalog.schema.json").read_text())


def _rows_dispatch_is_reports():
    """Two rows (CURRENT and ARCHIVE) for Reports:DispatchIS_Reports."""
    return [
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
        },
        {
            "repo": "Reports",
            "retention_tier": "ARCHIVE",
            "intra_repo_id": "DispatchIS_Reports",
            "path_template": "/Reports/ARCHIVE/DispatchIS_Reports/",
            "filename_template": "PUBLIC_DISPATCHIS_{date}.zip",
            "filename_regex": "^PUBLIC_DISPATCHIS_\\d{8}\\.zip$",
            "skeleton": "skel-2",
            "sample_filename": "PUBLIC_DISPATCHIS_20250407.zip",
            "anomaly_flag": "",
            "files_count": 375,
            "first_seen_snapshot": "2025-04-09",
            "last_seen_snapshot": "2026-04-18",
        },
    ]


def test_write_json_groups_rows_by_dataset_and_tier(tmp_path):
    rows = _rows_dispatch_is_reports()
    out = tmp_path / "auto-catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.18",
        as_of="2026-04-18T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    data = json.loads(out.read_text())
    assert "datasets" in data
    assert "Reports:DispatchIS_Reports" in data["datasets"]
    ds = data["datasets"]["Reports:DispatchIS_Reports"]
    assert set(ds["tiers"].keys()) == {"CURRENT", "ARCHIVE"}


def test_write_json_output_validates_against_schema(tmp_path):
    rows = _rows_dispatch_is_reports()
    out = tmp_path / "auto-catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.18",
        as_of="2026-04-18T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    data = json.loads(out.read_text())
    jsonschema.validate(instance=data, schema=SCHEMA)


def test_write_json_preserves_mixed_case_nemde_prefix(tmp_path):
    rows = [
        {
            "repo": "NEMDE",
            "retention_tier": "NEMDE_Files",
            "intra_repo_id": "NemPriceSetter",
            "path_template": "/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{month}/NEMDE_Market_Data/NEMDE_Files/",
            "filename_template": "NemPriceSetter_{date}_xml.zip",
            "filename_regex": "^NemPriceSetter_\\d{8}_xml\\.zip$",
            "skeleton": "skel-1",
            "sample_filename": "NemPriceSetter_20090701_xml.zip",
            "anomaly_flag": "",
            "files_count": 6118,
            "first_seen_snapshot": "2017-01-12",
            "last_seen_snapshot": "2026-04-01",
        }
    ]
    out = tmp_path / "auto-catalog.json"
    extract_patterns.write_json(rows, out_path=out, catalog_version="2026.04.18", as_of="2026-04-18T00:00:00Z", source_mirror_commit="79cbad2")
    data = json.loads(out.read_text())
    assert "NEMDE:NemPriceSetter" in data["datasets"]
    assert "NEMDE:NEMPriceSetter" not in data["datasets"]


def test_write_json_includes_top_level_fields(tmp_path):
    rows = _rows_dispatch_is_reports()
    out = tmp_path / "auto-catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.18",
        as_of="2026-04-18T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    data = json.loads(out.read_text())
    assert data["schema_version"] == "1.0.0"
    assert data["catalog_version"] == "2026.04.18"
    assert data["as_of"] == "2026-04-18T00:00:00Z"
    assert data["source_mirror_commit"] == "79cbad2"


def test_write_json_on_empty_rows_raises(tmp_path):
    """Test plan line 62: 'nemweb-mirror/ is empty → CI acceptance test should flag
    this as a failure.' write_json() must refuse to emit a zero-dataset catalog —
    shipping one would silently publish a blank Pages site to every consumer.
    Empty mirror is always a crawl bug or mis-configured CI, never a valid state."""
    out = tmp_path / "auto-catalog.json"
    with pytest.raises(ValueError, match="empty.*mirror|zero rows"):
        extract_patterns.write_json(
            [],
            out_path=out,
            catalog_version="2026.04.18",
            as_of="2026-04-18T00:00:00Z",
            source_mirror_commit="79cbad2",
        )
    assert not out.exists(), "must not write a file when refusing to emit"
