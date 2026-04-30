"""Tests for scripts/merge_catalog.py — the auto + curated merge step."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).parent.parent
MERGE_SCRIPT = REPO_ROOT / "scripts" / "merge_catalog.py"


def _write(path: Path, data: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))
    return path


def _write_auto(tmp_path: Path, datasets: dict[str, Any]) -> Path:
    return _write(
        tmp_path / "auto-catalog.json",
        {
            "schema_version": "2.0.0",
            "catalog_version": "2026.04.18",
            "as_of": "2026-04-18T00:00:00Z",
            "source_mirror_commit": "deadbee",
            "placeholders": {},
            "dataset_keys": list(datasets.keys()),
            "raw_keys": list(datasets.keys()),
            "datasets": datasets,
        },
    )


def _write_curated(tmp_path: Path, name: str, content: dict[str, Any]) -> Path:
    p = tmp_path / "curated" / f"{name}.yaml"
    p.parent.mkdir(exist_ok=True)
    p.write_text(yaml.safe_dump(content))
    return p


def _minimal_auto_with_key(key: str) -> dict[str, Any]:
    repo, intra_repo_id = key.split(":", 1)
    return {
        "schema_version": "2.0.0",
        "catalog_version": "2026.04.18",
        "as_of": "2026-04-18T00:00:00Z",
        "placeholders": {},
        "dataset_keys": [key],
        "raw_keys": [key],
        "datasets": {
            key: {
                "repo": repo,
                "intra_repo_id": intra_repo_id,
                "resolvable": True,
                "tiers": {
                    "T": [
                        {
                            "path_template": "/x/",
                            "filename_template": "x_{date}.zip",
                            "filename_regex": r"^x_\d{8}\.zip$",
                            "example": "x_20240101.zip",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    }


def _run_merge(
    auto_path: Path,
    curated_dir: Path,
    out_path: Path,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(MERGE_SCRIPT),
            "--auto",
            str(auto_path),
            "--curated",
            str(curated_dir),
            "--out",
            str(out_path),
        ],
        capture_output=True,
        text=True,
    )


def test_curated_only_field_accepted(tmp_path: Path) -> None:
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Foo": {
                "repo": "Reports",
                "intra_repo_id": "Foo",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/Reports/CURRENT/Foo/",
                            "filename_template": "foo_{date}.zip",
                            "filename_regex": r"^foo_\d{8}\.zip$",
                            "example": "foo_20240101.zip",
                            "cadence": "5min",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    _write_curated(tmp_path, "reports", {"Reports:Foo": {"anomaly_note": "Curated note here."}})
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0, r.stderr
    data = json.loads(out.read_text())
    assert data["datasets"]["Reports:Foo"]["anomaly_note"] == "Curated note here."


def test_field_overlap_curated_wins_with_warning(tmp_path: Path) -> None:
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Foo": {
                "repo": "Reports",
                "intra_repo_id": "Foo",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/Reports/CURRENT/Foo/",
                            "filename_template": "foo_{date}.zip",
                            "filename_regex": r"^foo_\d{8}\.zip$",
                            "example": "foo_20240101.zip",
                            "cadence": "5min",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": "Auto-derived note",
            }
        },
    )
    _write_curated(tmp_path, "reports", {"Reports:Foo": {"anomaly_note": "Curated override"}})
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0
    data = json.loads(out.read_text())
    assert data["datasets"]["Reports:Foo"]["anomaly_note"] == "Curated override"
    assert "WARNING:" in r.stderr
    assert "Reports:Foo.anomaly_note" in r.stderr


def test_auto_only_dataset_key_passes_through(tmp_path: Path) -> None:
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Bar": {
                "repo": "Reports",
                "intra_repo_id": "Bar",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/Reports/CURRENT/Bar/",
                            "filename_template": "bar_{date}.zip",
                            "filename_regex": r"^bar_\d{8}\.zip$",
                            "example": "bar_20240101.zip",
                            "cadence": "5min",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    (tmp_path / "curated").mkdir(exist_ok=True)
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0
    data = json.loads(out.read_text())
    assert "Reports:Bar" in data["datasets"]


def test_orphan_curated_key_warns_on_first_occurrence(tmp_path: Path) -> None:
    """B2: orphan override → fail immediately (no 2-run tolerance)."""
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Foo": {
                "repo": "Reports",
                "intra_repo_id": "Foo",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/",
                            "filename_template": "x",
                            "filename_regex": "x",
                            "example": "",
                            "cadence": "5min",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    _write_curated(tmp_path, "reports", {"Reports:GhostDataset": {"anomaly_note": "stale"}})
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode != 0
    assert "ORPHAN CURATED KEY" in r.stderr
    assert "Reports:GhostDataset" in r.stderr


def test_orphan_curated_key_fails_on_second_consecutive(tmp_path: Path) -> None:
    """B2: orphan override fails immediately regardless of prior runs."""
    auto = _write_auto(tmp_path, {})
    _write_curated(tmp_path, "reports", {"Reports:GhostDataset": {"anomaly_note": "still stale"}})
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 1
    assert "ORPHAN CURATED KEY" in r.stderr


def test_merge_applies_mmsdm_default_schema_source(tmp_path: Path) -> None:
    auto = _write_auto(
        tmp_path,
        {
            "MMSDM:FOO": {
                "repo": "MMSDM",
                "intra_repo_id": "FOO",
                "resolvable": True,
                "tiers": {
                    "DATA": [
                        {
                            "path_template": "/",
                            "filename_template": "x",
                            "filename_regex": "x",
                            "example": "",
                            "cadence": "5min",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    _write_curated(
        tmp_path,
        "mmsdm",
        {"__default__": {"schema_source": "https://tech-specs.docs.public.aemo.com.au/"}},
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0
    data = json.loads(out.read_text())
    assert data["datasets"]["MMSDM:FOO"]["schema_source"] == (
        "https://tech-specs.docs.public.aemo.com.au/"
    )


def test_merge_validates_output_against_schema(tmp_path: Path) -> None:
    """The merge script must validate its output against catalog.schema.json before writing."""
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Foo": {
                "repo": "Reports",
                "intra_repo_id": "Foo",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/Reports/CURRENT/Foo/",
                            "filename_template": "foo_{date}.zip",
                            "filename_regex": r"^foo_\d{8}\.zip$",
                            "example": "foo_20240101.zip",
                            "cadence": "5min",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    (tmp_path / "curated").mkdir(exist_ok=True)
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0
    assert "schema validation: OK" in r.stdout


def test_empty_auto_produces_valid_empty_catalog(tmp_path: Path) -> None:
    """Test plan line 59: empty patterns/auto/ → merge exits cleanly with warning
    and produces a valid-but-empty catalog.json that still validates against schema."""
    auto = _write(
        tmp_path / "auto.json",
        {
            "schema_version": "1.0.0",
            "catalog_version": "2026.04.18",
            "as_of": "2026-04-18T00:00:00Z",
            "placeholders": {},
            "dataset_keys": [],
            "raw_keys": [],
            "datasets": {},
        },
    )
    (tmp_path / "curated").mkdir(exist_ok=True)
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0, f"empty-auto merge must succeed, got {r.returncode}: {r.stderr}"
    assert "empty catalog" in r.stdout.lower(), "expected explicit empty-catalog warning"
    data = json.loads(out.read_text())
    assert data["datasets"] == {}
    assert data["dataset_keys"] == []
    assert "schema validation: OK" in r.stdout


def test_duplicate_curated_key_across_files_fails(tmp_path: Path) -> None:
    """Test plan line 60: duplicate dataset key across two curated YAMLs → merge
    exits 1 identifying both file locations."""
    auto = _write(tmp_path / "auto.json", _minimal_auto_with_key("Reports:Foo"))
    curated = tmp_path / "curated"
    curated.mkdir()
    (curated / "a.yaml").write_text("Reports:Foo:\n  anomaly_note: first\n")
    (curated / "b.yaml").write_text("Reports:Foo:\n  anomaly_note: second\n")
    r = _run_merge(auto, curated, tmp_path / "catalog.json")
    assert r.returncode == 1
    assert "duplicate curated key" in r.stderr.lower()
    assert "a.yaml" in r.stderr and "b.yaml" in r.stderr


def test_curated_only_inserts_placeholder_entry(tmp_path: Path) -> None:
    """B2: curated_only: true entries insert into catalog without needing an auto base."""
    auto = _write_auto(tmp_path, {})  # empty auto catalog
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:FakePlaceholder": {
                "curated_only": True,
                "resolvable": False,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/Reports/ARCHIVE/FakePlaceholder/",
                        "filename_template": None,
                        "filename_regex": None,
                        "example": "",
                        "cadence": "none",
                        "observed_range": None,
                    }
                },
                "anomaly_note": "Empty directory on AEMO; fixture test.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0, r.stderr
    data = json.loads(out.read_text())
    assert "Reports:FakePlaceholder" in data["datasets"]
    ds = data["datasets"]["Reports:FakePlaceholder"]
    assert ds["repo"] == "Reports"
    assert ds["intra_repo_id"] == "FakePlaceholder"
    assert ds["resolvable"] is False
    assert "curated_only" not in ds, (
        "curated_only is a YAML-layer marker; must not leak into catalog.json"
    )
    assert "Reports:FakePlaceholder" in data["raw_keys"], (
        "placeholder must be discoverable via raw_keys"
    )
    assert "Reports:FakePlaceholder" not in data["dataset_keys"], (
        "resolvable=false placeholders are intentionally excluded from dataset_keys (user-facing list)"  # noqa: E501
    )


def test_curated_only_with_conflicting_repo_field_fails(tmp_path: Path) -> None:
    """Regression for Copilot PR #1 review: a curated_only entry that explicitly
    sets a `repo` field different from the key must fail loudly. Pre-fix, the
    insert used `setdefault`, so a typo silently kept the YAML value and produced
    an inconsistent record (key says one thing, fields say another).
    """
    auto = _write_auto(tmp_path, {})
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:Conflicty": {
                "curated_only": True,
                "repo": "MMSDM",  # WRONG — key says Reports
                "resolvable": False,
                "tiers": {},
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode != 0
    assert "conflicting repo" in r.stderr.lower(), r.stderr


def test_curated_only_with_conflicting_intra_repo_id_fails(tmp_path: Path) -> None:
    """Same regression for the intra_repo_id field."""
    auto = _write_auto(tmp_path, {})
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:RealName": {
                "curated_only": True,
                "intra_repo_id": "WrongName",  # WRONG — key says RealName
                "resolvable": False,
                "tiers": {},
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode != 0
    assert "conflicting intra_repo_id" in r.stderr.lower(), r.stderr


def test_override_missing_auto_key_fails_immediately(tmp_path: Path) -> None:
    """B2: unmarked curated entry (override) whose key is not in auto catalog → FAIL on
    first run. No --prior-fail-count tolerance. This replaces the pre-B2 2-run counter.
    """
    auto = _write_auto(tmp_path, {})  # empty auto
    _write_curated(
        tmp_path,
        "reports",
        {
            # No curated_only → treated as override
            "Reports:DeletedByAemo": {
                "anomaly_note": "We used to override this but AEMO removed the dir.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode != 0, "override for missing auto key must fail"
    assert "ORPHAN" in r.stderr or "AEMO deletion" in r.stderr
    assert not out.exists(), "failed merge must not write catalog.json"


def test_curated_only_shadows_auto_emits_warning(tmp_path: Path) -> None:
    """B2: curated_only: true for a key that ALSO exists in auto → curated wins, but
    emit a warning so maintainers notice the unusual overlap."""
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Collision": {
                "repo": "Reports",
                "intra_repo_id": "Collision",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/Reports/CURRENT/Collision/",
                            "filename_template": "collision_{date}.zip",
                            "filename_regex": r"^collision_\d{8}\.zip$",
                            "example": "collision_20240101.zip",
                            "cadence": "5min",
                            "observed_range": None,
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:Collision": {
                "curated_only": True,
                "resolvable": False,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/Reports/ARCHIVE/Collision/",
                        "filename_template": None,
                        "filename_regex": None,
                        "example": "",
                        "cadence": "none",
                        "observed_range": None,
                    }
                },
                "anomaly_note": "Curated wins here.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0, r.stderr
    assert "shadows" in r.stderr.lower() or "curated_only" in r.stderr.lower(), (
        "must warn when curated_only entry overwrites an auto record"
    )
    data = json.loads(out.read_text())
    ds = data["datasets"]["Reports:Collision"]
    assert ds["resolvable"] is False  # curated won
    assert list(ds["tiers"].keys()) == ["ARCHIVE"]  # auto's CURRENT tier is replaced


def test_curated_only_without_tiers_fails_schema_validation(tmp_path: Path) -> None:
    """B2: curated_only: true entries must declare tiers (schema requires it).
    If YAML omits tiers, the inserted record fails validate() → SystemExit(1).
    """
    auto = _write_auto(tmp_path, {})
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:BrokenPlaceholder": {
                "curated_only": True,
                "resolvable": False,
                # Intentionally no tiers — should fail schema validation
                "anomaly_note": "Oops, forgot tiers.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode != 0, "malformed curated_only entry must fail"
    # The schema validator reports the missing required field:
    assert "tiers" in r.stderr


def test_last_crawl_fields_from_env(tmp_path, monkeypatch):
    """merge() copies LAST_CRAWL_ATTEMPTED_AT/COMPLETED_AT env vars into catalog."""
    from scripts.merge_catalog import merge

    auto = {
        "schema_version": "1.0.0",
        "catalog_version": "2026.04.20",
        "as_of": "2026-04-20T03:00:00Z",
        "source_mirror_commit": "abcd1234",
        "placeholders": {},
        "dataset_keys": [],
        "raw_keys": [],
        "datasets": {},
    }
    monkeypatch.setenv("LAST_CRAWL_ATTEMPTED_AT", "2026-04-20T03:00:00Z")
    monkeypatch.setenv("LAST_CRAWL_COMPLETED_AT", "2026-04-20T03:05:00Z")

    merged = merge(auto, overlays={}, defaults={})
    assert merged["last_crawl_attempted_at"] == "2026-04-20T03:00:00Z"
    assert merged["last_crawl_completed_at"] == "2026-04-20T03:05:00Z"


def test_last_crawl_fields_absent_when_env_unset(tmp_path, monkeypatch):
    from scripts.merge_catalog import merge

    auto = {
        "schema_version": "1.0.0",
        "catalog_version": "2026.04.20",
        "as_of": "2026-04-20T03:00:00Z",
        "source_mirror_commit": "abcd1234",
        "placeholders": {},
        "dataset_keys": [],
        "raw_keys": [],
        "datasets": {},
    }
    monkeypatch.delenv("LAST_CRAWL_ATTEMPTED_AT", raising=False)
    monkeypatch.delenv("LAST_CRAWL_COMPLETED_AT", raising=False)

    merged = merge(auto, overlays={}, defaults={})
    assert "last_crawl_attempted_at" not in merged
    assert "last_crawl_completed_at" not in merged


def test_merge_tiers_broadcasts_curated_field_to_all_records(tmp_path) -> None:
    """Task 5: RED test for merge-layer array adaptation.

    When auto has tiers["CURRENT"] = [rec1, rec2], and curated overlay sets
    tiers.CURRENT.retention_hint_unverified_days = 2, the merged output must
    have retention_hint_unverified_days == 2 on BOTH records.
    """
    from scripts.merge_catalog import merge

    auto = {
        "schema_version": "2.0.0",
        "catalog_version": "2026.04.28",
        "as_of": "2026-04-28T00:00:00Z",
        "source_mirror_commit": "abc1234",
        "placeholders": {},
        "dataset_keys": ["Reports:Test_Dataset"],
        "raw_keys": ["Reports:Test_Dataset"],
        "datasets": {
            "Reports:Test_Dataset": {
                "repo": "Reports",
                "intra_repo_id": "Test_Dataset",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/path/",
                            "filename_template": "FILE_A_{date}.zip",
                            "filename_regex": ".*",
                            "example": "FILE_A_20250101.zip",
                            "cadence": "5min",
                        },
                        {
                            "path_template": "/path/",
                            "filename_template": "FILE_B_{date}.zip",
                            "filename_regex": ".*",
                            "example": "FILE_B_20250101.zip",
                            "cadence": "5min",
                        },
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    }
    overlays = {
        "Reports:Test_Dataset": {"tiers": {"CURRENT": {"retention_hint_unverified_days": 2}}}
    }

    merged = merge(auto, overlays, {})

    # Both records should have the curated field broadcast to them
    current_tier = merged["datasets"]["Reports:Test_Dataset"]["tiers"]["CURRENT"]
    assert isinstance(current_tier, list), "CURRENT tier should be a list"
    assert len(current_tier) == 2, "CURRENT tier should have 2 records"
    assert current_tier[0]["retention_hint_unverified_days"] == 2
    assert current_tier[1]["retention_hint_unverified_days"] == 2


def test_merge_tiers_curated_only_tier_wraps_in_list(tmp_path) -> None:
    """Task 5: RED test for merge-layer array adaptation.

    When curated YAML provides a tiers.NEW_TIER: {…} entry that auto doesn't
    have, the merged tiers["NEW_TIER"] must be [curated_dict] (list, not dict).
    """
    from scripts.merge_catalog import merge

    auto = {
        "schema_version": "2.0.0",
        "catalog_version": "2026.04.28",
        "as_of": "2026-04-28T00:00:00Z",
        "source_mirror_commit": "abc1234",
        "placeholders": {},
        "dataset_keys": ["Reports:Test_Dataset"],
        "raw_keys": ["Reports:Test_Dataset"],
        "datasets": {
            "Reports:Test_Dataset": {
                "repo": "Reports",
                "intra_repo_id": "Test_Dataset",
                "resolvable": True,
                "tiers": {
                    "CURRENT": [
                        {
                            "path_template": "/path/",
                            "filename_template": "FILE_{date}.zip",
                            "filename_regex": ".*",
                            "example": "FILE_20250101.zip",
                            "cadence": "5min",
                        }
                    ]
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    }
    overlays = {
        "Reports:Test_Dataset": {
            "tiers": {
                "NEW_TIER": {
                    "path_template": "/new/",
                    "filename_template": "NEW_{date}.zip",
                    "filename_regex": "NEW_.*",
                    "example": "NEW_20250101.zip",
                    "cadence": "daily",
                }
            }
        }
    }

    merged = merge(auto, overlays, {})

    # NEW_TIER should exist and be a list with 1 element
    new_tier = merged["datasets"]["Reports:Test_Dataset"]["tiers"]["NEW_TIER"]
    assert isinstance(new_tier, list), "NEW_TIER should be a list"
    assert len(new_tier) == 1, "NEW_TIER should be a 1-element list"
    assert new_tier[0]["path_template"] == "/new/"
    assert new_tier[0]["filename_template"] == "NEW_{date}.zip"


def test_insert_curated_only_wraps_each_tier_dict(tmp_path) -> None:
    """Task 5: RED test for merge-layer array adaptation.

    When curated_only entry has tiers.ARCHIVE: {path_template: …, …},
    the merged tiers["ARCHIVE"] must be [the_dict] (wrapped in list).
    """
    from scripts.merge_catalog import merge

    auto = {
        "schema_version": "2.0.0",
        "catalog_version": "2026.04.28",
        "as_of": "2026-04-28T00:00:00Z",
        "source_mirror_commit": "abc1234",
        "placeholders": {},
        "dataset_keys": [],
        "raw_keys": [],
        "datasets": {},
    }
    overlays = {
        "Reports:FakePlaceholder": {
            "curated_only": True,
            "resolvable": False,
            "tiers": {
                "ARCHIVE": {
                    "path_template": "/Reports/ARCHIVE/FakePlaceholder/",
                    "filename_template": None,
                    "filename_regex": None,
                    "example": "",
                    "cadence": "none",
                }
            },
            "anomaly_note": "Placeholder entry for testing.",
        }
    }

    merged = merge(auto, overlays, {})

    # ARCHIVE tier in the curated_only record should be a list
    archive_tier = merged["datasets"]["Reports:FakePlaceholder"]["tiers"]["ARCHIVE"]
    assert isinstance(archive_tier, list), "ARCHIVE tier should be a list"
    assert len(archive_tier) == 1, "ARCHIVE tier should be a 1-element list"
    assert archive_tier[0]["path_template"] == "/Reports/ARCHIVE/FakePlaceholder/"
    assert archive_tier[0]["filename_template"] is None
