"""Tests for write_json() sub-pattern handling per issue #22.

Golden fixtures for each collision sub-pattern category:
- SAME_PATH_MULTI_FILE: 1 path, N filename families
- MIXED: parent dir with both sub-streams and same-path families
- DUPLICATE_STRADDLE: parent + /DUPLICATE/ sibling pairs
- MULTI_SUBDIR: N distinct path+filename pairs, no DUPLICATE

Each test verifies the structural invariant: every input row has a
corresponding output record under the v2.0.0 array-valued tier schema.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import extract_patterns  # noqa: E402


def _make_row_base(**kwargs):
    """Factory: build a minimal row dict with sensible defaults."""
    defaults = {
        "repo": "Reports",
        "retention_tier": "CURRENT",
        "intra_repo_id": "Test_Dataset",
        "path_template": "/Reports/CURRENT/Test_Dataset/",
        "filename_template": "TEST_{timestamp}.csv",
        "filename_regex": "^TEST_\\d{12}\\.csv$",
        "skeleton": "skel-1",
        "sample_filename": "TEST_202604160445.csv",
        "anomaly_flag": "",
        "files_count": 100,
        "first_seen_snapshot": "2026-04-16",
        "last_seen_snapshot": "2026-04-18",
    }
    defaults.update(kwargs)
    return defaults


def test_same_path_multi_file(tmp_path):
    """SAME_PATH_MULTI_FILE: 3 rows, same path, distinct filename families.

    Structural shape: 1 path_template x 3 filename_template values.
    Invariant: every input row -> one output record.
    """
    rows = [
        _make_row_base(
            repo="Reports",
            intra_repo_id="VicGas",
            path_template="/Reports/CURRENT/VicGas/",
            filename_template="vicgas_aaa_{date}.csv",
            filename_regex="^vicgas_aaa_\\d{8}\\.csv$",
            sample_filename="vicgas_aaa_20260416.csv",
            files_count=50,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="VicGas",
            path_template="/Reports/CURRENT/VicGas/",
            filename_template="vicgas_bbb_{date}.csv",
            filename_regex="^vicgas_bbb_\\d{8}\\.csv$",
            sample_filename="vicgas_bbb_20260416.csv",
            files_count=60,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="VicGas",
            path_template="/Reports/CURRENT/VicGas/",
            filename_template="vicgas_ccc_{date}.csv",
            filename_regex="^vicgas_ccc_\\d{8}\\.csv$",
            sample_filename="vicgas_ccc_20260416.csv",
            files_count=70,
        ),
    ]

    out = tmp_path / "catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.25",
        as_of="2026-04-25T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    catalog = json.loads(out.read_text())

    dataset_key = "Reports:VicGas"
    assert dataset_key in catalog["datasets"]
    ds = catalog["datasets"][dataset_key]
    assert "CURRENT" in ds["tiers"]

    emitted_records = ds["tiers"]["CURRENT"]
    assert isinstance(emitted_records, list)
    assert len(emitted_records) == 3, (
        f"Expected 3 tier records (one per filename family), got {len(emitted_records)}"
    )

    # All 3 records share the same path_template
    paths = {r["path_template"] for r in emitted_records}
    assert paths == {"/Reports/CURRENT/VicGas/"}, f"Expected 1 unique path, got {paths}"

    # All 3 distinct filename_templates appear
    filenames = {r["filename_template"] for r in emitted_records}
    expected_filenames = {
        "vicgas_aaa_{date}.csv",
        "vicgas_bbb_{date}.csv",
        "vicgas_ccc_{date}.csv",
    }
    assert filenames == expected_filenames, f"Expected 3 distinct filenames, got {filenames}"

    # Invariant: every input row has a corresponding output record
    input_pairs = {(r["path_template"], r["filename_template"]) for r in rows}
    output_pairs = {(r["path_template"], r["filename_template"]) for r in emitted_records}
    assert input_pairs == output_pairs, (
        f"Input-output mismatch: input={input_pairs}, output={output_pairs}"
    )
    assert len(emitted_records) == len(rows), (
        f"Input rows: {len(rows)}, output records: {len(emitted_records)}"
    )


def test_mixed(tmp_path):
    """MIXED: 4 rows, 2 distinct paths, 4 distinct filename families.

    Structural shape: 2 paths x varying filename families (some sub-streams).
    Invariant: every input row -> one output record.
    """
    rows = [
        _make_row_base(
            repo="Reports",
            intra_repo_id="STTM_Data",
            path_template="/Reports/CURRENT/STTM/",
            filename_template="sttm_parent_a_{date}.csv",
            filename_regex="^sttm_parent_a_\\d{8}\\.csv$",
            sample_filename="sttm_parent_a_20260416.csv",
            files_count=40,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="STTM_Data",
            path_template="/Reports/CURRENT/STTM/",
            filename_template="sttm_parent_b_{date}.csv",
            filename_regex="^sttm_parent_b_\\d{8}\\.csv$",
            sample_filename="sttm_parent_b_20260416.csv",
            files_count=50,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="STTM_Data",
            path_template="/Reports/CURRENT/STTM/Stream_A/",
            filename_template="stream_a_{date}.csv",
            filename_regex="^stream_a_\\d{8}\\.csv$",
            sample_filename="stream_a_20260416.csv",
            files_count=30,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="STTM_Data",
            path_template="/Reports/CURRENT/STTM/Stream_B/",
            filename_template="stream_b_{date}.csv",
            filename_regex="^stream_b_\\d{8}\\.csv$",
            sample_filename="stream_b_20260416.csv",
            files_count=35,
        ),
    ]

    out = tmp_path / "catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.25",
        as_of="2026-04-25T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    catalog = json.loads(out.read_text())

    dataset_key = "Reports:STTM_Data"
    assert dataset_key in catalog["datasets"]
    ds = catalog["datasets"][dataset_key]
    assert "CURRENT" in ds["tiers"]

    emitted_records = ds["tiers"]["CURRENT"]
    assert isinstance(emitted_records, list)
    assert len(emitted_records) == 4, (
        f"Expected 4 tier records (mixed parent + sub-stream), got {len(emitted_records)}"
    )

    # 2 distinct path_templates
    paths = {r["path_template"] for r in emitted_records}
    expected_paths = {
        "/Reports/CURRENT/STTM/",
        "/Reports/CURRENT/STTM/Stream_A/",
        "/Reports/CURRENT/STTM/Stream_B/",
    }
    assert paths == expected_paths, f"Expected 3 distinct paths, got {paths}"

    # 4 distinct filename_templates
    filenames = {r["filename_template"] for r in emitted_records}
    expected_filenames = {
        "sttm_parent_a_{date}.csv",
        "sttm_parent_b_{date}.csv",
        "stream_a_{date}.csv",
        "stream_b_{date}.csv",
    }
    assert filenames == expected_filenames, f"Expected 4 distinct filenames, got {filenames}"

    # Invariant: every input row has a corresponding output record
    input_pairs = {(r["path_template"], r["filename_template"]) for r in rows}
    output_pairs = {(r["path_template"], r["filename_template"]) for r in emitted_records}
    assert input_pairs == output_pairs, (
        f"Input-output mismatch: input={input_pairs}, output={output_pairs}"
    )
    assert len(emitted_records) == len(rows), (
        f"Input rows: {len(rows)}, output records: {len(emitted_records)}"
    )


def test_duplicate_straddle(tmp_path):
    """DUPLICATE_STRADDLE: 2 rows, parent + /DUPLICATE/ sibling, same filename.

    Structural shape: parent path and /DUPLICATE/ sibling path, identical
    filename patterns, represent the same underlying data duplicated/mirrored.
    Invariant: every input row -> one output record.
    """
    rows = [
        _make_row_base(
            repo="Reports",
            intra_repo_id="Dispatch_SCADA",
            path_template="/Reports/CURRENT/Dispatch_SCADA/",
            filename_template="scada_dispatch_{timestamp}.zip",
            filename_regex="^scada_dispatch_\\d{12}\\.zip$",
            sample_filename="scada_dispatch_202604160445.zip",
            files_count=200,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="Dispatch_SCADA",
            path_template="/Reports/CURRENT/Dispatch_SCADA/DUPLICATE/",
            filename_template="scada_dispatch_{timestamp}.zip",
            filename_regex="^scada_dispatch_\\d{12}\\.zip$",
            sample_filename="scada_dispatch_202604160445.zip",
            files_count=200,
        ),
    ]

    out = tmp_path / "catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.25",
        as_of="2026-04-25T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    catalog = json.loads(out.read_text())

    dataset_key = "Reports:Dispatch_SCADA"
    assert dataset_key in catalog["datasets"]
    ds = catalog["datasets"][dataset_key]
    assert "CURRENT" in ds["tiers"]

    emitted_records = ds["tiers"]["CURRENT"]
    assert isinstance(emitted_records, list)
    assert len(emitted_records) == 2, (
        f"Expected 2 tier records (parent + DUPLICATE sibling), got {len(emitted_records)}"
    )

    # Both paths should be present: parent and /DUPLICATE/ variant
    paths = {r["path_template"] for r in emitted_records}
    expected_paths = {
        "/Reports/CURRENT/Dispatch_SCADA/",
        "/Reports/CURRENT/Dispatch_SCADA/DUPLICATE/",
    }
    assert paths == expected_paths, f"Expected parent and DUPLICATE paths, got {paths}"

    # Both records share the same filename_template
    filenames = {r["filename_template"] for r in emitted_records}
    assert filenames == {"scada_dispatch_{timestamp}.zip"}, (
        f"Expected 1 unique filename, got {filenames}"
    )

    # Invariant: every input row has a corresponding output record
    input_pairs = {(r["path_template"], r["filename_template"]) for r in rows}
    output_pairs = {(r["path_template"], r["filename_template"]) for r in emitted_records}
    assert input_pairs == output_pairs, (
        f"Input-output mismatch: input={input_pairs}, output={output_pairs}"
    )
    assert len(emitted_records) == len(rows), (
        f"Input rows: {len(rows)}, output records: {len(emitted_records)}"
    )


def test_multi_subdir(tmp_path):
    """MULTI_SUBDIR: 3 rows, N distinct (path, filename) pairs, no DUPLICATE.

    Structural shape: 3 completely independent path+filename combinations;
    each row has a unique (path_template, filename_template) pair.
    No /DUPLICATE/ sibling relationships.
    Invariant: every input row -> one output record.
    """
    rows = [
        _make_row_base(
            repo="Reports",
            intra_repo_id="GSH_Data",
            path_template="/Reports/CURRENT/GSH/Main/",
            filename_template="gsh_main_{date}.csv",
            filename_regex="^gsh_main_\\d{8}\\.csv$",
            sample_filename="gsh_main_20260416.csv",
            files_count=100,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="GSH_Data",
            path_template="/Reports/CURRENT/GSH/Backup/",
            filename_template="gsh_backup_{date}.csv",
            filename_regex="^gsh_backup_\\d{8}\\.csv$",
            sample_filename="gsh_backup_20260416.csv",
            files_count=95,
        ),
        _make_row_base(
            repo="Reports",
            intra_repo_id="GSH_Data",
            path_template="/Reports/CURRENT/GSH/Archive/",
            filename_template="gsh_archive_{year}_{month}.csv",
            filename_regex="^gsh_archive_\\d{4}_\\d{2}\\.csv$",
            sample_filename="gsh_archive_2026_04.csv",
            files_count=50,
        ),
    ]

    out = tmp_path / "catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.25",
        as_of="2026-04-25T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    catalog = json.loads(out.read_text())

    dataset_key = "Reports:GSH_Data"
    assert dataset_key in catalog["datasets"]
    ds = catalog["datasets"][dataset_key]
    assert "CURRENT" in ds["tiers"]

    emitted_records = ds["tiers"]["CURRENT"]
    assert isinstance(emitted_records, list)
    assert len(emitted_records) == 3, (
        f"Expected 3 tier records (distinct subdirs), got {len(emitted_records)}"
    )

    # 3 distinct path_templates
    paths = {r["path_template"] for r in emitted_records}
    expected_paths = {
        "/Reports/CURRENT/GSH/Main/",
        "/Reports/CURRENT/GSH/Backup/",
        "/Reports/CURRENT/GSH/Archive/",
    }
    assert paths == expected_paths, f"Expected 3 distinct paths, got {paths}"

    # 3 distinct filename_templates
    filenames = {r["filename_template"] for r in emitted_records}
    expected_filenames = {
        "gsh_main_{date}.csv",
        "gsh_backup_{date}.csv",
        "gsh_archive_{year}_{month}.csv",
    }
    assert filenames == expected_filenames, f"Expected 3 distinct filenames, got {filenames}"

    # Invariant: every input row has a corresponding output record
    input_pairs = {(r["path_template"], r["filename_template"]) for r in rows}
    output_pairs = {(r["path_template"], r["filename_template"]) for r in emitted_records}
    assert input_pairs == output_pairs, (
        f"Input-output mismatch: input={input_pairs}, output={output_pairs}"
    )
    assert len(emitted_records) == len(rows), (
        f"Input rows: {len(rows)}, output records: {len(emitted_records)}"
    )
