"""Extract AEMO URL conventions from the local NEMWeb mirror.

Taxonomy (empirical, per reference/NEMWEB-STRUCTURE.md §1):

  Repo ∈ {Reports, MMSDM, NEMDE, FCAS_Causer_Pays} — exactly four.

  Dataset = (repo, intra-repo identifier). Cross-repo dataset identity
  is DEFAULT-SEPARATE per §4 — two entries with the same intra-repo
  identifier under different repos are distinct catalog keys and MUST
  NOT be merged without cited proof. This script does not attempt to
  merge; it preserves the separation.

  Intra-repo identifier is derived per repo:
    Reports:           stream subdir name (byte-exact per retention tier)
    MMSDM:             #-delimited TABLE for SQLLoader files;
                       special-case tier for MTPASA_DATA_EXPORT,
                       monthly bulk zips, and DOCUMENTATION
    NEMDE:             filename prefix within NEMDE_Files / File_Readers
    FCAS_Causer_Pays:  "CAUSER_PAYS" (one logical dataset, one file/year)

  Retention / view tier:
    Reports:           CURRENT or ARCHIVE
    MMSDM:             SQLLoader view (CTL, DATA, BCP_FMT, BCP_DATA,
                       MYSQL, INDEX, UTILITIES, LOGS, P5MIN_ALL_DATA,
                       PREDISP_ALL_DATA, DOCUMENTATION) or
                       MONTHLY_BULK / MTPASA_DATA_EXPORT
    NEMDE:             NEMDE_Files or File_Readers
    FCAS_Causer_Pays:  (single tier; year appears in the filename)

Field split per NEMWEB-STRUCTURE.md "stable vs snapshot" distinction:

  Stable fields (byte-deterministic across mirror re-runs):
    repo, retention_tier, intra_repo_id, path_template, filename_regex,
    filename_template, sample_filename, anomaly_flag

  Snapshot fields (volatile; drift on every mirror re-run because
  Reports/CURRENT rolls daily):
    file_count, first_seen, last_seen

Both are emitted into the same outputs; the CSV and the MD both label
snapshot columns explicitly so consumers can project out the stable
subset.

Outputs:
  reference/URL-CONVENTIONS.md   human-readable, grouped by repo → dataset
  reference/URL-CONVENTIONS.csv  flat rows

Known limitations (documented in the MD output):
  * Table-name evolution (rename / split / merge of the same logical
    dataset across time) is NOT resolved. Two distinct string
    identifiers that refer to the same AEMO data product over time
    appear as two separate datasets. Resolving them requires parsing
    MMS Data Model docs (Reports/CURRENT/.../DOCUMENTATION/) or a
    user-supplied alias map; both are out of scope for this script.
  * Snapshot fields reflect the moment of the walker run. Re-running
    the walker a week later gives different first_seen/last_seen/
    file_count. Stable fields do not drift.

Zero deps. Run: python3 scripts/extract_patterns.py
"""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import urllib.parse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

MIRROR = Path("nemweb-mirror")
OUT_MD = Path("reference/URL-CONVENTIONS.md")
OUT_CSV = Path("reference/URL-CONVENTIONS.csv")

# IIS auto-index row: "Thursday, April 16, 2026  4:40 AM  19629 <A HREF=...>name</A>"
ROW_RE = re.compile(
    rb'(\w+,\s+\w+\s+\d+,\s+\d+)\s+(\d+:\d+\s+[AP]M)\s+(<dir>|\d+)\s+'
    rb'<A HREF="([^"]+)">([^<]+)</A>',
    re.IGNORECASE,
)

HREF_ANY_RE = re.compile(rb'<A HREF="([^"]+)">')
DIGIT_RUN_RE = re.compile(r"\d+")

DIGIT_LABELS = {
    4: "year", 6: "yearmonth", 8: "date", 10: "yyyymmddhh",
    12: "timestamp", 14: "datetime", 16: "aemo_id",
}

MONTHS = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
}

VALID_REPOS = ("Reports", "MMSDM", "NEMDE", "FCAS_Causer_Pays")


# ---------- Skeleton / template / regex helpers ----------

def skeletonize(name: str) -> str:
    return DIGIT_RUN_RE.sub(lambda m: f"<d{len(m.group())}>", name)


def skeleton_to_regex(skel: str) -> str:
    parts: list[str] = []
    i = 0
    while i < len(skel):
        if skel[i] == "<" and i + 2 < len(skel) and skel[i + 1] == "d":
            close = skel.index(">", i)
            n = skel[i + 2 : close]
            parts.append(rf"\d{{{n}}}")
            i = close + 1
        else:
            parts.append(re.escape(skel[i]))
            i += 1
    return "".join(parts)


