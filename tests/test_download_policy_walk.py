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


# --- EXT-1: bounds-checking tests ---


def test_parse_args_policy_missing_value() -> None:
    """--policy with no following argument must raise SystemExit."""
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit):
        mod.parse_args(["--policy"])


def test_parse_args_policy_empty_string() -> None:
    """--policy "" (empty value) must raise SystemExit."""
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit):
        mod.parse_args(["--policy", ""])


def test_parse_args_policy_equals_empty() -> None:
    """--policy= (empty via = form) must raise SystemExit."""
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit):
        mod.parse_args(["--policy="])


def test_parse_args_threads_missing_value() -> None:
    """--threads with no following argument must raise SystemExit."""
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit):
        mod.parse_args(["--threads"])


def test_parse_args_threads_equals_empty() -> None:
    """--threads= (explicit empty RHS) must fail with the same 'requires a value'
    message used for bare --threads, not the 'positive integer' path. PR #19 review.
    """
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit) as exc_info:
        mod.parse_args(["--threads="])
    assert "requires a value" in str(exc_info.value)


def test_parse_args_threads_non_integer() -> None:
    """--threads abc must raise SystemExit with message about invalid integer."""
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit) as exc_info:
        mod.parse_args(["--threads", "abc"])
    assert "--threads" in str(exc_info.value)
    assert "abc" in str(exc_info.value)


def test_parse_args_threads_zero() -> None:
    """--threads 0 must raise SystemExit (must be >= 1)."""
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit) as exc_info:
        mod.parse_args(["--threads", "0"])
    assert "--threads" in str(exc_info.value)
    assert "0" in str(exc_info.value)


def test_parse_args_threads_negative() -> None:
    """--threads -5 must raise SystemExit (must be >= 1)."""
    import nemweb_download as mod
    import pytest

    with pytest.raises(SystemExit) as exc_info:
        mod.parse_args(["--threads", "-5"])
    assert "--threads" in str(exc_info.value)
    assert "-5" in str(exc_info.value)


def test_parse_args_happy_path_full_argv() -> None:
    """Full happy-path argv must parse correctly (acceptance criterion 8)."""
    import nemweb_download as mod

    gaps, _force, policy_path, threads, max_fetches = mod.parse_args(
        ["--policy", "foo.yaml", "--threads", "4", "--gaps", "5000"]
    )
    assert policy_path == "foo.yaml"
    assert threads == 4
    assert gaps is True
    assert max_fetches == 5000


def test_main_exits_2_on_policy_load_error(tmp_path: Path, monkeypatch, capsys) -> None:
    """main() must return 2 and print an 'ERROR: policy load failed:' prefix when
    Policy.load raises PolicyLoadError (e.g. version != 1 triggers the POL-1 guard)."""
    import nemweb_download as mod

    bad_policy = tmp_path / "bad_policy.yaml"
    bad_policy.write_text(
        "version: 2\nlast_reviewed: 2026-04-21\nreviewer: t\nrules:\n"
        '  - pattern: "/foo/**"\n    class: rolling\n'
    )
    monkeypatch.setattr(mod, "OUT", tmp_path)

    result = mod.main(["--policy", str(bad_policy), "1"])

    assert result == 2
    captured = capsys.readouterr()
    assert "ERROR: policy load failed:" in captured.err


def test_main_exits_2_on_href_extraction_shift_error(tmp_path: Path, monkeypatch, capsys) -> None:
    """main() must return 2 and print an 'ERROR:' prefix when walk() raises
    HREFExtractionShiftError.  walk() is monkey-patched to raise directly since
    triggering the real template-shift path requires a full HTTP mock + cached file
    and is out of scope for this contract-pinning test."""
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    monkeypatch.setattr(
        mod,
        "walk",
        lambda *args, **kwargs: (_ for _ in ()).throw(
            mod.HREFExtractionShiftError("/test/path/", before=10, after=0)
        ),
    )

    result = mod.main(["1"])

    assert result == 2
    captured = capsys.readouterr()
    assert "ERROR:" in captured.err


def _policy(tmp_path: Path, pattern: str, cls: str) -> Path:
    p = tmp_path / "policy.yaml"
    p.write_text(
        "version: 1\nlast_reviewed: 2026-04-20\nreviewer: t\nrules:\n"
        f'  - pattern: "{pattern}"\n    class: {cls}\n'
    )
    return p


# --- EXT-3: walk() fetch vs fetch_noop distinction ---


def test_walk_emits_fetch_when_mtime_changes(tmp_path: Path, monkeypatch) -> None:
    """walk() must return outcome 'fetch' when save_listing writes new content (mtime changes)."""
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)

    seed = "/Reports/NEW/"
    # No pre-existing cached file → mtime will change from None to something.
    html = b"<pre></pre>"
    with patch.object(mod, "throttled_fetch", return_value=(html, 200)):
        result = mod.walk([seed], threads=1, max_fetches=10)

    # New 4-tuple: (fetched, fetched_noop, reused, skipped)
    assert len(result) == 4
    fetched, fetched_noop, _reused, _skipped = result
    assert fetched == 1
    assert fetched_noop == 0


def test_walk_emits_fetch_noop_when_mtime_unchanged(tmp_path: Path, monkeypatch) -> None:
    """walk() must return 'fetch_noop' when save_listing short-circuits on identical content."""
    import nemweb_download as mod

    from scripts.policy import Policy

    # Use a rolling policy so the walker refetches despite cache.
    policy = Policy.load(_policy(tmp_path, "/Reports/**", "rolling"))
    monkeypatch.setattr(mod, "OUT", tmp_path)

    seed = "/Reports/CURRENT/x/"
    # Empty listing — no child links, so no wave 2 fetches.
    html = b"<pre></pre>"

    # Pre-populate the cached file with the same bytes that the server will return.
    cached = tmp_path / "Reports/CURRENT/x/index.html"
    cached.parent.mkdir(parents=True)
    cached.write_bytes(html)

    with patch.object(mod, "throttled_fetch", return_value=(html, 200)):
        result = mod.walk([seed], threads=1, max_fetches=10, policy=policy)

    assert len(result) == 4
    fetched, fetched_noop, _reused, _skipped = result
    # save_listing's content-identical short-circuit keeps mtime unchanged;
    # if that dedup is ever removed, this flips to fetched=1, fetched_noop=0.
    assert fetched_noop == 1
    assert fetched == 0
