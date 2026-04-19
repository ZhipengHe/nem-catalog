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
            "schema_version": "1.0.0",
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
        "schema_version": "1.0.0",
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
                    "T": {
                        "path_template": "/x/",
                        "filename_template": "x_{date}.zip",
                        "filename_regex": r"^x_\d{8}\.zip$",
                        "example": "x_20240101.zip",
                        "observed_range": None,
                    }
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
    prior_fail_count: int = 0,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(MERGE_SCRIPT),
            "--auto", str(auto_path),
            "--curated", str(curated_dir),
            "--out", str(out_path),
            "--prior-fail-count", str(prior_fail_count),
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
                    "CURRENT": {
                        "path_template": "/Reports/CURRENT/Foo/",
                        "filename_template": "foo_{date}.zip",
                        "filename_regex": r"^foo_\d{8}\.zip$",
                        "example": "foo_20240101.zip",
                        "cadence": "5min",
                        "observed_range": None,
                    }
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
                    "CURRENT": {
                        "path_template": "/Reports/CURRENT/Foo/",
                        "filename_template": "foo_{date}.zip",
                        "filename_regex": r"^foo_\d{8}\.zip$",
                        "example": "foo_20240101.zip",
                        "cadence": "5min",
                        "observed_range": None,
                    }
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
    assert "WARNING: field overlap" in r.stderr
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
                    "CURRENT": {
                        "path_template": "/Reports/CURRENT/Bar/",
                        "filename_template": "bar_{date}.zip",
                        "filename_regex": r"^bar_\d{8}\.zip$",
                        "example": "bar_20240101.zip",
                        "cadence": "5min",
                        "observed_range": None,
                    }
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
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Foo": {
                "repo": "Reports",
                "intra_repo_id": "Foo",
                "resolvable": True,
                "tiers": {
                    "CURRENT": {
                        "path_template": "/",
                        "filename_template": "x",
                        "filename_regex": "x",
                        "example": "",
                        "cadence": "5min",
                        "observed_range": None,
                    }
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    _write_curated(tmp_path, "reports", {"Reports:GhostDataset": {"anomaly_note": "stale"}})
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out, prior_fail_count=0)
    assert r.returncode == 0, r.stderr
    assert "ORPHAN CURATED KEY" in r.stderr
    assert "Reports:GhostDataset" in r.stderr


def test_orphan_curated_key_fails_on_second_consecutive(tmp_path: Path) -> None:
    auto = _write_auto(tmp_path, {})
    _write_curated(tmp_path, "reports", {"Reports:GhostDataset": {"anomaly_note": "still stale"}})
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out, prior_fail_count=1)
    assert r.returncode == 1
    assert "FAIL" in r.stderr


def test_merge_applies_mmsdm_default_schema_source(tmp_path: Path) -> None:
    auto = _write_auto(
        tmp_path,
        {
            "MMSDM:FOO": {
                "repo": "MMSDM",
                "intra_repo_id": "FOO",
                "resolvable": True,
                "tiers": {
                    "DATA": {
                        "path_template": "/",
                        "filename_template": "x",
                        "filename_regex": "x",
                        "example": "",
                        "cadence": "5min",
                        "observed_range": None,
                    }
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
                    "CURRENT": {
                        "path_template": "/Reports/CURRENT/Foo/",
                        "filename_template": "foo_{date}.zip",
                        "filename_regex": r"^foo_\d{8}\.zip$",
                        "example": "foo_20240101.zip",
                        "cadence": "5min",
                        "observed_range": None,
                    }
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