def label_digit_positions(skel: str, samples: list[str]) -> str:
    positions: list[tuple[int, int, int]] = []
    for m in re.finditer(r"<d(\d+)>", skel):
        positions.append((m.start(), m.end(), int(m.group(1))))
    if not positions:
        return skel
    capturing = skeleton_to_regex(skel)
    cap_pattern = re.compile("^" + re.sub(r"\\d\{(\d+)\}", r"(\\d{\1})", capturing) + "$")
    values_per_pos: list[list[str]] = [[] for _ in positions]
    for s in samples:
        m = cap_pattern.match(s)
        if not m:
            continue
        for i, g in enumerate(m.groups()):
            values_per_pos[i].append(g)

    def label_for(n: int, values: list[str]) -> str:
        base = DIGIT_LABELS.get(n, f"d{n}")
        if not values:
            return base
        if n == 4 and all(v.startswith(("19", "20")) for v in values):
            return "year"
        if n == 6 and all(v[:4].startswith(("19", "20")) for v in values):
            return "yearmonth"
        if n == 8 and all(v.startswith(("19", "20")) for v in values):
            return "date"
        if n == 12 and all(v.startswith(("19", "20")) for v in values):
            return "timestamp"
        if n == 14 and all(v.startswith(("19", "20")) for v in values):
            return "datetime"
        if n == 16:
            return "aemo_id"
        return base

    raw = [label_for(n, values_per_pos[i]) for i, (_, _, n) in enumerate(positions)]
    totals: dict[str, int] = defaultdict(int)
    for lbl in raw:
        totals[lbl] += 1
    counts: dict[str, int] = defaultdict(int)
    final: list[str] = []
    for lbl in raw:
        if totals[lbl] > 1:
            counts[lbl] += 1
            final.append(f"{lbl}{counts[lbl]}")
        else:
            final.append(lbl)
    out: list[str] = []
    last = 0
    for i, (start, end, _) in enumerate(positions):
        out.append(skel[last:start])
        out.append("{" + final[i] + "}")
        last = end
    out.append(skel[last:])
    return "".join(out)


# ---------- Path helpers ----------

def url_path_from_local(index_file: Path) -> str:
    rel = index_file.parent.relative_to(MIRROR).as_posix()
    return "/" + rel + "/" if rel else "/"


def path_template(url_path: str) -> str:
    segs = url_path.strip("/").split("/")
    if not segs or segs == [""]:
        return "/"
    return "/" + "/".join(skeletonize(seg) for seg in segs) + "/"


def path_template_labeled(url_path: str) -> str:
    # URL-decode %20 -> space so docs paths read naturally
    segs = [urllib.parse.unquote(s) for s in url_path.strip("/").split("/")]
    out: list[str] = []
    for seg in segs:
        s = skeletonize(seg)
        for m in list(re.finditer(r"<d(\d+)>", s))[::-1]:
            n = int(m.group(1))
            lbl = DIGIT_LABELS.get(n, f"d{n}")
            s = s[: m.start()] + "{" + lbl + "}" + s[m.end() :]
        out.append(s)
    return "/" + "/".join(out) + "/"


# ---------- Repo / tier / intra-repo classification ----------

def classify(url_path: str, filename: str) -> tuple[str, str, str, dict] | None:
    """Classify a file into (repo, retention_tier, intra_repo_id, extras).

    extras carries repo-specific metadata (e.g. sqlloader_view, stream_name).
    Returns None if the path doesn't fall under any of the 4 known repos —
    such paths are filtered out (they shouldn't exist in a clean mirror).
    """
    segs = url_path.strip("/").split("/")
    if not segs:
        return None

    # --- Reports ---
    if segs[0] == "Reports" and len(segs) >= 3 and segs[1] in ("CURRENT", "ARCHIVE"):
        repo = "Reports"
        tier = segs[1]  # CURRENT or ARCHIVE
        stream = segs[2]  # byte-exact per tier
        return repo, tier, stream, {"stream": stream}

    # --- Data_Archive subtrees ---
    if len(segs) >= 3 and segs[0] == "Data_Archive" and segs[1] == "Wholesale_Electricity":
        sub = segs[2]

        if sub == "MMSDM":
            return classify_mmsdm(segs, filename)
        if sub == "NEMDE":
            return classify_nemde(segs, filename)
        if sub == "FCAS_Causer_Pays":
            return "FCAS_Causer_Pays", "ANNUAL", "CAUSER_PAYS", {}

    return None  # Off-taxonomy; will be filtered


