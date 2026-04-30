"""Tests for Catalog class properties and basic accessors."""

from pathlib import Path

import pytest

from nem_catalog import load

REPO_ROOT = Path(__file__).parent.parent
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "sample_catalog.json"


@pytest.fixture
def catalog():
    return load(FIXTURE)


def test_schema_version(catalog):
    assert catalog.schema_version == "2.0.0"


def test_catalog_version(catalog):
    assert catalog.catalog_version == "2026.04.18"


def test_as_of_returns_datetime(catalog):
    assert catalog.as_of.year == 2026
    assert catalog.as_of.month == 4
    assert catalog.as_of.day == 18


def test_dataset_keys_excludes_aux(catalog):
    keys = catalog.dataset_keys()
    assert "Reports:DispatchIS_Reports" in keys
    assert "MMSDM:DISPATCHPRICE" in keys
    assert "MMSDM:DOCUMENTATION_AUX" not in keys  # AUX filtered


def test_raw_keys_includes_aux(catalog):
    keys = catalog.raw_keys()
    assert "MMSDM:DOCUMENTATION_AUX" in keys  # AUX preserved


def test_dataset_keys_is_subset_of_raw_keys(catalog):
    assert set(catalog.dataset_keys()).issubset(set(catalog.raw_keys()))
