"""Tests for per-record resolve() semantics in v2.0.0 schema.

Task 8 of PR-2 (#22): Four RED tests validating that resolve() will iterate
per-record within tiers and apply per-record token-skipping and observed_range
filtering after the schema bump from 1.0.0 (single tier dict) to 2.0.0 (tier
as list of records).

These tests expect 4 RED failures during the RED phase — today's resolve()
calls .get() on what will become a list and raises TypeError or AttributeError.
"""

import warnings

import pytest

from nem_catalog import Catalog
from nem_catalog.errors import NonResolvableTemplateError


def _make_catalog_v2(datasets: dict) -> Catalog:
    """Helper: construct a v2.0.0 schema Catalog (tiers as lists) for testing."""
    data = {
        "schema_version": "2.0.0",
        "catalog_version": "2026.04.28",
        "as_of": "2026-04-28T00:00:00Z",
        "placeholders": {},
        "dataset_keys": list(datasets.keys()),
        "raw_keys": list(datasets.keys()),
        "datasets": datasets,
    }
    return Catalog(data)


def test_resolve_iterates_all_records_in_a_tier():
    """Test that resolve() yields URLs from every record in a multi-record tier.

    Given: tiers["CURRENT"] = [rec_a, rec_b] where both are pure-temporal
    (filename_template with {date}, no non-temporal tokens).
    When: resolve(key, "2025-04-01", "2025-04-02")
    Then: should return 4 URLs (2 dates x 2 records), one per combination.

    This test validates the core semantic change from v1 (skip whole tier on
    multi-record collision) to v2 (iterate each record independently).
    """
    datasets = {
        "Test:MultiFile": {
            "repo": "Test",
            "intra_repo_id": "MultiFile",
            "resolvable": True,
            "tiers": {
                "CURRENT": [
                    {
                        "path_template": "/test/",
                        "filename_template": "vicgas_aaa_{date}.csv",
                        "filename_regex": ".*",
                        "example": "vicgas_aaa_20250401.csv",
                        "cadence": "daily",
                    },
                    {
                        "path_template": "/test/",
                        "filename_template": "vicgas_bbb_{date}.csv",
                        "filename_regex": ".*",
                        "example": "vicgas_bbb_20250401.csv",
                        "cadence": "daily",
                    },
                ]
            },
            "query_shape": None,
            "schema_source": None,
            "anomaly_note": None,
        }
    }
    cat = _make_catalog_v2(datasets)

    urls = cat.resolve("Test:MultiFile", from_="2025-04-01", to_="2025-04-02")

    # 2 dates x 2 records = 4 URLs
    assert len(urls) == 4, f"expected 4 URLs, got {len(urls)}: {urls}"
    assert all("/test/vicgas_aaa_" in u or "/test/vicgas_bbb_" in u for u in urls)
    assert any("vicgas_aaa_20250401" in u for u in urls)
    assert any("vicgas_aaa_20250402" in u for u in urls)
    assert any("vicgas_bbb_20250401" in u for u in urls)
    assert any("vicgas_bbb_20250402" in u for u in urls)


def test_resolve_skips_individual_record_with_non_temporal_token():
    """Test that resolve() skips individual non-temporal records but continues with others.

    Given: tiers["CURRENT"] = [pure_temporal_rec, rec_with_aemo_id]
    When: resolve(key, ...)
    Then: should return URLs for the pure-temporal record AND emit exactly one warning
          about the skipped record (not about the skipped tier — it's per-record).

    This validates per-record token-skipping: one record with {aemo_id} doesn't block
    its sibling pure-temporal record.
    """
    datasets = {
        "Test:MixedTokens": {
            "repo": "Test",
            "intra_repo_id": "MixedTokens",
            "resolvable": True,
            "tiers": {
                "CURRENT": [
                    {
                        "path_template": "/test/",
                        "filename_template": "temporal_{date}.csv",
                        "filename_regex": ".*",
                        "example": "temporal_20250401.csv",
                        "cadence": "daily",
                    },
                    {
                        "path_template": "/test/{aemo_id}/",
                        "filename_template": "site_data.csv",
                        "filename_regex": ".*",
                        "example": "site_data.csv",
                        "cadence": "static",
                    },
                ]
            },
            "query_shape": None,
            "schema_source": None,
            "anomaly_note": None,
        }
    }
    cat = _make_catalog_v2(datasets)

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        urls = cat.resolve("Test:MixedTokens", from_="2025-04-01", to_="2025-04-02")

    # Should have 2 URLs from the pure-temporal record (1 per date)
    assert len(urls) == 2, f"expected 2 URLs from pure-temporal record, got {len(urls)}: {urls}"
    assert all("temporal_" in u for u in urls)
    assert any("temporal_20250401" in u for u in urls)
    assert any("temporal_20250402" in u for u in urls)

    # Should have exactly one warning about the skipped record
    skipped_warns = [
        rec
        for rec in w
        if issubclass(rec.category, UserWarning)
        and "skipped" in str(rec.message).lower()
        and "aemo_id" in str(rec.message)
    ]
    assert len(skipped_warns) == 1, (
        f"expected exactly one skipped-record warning about aemo_id, got {len(skipped_warns)}: "
        f"{[str(r.message) for r in skipped_warns]}; all warnings: {[str(r.message) for r in w]}"
    )