def classify_mmsdm(segs: list[str], filename: str) -> tuple[str, str, str, dict]:
    """Classify an MMSDM file. segs starts with Data_Archive/Wholesale_Electricity/MMSDM/..."""
    # Strip the common prefix to see MMSDM-relative segs
    rel = segs[3:]  # everything after MMSDM/

    # Special case: MMSDM/MTPASA_DATA_EXPORT/<file>
    if rel and rel[0] == "MTPASA_DATA_EXPORT":
        return "MMSDM", "MTPASA_DATA_EXPORT", "MTPASA_DATA_EXPORT", {}

    # Year-rooted paths: MMSDM/{year}/...
    if rel and re.fullmatch(r"\d{4}", rel[0]):
        # MMSDM/{year}/MMSDM_{year}_{mm}.zip (monthly bulk zip)
        if len(rel) == 1:
            return "MMSDM", "MONTHLY_BULK", "MMSDM_MONTHLY_BULK", {}

        # MMSDM/{year}/MMSDM_{year}_{mm}/...
        if len(rel) >= 2 and re.fullmatch(r"MMSDM_\d{4}_\d{2}", rel[1]):
            # MMSDM/{year}/{month}/  root (e.g. AUTORUN.INF, disclaimer.htm)
            if len(rel) == 2:
                return "MMSDM", "MONTH_ROOT", "MONTH_ROOT_AUX", {}

            # MMSDM/{year}/{month}/MMSDM_Historical_Data_SQLLoader/...
            if len(rel) >= 3 and rel[2] == "MMSDM_Historical_Data_SQLLoader":
                if len(rel) == 3:
                    return "MMSDM", "SQLLOADER_ROOT", "SQLLOADER_AUX", {}
                view = rel[3]  # CTL, DATA, BCP_FMT, etc.

                # DOCUMENTATION is a further nested tree (MMS Data Model/v*/...)
                if view == "DOCUMENTATION":
                    # intra_repo_id from path segments (MMS Data Model version) if present
                    path_tail = "/".join(rel[4:])
                    # e.g. "MMS%20Data%20Model/v5.1/..."
                    m = re.match(r"MMS%20Data%20Model/(v[\w.]+)/?", path_tail)
                    if m:
                        return "MMSDM", "DOCUMENTATION", f"MMS_DATA_MODEL_{m.group(1)}", {"mms_version": m.group(1)}
                    return "MMSDM", "DOCUMENTATION", "DOCUMENTATION_AUX", {}

                # SQLLoader view file: extract #TABLE# from filename
                table = extract_mmsdm_table(filename) or "UNPARSED"
                return "MMSDM", view, table, {"sqlloader_view": view}

    # Fallback: unknown MMSDM path
    return "MMSDM", "OTHER", "UNKNOWN", {}


def classify_nemde(segs: list[str], filename: str) -> tuple[str, str, str, dict]:
    """Classify an NEMDE file. segs starts with Data_Archive/Wholesale_Electricity/NEMDE/..."""
    rel = segs[3:]  # everything after NEMDE/

    # NEMDE/{year}/NEMDE_{year}_{mm}/NEMDE_Market_Data/{NEMDE_Files|File_Readers}/...
    if len(rel) >= 4 and rel[3] in ("NEMDE_Files", "File_Readers"):
        subtree = rel[3]
        # intra_repo_id = filename prefix (before first digit-run or extension)
        intra_id = extract_nemde_prefix(filename) or "UNKNOWN"
        return "NEMDE", subtree, intra_id, {"nemde_subtree": subtree}

    # Other NEMDE paths (root, year, month, Market_Data root)
    return "NEMDE", "ROOT_AUX", "ROOT_AUX", {}


def extract_mmsdm_table(filename: str) -> str | None:
    """MMSDM SQLLoader filenames: PUBLIC_ARCHIVE%23<TABLE>%23FILE<NN>%23<date>.<ext>
    URL-decoded: PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<date>.<ext>
    """
    decoded = urllib.parse.unquote(filename)
    if "#" not in decoded:
        return None
    parts = decoded.split("#")
    if len(parts) >= 2 and parts[0] in ("PUBLIC_ARCHIVE", "PUBLIC"):
        return parts[1]
    if len(parts) >= 2:
        return parts[1]
    return None


def extract_nemde_prefix(filename: str) -> str | None:
    """NEMDE filenames like NemPriceSetter_20141201_xml.zip -> 'NemPriceSetter'."""
    decoded = urllib.parse.unquote(filename)
    stem = decoded.rsplit(".", 1)[0]
    tokens = stem.split("_")
    literal: list[str] = []
    for tok in tokens:
        if tok.isdigit() or (len(tok) >= 4 and all(c.isdigit() for c in tok)):
            break
        literal.append(tok)
    return "_".join(literal) if literal else None


# ---------- Anomaly detection (Reports casing mismatches; AEMO URL typos) ----------

# Pre-known AEMO-side anomalies, verified in NEMWEB-STRUCTURE.md §3
REPORTS_CASING_MISMATCHES = {
    ("DISPATCH_NEGATIVE_RESIDUE", "Dispatch_Negative_Residue"),
    ("PDPASA_DUIDAvailability", "PDPASA_DUIDAVAILABILITY"),
    ("STPASA_DUIDAvailability", "STPASA_DUIDAVAILABILITY"),
}
AEMO_URL_TYPOS = {
    "NEXT_DAY_OFFER_ENERGY)SPARSE",  # should be Next_Day_Offer_Energy_SPARSE
}


def anomaly_flag(repo: str, retention_tier: str, intra_repo_id: str) -> str:
    if repo == "Reports":
        if intra_repo_id in AEMO_URL_TYPOS:
            return "aemo_url_typo"
        for a, b in REPORTS_CASING_MISMATCHES:
            if intra_repo_id == a or intra_repo_id == b:
                return "casing_mismatch_vs_sibling_tier"
    return ""


