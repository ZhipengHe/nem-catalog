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
            "path_template": "/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{month}/NEMDE_Market_Data/NEMDE_Files/",  # noqa: E501
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
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.18",
        as_of="2026-04-18T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
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
    assert data["schema_version"] == "2.0.0"
    assert data["catalog_version"] == "2026.04.18"
    assert data["as_of"] == "2026-04-18T00:00:00Z"
    assert data["source_mirror_commit"] == "79cbad2"


def test_write_json_placeholders_cover_every_emitted_token(tmp_path):
    """B1b: placeholders section must declare every {token} used in any emitted
    filename_template or path_template.

    Catching the case where the extractor emits `{yearmonth}` or `{date1}` in a
    filename template but leaves them out of the top-level `placeholders` dict.
    Inconsistent catalog → users querying catalog.placeholders['yearmonth']
    get a KeyError while the token is live in templates.
    """
    import re

    rows = [
        # Row that uses {yearmonth} (not in _DEFAULT_PLACEHOLDERS as of pre-B1b)
        {
            "repo": "Reports",
            "retention_tier": "CURRENT",
            "intra_repo_id": "Market_Notice",
            "path_template": "/Reports/CURRENT/Market_Notice/",
            "filename_template": "NEMITWEB{d1}_MKTNOTICE_{date}.R{yearmonth}",
            "filename_regex": "^NEMITWEB\\d{1}_MKTNOTICE_\\d{8}\\.R\\d{6}$",
            "skeleton": "skel-1",
            "sample_filename": "NEMITWEB1_MKTNOTICE_20260410.R202604",
            "anomaly_flag": "",
            "files_count": 100,
            "first_seen_snapshot": "2024-01-01",
            "last_seen_snapshot": "2026-04-18",
        },
        # Row that uses {date1}, {date2} pair
        {
            "repo": "Reports",
            "retention_tier": "ARCHIVE",
            "intra_repo_id": "PredispatchIS_Reports",
            "path_template": "/Reports/ARCHIVE/PredispatchIS_Reports/",
            "filename_template": "PUBLIC_PREDISPATCHIS_{date1}_{date2}.zip",
            "filename_regex": "^PUBLIC_PREDISPATCHIS_\\d{8}_\\d{8}\\.zip$",
            "skeleton": "skel-2",
            "sample_filename": "PUBLIC_PREDISPATCHIS_20210101_20210102.zip",
            "anomaly_flag": "",
            "files_count": 500,
            "first_seen_snapshot": "2009-07-01",
            "last_seen_snapshot": "2023-12-31",
        },
        # Row that uses {datetime} and {d3}
        {
            "repo": "Reports",
            "retention_tier": "CURRENT",
            "intra_repo_id": "Adjusted_Prices_Reports",
            "path_template": "/Reports/CURRENT/Adjusted_Prices_Reports/",
            "filename_template": "PUBLIC_PRICE_REVISION_DISPATCH_{datetime}_{aemo_id}.R{d3}",
            "filename_regex": "^PUBLIC_PRICE_REVISION_DISPATCH_\\d{14}_\\d{16}\\.R\\d{3}$",
            "skeleton": "skel-3",
            "sample_filename": "PUBLIC_PRICE_REVISION_DISPATCH_20260416044500_0000000513144978.R001",  # noqa: E501
            "anomaly_flag": "",
            "files_count": 50,
            "first_seen_snapshot": "2026-04-16",
            "last_seen_snapshot": "2026-04-18",
        },
    ]
    out = tmp_path / "auto-catalog.json"
    extract_patterns.write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.18",
        as_of="2026-04-18T00:00:00Z",
        source_mirror_commit="79cbad2",
    )
    data = json.loads(out.read_text())
    placeholders = data["placeholders"]

    # Collect every {token} appearing in any template (filename or path)
    token_re = re.compile(r"\{(\w+)\}")
    used: set[str] = set()
    for rec in data["datasets"].values():
        for tier_list in rec["tiers"].values():
            for tier in tier_list:
                for key in ("filename_template", "path_template"):
                    value = tier.get(key) or ""
                    used.update(token_re.findall(value))

    missing = used - placeholders.keys()
    assert not missing, (
        f"placeholders section is missing {sorted(missing)}; "
        f"templates reference them but there is no declaration. "
        f"declared: {sorted(placeholders.keys())}"
    )

    # Each declared placeholder must have the contract fields (regex + format).
    for name, defn in placeholders.items():
        assert "regex" in defn, f"placeholder {name!r} missing 'regex' field"
        assert "format" in defn, f"placeholder {name!r} missing 'format' field"


def test_write_json_on_empty_rows_raises(tmp_path):
    """Test plan line 62: 'nemweb-mirror/ is empty → CI acceptance test should flag
    this as a failure.' write_json() must refuse to emit a zero-dataset catalog —
    shipping one would silently publish a blank Pages site to every consumer.
    Empty mirror is always a crawl bug or mis-configured CI, never a valid state."""
    out = tmp_path / "auto-catalog.json"
    with pytest.raises(ValueError, match=r"empty.*mirror|zero rows"):
        extract_patterns.write_json(
            [],
            out_path=out,
            catalog_version="2026.04.18",
            as_of="2026-04-18T00:00:00Z",
            source_mirror_commit="79cbad2",
        )
    assert not out.exists(), "must not write a file when refusing to emit"


