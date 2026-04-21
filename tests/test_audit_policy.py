"""Tests for audit_policy: stateless reclassify-up/down/new-paths detection."""

from __future__ import annotations

from pathlib import Path

from scripts.audit_policy import run_audit


def _mirror(tmp_path: Path, path: str, hrefs: list[str]) -> Path:
    """Create a mirror index.html at the given relative path with given HREFs."""
    p = tmp_path / "nemweb-mirror" / path.lstrip("/") / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    body = b"<pre>" + b"".join(f'<A HREF="{h}">x</A>'.encode() for h in hrefs) + b"</pre>"
    p.write_bytes(body)
    return p


def _policy(tmp_path: Path, pattern: str, cls: str) -> Path:
    p = tmp_path / "policy.yaml"
    p.write_text(
        "version: 1\nlast_reviewed: 2026-04-20\nreviewer: t\nrules:\n"
        f'  - pattern: "{pattern}"\n    class: {cls}\n'
    )
    return p


def test_static_path_that_changed_flags_reclassify_up(tmp_path):
    # Policy says /Data_Archive/** is static. Audit finds HREFs differ
    # between the cached mirror and the live refetch, so flag as
    # reclassify-up candidate.
    policy_path = _policy(tmp_path, "/Data_Archive/**", "static")
    mirror_root = tmp_path / "nemweb-mirror"
    _mirror(tmp_path, "/Data_Archive/x/", ["/a/"])
    # "Fresh fetches" are passed in as dict[path, bytes] simulating a
    # force-refetch pass done by the workflow.
    fresh = {"/Data_Archive/x/": b'<pre><A HREF="/a/">a</A><A HREF="/b/">b</A></pre>'}
    findings = run_audit(policy_path, mirror_root, fresh)
    assert any(f.kind == "reclassify_up" and f.path == "/Data_Archive/x/" for f in findings)


def test_rolling_path_with_no_change_flags_reclassify_down(tmp_path):
    policy_path = _policy(tmp_path, "/Reports/CURRENT/x/", "rolling")
    mirror_root = tmp_path / "nemweb-mirror"
    _mirror(tmp_path, "/Reports/CURRENT/x/", ["/a/"])
    fresh = {"/Reports/CURRENT/x/": b'<pre><A HREF="/a/">a</A></pre>'}
    findings = run_audit(policy_path, mirror_root, fresh)
    assert any(f.kind == "reclassify_down" and f.path == "/Reports/CURRENT/x/" for f in findings)


def test_new_path_not_in_policy_flags_new_path(tmp_path):
    # Policy covers only /Data_Archive/**. A fresh-fetched path outside
    # any rule surfaces as a new-path finding.
    policy_path = _policy(tmp_path, "/Data_Archive/**", "static")
    mirror_root = tmp_path / "nemweb-mirror"
    fresh = {"/Reports/NEW_STREAM/": b'<pre><A HREF="/a/">a</A></pre>'}
    findings = run_audit(policy_path, mirror_root, fresh)
    assert any(f.kind == "new_path" and f.path == "/Reports/NEW_STREAM/" for f in findings)


def test_clean_audit_returns_no_findings(tmp_path):
    policy_path = _policy(tmp_path, "/Reports/CURRENT/x/", "rolling")
    mirror_root = tmp_path / "nemweb-mirror"
    _mirror(tmp_path, "/Reports/CURRENT/x/", ["/a/", "/b/"])
    # Rolling path with real change — no finding.
    fresh = {"/Reports/CURRENT/x/": b'<pre><A HREF="/b/">b</A><A HREF="/c/">c</A></pre>'}
    findings = run_audit(policy_path, mirror_root, fresh)
    assert findings == []


def test_load_fresh_root_index_maps_to_slash(tmp_path):
    from scripts.audit_policy import _load_fresh

    # Root-level index.html — fresh_dir itself contains the file.
    root_idx = tmp_path / "index.html"
    root_idx.write_bytes(b"<pre></pre>")

    result = _load_fresh(tmp_path)

    # Must produce "/" not "/./"
    assert "/" in result, f"Expected key '/' in result, got: {list(result.keys())}"
    assert "/./" not in result, f"Got wrong key '/./'; keys: {list(result.keys())}"
    assert result["/"] == b"<pre></pre>"


def test_load_fresh_nested_index_maps_correctly(tmp_path):
    from scripts.audit_policy import _load_fresh

    # Nested index.html — should produce /Reports/CURRENT/ (no regression).
    nested = tmp_path / "Reports" / "CURRENT"
    nested.mkdir(parents=True)
    (nested / "index.html").write_bytes(b"<pre>nested</pre>")

    result = _load_fresh(tmp_path)

    assert "/Reports/CURRENT/" in result, (
        f"Expected '/Reports/CURRENT/' in result, got: {list(result.keys())}"
    )
    assert result["/Reports/CURRENT/"] == b"<pre>nested</pre>"