# ---------- IIS row parsing ----------

def parse_iis_date(datestamp: str, time: str) -> datetime | None:
    try:
        _, rest = datestamp.split(",", 1)
        rest = rest.strip()
        month_str, day_year = rest.split(" ", 1)
        day_str, year_str = day_year.split(",", 1)
        month = MONTHS[month_str.strip()]
        day = int(day_str.strip())
        year = int(year_str.strip())
        t = time.strip().upper()
        h, rest2 = t.split(":", 1)
        mm, ampm = rest2.split(" ", 1)
        hour = int(h)
        minute = int(mm)
        if ampm == "PM" and hour != 12:
            hour += 12
        if ampm == "AM" and hour == 12:
            hour = 0
        return datetime(year, month, day, hour, minute)
    except Exception:
        return None


def parse_listing(index_file: Path, parent_path: str) -> list[dict]:
    """Return list of {name, url_path, last_modified} — files only (not dirs)."""
    data = index_file.read_bytes()
    files: list[dict] = []
    seen_paths: set[str] = set()

    for m in ROW_RE.finditer(data):
        datestamp = m.group(1).decode("ascii", errors="replace")
        time = m.group(2).decode("ascii", errors="replace")
        size_token = m.group(3).decode("ascii", errors="replace")
        href = m.group(4).decode("ascii", errors="replace")
        if size_token == "<dir>":
            continue
        if href.startswith("http"):
            p = urllib.parse.urlparse(href)
            if p.netloc and p.netloc != "nemweb.com.au":
                continue
            new_path = p.path
        else:
            new_path = urllib.parse.urljoin(parent_path, href)
        if parent_path.startswith(new_path) and new_path != parent_path:
            continue
        if new_path.endswith("/"):
            continue
        basename = urllib.parse.unquote(new_path.rsplit("/", 1)[-1])
        seen_paths.add(new_path)
        files.append({
            "name": basename,
            "url_path": new_path,
            "last_modified": parse_iis_date(datestamp, time),
        })

    # Pick up files missed by ROW_RE (rare; no date info)
    for m in HREF_ANY_RE.finditer(data):
        try:
            href = m.group(1).decode("ascii")
        except UnicodeDecodeError:
            continue
        if href.startswith("http"):
            p = urllib.parse.urlparse(href)
            if p.netloc and p.netloc != "nemweb.com.au":
                continue
            new_path = p.path
        else:
            new_path = urllib.parse.urljoin(parent_path, href)
        if parent_path.startswith(new_path) and new_path != parent_path:
            continue
        if new_path.endswith("/") or new_path in seen_paths:
            continue
        basename = urllib.parse.unquote(new_path.rsplit("/", 1)[-1])
        files.append({"name": basename, "url_path": new_path, "last_modified": None})
    return files


# ---------- Main extraction ----------

