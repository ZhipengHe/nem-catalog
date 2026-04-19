"""Tests for nemweb_download.save_listing: content-aware write + template-shift guard."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# scripts/nemweb_download.py uses relative paths; tests need the project root
# on sys.path so `import nemweb_download` works.
PROJECT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT / "scripts"))


def test_skips_write_when_hrefs_unchanged(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    idx = tmp_path / "Reports/CURRENT/x/index.html"
    idx.parent.mkdir(parents=True)
    original = b'<html><body><pre><A HREF="/a/">a</A><br><A HREF="/b/">b</A></pre></body></html>'
    idx.write_bytes(original)
    idx_mtime = idx.stat().st_mtime_ns

    # Same HREF set, different bytes (AEMO re-rendered mtime in another column).
    refetched = (
        b'<html><body><pre>Monday  <A HREF="/a/">a</A><br><A HREF="/b/">b</A></pre></body></html>'
    )
    mod.save_listing("/Reports/CURRENT/x/", refetched)

    assert idx.read_bytes() == original, "write should be skipped when HREFs unchanged"
    assert idx.stat().st_mtime_ns == idx_mtime


def test_writes_when_hrefs_change(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    idx = tmp_path / "Reports/CURRENT/x/index.html"
    idx.parent.mkdir(parents=True)
    idx.write_bytes(b'<pre><A HREF="/a/">a</A></pre>')

    refetched = b'<pre><A HREF="/a/">a</A><br><A HREF="/new/">new</A></pre>'
    mod.save_listing("/Reports/CURRENT/x/", refetched)

    assert idx.read_bytes() == refetched


def test_writes_when_no_cached_file(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    data = b'<pre><A HREF="/a/">a</A></pre>'
    mod.save_listing("/Reports/CURRENT/x/", data)

    assert (tmp_path / "Reports/CURRENT/x/index.html").read_bytes() == data


def test_template_shift_raises_when_new_empty(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    idx = tmp_path / "Reports/CURRENT/x/index.html"
    idx.parent.mkdir(parents=True)
    idx.write_bytes(b'<pre><A HREF="/a/">a</A><A HREF="/b/">b</A></pre>')

    # Refetched bytes contain no parseable <A HREF="..."> — template shift.
    refetched = b'<pre><a href="/a/">a</a></pre>'  # lowercase, regex misses
    with pytest.raises(mod.HREFExtractionShiftError):
        mod.save_listing("/Reports/CURRENT/x/", refetched)
    # Forensic write: the bytes ARE saved even though the guard raised.
    assert idx.read_bytes() == refetched


def test_template_shift_raises_when_new_drops_half(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    idx = tmp_path / "Reports/CURRENT/x/index.html"
    idx.parent.mkdir(parents=True)
    # Old: 10 HREFs
    old_hrefs = b"".join(f'<A HREF="/x{i}/">x</A>'.encode() for i in range(10))
    idx.write_bytes(b"<pre>" + old_hrefs + b"</pre>")

    # New: 4 HREFs (60% drop) — should trigger guard (threshold ≥ 50%).
    new_hrefs = b"".join(f'<A HREF="/x{i}/">x</A>'.encode() for i in range(4))
    refetched = b"<pre>" + new_hrefs + b"</pre>"
    with pytest.raises(mod.HREFExtractionShiftError):
        mod.save_listing("/Reports/CURRENT/x/", refetched)


def test_template_shift_triggers_at_exact_50pct_boundary(tmp_path: Path, monkeypatch) -> None:
    """Design locks the threshold at >=50% HREF drop; 10 -> 5 MUST trigger."""
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    idx = tmp_path / "Reports/CURRENT/x/index.html"
    idx.parent.mkdir(parents=True)
    # Old: 10 HREFs
    idx.write_bytes(
        b"<pre>" + b"".join(f'<A HREF="/x{i}/">x</A>'.encode() for i in range(10)) + b"</pre>"
    )
    # New: exactly 5 HREFs (exactly 50% drop).
    refetched = (
        b"<pre>" + b"".join(f'<A HREF="/x{i}/">x</A>'.encode() for i in range(5)) + b"</pre>"
    )
    with pytest.raises(mod.HREFExtractionShiftError):
        mod.save_listing("/Reports/CURRENT/x/", refetched)


def test_template_shift_does_not_trigger_on_small_drop(tmp_path: Path, monkeypatch) -> None:
    import nemweb_download as mod

    monkeypatch.setattr(mod, "OUT", tmp_path)
    idx = tmp_path / "Reports/CURRENT/x/index.html"
    idx.parent.mkdir(parents=True)
    # Old: 10, new: 6 (40% drop — under the 50% threshold).
    idx.write_bytes(
        b"<pre>" + b"".join(f'<A HREF="/x{i}/">x</A>'.encode() for i in range(10)) + b"</pre>"
    )
    refetched = (
        b"<pre>" + b"".join(f'<A HREF="/x{i}/">x</A>'.encode() for i in range(6)) + b"</pre>"
    )
    # Should NOT raise — a legitimate 40% rolloff in a rolling directory.
    mod.save_listing("/Reports/CURRENT/x/", refetched)
    assert idx.read_bytes() == refetched, "40% drop is within threshold; write should proceed"
