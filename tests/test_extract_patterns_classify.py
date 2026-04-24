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


def test_extract_mmsdm_table_underscore_public_dvd_timestamp_zip():
    # DATA-tier files use 12-digit timestamps + .zip (not a .DATA extension).
    # Real sample from mirror: PUBLIC_DVD_APEVENT_201510010000.zip
    assert extract_patterns.extract_mmsdm_table("PUBLIC_DVD_APEVENT_201510010000.zip") == "APEVENT"


def test_extract_mmsdm_table_underscore_public_dvd_handles_all_observed_extensions():
    # Observed extensions per `grep -rho 'PUBLIC_DVD_[^"]*\.[a-zA-Z]*' nemweb-mirror/`
    # (2026-04-25): .ctl, .ctlbak, .ctlBak, .fmt, .zip. No .DATA / .bcp.
    for ext in ("ctl", "ctlbak", "ctlBak", "fmt", "zip"):
        fname = f"PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_202403.{ext}"
        assert extract_patterns.extract_mmsdm_table(fname) == "AUCTION_IC_ALLOCATIONS"


def test_extract_mmsdm_table_preserves_hash_format_compatibility():
    # Regression guard: the pre-existing # path MUST still work.
    # PUBLIC_ARCHIVE#DISPATCH#FILE01#202408.ctl → DISPATCH
    assert (
        extract_patterns.extract_mmsdm_table("PUBLIC_ARCHIVE%23DISPATCH%23FILE01%23202408.ctl")
        == "DISPATCH"
    )


def test_extract_mmsdm_table_hash_five_part_all_dialect():
    # 5-part dialect seen in P5MIN_ALL_DATA / PREDISP_ALL_DATA view tiers:
    # PUBLIC_ARCHIVE # TABLE # ALL # FILE<NN> # <date>.<ext>
    assert (
        extract_patterns.extract_mmsdm_table(
            "PUBLIC_ARCHIVE%23P5MIN_CONSTRAINTSOLUTION%23ALL%23FILE01%23202408010000.zip"
        )
        == "P5MIN_CONSTRAINTSOLUTION"
    )
    assert (
        extract_patterns.extract_mmsdm_table(
            "PUBLIC_ARCHIVE%23PREDISPATCHLOAD%23ALL%23FILE01%23202408010000.zip"
        )
        == "PREDISPATCHLOAD"
    )


def test_extract_mmsdm_table_hash_rejects_unknown_dialects():
    # Defensive: a #-containing filename that doesn't match a known dialect
    # must return None so the caller surfaces it as UNPARSED (a gap signal),
    # not silently promote a random substring to an intra_repo_id.
    assert extract_patterns.extract_mmsdm_table("garbage#foo#bar") is None
    assert (
        extract_patterns.extract_mmsdm_table("PUBLIC_ARCHIVE#TABLE#NOT_A_FILE#202408.ctl") is None
    )
    assert extract_patterns.extract_mmsdm_table("PUBLIC_ARCHIVE#TABLE#FILE01#notadate.ctl") is None


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


# ---------- aux_id_from_filename_template helper ----------


def test_aux_id_simple_filename():
    assert extract_patterns.aux_id_from_filename_template("AUTORUN.INF") == "AUTORUN_INF"


def test_aux_id_case_variants_remain_distinct():
    # §3.1 byte-exact casing: Readme.htm (115 files) and readme.htm (1 file)
    # are served by AEMO as distinct filenames — they MUST resolve to distinct
    # aux_ids so write_json doesn't collapse them into a single catalog row.
    a = extract_patterns.aux_id_from_filename_template("Readme.htm")
    b = extract_patterns.aux_id_from_filename_template("readme.htm")
    assert a == "Readme_htm"
    assert b == "readme_htm"
    assert a != b


def test_aux_id_skeleton_tokens_stripped_angle_bracket_form():
    # skeletonize() emits <dN>. Helper receives skeletonize() output from
    # classify_mmsdm / classify_nemde, so it MUST strip <dN> form too.
    assert extract_patterns.aux_id_from_filename_template("nemlogo<d1>.gif") == "nemlogo_gif"
    assert extract_patterns.aux_id_from_filename_template("background<d1>.gif") == "background_gif"


