"""Catalog loading: primary `load()` and opt-in `fetch_latest()`.

`load()` is pure: given a path or URL, returns a Catalog object. No cache,
no fallback, no implicit I/O beyond the single read. Tool-builders adopt this.

`fetch_latest()` wraps load() with ETag-cached fetch + last-good fallback,
for script users. It lives in Task 10; this file stubs it.
"""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

from nem_catalog.catalog import Catalog
from nem_catalog.errors import IncompatibleCatalogError

_SUPPORTED_MAJOR = 1


def load(path_or_url: str | Path) -> Catalog:
    """Load a catalog from a local path or HTTPS URL.

    Deterministic: reads once, parses, validates the schema major version,
    returns a Catalog. Raises FileNotFoundError / ValueError / IncompatibleCatalogError
    but does NOT do caching or fallback.
    """
    if isinstance(path_or_url, Path) or not str(path_or_url).startswith(("http://", "https://")):
        raw = Path(path_or_url).read_text()
    else:
        req = urllib.request.Request(
            str(path_or_url),
            headers={"User-Agent": "nem-catalog-sdk/0.1"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            raw = resp.read().decode("utf-8")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"invalid JSON: {e}") from e

    _check_compat(data.get("schema_version", "0.0.0"))
    return Catalog(data)


def _check_compat(schema_version: str) -> None:
    try:
        major = int(schema_version.split(".", 1)[0])
    except (ValueError, IndexError) as e:
        raise IncompatibleCatalogError(f"invalid schema_version string {schema_version!r}") from e
    if major != _SUPPORTED_MAJOR:
        raise IncompatibleCatalogError(
            f"catalog schema version {schema_version} not supported by SDK 0.1 "
            f"(supports {_SUPPORTED_MAJOR}.x)"
        )


def fetch_latest(
    cache_dir: str | Path | None = None, catalog_version: str | None = None
) -> Catalog:
    """Opt-in convenience: live fetch with ETag cache + last-good fallback.

    Implementation lives in Task 10.
    """
    raise NotImplementedError("fetch_latest is implemented in Task 10")