def main() -> int:
    if not MIRROR.exists():
        print(f"Mirror not found at {MIRROR}", file=sys.stderr)
        return 2

    # (repo, retention_tier, intra_repo_id, path_template, skeleton) -> aggregate
    agg: dict[tuple[str, str, str, str, str], dict] = {}
    off_taxonomy_count = 0
    total_listings = 0
    total_listings_with_files = 0
    total_files = 0
    empty_listings: list[dict] = []  # directory-level anomalies (listing with zero files)

    for idx in sorted(MIRROR.rglob("index.html")):
        total_listings += 1
        parent_path = url_path_from_local(idx)
        files = parse_listing(idx, parent_path)
        if not files:
            # Empty listing — could be branch-only (children are dirs, which is normal) or
            # an anomalous leaf (no files, no children, or AEMO URL typo dir).
            # We only flag leaves with a known anomaly fingerprint.
            segs = parent_path.strip("/").split("/")
            if (
                len(segs) >= 3
                and segs[0] == "Reports"
                and segs[1] in ("CURRENT", "ARCHIVE")
                and segs[2] in AEMO_URL_TYPOS
            ):
                empty_listings.append({
                    "url_path": parent_path,
                    "reason": "aemo_url_typo (directory exists with no files)",
                })
            continue
        total_listings_with_files += 1
        total_files += len(files)

        for f in files:
            cls = classify(f["url_path"], f["name"])
            if cls is None:
                off_taxonomy_count += 1
                continue
            repo, tier, intra_id, extras = cls
            assert repo in VALID_REPOS, f"Unexpected repo: {repo}"

            skel = skeletonize(f["name"])
            ptpl = path_template(parent_path)
            key = (repo, tier, intra_id, ptpl, skel)
            g = agg.setdefault(key, {
                "repo": repo,
                "retention_tier": tier,
                "intra_repo_id": intra_id,
                "path_template": ptpl,
                "path_template_labeled": path_template_labeled(parent_path),
                "skeleton": skel,
                "samples": [],
                "all_names": [],
                "count": 0,
                "first_seen": None,
                "last_seen": None,
                "example_dir": parent_path,
                "anomaly": anomaly_flag(repo, tier, intra_id),
                "extras": extras,
            })
            g["count"] += 1
            if len(g["samples"]) < 3:
                g["samples"].append(f["name"])
            if len(g["all_names"]) < 200:
                g["all_names"].append(f["name"])
            lm = f["last_modified"]
            if lm is not None:
                if g["first_seen"] is None or lm < g["first_seen"]:
                    g["first_seen"] = lm
                if g["last_seen"] is None or lm > g["last_seen"]:
                    g["last_seen"] = lm

    # Materialize rows
    rows: list[dict] = []
    for _key, g in agg.items():
        regex = skeleton_to_regex(g["skeleton"])
        template = label_digit_positions(g["skeleton"], g["all_names"])
        rows.append({
            "repo": g["repo"],
            "retention_tier": g["retention_tier"],
            "intra_repo_id": g["intra_repo_id"],
            "path_template_labeled": g["path_template_labeled"],
            "path_template": g["path_template"],
            "filename_template": template,
            "filename_regex": regex,
            "sample_filename": g["samples"][0] if g["samples"] else "",
            "anomaly": g["anomaly"],
            # Snapshot (volatile):
            "file_count_snapshot": g["count"],
            "first_seen_snapshot": g["first_seen"].isoformat() if g["first_seen"] else "",
            "last_seen_snapshot": g["last_seen"].isoformat() if g["last_seen"] else "",
        })

    # Sort stable-first for deterministic output
    rows.sort(key=lambda r: (
        VALID_REPOS.index(r["repo"]),
        r["retention_tier"],
        r["intra_repo_id"],
        r["path_template"],
        r["filename_regex"],
    ))

    print(
        f"Listings scanned: {total_listings}  with files: {total_listings_with_files}  "
        f"total files: {total_files}  off-taxonomy: {off_taxonomy_count}  "
        f"rows: {len(rows)}"
    )
    repo_counts: dict[str, int] = defaultdict(int)
    dataset_keys: set[tuple[str, str]] = set()
    for r in rows:
        repo_counts[r["repo"]] += 1
        dataset_keys.add((r["repo"], r["intra_repo_id"]))
    print(f"  per-repo pattern rows: {dict(repo_counts)}")
    print(f"  distinct datasets (repo, intra_repo_id): {len(dataset_keys)}")
    if empty_listings:
        print(f"  empty-listing anomalies: {len(empty_listings)}")

    write_csv(rows)
    write_md(rows, total_listings, total_listings_with_files, total_files, dataset_keys, empty_listings)

    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except Exception:
        commit = "unknown"

    Path("patterns/auto/").mkdir(parents=True, exist_ok=True)
    write_json(
        rows,
        out_path=Path("patterns/auto/catalog.json"),
        catalog_version=datetime.now(timezone.utc).strftime("%Y.%m.%d"),
        as_of=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        source_mirror_commit=commit,
    )
    return 0


def write_csv(rows: list[dict]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "repo", "retention_tier", "intra_repo_id",
        "path_template_labeled", "path_template",
        "filename_template", "filename_regex", "sample_filename",
        "anomaly",
        "file_count_snapshot", "first_seen_snapshot", "last_seen_snapshot",
    ]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in fields})
    print(f"wrote {OUT_CSV}  ({len(rows)} rows)")


