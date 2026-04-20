# NEMWeb Structural Findings

Empirical observations about the layout of `https://nemweb.com.au/`, derived from the 2863 IIS directory listings captured in `nemweb-mirror/` on 2026-04-19/20. This file records what the site *actually* looks like, so downstream catalog work starts from ground truth instead of guesswork.

**Revision history**

- **2026-04-21 (latest)** — §2.1.1 class-(a) classification correction. Byte-level primary-source re-walk of every `/DUPLICATE/` index.html found only 2 `_LEGACY.zip` files exist (in `Dispatch_Reports/DUPLICATE/` and `Predispatch_Reports/DUPLICATE/`), not 12. The prior revision pattern-inferred the 12 single-file DUPLICATEs as class-(a) placeholders without exhaustive filename reading; 10 of them actually hold plain non-LEGACY files and are functionally class-(b) stragglers. Distribution now: class-(a) = 2 dirs/2 files, class-(b) = 15 dirs/33 files, class-(c) = 1 dir/617 files. Three-class model itself unchanged — the `_LEGACY.zip` suffix is still a reliable file-level discriminator; only the claimed counts were wrong. Also corrected inline prose "8 CURRENT and 5 ARCHIVE" legit-nested to "9 and 4" (matches the table in the same section). Discovered during v0.1.2 DUPLICATE filter implementation when `Skipped 2 _LEGACY files` on the real mirror contradicted the expected 12.
- **2026-04-20** — Crawled `DOCUMENTATION/` tree across all 13 MMSDM schema versions (v4.26 → v5.6 + v5.3_PreRelease); captured 118 files (PDFs, xlsx, DDL bundles, release notes) to local `reference/aemo-mmsdm-docs/` (gitignored — regeneratable from nemweb.com.au, see `reference/aemo-mmsdm-docs/INVENTORY.md`). Extracted 7 versions of the AEMO cross-boundary Table↔File↔Report Relationships xlsx to CSV (336 → 392 mappings). Added schema-version timeline + cross-doc references to §2.2, §4, §6.
- **2026-04-20 (later)** — Deep-dive investigations: (1) ARCHIVE delta probe — 12 mirror dirs uncovered by catalog, 11 are empty listings; (2) MMSDM table inventory — 278 distinct tables cross-era, filename-format cutover at 2024-08 (DVD-era vs ARCHIVE-era); (3) `File_Readers/` characterized as static duplicated utility content; (4) `MTPASA_DATA_EXPORT` and `PDRCONFIG` contents enumerated; (5) DUPLICATE filename patterns classified. Resulting updates: rewrote §2.2 MMSDM filename section with dual-era tables; refined §2.1.1 DUPLICATE semantic model; corrected §3.3 `DispatchIS_FCAS_Fix` claim (now empty); added §3.5 MMSDM 2024-08 platform transition; tightened §6 coverage numbers.
- **2026-04-20** — Audit against mirror + AEMO's published catalog (`reference/aemo-catalog/`). Added §2.1.1 nested-subdir inventory and DUPLICATE table; reconciled §2.1 overlap math with §3.1 case-sensitivity rule; rewrote §2.2 MMSDM view table with per-month coverage; added §6 referencing AEMO's published catalog as supplementary metadata.
- **2026-04-19/20** — Initial structural survey from mirror walk.

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
- Inside a stream subdir, files are time-stamped zips (sometimes `.csv`, `.xml`, etc.). **Most** subdirs are flat, but 26 of 103 CURRENT dirs and 5 of 68 ARCHIVE dirs have further subdirectories — see §2.1.1.
- The same stream can appear in both tiers (a live 5-min file in `CURRENT/` rolls into a daily bundle in `ARCHIVE/`), or only in one tier.

Stream population across tiers (empirical). §3.1 mandates no case normalization, so both views are recorded:

| View | Both tiers | Only CURRENT | Only ARCHIVE |
|---|---:|---:|---:|
| **Case-sensitive** (byte-exact match) | 63 | 40 | 5 |
| **Case-insensitive** (after lowercasing) | 66 | 37 | 2 |

The 3-stream delta between views is exactly the 3 casing-mismatch pairs in §3.1 — under case-sensitive reading they count as CURRENT-only + ARCHIVE-only, under case-folding they collapse to one cross-tier pair each.

**Case-sensitive "Only in CURRENT/" (40)** includes, e.g., `ANCILLARY_SERVICES_REPORTS`, `Alt_Limits`, `Ancillary_Services_Payments`, `Auction_Units_Reports`, `CSC_CSP_*`, `Causer_Pays_*`, `DISPATCH_NEGATIVE_RESIDUE`, `DISPATCHIS_PRICE_REVISIONS`, `DWGM`, `Directions_Reconciliation`, `ECGS`, `FPP`, `FPP_HIST_REG_PERF`, `Gas_Supply_Guarantee`, `HighImpactOutages`, `IBEI`, `Marginal_Loss_Factors`, `Market_Notice`, `MMSDataModelReport`, `Network`, `PasaSnap`, `PD7Day`, `PDPASA_DUIDAvailability`, `Public_Prices`, `PublishedModelDataAccess`, `Regional_Summary_Report`, `Reserve_Contract_Recovery`, `SRA_*`, `SSM_ENABLEMENT_*`, `STPASA_DUIDAvailability`, `SupplyDemand`, `Trading_Cumulative_Price`, `VicGas`, `Vwa_Fcas_Prices`, `Weekly_Constraint_Reports`, `Yesterdays_MNSPBids_Reports`.

