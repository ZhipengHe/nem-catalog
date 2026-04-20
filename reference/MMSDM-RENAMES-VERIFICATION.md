# MMSDM Table Renames — Verification Report

_Generated 2026-04-20 by `scripts/synthesize_mmsdm_timeline.py`._

Verifies the rename hypotheses in `MMSDM-TABLE-LIFECYCLE.md §6` against AEMO-shipped DDL (`MMSDM-DDL-RENAMES.csv`, `MMSDM-DDL-COLUMNS.csv`), Upgrade Report change-lists (`MMSDM-UPGRADE-TABLES.csv`), and the existing mirror-walk lifecycle (`MMSDM-TABLE-LIFECYCLE.csv`).

## 1. Coverage

| Source | Coverage |
|---|---|
| DDL CREATE TABLE | 5 versions: v5.2, v5.3, v5.4, v5.5, v5.6 |
| Upgrade Report change-lists | 12 versions |
| sp_rename calls | 22 total (6 table, 2 column, 14 object/index/constraint) |

## 2. Verdict summary

| ID | Successor(s) | Predecessor(s) | Stated | Verdict |
|---|---|---|---|---|
| H1-BIDOFFERPERIOD | `BIDOFFERPERIOD` | `BIDPEROFFER1`, `BIDPEROFFER2` | AEMO-CONFIRMED | **CONFIRMED** |
| H2-MTPASA_CONSTRAINT | `MTPASA_CONSTRAINTRESULT`, `MTPASA_CONSTRAINTSUMMARY` | `MTPASA_CONSTRAINTSOLUTION` | HIGH | **DATA-FLOW-REPLACEMENT** |
| H3-MTPASA_INTERCONNECTOR | `MTPASA_INTERCONNECTORRESULT` | `MTPASA_INTERCONNECTORSOLUTION` | HIGH | **DATA-FLOW-REPLACEMENT** |
| H4-MTPASA_REGION | `MTPASA_REGIONRESULT`, `MTPASA_REGIONSUMMARY`, `MTPASA_REGIONITERATION` | `MTPASA_REGIONSOLUTION` | HIGH | **DATA-FLOW-REPLACEMENT** |
| H5-MTPASA_LOLP | `MTPASA_LOLPRESULT` | `MTPASA_RESERVELIMITSOLUTION` | MEDIUM | **DATA-FLOW-REPLACEMENT** |
| H6-P5MIN_CONSTRAINTSOLUTION | `P5MIN_CONSTRAINTSOLUTION` | `P5MIN_CONSTRAINTSOLUTION1`, `P5MIN_CONSTRAINTSOLUTION2`, `P5MIN_CONSTRAINTSOLUTION3`, `P5MIN_CONSTRAINTSOLUTION4` | HIGH | **PRE-DDL-CAPTURED** |
| H7-P5MIN_SCENARIODEMAND | `P5MIN_SCENARIODEMAND` | `P5MINSCENARIODEMAND` | VERY HIGH | **PRE-DDL-CAPTURED** |
| H8-P5MIN_SCENARIODEMANDTRK | `P5MIN_SCENARIODEMANDTRK` | `P5MINSCENARIODEMANDTRK` | VERY HIGH | **PRE-DDL-CAPTURED** |
| H9-PREDISPATCH-D-DROP | `PREDISPATCHCONSTRAINT`, `PREDISPATCHINTERCONNECTORRES`, `PREDISPATCHLOAD`, `PREDISPATCHPRICE`, `PREDISPATCHPRICESENSITIVITIES`, `PREDISPATCHREGIONSUM`, `PREDISPATCHSCENARIODEMAND`, `PREDISPATCHSCENARIODEMANDTRK` | `PREDISPATCHCONSTRAINT_D`, `PREDISPATCHINTERCONNECTORRES_D`, `PREDISPATCHLOAD_D`, `PREDISPATCHPRICE_D`, `PREDISPATCHPRICESENSITIVITIES_D`, `PREDISPATCHREGIONSUM_D`, `PREDISPATCHSCENARIODEMAND_D`, `PREDISPATCHSCENARIODEMANDTRK_D` | MEDIUM | **PRE-DDL-CAPTURED** |
| H10-DISPATCHLOAD-VS-TRADINGLOAD | `DISPATCHLOAD`, `DISPATCHREGIONSUM` | `TRADINGLOAD`, `TRADINGREGIONSUM` | HIGH | **DATA-FLOW-REPLACEMENT** |
| H11-DISPATCHINTERCONNECTORRES | `DISPATCHINTERCONNECTORRES` | `INTERCONNMWFLOW` | MEDIUM | **DATA-FLOW-REPLACEMENT** |
| H12-MARKET_SUSPEND | `MARKET_SUSPEND_REGIME_SUM`, `MARKET_SUSPEND_REGION_SUM`, `MARKET_SUSPEND_SCHEDULE`, `MARKET_SUSPEND_SCHEDULE_TRK` | `MARKETNOTICEDATA` | LOW | **DATA-FLOW-REPLACEMENT** |

