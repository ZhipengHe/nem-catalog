# MMSDM DATA/ Table Lifecycle

Full lifecycle classification of every `<TABLE>` identifier observed under `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{month}/MMSDM_Historical_Data_SQLLoader/DATA/` across 135 months (2015-01 to 2026-03). Companion to `reference/NEMWEB-STRUCTURE.md` §2.2 and §3.5.

**Data source:** 135 DATA/ listing files captured in `nemweb-mirror/` on 2026-04-19/20. Filenames parsed with dual-format regex (`PUBLIC_DVD_<TABLE>_<timestamp>.zip` for DVD-era, `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<timestamp>.zip` for ARCHIVE-era). `<TABLE>` extraction validates 278 distinct identifiers.

**Per-table machine-readable detail:** `reference/MMSDM-TABLE-LIFECYCLE.csv` (278 rows).

**Cross-references to AEMO-published docs:**

- **Version timeline:** `reference/NEMWEB-STRUCTURE.md` §2.2.1 maps each of the 13 MMSDM schema versions (v4.26 → v5.6) to its first-seen month on the mirror.
- **Per-version Upgrade Reports + DDL + Release Notes:** captured to `reference/aemo-mmsdm-docs/` (gitignored, regeneratable; see that directory's `INVENTORY.md`). Each version's Upgrade Report PDF is AEMO's authoritative table-level change log vs prior version; `MMSDM_create_v{X.Y}.zip` and `MMSDM_upgrade_v{X.Y}.zip` carry the actual DDL.
- **Cross-boundary MMSDM ↔ Reports identity:** `reference/aemo-mmsdm-docs/{v4.26→v5.1}/table-file-report-mapping.csv` (7 versions, 336–392 rows each) — AEMO's own `Table to File to Report Relationships.xlsx` extracted to CSV. AEMO stopped publishing this after v5.1.

**Scope limit:** only the `DATA/` view. `BCP_DATA/`, `BCP_FMT/`, `CTL/`, `MYSQL/`, `PREDISP_ALL_DATA/`, `P5MIN_ALL_DATA/` may carry additional tables not captured here — spot-checks suggest the table sets mostly overlap with `DATA/` but this has not been verified exhaustively. Pre-2015 months exist on the mirror at the year level but were not walked to listing-level; any tables that existed before 2015-01 and were retired before 2015-01 are invisible to this analysis.

---

## 1. Lifecycle class distribution

Every table falls into exactly one of 7 classes:

| Class | Count | Definition |
|---|---:|---|
| **ALWAYS_PRESENT** | 90 | Present every month 2015-01 → 2026-03. The stable MMSDM core. |
| **ADDED_AT_CUTOVER** | 70 | First appearance exactly at MMSDM_2024_08 (the platform-transition cutover); contiguous thereafter. |
| **INTERMITTENT** | 46 | Present for at least one month but with gaps within its lifetime. Either event-driven or has 1-month data gaps. |
| **ADDED_IN_ARCHIVE_ERA** | 32 | First appearance after 2024-08 (post-cutover); still present in latest month. |
| **RETIRED_AT_CUTOVER** | 19 | Last appearance MMSDM_2024_07 (last DVD-era month); gone 2024-08+. |
| **ADDED_LATE_STILL_LIVE** | 13 | First appearance after 2015-01 but before 2024-08; contiguous through present. |
| **RETIRED_EARLY** | 8 | Contiguous presence, last appearance before 2024-07. |
| **BOUNDED_CONTIGUOUS** | 0 | First>2015-01 AND last<2026-03 AND contiguous. Empty class in current data. |
| **TOTAL** | **278** | |

## 2. ALWAYS_PRESENT — the stable core (90 tables)

These 90 tables have appeared in every one of the 135 months 2015-01 to 2026-03. They are the functional definition of "what MMSDM is." Any consumer should expect these to be present month-over-month without exception.

<details><summary>Full list (alphabetical)</summary>

`ANCILLARY_RECOVERY_SPLIT` · `BIDDAYOFFER` · `BIDDUIDDETAILS`  
`BIDDUIDDETAILSTRK` · `BIDTYPES` · `BIDTYPESTRK`  
`BILLINGCALENDAR` · `BILLINGDAYTRK` · `BILLINGRUNTRK`  
`DISPATCHABLEUNIT` · `DISPATCHCASESOLUTION` · `DISPATCHCONSTRAINT`  
`DISPATCHINTERCONNECTORRES` · `DISPATCHLOAD` · `DISPATCHOFFERTRK`  
`DISPATCHPRICE` · `DISPATCHREGIONSUM` · `DISPATCH_MNSPBIDTRK`  
`DISPATCH_UNIT_SCADA` · `DUDETAIL` · `DUDETAILSUMMARY`  
`EMSMASTER` · `GENCONDATA` · `GENCONSET`  
`GENCONSETINVOKE` · `GENCONSETTRK` · `GENERICCONSTRAINTRHS`  
`GENUNITS` · `GST_BAS_CLASS` · `GST_RATE`  
`GST_TRANSACTION_CLASS` · `GST_TRANSACTION_TYPE` · `INSTRUCTIONSUBTYPE`  
`INSTRUCTIONTYPE` · `INTERCONNECTOR` · `INTERCONNECTORCONSTRAINT`  
`IRFMAMOUNT` · `IRFMEVENTS` · `LOSSFACTORMODEL`  
`LOSSMODEL` · `MARKETFEE` · `MARKETFEEDATA`  
`MARKETFEETRK` · `MARKETNOTICETYPE` · `MARKETSUSPENSION`  
`MARKETSUSREGION` · `MARKET_PRICE_THRESHOLDS` · `MCC_CASESOLUTION`  
`MCC_CONSTRAINTSOLUTION` · `MNSP_INTERCONNECTOR` · `MNSP_PARTICIPANT`  
`MTPASA_RESERVELIMIT` · `MTPASA_RESERVELIMIT_REGION` · `MTPASA_RESERVELIMIT_SET`  
`OVERRIDERRP` · `P5MIN_CASESOLUTION` · `P5MIN_INTERCONNECTORSOLN`  
`P5MIN_REGIONSOLUTION` · `PARTICIPANT` · `PARTICIPANTCATEGORY`  
`PARTICIPANTCATEGORYALLOC` · `PARTICIPANTCLASS` · `PDPASA_CASESOLUTION`  
`PDPASA_REGIONSOLUTION` · `PERDEMAND` · `PREDISPATCHCASESOLUTION`  
`PREDISPATCHOFFERTRK` · `PREDISPATCHSCENARIODEMAND` · `PREDISPATCHSCENARIODEMANDTRK`  
`PREDISPATCH_MNSPBIDTRK` · `REGION` · `REGIONAPC`  
`REGIONAPCINTERVALS` · `REGIONSTANDINGDATA` · `RESDEMANDTRK`  
`SETCFG_PARTICIPANT_MPF` · `SETCFG_PARTICIPANT_MPFTRK` · `SPDCONNECTIONPOINTCONSTRAINT`  
`SPDINTERCONNECTORCONSTRAINT` · `STADUALLOC` · `STATION`  
`STATIONOPERATINGSTATUS` · `STATIONOWNER` · `STATIONOWNERTRK`  
`STPASA_CASESOLUTION` · `STPASA_CONSTRAINTSOLUTION` · `STPASA_INTERCONNECTORSOLN`  
`STPASA_REGIONSOLUTION` · `TRADINGINTERCONNECT` · `TRADINGPRICE`  

</details>

## 3. Retirements

### 3.1 RETIRED_EARLY (8 tables) — disappeared pre-cutover

| Table | First | Last | Months | Likely successor(s) |
|---|---|---|---:|---|
| `INTERCONNMWFLOW` | 2015-01 | 2021-05 | 77 | No direct match. Retired 2021-05; predates 2021-10 five-minute settlement rule. Possibly absorbed into DISPATCHINTERCONNECTORRES (ALWAYS_PRESENT). |
| `MTPASA_CONSTRAINTSOLUTION` | 2015-01 | 2018-05 | 41 | MTPASA_CONSTRAINTRESULT + MTPASA_CONSTRAINTSUMMARY (both first=2018-05, same month) |
| `MTPASA_INTERCONNECTORSOLUTION` | 2015-01 | 2018-05 | 41 | MTPASA_INTERCONNECTORRESULT (first=2018-05, same month) |
| `MTPASA_REGIONSOLUTION` | 2015-01 | 2018-05 | 41 | MTPASA_REGIONRESULT + MTPASA_REGIONSUMMARY + MTPASA_REGIONITERATION (all first=2018-05) |
| `MTPASA_RESERVELIMITSOLUTION` | 2015-01 | 2018-05 | 41 | No direct match — MTPASA_LOLPRESULT (first=2018-05) covers reserve-limit conceptually but naming diverges |
| `PREDISPATCHCONSTRAINT2` | 2018-03 | 2018-03 | 1 | Appears in 2018-03 only (single month). Likely a test / one-off artifact. No pattern match. |
| `TRADINGLOAD` | 2015-01 | 2021-09 | 81 | No direct match. Retired 2021-09, aligns with October 2021 five-minute settlement. Trading-interval (30-min) rollups deprecated; consumers use DISPATCHLOAD (ALWAYS_PRESENT) at 5-min. |
| `TRADINGREGIONSUM` | 2015-01 | 2021-09 | 81 | Same as TRADINGLOAD — retired at 2021 five-minute settlement. DISPATCHREGIONSUM (ALWAYS_PRESENT) covers 5-min. |

**Two distinct retirement waves:**

1. **2018-05 MTPASA redesign** — 4 `*_SOLUTION` tables replaced by a richer schema using `*_RESULT`, `*_SUMMARY`, `*_ITERATION`, `*_LOLPRESULT`. The replacement tables all have `first=2018-05` (classified `ADDED_LATE_STILL_LIVE` — see §5). Clean same-month transition.
2. **2021-05 / 2021-09 five-minute settlement prep** — `INTERCONNMWFLOW`, `TRADINGLOAD`, `TRADINGREGIONSUM` retired ahead of the October 2021 five-minute settlement rule. The underlying data is still available via the 5-min-native `DISPATCH*` tables.

### 3.2 RETIRED_AT_CUTOVER (19 tables) — retired 2024-08 platform transition

All 19 tables have their last month = 2024-07 (last DVD-era month) and do not appear 2024-08+. Three sub-patterns:

**Pattern A: `_D` suffix tables dropped** (8 tables) — these had `_D` ("daily"?) suffixes and ran alongside un-suffixed equivalents. At cutover, only the suffixed variant was dropped; the base table continues as ALWAYS_PRESENT.

| Retired | Surviving counterpart |
|---|---|
| `PREDISPATCHCONSTRAINT_D` | `PREDISPATCHCONSTRAINT` |
| `PREDISPATCHLOAD_D` | `PREDISPATCHLOAD` |
| `PREDISPATCHPRICE_D` | `PREDISPATCHPRICE` |
| `PREDISPATCHPRICESENSITIVITIE_D` | `PREDISPATCHPRICESENSITIVITIES` |
| `PREDISPATCHREGIONSUM_D` | `PREDISPATCHREGIONSUM` |
| `PREDISPATCHINTERCONNECTORRES_D` | `PREDISPATCHINTERCONNECTORRES` |
| `PREDISPATCHINTERCONNECTR_SENS_D` | `PREDISPATCHINTERCONNECTORRES (closest; no suffixed equivalent)` |
| `PREDISPATCH_FCAS_REQ_D` | `PREDISPATCH_FCAS_REQ` |

**Pattern B: sharded tables consolidated** (6 tables) — 4 numbered `P5MIN_CONSTRAINTSOLUTION{1-4}` shards merged into a single `P5MIN_CONSTRAINTSOLUTION` (ADDED_AT_CUTOVER). Separately 2 numbered `BIDPEROFFER{1,2}` tables merged into `BIDOFFERPERIOD` (ADDED_AT_CUTOVER, also renamed).

| Retired | Successor |
|---|---|
| `P5MIN_CONSTRAINTSOLUTION1` | `P5MIN_CONSTRAINTSOLUTION (new, 2024-08)` |
| `P5MIN_CONSTRAINTSOLUTION2` | `P5MIN_CONSTRAINTSOLUTION (new, 2024-08)` |
| `P5MIN_CONSTRAINTSOLUTION3` | `P5MIN_CONSTRAINTSOLUTION (new, 2024-08)` |
| `P5MIN_CONSTRAINTSOLUTION4` | `P5MIN_CONSTRAINTSOLUTION (new, 2024-08)` |
| `BIDPEROFFER1` | `BIDOFFERPERIOD (new, 2024-08) — also includes rename` |
| `BIDPEROFFER2` | `BIDOFFERPERIOD (new, 2024-08)` |

**Pattern C: renamed with underscore reformatting** (2 tables) — `P5MINSCENARIODEMAND` and `P5MINSCENARIODEMANDTRK` lost their `P5MIN`-prefix concatenation and gained the underscore: `P5MIN_SCENARIODEMAND`, `P5MIN_SCENARIODEMANDTRK`. Same data, cleaner naming.

**Pattern D: outright removed** (3 tables, no clear successor)

| Retired | Notes |
|---|---|
| `MTPASA_CASESOLUTION` | Remnant of the 2018-05 MTPASA redesign. The `*_RESULT` replacements from 2018 did not include a CASESOLUTION equivalent; this legacy table kept running in parallel for 6 more years. Finally dropped at 2024-08. |
| `MARKETNOTICEDATA` | Retired at cutover. `MARKET_SUSPEND_SCHEDULE` and related tables (ADDED_AT_CUTOVER) cover the market-suspension-notice subspace but naming is different; not a clean rename. |
| `BILLSMELTERRATE` | Retired at cutover with no clear successor. Smelter-rate billing was likely absorbed into general billing tables or deprecated entirely. |

## 4. Late arrivals

### 4.1 ADDED_LATE_STILL_LIVE (13 tables) — entered pre-cutover, still running

| Table | First | Months | Context |
|---|---|---:|---|
| `DUALLOC` | 2020-10 | 66 | 2020-10 — ancillary tracking addition |
| `MTPASA_CASERESULT` | 2018-05 | 95 | 2018-05 MTPASA redesign wave |
| `MTPASA_CONSTRAINTRESULT` | 2018-05 | 95 | 2018-05 MTPASA redesign wave (replaces MTPASA_CONSTRAINTSOLUTION) |
| `MTPASA_CONSTRAINTSUMMARY` | 2018-05 | 95 | 2018-05 MTPASA redesign wave |
| `MTPASA_INTERCONNECTORRESULT` | 2018-05 | 95 | 2018-05 MTPASA redesign wave (replaces MTPASA_INTERCONNECTORSOLUTION) |
| `MTPASA_LOLPRESULT` | 2018-05 | 95 | 2018-05 MTPASA redesign wave (Loss of Load Probability) |
| `MTPASA_REGIONITERATION` | 2018-05 | 95 | 2018-05 MTPASA redesign wave |
| `MTPASA_REGIONRESULT` | 2018-05 | 95 | 2018-05 MTPASA redesign wave (replaces MTPASA_REGIONSOLUTION) |
| `MTPASA_REGIONSUMMARY` | 2018-05 | 95 | 2018-05 MTPASA redesign wave |
| `PDPASA_CONSTRAINTSOLUTION` | 2021-02 | 62 | 2021-02 — PDPASA constraint-solution tracking added |
| `PDPASA_INTERCONNECTORSOLN` | 2021-02 | 62 | 2021-02 — PDPASA interconnector-solution tracking added |
| `ROOFTOP_PV_ACTUAL` | 2016-08 | 116 | 2016-08 rooftop-PV data collection began |
| `ROOFTOP_PV_FORECAST` | 2016-08 | 116 | 2016-08 rooftop-PV data collection began |

**Major entry waves:**

1. **2016-08** — `ROOFTOP_PV_ACTUAL` + `ROOFTOP_PV_FORECAST`. Distributed-PV observability added to the dispatch data model. Both have been continuous for 116 months.
2. **2018-05** — 8 MTPASA replacement tables appear the same month 4 old `*_SOLUTION` variants retired. Single atomic schema migration.
3. **2020-10** — `DUALLOC` (ancillary dual-allocation tracking).
4. **2021-02** — 2 PDPASA tables added (`*_CONSTRAINTSOLUTION`, `*_INTERCONNECTORSOLN`).

### 4.2 ADDED_AT_CUTOVER (70 tables) — brand new at 2024-08

70 tables with their first month exactly equal to 2024-08 (contiguous through present). This is the largest structural change since 2015 — the MMSDM schema expanded by ~41% in one month.

**Observable subsystems** (grouped by naming prefix):

| Prefix | Count | Tables |
|---|---:|---|
| `INTERMITTENT_*` | 7 | `INTERMITTENT_CLUSTER_AVAIL`, `INTERMITTENT_CLUSTER_AVAIL_DAY`, `INTERMITTENT_DS_PRED`, `INTERMITTENT_DS_RUN`, `INTERMITTENT_FORECAST_TRK`, `INTERMITTENT_GEN_LIMIT`, `INTERMITTENT_GEN_LIMIT_DAY` |
| `NETWORK_*` | 7 | `NETWORK_EQUIPMENTDETAIL`, `NETWORK_OUTAGECONSTRAINTSET`, `NETWORK_OUTAGEDETAIL`, `NETWORK_OUTAGESTATUSCODE`, `NETWORK_RATING`, `NETWORK_STATICRATING`, `NETWORK_SUBSTATIONDETAIL` |
| `P5MIN_*` | 6 | `P5MIN_CONSTRAINTSOLUTION`, `P5MIN_INTERSENSITIVITIES`, `P5MIN_LOCAL_PRICE`, `P5MIN_PRICESENSITIVITIES`, `P5MIN_SCENARIODEMAND`, `P5MIN_SCENARIODEMANDTRK` |
| `PD7DAY_*` | 5 | `PD7DAY_CASESOLUTION`, `PD7DAY_CONSTRAINTSOLUTION`, `PD7DAY_INTERCONNECTORSOLUTION`, `PD7DAY_MARKET_SUMMARY`, `PD7DAY_PRICESOLUTION` |
| `MARKET_*` | 4 | `MARKET_SUSPEND_REGIME_SUM`, `MARKET_SUSPEND_REGION_SUM`, `MARKET_SUSPEND_SCHEDULE`, `MARKET_SUSPEND_SCHEDULE_TRK` |
| `MTPASA_*` | 3 | `MTPASA_DUIDAVAILABILITY`, `MTPASA_REGIONAVAILABILITY`, `MTPASA_REGIONAVAIL_TRK` |
| `SETCFG_*` | 3 | `SETCFG_SAPS_SETT_PRICE`, `SETCFG_WDRRR_CALENDAR`, `SETCFG_WDR_REIMBURSE_RATE` |
| `DISPATCH_*` | 2 | `DISPATCH_INTERCONNECTION`, `DISPATCH_LOCAL_PRICE` |
| `FCAS_*` | 2 | `FCAS_REGU_USAGE_FACTORS`, `FCAS_REGU_USAGE_FACTORS_TRK` |
| `PMS_*` | 2 | `PMS_GROUP`, `PMS_GROUPSERVICE` |
| `PREDISPATCH_*` | 2 | `PREDISPATCH_FCAS_REQ`, `PREDISPATCH_LOCAL_PRICE` |
| `SET_*` | 2 | `SET_ENERGY_REGION_SUMMARY`, `SET_NMAS_RECOVERY_RBF` |
| `SRA_*` | 2 | `SRA_FINANCIAL_RUNTRK`, `SRA_PRUDENTIAL_RUN` |
| `VOLTAGE_*` | 2 | `VOLTAGE_INSTRUCTION`, `VOLTAGE_INSTRUCTION_TRK` |
| (other) | 21 | `ADG_DETAIL`, `AGGREGATE_DISPATCH_GROUP`, `AVERAGEPRICE30`, `BIDOFFERPERIOD`, `BILLING_DIRECTION_RECON_OTHER`, `CONSTRAINTRELAXATION_OCD`, `DEMANDOPERATIONALACTUAL`, `DEMANDOPERATIONALFORECAST`, `GENUNITS_UNIT`, `METERDATA_INTERCONNECTOR`, `MNSP_BIDOFFERPERIOD`, `NEGATIVE_RESIDUE`, `PREDISPATCHCONSTRAINT`, `PREDISPATCHINTERCONNECTORRES`, `PREDISPATCHLOAD`, `PREDISPATCHPRICE`, `PREDISPATCHPRICESENSITIVITIES`, `PREDISPATCHREGIONSUM`, `SECDEPOSIT_INTEREST_RATE`, `SETLOCALAREAENERGY`, `SETLOCALAREATNI` |

**Thematic reading** (not AEMO-documented — inferred from table names):

- **MARKET_SUSPEND_\*** (4 tables): formalizing market-suspension-regime publication. Replaces `MARKETNOTICEDATA` (retired at cutover) with a structured schema.
- **INTERMITTENT_\*** (6 tables): intermittent-generation (wind/solar) tracking at higher granularity. Earlier DVD-era had a few `INTERMITTENT*` fields but not as a schema block.
- **MTPASA_DUIDAVAILABILITY + MTPASA_REGIONAVAILABILITY + MTPASA_REGIONAVAIL_TRK** — make the MTPASA availability data first-class (previously only in the `MTPASA_DATA_EXPORT/` sibling, see NEMWEB-STRUCTURE.md §2.2).
- **PD7DAY_\*** (2+ tables): 7-day pre-dispatch. New product.
- **METERDATA_\*, GENUNITS_\*, BILLING_\***: billing/metering-subsystem surface expansion.
- **VOLTAGE_INSTRUCTION_\***: voltage-instruction tracking added.

### 4.3 ADDED_IN_ARCHIVE_ERA (32 tables) — new after 2024-08

Entry wave at **2024-12**: 20 new tables, dominated by the FPP (Forecast Performance Payment) subsystem.

| Table | First | Notes |
|---|---|---|
| `DISPATCH_FCAS_REQ_CONSTRAINT` | 2024-12 |  |
| `DISPATCH_FCAS_REQ_RUN` | 2024-12 |  |
| `FPP_CONSTRAINT_FREQ_MEASURE` | 2024-12 | FPP subsystem |
| `FPP_CONTRIBUTION_FACTOR` | 2024-12 | FPP subsystem |
| `FPP_EST_PERF_COST_RATE` | 2024-12 | FPP subsystem |
| `FPP_EST_RESIDUAL_COST_RATE` | 2024-12 | FPP subsystem |
| `FPP_FCAS_SUMMARY` | 2024-12 | FPP subsystem |
| `FPP_FORECAST_DEFAULT_CF` | 2024-12 | FPP subsystem |
| `FPP_FORECAST_RESIDUAL_DCF` | 2024-12 | FPP subsystem |
| `FPP_HIST_PERFORMANCE` | 2024-12 | FPP subsystem |
| `FPP_HIST_REGION_PERFORMANCE` | 2025-04 | FPP subsystem |
| `FPP_P5_FWD_EST_RESIDUALRATE` | 2025-01 | FPP subsystem |
| `FPP_PD_FWD_EST_RESIDUALRATE` | 2025-01 | FPP subsystem |
| `FPP_PERFORMANCE` | 2024-12 | FPP subsystem |
| `FPP_RCR` | 2024-12 | FPP subsystem |
| `FPP_REGION_FREQ_MEASURE` | 2024-12 | FPP subsystem |
| `FPP_RESIDUAL_CF` | 2024-12 | FPP subsystem |
| `FPP_RESIDUAL_PERFORMANCE` | 2024-12 | FPP subsystem |
| `FPP_RUN` | 2024-12 | FPP subsystem |
| `FPP_UNIT_MW` | 2024-12 | FPP subsystem |
| `FPP_USAGE` | 2024-12 | FPP subsystem |
| `INTERMITTENT_GEN_SCADA` | 2024-12 |  |
| `P5MIN_FCAS_REQ_CONSTRAINT` | 2024-12 |  |
| `P5MIN_FCAS_REQ_RUN` | 2024-12 |  |
| `PDPASA_DUIDAVAILABILITY` | 2025-07 |  |
| `PD_FCAS_REQ_CONSTRAINT` | 2024-12 |  |
| `PD_FCAS_REQ_RUN` | 2024-12 |  |
| `SET_FCAS_CLAWBACK_REQ` | 2026-01 |  |
| `SET_FCAS_CLAWBACK_RUN_TRK` | 2026-01 |  |
| `SSM_ENABLEMENT_COSTS` | 2025-11 |  |
| `SSM_ENABLEMENT_PERIOD` | 2025-11 |  |
| `STPASA_DUIDAVAILABILITY` | 2025-07 |  |

**Key events:**

- **2024-12**: FPP subsystem goes live — 17 `FPP_*` tables appear simultaneously. Matches the AEMO-published FPP ruleset taking effect.
- **2024-09 to 2024-10**: Minor additions (DISPATCHBLOCKEDCONSTRAINT, P5MIN_BLOCKEDCONSTRAINT, BILLING_NMAS_TST_RECVRY_*).
- **2025-04 to 2026-01**: Further incremental additions (FPP_P5_FWD_EST_RESIDUALRATE, SET_FCAS_CLAWBACK_*, etc.).
- **2025-07**: `PDPASA_DUIDAVAILABILITY` + `STPASA_DUIDAVAILABILITY` enter MMSDM (these names already exist in `Reports/` under different casing — see NEMWEB-STRUCTURE.md §3.1).
- **2025-11**: `SSM_ENABLEMENT_COSTS` + `SSM_ENABLEMENT_PERIOD` added — System Security Mechanism enablement data.

## 5. INTERMITTENT tables (46)

Tables with at least one gap-month inside their lifetime. Three sub-patterns:

### 5.1 Single-gap tables (16 tables, 1-gap-month each)

Present continuously except for **one** specific missing month. Likely reflects 1-month data outages on AEMO's side, not schema changes. The missing month is consistent across most of these — the common pattern is one month's data never made it into the archive (e.g. a data-pipeline incident). Consumers should expect these tables to be reliable everywhere except the one anomaly month.

**Tables:** `BIDPEROFFER`, `BILLINGREGIONEXPORTS`, `BILLINGREGIONFIGURES`, `BILLINGREGIONIMPORTS`, `BILLING_CO2E_PUBLICATION`, `BILLING_CO2E_PUBLICATION_TRK`, `DAYTRACK`, `DISPATCH_FCAS_REQ`, `MNSP_DAYOFFER`, `MNSP_OFFERTRK`, `MNSP_PEROFFER`, `P5MIN_UNITSOLUTION`, `SETCPDATAREGION`, `SETFCASREGIONRECOVERY`, `SETGENDATAREGION`, `SETINTRAREGIONRESIDUES`, `SETIRSURPLUS`, `SET_ANCILLARY_SUMMARY`, `SET_FCAS_REGULATION_TRK`

### 5.2 Event-driven tables (many gap-months)

Tables that only appear in months when specific events occur (auctions, residue settlements, price-revision events, etc.). Intermittent by design — gaps are not bugs, they're "no events this month."

| Table | First | Last | Present | Gap months | Likely trigger |
|---|---|---|---:|---:|---|
| `DISPATCH_PRICE_REVISION` | 2015-02 | 2026-03 | 28 | 106 | Price-revision events |
| `GDINSTRUCT` | 2015-01 | 2026-03 | 35 | 100 | GD instruction events |
| `APEVENT` | 2015-10 | 2026-03 | 33 | 93 | Administered-pricing events |
| `APEVENTREGION` | 2015-10 | 2026-03 | 33 | 93 | Administered-pricing events |
| `AUCTION_TRANCHE` | 2015-01 | 2026-03 | 48 | 87 | Auction events |
| `RESIDUE_CON_FUNDS` | 2015-05 | 2026-01 | 45 | 84 | Residue settlement events |
| `RESIDUE_PRICE_FUNDS_BID` | 2015-03 | 2026-03 | 49 | 84 | Residue auction events |
| `RESIDUE_PUBLIC_DATA` | 2015-03 | 2026-03 | 53 | 80 | Residue settlement events |
| `RESIDUE_TRK` | 2015-03 | 2026-03 | 54 | 79 | Residue settlement events |
| `AUCTION_CALENDAR` | 2015-01 | 2026-03 | 60 | 75 | Auction scheduling |
| `AUCTION_IC_ALLOCATIONS` | 2015-01 | 2026-03 | 92 | 43 | Auction events |
| `AUCTION` | 2015-03 | 2026-03 | 92 | 41 | Auction events |
| `BIDDAYOFFER_D` | 2015-01 | 2026-03 | 94 | 41 | Daily bid-offer events (DVD-era _D variant) |
| `BIDPEROFFER_D` | 2015-01 | 2026-03 | 94 | 41 | Daily bid-per-offer events (DVD-era _D variant) |
| `RESIDUE_CONTRACTS` | 2015-03 | 2026-03 | 92 | 41 | Residue settlement events |
| `PRUDENTIALRUNTRK` | 2015-01 | 2026-03 | 97 | 38 | Prudential-run events |
| `SPDREGIONCONSTRAINT` | 2015-01 | 2026-03 | 98 | 37 | SPD solver region constraints |
| `RESERVE` | 2015-01 | 2018-05 | 27 | 14 | Reserve-contract events (retired 2018-05) |
| `DISPATCH_CONSTRAINT_FCAS_OCD` | 2024-10 | 2026-02 | 5 | 12 |  |
| `GENERICEQUATIONDESC` | 2015-01 | 2026-03 | 125 | 10 | Generic-constraint updates |
| `DISPATCHBLOCKEDCONSTRAINT` | 2024-09 | 2026-03 | 11 | 8 |  |
| `P5MIN_BLOCKEDCONSTRAINT` | 2024-09 | 2026-03 | 11 | 8 |  |
| `GENERICEQUATIONRHS` | 2015-01 | 2026-03 | 129 | 6 | Generic-constraint updates |

### 5.3 Cutover-adjacent tables (appeared shortly before / after 2024-08 with gaps)

A handful of tables first appeared around the 2024-08 platform transition and have subsequent gaps — likely teething issues with the new pipeline. Not event-driven.

- `BILLING_NMAS_TST_RECVRY_RBF` — first=2024-10, last=2026-03, present=14, gap_months=4
- `BILLING_NMAS_TST_RECVRY_TRK` — first=2024-12, last=2026-03, present=11, gap_months=5
- `DISPATCHBLOCKEDCONSTRAINT` — first=2024-09, last=2026-03, present=11, gap_months=8
- `DISPATCH_CONSTRAINT_FCAS_OCD` — first=2024-10, last=2026-02, present=5, gap_months=12
- `P5MIN_BLOCKEDCONSTRAINT` — first=2024-09, last=2026-03, present=11, gap_months=8
- `PREDISPATCHBLOCKEDCONSTRAINT` — first=2025-02, last=2026-02, present=9, gap_months=4

## 6. Rename / consolidation summary — verified

Original lexical/temporal hypotheses have now been verified against AEMO-shipped DDL bundles + Upgrade Report PDFs by `scripts/synthesize_mmsdm_timeline.py`. Full evidence per row in `reference/MMSDM-RENAMES-VERIFICATION.md`. Re-running:

```bash
python3 scripts/synthesize_mmsdm_timeline.py \
    --columns reference/MMSDM-DDL-COLUMNS.csv \
    --renames reference/MMSDM-DDL-RENAMES.csv \
    --upgrade reference/MMSDM-UPGRADE-TABLES.csv \
    --lifecycle reference/MMSDM-TABLE-LIFECYCLE.csv \
    --timeline-out reference/MMSDM-TABLE-TIMELINE.csv \
    --report-out reference/MMSDM-RENAMES-VERIFICATION.md
```

### 6.1 The "rename" framing was wrong — three distinct phenomena

The verification surfaced that what the lexical analysis grouped as "renames" actually splits into three distinct AEMO behaviours, only one of which is a rename in the strict DDL sense:

- **CONFIRMED** — AEMO shipped explicit `EXEC sp_rename` SQL renaming the table in the live DDL. 1 of 12 hypotheses.
- **DATA-FLOW-REPLACEMENT** — AEMO keeps both the predecessor and the successor table definitions in the schema indefinitely (the predecessor is never dropped from `MMSDM_create_v*.sql`), but stops publishing data files for the predecessor at the transition month and starts publishing under the successor name. The DDL coexistence makes this look like NOT a rename, but the mirror data flow says otherwise. 7 of 12 hypotheses.
- **PRE-DDL-CAPTURED** — the predecessor was renamed/dropped from DDL before our v5.2 capture window opened (May 2023). The DDL only knows the successor; the predecessor is visible only in the older mirror data. Mirror lifecycle confirms the data-side transition. 4 of 12 hypotheses.

Practical implication for downstream consumers: **consulting only the latest DDL is insufficient to detect predecessor names**. A consumer parsing v5.6 `create_mms_data_model.sql` would never see `TRADINGLOAD`, `MTPASA_CONSTRAINTSOLUTION`, `INTERCONNMWFLOW`, etc. as "old" — they are still defined, just no longer fed.

### 6.2 Per-hypothesis verdict

| ID | Successor(s) | Predecessor(s) | Transition | Verdict |
|---|---|---|---:|---|
| H1 | `BIDOFFERPERIOD` | `BIDPEROFFER1 + BIDPEROFFER2` | 2024-08 | **CONFIRMED** — sp_rename in v5.3, AEMO migration kit in v5.3_PreRelease |
| H2 | `MTPASA_CONSTRAINTRESULT + MTPASA_CONSTRAINTSUMMARY` | `MTPASA_CONSTRAINTSOLUTION` | 2018-05 | **DATA-FLOW-REPLACEMENT** |
| H3 | `MTPASA_INTERCONNECTORRESULT` | `MTPASA_INTERCONNECTORSOLUTION` | 2018-05 | **DATA-FLOW-REPLACEMENT** |
| H4 | `MTPASA_REGIONRESULT + MTPASA_REGIONSUMMARY + MTPASA_REGIONITERATION` | `MTPASA_REGIONSOLUTION` | 2018-05 | **DATA-FLOW-REPLACEMENT** |
| H5 | `MTPASA_LOLPRESULT` | `MTPASA_RESERVELIMITSOLUTION` | 2018-05 | **DATA-FLOW-REPLACEMENT** |
| H6 | `P5MIN_CONSTRAINTSOLUTION (unified)` | `P5MIN_CONSTRAINTSOLUTION{1,2,3,4}` | 2024-08 | **PRE-DDL-CAPTURED** — numbered variants absent in all v5.2+ DDL |
| H7 | `P5MIN_SCENARIODEMAND` | `P5MINSCENARIODEMAND` | 2024-08 | **PRE-DDL-CAPTURED** — no-underscore form absent in all v5.2+ DDL |
| H8 | `P5MIN_SCENARIODEMANDTRK` | `P5MINSCENARIODEMANDTRK` | 2024-08 | **PRE-DDL-CAPTURED** |
| H9 | base `PREDISPATCH*` (8 tables) | 8 `PREDISPATCH*_D` siblings | 2024-08 | **PRE-DDL-CAPTURED** — `_D` variants absent in all v5.2+ DDL; the base tables existed throughout |
| H10 | `DISPATCHLOAD / DISPATCHREGIONSUM` (5-min) | `TRADINGLOAD / TRADINGREGIONSUM` (30-min) | 2021-09 | **DATA-FLOW-REPLACEMENT** — both schemas still in v5.6 DDL; mirror stops TRADINGLOAD at 202109 |
| H11 | `DISPATCHINTERCONNECTORRES` | `INTERCONNMWFLOW` | 2021-05 | **DATA-FLOW-REPLACEMENT** — both still in v5.6 DDL; mirror stops INTERCONNMWFLOW at 202105 |
| H12 | `MARKET_SUSPEND_*` (4 tables) | `MARKETNOTICEDATA` | 2024-08 | **DATA-FLOW-REPLACEMENT** by lifecycle alignment, but stated note still applies — likely orthogonal replacement (different capability) rather than direct rename |

### 6.3 Renames discovered in DDL but not in the original hypothesis list

Surfaced by the same verification pipeline:

| Version | Scope | Target table | Old → New |
|---|---|---|---|
| v5.5 | column | `FPP_FCAS_SUMMARY` | `USAGE` → `USAGE_VALUE` |
| v5.5 | column | `FPP_USAGE` | `USAGE` → `USAGE_VALUE` |

Both are AEMO-shipped via `EXEC sp_rename ... 'COLUMN'` in `MMSDM_upgrade_5.5.zip → SQLServer/5.5/alter_mms_data_model.sql`. Same renaming pattern (`USAGE` → `USAGE_VALUE`) applied to two different FPP tables in the same release.

### 6.4 What this means for the catalog

For any consumer of `nem-catalog` who needs to map NEMWEB filenames over time to a current schema:

- **Rename hypothesis files (6.2 H6-H9)** — must include explicit pre-v5.2 → post-v5.2 rename mapping in catalog metadata, since DDL alone misses these.
- **Data-flow-replacement files (6.2 H2-H5, H10-H12)** — both names remain valid identifiers; consumer code should treat them as paired streams with a switch-month, not as a strict rename.
- **CONFIRMED renames (6.2 H1)** — direct DDL rename; treat predecessor as a hard-deprecated alias.

## 7. Open questions and limitations

1. **`DATA/` view only** — this analysis did not audit `BCP_DATA/`, `BCP_FMT/`, `CTL/`, `MYSQL/`, `PREDISP_ALL_DATA/`, `P5MIN_ALL_DATA/` for tables not appearing in `DATA/`. Spot-checks suggest the sets heavily overlap but a minority of tables may be view-specific. **Cross-check path:** open `reference/aemo-mmsdm-docs/v5.6/Electricity_Data_Model_Report.pdf` — AEMO's own authoritative table inventory for the current version. Any table listed there but absent from our DATA/ analysis indicates a view-specific table.
2. **Pre-2015 coverage gap** — the mirror did not walk any `MMSDM_2009_*` through `MMSDM_2014_*` month. 66 months of pre-2015 data are listed in AEMO's own catalog (`reference/aemo-catalog/datasets/mms-data-model-definition.yaml`'s `monthList` field) but not captured here. Tables present only before 2015-01 are invisible to this analysis. **Mitigation:** `reference/aemo-mmsdm-docs/v4.26/MMS_Data_Model_Upgrade_Report.pdf` is the earliest captured upgrade report (covers transition INTO v4.26 from v4.25) — reading its "removed tables" section gives pre-2015 table names we'd never see otherwise.
3. **Rename confirmation** — done as of 2026-04-20 (see §6 for verdicts and `reference/MMSDM-RENAMES-VERIFICATION.md` for full evidence). All 12 original hypotheses verified against captured DDL + Upgrade Report PDFs; 1 CONFIRMED, 7 reclassified as DATA-FLOW-REPLACEMENT, 4 as PRE-DDL-CAPTURED. Two additional renames (FPP_FCAS_SUMMARY/FPP_USAGE column rename in v5.5) discovered and folded back into §6.3.
4. **INTERMITTENT tables need content inspection** — the "1-gap anomaly" tables (§5.1) all share what appears to be a single month outage. Identifying that month (likely all the same) would confirm a single upstream incident rather than independent gaps per table.
5. **ADDED_AT_CUTOVER "70 new tables" vs AEMO's documented schema** — how many of these 70 were truly new versus renames from pre-existing DVD-era tables not surfaced by the lexical-similarity search? **Now doable:** `reference/aemo-mmsdm-docs/v5.3/EMMS_Technical_Specification_-_Data_Model_v5.3_-_April_2024_markedup.pdf` is AEMO's own marked-up diff PDF for the v5.2 → v5.3 transition (which spans the 2024-08 cutover).

---

## Appendix: methodology

1. Walk every `MMSDM_{year}_{month}/MMSDM_Historical_Data_SQLLoader/DATA/index.html` file on disk (135 total).
2. Parse filenames matching either regex:
   - DVD-era: `PUBLIC_DVD_<TABLE>_<yyyymmddHHMMSS>.zip`
   - ARCHIVE-era: `PUBLIC_ARCHIVE#<TABLE>#FILE<NN>#<yyyymmddHHMMSS>.zip`
3. Extract `<TABLE>` identifier; record the month it was observed in.
4. Classify each table into one of 8 lifecycle classes based on first/last month + contiguity.
5. For retired tables, search ±24 months for successors with ≥0.5 string similarity or shared token prefixes.

Machine-readable output: `reference/MMSDM-TABLE-LIFECYCLE.csv` (278 rows).