def test_aux_id_skeleton_tokens_stripped_curly_form():
    # label_digit_positions() emits {year} / {yearmonth} / {d1}. Helper may
    # receive either form depending on call site; strip both.
    assert extract_patterns.aux_id_from_filename_template("nemlogo{d1}.gif") == "nemlogo_gif"
    assert (
        extract_patterns.aux_id_from_filename_template("marketnoticedata_{yearmonth}.par")
        == "marketnoticedata_par"
    )


def test_aux_id_pipeline_via_skeletonize():
    # End-to-end: the actual call pattern classify_mmsdm uses.
    raw = "nemlogo1.gif"
    assert (
        extract_patterns.aux_id_from_filename_template(extract_patterns.skeletonize(raw))
        == "nemlogo_gif"
    )


def test_aux_id_multi_dot_filename():
    assert (
        extract_patterns.aux_id_from_filename_template("Participant_Monthly_DVD.doc")
        == "Participant_Monthly_DVD_doc"
    )
    assert (
        extract_patterns.aux_id_from_filename_template("monthlydvd_tables.bat")
        == "monthlydvd_tables_bat"
    )


def test_aux_id_empty_after_strip_falls_back():
    # Defensive: all-token filename (would produce empty string otherwise).
    assert extract_patterns.aux_id_from_filename_template("{token}") == "AUX"
    assert extract_patterns.aux_id_from_filename_template("<d4>") == "AUX"


# ---------- MONTH_ROOT_AUX / SQLLOADER_AUX / DOCUMENTATION_AUX / MARKETNOTICEDATA ----------


def test_classify_mmsdm_month_root_autorun_inf_promoted():
    url = "/Data_Archive/Wholesale_Electricity/MMSDM/2009/MMSDM_2009_07/AUTORUN.INF"
    result = extract_patterns.classify(url, "AUTORUN.INF")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "MMSDM"
    assert tier == "MONTH_ROOT_AUX"
    assert intra == "AUTORUN_INF"


def test_classify_mmsdm_month_root_case_variants_stay_distinct():
    # Byte-exact: two real case variants must emit distinct intra_repo_ids.
    url_cap = "/Data_Archive/Wholesale_Electricity/MMSDM/2009/MMSDM_2009_07/Readme.htm"
    url_low = "/Data_Archive/Wholesale_Electricity/MMSDM/2009/MMSDM_2009_07/readme.htm"
    _, _, cap_id, _ = extract_patterns.classify(url_cap, "Readme.htm")
    _, _, low_id, _ = extract_patterns.classify(url_low, "readme.htm")
    assert cap_id == "Readme_htm"
    assert low_id == "readme_htm"
    assert cap_id != low_id


def test_classify_mmsdm_sqlloader_root_file_promoted():
    # Files directly under MMSDM_Historical_Data_SQLLoader/ (not in a view subdir)
    url = (
        "/Data_Archive/Wholesale_Electricity/MMSDM/2009/MMSDM_2009_07/"
        "MMSDM_Historical_Data_SQLLoader/README.txt"
    )
    result = extract_patterns.classify(url, "README.txt")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "MMSDM"
    assert tier == "SQLLOADER_AUX"
    assert intra == "README_txt"


def test_classify_mmsdm_documentation_marketnoticedata_promoted():
    url = (
        "/Data_Archive/Wholesale_Electricity/MMSDM/2011/MMSDM_2011_06/"
        "MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/marketnoticedata_201106.par"
    )
    result = extract_patterns.classify(url, "marketnoticedata_201106.par")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "MMSDM"
    assert tier == "DOCUMENTATION"
    assert intra == "MARKETNOTICEDATA"


def test_classify_mmsdm_documentation_aux_other_files_stem_derived():
    url = (
        "/Data_Archive/Wholesale_Electricity/MMSDM/2011/MMSDM_2011_06/"
        "MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/Participant_Monthly_DVD.pdf"
    )
    result = extract_patterns.classify(url, "Participant_Monthly_DVD.pdf")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "MMSDM"
    assert tier == "DOCUMENTATION_AUX"
    assert intra == "Participant_Monthly_DVD_pdf"


# ---------- MTPASA_DATA_EXPORT split ----------