## 3. Detailed verdicts

### H1-BIDOFFERPERIOD

- **Successor(s):** `BIDOFFERPERIOD`
- **Predecessor(s):** `BIDPEROFFER1`, `BIDPEROFFER2`
- **Stated transition month:** 202408
- **Stated confidence:** AEMO-CONFIRMED
- **Stated evidence:** v5.3_PreRelease/MMSDM_Switch_Bidoffer_Table_Names_v1.1.zip
- **Verdict:** **CONFIRMED**
- **Evidence:**
  - sp_rename: `BIDOFFERPERIOD` -> `BIDOFFERPERIOD_PRE53` in v5.3 alter.sql
  - DDL: `BIDPEROFFER1` present in (none — absent in all captured DDL)
  - DDL: `BIDPEROFFER2` present in (none — absent in all captured DDL)
  - DDL: `BIDOFFERPERIOD` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Upgrade report mentions successor: ['v5.0:BIDOFFERPERIOD', 'v5.3:BIDOFFERPERIOD', 'v5.5:BIDOFFERPERIOD']
  - Lifecycle: `BIDOFFERPERIOD` first_month = 202408
  - Lifecycle: `BIDPEROFFER1` last_month = 202407
  - Lifecycle: `BIDPEROFFER2` last_month = 202407

### H2-MTPASA_CONSTRAINT

- **Successor(s):** `MTPASA_CONSTRAINTRESULT`, `MTPASA_CONSTRAINTSUMMARY`
- **Predecessor(s):** `MTPASA_CONSTRAINTSOLUTION`
- **Stated transition month:** 201805
- **Stated confidence:** HIGH
- **Stated evidence:** v4.27 upgrade report (covers 2018 schema changes)
- **Verdict:** **DATA-FLOW-REPLACEMENT**
- **Evidence:**
  - DDL: `MTPASA_CONSTRAINTSOLUTION` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MTPASA_CONSTRAINTRESULT` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MTPASA_CONSTRAINTSUMMARY` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Both DDL-coexist in v5.6, but mirror lifecycle shows MTPASA_CONSTRAINTSOLUTION stops publishing at ~201805 as MTPASA_CONSTRAINTRESULT, MTPASA_CONSTRAINTSUMMARY starts at transition. DDL keeps both definitions for backward-compat; data flow replaces.
  - Upgrade report mentions successor: ['v4.27:MTPASA_CONSTRAINTRESULT', 'v4.27:MTPASA_CONSTRAINTSUMMARY']
  - Lifecycle: `MTPASA_CONSTRAINTRESULT` first_month = 201805
  - Lifecycle: `MTPASA_CONSTRAINTSUMMARY` first_month = 201805
  - Lifecycle: `MTPASA_CONSTRAINTSOLUTION` last_month = 201805

### H3-MTPASA_INTERCONNECTOR