def test_resolve_per_record_observed_range_filter():
    """Test that observed_range filtering is applied per-record.

    Given: tiers["ARCHIVE"] = [rec_2024, rec_2025] with
           rec_2024.observed_range = {"from": "2024-01-01", "to": "2024-12-31"}
           rec_2025.observed_range = {"from": "2025-01-01", "to": "2025-12-31"}
    When: resolve(key, from_="2024-06-01", to_="2024-12-31")
    Then: should return URLs only from rec_2024 (the only overlapping record).

    This validates per-record observed_range filtering: the 2025 record is
    silently skipped (no URLs produced, no warning) because it doesn't overlap
    the request window.
    """
    datasets = {
        "Test:PerRecordObs": {
            "repo": "Test",
            "intra_repo_id": "PerRecordObs",
            "resolvable": True,
            "tiers": {
                "ARCHIVE": [
                    {
                        "path_template": "/archive/2024/",
                        "filename_template": "data_2024_{date}.csv",
                        "filename_regex": ".*",
                        "example": "data_2024_20240601.csv",
                        "cadence": "daily",
                        "observed_range": {"from": "2024-01-01", "to": "2024-12-31"},
                    },
                    {
                        "path_template": "/archive/2025/",
                        "filename_template": "data_2025_{date}.csv",
                        "filename_regex": ".*",
                        "example": "data_2025_20250601.csv",
                        "cadence": "daily",
                        "observed_range": {"from": "2025-01-01", "to": "2025-12-31"},
                    },
                ]
            },
            "query_shape": None,
            "schema_source": None,
            "anomaly_note": None,
        }
    }
    cat = _make_catalog_v2(datasets)

    urls = cat.resolve("Test:PerRecordObs", from_="2024-06-01", to_="2024-12-31")

    # Should have exactly 214 URLs from rec_2024 (June 1 through Dec 31).
    # Breakdown: 30 (Jun) + 31 (Jul) + 31 (Aug) + 30 (Sep) + 31 (Oct) + 30 (Nov) + 31 (Dec) = 214
    # The 2025 record doesn't overlap the request, so it's skipped.
    assert all("data_2024_" in u for u in urls), f"expected all URLs from 2024 record, got: {urls}"
    assert not any("data_2025_" in u for u in urls), f"unexpected 2025 URLs in result: {urls}"

    expected_count = 214  # Daily 2024-06-01 to 2024-12-31 inclusive
    assert len(urls) == expected_count, (
        f"expected {expected_count} URLs from 2024 record (214 days x 1 record), "
        f"got {len(urls)}: first 5 = {urls[:5]}"
    )

    # Verify exact boundary dates present (catches off-by-one in observed_range)
    first_5 = urls[:5] if urls else []
    last_5 = urls[-5:] if urls else []
    assert any("20240601" in u for u in urls), (
        f"June 1 start date missing from URLs; first 5 = {first_5}"
    )
    assert any("20241231" in u for u in urls), (
        f"December 31 end date missing from URLs; last 5 = {last_5}"
    )


def test_resolve_raises_when_every_record_is_non_temporal():
    """Test that resolve() raises NonResolvableTemplateError when no records can be resolved.

    Given: tiers["CURRENT"] = [rec_with_aemo_id_1, rec_with_aemo_id_2]
           (both contain non-temporal {aemo_id} token, no pure-temporal sibling)
    When: resolve(key, ...)
    Then: should raise NonResolvableTemplateError (not silently return empty list or skip
          the tier).

    This validates the error-raising semantics: if EVERY selected record is
    non-temporal AND no URLs were built, raise. This differs from v1 where the
    check was per-tier; in v2 it's per-record.
    """
    datasets = {
        "Test:AllNonTemporal": {
            "repo": "Test",
            "intra_repo_id": "AllNonTemporal",
            "resolvable": True,
            "tiers": {
                "CURRENT": [
                    {
                        "path_template": "/test/{aemo_id}/",
                        "filename_template": "site_a.csv",
                        "filename_regex": ".*",
                        "example": "site_a.csv",
                        "cadence": "static",
                    },
                    {
                        "path_template": "/test/{aemo_id}/",
                        "filename_template": "site_b.csv",
                        "filename_regex": ".*",
                        "example": "site_b.csv",
                        "cadence": "static",
                    },
                ]
            },
            "query_shape": None,
            "schema_source": None,
            "anomaly_note": None,
        }
    }
    cat = _make_catalog_v2(datasets)

    with pytest.raises(NonResolvableTemplateError) as exc_info:
        cat.resolve("Test:AllNonTemporal", from_="2025-04-01", to_="2025-04-02")

    # Error should mention the unresolvable tokens
    assert "aemo_id" in str(exc_info.value)
