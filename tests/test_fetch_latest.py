"""Tests for nem_catalog.fetch_latest() — opt-in convenience with cache + fallback."""

import http.server
import re
import threading
from pathlib import Path

import pytest

from nem_catalog import NemCatalogFetchError, fetch_latest

REPO_ROOT = Path(__file__).parent.parent
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "sample_catalog.json"


class _Server(http.server.HTTPServer):
    def __init__(self, addr, handler, body: bytes, etag: str, status: int = 200):
        super().__init__(addr, handler)
        self.body = body
        self.etag = etag
        self.status = status
        self.served_count = 0


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        srv: _Server = self.server  # type: ignore[assignment]
        srv.served_count += 1
        if self.headers.get("If-None-Match") == srv.etag:
            self.send_response(304)
            self.end_headers()
            return
        self.send_response(srv.status)
        self.send_header("ETag", srv.etag)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(srv.body)

    def log_message(self, *a, **kw):
        pass


@pytest.fixture
def server():
    body = FIXTURE.read_bytes()
    srv = _Server(("127.0.0.1", 0), _Handler, body, etag='"abc123"')
    host, port = srv.server_address
    thread = threading.Thread(target=srv.serve_forever, daemon=True)
    thread.start()
    yield srv, f"http://{host}:{port}/catalog.json"
    srv.shutdown()


def test_cold_fetch_writes_cache(server, tmp_path, monkeypatch):
    _srv, url = server
    monkeypatch.setenv("NEM_CATALOG_URL", url)
    c = fetch_latest(cache_dir=tmp_path)
    assert c.schema_version == "1.0.0"
    cached = tmp_path / "catalog.json"
    assert cached.exists()


def test_warm_fetch_304_serves_cached(server, tmp_path, monkeypatch):
    srv, url = server
    monkeypatch.setenv("NEM_CATALOG_URL", url)
    c1 = fetch_latest(cache_dir=tmp_path)
    assert srv.served_count == 1
    c2 = fetch_latest(cache_dir=tmp_path)
    # Second call hits the server with If-None-Match, gets 304, serves cache.
    assert srv.served_count == 2
    assert c2.catalog_version == c1.catalog_version


def test_network_error_with_cache_warns_and_serves_cached(server, tmp_path, monkeypatch, recwarn):
    srv, url = server
    monkeypatch.setenv("NEM_CATALOG_URL", url)
    # Prime the cache
    fetch_latest(cache_dir=tmp_path)
    # Shut down the server to simulate network error
    srv.shutdown()
    # Now fetch again — should fall back to cache
    c = fetch_latest(cache_dir=tmp_path)
    assert c.schema_version == "1.0.0"
    assert any(
        "network" in str(w.message).lower() or "cache" in str(w.message).lower()
        for w in recwarn.list
    )


def test_cold_fetch_network_error_with_no_cache_raises(tmp_path, monkeypatch):
    monkeypatch.setenv("NEM_CATALOG_URL", "http://127.0.0.1:1/nope.json")  # definitely unreachable
    with pytest.raises(NemCatalogFetchError):
        fetch_latest(cache_dir=tmp_path)


def test_catalog_version_pin_uses_release_url(server, tmp_path, monkeypatch):
    _srv, url = server
    # Simulate the release asset URL template: same server, different path.
    monkeypatch.setenv(
        "NEM_CATALOG_RELEASE_URL_TEMPLATE", url.replace("/catalog.json", "/catalog-{version}.json")
    )
    # Serve it anyway (our fake server returns the same body for any path)
    c = fetch_latest(cache_dir=tmp_path, catalog_version="2026.04.18")
    assert c.catalog_version == "2026.04.18"


def test_release_url_template_matches_publish_workflow():
    """Contract: loader's release URL template must match what publish-catalog.yml
    actually creates. If TAG= or the asset filename drifts, fetch_latest(catalog_version=...)
    404s silently on every call. Parse the workflow file and compare.
    """
    workflow = (REPO_ROOT / ".github" / "workflows" / "publish-catalog.yml").read_text()

    tag_match = re.search(r'TAG="([^"]+)"', workflow)
    assert tag_match, "could not find TAG= assignment in publish-catalog.yml"
    tag_pattern = tag_match.group(1).replace("$VERSION", "{version}")

    asset_match = re.search(r'cp catalog\.json "([^"]+)"', workflow)
    assert asset_match, "could not find asset filename (cp catalog.json ...) in publish-catalog.yml"
    asset_pattern = asset_match.group(1).replace("$VERSION", "{version}")

    from nem_catalog.loader import _DEFAULT_RELEASE_URL_TEMPLATE

    version = "2026.04.19"
    expected_path = f"{tag_pattern}/{asset_pattern}".format(version=version)
    actual = _DEFAULT_RELEASE_URL_TEMPLATE.format(version=version)
    assert actual.endswith(expected_path), (
        f"release URL contract mismatch:\n"
        f"  publish-catalog.yml produces path: .../{expected_path}\n"
        f"  loader constructs:                 {actual}"
    )