**Case-sensitive "Only in ARCHIVE/" (5):** `Dispatch_Negative_Residue`, `DispatchIS_FCAS_Fix` (one-off historical correction), `NEXT_DAY_OFFER_ENERGY)SPARSE` (typo — see §3.2), `PDPASA_DUIDAVAILABILITY`, `STPASA_DUIDAVAILABILITY`. Three of those five (the `Negative_Residue` + the two `DUIDAVAILABILITY` entries) become cross-tier pairs under case-folding.

#### 2.1.1 Nested subdirectory structures in Reports/

The "usually flat" claim needs qualification. Two patterns exist: **AEMO-created sub-datasets** (legit multi-dataset children of a parent stream) and **`DUPLICATE/` subtrees** (anomalous; see discussion below).

**Legit nested sub-dataset structure.** 9 CURRENT dirs and 4 ARCHIVE dirs contain named child datasets the consumer needs to enumerate separately:

| Parent stream | CURRENT subdirs | ARCHIVE subdirs | Notes |
|---|---|---|---|
| `GSH/` | 13 | 13 | Gas Supply Hub sub-datasets: `GSH_Participants`, `GSH_Daily_Trans_Summary`, `GSH_Historical_Trans_Summary`, `GSH_ZONE_CURTAILMENT_INFORMATION`, `GSH_CAPACITY_TRANSACTION`, `GSH_CAPACITY_TRANSFER_AUCTION_NOTICE`, `GSH_AUCTION_CURTAILMENT_NOTICE`, `GSH_AUCTION_QUANTITIES`, `GSH_REVISED_AUCTION_QUANTITIES`, `GSH_AUCTION_PRICE_VOLUME`, `GSH_REGISTERED_FACILITIES`, `GSH_REGISTERED_SERVICE_POINTS`, `Benchmark_Price`. |
| `Operational_Demand/` | 9 | 6 | `ACTUAL_5MIN`, `ACTUAL_HH`, `ACTUAL_DAILY`, `ACTUAL_HH_AREA`, `ACTUAL_DAILY_AREA`, `ACTUAL_UPDATE`, `ACTUAL_UPDATE_AREA`, `FORECAST_HH`, `FORECAST_HH_AREA`. ARCHIVE is a subset (no `ACTUAL_5MIN`, `ACTUAL_UPDATE`, `ACTUAL_UPDATE_AREA`). |
| `ROOFTOP_PV/` | 4 | 4 | `FORECAST`, `FORECAST_AREA`, `ACTUAL`, `ACTUAL_AREA`. Full parity. |
| `Operational_Demand_Less_SNSG/` | 3 | 2 | `ACTUAL_UPDATE`, `ACTUAL_DAILY`, `ACTUAL_HH` (ARCHIVE lacks `ACTUAL_UPDATE`). |
| `MMSDataModelReport/` | 3 | — | `Gas/`, `Electricity/`, `PDRCONFIG/`. `Gas/` and `Electricity/` are HTML-document trees (the published MMS Data Model reports). `PDRCONFIG/` holds exactly 2 files: `PREPROD_PUBLIC_PDR_CONFIG_FULL.zip` + `PROD_PUBLIC_PDR_CONFIG_FULL.zip` (PDR = "Public Data Release"; these are environment-specific config bundles). CURRENT-only. |
| `GBB/` | 3 | — | `ForecastUtilisation/`, `GBB_PIPELINE_CONNECTION_FLOW/`, `DUPLICATE/`. Two legit sub-datasets plus a DUPLICATE. CURRENT-only (Gas Bulletin Board is `CURRENT`-tier-only). |
| `STTM/` | 2 | — | `Contingency_Gas/`, `MOS%20Estimates/` (URL-encoded "MOS Estimates", with a literal space). CURRENT-only. |
| `DWGM/` | 1 | — | `MOS%20Estimates/`. CURRENT-only. |
| `ECGS/` | 1 | — | `ECGS_Notices/` — itself contains an `Attachments/` sub-sub-dir (the only 3-level nesting in `/Reports/`). CURRENT-only. |

**DUPLICATE subtree anomaly (CURRENT-only phenomenon).** 18 CURRENT dirs have a `DUPLICATE/` subdir. **`DUPLICATE/` does NOT appear in the ARCHIVE tier for any stream.** File-count distribution:

| Parent stream | Files in DUPLICATE/ | Character |
|---|---:|---|
| `GBB/` | **617** | Rolling timestamped archive — `GasBB*.zip`/`.CSV` (matches parent filenames) plus timestamped variants like `GasBBActualFlowStorageLast31_{yyyymmddHHMMSS}.CSV`. The parent `GBB/` dir holds only "latest" copies; `GBB/DUPLICATE/` preserves the historical snapshots. Parent stream curated as `append_only` in `patterns/curated/freshness-policy.yaml:86`. |
| `PredispatchIS_Reports/` | 9 | Non-LEGACY filenames matching parent regex (`PUBLIC_PREDISPATCHIS_{yyyymmddHHMM}_{yyyymmddHHMMSS}.zip`). Sparse timestamps (e.g. 2016-10-23, 2016-11-14). Orphan files. |
| `Next_Day_PreDispatch/` | 6 | Non-LEGACY, parent regex match (`PUBLIC_NEXT_DAY_PREDISPATCH_{yyyymmdd}_{aemo_id}.zip`). Sparse timestamps across multiple years. |
| `MCCDispatch/` | 3 | Non-LEGACY, parent regex match (`PUBLIC_MCCDISPATCH_{yyyymmddHHMM}_{aemo_id}.zip`). 3 files spread across 9 years (2017, 2025, 2026). One-off orphans. |
| `Next_Day_Intermittent_DS/` | 3 | Non-LEGACY, parent regex match. All 3 from 2020. |
| `Trading_Cumulative_Price/` | 2 | Non-LEGACY, parent regex match (`PUBLIC_TRADING_CUMULATIVE_PRICE_{yyyymmddHHMM}_{aemo_id}.zip`). Two files: 2020-08-23 and 2025-08-12. |
| 2 CURRENT dirs (class-(a) `_LEGACY.zip` placeholders) | 1 each | `Dispatch_Reports/DUPLICATE/` + `Predispatch_Reports/DUPLICATE/`. Filename ends in `_LEGACY.zip`. These are the only 2 dirs where the parent stream publishes `_LEGACY` filenames in CURRENT (`Dispatch_Reports/`: 577 `_LEGACY`, `Predispatch_Reports/`: 672 `_LEGACY`), so the DUPLICATE placeholder is a 1-copy self-reference of the legacy-format convention. |
| 10 CURRENT dirs (class-(b) non-LEGACY singletons) | 1 each | See list below. Filenames match parent's ordinary regex; **no `_LEGACY` suffix**. Functionally identical to the 5 multi-file straggler subtrees above. |
| **Total** | **652** | |

**Class-(b) non-LEGACY singletons (10 dirs).** `DISPATCH_NEGATIVE_RESIDUE`, `Dispatch_IRSR`, `Dispatch_SCADA`, `Dispatchprices_PRE_AP`, `P5_Reports`, `P5MINFCST`, `Predispatch_Sensitivities`, `SEVENDAYOUTLOOK_FULL`, `TradingIS_Reports`, `Yesterdays_Bids_Reports`. Each holds exactly one file matching the parent stream's non-LEGACY filename regex (e.g. `Dispatch_SCADA/DUPLICATE/PUBLIC_DISPATCHSCADA_202508121115_0000000475994495.zip` — plain parent-regex filename, not `_LEGACY`). Timestamps are sparse across years (2016–2026). Mechanism unclear: sparse one-off republishes from the parent stream, not format-migration placeholders.

Semantics are undocumented by AEMO — AEMO's published catalog (see §6) is silent on every `DUPLICATE/` subtree. Observed filename evidence supports a **three-category classification**:

1. **Class (a) — single-file `_LEGACY.zip` placeholders** (**2 cases**: `Dispatch_Reports/DUPLICATE/`, `Predispatch_Reports/DUPLICATE/`). Exactly one file, ends in `_LEGACY.zip`, matches the parent stream's documented `LEGACY` filename convention (parent also publishes `_LEGACY` files as live data). A 1-copy self-reference of that legacy-format convention. Not live data.
2. **Class (b) — non-LEGACY straggler subtrees** (**15 cases**, 33 files total). Splits into:
   - *Multi-file stragglers* (5 cases, 23 files): `MCCDispatch`, `Next_Day_Intermittent_DS`, `Next_Day_PreDispatch`, `PredispatchIS_Reports`, `Trading_Cumulative_Price`.
   - *Single-file non-LEGACY* (10 cases, 10 files): see list above.
   Filenames match parent's non-legacy regex; no `_LEGACY` suffix. Timestamps are sparse across years, suggesting one-off orphans / residue from specific events, not continuous streams. Structurally identical to parent content; unclear whether to treat as data or residue.
3. **Class (c) — `GBB/DUPLICATE/` rolling archive** (1 case, 617 files) — parent-dataset filenames with optional `_{yyyymmddHHMMSS}` suffix. Parent `GBB/` holds one current copy of each file; `GBB/DUPLICATE/` holds historical timestamped copies. Functionally an append-only archive masquerading as a DUPLICATE subtree, operationally indistinguishable from a live dataset.

**Recon history on class (a).** A prior revision of this section listed all 12 single-file DUPLICATE dirs as class-(a) `_LEGACY.zip` placeholders. Primary-source re-walk of every filename in every `/DUPLICATE/` index.html (see `scripts/extract_patterns.py` fix log, v0.1.2) found only 2 dirs actually contain `_LEGACY` filenames; the other 10 hold plain non-LEGACY parent-regex filenames. The pattern-inferred count was wrong. Byte-level verification: `grep -c '_LEGACY' nemweb-mirror/Reports/CURRENT/*/DUPLICATE/index.html` returns exactly 2 non-zero matches.

Any catalog filter touching `/DUPLICATE/` must distinguish these three sub-cases — an unconditional skip regresses `GBB/DUPLICATE`'s 617 files and the 23 multi-file + 10 single-file non-LEGACY stragglers, total 650 files lost. The `_LEGACY.zip` filename suffix is a reliable discriminator at the **file** level: present = class-(a) placeholder, absent = class-(b) or class-(c) real file. A **listing-level** filter ("skip listing if every file ends in `_LEGACY.zip`") catches exactly the 2 class-(a) dirs without false positives.