- **Successor(s):** `MTPASA_INTERCONNECTORRESULT`
- **Predecessor(s):** `MTPASA_INTERCONNECTORSOLUTION`
- **Stated transition month:** 201805
- **Stated confidence:** HIGH
- **Stated evidence:** v4.27 upgrade report
- **Verdict:** **DATA-FLOW-REPLACEMENT**
- **Evidence:**
  - DDL: `MTPASA_INTERCONNECTORSOLUTION` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MTPASA_INTERCONNECTORRESULT` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Both DDL-coexist in v5.6, but mirror lifecycle shows MTPASA_INTERCONNECTORSOLUTION stops publishing at ~201805 as MTPASA_INTERCONNECTORRESULT starts at transition. DDL keeps both definitions for backward-compat; data flow replaces.
  - Upgrade report mentions successor: ['v4.27:MTPASA_INTERCONNECTORRESULT']
  - Lifecycle: `MTPASA_INTERCONNECTORRESULT` first_month = 201805
  - Lifecycle: `MTPASA_INTERCONNECTORSOLUTION` last_month = 201805

### H4-MTPASA_REGION

- **Successor(s):** `MTPASA_REGIONRESULT`, `MTPASA_REGIONSUMMARY`, `MTPASA_REGIONITERATION`
- **Predecessor(s):** `MTPASA_REGIONSOLUTION`
- **Stated transition month:** 201805
- **Stated confidence:** HIGH
- **Stated evidence:** v4.27 upgrade report
- **Verdict:** **DATA-FLOW-REPLACEMENT**
- **Evidence:**
  - DDL: `MTPASA_REGIONSOLUTION` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MTPASA_REGIONRESULT` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MTPASA_REGIONSUMMARY` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MTPASA_REGIONITERATION` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Both DDL-coexist in v5.6, but mirror lifecycle shows MTPASA_REGIONSOLUTION stops publishing at ~201805 as MTPASA_REGIONRESULT, MTPASA_REGIONSUMMARY, MTPASA_REGIONITERATION starts at transition. DDL keeps both definitions for backward-compat; data flow replaces.
  - Upgrade report mentions successor: ['v4.27:MTPASA_REGIONITERATION', 'v4.27:MTPASA_REGIONRESULT', 'v4.27:MTPASA_REGIONSUMMARY', 'v4.28:MTPASA_REGIONRESULT', 'v4.28:MTPASA_REGIONSUMMARY', 'v5.0:MTPASA_REGIONRESULT']
  - Lifecycle: `MTPASA_REGIONRESULT` first_month = 201805
  - Lifecycle: `MTPASA_REGIONSUMMARY` first_month = 201805
  - Lifecycle: `MTPASA_REGIONITERATION` first_month = 201805
  - Lifecycle: `MTPASA_REGIONSOLUTION` last_month = 201805

### H5-MTPASA_LOLP

