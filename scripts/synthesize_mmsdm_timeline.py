"""Synthesize MMSDM table-change timeline + §6 rename verification report.

Reads:
  reference/MMSDM-DDL-COLUMNS.csv      (per-table-per-version columns, v5.2+)
  reference/MMSDM-DDL-RENAMES.csv      (sp_rename evidence, v5.3 + v5.5)
  reference/MMSDM-UPGRADE-TABLES.csv   (per-version table-change list, all 12 versions)
  reference/MMSDM-TABLE-LIFECYCLE.csv  (mirror-walk lifecycle, all 278 tables)

Writes:
  reference/MMSDM-TABLE-TIMELINE.csv   (per-(table, version) action row)
  reference/MMSDM-RENAMES-VERIFICATION.md  (§6 hypothesis verdicts + new findings)

Action classification per (table, version):
  ADDED       — first time the table appears in any DDL; or first appearance in
                upgrade-report change-list with no prior DDL or report mention.
  MODIFIED    — table appears in upgrade-report change-list but is not first-seen.
  REMOVED     — table present in DDL for version N-1 and absent in DDL for N.
                Only computable across DDL-covered versions (v5.2 onwards).
  RENAMED_FROM/RENAMED_TO — table is the source/target of an sp_rename call.

§6 rename hypothesis verdicts:
  CONFIRMED        — sp_rename or AEMO-shipped migration kit is the evidence.
  DDL-INFERRED     — predecessor disappears + successor appears in same DDL transition,
                     and column shapes overlap above a threshold.
  REPORT-INFERRED  — same shape from upgrade-report change-list (used for pre-v5.2).
  LIFECYCLE-MATCH  — only mirror-walk lifecycle months align; weakest signal.
  NOT-VERIFIABLE   — no available source contradicts or supports the hypothesis.

Usage:

    python scripts/synthesize_mmsdm_timeline.py \\
        --columns reference/MMSDM-DDL-COLUMNS.csv \\
        --renames reference/MMSDM-DDL-RENAMES.csv \\
        --upgrade reference/MMSDM-UPGRADE-TABLES.csv \\
        --lifecycle reference/MMSDM-TABLE-LIFECYCLE.csv \\
        --timeline-out reference/MMSDM-TABLE-TIMELINE.csv \\
        --report-out reference/MMSDM-RENAMES-VERIFICATION.md
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

# --------------------------------------------------------------------------------------
# §6 hypotheses (transcribed from reference/MMSDM-TABLE-LIFECYCLE.md §6).
# Updating §6 markdown? Update this list to keep verdicts in sync.
# --------------------------------------------------------------------------------------
HYPOTHESES: list[dict] = [
    {
        "id": "H1-BIDOFFERPERIOD",
        "successors": ["BIDOFFERPERIOD"],
        "predecessors": ["BIDPEROFFER1", "BIDPEROFFER2"],
        "transition_yyyymm": 202408,
        "stated_confidence": "AEMO-CONFIRMED",
        "stated_evidence": "v5.3_PreRelease/MMSDM_Switch_Bidoffer_Table_Names_v1.1.zip",
    },
    {
        "id": "H2-MTPASA_CONSTRAINT",
        "successors": ["MTPASA_CONSTRAINTRESULT", "MTPASA_CONSTRAINTSUMMARY"],
        "predecessors": ["MTPASA_CONSTRAINTSOLUTION"],
        "transition_yyyymm": 201805,
        "stated_confidence": "HIGH",
        "stated_evidence": "v4.27 upgrade report (covers 2018 schema changes)",
    },
    {
        "id": "H3-MTPASA_INTERCONNECTOR",
        "successors": ["MTPASA_INTERCONNECTORRESULT"],
        "predecessors": ["MTPASA_INTERCONNECTORSOLUTION"],
        "transition_yyyymm": 201805,
        "stated_confidence": "HIGH",
        "stated_evidence": "v4.27 upgrade report",
    },
    {
        "id": "H4-MTPASA_REGION",
        "successors": ["MTPASA_REGIONRESULT", "MTPASA_REGIONSUMMARY", "MTPASA_REGIONITERATION"],
        "predecessors": ["MTPASA_REGIONSOLUTION"],
        "transition_yyyymm": 201805,
        "stated_confidence": "HIGH",
        "stated_evidence": "v4.27 upgrade report",
    },
    {
        "id": "H5-MTPASA_LOLP",
        "successors": ["MTPASA_LOLPRESULT"],
        "predecessors": ["MTPASA_RESERVELIMITSOLUTION"],
        "transition_yyyymm": 201805,
        "stated_confidence": "MEDIUM",
        "stated_evidence": "v4.27/v4.28 DOCUMENTATION HTMs (column-match)",
    },
    {
        "id": "H6-P5MIN_CONSTRAINTSOLUTION",
        "successors": ["P5MIN_CONSTRAINTSOLUTION"],
        "predecessors": [
            "P5MIN_CONSTRAINTSOLUTION1",
            "P5MIN_CONSTRAINTSOLUTION2",
            "P5MIN_CONSTRAINTSOLUTION3",
            "P5MIN_CONSTRAINTSOLUTION4",
        ],
        "transition_yyyymm": 202408,
        "stated_confidence": "HIGH",
        "stated_evidence": "v5.3 upgrade DDL",
        "consolidation_note": "Single unified table absorbs four numbered variants.",
    },
    {
        "id": "H7-P5MIN_SCENARIODEMAND",
        "successors": ["P5MIN_SCENARIODEMAND"],
        "predecessors": ["P5MINSCENARIODEMAND"],
        "transition_yyyymm": 202408,
        "stated_confidence": "VERY HIGH",
        "stated_evidence": "v5.3 upgrade DDL (underscore added)",
    },
    {
        "id": "H8-P5MIN_SCENARIODEMANDTRK",
        "successors": ["P5MIN_SCENARIODEMANDTRK"],
        "predecessors": ["P5MINSCENARIODEMANDTRK"],
        "transition_yyyymm": 202408,
        "stated_confidence": "VERY HIGH",
        "stated_evidence": "v5.3 upgrade DDL (underscore added)",
    },
    {
        "id": "H9-PREDISPATCH-D-DROP",
        "successors": [
            "PREDISPATCHCONSTRAINT",
            "PREDISPATCHINTERCONNECTORRES",
            "PREDISPATCHLOAD",
            "PREDISPATCHPRICE",
            "PREDISPATCHPRICESENSITIVITIES",
            "PREDISPATCHREGIONSUM",
            "PREDISPATCHSCENARIODEMAND",
            "PREDISPATCHSCENARIODEMANDTRK",
        ],
        "predecessors": [
            "PREDISPATCHCONSTRAINT_D",
            "PREDISPATCHINTERCONNECTORRES_D",
            "PREDISPATCHLOAD_D",
            "PREDISPATCHPRICE_D",
            "PREDISPATCHPRICESENSITIVITIES_D",
            "PREDISPATCHREGIONSUM_D",
            "PREDISPATCHSCENARIODEMAND_D",
            "PREDISPATCHSCENARIODEMANDTRK_D",
        ],
        "transition_yyyymm": 202408,
        "stated_confidence": "MEDIUM",
        "stated_evidence": "v5.3 DDL + upgrade-report cross-check",
        "consolidation_note": (
            "NOT a rename — _D variants dropped at 2024-08, "
            "base existed in parallel throughout DVD era."
        ),
    },
    {
        "id": "H10-DISPATCHLOAD-VS-TRADINGLOAD",
        "successors": ["DISPATCHLOAD", "DISPATCHREGIONSUM"],
        "predecessors": ["TRADINGLOAD", "TRADINGREGIONSUM"],
        "transition_yyyymm": 202109,
        "stated_confidence": "HIGH",
        "stated_evidence": "v5.0/v5.1 5MS technical specifications",
        "consolidation_note": (
            "5-min vs 30-min interval change; not a strict rename, an interval-resolution shift."
        ),
    },
    {
        "id": "H11-DISPATCHINTERCONNECTORRES",
        "successors": ["DISPATCHINTERCONNECTORRES"],
        "predecessors": ["INTERCONNMWFLOW"],
        "transition_yyyymm": 202105,
        "stated_confidence": "MEDIUM",
        "stated_evidence": "v5.0 upgrade report",
    },
    {
        "id": "H12-MARKET_SUSPEND",
        "successors": [
            "MARKET_SUSPEND_REGIME_SUM",
            "MARKET_SUSPEND_REGION_SUM",
            "MARKET_SUSPEND_SCHEDULE",
            "MARKET_SUSPEND_SCHEDULE_TRK",
        ],
        "predecessors": ["MARKETNOTICEDATA"],
        "transition_yyyymm": 202408,
        "stated_confidence": "LOW",
        "stated_evidence": "v5.3 DDL / upgrade-report (likely NOT a rename)",
        "consolidation_note": "Thematic match only; orthogonal capability rather than rename.",
    },
]


# --------------------------------------------------------------------------------------
# Data classes
# --------------------------------------------------------------------------------------
@dataclass
class TableLifecycle:
    table: str
    lifecycle_class: str
    first_month: int
    last_month: int


@dataclass
class TimelineRow:
    table: str
    version: str
    action: str  # ADDED | MODIFIED | REMOVED | RENAMED_FROM | RENAMED_TO
    package: str = ""
    visibility: str = ""
    source: str = ""  # ddl | upgrade-report | sp_rename
    note: str = ""


# --------------------------------------------------------------------------------------
# Loaders
# --------------------------------------------------------------------------------------
def load_columns(path: Path) -> dict[str, dict[str, list[dict]]]:
    """Return {version: {table: [column_dict, ...]}}."""
    out: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    with path.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[r["version"]][r["table"]].append(r)
    return out


def load_renames(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_upgrade_tables(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_lifecycle(path: Path) -> dict[str, TableLifecycle]:
    out: dict[str, TableLifecycle] = {}
    with path.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[r["table"]] = TableLifecycle(
                table=r["table"],
                lifecycle_class=r["lifecycle_class"],
                first_month=int(r["first_month"]),
                last_month=int(r["last_month"]),
            )
    return out


# --------------------------------------------------------------------------------------
# Timeline synthesis
# --------------------------------------------------------------------------------------
DDL_VERSIONS_ORDERED = ["v5.2", "v5.3", "v5.3_PreRelease", "v5.4", "v5.5", "v5.6"]
ALL_VERSIONS_ORDERED = [
    "v4.26",
    "v4.27",
    "v4.28",
    "v4.29",
    "v4.30",
    "v5.0",
    "v5.1",
    "v5.2",
    "v5.3",
    "v5.4",
    "v5.5",
    "v5.6",
]


def build_timeline(
    columns_by_v: dict[str, dict[str, list[dict]]],
    upgrade_rows: list[dict],
    rename_rows: list[dict],
) -> list[TimelineRow]:
    timeline: list[TimelineRow] = []

    # Determine ADDED vs REMOVED via DDL set diff (v5.2+ only — only DDL provides full
    # schema state per version; upgrade reports are change-only and can't tell us
    # what's no longer there).
    ddl_versions_with_create = [v for v in DDL_VERSIONS_ORDERED if columns_by_v.get(v)]
    prior_tables: set[str] = set()
    for v in ddl_versions_with_create:
        present = set(columns_by_v[v].keys())
        added = present - prior_tables if prior_tables else set()
        removed = prior_tables - present if prior_tables else set()
        for t in sorted(added):
            timeline.append(TimelineRow(table=t, version=v, action="ADDED", source="ddl"))
        for t in sorted(removed):
            timeline.append(TimelineRow(table=t, version=v, action="REMOVED", source="ddl"))
        prior_tables = present

    # Upgrade-report rows: every entry is a change. Use ADDED if not seen before in
    # any prior version's report or DDL; else MODIFIED.
    seen_anywhere: dict[str, str] = {}  # table -> first version seen
    # Pre-seed with v5.2 DDL state (everything in v5.2 DDL is pre-existing as of v5.2).
    for t in columns_by_v.get("v5.2", {}):
        seen_anywhere[t] = "v5.2"
    for v in ALL_VERSIONS_ORDERED:
        rows_this_v = [r for r in upgrade_rows if r["version"] == v]
        for r in rows_this_v:
            t = r["table"]
            action = "ADDED" if t not in seen_anywhere else "MODIFIED"
            timeline.append(
                TimelineRow(
                    table=t,
                    version=v,
                    action=action,
                    package=r["package"],
                    visibility=r["visibility"],
                    source="upgrade-report",
                )
            )
            seen_anywhere.setdefault(t, v)

    # Rename evidence (sp_rename rows). Emit RENAMED_FROM and RENAMED_TO with note
    # for cross-reference.
    for r in rename_rows:
        scope = r["scope"]
        old_full = r["old_name"]
        new_full = r["new_name"]
        if scope == "table":
            timeline.append(
                TimelineRow(
                    table=old_full,
                    version=r["version"],
                    action="RENAMED_FROM",
                    source="sp_rename",
                    note=f"-> {new_full}",
                )
            )
            timeline.append(
                TimelineRow(
                    table=new_full,
                    version=r["version"],
                    action="RENAMED_TO",
                    source="sp_rename",
                    note=f"<- {old_full}",
                )
            )
        elif scope == "column":
            target = r["target_table"]
            timeline.append(
                TimelineRow(
                    table=target,
                    version=r["version"],
                    action="MODIFIED",
                    source="sp_rename",
                    note=f"column rename: {old_full} -> {new_full}",
                )
            )

    timeline.sort(key=lambda x: (x.table, x.version, x.action))
    return timeline


# --------------------------------------------------------------------------------------
# Hypothesis verification
# --------------------------------------------------------------------------------------
def verify_hypothesis(
    h: dict,
    columns_by_v: dict[str, dict[str, list[dict]]],
    rename_rows: list[dict],
    upgrade_rows: list[dict],
    lifecycle: dict[str, TableLifecycle],
) -> dict:
    successors = h["successors"]
    predecessors = h["predecessors"]

    evidence: list[str] = []
    verdict_parts: list[str] = []

    # 1) sp_rename evidence — strongest. Match either direction.
    for r in rename_rows:
        if r["scope"] != "table":
            continue
        if r["old_name"] in predecessors + successors or r["new_name"] in predecessors + successors:
            evidence.append(
                f"sp_rename: `{r['old_name']}` -> `{r['new_name']}` in {r['version']} alter.sql"
            )
            verdict_parts.append("CONFIRMED")

    # 2) DDL set diff (v5.2+ only). The DDL is "current state per release", not a
    # historical snapshot — so a predecessor renamed BEFORE the v5.2 capture window
    # (the earliest DDL we have) will simply be absent from every captured DDL,
    # while the successor will be present in every one. That pattern is itself
    # evidence; absent DDL contradiction means the rename happened pre-window.
    ddl_pred_present: dict[str, set[str]] = {p: set() for p in predecessors}
    ddl_succ_present: dict[str, set[str]] = {s: set() for s in successors}
    for v, tables in columns_by_v.items():
        for p in predecessors:
            if p in tables:
                ddl_pred_present[p].add(v)
        for s in successors:
            if s in tables:
                ddl_succ_present[s].add(v)
    for p, vs in ddl_pred_present.items():
        evidence.append(
            f"DDL: `{p}` present in {sorted(vs) if vs else '(none — absent in all captured DDL)'}"
        )
    for s, vs in ddl_succ_present.items():
        evidence.append(
            f"DDL: `{s}` present in {sorted(vs) if vs else '(none — absent in all captured DDL)'}"
        )

    latest_ddl = sorted([v for v in DDL_VERSIONS_ORDERED if columns_by_v.get(v)])[-1]
    latest_pred_present = [p for p in predecessors if latest_ddl in ddl_pred_present[p]]
    latest_succ_present = [s for s in successors if latest_ddl in ddl_succ_present[s]]

    # Compute lifecycle (mirror data flow) alignment up-front — needed for both
    # DATA-FLOW-REPLACEMENT and LIFECYCLE-MATCH branches.
    #
    # Predecessor retirement: last_month should land at the transition month or the
    # month immediately before. AEMO's lifecycle convention records the LAST month a
    # table appeared, so a table retired AT cutover has last_month == transition;
    # one retired the month before has last_month == transition - 1.
    #
    # Successor activation: two valid patterns —
    #   (a) NEW table that first appears at the transition (first_month near transition), or
    #   (b) PRE-EXISTING table that takes over the predecessor's role (already active
    #       through the transition month — no first_month constraint needed beyond
    #       "was alive during the transition month").
    transition = h["transition_yyyymm"]
    prior_yyyymm = transition - 1 if (transition % 100) > 1 else transition - 89
    pred_stops_at_transition = [
        p
        for p in predecessors
        if p in lifecycle and lifecycle[p].last_month in (prior_yyyymm, transition - 1, transition)
    ]
    succ_active_through_transition = [
        s
        for s in successors
        if s in lifecycle
        and lifecycle[s].first_month <= transition
        and lifecycle[s].last_month >= transition
    ]
    succ_starts_at_transition = [
        s
        for s in successors
        if s in lifecycle and lifecycle[s].first_month in (transition, prior_yyyymm, transition - 1)
    ]
    succ_aligned = succ_starts_at_transition or succ_active_through_transition
    lifecycle_aligned = bool(pred_stops_at_transition) and bool(succ_aligned)

    if latest_pred_present and latest_succ_present:
        # Both predecessor and successor live in the latest DDL. DDL alone doesn't
        # show a rename — but the underlying claim may still be valid at the
        # data-flow layer. Disambiguate via mirror lifecycle.
        if lifecycle_aligned:
            verdict_parts.append("DATA-FLOW-REPLACEMENT")
            succ_label = (
                f"{', '.join(succ_starts_at_transition)} starts at transition"
                if succ_starts_at_transition
                else f"{', '.join(succ_active_through_transition)} already active"
            )
            evidence.append(
                f"Both DDL-coexist in {latest_ddl}, but mirror lifecycle shows "
                f"{', '.join(pred_stops_at_transition)} stops publishing at ~{transition} "
                f"as {succ_label}. DDL keeps both definitions for backward-compat; "
                f"data flow replaces."
            )
        else:
            verdict_parts.append("CONTRADICTED-COEXIST")
            evidence.append(
                f"Both predecessor ({', '.join(latest_pred_present)}) and successor "
                f"({', '.join(latest_succ_present)}) coexist in latest DDL ({latest_ddl}), "
                f"AND mirror lifecycle does not show data-flow replacement at the "
                f"stated transition month {transition}. Hypothesis appears wrong."
            )
    else:
        # Pattern A: pred present in some DDL then disappears, succ appears in same window.
        pred_disappears_in_window = any(
            ddl_pred_present[p] and not (ddl_pred_present[p] & set(DDL_VERSIONS_ORDERED[-3:]))
            for p in predecessors
        )
        succ_appears = any(ddl_succ_present[s] for s in successors)
        if pred_disappears_in_window and succ_appears:
            verdict_parts.append("DDL-INFERRED")

        # Pattern B: pred entirely absent in DDL window (renamed pre-v5.2), succ present
        # in every DDL version. Lifecycle CSV must show the predecessor in the mirror walk
        # for this to count — otherwise the predecessor name is purely speculative.
        pred_in_lifecycle = any(p in lifecycle for p in predecessors)
        all_pred_absent = all(not ddl_pred_present[p] for p in predecessors)
        all_succ_present = bool(latest_succ_present) and all(
            ddl_succ_present[s] for s in successors
        )
        if all_pred_absent and all_succ_present and pred_in_lifecycle:
            verdict_parts.append("PRE-DDL-CAPTURED")

    # 3) Upgrade-report set diff (all 12 versions)
    pred_in_reports: set[str] = set()
    succ_in_reports: set[str] = set()
    for r in upgrade_rows:
        if r["table"] in predecessors:
            pred_in_reports.add(f"{r['version']}:{r['table']}")
        if r["table"] in successors:
            succ_in_reports.add(f"{r['version']}:{r['table']}")
    if succ_in_reports:
        evidence.append(f"Upgrade report mentions successor: {sorted(succ_in_reports)}")
    if pred_in_reports:
        evidence.append(f"Upgrade report mentions predecessor: {sorted(pred_in_reports)}")
    if pred_in_reports and succ_in_reports:
        verdict_parts.append("REPORT-INFERRED")

    # 4) Mirror-walk lifecycle alignment (existing CSV)
    lifecycle_pred_last = [(p, lifecycle[p].last_month) for p in predecessors if p in lifecycle]
    lifecycle_succ_first = [(s, lifecycle[s].first_month) for s in successors if s in lifecycle]
    transition = h["transition_yyyymm"]
    aligned = False
    for s, first in lifecycle_succ_first:
        # Successor first month should match (or precede by 1) the stated transition
        if first == transition or first == transition - 1:
            aligned = True
        evidence.append(f"Lifecycle: `{s}` first_month = {first}")
    for p, last in lifecycle_pred_last:
        prior = transition - 1 if (transition % 100) > 1 else transition - 89  # 202408->202407
        if last in (prior, transition - 1):
            aligned = True
        evidence.append(f"Lifecycle: `{p}` last_month = {last}")
    if aligned and not verdict_parts:
        verdict_parts.append("LIFECYCLE-MATCH")

    # 5) Column-shape match (v5.2+ only; for two-version transitions only)
    shape_evidence: list[str] = []
    for v_pred in DDL_VERSIONS_ORDERED:
        for v_succ in DDL_VERSIONS_ORDERED:
            if DDL_VERSIONS_ORDERED.index(v_pred) >= DDL_VERSIONS_ORDERED.index(v_succ):
                continue
            for p in predecessors:
                if p not in columns_by_v.get(v_pred, {}):
                    continue
                pred_cols = {c["column"] for c in columns_by_v[v_pred][p]}
                for s in successors:
                    if s not in columns_by_v.get(v_succ, {}):
                        continue
                    succ_cols = {c["column"] for c in columns_by_v[v_succ][s]}
                    overlap = pred_cols & succ_cols
                    if pred_cols and succ_cols:
                        ratio = len(overlap) / max(len(pred_cols), len(succ_cols))
                        if ratio >= 0.5:
                            shape_evidence.append(
                                f"Column overlap `{p}@{v_pred}` vs `{s}@{v_succ}`: "
                                f"{len(overlap)}/{max(len(pred_cols), len(succ_cols))} "
                                f"({ratio:.0%})"
                            )
    if shape_evidence:
        evidence.extend(shape_evidence[:3])  # cap noise

    # Synthesize verdict. Verdict ladder (most → least specific):
    #   CONFIRMED              — explicit AEMO sp_rename evidence
    #   DATA-FLOW-REPLACEMENT  — both schemas coexist in DDL but mirror data flow
    #                            replaces at the stated transition month
    #   DDL-INFERRED           — predecessor disappears in captured DDL window,
    #                            successor appears
    #   PRE-DDL-CAPTURED       — predecessor renamed before v5.2 capture window;
    #                            mirror lifecycle has the predecessor, DDL has only
    #                            the successor
    #   REPORT-INFERRED        — both names appear in upgrade-report change-lists
    #   LIFECYCLE-MATCH        — only mirror lifecycle months align (weakest)
    #   CONTRADICTED-COEXIST   — both in DDL AND mirror lifecycle does not show
    #                            data-flow replacement → hypothesis appears wrong
    #   NOT-VERIFIABLE         — no source supports or contradicts
    if "CONFIRMED" in verdict_parts:
        verdict = "CONFIRMED"
    elif "DATA-FLOW-REPLACEMENT" in verdict_parts:
        verdict = "DATA-FLOW-REPLACEMENT"
    elif "DDL-INFERRED" in verdict_parts:
        verdict = "DDL-INFERRED"
    elif "PRE-DDL-CAPTURED" in verdict_parts:
        verdict = "PRE-DDL-CAPTURED"
    elif "REPORT-INFERRED" in verdict_parts:
        verdict = "REPORT-INFERRED"
    elif "LIFECYCLE-MATCH" in verdict_parts:
        verdict = "LIFECYCLE-MATCH"
    elif "CONTRADICTED-COEXIST" in verdict_parts:
        verdict = "CONTRADICTED-COEXIST"
    else:
        verdict = "NOT-VERIFIABLE"

    return {
        "id": h["id"],
        "verdict": verdict,
        "stated_confidence": h["stated_confidence"],
        "stated_evidence": h["stated_evidence"],
        "consolidation_note": h.get("consolidation_note", ""),
        "transition_yyyymm": h["transition_yyyymm"],
        "successors": successors,
        "predecessors": predecessors,
        "evidence": evidence,
    }


def find_unhypothesized_renames(rename_rows: list[dict], hypotheses: list[dict]) -> list[dict]:
    """Surface table/column renames in DDL not covered by any §6 hypothesis."""
    hypothesized = set()
    for h in hypotheses:
        for n in h["successors"] + h["predecessors"]:
            hypothesized.add(n)

    # Strip *_PRE53 / *_PREXX suffixes — those are AEMO's "rename to legacy" markers,
    # not novel rename targets. Filter them out so we don't show the legacy half of
    # an already-hypothesized rename as a new finding.
    def is_legacy_marker(name: str) -> bool:
        import re

        return bool(re.search(r"_PRE\d+$", name) or re.search(r"_DM\d+$", name))

    out = []
    for r in rename_rows:
        if r["scope"] not in ("table", "column"):
            continue
        old, new = r["old_name"], r["new_name"]
        if is_legacy_marker(new):
            continue  # rename to *_PRE53 etc. is the legacy-marking half of a known rename
        if old in hypothesized or new in hypothesized:
            continue
        if r["scope"] == "column":
            target = r["target_table"]
            if target in hypothesized:
                continue
            if is_legacy_marker(new):
                continue
        out.append(r)
    return out


# --------------------------------------------------------------------------------------
# Output writers
# --------------------------------------------------------------------------------------
def write_timeline(rows: list[TimelineRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["table", "version", "action", "package", "visibility", "source", "note"])
        for r in rows:
            w.writerow([r.table, r.version, r.action, r.package, r.visibility, r.source, r.note])


def write_report(
    verdicts: list[dict],
    new_renames: list[dict],
    columns_by_v: dict[str, dict[str, list[dict]]],
    upgrade_rows: list[dict],
    rename_rows: list[dict],
    path: Path,
) -> None:
    today = datetime.now(UTC).strftime("%Y-%m-%d")
    lines: list[str] = []
    lines.append("# MMSDM Table Renames — Verification Report")
    lines.append("")
    lines.append(f"_Generated {today} by `scripts/synthesize_mmsdm_timeline.py`._")
    lines.append("")
    lines.append(
        "Verifies the rename hypotheses in `MMSDM-TABLE-LIFECYCLE.md §6` "
        "against AEMO-shipped DDL (`MMSDM-DDL-RENAMES.csv`, `MMSDM-DDL-COLUMNS.csv`), "
        "Upgrade Report change-lists (`MMSDM-UPGRADE-TABLES.csv`), and the existing "
        "mirror-walk lifecycle (`MMSDM-TABLE-LIFECYCLE.csv`)."
    )
    lines.append("")

    # Coverage summary
    lines.append("## 1. Coverage")
    lines.append("")
    lines.append("| Source | Coverage |")
    lines.append("|---|---|")
    ddl_versions = sorted(columns_by_v.keys())
    lines.append(f"| DDL CREATE TABLE | {len(ddl_versions)} versions: {', '.join(ddl_versions)} |")
    n_upgrade = len({r["version"] for r in upgrade_rows})
    lines.append(f"| Upgrade Report change-lists | {n_upgrade} versions |")
    n_renames = len(rename_rows)
    n_table_renames = sum(1 for r in rename_rows if r["scope"] == "table")
    n_column_renames = sum(1 for r in rename_rows if r["scope"] == "column")
    n_other = n_renames - n_table_renames - n_column_renames
    lines.append(
        f"| sp_rename calls | {n_renames} total "
        f"({n_table_renames} table, {n_column_renames} column, "
        f"{n_other} object/index/constraint) |"
    )
    lines.append("")

    # Verdict summary table
    lines.append("## 2. Verdict summary")
    lines.append("")
    lines.append("| ID | Successor(s) | Predecessor(s) | Stated | Verdict |")
    lines.append("|---|---|---|---|---|")
    for v in verdicts:
        succs = ", ".join(f"`{s}`" for s in v["successors"])
        preds = ", ".join(f"`{p}`" for p in v["predecessors"])
        lines.append(
            f"| {v['id']} | {succs} | {preds} | {v['stated_confidence']} | **{v['verdict']}** |"
        )
    lines.append("")

    # Detailed verdicts
    lines.append("## 3. Detailed verdicts")
    for v in verdicts:
        lines.append("")
        lines.append(f"### {v['id']}")
        lines.append("")
        lines.append(f"- **Successor(s):** {', '.join(f'`{s}`' for s in v['successors'])}")
        lines.append(f"- **Predecessor(s):** {', '.join(f'`{p}`' for p in v['predecessors'])}")
        lines.append(f"- **Stated transition month:** {v['transition_yyyymm']}")
        lines.append(f"- **Stated confidence:** {v['stated_confidence']}")
        lines.append(f"- **Stated evidence:** {v['stated_evidence']}")
        if v["consolidation_note"]:
            lines.append(f"- **Note:** {v['consolidation_note']}")
        lines.append(f"- **Verdict:** **{v['verdict']}**")
        if v["evidence"]:
            lines.append("- **Evidence:**")
            for e in v["evidence"]:
                lines.append(f"  - {e}")
        else:
            lines.append("- **Evidence:** _(none found in available sources)_")

    # New findings
    lines.append("")
    lines.append("## 4. Renames in DDL not covered by §6")
    lines.append("")
    if new_renames:
        lines.append(
            "These renames appear in AEMO's upgrade DDL but are not listed as hypotheses "
            "in `MMSDM-TABLE-LIFECYCLE.md §6`. Consider adding rows."
        )
        lines.append("")
        lines.append("| Version | Scope | Target table | Old | New |")
        lines.append("|---|---|---|---|---|")
        for r in new_renames:
            target = r.get("target_table", "")
            lines.append(
                f"| {r['version']} | {r['scope']} | `{target}` | "
                f"`{r['old_name']}` | `{r['new_name']}` |"
            )
    else:
        lines.append("_No unhypothesized renames found._")

    lines.append("")
    lines.append("## 5. How to re-run")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 scripts/synthesize_mmsdm_timeline.py \\")
    lines.append("    --columns reference/MMSDM-DDL-COLUMNS.csv \\")
    lines.append("    --renames reference/MMSDM-DDL-RENAMES.csv \\")
    lines.append("    --upgrade reference/MMSDM-UPGRADE-TABLES.csv \\")
    lines.append("    --lifecycle reference/MMSDM-TABLE-LIFECYCLE.csv \\")
    lines.append("    --timeline-out reference/MMSDM-TABLE-TIMELINE.csv \\")
    lines.append("    --report-out reference/MMSDM-RENAMES-VERIFICATION.md")
    lines.append("```")
    lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--columns", type=Path, required=True)
    ap.add_argument("--renames", type=Path, required=True)
    ap.add_argument("--upgrade", type=Path, required=True)
    ap.add_argument("--lifecycle", type=Path, required=True)
    ap.add_argument("--timeline-out", type=Path, required=True)
    ap.add_argument("--report-out", type=Path, required=True)
    args = ap.parse_args()

    columns_by_v = load_columns(args.columns)
    rename_rows = load_renames(args.renames)
    upgrade_rows = load_upgrade_tables(args.upgrade)
    lifecycle = load_lifecycle(args.lifecycle)

    print(
        f"Loaded {sum(len(t) for t in columns_by_v.values())} table-version DDL entries "
        f"across {len(columns_by_v)} versions"
    )
    print(f"Loaded {len(rename_rows)} sp_rename rows")
    print(f"Loaded {len(upgrade_rows)} upgrade-report rows")
    print(f"Loaded {len(lifecycle)} lifecycle rows")
    print()

    timeline = build_timeline(columns_by_v, upgrade_rows, rename_rows)
    write_timeline(timeline, args.timeline_out)
    print(f"Wrote {len(timeline):,} timeline rows -> {args.timeline_out}")

    verdicts = [
        verify_hypothesis(h, columns_by_v, rename_rows, upgrade_rows, lifecycle) for h in HYPOTHESES
    ]
    new_renames = find_unhypothesized_renames(rename_rows, HYPOTHESES)
    write_report(verdicts, new_renames, columns_by_v, upgrade_rows, rename_rows, args.report_out)
    print(f"Wrote verification report -> {args.report_out}")

    print()
    print("Verdicts:")
    for v in verdicts:
        print(f"  {v['id']:35s} stated={v['stated_confidence']:18s} -> {v['verdict']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