### 2.2 MMSDM

- Layer 1: 18 year dirs (`2009/` through `2026/`) plus one sibling subtree, `MTPASA_DATA_EXPORT/`.
- Layer 2: one dir per month, named `MMSDM_{year}_{month}/`. Earliest month on mirror is `MMSDM_2009_07` (July 2009); latest as of 2026-04-20 is `MMSDM_2026_03`. **Total: 135 month dirs** (not 216 = 18×12 — 2009 starts in July and 2026 only runs through the latest complete month).
- Layer 3: always `MMSDM_Historical_Data_SQLLoader/` (single child of each month).
- Layer 4: file-type views under SQLLoader. **11 views exist in the union across all months, but no single month exposes all 11.** Per-month presence varies substantially:

| View | Months present / 135 | Notes |
|---|---:|---|
| `BCP_DATA/` | 135 | Bulk-copy data files. Stable core. |
| `BCP_FMT/` | 135 | BCP format descriptors. Stable core. |
| `CTL/` | 135 | SQL*Loader control files. Stable core. |
| `DATA/` | 135 | Primary monthly table data (zip). Stable core. |
| `DOCUMENTATION/` | 135 | Versioned HTML docs for the MMS Data Model (authoritative table inventory per version — **v4.26–v4.30, v5.0–v5.6, plus v5.3_PreRelease** observed, 13 versions total). Stable core. |
| `PREDISP_ALL_DATA/` | 135 | Pre-dispatch rolled-up data. Stable core. |
| `UTILITIES/` | 134 | SQL*Loader / BCP helper scripts. **Missing from `MMSDM_2022_10`.** |
| `INDEX/` | 133 | Oracle index creation scripts. **Missing from `MMSDM_2024_08` and `MMSDM_2025_09`.** |
| `P5MIN_ALL_DATA/` | 85 | 5-min-granular rolled-up data. **Added 2019-03** (aligns with 5-minute settlement rule introduction). |
| `LOGS/` | 59 | SQL*Loader run logs. Non-contiguous: 2015-01 to 2018-05 continuous, **gap 2018-06 to 2024-02**, resumes 2024-03 onward. |
| `MYSQL/` | 20 | MySQL DDL / DML variants. **Added 2024-08.** |

The **stable-core set is 6 views** (BCP_DATA, BCP_FMT, CTL, DATA, DOCUMENTATION, PREDISP_ALL_DATA), present in 135/135 months. Everything else has coverage gaps the catalog must encode per-month.

**Filename convention inside each view changed at 2024-08 — dual-era split.** Files use one of two formats depending on month:

| Era | Month range | Filename pattern (DATA/BCP_DATA/P5MIN_ALL_DATA) | Filename pattern (BCP_FMT/CTL/MYSQL) | File-per-table count |
|---|---|---|---|---:|
| **DVD-era** | 2015-01 → 2024-07 (115 months) | `PUBLIC_DVD_<TABLE>_<yyyymmddHHMMSS>.zip` | `PUBLIC_DVD_<TABLE>_<yyyymm>.{fmt,ctl}` (month granularity) | 1 per table per month |
| **ARCHIVE-era** | 2024-08 → current (20 months) | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymmddHHMMSS>.zip` | `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymm>.{fmt,ctl,sql}` | N per table per month (split into `FILE01`, `FILE02`, …) |

The cutover is **clean**: no month has both formats. The move to `FILE<NN>` splitting means per-month file count roughly doubled (~284 → ~742 files/month). See §3.5 for the full platform-transition context.

- A **dataset** inside MMSDM = one `<TABLE>` identifier embedded in the filename (before the first `_` separator in DVD-era, between `#` delimiters in ARCHIVE-era).
- **MMSDM distinct-table inventory (this walk):**
  - DVD-era: **170 distinct tables** across 115 months.
  - ARCHIVE-era: **246 distinct tables** across 20 months.
  - Cross-era union: **278 distinct tables** (138 appear in both eras, 32 appear only in DVD-era, 108 appear only in ARCHIVE-era).
  - Per-month table count: range 131–238, mean ~157. Min at `MMSDM_2021_05` (131), max at `MMSDM_2026_03` (238).
  - Full lifecycle classification of every table lives in `reference/MMSDM-TABLE-LIFECYCLE.md` (companion doc) + `reference/MMSDM-TABLE-LIFECYCLE.csv` (per-table machine-readable detail). Seven lifecycle classes: 90 ALWAYS_PRESENT core, 70 ADDED_AT_CUTOVER (2024-08 platform transition), 46 INTERMITTENT (gaps within lifetime), 32 ADDED_IN_ARCHIVE_ERA (post-cutover additions including 17-table FPP subsystem at 2024-12), 19 RETIRED_AT_CUTOVER, 13 ADDED_LATE_STILL_LIVE (incl. 2018-05 MTPASA schema redesign + 2016-08 rooftop-PV addition), 8 RETIRED_EARLY (incl. 2021 five-minute-settlement-era retirements: `TRADINGLOAD`, `TRADINGREGIONSUM`, `INTERCONNMWFLOW`).