def write_md(
    rows: list[dict],
    total_listings: int,
    total_listings_with_files: int,
    total_files: int,
    dataset_keys: set[tuple[str, str]],
    empty_listings: list[dict],
) -> None:
    def esc(s: str) -> str:
        return str(s).replace("|", "\\|")

    lines: list[str] = []
    lines.append("# NEMWeb URL Conventions")
    lines.append("")
    lines.append(
        f"Empirically derived from {total_listings} IIS directory listings in "
        f"`nemweb-mirror/`. {total_listings_with_files} listings contained files; "
        f"{total_files} filenames analyzed. **{len(dataset_keys)} distinct datasets** "
        f"across {len(set(r['repo'] for r in rows))} of 4 repositories, "
        f"{len(rows)} (dataset, tier, path, pattern) rows."
    )
    lines.append("")
    lines.append(
        "**Taxonomy** (per `reference/NEMWEB-STRUCTURE.md` §1):"
    )
    lines.append("")
    lines.append(
        "- **Repo** ∈ {`Reports`, `MMSDM`, `NEMDE`, `FCAS_Causer_Pays`} — exactly four.\n"
        "- **Dataset** = `(repo, intra_repo_id)`. Cross-repo identity is **default-separate** — "
        "two entries with the same `intra_repo_id` under different repos are distinct catalog keys "
        "and are NOT merged (see NEMWEB-STRUCTURE.md §4).\n"
        "- **Retention / view tier** depends on repo: Reports has CURRENT/ARCHIVE; MMSDM uses "
        "the SQLLoader view name (CTL, DATA, BCP_FMT, BCP_DATA, MYSQL, INDEX, UTILITIES, LOGS, "
        "P5MIN_ALL_DATA, PREDISP_ALL_DATA, DOCUMENTATION) plus MONTHLY_BULK and MTPASA_DATA_EXPORT; "
        "NEMDE uses NEMDE_Files or File_Readers; FCAS_Causer_Pays is single-tier."
    )
    lines.append("")
    lines.append(
        "**Field split: stable vs snapshot.** The fields `repo`, `retention_tier`, "
        "`intra_repo_id`, `path_template`, `filename_template`, `filename_regex`, and "
        "`anomaly` are **stable** — they are byte-deterministic across mirror re-runs. "
        "The `file_count_snapshot`, `first_seen_snapshot`, and `last_seen_snapshot` "
        "columns are **volatile** — they drift every time the walker runs because "
        "`/Reports/CURRENT/` rolls daily. Stable fields are the catalog; snapshot "
        "fields are provenance-of-the-walk."
    )
    lines.append("")
    lines.append(
        "**Known limitation — table-name evolution is NOT resolved here.** "
        "When AEMO renames a table (e.g. an MMSDM table's name string changes across "
        "MMS Data Model versions), the old name and new name appear here as two "
        "separate `(repo, intra_repo_id)` datasets. Merging them requires either "
        "parsing the `MMS Data Model/v*/` HTML docs inside the mirror, or supplying "
        "an alias map externally — both are out of scope for this script."
    )
    lines.append("")

    # Group rows by repo, then by intra_repo_id
    by_repo: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_repo[r["repo"]].append(r)

    for repo in VALID_REPOS:
        if repo not in by_repo:
            continue
        repo_rows = by_repo[repo]
        by_ds: dict[str, list[dict]] = defaultdict(list)
        for r in repo_rows:
            by_ds[r["intra_repo_id"]].append(r)

        lines.append(f"## Repo: `{repo}`  ({len(by_ds)} dataset{'s' if len(by_ds) != 1 else ''}, {len(repo_rows)} rows)")
        lines.append("")

        for intra_id in sorted(by_ds.keys()):
            ds_rows = sorted(by_ds[intra_id], key=lambda r: (r["retention_tier"], r["path_template"], r["filename_regex"]))
            total_files_for_ds = sum(r["file_count_snapshot"] for r in ds_rows)
            dates = [r["first_seen_snapshot"] for r in ds_rows if r["first_seen_snapshot"]] + \
                    [r["last_seen_snapshot"] for r in ds_rows if r["last_seen_snapshot"]]
            span = f"{min(dates)[:10]} → {max(dates)[:10]}" if dates else "no-dates"
            anomalies = sorted({r["anomaly"] for r in ds_rows if r["anomaly"]})

            lines.append(f"### `{repo}` · `{intra_id}`")
            lines.append("")
            anomaly_note = f" · **anomaly:** {', '.join(anomalies)}" if anomalies else ""
            lines.append(
                f"_{len(ds_rows)} pattern row{'s' if len(ds_rows) != 1 else ''}, "
                f"{total_files_for_ds} files (snapshot), observed {span} (snapshot)"
                f"{anomaly_note}_"
            )
            lines.append("")
            lines.append(
                "| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |"
            )
            lines.append("|---|---|---|---|---|---:|---|---|")
            for r in ds_rows:
                lines.append(
                    "| `{tier}` | `{ptpl}` | `{tmpl}` | `{rx}` | `{s}` | {fc} | {fs} | {ls} |".format(
                        tier=esc(r["retention_tier"]),
                        ptpl=esc(r["path_template_labeled"]),
                        tmpl=esc(r["filename_template"]),
                        rx=esc(r["filename_regex"]),
                        s=esc(r["sample_filename"]),
                        fc=r["file_count_snapshot"],
                        fs=r["first_seen_snapshot"][:10] if r["first_seen_snapshot"] else "—",
                        ls=r["last_seen_snapshot"][:10] if r["last_seen_snapshot"] else "—",
                    )
                )
            lines.append("")

    # Appendix: directory-level anomalies (empty listings with known AEMO issues)
    if empty_listings:
        lines.append("## Appendix: directory-level anomalies")
        lines.append("")
        lines.append(
            "Directories observed on NEMWeb that exist and return HTTP 200 but contain "
            "zero files. These do not appear in the pattern rows above (no filenames to "
            "group), but they are real URLs under the `Reports` repo and must be called "
            "out for catalog completeness."
        )
        lines.append("")
        lines.append("| URL path | Reason |")
        lines.append("|---|---|")
        for e in sorted(empty_listings, key=lambda x: x["url_path"]):
            lines.append(f"| `{esc(e['url_path'])}` | {esc(e['reason'])} |")
        lines.append("")
        lines.append(
            "See `reference/NEMWEB-STRUCTURE.md` §3.2 for the canonical AEMO URL-typo "
            "finding and §3.1 for the related casing-mismatch anomalies (those DO appear "
            "in pattern rows above because their directories contain files)."
        )
        lines.append("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT_MD}  ({len(dataset_keys)} datasets, {len(rows)} rows)")


