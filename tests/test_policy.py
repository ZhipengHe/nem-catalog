"""Tests for scripts/policy.py: freshness-policy loader + matcher."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.policy import Policy, PolicyLoadError


def _write(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "freshness-policy.yaml"
    p.write_text(body)
    return p


def test_load_minimal_valid(tmp_path: Path) -> None:
    policy = Policy.load(
        _write(
            tmp_path,
            "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
            '  - pattern: "/Reports/**"\n    class: rolling\n',
        )
    )
    assert policy.version == 1
    assert len(policy.rules) == 1


def test_class_for_exact_match(tmp_path: Path) -> None:
    policy = Policy.load(
        _write(
            tmp_path,
            "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
            '  - pattern: "/Reports/CURRENT/Dispatch_Reports/"\n    class: rolling\n',
        )
    )
    assert policy.class_for("/Reports/CURRENT/Dispatch_Reports/") == "rolling"


def test_class_for_unmatched_returns_unclassified(tmp_path: Path) -> None:
    policy = Policy.load(
        _write(
            tmp_path,
            "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
            '  - pattern: "/Reports/CURRENT/**"\n    class: rolling\n',
        )
    )
    assert policy.class_for("/Data_Archive/x/") == "unclassified"


def test_longest_match_wins(tmp_path: Path) -> None:
    policy = Policy.load(
        _write(
            tmp_path,
            "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
            '  - pattern: "/Data_Archive/**"\n    class: static\n'
            '  - pattern: "/Data_Archive/Wholesale_Electricity/MMSDM/*/"\n'
            "    class: parent_index\n",
        )
    )
    assert policy.class_for("/Data_Archive/Wholesale_Electricity/MMSDM/2026/") == "parent_index"
    assert (
        policy.class_for(
            "/Data_Archive/Wholesale_Electricity/MMSDM/2026/MMSDM_2026_01/"
            "MMSDM_Historical_Data_SQLLoader/"
        )
        == "static"
    )


def test_star_matches_one_segment(tmp_path: Path) -> None:
    policy = Policy.load(
        _write(
            tmp_path,
            "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
            '  - pattern: "/Data_Archive/Wholesale_Electricity/MMSDM/*/"\n'
            "    class: parent_index\n",
        )
    )
    # single-segment `*` matches `2026`
    assert policy.class_for("/Data_Archive/Wholesale_Electricity/MMSDM/2026/") == "parent_index"
    # does not match a deeper path
    assert (
        policy.class_for("/Data_Archive/Wholesale_Electricity/MMSDM/2026/MMSDM_2026_01/")
        == "unclassified"
    )


def test_double_star_matches_zero_or_more_segments(tmp_path: Path) -> None:
    policy = Policy.load(
        _write(
            tmp_path,
            "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
            '  - pattern: "/Reports/ARCHIVE/**"\n    class: append_only\n',
        )
    )
    assert policy.class_for("/Reports/ARCHIVE/") == "append_only"
    assert policy.class_for("/Reports/ARCHIVE/DISPATCHFCST/") == "append_only"
    assert policy.class_for("/Reports/ARCHIVE/DISPATCHFCST/sub/") == "append_only"


def test_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError):
        Policy.load(tmp_path / "does-not-exist.yaml")


def test_malformed_yaml_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError):
        Policy.load(_write(tmp_path, "version: 1\n  rules:\n not yaml ["))


def test_missing_rules_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError):
        Policy.load(_write(tmp_path, "version: 1\nreviewer: x\n"))


def test_unknown_class_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError):
        Policy.load(
            _write(
                tmp_path,
                "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
                '  - pattern: "/x/"\n    class: bogus_class\n',
            )
        )


def test_pattern_without_leading_slash_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError):
        Policy.load(
            _write(
                tmp_path,
                "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
                '  - pattern: "Reports/"\n    class: rolling\n',
            )
        )


def test_version_0_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError, match="unsupported policy version 0"):
        Policy.load(
            _write(
                tmp_path,
                "version: 0\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
                '  - pattern: "/Reports/**"\n    class: rolling\n',
            )
        )


def test_version_2_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError, match="unsupported policy version 2"):
        Policy.load(
            _write(
                tmp_path,
                "version: 2\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
                '  - pattern: "/Reports/**"\n    class: rolling\n',
            )
        )


def test_missing_version_raises(tmp_path: Path) -> None:
    with pytest.raises(PolicyLoadError, match="unsupported policy version 0"):
        Policy.load(
            _write(
                tmp_path,
                "last_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
                '  - pattern: "/Reports/**"\n    class: rolling\n',
            )
        )


def test_data_archive_bare_path_is_parent_index_not_static(tmp_path: Path) -> None:
    """Pins the fix for the /Data_Archive/** shadow bug.

    The static catchall must not shadow the bare /Data_Archive/ parent_index
    rule; otherwise the walker skips the bare index and cannot discover a new
    top-level sibling of Wholesale_Electricity. Fix: static catchall is
    /Data_Archive/*/** which requires at least one segment.
    """
    policy = Policy.load(
        _write(
            tmp_path,
            "version: 1\nlast_reviewed: 2026-04-20\nreviewer: x\nrules:\n"
            '  - pattern: "/Data_Archive/"\n    class: parent_index\n'
            '  - pattern: "/Data_Archive/*/**"\n    class: static\n',
        )
    )
    # Bare parent index must win.
    assert policy.class_for("/Data_Archive/") == "parent_index"
    # Deep archive paths still classify as static.
    assert (
        policy.class_for("/Data_Archive/Wholesale_Electricity/MMSDM/2015/MMSDM_2015_01/")
        == "static"
    )
