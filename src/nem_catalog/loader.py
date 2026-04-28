"""Catalog loading: primary `load()` and opt-in `fetch_latest()`.

load() — pure, deterministic, no implicit I/O beyond the one read.
fetch_latest() — opt-in convenience: live fetch, ETag cache, last-good fallback.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
import warnings
from pathlib import Path

from nem_catalog.catalog import Catalog
from nem_catalog.errors import IncompatibleCatalogError, NemCatalogFetchError

_SUPPORTED_MAJOR = 2
_DEFAULT_URL = "https://zhipenghe.me/nem-catalog/catalog.json"
_DEFAULT_RELEASE_URL_TEMPLATE = (
    "https://github.com/ZhipengHe/nem-catalog/releases/download/"
    "catalog-{version}/catalog-{version}.json"
)
_USER_AGENT = "nem-catalog-sdk/0.1"


def load(path_or_url: str | Path) -> Catalog:
    """Load a catalog from a local path or HTTP(S) URL. Pure: no cache, no fallback.

    URL loading accepts both `http://` and `https://`. Production consumers
    should use `https://` (the canonical Pages URL is HTTPS); plain HTTP is
    accepted to support local test servers and air-gapped mirrors.
    """
    if isinstance(path_or_url, Path) or not str(path_or_url).startswith(("http://", "https://")):
        raw = Path(path_or_url).read_text()
    else:
        req = urllib.request.Request(str(path_or_url), headers={"User-Agent": _USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"invalid JSON: {e}") from e

    _check_compat(data.get("schema_version", "0.0.0"))
    return Catalog(data)


def fetch_latest(
    cache_dir: str | Path | None = None,
    catalog_version: str | None = None,
) -> Catalog:
    """Live fetch + ETag cache + last-good fallback. For scripts and notebooks.

    Parameters
    ----------
    cache_dir : directory for cached catalog + ETag. Defaults to ~/.cache/nem-catalog.
    catalog_version : optional CalVer pin. When set, fetches the versioned release
        asset URL instead of the stable `latest` URL. Use for reproducible research.
    """
    cache_dir = Path(cache_dir or "~/.cache/nem-catalog").expanduser()
    cache_dir.mkdir(parents=True, exist_ok=True)

    if catalog_version:
        template = os.environ.get("NEM_CATALOG_RELEASE_URL_TEMPLATE", _DEFAULT_RELEASE_URL_TEMPLATE)
        url = template.format(version=catalog_version)
        cache_name = f"catalog-{catalog_version}.json"
    else:
        url = os.environ.get("NEM_CATALOG_URL", _DEFAULT_URL)
        cache_name = "catalog.json"

    cached_path = cache_dir / cache_name
    etag_path = cache_dir / f"{cache_name}.etag"
    cached_etag = etag_path.read_text().strip() if etag_path.exists() else None

    try:
        headers = {"User-Agent": _USER_AGENT}
        if cached_etag:
            headers["If-None-Match"] = cached_etag
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read()
            etag = resp.headers.get("ETag") or ""
        cached_path.write_bytes(body)
        if etag:
            etag_path.write_text(etag)
    except urllib.error.HTTPError as e:
        if e.code == 304 and cached_path.exists():
            # Revalidation hit — serve from cache
            pass
        else:
            return _serve_cache_with_warning(cached_path, str(e))
    except (urllib.error.URLError, TimeoutError) as e:
        return _serve_cache_with_warning(cached_path, str(e))

    try:
        data = json.loads(cached_path.read_text())
    except (json.JSONDecodeError, FileNotFoundError) as e:
        raise NemCatalogFetchError(f"catalog cache corrupt or missing: {e}") from e

    _check_compat(data.get("schema_version", "0.0.0"))
    return Catalog(data)


def _serve_cache_with_warning(cached_path: Path, error_detail: str) -> Catalog:
    if not cached_path.exists():
        raise NemCatalogFetchError(f"live fetch failed and no cache available: {error_detail}")
    warnings.warn(
        f"nem_catalog: network error, serving cached catalog ({error_detail})",
        stacklevel=2,
    )
    data = json.loads(cached_path.read_text())
    _check_compat(data.get("schema_version", "0.0.0"))
    return Catalog(data)


def _check_compat(schema_version: str) -> None:
    try:
        major = int(schema_version.split(".", 1)[0])
    except (ValueError, IndexError) as e:
        raise IncompatibleCatalogError(f"invalid schema_version {schema_version!r}") from e
    if major != _SUPPORTED_MAJOR:
        raise IncompatibleCatalogError(
            f"catalog schema version {schema_version} not supported by SDK 0.1 "
            f"(supports {_SUPPORTED_MAJOR}.x)"
        )
