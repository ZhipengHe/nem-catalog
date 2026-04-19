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
        catalog.resolve(
            "Reports:DispatchIS_Report", from_="2025-04-01", to_="2025-04-02"
        )  # missing s
    msg = str(ei.value)
    assert "did you mean" in msg.lower()
    assert "Reports:DispatchIS_Reports" in msg


def test_to_before_from_raises_value_error(catalog):
    with pytest.raises(ValueError):
        catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-02", to_="2025-04-01")


def test_unresolvable_dataset_raises(catalog):
    with pytest.raises(UnresolvableDatasetError):
        catalog.resolve(
            "Reports:NEXT_DAY_OFFER_ENERGY)SPARSE", from_="2025-04-01", to_="2025-04-02"
        )


def test_resolve_returns_urls_when_tier_has_no_observed_range():
    """Regression for Copilot PR #1 review (catalog.py:190).

    Pre-fix: the non-rolling branch only set `any_overlap = True` when a tier
    HAD observed_range and overlapped. If every selected tier omitted
    observed_range, `any_overlap` stayed False, and the function returned []
    + warning — silently discarding URLs that resolve had already built.

    Post-fix: short-circuit to empty only when EVERY selected tier has
    observed_range AND none overlap. Tiers without observed_range are
    treated as "coverage unknown" and trusted.
    """
    from nem_catalog.catalog import Catalog

    data = {
        "schema_version": "1.0.0",
        "catalog_version": "2026.04.18",
        "as_of": "2026-04-18T00:00:00Z",
        "placeholders": {},
        "dataset_keys": ["Test:NoObs"],
        "raw_keys": ["Test:NoObs"],
        "datasets": {
            "Test:NoObs": {
                "repo": "Reports",
                "intra_repo_id": "NoObs",
                "resolvable": True,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/test/",
                        "filename_template": "file_{date}.zip",
                        # observed_range deliberately omitted — curated tiers
                        # can legitimately opt out (e.g. annual aggregates).
                    }
                },
            }
        },
    }
    c = Catalog(data)
    urls = c.resolve("Test:NoObs", from_="2025-01-01", to_="2025-01-03")
    assert len(urls) == 3
    assert all("/test/file_" in u for u in urls)
    assert urls[0].endswith("file_20250101.zip")
    assert urls[-1].endswith("file_20250103.zip")


def test_resolve_archive_daily_rollup_returns_one_url_per_day(catalog):
    # from_=2025-04-01 is far older than (as_of=2026-04-18 - retention_hint_unverified_days=2),
    # so the router returns ARCHIVE-only per design doc line 38.
    urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-01", to_="2025-04-03")
    archive_urls = [u for u in urls if "/ARCHIVE/" in u]
    current_urls = [u for u in urls if "/CURRENT/" in u]
    assert len(archive_urls) == 3
    assert len(current_urls) == 0  # outside retention window → no CURRENT URLs
    assert (
        f"{NEMWEB}/Reports/ARCHIVE/DispatchIS_Reports/PUBLIC_DISPATCHIS_20250401.zip"
        in archive_urls
    )
    assert (
        f"{NEMWEB}/Reports/ARCHIVE/DispatchIS_Reports/PUBLIC_DISPATCHIS_20250403.zip"
        in archive_urls
    )