- **Successor(s):** `MTPASA_LOLPRESULT`
- **Predecessor(s):** `MTPASA_RESERVELIMITSOLUTION`
- **Stated transition month:** 201805
- **Stated confidence:** MEDIUM
- **Stated evidence:** v4.27/v4.28 DOCUMENTATION HTMs (column-match)
- **Verdict:** **DATA-FLOW-REPLACEMENT**
- **Evidence:**
  - DDL: `MTPASA_RESERVELIMITSOLUTION` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MTPASA_LOLPRESULT` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Both DDL-coexist in v5.6, but mirror lifecycle shows MTPASA_RESERVELIMITSOLUTION stops publishing at ~201805 as MTPASA_LOLPRESULT starts at transition. DDL keeps both definitions for backward-compat; data flow replaces.
  - Upgrade report mentions successor: ['v4.27:MTPASA_LOLPRESULT']
  - Lifecycle: `MTPASA_LOLPRESULT` first_month = 201805
  - Lifecycle: `MTPASA_RESERVELIMITSOLUTION` last_month = 201805

### H6-P5MIN_CONSTRAINTSOLUTION

- **Successor(s):** `P5MIN_CONSTRAINTSOLUTION`
- **Predecessor(s):** `P5MIN_CONSTRAINTSOLUTION1`, `P5MIN_CONSTRAINTSOLUTION2`, `P5MIN_CONSTRAINTSOLUTION3`, `P5MIN_CONSTRAINTSOLUTION4`
- **Stated transition month:** 202408
- **Stated confidence:** HIGH
- **Stated evidence:** v5.3 upgrade DDL
- **Note:** Single unified table absorbs four numbered variants.
- **Verdict:** **PRE-DDL-CAPTURED**
- **Evidence:**
  - DDL: `P5MIN_CONSTRAINTSOLUTION1` present in (none — absent in all captured DDL)
  - DDL: `P5MIN_CONSTRAINTSOLUTION2` present in (none — absent in all captured DDL)
  - DDL: `P5MIN_CONSTRAINTSOLUTION3` present in (none — absent in all captured DDL)
  - DDL: `P5MIN_CONSTRAINTSOLUTION4` present in (none — absent in all captured DDL)
  - DDL: `P5MIN_CONSTRAINTSOLUTION` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Upgrade report mentions successor: ['v4.28:P5MIN_CONSTRAINTSOLUTION']
  - Lifecycle: `P5MIN_CONSTRAINTSOLUTION` first_month = 202408
  - Lifecycle: `P5MIN_CONSTRAINTSOLUTION1` last_month = 202407
  - Lifecycle: `P5MIN_CONSTRAINTSOLUTION2` last_month = 202407
  - Lifecycle: `P5MIN_CONSTRAINTSOLUTION3` last_month = 202407
  - Lifecycle: `P5MIN_CONSTRAINTSOLUTION4` last_month = 202407

### H7-P5MIN_SCENARIODEMAND

- **Successor(s):** `P5MIN_SCENARIODEMAND`
- **Predecessor(s):** `P5MINSCENARIODEMAND`
- **Stated transition month:** 202408
- **Stated confidence:** VERY HIGH
- **Stated evidence:** v5.3 upgrade DDL (underscore added)
- **Verdict:** **PRE-DDL-CAPTURED**
- **Evidence:**
  - DDL: `P5MINSCENARIODEMAND` present in (none — absent in all captured DDL)
  - DDL: `P5MIN_SCENARIODEMAND` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Upgrade report mentions successor: ['v5.0:P5MIN_SCENARIODEMAND']
  - Lifecycle: `P5MIN_SCENARIODEMAND` first_month = 202408
  - Lifecycle: `P5MINSCENARIODEMAND` last_month = 202407

### H8-P5MIN_SCENARIODEMANDTRK

- **Successor(s):** `P5MIN_SCENARIODEMANDTRK`
- **Predecessor(s):** `P5MINSCENARIODEMANDTRK`
- **Stated transition month:** 202408
- **Stated confidence:** VERY HIGH
- **Stated evidence:** v5.3 upgrade DDL (underscore added)
- **Verdict:** **PRE-DDL-CAPTURED**
- **Evidence:**
  - DDL: `P5MINSCENARIODEMANDTRK` present in (none — absent in all captured DDL)
  - DDL: `P5MIN_SCENARIODEMANDTRK` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Upgrade report mentions successor: ['v5.0:P5MIN_SCENARIODEMANDTRK']
  - Lifecycle: `P5MIN_SCENARIODEMANDTRK` first_month = 202408
  - Lifecycle: `P5MINSCENARIODEMANDTRK` last_month = 202407

### H9-PREDISPATCH-D-DROP

- **Successor(s):** `PREDISPATCHCONSTRAINT`, `PREDISPATCHINTERCONNECTORRES`, `PREDISPATCHLOAD`, `PREDISPATCHPRICE`, `PREDISPATCHPRICESENSITIVITIES`, `PREDISPATCHREGIONSUM`, `PREDISPATCHSCENARIODEMAND`, `PREDISPATCHSCENARIODEMANDTRK`
- **Predecessor(s):** `PREDISPATCHCONSTRAINT_D`, `PREDISPATCHINTERCONNECTORRES_D`, `PREDISPATCHLOAD_D`, `PREDISPATCHPRICE_D`, `PREDISPATCHPRICESENSITIVITIES_D`, `PREDISPATCHREGIONSUM_D`, `PREDISPATCHSCENARIODEMAND_D`, `PREDISPATCHSCENARIODEMANDTRK_D`
- **Stated transition month:** 202408
- **Stated confidence:** MEDIUM
- **Stated evidence:** v5.3 DDL + upgrade-report cross-check
- **Note:** NOT a rename — _D variants dropped at 2024-08, base existed in parallel throughout DVD era.
- **Verdict:** **PRE-DDL-CAPTURED**
- **Evidence:**
  - DDL: `PREDISPATCHCONSTRAINT_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHINTERCONNECTORRES_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHLOAD_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHPRICE_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHPRICESENSITIVITIES_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHREGIONSUM_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHSCENARIODEMAND_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHSCENARIODEMANDTRK_D` present in (none — absent in all captured DDL)
  - DDL: `PREDISPATCHCONSTRAINT` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `PREDISPATCHINTERCONNECTORRES` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `PREDISPATCHLOAD` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `PREDISPATCHPRICE` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `PREDISPATCHPRICESENSITIVITIES` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `PREDISPATCHREGIONSUM` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `PREDISPATCHSCENARIODEMAND` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `PREDISPATCHSCENARIODEMANDTRK` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Upgrade report mentions successor: ['v4.29:PREDISPATCHREGIONSUM', 'v5.1:PREDISPATCHREGIONSUM', 'v5.2:PREDISPATCHLOAD', 'v5.2:PREDISPATCHPRICE', 'v5.2:PREDISPATCHREGIONSUM', 'v5.3:PREDISPATCHLOAD', 'v5.3:PREDISPATCHREGIONSUM', 'v5.5:PREDISPATCHLOAD', 'v5.5:PREDISPATCHREGIONSUM', 'v5.6:PREDISPATCHLOAD']
  - Lifecycle: `PREDISPATCHCONSTRAINT` first_month = 202408
  - Lifecycle: `PREDISPATCHINTERCONNECTORRES` first_month = 202408
  - Lifecycle: `PREDISPATCHLOAD` first_month = 202408
  - Lifecycle: `PREDISPATCHPRICE` first_month = 202408
  - Lifecycle: `PREDISPATCHPRICESENSITIVITIES` first_month = 202408
  - Lifecycle: `PREDISPATCHREGIONSUM` first_month = 202408
  - Lifecycle: `PREDISPATCHSCENARIODEMAND` first_month = 201501
  - Lifecycle: `PREDISPATCHSCENARIODEMANDTRK` first_month = 201501
  - Lifecycle: `PREDISPATCHCONSTRAINT_D` last_month = 202407
  - Lifecycle: `PREDISPATCHINTERCONNECTORRES_D` last_month = 202407
  - Lifecycle: `PREDISPATCHLOAD_D` last_month = 202407
  - Lifecycle: `PREDISPATCHPRICE_D` last_month = 202407
  - Lifecycle: `PREDISPATCHREGIONSUM_D` last_month = 202407

### H10-DISPATCHLOAD-VS-TRADINGLOAD

- **Successor(s):** `DISPATCHLOAD`, `DISPATCHREGIONSUM`
- **Predecessor(s):** `TRADINGLOAD`, `TRADINGREGIONSUM`
- **Stated transition month:** 202109
- **Stated confidence:** HIGH
- **Stated evidence:** v5.0/v5.1 5MS technical specifications
- **Note:** 5-min vs 30-min interval change; not a strict rename, an interval-resolution shift.
- **Verdict:** **DATA-FLOW-REPLACEMENT**
- **Evidence:**
  - DDL: `TRADINGLOAD` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `TRADINGREGIONSUM` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `DISPATCHLOAD` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `DISPATCHREGIONSUM` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Both DDL-coexist in v5.6, but mirror lifecycle shows TRADINGLOAD, TRADINGREGIONSUM stops publishing at ~202109 as DISPATCHLOAD, DISPATCHREGIONSUM already active. DDL keeps both definitions for backward-compat; data flow replaces.
  - Upgrade report mentions successor: ['v4.29:DISPATCHREGIONSUM', 'v5.1:DISPATCHLOAD', 'v5.1:DISPATCHREGIONSUM', 'v5.2:DISPATCHLOAD', 'v5.2:DISPATCHREGIONSUM', 'v5.3:DISPATCHLOAD', 'v5.3:DISPATCHREGIONSUM', 'v5.5:DISPATCHLOAD', 'v5.5:DISPATCHREGIONSUM', 'v5.6:DISPATCHLOAD']
  - Lifecycle: `DISPATCHLOAD` first_month = 201501
  - Lifecycle: `DISPATCHREGIONSUM` first_month = 201501
  - Lifecycle: `TRADINGLOAD` last_month = 202109
  - Lifecycle: `TRADINGREGIONSUM` last_month = 202109
  - Column overlap `TRADINGREGIONSUM@v5.2` vs `DISPATCHREGIONSUM@v5.3`: 89/125 (71%)
  - Column overlap `TRADINGREGIONSUM@v5.2` vs `DISPATCHREGIONSUM@v5.4`: 89/125 (71%)
  - Column overlap `TRADINGREGIONSUM@v5.2` vs `DISPATCHREGIONSUM@v5.5`: 89/127 (70%)

### H11-DISPATCHINTERCONNECTORRES

- **Successor(s):** `DISPATCHINTERCONNECTORRES`
- **Predecessor(s):** `INTERCONNMWFLOW`
- **Stated transition month:** 202105
- **Stated confidence:** MEDIUM
- **Stated evidence:** v5.0 upgrade report
- **Verdict:** **DATA-FLOW-REPLACEMENT**
- **Evidence:**
  - DDL: `INTERCONNMWFLOW` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `DISPATCHINTERCONNECTORRES` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Both DDL-coexist in v5.6, but mirror lifecycle shows INTERCONNMWFLOW stops publishing at ~202105 as DISPATCHINTERCONNECTORRES already active. DDL keeps both definitions for backward-compat; data flow replaces.
  - Lifecycle: `DISPATCHINTERCONNECTORRES` first_month = 201501
  - Lifecycle: `INTERCONNMWFLOW` last_month = 202105

### H12-MARKET_SUSPEND

- **Successor(s):** `MARKET_SUSPEND_REGIME_SUM`, `MARKET_SUSPEND_REGION_SUM`, `MARKET_SUSPEND_SCHEDULE`, `MARKET_SUSPEND_SCHEDULE_TRK`
- **Predecessor(s):** `MARKETNOTICEDATA`
- **Stated transition month:** 202408
- **Stated confidence:** LOW
- **Stated evidence:** v5.3 DDL / upgrade-report (likely NOT a rename)
- **Note:** Thematic match only; orthogonal capability rather than rename.
- **Verdict:** **DATA-FLOW-REPLACEMENT**
- **Evidence:**
  - DDL: `MARKETNOTICEDATA` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MARKET_SUSPEND_REGIME_SUM` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MARKET_SUSPEND_REGION_SUM` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MARKET_SUSPEND_SCHEDULE` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - DDL: `MARKET_SUSPEND_SCHEDULE_TRK` present in ['v5.2', 'v5.3', 'v5.4', 'v5.5', 'v5.6']
  - Both DDL-coexist in v5.6, but mirror lifecycle shows MARKETNOTICEDATA stops publishing at ~202408 as MARKET_SUSPEND_REGIME_SUM, MARKET_SUSPEND_REGION_SUM, MARKET_SUSPEND_SCHEDULE, MARKET_SUSPEND_SCHEDULE_TRK starts at transition. DDL keeps both definitions for backward-compat; data flow replaces.
  - Upgrade report mentions successor: ['v4.27:MARKET_SUSPEND_REGIME_SUM', 'v4.27:MARKET_SUSPEND_REGION_SUM', 'v4.27:MARKET_SUSPEND_SCHEDULE', 'v4.27:MARKET_SUSPEND_SCHEDULE_TRK', 'v5.2:MARKET_SUSPEND_SCHEDULE']
  - Lifecycle: `MARKET_SUSPEND_REGIME_SUM` first_month = 202408
  - Lifecycle: `MARKET_SUSPEND_REGION_SUM` first_month = 202408
  - Lifecycle: `MARKET_SUSPEND_SCHEDULE` first_month = 202408
  - Lifecycle: `MARKET_SUSPEND_SCHEDULE_TRK` first_month = 202408
  - Lifecycle: `MARKETNOTICEDATA` last_month = 202407

## 4. Renames in DDL not covered by §6

These renames appear in AEMO's upgrade DDL but are not listed as hypotheses in `MMSDM-TABLE-LIFECYCLE.md §6`. Consider adding rows.

| Version | Scope | Target table | Old | New |
|---|---|---|---|---|
| v5.5 | column | `FPP_FCAS_SUMMARY` | `USAGE` | `USAGE_VALUE` |
| v5.5 | column | `FPP_USAGE` | `USAGE` | `USAGE_VALUE` |

## 5. How to re-run

```bash
python3 scripts/synthesize_mmsdm_timeline.py \
    --columns reference/MMSDM-DDL-COLUMNS.csv \
    --renames reference/MMSDM-DDL-RENAMES.csv \
    --upgrade reference/MMSDM-UPGRADE-TABLES.csv \
    --lifecycle reference/MMSDM-TABLE-LIFECYCLE.csv \
    --timeline-out reference/MMSDM-TABLE-TIMELINE.csv \
    --report-out reference/MMSDM-RENAMES-VERIFICATION.md
```

