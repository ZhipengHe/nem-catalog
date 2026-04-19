# NEMWeb Structural Findings

Empirical observations about the layout of `https://nemweb.com.au/`, derived from the 2863 IIS directory listings captured in `nemweb-mirror/` on 2026-04-18. This file records what the site *actually* looks like, so downstream catalog work starts from ground truth instead of guesswork.

---

## 1. Top-level repositories

NEMWeb has **four** logical repositories, not dozens. A repository = a top-level URL subtree with its own organizational conventions.

| # | Repository | URL root | How it organizes content |
|---|---|---|---|
| 1 | **Reports** | `/Reports/` | Operational publishing hub. Two retention tiers (`CURRENT/`, `ARCHIVE/`). Each immediate child is one data stream. |
| 2 | **MMSDM** | `/Data_Archive/Wholesale_Electricity/MMSDM/` | Monthly bulk MMS Data Model dumps. Organized by `{year}/MMSDM_{year}_{month}/MMSDM_Historical_Data_SQLLoader/{file_type_view}/`. |
| 3 | **NEMDE** | `/Data_Archive/Wholesale_Electricity/NEMDE/` | Historical dispatch-engine XML bundles, organized by year. |
| 4 | **FCAS_Causer_Pays** | `/Data_Archive/Wholesale_Electricity/FCAS_Causer_Pays/` | Small historical causer-pays dataset. Only years 2011 and 2012 present. |

That's the full list. `/Reports/` and `/Data_Archive/` are the only two paths with children on nemweb.com.au; inside `/Data_Archive/` there is only one child, `/Data_Archive/Wholesale_Electricity/`, which contains the three repos above.

---

## 2. Per-repository structure

### 2.1 Reports

- Two retention tiers: `/Reports/CURRENT/` and `/Reports/ARCHIVE/`.
- `CURRENT/` holds **103 stream subdirs**.
- `ARCHIVE/` holds **68 stream subdirs**.
- Each stream subdir = one AEMO data stream (e.g. `DispatchIS_Reports/`, `TradingIS_Reports/`, `P5_Reports/`, `PREDISPATCHIS`-style, `Billing/`, `Settlements/`).
- Inside a stream subdir, files are time-stamped zips (sometimes `.csv`, `.xml`, etc.). Usually a flat listing with no further subdirectories.
- The same stream can appear in both tiers (a live 5-min file in `CURRENT/` rolls into a daily bundle in `ARCHIVE/`), or only in one tier.

Stream population across tiers (empirical):

- **Streams in both tiers (matched by case-insensitive name):** 66
- **Only in `CURRENT/`:** 37 (e.g. `ANCILLARY_SERVICES_REPORTS`, `Alt_Limits`, `Ancillary_Services_Payments`, `Auction_Units_Reports`, `CSC_CSP_*`, `Causer_Pays_*`, `DISPATCHIS_PRICE_REVISIONS`, `DWGM`, `Directions_Reconciliation`, `ECGS`, `FPP`, `FPP_HIST_REG_PERF`, `Gas_Supply_Guarantee`, `HighImpactOutages`, `IBEI`, `Marginal_Loss_Factors`, `Market_Notice`, `MMSDataModelReport`, `Network`, `PasaSnap`, `PD7Day`, `Public_Prices`, `PublishedModelDataAccess`, `Regional_Summary_Report`, `Reserve_Contract_Recovery`, `SRA_*`, `SSM_ENABLEMENT_*`, `SupplyDemand`, `Trading_Cumulative_Price`, `VicGas`, `Vwa_Fcas_Prices`, `Weekly_Constraint_Reports`, `Yesterdays_MNSPBids_Reports`).
- **Only in `ARCHIVE/`:** 2 — `DispatchIS_FCAS_Fix/` (one-off historical correction stream) and `NEXT_DAY_OFFER_ENERGY)SPARSE/` (anomaly — see §3).

### 2.2 MMSDM

- Layer 1: 18 year dirs (`2009/` through `2026/`) plus one sibling subtree, `MTPASA_DATA_EXPORT/`.
- Layer 2: one dir per month, named `MMSDM_{year}_{month}/`.
- Layer 3: always `MMSDM_Historical_Data_SQLLoader/` (single child of each month).
- Layer 4: **eleven** file-type views, each a sibling dir under SQLLoader (union across all months; individual months may expose a subset):