def write_json(
    rows: list[dict],
    out_path: Path | str,
    catalog_version: str,
    as_of: str,
    source_mirror_commit: str,
) -> None:
    """Emit a JSON Schema v1.0.0 conformant catalog from extractor rows.

    Groups flat rows by (repo, intra_repo_id) and nests tier records under
    each dataset. Preserves exact case of intra_repo_id (do not normalize).
    Called after classify() + aggregate() produce the flat rows list.

    Refuses to emit a zero-row catalog — empty mirror or crawl failure is
    always a pipeline bug, never a valid state. Publishing a blank catalog
    would silently push an empty Pages site to every consumer.
    """
    if not rows:
        raise ValueError(
            "refusing to emit empty catalog: zero rows from extractor; "
            "likely empty mirror or crawl failure. Fix the pipeline rather than "
            "publishing a blank catalog."
        )

    datasets: dict[str, dict] = {}
    all_raw_keys: list[str] = []

    for row in rows:
        repo = row["repo"]
        intra_repo_id = row["intra_repo_id"]
        key = f"{repo}:{intra_repo_id}"
        tier_name = row["retention_tier"]

        if key not in datasets:
            all_raw_keys.append(key)
            datasets[key] = {
                "repo": repo,
                "intra_repo_id": intra_repo_id,
                "resolvable": True,
                "tiers": {},
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": _anomaly_note_from_flag(
                    row.get("anomaly") or row.get("anomaly_flag", ""), row
                ),
            }

        tier_record = {
            "path_template": row["path_template"],
            "filename_template": row.get("filename_template") or None,
            "filename_regex": row.get("filename_regex") or None,
            "example": row.get("sample_filename", ""),
            "cadence": _infer_cadence(repo, tier_name),
        }

        # Only include observed_range if we have any observed values
        first = row.get("first_seen_snapshot")
        last = row.get("last_seen_snapshot")
        if first and last:
            tier_record["observed_range"] = {"from": first, "to": last}
        else:
            tier_record["observed_range"] = None

        datasets[key]["tiers"][tier_name] = tier_record

    # Curate dataset_keys: resolvable=true AND not in AUX/placeholder keys
    dataset_keys = _curate_keys(list(datasets.keys()), datasets)

    placeholders = _placeholders_for(datasets)

    payload = {
        "schema_version": "1.0.0",
        "catalog_version": catalog_version,
        "as_of": as_of,
        "source_mirror_commit": source_mirror_commit,
        "placeholders": placeholders,
        "dataset_keys": dataset_keys,
        "raw_keys": sorted(all_raw_keys),
        "datasets": datasets,
    }
    Path(out_path).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def _anomaly_note_from_flag(flag: str, row: dict) -> str | None:
    """Translate extractor anomaly_flag into a human-readable anomaly_note."""
    if not flag:
        return None
    if flag == "aemo_url_typo":
        return (
            f"Directory-level anomaly: AEMO published this stream with a malformed name. "
            f"URL is correct as stated — do NOT URL-encode special characters. "
            f"Treat as resolvable only if filename_template is not null."
        )
    if flag == "casing_mismatch_vs_sibling_tier":
        return (
            "CURRENT/ARCHIVE tiers use different casing for this stream. "
            "Preserve exact case per tier when constructing URLs; do not normalize."
        )
    return f"Extractor flag: {flag}"


def _infer_cadence(repo: str, tier: str) -> str:
    """Best-effort cadence label based on repo and tier name."""
    if repo == "Reports" and tier == "CURRENT":
        return "5min"
    if repo == "Reports" and tier == "ARCHIVE":
        return "daily_rollup"
    if repo == "MMSDM":
        if tier in {"DATA", "P5MIN_ALL_DATA", "PREDISP_ALL_DATA"}:
            return "5min"
        return "monthly_bulk"
    if repo == "NEMDE":
        return "daily"
    if repo == "FCAS_Causer_Pays":
        return "annual"
    return "unknown"


_AUX_SUFFIXES = {"_AUX", "DOCUMENTATION_AUX", "ROOT_AUX", "MONTH_ROOT_AUX", "SQLLOADER_AUX"}
_AUX_EXACT = {"MMSDM_MONTHLY_BULK", "MTPASA_DATA_EXPORT", "UNKNOWN", "UNPARSED"}
_UTILITY_EXTENSIONS = {".dll", ".exe", ".bat", ".sh", ".cmd", ".tar", ".gz"}


def _curate_keys(all_keys: list[str], datasets: dict) -> list[str]:
    """Return the curated user-facing subset of dataset keys.

    Rule: resolvable=true AND intra_repo_id not AUX/placeholder AND not utility-file.
    """
    out = []
    for key in sorted(all_keys):
        ds = datasets[key]
        if not ds["resolvable"]:
            continue
        iid = ds["intra_repo_id"]
        if iid in _AUX_EXACT:
            continue
        if any(iid.endswith(suf) for suf in _AUX_SUFFIXES):
            continue
        if any(iid.lower().endswith(ext) for ext in _UTILITY_EXTENSIONS):
            continue
        out.append(key)
    return out