def test_classify_mmsdm_mtpasa_regionavail_trk_promoted():
    url = (
        "/Data_Archive/Wholesale_Electricity/MMSDM/MTPASA_DATA_EXPORT/"
        "PUBLIC_MTPASA_REGIONAVAIL_TRK_20191024093822_NEM02.zip"
    )
    result = extract_patterns.classify(
        url, "PUBLIC_MTPASA_REGIONAVAIL_TRK_20191024093822_NEM02.zip"
    )
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "MMSDM"
    assert tier == "MTPASA_DATA_EXPORT"
    assert intra == "MTPASA_REGIONAVAIL_TRK"


def test_classify_mmsdm_mtpasa_regionavailability_promoted():
    url = (
        "/Data_Archive/Wholesale_Electricity/MMSDM/MTPASA_DATA_EXPORT/"
        "2014_DATA_EXPORT_MTPASA_REGIONAVAILABILITY.zip"
    )
    result = extract_patterns.classify(url, "2014_DATA_EXPORT_MTPASA_REGIONAVAILABILITY.zip")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "MMSDM"
    assert tier == "MTPASA_DATA_EXPORT"
    assert intra == "MTPASA_REGIONAVAILABILITY"


def test_classify_mmsdm_mms_data_model_versioned_preserved():
    # Regression guard: the existing MMS%20Data%20Model/v<x> branch must stay.
    url = (
        "/Data_Archive/Wholesale_Electricity/MMSDM/2011/MMSDM_2011_06/"
        "MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS%20Data%20Model/v5.1/index.htm"
    )
    result = extract_patterns.classify(url, "index.htm")
    assert result is not None
    repo, tier, intra, extras = result
    assert repo == "MMSDM"
    assert tier == "DOCUMENTATION"
    assert intra == "MMS_DATA_MODEL_v5.1"
    assert extras == {"mms_version": "v5.1"}


# ---------- NEMDE ----------


def test_classify_nemde_monthly_bulk_zip_promoted():
    url = "/Data_Archive/Wholesale_Electricity/NEMDE/2009/NEMDE_2009_07.zip"
    result = extract_patterns.classify(url, "NEMDE_2009_07.zip")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "NEMDE"
    assert tier == "MONTHLY_BULK"
    assert intra == "NEMDE_MONTHLY_BULK"


def test_classify_nemde_month_root_aux_promoted_by_filename():
    url = "/Data_Archive/Wholesale_Electricity/NEMDE/2009/NEMDE_2009_07/AUTORUN.INF"
    result = extract_patterns.classify(url, "AUTORUN.INF")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "NEMDE"
    assert tier == "ROOT_AUX"
    assert intra == "AUTORUN_INF"


def test_classify_nemde_readme_case_variants_stay_distinct():
    # Readme.htm (115 files) and readme.htm (1 file) — byte-exact casing.
    url_cap = "/Data_Archive/Wholesale_Electricity/NEMDE/2014/NEMDE_2014_12/Readme.htm"
    url_low = "/Data_Archive/Wholesale_Electricity/NEMDE/2014/NEMDE_2014_12/readme.htm"
    _, _, cap_id, _ = extract_patterns.classify(url_cap, "Readme.htm")
    _, _, low_id, _ = extract_patterns.classify(url_low, "readme.htm")
    assert cap_id != low_id


def test_classify_nemde_market_data_aux_subtree_distinct_tier():
    # Files under NEMDE_Market_Data/ (not the NEMDE_Files / File_Readers
    # subtree) get tier = MARKET_DATA_AUX.
    url = (
        "/Data_Archive/Wholesale_Electricity/NEMDE/2009/NEMDE_2009_07/"
        "NEMDE_Market_Data/disclaimer.htm"
    )
    result = extract_patterns.classify(url, "disclaimer.htm")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "NEMDE"
    assert tier == "MARKET_DATA_AUX"
    assert intra == "disclaimer_htm"


def test_classify_nemde_preserves_nemde_files_subtree():
    # Regression guard: the NEMDE_Files subtree branch must still work.
    url = (
        "/Data_Archive/Wholesale_Electricity/NEMDE/2014/NEMDE_2014_12/"
        "NEMDE_Market_Data/NEMDE_Files/NemPriceSetter_20141201_xml.zip"
    )
    result = extract_patterns.classify(url, "NemPriceSetter_20141201_xml.zip")
    assert result is not None
    repo, tier, intra, _ = result
    assert repo == "NEMDE"
    assert tier == "NEMDE_Files"
    assert intra == "NemPriceSetter"