def test_freshness_class_populated_from_policy(tmp_path):
    """write_json joins freshness_class per dataset from a Policy instance."""
    from scripts.extract_patterns import write_json
    from scripts.policy import Policy

    policy = Policy.load(_write_policy(tmp_path))
    rows = [
        {
            "repo": "Reports",
            "intra_repo_id": "DISPATCHFCST",
            "retention_tier": "CURRENT",
            "path_template": "/Reports/CURRENT/DISPATCHFCST/",
            "filename_template": "PUBLIC_DISPATCHFCST_{timestamp}.zip",
            "filename_regex": "PUBLIC_DISPATCHFCST_\\d+\\.zip",
            "sample_filename": "PUBLIC_DISPATCHFCST_202604200000.zip",
            "first_seen_snapshot": "2026-04-16T00:00:00",
            "last_seen_snapshot": "2026-04-20T00:00:00",
        }
    ]
    out = tmp_path / "out.json"
    write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.20",
        as_of="2026-04-20T00:00:00Z",
        source_mirror_commit="abcd1234",
        policy=policy,
    )
    import json

    data = json.loads(out.read_text())
    ds = data["datasets"]["Reports:DISPATCHFCST"]
    assert ds["freshness_class"] == "rolling"


def _write_policy(tmp_path):
    p = tmp_path / "freshness-policy.yaml"
    p.write_text(
        "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
        '  - pattern: "/Reports/CURRENT/**"\n    class: rolling\n'
    )
    return p


def test_last_observed_change_at_from_git_log(tmp_path, monkeypatch):
    """last_observed_change_at comes from git log -1 --format=%aI, not filesystem mtime."""
    from scripts import extract_patterns as ep
    from scripts.extract_patterns import write_json

    # Stub the git log call to return a deterministic ISO timestamp.
    def fake_git_log(path: str) -> str | None:
        return "2026-04-18T04:45:00+00:00"

    monkeypatch.setattr(ep, "_last_observed_change_at", fake_git_log)

    rows = [
        {
            "repo": "Reports",
            "intra_repo_id": "DISPATCHFCST",
            "retention_tier": "CURRENT",
            "path_template": "/Reports/CURRENT/DISPATCHFCST/",
            "filename_template": "PUBLIC_DISPATCHFCST_{timestamp}.zip",
            "filename_regex": "PUBLIC_DISPATCHFCST_\\d+\\.zip",
            "sample_filename": "PUBLIC_DISPATCHFCST_202604200000.zip",
            "first_seen_snapshot": "2026-04-16T00:00:00",
            "last_seen_snapshot": "2026-04-20T00:00:00",
        }
    ]
    out = tmp_path / "out.json"
    write_json(
        rows,
        out_path=out,
        catalog_version="2026.04.20",
        as_of="2026-04-20T00:00:00Z",
        source_mirror_commit="abcd1234",
    )
    import json

    data = json.loads(out.read_text())
    ds = data["datasets"]["Reports:DISPATCHFCST"]
    assert ds["last_observed_change_at"] == "2026-04-18T04:45:00+00:00"


# ---------- 3-class DUPLICATE filter regression test (v0.1.2) ----------


def _write_iis_listing(dir_path: Path, filenames: list[str]) -> None:
    """Write a minimal valid IIS-style index.html with one row per filename.

    ROW_RE in extract_patterns.py expects:
        <weekday>, <month> <day>, <year>  HH:MM [AP]M  <size|<dir>>  <A HREF="..">..</A>
    """
    dir_path.mkdir(parents=True, exist_ok=True)
    rows = [
        f'<pre>Thursday,  May 13, 2021  4:30 PM    12345 <A HREF="{name}">{name}</A>'
        for name in filenames
    ]
    dir_path.joinpath("index.html").write_text(
        "<html><body>" + "\n".join(rows) + "</body></html>", encoding="utf-8"
    )


