"""Parse AEMO MMSDM Upgrade Report text dumps into a per-version table-change CSV.

The Upgrade Report PDFs are CHANGE-LOGS, not full schema dumps — each PDF lists
only the tables that changed in that version (added or modified). Per-table
detail sections include AEMO's own "Visibility" classification:

  Public                       — all participants have access
  Private                      — confidential to the participant
  Private, Public Next-Day     — confidential until 4am next day
  Private & Public             — mixed

This is the authoritative public/private boundary for each table at the time
the version shipped. We pair it with the table-change list to produce a
reviewable per-version timeline.

Source: pre-extracted PDF text at
`reference/aemo-mmsdm-docs/_extracted/upgrade-reports/<version>.txt`
(written by `scripts/extract_mmsdm_upgrade_reports.py`).

Coverage: 12 versions (all except v5.3_PreRelease, which ships no upgrade report).

Naming drift handled in upstream script: `MMS_Data_Model_Upgrade_Report.pdf`
(v4.26-v5.3) → `Electricity_Data_Model_Upgrade_Report.pdf` (v5.4-v5.6).

Usage:

    python scripts/extract_mmsdm_upgrade_tables.py \\
        --reports-root reference/aemo-mmsdm-docs/_extracted/upgrade-reports \\
        --out reference/MMSDM-UPGRADE-TABLES.csv

The `change_type` column is INTENTIONALLY empty here: this script extracts what
the PDF says about each version in isolation. Cross-version diffing to assign
ADDED / MODIFIED / REMOVED is a downstream synthesis step (see
`scripts/build_mmsdm_table_timeline.py`).
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# Body-section table header: e.g. "6.3 Table: DUDETAIL". TOC also has "Table: NAME ...... 28"
# but the body version starts with a section number and is followed by a Name/Comment block.
# Match BOTH and dedupe by table-name later.
TABLE_HEADER_RE = re.compile(
    r"^\s*(?:(\d+\.\d+(?:\.\d+)?)\s+)?Table:\s+([A-Z][A-Z0-9_]+)\s*$",
    re.MULTILINE,
)

# Section header for packages, body form: "3 Package: DEMAND_FORECASTS"
PACKAGE_HEADER_RE = re.compile(
    r"^\s*(\d+)\s+Package:\s+([A-Z][A-Z0-9_]+)\s*$",
    re.MULTILINE,
)

# Visibility values per AEMO §2.1. Order matters — match longest first so
# "Private, Public Next-Day" wins over "Private" / "Public".
VISIBILITY_VALUES = (
    "Private, Public Next-Day",
    "Private & Public",
    "Public",
    "Private",
)
# pymupdf line breaks split the Visibility table cells across multiple lines:
#   Visibility
#   <blank>
#   Public
# So search for "Visibility" followed within ~5 lines by a known value.
VISIBILITY_AFTER_LABEL_RE = re.compile(
    r"Visibility\s*\n(?:\s*\n)?\s*(" + "|".join(re.escape(v) for v in VISIBILITY_VALUES) + r")\b",
    re.MULTILINE,
)


def find_packages(text: str) -> list[tuple[int, str]]:
    """Return list of (char_offset, package_name) for body-form package headers."""
    return [(m.start(), m.group(2)) for m in PACKAGE_HEADER_RE.finditer(text)]


def find_table_sections(text: str) -> list[tuple[int, str | None, str]]:
    """Return list of (char_offset, section_number_or_none, table_name).

    Filters out TOC entries (no section number prefix) when a body-form
    duplicate exists for the same table.
    """
    matches = [(m.start(), m.group(1), m.group(2)) for m in TABLE_HEADER_RE.finditer(text)]
    body_tables = {t for _, sec, t in matches if sec}
    # Keep all body-form (sec is non-None). Keep TOC-form only for tables with no body
    # entry (defensive — should be rare; means PDF reference exists in TOC but body
    # section was missed by the regex).
    out = [(o, s, t) for o, s, t in matches if s] + [
        (o, None, t) for o, s, t in matches if s is None and t not in body_tables
    ]
    out.sort()
    return out


def package_for_offset(packages: list[tuple[int, str]], offset: int) -> str:
    """Return the package name covering the given char offset (body-form scan)."""
    pkg = ""
    for off, name in packages:
        if off <= offset:
            pkg = name
        else:
            break
    return pkg


def extract_visibility_for_section(text: str, start: int, end: int) -> str:
    """Search for AEMO Visibility marker within [start, end). Return '' if absent."""
    m = VISIBILITY_AFTER_LABEL_RE.search(text, start, end)
    return m.group(1) if m else ""


def parse_one_report(text: str, version: str) -> list[tuple[str, str, str, str, int | None]]:
    """Return list of (version, package, table, visibility, page_hint)."""
    packages = find_packages(text)
    sections = find_table_sections(text)

    rows: list[tuple[str, str, str, str, int | None]] = []
    seen: set[tuple[str, str]] = set()

    for i, (offset, _sec, table) in enumerate(sections):
        # Window for visibility lookup: from this table header to the next table header
        # (or end of document). Avoids cross-table contamination.
        next_offset = sections[i + 1][0] if i + 1 < len(sections) else len(text)
        visibility = extract_visibility_for_section(text, offset, next_offset)
        package = package_for_offset(packages, offset)

        # Best-effort page hint by counting "=== PAGE n ===" markers up to this offset.
        prefix = text[:offset]
        page_marks = re.findall(r"=== PAGE (\d+) ===", prefix)
        page_hint = int(page_marks[-1]) if page_marks else None

        key = (version, table)
        if key in seen:
            continue  # dedupe across TOC + body if both leaked through
        seen.add(key)
        rows.append((version, package, table, visibility, page_hint))

    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--reports-root", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    txts = sorted(args.reports_root.glob("*.txt"))
    if not txts:
        print(f"ERROR: no .txt files under {args.reports_root}", file=sys.stderr)
        return 2

    all_rows: list[tuple[str, str, str, str, int | None]] = []
    summary: list[tuple[str, int, int]] = []  # (version, tables, with_visibility)

    for txt in txts:
        version = txt.stem
        text = txt.read_text(encoding="utf-8", errors="replace")
        rows = parse_one_report(text, version)
        with_vis = sum(1 for r in rows if r[3])
        summary.append((version, len(rows), with_vis))
        all_rows.extend(rows)
        print(f"{version:20s} {len(rows):4d} tables ({with_vis} with visibility tag)")

    all_rows.sort()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["version", "package", "table", "visibility", "page_hint"])
        for v, p, t, vis, pg in all_rows:
            w.writerow([v, p, t, vis, "" if pg is None else pg])

    print(f"\nTotal rows: {len(all_rows):,} -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
