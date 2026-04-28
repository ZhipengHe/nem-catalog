"""Integration regression: every non-AUX CSV row maps to a record in catalog.json.

This test pins the issue #22 acceptance criterion:
"All 474 previously-collapsed groups surface their full tier records."

Approach A: reads the committed catalog.json — deterministic and fast (< 1s).
The catalog.json was regenerated in Task 6 (schema_version 2.0.0) and reflects
every non-AUX row from reference/URL-CONVENTIONS.csv.
"""

import csv
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Classifier labels that indicate auxiliary / non-dataset rows in the CSV.
# These are excluded from the catalog and must not be asserted.
AUX = {
    "UNPARSED",
    "UNKNOWN",
    "ROOT_AUX",
    "SQLLOADER_AUX",
    "MONTH_ROOT_AUX",
    "DOCUMENTATION_AUX",
    "MMSDM_MONTHLY_BULK",
    "MTPASA_DATA_EXPORT",
}


def test_every_non_aux_csv_row_maps_to_a_record():
    """Every non-AUX row in URL-CONVENTIONS.csv has a matching record in catalog.json."""
    csv_path = REPO_ROOT / "reference" / "URL-CONVENTIONS.csv"
    catalog_path = REPO_ROOT / "catalog.json"

    rows = list(csv.DictReader(csv_path.open()))
    catalog = json.loads(catalog_path.read_text())

    # Sanity: catalog is v2.0.0 with a reasonable dataset count.
    assert catalog["schema_version"] == "2.0.0", (
        f"catalog.json should be v2.0.0, got {catalog['schema_version']!r}"
    )
    assert len(catalog["datasets"]) >= 442, (
        f"expected at least 442 datasets, got {len(catalog['datasets'])}"
    )

    non_aux_rows = [r for r in rows if r["intra_repo_id"] not in AUX]
    assert len(non_aux_rows) > 0, "expected non-zero non-AUX rows in CSV"

    unmatched = []
    for row in non_aux_rows:
        key = f"{row['repo']}:{row['intra_repo_id']}"
        ds = catalog["datasets"].get(key)
        if ds is None:
            unmatched.append({"reason": "dataset key absent", "row": row})
            continue
        tier_recs = ds["tiers"].get(row["retention_tier"])
        if tier_recs is None:
            unmatched.append({"reason": f"tier {row['retention_tier']} absent", "row": row})
            continue
        # Match on (path_template, filename_template); treat None == "" for
        # directory-level anomalies that have no filename_template.
        match = any(
            rec.get("path_template") == row["path_template"]
            and (rec.get("filename_template") or "") == (row.get("filename_template") or "")
            for rec in tier_recs
        )
        if not match:
            unmatched.append({"reason": "no record matches (path, filename)", "row": row})

    assert not unmatched, (
        f"{len(unmatched)} of {len(non_aux_rows)} non-AUX rows unmatched in catalog.json. "
        f"First 5: {unmatched[:5]}"
    )
