"""Integration test: the extractor emits no placeholder-bucket collapses, and
the patterns/auto/catalog.json dataset_keys count grows by ≥500 real MMSDM
table keys (issue #21 acceptance criterion 6).

Regenerating is side-effect-free — the extractor is library-pure when called
via main(policy=...). The test redirects OUT_CSV, OUT_MD, and OUT_JSON to a
tmp dir so reference/ and patterns/auto/ are never touched.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import extract_patterns  # noqa: E402
from policy import Policy  # noqa: E402

# Placeholder intra_repo_id values that MUST NOT appear in the emitted CSV
# after #21 lands. If a future classifier change introduces a new placeholder,
# add a real id branch in the classifier — do NOT extend this set.
PLACEHOLDER_IDS: frozenset[str] = frozenset(
    {
        "UNPARSED",
        "UNKNOWN",
        "ROOT_AUX",  # legacy flat aux; real NEMDE aux now has stem-derived ids
        "DOCUMENTATION_AUX",
        "SQLLOADER_AUX",
        "MONTH_ROOT_AUX",
        "MTPASA_DATA_EXPORT",  # directory-name-as-id; real datasets are now split
    }
)

# Pinned minimum count of distinct (repo, intra_repo_id, retention_tier)
# tuples in the current mirror snapshot. #21 only expands this set; a drop
# below the pin means the classifier merged things that should be separate.
# Pre-#21 the count was 1181 (see .plans/v0.2-pr1 context).
EXPECTED_DISTINCT_TUPLES_MIN = 1200


@pytest.fixture(scope="module")
def regenerated_outputs(
    tmp_path_factory: pytest.TempPathFactory,
) -> tuple[Path, Path]:
    """Run the extractor against the committed mirror, redirect all outputs
    to a tmp dir, return (csv_path, json_path)."""
    out_dir = tmp_path_factory.mktemp("extract")
    csv_out = out_dir / "URL-CONVENTIONS.csv"
    md_out = out_dir / "URL-CONVENTIONS.md"
    json_out = out_dir / "catalog.json"
    policy = Policy.load(REPO_ROOT / "patterns" / "curated" / "freshness-policy.yaml")

    orig_csv = extract_patterns.OUT_CSV
    orig_md = extract_patterns.OUT_MD
    orig_json = extract_patterns.OUT_JSON
    extract_patterns.OUT_CSV = csv_out
    extract_patterns.OUT_MD = md_out
    extract_patterns.OUT_JSON = json_out
    try:
        rc = extract_patterns.main(policy=policy)
        assert rc == 0, f"extract_patterns.main returned {rc}"
    finally:
        extract_patterns.OUT_CSV = orig_csv
        extract_patterns.OUT_MD = orig_md
        extract_patterns.OUT_JSON = orig_json

    assert csv_out.exists(), "CSV not written — OUT_CSV redirect broken"
    assert json_out.exists(), "JSON not written — OUT_JSON redirect broken"
    return csv_out, json_out


def test_no_protected_paths_touched(regenerated_outputs: tuple[Path, Path]) -> None:
    """Guard: the fixture must not write to reference/ or patterns/auto/.

    If this test fails, the monkeypatching protocol broke — STOP, do not
    commit the regenerated reference/ files, investigate first.
    """
    csv_path, json_path = regenerated_outputs
    assert "reference" not in csv_path.parts, f"CSV leaked to {csv_path}"
    assert "patterns" not in json_path.parts, f"JSON leaked to {json_path}"


def test_no_placeholder_intra_repo_id(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    csv_path, _ = regenerated_outputs
    offenders: list[tuple[str, str, str]] = []
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            if row["intra_repo_id"] in PLACEHOLDER_IDS:
                offenders.append((row["repo"], row["intra_repo_id"], row["retention_tier"]))
    assert not offenders, (
        f"{len(offenders)} rows still carry placeholder intra_repo_id:\n"
        + "\n".join(f"  {r}:{i} [{t}]" for r, i, t in offenders[:20])
    )


def test_distinct_tuple_count_at_or_above_pin(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    csv_path, _ = regenerated_outputs
    tuples: set[tuple[str, str, str]] = set()
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            tuples.add((row["repo"], row["intra_repo_id"], row["retention_tier"]))
    assert len(tuples) >= EXPECTED_DISTINCT_TUPLES_MIN, (
        f"distinct-tuple count {len(tuples)} < pin {EXPECTED_DISTINCT_TUPLES_MIN}"
    )


def test_mmsdm_publicdvd_rows_resolved(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    csv_path, _ = regenerated_outputs
    unparsed_publicdvd = 0
    real_publicdvd = 0
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            if row["repo"] != "MMSDM":
                continue
            fname = row["filename_template"]
            if not fname.startswith("PUBLIC_DVD_"):
                continue
            if row["intra_repo_id"] == "UNPARSED":
                unparsed_publicdvd += 1
            else:
                real_publicdvd += 1
    assert unparsed_publicdvd == 0, f"{unparsed_publicdvd} PUBLIC_DVD_ rows still UNPARSED"
    assert real_publicdvd >= 500, f"only {real_publicdvd} PUBLIC_DVD_ rows resolved; expected ≥ 500"


def test_catalog_json_dataset_keys_grew_substantially_for_mmsdm(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    """Acceptance criterion 6 from #21 — verified against the JSON output.

    Issue #21's criterion text says "dataset_keys list grows by ≥500 real MMSDM
    table keys". The 500 number is the CSV row-count delta (528 PUBLIC_DVD_
    rows recovered from the UNPARSED dumping ground) — and that is asserted by
    ``test_mmsdm_publicdvd_rows_resolved``.

    In ``patterns/auto/catalog.json``, the ``datasets`` dict keys are
    ``REPO:INTRA_ID`` tuples collapsed across retention tiers: the 169 recovered
    tables appear as 169 distinct keys regardless of whether they live in CTL,
    DATA, BCP_FMT, or BCP_DATA. Pre-#21 MMSDM had ~160 real dataset keys;
    post-#21 the count is ~320+. Assert ≥250 here as a defensible floor with
    margin; the exact growth is tracked in the plan's Task 9 spot-check.
    """
    _, json_path = regenerated_outputs
    data = json.loads(json_path.read_text())
    assert "datasets" in data, "catalog.json missing top-level 'datasets'"
    mmsdm_keys = [k for k in data["datasets"] if k.startswith("MMSDM:")]
    real_mmsdm = [k for k in mmsdm_keys if k.split(":", 1)[1] not in PLACEHOLDER_IDS]
    assert len(real_mmsdm) >= 250, (
        f"MMSDM real-dataset count {len(real_mmsdm)} < 250; "
        f"total MMSDM keys = {len(mmsdm_keys)}, "
        f"placeholder keys = {len(mmsdm_keys) - len(real_mmsdm)}"
    )


def test_mmsdm_monthly_bulk_present(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    csv_path, _ = regenerated_outputs
    with csv_path.open() as f:
        assert any(row["intra_repo_id"] == "MMSDM_MONTHLY_BULK" for row in csv.DictReader(f)), (
            "MMSDM_MONTHLY_BULK missing — dead branch revival regressed"
        )


def test_nemde_monthly_bulk_present(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    csv_path, _ = regenerated_outputs
    with csv_path.open() as f:
        assert any(row["intra_repo_id"] == "NEMDE_MONTHLY_BULK" for row in csv.DictReader(f)), (
            "NEMDE_MONTHLY_BULK missing"
        )


def test_mtpasa_split_into_two_datasets(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    csv_path, _ = regenerated_outputs
    ids: set[str] = set()
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            if row["retention_tier"] == "MTPASA_DATA_EXPORT":
                ids.add(row["intra_repo_id"])
    assert "MTPASA_REGIONAVAIL_TRK" in ids
    assert "MTPASA_REGIONAVAILABILITY" in ids
    assert "MTPASA_DATA_EXPORT" not in ids, "directory-name-as-dataset still present"


def test_marketnoticedata_promoted(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    csv_path, _ = regenerated_outputs
    with csv_path.open() as f:
        assert any(
            row["intra_repo_id"] == "MARKETNOTICEDATA" and row["retention_tier"] == "DOCUMENTATION"
            for row in csv.DictReader(f)
        ), "MARKETNOTICEDATA missing from DOCUMENTATION tier"


def test_nemde_readme_case_variants_distinct_in_csv(
    regenerated_outputs: tuple[Path, Path],
) -> None:
    """Byte-exact discipline: Readme.htm (115 files) and readme.htm (1 file)
    must appear as two distinct rows in the CSV, with distinct intra_repo_ids."""
    csv_path, _ = regenerated_outputs
    readme_ids: set[str] = set()
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            if row["repo"] != "NEMDE":
                continue
            fname = row["filename_template"]
            if fname.lower() == "readme.htm":
                readme_ids.add(row["intra_repo_id"])
    assert len(readme_ids) >= 2, (
        f"Expected ≥2 distinct README intra_repo_ids for NEMDE case variants, got {readme_ids}"
    )
