"""Tests for Catalog.resolve() — URL expansion + tier routing."""

import warnings
from pathlib import Path

import pytest

from nem_catalog import UnresolvableDatasetError, load

REPO_ROOT = Path(__file__).parent.parent
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "sample_catalog.json"
NEMWEB = "https://nemweb.com.au"


@pytest.fixture
def catalog():
    return load(FIXTURE)


def test_unknown_key_raises_key_error(catalog):
    with pytest.raises(KeyError) as ei:
        catalog.resolve("Reports:NoSuchStream", from_="2025-04-01", to_="2025-04-02")
    assert "Reports:NoSuchStream" in str(ei.value)


def test_key_error_includes_close_match_suggestion(catalog):
    with pytest.raises(KeyError) as ei:
        catalog.resolve("Reports:DispatchIS_Report", from_="2025-04-01", to_="2025-04-02")  # missing s
    msg = str(ei.value)
    assert "did you mean" in msg.lower()
    assert "Reports:DispatchIS_Reports" in msg


def test_to_before_from_raises_value_error(catalog):
    with pytest.raises(ValueError):
        catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-02", to_="2025-04-01")


def test_unresolvable_dataset_raises(catalog):
    with pytest.raises(UnresolvableDatasetError):
        catalog.resolve("Reports:NEXT_DAY_OFFER_ENERGY)SPARSE", from_="2025-04-01", to_="2025-04-02")


def test_resolve_archive_daily_rollup_returns_one_url_per_day(catalog):
    # from_=2025-04-01 is far older than (as_of=2026-04-18 − retention_hint_unverified_days=2),
    # so the router returns ARCHIVE-only per design doc line 38.
    urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-01", to_="2025-04-03")
    archive_urls = [u for u in urls if "/ARCHIVE/" in u]
    current_urls = [u for u in urls if "/CURRENT/" in u]
    assert len(archive_urls) == 3
    assert len(current_urls) == 0  # outside retention window → no CURRENT URLs
    assert f"{NEMWEB}/Reports/ARCHIVE/DispatchIS_Reports/PUBLIC_DISPATCHIS_20250401.zip" in archive_urls
    assert f"{NEMWEB}/Reports/ARCHIVE/DispatchIS_Reports/PUBLIC_DISPATCHIS_20250403.zip" in archive_urls


def test_resolve_reports_inside_retention_window_returns_current_only(catalog):
    """Test plan line 30: from_ inside CURRENT retention window → only CURRENT tier URLs."""
    # Fixture's as_of is 2026-04-18, retention_hint_unverified_days for CURRENT is 2.
    # retention_cutoff = 2026-04-16. Request from_=2026-04-17 is inside the window.
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-17", to_="2026-04-18")
    current_urls = [u for u in urls if "/CURRENT/" in u]
    archive_urls = [u for u in urls if "/ARCHIVE/" in u]
    assert len(current_urls) > 0, "expected CURRENT URLs inside retention window"
    assert len(archive_urls) == 0, "must not emit ARCHIVE URLs when request is inside retention"
    assert not any("older than" in str(rec.message) for rec in w), "no pre-retention warning inside window"


def test_resolve_reports_before_retention_warns_and_emits_archive(catalog):
    """Test plan line 31: from_ outside retention → warning + ARCHIVE URLs only."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2024-01-01", to_="2024-01-03")
    current_urls = [u for u in urls if "/CURRENT/" in u]
    archive_urls = [u for u in urls if "/ARCHIVE/" in u]
    assert len(current_urls) == 0
    assert len(archive_urls) == 3
    assert any("retention" in str(rec.message).lower() for rec in w), "expected pre-retention warning"


def test_resolve_reports_straddling_retention_boundary_emits_both_tiers(catalog):
    """Test plan line 32: range spanning CURRENT/ARCHIVE boundary → both tiers' URLs."""
    # retention_cutoff = 2026-04-18 − 2 days = 2026-04-16. Range 2026-04-15 .. 2026-04-18 straddles.
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-15", to_="2026-04-18")
    current_urls = [u for u in urls if "/CURRENT/" in u]
    archive_urls = [u for u in urls if "/ARCHIVE/" in u]
    assert len(current_urls) > 0, "straddle must include CURRENT"
    assert len(archive_urls) > 0, "straddle must include ARCHIVE"
    assert any("retention" in str(rec.message).lower() for rec in w), "straddle emits pre-retention warning"


def test_resolve_fcas_annual_covers_observed_range(catalog):
    urls = catalog.resolve("FCAS_Causer_Pays:CAUSER_PAYS", from_="2011-01-01", to_="2012-12-31")
    assert f"{NEMWEB}/Data_Archive/Wholesale_Electricity/FCAS_Causer_Pays/2011/2011.txt" in urls
    assert f"{NEMWEB}/Data_Archive/Wholesale_Electricity/FCAS_Causer_Pays/2012/2012.txt" in urls
    assert len(urls) == 2


def test_resolve_fcas_outside_observed_range_warns_and_returns_empty(catalog):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        urls = catalog.resolve("FCAS_Causer_Pays:CAUSER_PAYS", from_="2020-01-01", to_="2020-12-31")
    assert urls == []
    assert any("outside observed_range" in str(rec.message) for rec in w)


def test_resolve_mmsdm_view_filter_narrows_fanout(catalog):
    urls_all = catalog.resolve("MMSDM:DISPATCHPRICE", from_="2025-04-01", to_="2025-04-30")
    urls_data_only = catalog.resolve("MMSDM:DISPATCHPRICE", from_="2025-04-01", to_="2025-04-30", view="DATA")
    assert all("/DATA/" in u for u in urls_data_only)
    assert len(urls_data_only) < len(urls_all)


def test_resolve_returns_strings(catalog):
    urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-01", to_="2025-04-02")
    assert all(isinstance(u, str) for u in urls)
