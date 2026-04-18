"""Error types for nem_catalog.

Every error message includes a `See: <docs_url>` suffix so CLI/library users
can jump directly to the troubleshooting entry.
"""

from __future__ import annotations

_DOCS_BASE = "https://zhipenghe.github.io/nem-catalog/docs/troubleshooting"


def docs_url(anchor: str) -> str:
    """Build a docs URL for the given troubleshooting anchor."""
    return f"{_DOCS_BASE}#{anchor}"


class NemCatalogError(Exception):
    """Base class for all nem_catalog errors."""


class _WithDocsUrl(NemCatalogError):
    """Internal mixin that appends the docs URL to the message."""

    _anchor: str = "general"

    def __init__(self, message: str) -> None:
        full = f"{message}. See: {docs_url(self._anchor)}"
        super().__init__(full)


class IncompatibleCatalogError(_WithDocsUrl):
    """Catalog schema MAJOR version is not supported by this SDK.

    SDK 0.1.x supports schemas with major == 1. Catalogs with major == 2 or
    higher require an SDK upgrade.
    """

    _anchor = "incompatible-catalog"


class NemCatalogFetchError(_WithDocsUrl):
    """Live fetch failed and no usable cache is available.

    Raised by `fetch_latest()` on cold network failure. If a cache exists,
    `fetch_latest()` warns and serves the cached copy instead of raising.
    """

    _anchor = "fetch-failed"


class UnresolvableDatasetError(_WithDocsUrl):
    """The requested dataset exists in the catalog but is marked resolvable=false.

    Raised by `resolve()` when the key is present but the record describes a
    directory-level anomaly with no files (e.g., NEXT_DAY_OFFER_ENERGY)SPARSE).
    """

    _anchor = "unresolvable-dataset"
