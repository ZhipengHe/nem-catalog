"""Tests for Catalog.resolve() — URL expansion + tier routing."""

import warnings
from pathlib import Path

import pytest

from nem_catalog import UnresolvableDatasetError, load
from nem_catalog.errors import NonResolvableTemplateError

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


def test_resolve_returns_strings(catalog):
    urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-01", to_="2025-04-02")
    assert all(isinstance(u, str) for u in urls)


# ---- STRICT: NonResolvableTemplateError for non-temporal placeholders -------


def test_resolve_raises_when_current_tier_has_aemo_id(catalog):
    """Inside retention → router selects CURRENT only → CURRENT has {aemo_id} → raise.

    Replaces the pre-STRICT test that asserted CURRENT-only URL output. Under the
    STRICT contract the router still selects CURRENT alone, but the template has
    a non-temporal placeholder ({aemo_id}), so resolve() raises before building
    any URL. The error tier == 'CURRENT' proves the router chose correctly.
    """
    with pytest.raises(NonResolvableTemplateError) as ei:
        catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-17", to_="2026-04-18")
    assert ei.value.dataset_key == "Reports:DispatchIS_Reports"
    assert ei.value.tier == "CURRENT"
    assert "aemo_id" in ei.value.tokens


def test_resolve_raises_when_straddle_includes_current_tier(catalog):
    """Straddle → router selects both tiers → CURRENT has {aemo_id} → raise.

    Replaces the pre-STRICT test that asserted both-tier URL emission. Under
    STRICT the router still straddles (both tiers selected), but the CURRENT
    tier raises before URL building.
    """
    with pytest.raises(NonResolvableTemplateError) as ei:
        catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-15", to_="2026-04-18")
    assert ei.value.tier == "CURRENT"
    assert "aemo_id" in ei.value.tokens


def test_resolve_raises_when_mmsdm_template_has_nn(catalog):
    """MMSDM:DISPATCHPRICE has {nn} in both views → raise even with view= filter.

    Replaces the pre-STRICT view=filter test. view= routing still applies, but
    the selected tier's template has {nn} which resolve() cannot compute.
    """
    with pytest.raises(NonResolvableTemplateError) as ei:
        catalog.resolve("MMSDM:DISPATCHPRICE", from_="2025-04-01", to_="2025-04-30", view="DATA")
    assert ei.value.dataset_key == "MMSDM:DISPATCHPRICE"
    assert ei.value.tier == "DATA"
    assert "nn" in ei.value.tokens


def test_non_resolvable_error_names_multiple_tokens(catalog):
    """The error lists every unresolvable token in the offending tier."""
    with pytest.raises(NonResolvableTemplateError) as ei:
        catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-18", to_="2026-04-18")
    tokens = ei.value.tokens
    assert isinstance(tokens, frozenset)
    # CURRENT template is PUBLIC_DISPATCHIS_{timestamp}_{aemo_id}.zip:
    # {timestamp} is temporal, {aemo_id} is not. Only aemo_id must be listed.
    assert tokens == frozenset({"aemo_id"})


def test_non_resolvable_error_message_includes_dataset_and_tokens(catalog):
    """Error message is informative enough for a user to debug without reading docs."""
    with pytest.raises(NonResolvableTemplateError) as ei:
        catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-18", to_="2026-04-18")
    msg = str(ei.value)
    assert "Reports:DispatchIS_Reports" in msg
    assert "aemo_id" in msg
    assert "CURRENT" in msg


def test_resolve_fcas_annual_still_returns_urls_under_strict(catalog):
    """FCAS_Causer_Pays:CAUSER_PAYS template is pure temporal ({year}.txt) → unaffected."""
    urls = catalog.resolve("FCAS_Causer_Pays:CAUSER_PAYS", from_="2011-01-01", to_="2012-12-31")
    assert len(urls) == 2
    assert all(isinstance(u, str) for u in urls)
    assert all("{" not in u for u in urls)  # no surviving placeholder literals


def test_resolve_nemde_still_returns_urls_under_strict(catalog):
    """NEMDE:NemPriceSetter template is pure temporal ({date}) → unaffected."""
    urls = catalog.resolve("NEMDE:NemPriceSetter", from_="2024-06-01", to_="2024-06-03")
    assert len(urls) == 3
    assert all("{" not in u for u in urls)
