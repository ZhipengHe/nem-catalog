"""Tests for --policy flag + walker policy dispatch in nemweb_download.py."""

from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(PROJECT / "scripts"))


def test_parse_args_accepts_policy_flag() -> None:
    import nemweb_download as mod

    gaps, force, policy_path, _threads, _max_fetches = mod.parse_args(["--policy", "foo.yaml"])
    assert policy_path == "foo.yaml"
    assert force is False
    assert gaps is False


def test_parse_args_without_policy_is_none() -> None:
    import nemweb_download as mod

    _gaps, _force, policy_path, _threads, _max_fetches = mod.parse_args([])
    assert policy_path is None


def test_parse_args_accepts_all_flags_together() -> None:
    import nemweb_download as mod

    gaps, _force, policy_path, threads, max_fetches = mod.parse_args(
        ["--gaps", "--policy", "p.yaml", "--threads=2", "100"]
    )
    assert gaps is True
    assert policy_path == "p.yaml"
    assert threads == 2
    assert max_fetches == 100


def test_process_one_skips_static_when_cached(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    from scripts.policy import Policy

    policy = Policy.load(_policy(tmp_path, "/Data_Archive/**", "static"))
    monkeypatch.setattr(mod, "OUT", tmp_path)
    cached = tmp_path / "Data_Archive/x/index.html"
    cached.parent.mkdir(parents=True)
    cached.write_bytes(b'<pre><A HREF="/a/">a</A></pre>')

    # Build a fake walker closure: we test the path directly via the code that
    # would be inside process_one, using the helpers the walker exposes.
    with patch.object(mod, "throttled_fetch") as fetch_mock:
        outcome = mod._process_one_for_test("/Data_Archive/x/", force=False, policy=policy)
    assert outcome[1] == "reuse"
    fetch_mock.assert_not_called()


def test_process_one_forces_rolling_when_cached(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    from scripts.policy import Policy

    policy = Policy.load(_policy(tmp_path, "/Reports/CURRENT/x/", "rolling"))
    monkeypatch.setattr(mod, "OUT", tmp_path)
    cached = tmp_path / "Reports/CURRENT/x/index.html"
    cached.parent.mkdir(parents=True)
    cached.write_bytes(b'<pre><A HREF="/a/">a</A></pre>')

    with patch.object(
        mod, "throttled_fetch", return_value=(b'<pre><A HREF="/a/">a</A></pre>', 200)
    ) as fetch_mock:
        outcome = mod._process_one_for_test("/Reports/CURRENT/x/", force=False, policy=policy)
    # Network fetch attempted despite cached file existing.
    fetch_mock.assert_called_once()
    # Outcome depends on whether content-aware write preserved or wrote;
    # either way it's NOT "reuse" (which means "short-circuited on cache").
    assert outcome[1] in {"fetch", "fetch_noop"}


def test_process_one_unclassified_refetches(tmp_path: Path, monkeypatch) -> None:
    """Unmatched paths are treated as force-refetch (conservative)."""
    import nemweb_download as mod

    from scripts.policy import Policy

    policy = Policy.load(_policy(tmp_path, "/other/", "rolling"))
    monkeypatch.setattr(mod, "OUT", tmp_path)
    cached = tmp_path / "unmatched/x/index.html"
    cached.parent.mkdir(parents=True)
    cached.write_bytes(b"<pre></pre>")

    with patch.object(mod, "throttled_fetch", return_value=(b"<pre></pre>", 200)) as fetch_mock:
        mod._process_one_for_test("/unmatched/x/", force=False, policy=policy)
    fetch_mock.assert_called_once()


def _policy(tmp_path: Path, pattern: str, cls: str) -> Path:
    p = tmp_path / "policy.yaml"
    p.write_text(
        "version: 1\nlast_reviewed: 2026-04-20\nreviewer: t\nrules:\n"
        f'  - pattern: "{pattern}"\n    class: {cls}\n'
    )
    return p
