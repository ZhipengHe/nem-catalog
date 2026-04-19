"""Tests for nem_catalog.load() — pure library loader."""

import json
from pathlib import Path

import pytest

from nem_catalog import Catalog, IncompatibleCatalogError, load

REPO_ROOT = Path(__file__).parent.parent
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "sample_catalog.json"


def test_load_local_path_returns_catalog():
    c = load(str(FIXTURE))
    assert isinstance(c, Catalog)
    assert c.schema_version == "1.0.0"
    assert c.catalog_version == "2026.04.18"


def test_load_accepts_pathlib_path():
    c = load(FIXTURE)
    assert isinstance(c, Catalog)


def test_load_raises_on_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load(str(tmp_path / "nope.json"))


def test_load_raises_on_malformed_json(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{not valid json")
    with pytest.raises(ValueError):
        load(str(bad))


def test_load_raises_on_incompatible_major(tmp_path):
    incompatible = tmp_path / "v2.json"
    data = json.loads(FIXTURE.read_text())
    data["schema_version"] = "2.0.0"
    incompatible.write_text(json.dumps(data))
    with pytest.raises(IncompatibleCatalogError):
        load(str(incompatible))


def test_load_accepts_compatible_minor_bump(tmp_path):
    """SDK ignores unknown optional fields on same major."""
    compat = tmp_path / "v1.5.json"
    data = json.loads(FIXTURE.read_text())
    data["schema_version"] = "1.5.0"
    data["brand_new_optional_field"] = "future stuff"
    compat.write_text(json.dumps(data))
    c = load(str(compat))
    assert c.schema_version == "1.5.0"


def test_load_accepts_http_url():
    """load() must fetch from an HTTP(S) URL using a local test server.

    Mirrors the local-server pattern in tests/test_fetch_latest.py — exercises
    the URL branch in load() that splits on `path_or_url.startswith(("http://",
    "https://"))`. Without this, the URL branch only runs in production.
    """
    import http.server
    import threading

    body = FIXTURE.read_bytes()

    class _H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a, **kw):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), _H)
    host, port = srv.server_address
    thread = threading.Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    try:
        c = load(f"http://{host}:{port}/catalog.json")
        assert isinstance(c, Catalog)
        assert c.schema_version == "1.0.0"
    finally:
        srv.shutdown()
