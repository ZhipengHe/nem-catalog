"""Tests for nem_catalog error types."""

import pytest

from nem_catalog.errors import (
    IncompatibleCatalogError,
    NemCatalogError,
    NemCatalogFetchError,
    UnresolvableDatasetError,
    docs_url,
)

DOCS_BASE = "https://zhipenghe.me/nem-catalog/docs/troubleshooting"


def test_base_error_is_exception():
    assert issubclass(NemCatalogError, Exception)


def test_incompatible_catalog_error_is_base():
    assert issubclass(IncompatibleCatalogError, NemCatalogError)


def test_fetch_error_is_base():
    assert issubclass(NemCatalogFetchError, NemCatalogError)


def test_unresolvable_error_is_base():
    assert issubclass(UnresolvableDatasetError, NemCatalogError)


def test_docs_url_anchor():
    url = docs_url("unresolvable-dataset")
    assert url == f"{DOCS_BASE}#unresolvable-dataset"


def test_incompatible_error_message_has_docs_url():
    err = IncompatibleCatalogError("catalog schema version 2.0.0 not supported by SDK 0.1 (supports 1.x)")
    assert "See:" in str(err)
    assert DOCS_BASE in str(err)
    assert "#incompatible-catalog" in str(err)


def test_fetch_error_message_has_docs_url():
    err = NemCatalogFetchError("cold fetch failed, no cache available")
    assert "See:" in str(err)
    assert "#fetch-failed" in str(err)


def test_unresolvable_error_message_has_docs_url():
    err = UnresolvableDatasetError("Reports:NEXT_DAY_OFFER_ENERGY)SPARSE is a directory-level anomaly")
    assert "See:" in str(err)
    assert "#unresolvable-dataset" in str(err)


def test_raise_and_catch_via_base():
    with pytest.raises(NemCatalogError):
        raise IncompatibleCatalogError("test")
