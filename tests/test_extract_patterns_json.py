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
    assert data["schema_version"] == "1.0.0"
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
        for tier in rec["tiers"].values():
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


def _write_iis_listing(path: Path, hrefs: list[str]) -> None:
    """Write a minimal IIS-style index.html with the given file HREFs.

    Uses the HREF-only fallback format (picked up by HREF_ANY_RE in
    parse_listing). Sufficient for exercising walk + classify + write_json.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    body = b"<pre>"
    for h in hrefs:
        basename = h.rsplit("/", 1)[-1].encode("ascii")
        body += b'<A HREF="' + h.encode("ascii") + b'">' + basename + b"</A><br>"
    body += b"</pre>"
    path.write_bytes(body)


def test_main_skips_duplicate_subdir(tmp_path, monkeypatch):
    """Regression test for issue #5 primary (T5T6-I2).

    Before the DUPLICATE-filter fix, a dataset with files in both
    /Reports/CURRENT/X/ and /Reports/CURRENT/X/DUPLICATE/ classifies both
    paths to the same (repo, tier, intra_id) tuple; sort-order + write_json
    last-write-wins lets the DUPLICATE path overwrite the real-data path.
    Curated policy's /Reports/CURRENT/Dispatch_Reports/ -> rolling rule
    then fails to match, and the dataset classifies as unclassified.

    Uses the real curated policy file plus a real affected dataset name
    (Dispatch_Reports) under a synthetic mirror.
    """
    # --- Build synthetic mirror with Dispatch_Reports in both locations ---
    mirror = tmp_path / "nemweb-mirror"
    real_listing = mirror / "Reports" / "CURRENT" / "Dispatch_Reports" / "index.html"
    dup_listing = mirror / "Reports" / "CURRENT" / "Dispatch_Reports" / "DUPLICATE" / "index.html"

    _write_iis_listing(
        real_listing,
        [
            "/Reports/CURRENT/Dispatch_Reports/PUBLIC_DISPATCH_202604200000_0000000000000001_LEGACY.zip",
            "/Reports/CURRENT/Dispatch_Reports/PUBLIC_DISPATCH_202604200005_0000000000000002_LEGACY.zip",
            "/Reports/CURRENT/Dispatch_Reports/PUBLIC_DISPATCH_202604200010_0000000000000003_LEGACY.zip",
        ],
    )
    _write_iis_listing(
        dup_listing,
        [
            "/Reports/CURRENT/Dispatch_Reports/DUPLICATE/PUBLIC_DISPATCH_202604180000_0000000000000000_LEGACY.zip",
        ],
    )

    # --- Use the REAL curated policy (per D2 "under the curated policy") ---
    from scripts.policy import Policy

    curated_policy_path = REPO_ROOT / "patterns" / "curated" / "freshness-policy.yaml"
    assert curated_policy_path.exists(), (
        f"curated policy not found at {curated_policy_path}; the test depends on it"
    )
    policy = Policy.load(curated_policy_path)

    # --- Redirect all main() writes into tmp_path ---
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(extract_patterns, "MIRROR", mirror)
    monkeypatch.setattr(extract_patterns, "OUT_MD", Path("reference") / "URL-CONVENTIONS.md")
    monkeypatch.setattr(extract_patterns, "OUT_CSV", Path("reference") / "URL-CONVENTIONS.csv")

    rc = extract_patterns.main(policy=policy)
    assert rc == 0, f"extract_patterns.main returned non-zero: {rc}"

    # --- Inspect the emitted catalog ---
    catalog_path = tmp_path / "patterns" / "auto" / "catalog.json"
    assert catalog_path.exists(), f"catalog not written at {catalog_path}"
    catalog = json.loads(catalog_path.read_text())

    key = "Reports:Dispatch_Reports"
    assert key in catalog["datasets"], f"{key} missing; keys = {sorted(catalog['datasets'].keys())}"
    ds = catalog["datasets"][key]
    tiers = ds["tiers"]
    assert "CURRENT" in tiers, f"CURRENT tier missing; tiers = {list(tiers.keys())}"

    path_template = tiers["CURRENT"]["path_template"]
    freshness_class = ds.get("freshness_class")

    # D2 assertion 1: path_template does NOT contain /DUPLICATE/
    assert "/DUPLICATE/" not in path_template, (
        f"Regression: path_template still contains /DUPLICATE/: {path_template!r}. "
        "T5T6-I2 fix did not prevent the dedup-subdir from winning the sort-order "
        "overwrite."
    )

    # D2 assertion 2: path_template is the real-data parent path
    assert path_template == "/Reports/CURRENT/Dispatch_Reports/", (
        f"path_template was {path_template!r}, expected '/Reports/CURRENT/Dispatch_Reports/'"
    )

    # D2 assertion 3: dataset classifies as rolling under the curated policy
    # (freshness_class lives at DATASET root, not under the tier; see
    # scripts/extract_patterns.py:875-892)
    assert freshness_class == "rolling", (
        f"freshness_class was {freshness_class!r}, expected 'rolling'. "
        "The curated policy's /Reports/CURRENT/Dispatch_Reports/ -> rolling rule "
        "should have matched."
    )