| View | Filename pattern (empirical) | Contents |
|---|---|---|
| `BCP_DATA/` | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymmddHHMM>.<ext>` | Bulk-copy data files |
| `BCP_FMT/`  | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymm>.fmt` | BCP format descriptors |
| `CTL/`      | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymm>.ctl` | SQL*Loader control files |
| `DATA/`     | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymmddHHMM>.zip` | Data archives (zip) |
| `DOCUMENTATION/` | `MMS Data Model/v{major}.{minor}/…` | Versioned HTML docs for the MMS Data Model (authoritative table inventory per version — **v4.26–v4.30, v5.0–v5.6, plus v5.3_PreRelease** observed) |
| `INDEX/`    | index files | Oracle index creation scripts |
| `LOGS/`     | loader log files | SQL*Loader run logs (month-scoped) |
| `MYSQL/`    | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymm>.sql` | MySQL DDL / DML variants per table |
| `P5MIN_ALL_DATA/` | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymmddHHMM>.zip` | 5-min-granular rolled-up data (subset of tables) |
| `PREDISP_ALL_DATA/` | similar | Pre-dispatch rolled-up data |
| `UTILITIES/` | loader utilities | SQL*Loader / BCP helper scripts |

- A **dataset** inside MMSDM = one `<TABLE>` identifier embedded in the `#`-delimited filename. A single table typically appears across multiple views (CTL + DATA + BCP_FMT + MYSQL in older months; view coverage differs by month).
- **`MTPASA_DATA_EXPORT/`** is a flat leaf directory at the MMSDM root level (not under any year). Contains a handful of MTPASA region-availability exports — a special-case dataset outside the year/month rhythm.
- Authoritative table inventory per MMS Data Model version lives in `MMSDM/{year}/MMSDM_{year}_{month}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{x.y}/` HTML files. These are the canonical source for resolving "same logical table, renamed across versions" questions.

### 2.3 NEMDE

- Layer 1: 18 year dirs (`2009/` through `2026/`).
- Layer 2: `NEMDE_{year}_{month}/`.
- Layer 3: `NEMDE_Market_Data/`.
- Layer 4: **two sibling subtrees** under `NEMDE_Market_Data/`:
  - `NEMDE_Files/` — the primary content tree.
  - `File_Readers/` — a separate subtree (reader scripts / utilities) present in every month.
- Layer 5 (leaf, under `NEMDE_Files/`): `NemPriceSetter_{yyyymmdd}_xml.zip` files — daily dispatch-engine price-setter XML bundles.

Shallower than MMSDM. Two subtrees per month, not one — any NEMDE catalog entry needs to distinguish `NEMDE_Files/` content from `File_Readers/` content.

### 2.4 FCAS_Causer_Pays

- Only two year dirs: `2011/` and `2012/`.
- Each year has a single `.txt` file (`2011.txt`, `2012.txt`).
- No retention-tier partitioning. Legacy dataset frozen at two years.

---

## 3. Structural anomalies in NEMWeb itself

Issues that originate on AEMO's side, not in my walker. Each one is load-bearing for any URL-catalog that tries to faithfully describe NEMWeb.

### 3.1 Casing inconsistency between CURRENT and ARCHIVE tiers

Three streams have different casing in CURRENT vs ARCHIVE for what is (empirically) the same data stream:

| CURRENT casing | ARCHIVE casing |
|---|---|
| `DISPATCH_NEGATIVE_RESIDUE` | `Dispatch_Negative_Residue` |
| `PDPASA_DUIDAvailability` | `PDPASA_DUIDAVAILABILITY` |
| `STPASA_DUIDAvailability` | `STPASA_DUIDAVAILABILITY` |

On AEMO's stated 2026-04-21 case-sensitivity enforcement, these become two different URLs for what is logically one dataset. Catalog entries must record the tier-specific casing exactly as observed in each tier's parent listing; no case normalization.

### 3.2 AEMO-side URL typo

`/Reports/ARCHIVE/NEXT_DAY_OFFER_ENERGY)SPARSE/` — close-paren instead of underscore, clearly unintended. The canonical form exists in both tiers as `Next_Day_Offer_Energy_SPARSE/`. The typo'd directory is a real, reachable URL on NEMWeb today (HTTP 200). Catalogs need to decide whether to: record it for completeness, flag it as an AEMO bug, or exclude it.

### 3.3 Retention asymmetry

- 37 streams exist in CURRENT but never roll over into ARCHIVE. Some of these may be permanent-live (e.g. `Market_Notice`), some may be short-lived (e.g. `PasaSnap`), some may be newer additions.
- 2 streams exist only in ARCHIVE (`DispatchIS_FCAS_Fix` for the historical correction; `NEXT_DAY_OFFER_ENERGY)SPARSE` for the typo).
- Any catalog that describes a Reports stream needs a retention-tier field, not an assumption of "both tiers always".

### 3.4 Filename-convention split: date-stamp vs full-timestamp within one dataset

