"""Extract text from AEMO MMSDM Upgrade Report PDFs across all schema versions.

AEMO ships an "Upgrade Report" PDF with each MMSDM release that lists per-table
schema changes (added / modified / removed). PDFs span 12 of 13 captured
versions; v5.3_PreRelease ships no upgrade report (it is a migration-only
release containing the BidOffer rename SQL kit).

Naming drift across versions:
  v4.26 - v5.3   MMS_Data_Model_Upgrade_Report.pdf
  v5.4 - v5.6    Electricity_Data_Model_Upgrade_Report.pdf
  v5.3_PreRelease  none

Phase 1 (this script): dump raw extracted text per version into the gitignored
`reference/aemo-mmsdm-docs/_extracted/upgrade-reports/<ver>.txt` workspace so
the actual section structure can be inspected before designing a parser.
A subsequent script will parse the dumps into a per-table-per-version timeline.

Usage:

    uv run --with pymupdf python scripts/extract_mmsdm_upgrade_reports.py \\
        --docs-root reference/aemo-mmsdm-docs \\
        --out-root reference/aemo-mmsdm-docs/_extracted/upgrade-reports
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

UPGRADE_REPORT_NAMES = (
    "MMS_Data_Model_Upgrade_Report.pdf",
    "Electricity_Data_Model_Upgrade_Report.pdf",
)


def find_upgrade_report(version_dir: Path) -> Path | None:
    for name in UPGRADE_REPORT_NAMES:
        p = version_dir / name
        if p.is_file():
            return p
    return None


def extract_pdf_text(pdf_path: Path) -> tuple[int, str]:
    import pymupdf  # imported here so --help works without pymupdf installed

    doc = pymupdf.open(str(pdf_path))
    pages: list[str] = []
    for i, page in enumerate(doc, start=1):
        pages.append(f"\n=== PAGE {i} ===\n")
        pages.append(page.get_text("text"))
    text = "".join(pages)
    return len(doc), text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--docs-root", type=Path, required=True)
    ap.add_argument("--out-root", type=Path, required=True)
    args = ap.parse_args()

    version_dirs = sorted(
        p for p in args.docs_root.iterdir() if p.is_dir() and p.name.startswith("v")
    )
    if not version_dirs:
        print(f"ERROR: no version dirs found under {args.docs_root}", file=sys.stderr)
        return 2

    args.out_root.mkdir(parents=True, exist_ok=True)

    found = 0
    missing: list[str] = []
    for vd in version_dirs:
        pdf = find_upgrade_report(vd)
        if pdf is None:
            missing.append(vd.name)
            continue
        pages, text = extract_pdf_text(pdf)
        out = args.out_root / f"{vd.name}.txt"
        header = (
            f"# Source: {pdf.relative_to(args.docs_root.parent)}\n"
            f"# Pages: {pages}\n"
            f"# Bytes (source PDF): {pdf.stat().st_size}\n\n"
        )
        out.write_text(header + text, encoding="utf-8")
        print(f"{vd.name:20s} {pages:4d} pages -> {out}")
        found += 1

    print(f"\nExtracted {found} reports; missing for: {', '.join(missing) or '(none)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