def test_resolve_reports_before_retention_warns_and_emits_archive(catalog):
    """Test plan line 31: from_ outside retention → warning + ARCHIVE URLs only."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2024-01-01", to_="2024-01-03")
    current_urls = [u for u in urls if "/CURRENT/" in u]
    archive_urls = [u for u in urls if "/ARCHIVE/" in u]
    assert len(current_urls) == 0
    assert len(archive_urls) == 3
    assert any("retention" in str(rec.message).lower() for rec in w), (
        "expected pre-retention warning"
    )


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


def test_resolve_straddle_serves_archive_warns_about_unresolvable_current(catalog):
    """Straddle with one non-resolvable tier: serve what we can, warn on the rest.

    Under the post-review STRICT-per-tier contract, resolve() no longer hard-raises
    when a straddle selects both a pure-temporal ARCHIVE and a non-resolvable
    CURRENT. It returns the ARCHIVE partition URLs and emits a warning for the
    skipped CURRENT tier. This prevents users from losing valid pre-cutoff data
    because of a post-cutoff tier's template shape.
    """
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-15", to_="2026-04-18")
    # ARCHIVE partition is [dt_from, cutoff - 1 day] = [2026-04-15, 2026-04-15]
    # → exactly 1 URL, from the pure-temporal ARCHIVE tier.
    archive_urls = [u for u in urls if "/ARCHIVE/" in u]
    current_urls = [u for u in urls if "/CURRENT/" in u]
    assert len(archive_urls) == 1, f"expected 1 ARCHIVE URL, got {archive_urls}"
    assert current_urls == [], "CURRENT is non-resolvable; must not emit URLs"
    # Warning must mention the skipped tier + its non-temporal token
    skip_warnings = [rec for rec in w if "skipped tier" in str(rec.message)]
    assert skip_warnings, "expected a skipped-tier warning for CURRENT"
    msg = str(skip_warnings[0].message)
    assert "CURRENT" in msg
    assert "aemo_id" in msg


def test_resolve_raises_when_all_tiers_are_non_resolvable(catalog):
    """When ZERO tiers can resolve, raise with the first skipped tier's info."""
    # DispatchIS_Reports inside retention window → CURRENT only → non-resolvable.
    with pytest.raises(NonResolvableTemplateError) as ei:
        catalog.resolve("Reports:DispatchIS_Reports", from_="2026-04-17", to_="2026-04-18")
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


def test_resolve_substitutes_extended_temporal_tokens():
    """Regression guard: tokens {yearmonth}, {datetime}, {yyyymmddhh} ARE temporal.
    The extractor emits them; the SDK must substitute them, not raise STRICT.

    Uses a synthetic catalog dict to isolate the token-substitution behavior
    from observed_range / retention routing.
    """
    from nem_catalog.catalog import Catalog

    raw = {
        "schema_version": "1.0.0",
        "catalog_version": "test",
        "as_of": "2026-04-19T00:00:00Z",
        "placeholders": {},
        "dataset_keys": ["Reports:YearMonthOnly", "Reports:DatetimeOnly", "Reports:HourOnly"],
        "raw_keys": ["Reports:YearMonthOnly", "Reports:DatetimeOnly", "Reports:HourOnly"],
        "datasets": {
            "Reports:YearMonthOnly": {
                "repo": "Reports",
                "intra_repo_id": "YearMonthOnly",
                "resolvable": True,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/test/",
                        "filename_template": "MONTHLY_{yearmonth}.zip",
                        "time_granularity": "yearmonth",
                        "observed_range": {"from": "2020-01", "to": "2026-12"},
                    }
                },
            },
            "Reports:DatetimeOnly": {
                "repo": "Reports",
                "intra_repo_id": "DatetimeOnly",
                "resolvable": True,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/test/",
                        "filename_template": "EVENT_{datetime}.zip",
                        "time_granularity": "datetime",
                        "observed_range": {"from": "2026-04-15", "to": "2026-04-20"},
                    }
                },
            },
            "Reports:HourOnly": {
                "repo": "Reports",
                "intra_repo_id": "HourOnly",
                "resolvable": True,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/test/",
                        "filename_template": "HOURLY_{yyyymmddhh}.zip",
                        "time_granularity": "yyyymmddhh",
                        "observed_range": {"from": "2026-04-15", "to": "2026-04-20"},
                    }
                },
            },
        },
    }
    c = Catalog(raw)

    # yearmonth: monthly iteration, 6-digit yyyymm substitution
    urls = c.resolve("Reports:YearMonthOnly", from_="2025-01-01", to_="2025-03-31")
    assert len(urls) == 3
    assert "MONTHLY_202501.zip" in urls[0]
    assert "MONTHLY_202503.zip" in urls[-1]

    # datetime: 5-minute iteration, 14-digit yyyymmddhhmmss substitution
    urls = c.resolve("Reports:DatetimeOnly", from_="2026-04-16T00:00:00", to_="2026-04-16T00:10:00")
    assert len(urls) == 3  # 00:00, 00:05, 00:10
    assert "EVENT_20260416000000.zip" in urls[0]
    assert "EVENT_20260416001000.zip" in urls[-1]

    # yyyymmddhh: hourly iteration, 10-digit substitution
    urls = c.resolve("Reports:HourOnly", from_="2026-04-16T00:00:00", to_="2026-04-16T02:00:00")
    assert len(urls) == 3  # 00, 01, 02
    assert "HOURLY_2026041600.zip" in urls[0]
    assert "HOURLY_2026041602.zip" in urls[-1]