def test_main_handles_all_duplicate_classes(tmp_path, monkeypatch, capsys):
    """Per reference/NEMWEB-STRUCTURE.md §2.1.1, /DUPLICATE/ subtrees split
    into three classes. Guard in main() must skip only class (a).

      (a) listings where every file is a _LEGACY.zip placeholder -> SKIP
      (b) multi-file non-_LEGACY stragglers                       -> KEEP
      (c) GBB/DUPLICATE/ rolling timestamped archive               -> KEEP

    Class-(c) assertion pins the PR #9 regression — an unconditional
    /DUPLICATE/ skip lost 617 GBB files. Do not let that re-ship.
    """
    mirror = tmp_path / "nemweb-mirror"

    # Parent streams each need a sibling real listing so the stream is
    # registered as a dataset before the DUPLICATE/ child is visited.
    _write_iis_listing(
        mirror / "Reports/CURRENT/Dispatch_Reports",
        ["PUBLIC_DISPATCH_20210513163000_0000000334543234.zip"],
    )
    # Class (a): every file is _LEGACY.zip -> skipped by guard.
    _write_iis_listing(
        mirror / "Reports/CURRENT/Dispatch_Reports/DUPLICATE",
        ["PUBLIC_DISPATCH_20210513163000_0000000334543234_LEGACY.zip"],
    )

    _write_iis_listing(
        mirror / "Reports/CURRENT/Trading_Cumulative_Price",
        ["PUBLIC_TRADING_CUMULATIVE_PRICE_202008231100_0000000412345678.zip"],
    )
    # Class (b): multi-file, no _LEGACY suffix -> kept.
    _write_iis_listing(
        mirror / "Reports/CURRENT/Trading_Cumulative_Price/DUPLICATE",
        [
            "PUBLIC_TRADING_CUMULATIVE_PRICE_202008231100_0000000412345678.zip",
            "PUBLIC_TRADING_CUMULATIVE_PRICE_202508121400_0000000512345678.zip",
        ],
    )

    _write_iis_listing(
        mirror / "Reports/CURRENT/GBB",
        ["GasBBActualFlowStorageLast31.CSV"],
    )
    # Class (c): GBB rolling timestamped archive -> kept (PR #9 regression pin).
    _write_iis_listing(
        mirror / "Reports/CURRENT/GBB/DUPLICATE",
        ["GasBBActualFlowStorageLast31_20260101000000.CSV"],
    )

    # Class (b) — single-file non-LEGACY (e.g. Dispatch_SCADA on the real mirror).
    # This pins the 2026-04-21 §2.1.1 correction: 10 of the 12 "single-file"
    # DUPLICATE dirs hold a plain parent-regex filename, NOT _LEGACY. They must
    # be kept, same as the multi-file class-(b) case.
    _write_iis_listing(
        mirror / "Reports/CURRENT/Dispatch_SCADA",
        ["PUBLIC_DISPATCHSCADA_202604181445_0000000513537601.zip"],
    )
    _write_iis_listing(
        mirror / "Reports/CURRENT/Dispatch_SCADA/DUPLICATE",
        ["PUBLIC_DISPATCHSCADA_202508121115_0000000475994495.zip"],
    )

    monkeypatch.setattr(extract_patterns, "MIRROR", mirror)
    monkeypatch.chdir(tmp_path)

    rc = extract_patterns.main()
    assert rc == 0

    # Assert on the flat CSV output — one row per
    # (repo, tier, intra_id, path_template, skeleton).
    import csv

    with (tmp_path / "reference" / "URL-CONVENTIONS.csv").open() as f:
        rows = list(csv.DictReader(f))

    path_templates_by_stream: dict[str, set[str]] = {}
    for r in rows:
        path_templates_by_stream.setdefault(r["intra_repo_id"], set()).add(r["path_template"])

    # Class (a): Dispatch_Reports must NOT have a DUPLICATE-pathed row.
    assert "/Reports/CURRENT/Dispatch_Reports/" in path_templates_by_stream["Dispatch_Reports"]
    assert not any("DUPLICATE" in p for p in path_templates_by_stream["Dispatch_Reports"]), (
        "class-(a) _LEGACY placeholders must be skipped"
    )

    # Class (b) multi-file: Trading_Cumulative_Price keeps both parent AND DUPLICATE path_templates.
    tcp_paths = path_templates_by_stream["Trading_Cumulative_Price"]
    assert "/Reports/CURRENT/Trading_Cumulative_Price/" in tcp_paths
    assert any("DUPLICATE" in p for p in tcp_paths), "class-(b) multi-file stragglers must be kept"

    # Class (b) single-file: Dispatch_SCADA keeps both parent AND DUPLICATE path_templates.
    # Pins the §2.1.1 correction — single-file non-LEGACY DUPLICATEs are NOT class-(a).
    scada_paths = path_templates_by_stream["Dispatch_SCADA"]
    assert "/Reports/CURRENT/Dispatch_SCADA/" in scada_paths
    assert any("DUPLICATE" in p for p in scada_paths), (
        "class-(b) single-file non-LEGACY stragglers must be kept "
        "(10 such dirs on real mirror; §2.1.1 2026-04-21 correction)"
    )

    # Class (c): GBB keeps the DUPLICATE path (PR #9 regression pin).
    gbb_paths = path_templates_by_stream["GBB"]
    assert any("DUPLICATE" in p for p in gbb_paths), (
        "class-(c) GBB rolling archive must be kept — "
        "unconditional skip regresses PR #9 (617 files lost)"
    )

    # Observability: guard emits a single-line summary to stderr.
    captured = capsys.readouterr()
    assert "Skipped 1 _LEGACY" in captured.err, (
        f"expected 'Skipped 1 _LEGACY' in stderr, got: {captured.err!r}"
    )
