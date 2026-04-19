"""Error types for nem_catalog.

Every error message includes a `See: <docs_url>` suffix so CLI/library users
can jump directly to the troubleshooting entry.
"""

from __future__ import annotations

_DOCS_BASE = "https://zhipenghe.me/nem-catalog/docs/troubleshooting"


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


class NonResolvableTemplateError(NemCatalogError):
    """A selected tier's filename/path template contains a placeholder the SDK
    cannot compute from a date range.

    v0.1 resolve() only substitutes temporal placeholders (date, timestamp,
    yyyymm, year, month, and their aliases). Templates with non-temporal
    tokens like `{aemo_id}` (per-participant), `{nn}` (file sequence), or
    `{d2}` (MMSDM day marker) raise this error to avoid returning URLs
    containing unsubstituted `{...}` literals.

    Inspect the raw template via `catalog.datasets[dataset_key]["tiers"]`.
    A future SDK release will add an enumeration API for these datasets.
    """

    _anchor = "non-resolvable-template"

    def __init__(
        self,
        dataset_key: str,
        tier: str,
        tokens: frozenset[str],
    ) -> None:
        self.dataset_key = dataset_key
        self.tier = tier
        self.tokens = tokens
        token_str = ", ".join(sorted(tokens))
        msg = (
            f"dataset {dataset_key!r} tier {tier!r} template has non-temporal "
            f"placeholder(s) {{{token_str}}} which resolve() cannot substitute "
            f"from a date range. Inspect the raw template via "
            f"catalog.datasets[{dataset_key!r}]['tiers'][{tier!r}]. "
            f"See: {docs_url(self._anchor)}"
        )
        super().__init__(msg)