- A single table typically appears across multiple views (CTL + DATA + BCP_FMT in all months; + MYSQL from 2024-08; + P5MIN_ALL_DATA from 2019-03 for eligible tables). The view-coverage table above is the authoritative reference for which views to expect in a given month.
- **`MTPASA_DATA_EXPORT/`** is a flat leaf directory at the MMSDM root level (not under any year). Contains exactly **7 files**: 6 yearly zips `{year}_DATA_EXPORT_MTPASA_REGIONAVAILABILITY.zip` for 2014–2019, plus one one-off tracking file `PUBLIC_MTPASA_REGIONAVAIL_TRK_20191024093822_NEM02.zip`. **Last updated 2019-10 — the dataset appears frozen.** AEMO's published catalog (§6) does not reference this subtree.
- Authoritative table inventory per MMS Data Model version lives in `MMSDM/{year}/MMSDM_{year}_{month}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{x.y}/` HTML files. These are the canonical source for resolving "same logical table, renamed across versions" questions. A newer, live-served version is also published at `https://nemweb.com.au/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity%20Data%20Model%20Report.htm` (reachable from `Reports/CURRENT/MMSDataModelReport/`, see §2.1.1).
- **Local capture of every MMSDM DOCUMENTATION/ version lives at `reference/aemo-mmsdm-docs/`** (gitignored — 177 MB, regeneratable). Contains one subdir per schema version (v4.26 through v5.6 plus v5.3_PreRelease, 13 versions total) with the Upgrade Report PDF, Package Summary PDF, Data Model Report PDF, EMMS Technical Specification / Release Notes PDF, `MMSDM_create_v{X.Y}.zip` / `MMSDM_upgrade_v{X.Y}.zip` DDL bundles, and — for v4.26 through v5.1 — the authoritative Table↔File↔Report Relationships xlsx (see §4 and `reference/aemo-mmsdm-docs/INVENTORY.md`).

### 2.2.1 MMSDM schema version timeline

Every monthly MMSDM/{year}/{month}/ directory's `DOCUMENTATION/MMS Data Model/` contains exactly one current schema version. The version → first-month map (derived from mirror walk):

| Version | First month | Last month | Months live | Release context |
|---|---|---|---:|---|
| v4.26 | 2016-09 | 2017-10 | 14 | earliest walked — Nov 2016 Wholesale Systems Tech Spec |
| v4.27 | 2017-11 | 2018-11 | 13 | Oct–Dec 2017 EMMS release |
| v4.28 | 2018-12 | 2019-08 | 9 | Jan 2019 release |
| v4.29 | 2019-09 | 2020-02 | 6 | Oct 2019 SRA release |
| v4.30 | 2020-03 | 2021-02 | 12 | last v4.x — 5MS Reallocations |
| v5.0 | 2021-03 | 2021-09 | 7 | 5-minute-settlement design (Oct 2020 FAQ) |
| v5.1 | 2021-10 | 2023-04 | **18** | 5-minute settlement goes live (Oct 2021) — longest-running |
| v5.2 | 2023-05 | 2024-02 | 10 | May 2023 |
| v5.3_PreRelease | 2024-02 | 2024-09 | 8 | BidOffer table-rename prep — transition scripts |
| v5.3 | 2024-03 | 2024-09 | 7 | April 2024 — DVD→ARCHIVE filename cutover mid-lifecycle at 2024-08 |
| v5.4 | 2024-10 | 2025-03 | 6 | Nov 2024 — doc naming switches to "Electricity Data Model …" |
| v5.5 | 2025-04 | 2025-10 | 7 | April 2025 — FPP (Frequency Performance Payments) |
| v5.6 | 2025-10 | 2026-03 | 6 | Nov 2025 — SSM + ISF; GA 2025-11-19 |

Pre-2015 MMSDM months exist on AEMO but were not walked to listing level; earlier v4.0 through v4.25 documentation presumably lives there. See `reference/aemo-mmsdm-docs/INVENTORY.md` for per-version file lists and SHA256 checksums.

### 2.3 NEMDE

- Layer 1: 18 year dirs (`2009/` through `2026/`).
- Layer 2: `NEMDE_{year}_{month}/`. Earliest month `NEMDE_2009_07` (July 2009); AEMO's published catalog lists 201 month entries for NEMDE — see §6.
- Layer 3: `NEMDE_Market_Data/`.
- Layer 4: **two sibling subtrees** under `NEMDE_Market_Data/`:
  - `NEMDE_Files/` — the primary content tree (month-varying data).
  - `File_Readers/` — a **static utility subtree duplicated identically into every month**. Verified 2026-04-20: 5 sampled months (2009-07, 2015-06, 2020-01, 2024-06, 2026-03) each contain exactly the same 2 files — `NEMDE 1-18 File Readers.zip` (524,878 bytes, byte-exact across all months) and `Readme.htm`. AEMO's published catalog does not reference this subtree. For catalog purposes treat as one canonical reference asset, not per-month content.
- Layer 5 (leaf, under `NEMDE_Files/`): `NemPriceSetter_{yyyymmdd}_xml.zip` files — daily dispatch-engine price-setter XML bundles.

Shallower than MMSDM. Two subtrees per month, not one — but one of the two (`File_Readers/`) is static across all months, so a catalog should not expose 201 redundant copies.

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