# ---- B5: straddle partitions at cutoff (no cross-tier date overlap) ---------


def _extract_date(url: str) -> str:
    """Extract the yyyymmdd substring from a fixture ROLLING_/ARCHIVED_ URL."""
    import re

    m = re.search(r"_(\d{8})\.zip", url)
    assert m, f"no date substring in URL {url!r}"
    return m.group(1)


def test_resolve_straddle_partitions_at_cutoff(catalog):
    """B5: when a date range straddles the rolling/archive cutoff, CURRENT URLs
    must cover post-cutoff dates only (inclusive) and ARCHIVE URLs pre-cutoff
    dates only. No date is served by both tiers.

    Fixture: as_of=2026-04-18, retention_hint_unverified_days=2
    → cutoff = 2026-04-16. Request 2026-04-14..2026-04-17 straddles.
    Expected: ARCHIVE gets 2026-04-14, 2026-04-15; CURRENT gets 2026-04-16, 2026-04-17.
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # suppress pre-retention warning
        urls = catalog.resolve("Reports:PureTemporalRolling", from_="2026-04-14", to_="2026-04-17")

    current_dates = {_extract_date(u) for u in urls if "/CURRENT/" in u}
    archive_dates = {_extract_date(u) for u in urls if "/ARCHIVE/" in u}

    assert current_dates == {"20260416", "20260417"}, (
        f"CURRENT tier must cover post-cutoff dates only. Got: {sorted(current_dates)}"
    )
    assert archive_dates == {"20260414", "20260415"}, (
        f"ARCHIVE tier must cover pre-cutoff dates only. Got: {sorted(archive_dates)}"
    )
    assert current_dates.isdisjoint(archive_dates), (
        f"No date may be served by both tiers. Overlap: {current_dates & archive_dates}"
    )


def test_resolve_straddle_preserves_retention_warning(catalog):
    """Partitioning the range must not drop the existing pre-retention warning."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        catalog.resolve("Reports:PureTemporalRolling", from_="2026-04-14", to_="2026-04-17")
    assert any("retention" in str(rec.message).lower() for rec in w), (
        "straddle must still emit a pre-retention warning after partition"
    )


def test_resolve_current_only_unchanged_after_partition_fix(catalog):
    """Inside retention window (no straddle): CURRENT-only, full range.
    Regression guard for the non-straddle happy path."""
    urls = catalog.resolve("Reports:PureTemporalRolling", from_="2026-04-17", to_="2026-04-18")
    current_dates = {_extract_date(u) for u in urls if "/CURRENT/" in u}
    archive_dates = [u for u in urls if "/ARCHIVE/" in u]
    assert current_dates == {"20260417", "20260418"}
    assert archive_dates == []


def test_resolve_archive_only_unchanged_after_partition_fix(catalog):
    """Entire range below cutoff: ARCHIVE-only, full range."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        urls = catalog.resolve("Reports:PureTemporalRolling", from_="2024-01-01", to_="2024-01-03")
    current = [u for u in urls if "/CURRENT/" in u]
    archive_dates = {_extract_date(u) for u in urls if "/ARCHIVE/" in u}
    assert current == []
    assert archive_dates == {"20240101", "20240102", "20240103"}