_DEFAULT_PLACEHOLDERS = {
    "date": {"format": "yyyymmdd", "example": "20250407", "regex": "\\d{8}"},
    "timestamp": {"format": "yyyymmddhhmm", "example": "202504070445", "regex": "\\d{12}"},
    "aemo_id": {"format": "16-digit AEMO identifier", "example": "0000000513144978", "regex": "\\d{16}"},
    "year": {"format": "yyyy", "example": "2025", "regex": "\\d{4}"},
    "month": {"format": "mm", "example": "04", "regex": "\\d{2}"},
    "yyyymm": {"format": "yyyymm", "example": "202504", "regex": "\\d{6}"},
    "yyyymmddHHMM": {"format": "yyyymmddHHMM", "example": "202504070445", "regex": "\\d{12}"},
    "nn": {"format": "zero-padded 2-digit", "example": "00", "regex": "\\d{2}"},
    "d1": {"format": "single digit", "example": "1", "regex": "\\d{1}"},
    "d2": {"format": "two digits", "example": "04", "regex": "\\d{2}"},
    "d11": {"format": "11 digits", "example": "20220604167", "regex": "\\d{11}"},
    "d13": {"format": "13 digits", "example": "2011110909700", "regex": "\\d{13}"},
}

# Base name → semantics for disambiguated variants (e.g. date1, date2; year1, year2).
# Matched against the suffix-stripped token name.
_BASE_LABEL_REGEX = {
    "date": ("yyyymmdd", "\\d{8}", "20250407"),
    "timestamp": ("yyyymmddhhmm", "\\d{12}", "202504070445"),
    "datetime": ("yyyymmddhhmmss", "\\d{14}", "20260416044500"),
    "year": ("yyyy", "\\d{4}", "2025"),
    "yearmonth": ("yyyymm", "\\d{6}", "202504"),
    "yyyymmddhh": ("yyyymmddhh", "\\d{10}", "2025040704"),
    "aemo_id": ("16-digit AEMO identifier", "\\d{16}", "0000000513144978"),
}

_VARIANT_SUFFIX_RE = re.compile(r"^(?P<base>[a-zA-Z]+?)(?P<idx>\d+)$")
_TOKEN_SCAN_RE = re.compile(r"\{(\w+)\}")


def _infer_placeholder_def(name: str) -> dict[str, str]:
    """Best-effort definition for a placeholder name the extractor emitted.

    Coverage is intentionally conservative. The extractor's labeler can produce
    names like `d21`/`d22` — these are disambiguation suffixes of `d2` (two
    2-digit positions in the same template), NOT 21/22-digit fields. Recovering
    the original digit count from the name alone is ambiguous, so for any
    d-token not in the curator's `_DEFAULT_PLACEHOLDERS`, the inference emits
    a broad `\\d+` regex and directs users to the per-tier `filename_regex`
    for the exact shape.
    """
    if name in _DEFAULT_PLACEHOLDERS:
        return _DEFAULT_PLACEHOLDERS[name]

    # Direct base-name match (yearmonth, datetime, yyyymmddhh, aemo_id — fixed shape)
    if name in _BASE_LABEL_REGEX:
        fmt, rx, ex = _BASE_LABEL_REGEX[name]
        return {"format": fmt, "example": ex, "regex": rx}

    # Disambiguation suffix variants of known temporal bases (date1, date2, year1, year2)
    mv = _VARIANT_SUFFIX_RE.match(name)
    if mv and mv.group("base") in _BASE_LABEL_REGEX:
        fmt, rx, ex = _BASE_LABEL_REGEX[mv.group("base")]
        return {"format": fmt, "example": ex, "regex": rx}

    # Anything else (d{N} disambiguation variants, unknown suffixes): conservative
    # fallback. The per-tier `filename_regex` is the authoritative shape — the
    # placeholder record is informational for discoverability.
    return {
        "format": f"extractor-emitted token {name!r}; see per-tier filename_regex for exact shape",
        "example": "",
        "regex": "\\d+",
    }


def _placeholders_for(datasets: dict) -> dict[str, dict]:
    """Return a placeholders section that declares every token used in any
    emitted filename_template or path_template.

    Scans the datasets dict after tier records are built, collects the union
    of `{token}` names, and ensures each has a definition. Seed with
    _DEFAULT_PLACEHOLDERS for the known-good curated set, then infer the rest.
    """
    used: set[str] = set()
    for rec in datasets.values():
        for tier in rec.get("tiers", {}).values():
            for key in ("filename_template", "path_template"):
                value = tier.get(key) or ""
                used.update(_TOKEN_SCAN_RE.findall(value))

    result: dict[str, dict] = dict(_DEFAULT_PLACEHOLDERS)
    for name in sorted(used):
        if name not in result:
            result[name] = _infer_placeholder_def(name)
    return result


if __name__ == "__main__":
    sys.exit(main())