Observed in MMSDM SQLLoader views (documented here because it's a real anomaly the catalog must handle). For a single table (e.g. `AGGREGATE_DISPATCH_GROUP`):

- `CTL/`, `BCP_FMT/`, `MYSQL/` carry a `{yyyymm}` stamp (month resolution).
- `DATA/`, `P5MIN_ALL_DATA/` carry a `{yyyymmddHHMM}` stamp (minute resolution — full datetime).

Same dataset, different time-granularity in the filename depending on the view. Not a bug — reflects AEMO's internal use of BCP/CTL as month-scoped bulk artifacts vs DATA as event-timestamped content.

---

## 4. Dataset identity across repositories (default: separate, merging requires proof)

**Default rule:** datasets living under different repos are treated as **separate datasets**, even when their names suggest otherwise. `Reports/DispatchIS_Reports` and `MMSDM/DISPATCHIS` are NOT presumed to be the same dataset. Nor are `Reports/TradingIS_Reports` and `MMSDM/TRADINGPRICE + TRADINGLOAD`. The URL structure alone does not establish identity, and name similarity is circumstantial.

**When to merge:** two cross-repo entries may be declared the same dataset **only** with explicit proof. Acceptable proof types:

1. **AEMO's own documentation says so** — a quoted statement from an AEMO doc (MMS Data Model HTML docs inside the mirror, a published AEMO data guide, an AEMO support note) that identifies the Reports stream and the MMSDM table as the same data product.
2. **Column-schema match** — if the contents of a Reports zip file and the corresponding MMSDM table share their column schema identically (same column names, types, order), that is strong evidence of identity. Requires opening files, which is outside the current scope of this document.
3. **AEMO's own internal cross-reference** — a reference in an MMSDM loader script, a README inside the mirror, or a filename that mentions the Reports-tier origin.

**When not to merge:**

- Matching prefixes (e.g. both contain "DISPATCHIS") is NOT proof; it is circumstantial.
- Same apparent content topic is NOT proof.
- Same publication cadence is NOT proof.
- "It seems obvious" is NOT proof.

**Catalog consequence:** dataset identity keys are `(repo, intra-repo_identifier)`. Two entries with structurally identical-looking names under different repos are distinct catalog entries until proof is supplied. Merge aliasing, if ever introduced, must cite the evidence inline (which doc, which section, which column comparison).

**Candidate merge-evidence sources in the mirror (for future work only — not to be used as assumptions now):**

- `MMSDM/.../DOCUMENTATION/MMS Data Model/v*/` HTML docs per-version table descriptions.
- Any `Readme.htm` or `disclaimer.htm` file present in MMSDM month dirs.
- External AEMO docs (not in the mirror; require explicit fetch).

---

## 5. Survey source

- Mirror root: `nemweb-mirror/` (local, not committed).
- Download run: 2026-04-18, approximately 2h15m at ≤1 req/s, single thread.
- Total listings captured: 2863.
- Completeness verified 2026-04-18 via HREF reverse-scan: every non-root directory HREF referenced in any saved page is on disk (only `/` is excluded, by design — it returns a 307 redirect off-site to aemo.com.au).
- Byte-exact HREF discipline: walker never normalized casing; every observation in this document is consistent with AEMO's canonical form as served in the parent listings.

---

## Build pipeline

```
┌──────────────────────────────────────┐
│ weekly cron (.github/weekly-refresh) │
└───────────────┬──────────────────────┘
                ▼
┌───────────────────────────────────────┐
│ nemweb_download.py --gaps (1 req/s)   │
│   → nemweb-mirror/** (HTML listings)  │
│ monthly: full recrawl as cross-check  │
└───────────────┬───────────────────────┘
                ▼
┌───────────────────────────────────────┐
│ extract_patterns.py::write_json       │
│   → patterns/auto/catalog.json        │
└───────────────┬───────────────────────┘
                ▼
       ┌────────┴─────────┐
       ▼                  ▼
┌──────────────┐  ┌────────────────────┐
│ patterns/    │  │ patterns/curated/  │
│ auto/ (gen)  │  │ (human overlays)   │
└──────┬───────┘  └─────────┬──────────┘
       └────────┬───────────┘
                ▼
┌──────────────────────────────────────┐
│ scripts/merge_catalog.py             │
│  5 merge rules + schema validation   │
│  → catalog.json                      │
└───────────────┬──────────────────────┘
                ▼
    ┌───────────┴─────────────┐
    ▼                         ▼
┌────────────────┐   ┌──────────────────┐
│ GH Releases +  │   │ PR with diff +   │
│ GitHub Pages   │   │ curated-audit    │
│ (canonical)    │   │ checklist        │
└────────────────┘   └──────────────────┘
         ▲
         │  catalog() live fetch (ETag) → cache → fallback
         │  catalog(catalog_version=X): pinned Release asset
         │  load(path_or_url): offline, deterministic
         │
┌────────┴─────────┐
│ nem_catalog SDK  │
│ (PyPI, stdlib)   │
└──────────────────┘
```

## Merge semantics

See `scripts/merge_catalog.py:merge`. Five rules:

1. Field overlap on auto-discovered key → curated wins, build warns with both values.
2. Curated-only field on an existing auto-discovered key → accept unconditionally.
3. Auto-only field or key → pass through untouched to the catalog.
4. Orphan curated key without `curated_only: true` → fail immediately.
5. Curated placeholder key with `curated_only: true` → keep it in the catalog as a curated-only entry.