- 37 streams (case-insensitive count; 40 case-sensitive) exist in CURRENT but never roll over into ARCHIVE. Some of these may be permanent-live (e.g. `Market_Notice`), some may be short-lived (e.g. `PasaSnap`), some may be newer additions.
- 2 streams (case-insensitive; 5 case-sensitive counting the §3.1 casing-pair doubles) exist only in ARCHIVE. `NEXT_DAY_OFFER_ENERGY)SPARSE` is the §3.2 typo. `DispatchIS_FCAS_Fix` is a stub — earlier revisions of this doc described it as a "historical correction stream", but live-probe verification 2026-04-20 shows the listing is **empty** (only a `[To Parent Directory]` link). Whatever historical-correction content once lived there has been removed. For catalog purposes treat as an empty shell.
- **11 of 12 ARCHIVE dirs not covered by AEMO's published catalog (see §6) are also empty listings** — `Bidmove_Summary`, `CDEII`, `DispatchIS_FCAS_Fix`, `GBB`, `Market_Notice`, `Next_Day_Offer_Energy`, `NEXT_DAY_OFFER_ENERGY)SPARSE`, `Next_Day_Offer_FCAS`, `Weekly_Bulletin`, `Yesterdays_Bids_Reports`, `Yesterdays_MNSPBids_Reports`. Only `HistDemand` (12 zip files) has actual content. These 11 empty-ARCHIVE stubs appear to be placeholder dirs AEMO provisions but hasn't populated.
- Any catalog that describes a Reports stream needs both a retention-tier field and an "empty-ARCHIVE" flag, not an assumption of "both tiers always carry data".

### 3.4 Filename-convention split: date-stamp vs full-timestamp within one dataset

