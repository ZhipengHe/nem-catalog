"""Classifier-level unit tests for scripts/extract_patterns.py.

These tests are hermetic — no mirror reads, no filesystem. They exercise
classify(), classify_mmsdm(), classify_nemde(), extract_mmsdm_table(),
and aux_id_from_filename_template() with crafted inputs drawn from
reference/URL-CONVENTIONS.csv ground truth.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import extract_patterns  # noqa: E402

# ---------- extract_mmsdm_table: PUBLIC_DVD_ underscore format ----------


def test_extract_mmsdm_table_underscore_public_dvd_simple():
    # Real sample from reference/URL-CONVENTIONS.csv (MMSDM BCP_FMT row):
    # filename PUBLIC_DVD_APEVENTREGION_202403.ctl → table = APEVENTREGION
    assert (
        extract_patterns.extract_mmsdm_table("PUBLIC_DVD_APEVENTREGION_202403.ctl")
        == "APEVENTREGION"
    )


def test_extract_mmsdm_table_underscore_public_dvd_multiword_table():
    # Table names often contain underscores themselves.
    # PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_202403.ctl → ANCILLARY_RECOVERY_SPLIT
    assert (
        extract_patterns.extract_mmsdm_table("PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_202403.ctl")
        == "ANCILLARY_RECOVERY_SPLIT"
    )


def test_extract_mmsdm_table_underscore_public_dvd_data_extension():
    assert (
        extract_patterns.extract_mmsdm_table("PUBLIC_DVD_AUCTION_CALENDAR_202403.DATA")
        == "AUCTION_CALENDAR"
    )


def test_extract_mmsdm_table_underscore_public_dvd_handles_all_observed_extensions():
    # CTL, DATA, fmt, bcp — every SQLLoader view extension seen in the mirror.
    for ext in ("ctl", "DATA", "fmt", "bcp"):
        fname = f"PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_202403.{ext}"
        assert extract_patterns.extract_mmsdm_table(fname) == "AUCTION_IC_ALLOCATIONS"


def test_extract_mmsdm_table_preserves_hash_format_compatibility():
    # Regression guard: the pre-existing # path MUST still work.
    # PUBLIC_ARCHIVE#DISPATCH#FILE01#202408.ctl → DISPATCH
    assert (
        extract_patterns.extract_mmsdm_table("PUBLIC_ARCHIVE%23DISPATCH%23FILE01%23202408.ctl")
        == "DISPATCH"
    )


# ---------- classify: MMSDM_MONTHLY_BULK (dead branch revived) ----------


def test_classify_mmsdm_monthly_bulk_zip_promoted():
    # Real URL from mirror: /Data_Archive/Wholesale_Electricity/MMSDM/2009/MMSDM_2009_07.zip
    url = "/Data_Archive/Wholesale_Electricity/MMSDM/2009/MMSDM_2009_07.zip"
    result = extract_patterns.classify(url, "MMSDM_2009_07.zip")
    assert result is not None
    repo, tier, intra, _extras = result
    assert repo == "MMSDM"
    assert tier == "MONTHLY_BULK"
    assert intra == "MMSDM_MONTHLY_BULK"


def test_classify_mmsdm_month_root_still_unknown_before_task4():
    # Locked behaviour until Task 4 reclassifies it. Files under
    # MMSDM/{year}/MMSDM_{year}_{mm}/ still fall through to UNKNOWN/OTHER
    # because the MONTH_ROOT_AUX branch hasn't been fixed yet.
    url = "/Data_Archive/Wholesale_Electricity/MMSDM/2009/MMSDM_2009_07/AUTORUN.INF"
    result = extract_patterns.classify(url, "AUTORUN.INF")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "MMSDM"
    # Task 4 will change this to MONTH_ROOT_AUX / AUTORUN_INF.
    assert (tier, intra) == ("OTHER", "UNKNOWN")