Observed in MMSDM SQLLoader views (documented here because it's a real anomaly the catalog must handle). For a single table (e.g. `AGGREGATE_DISPATCH_GROUP`) in the **ARCHIVE-era format** (2024-08+, see §3.5):

- `CTL/`, `BCP_FMT/`, `MYSQL/` carry a `{yyyymm}` stamp (month resolution).
- `DATA/`, `P5MIN_ALL_DATA/`, `BCP_DATA/` carry a `{yyyymmddHHMMSS}` stamp (second resolution — full datetime).

Same dataset, different time-granularity in the filename depending on the view. Not a bug — reflects AEMO's internal use of BCP/CTL as month-scoped bulk artifacts vs DATA as event-timestamped content. The DVD-era format (pre-2024-08) has the same month-vs-datetime split at filename position, but with `PUBLIC_DVD_<TABLE>_...` naming instead of `PUBLIC_ARCHIVE#<TABLE>#...`.

### 3.5 MMSDM platform transition at 2024-08

A simultaneous multi-change cutover happened at `MMSDM_2024_08`. Everything on this list starts that month, with no overlap in either direction:

1. **Filename format change** — `PUBLIC_DVD_<TABLE>_<timestamp>.zip` → `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<timestamp>.zip`. Delimiter changes from `_` to `#`; prefix changes from `DVD` to `ARCHIVE`; a new `FILE<NN>` sub-index appears.
2. **Multi-file table splitting** — DVD-era had 1 file per table per month. ARCHIVE-era splits each table's monthly data across multiple `FILE01`, `FILE02`, … archives. Per-month total file count roughly doubled (e.g. 2015-01: 284 DATA files → 2026-03: 742 DATA files).
3. **`MYSQL/` view added** — SQL dump variants of each table, previously absent.
4. **Table-schema additions** — 108 new tables appear in ARCHIVE-era that were not in DVD-era; 32 DVD-era-only tables are absent (likely renamed or retired). 138 tables are stable across both eras.

Any catalog covering MMSDM pre-2024-08 and post-2024-08 months must treat these as two distinct filename dialects — a single regex does not cover both. `reference/URL-CONVENTIONS.md` should record both dialects explicitly.

The catalog published by AEMO (§6) ignores everything below the `DATA/` view, so this transition is only visible via the mirror walk.

---

## 4. Dataset identity across repositories (default: separate, merging requires proof)

**Default rule:** datasets living under different repos are treated as **separate datasets**, even when their names suggest otherwise. `Reports/DispatchIS_Reports` and `MMSDM/DISPATCHIS` are NOT presumed to be the same dataset. Nor are `Reports/TradingIS_Reports` and `MMSDM/TRADINGPRICE + TRADINGLOAD`. The URL structure alone does not establish identity, and name similarity is circumstantial.

**When to merge:** two cross-repo entries may be declared the same dataset **only** with explicit proof. Acceptable proof types:

1. **AEMO's own documentation says so** — a quoted statement from an AEMO doc (MMS Data Model HTML docs inside the mirror, a published AEMO data guide, an AEMO support note) that identifies the Reports stream and the MMSDM table as the same data product.
2. **Column-schema match** — if the contents of a Reports zip file and the corresponding MMSDM table share their column schema identically (same column names, types, order), that is strong evidence of identity. Requires opening files, which is outside the current scope of this document.
3. **AEMO's own internal cross-reference** — a reference in an MMSDM loader script, a README inside the mirror, or a filename that mentions the Reports-tier origin. **Primary artifact: the `MMS Data Model Table to File to Report Relationships.xlsx` that AEMO shipped in every MMSDM version v4.26 through v5.1.** Captured locally to `reference/aemo-mmsdm-docs/{version}/Table_File_Report_Relationships.xlsx` and extracted to `table-file-report-mapping.csv` for 7 versions (336–392 rows per version). Each row maps `MMSDM_PACKAGE_NAME` × `MMSDM_TABLE_NAME` → `PDR_REPORT_NAME` (Reports/ stream) × `FILE_NAME` (template) × `PDR_REPORT_TRANSACTION_TYPE`. Example resolved pairs: `DEMANDOPERATIONALACTUAL` (MMSDM) ↔ `OPERATIONAL_DEMAND` (Reports); `APEVENT` (MMSDM) ↔ `AP` (Reports); `CONSTRAINTRELAXATION_OCD` (MMSDM) ↔ `DISPATCHOCD` (Reports); `GDINSTRUCT` (MMSDM) ↔ `GD_INSTRUCT` (Reports); `MARKETNOTICEDATA` (MMSDM) ↔ `MARKET_NOTICE` (Reports). **AEMO stopped publishing the xlsx after v5.1 (Oct 2021)** — post-v5.1 additions (FPP_*, SSM_*, AREA, REGION_AREA, etc.) require proof type 2 (column-schema match) instead.

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

## 5. Survey sources

**Primary — mirror walk:**

- Mirror root: `nemweb-mirror/` (local, not committed).
- Download run: **2026-04-19 / 2026-04-20** (2262 listings dated 2026-04-19, 601 listings dated 2026-04-20). Approximately 2h15m at ≤1 req/s, single thread. Earlier revisions of this doc cited "2026-04-18"; that was off by 1-2 days — the 2026-04-18 line in prior revisions predates the actual walk.
- Total listings captured: 2863 (plus one non-listing file, `nemweb-mirror/download.log`, for 2864 files total on disk).
- Completeness verified via HREF reverse-scan: every non-root directory HREF referenced in any saved page is on disk (only `/` is excluded, by design — it returns a 307 redirect off-site to aemo.com.au).
- Byte-exact HREF discipline: walker never normalized casing; every observation in this document is consistent with AEMO's canonical form as served in the parent listings.

**Secondary — AEMO-published catalog (`reference/aemo-catalog/`):**

- Captured 2026-04-20 from `https://visualisations.aemo.com.au/aemo/nemweb/`.
- 97 dataset manifests + 97 field-schema YAMLs + master `dataset-list.yaml`.
- See `reference/aemo-catalog/FETCH-MANIFEST.md` for SHA256 checksums and re-capture command.
- Usage: see §6 below.

**Tertiary — per-version MMSDM DOCUMENTATION (`reference/aemo-mmsdm-docs/`, gitignored):**

- Captured 2026-04-20. 118 files across 13 schema version dirs (v4.26 → v5.6 + v5.3_PreRelease), 177 MB.
- Contents per version: Upgrade Report PDF, Package Summary PDF, Data Model Report PDF, EMMS Technical Specification / Release Notes PDF, DDL zips (`MMSDM_create_v{X.Y}.zip`, `MMSDM_upgrade_v{X.Y}.zip`), and (v4.26–v5.1 only) Table↔File↔Report Relationships xlsx + extracted CSV.
- Not committed — regeneratable from nemweb.com.au per `reference/aemo-mmsdm-docs/INVENTORY.md`.
- Usage: primary source for §4 cross-repo identity (via the captured xlsx), §2.2.1 version timeline, and `reference/MMSDM-TABLE-LIFECYCLE.md` rename confirmation.

---

## 6. AEMO's published catalog (supplementary cross-reference)

AEMO publishes a machine-readable catalog at `https://visualisations.aemo.com.au/aemo/nemweb/`, served as the data source behind AEMO's JS-rendered market-data browser. A frozen local capture (2026-04-20) lives at `reference/aemo-catalog/` — see that directory's `FETCH-MANIFEST.md` for provenance.

**Structure of AEMO's catalog:**

- `datasets/dataset-list.yaml` — master list, 97 `!file` entries grouped under 15 top-level `!dataset` categories (Bids, Data Model, Demand and Forecasts, Dispatch, FPP, Gas Supply Hub, NEMDE, Network, Other, PASA, Pre-Dispatch, Prices, Settlement Residues, Settlements, Trading).
- `manifests/<slug>.yaml` — per-dataset URL manifests (CURRENT + ARCHIVE pairs for Reports datasets; monthly partition lists for MMSDM and NEMDE).
- `datasets/<slug>-definition.yaml` — per-dataset field-level schema with DB types (e.g. `NUMBER(15,5)`, `VARCHAR2(20)`). Machine-readable.

**Role in this project: supplementary metadata, not structural authority.** The AEMO catalog's coverage is incomplete across every subtree on NEMWeb:

| Subtree | Mirror (authoritative) | AEMO catalog covers | Gap |
|---|---|---|---|
| `/Reports/CURRENT/` | 103 dirs | 70 dirs (+ 4 with casing-broken URLs that would 404 on strict case-sensitive serving) | ~37 mirror dirs uncovered — includes load-bearing datasets like `GBB`, `MCCDispatch`, `STTM`, `ECGS`, `Market_Notice`, `Causer_Pays*`, `CDEII`, `SupplyDemand`, `Weekly_Bulletin`, `Yesterdays_Bids_Reports` |
| `/Reports/ARCHIVE/` | 68 dirs | **56 unique dirs** via catalog URLs (+ 6 with casing-broken URLs); catalog datasets often share an ARCHIVE dir so the "77 ARCHIVE URL claims" I noted earlier collapse to 56 unique URL paths | **12 mirror ARCHIVE dirs uncovered** — `Bidmove_Summary`, `CDEII`, `DispatchIS_FCAS_Fix`, `GBB`, `HistDemand`, `Market_Notice`, `Next_Day_Offer_Energy`, `NEXT_DAY_OFFER_ENERGY)SPARSE`, `Next_Day_Offer_FCAS`, `Weekly_Bulletin`, `Yesterdays_Bids_Reports`, `Yesterdays_MNSPBids_Reports`. **11 of these 12 are empty listings** (only `HistDemand` has real content, 12 zip files). See §3.3. |
| `/Data_Archive/.../MMSDM/` months | 135 months (2009-07 onwards on mirror) | 135 manifest URLs **2015-01 onwards only** | Catalog is internally inconsistent: the `monthList` field in `mms-data-model-definition.yaml` claims **201 months** (200907 → 202603) but the companion `mms-data-model.yaml` manifest only lists URLs for 135 (2015-01 → 2026-03). 66 months have no URL pointer despite being acknowledged. Mirror did not walk the 2009-2014 dirs (only listed the year-level index), so the mirror's 135-month figure may itself underrepresent AEMO's actual archive. |
| `/Data_Archive/.../MMSDM/{month}/...` | ~9 views per month (11 in total union) | `url:` points only at `DATA/` (and `urlZip:` at the month-level bulk zip) | ~89% of per-month content invisible: `BCP_DATA`, `BCP_FMT`, `CTL`, `DOCUMENTATION`, `INDEX`, `P5MIN_ALL_DATA`, `PREDISP_ALL_DATA`, `UTILITIES`, sometimes `LOGS`/`MYSQL` all elided. The 2024-08 filename-format transition (§3.5) is completely invisible from the catalog. |
| `/Data_Archive/.../MMSDM/MTPASA_DATA_EXPORT/` | 7 files, frozen 2019-10 | Absent | 100% gap |
| `/Data_Archive/.../NEMDE/{month}/NEMDE_Market_Data/` | `NEMDE_Files/` (month-varying) + `File_Readers/` (static, identical across all months) | `NEMDE_Files/` only | 100% of `File_Readers/` content uncovered. Since `File_Readers/` is static (§2.3), this gap is tolerable — one canonical asset rather than per-month data. |
| `/Data_Archive/.../FCAS_Causer_Pays/` | 2011, 2012 txt files | Absent | 100% gap |
| `/Reports/CURRENT/*/DUPLICATE/` | 18 subtrees (652 files total; 617 in `GBB/DUPLICATE/`) | Absent | 100% gap — catalog silent on every `DUPLICATE/`. The single-file `_LEGACY.zip` placeholders (2 cases) can safely be skipped; the remaining 15 class-(b) non-LEGACY straggler dirs and especially `GBB/DUPLICATE/` carry real data (§2.1.1). |
| `/Reports/CURRENT/MMSDataModelReport/PDRCONFIG/` | 2 PDR config bundles (preprod + prod) | Absent | 100% gap |

**Catalog URLs with casing mismatched from the mirror** (will 404 after AEMO's stated 2026-04-21 case-sensitivity enforcement):

- CURRENT tier (4): `DispatchIS_Price_Revisions`, `MCCDISPATCH`, `NEXT_DAY_ACTUAL_GEN`, `NEXT_DAY_INTERMITTENT_GEN_SCADA`.
- ARCHIVE tier (6): `DISPATCH_NEGATIVE_RESIDUE`, `MCCDISPATCH`, `NEXT_DAY_ACTUAL_GEN`, `NEXT_DAY_INTERMITTENT_GEN_SCADA`, `PDPASA_DUIDAvailability`, `STPASA_DUIDAvailability`.

All 10 URLs currently return HTTP 200 because nemweb.com.au serves case-insensitively today, but will break the day strict casing flips on.

**How this project uses the AEMO catalog:**

1. **Metadata enrichment** for the 70 Reports datasets it covers — kebab-case canonical slug, AEMO's 15-group taxonomy, field-level schema, ARCHIVE-availability signal.
2. **Cross-validation** — extractor-emitted URL patterns in the overlap region must resolve to the same URLs AEMO publishes. Disagreements indicate a bug somewhere; triage case-by-case.
3. **Catalog-bug detection** — our mirror walk surfaces AEMO's own catalog casing errors + internal inconsistencies. Useful for a public "AEMO catalog audit" artifact.
4. **Weekly change feed (overlap region)** — re-fetch `reference/aemo-catalog/` weekly; diff against previous snapshot to detect AEMO adding / removing / renaming covered datasets.

**How this project does NOT use the AEMO catalog:**

- NOT as a replacement for the mirror walk. The catalog undercovers the mirror on every axis.
- NOT as dispositive on DUPLICATE / legacy / undocumented subtrees. Catalog silence means AEMO's UI browser doesn't surface them; it does not mean they are invalid or should be excluded (e.g. GBB/DUPLICATE's 617-file operational tree).
- NOT for MMSDM per-month view enumeration. The catalog only points at `DATA/`; the other 8-10 views are mirror-walk-only.
