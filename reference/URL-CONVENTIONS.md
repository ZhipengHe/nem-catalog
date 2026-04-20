# NEMWeb URL Conventions

Empirically derived from 2863 IIS directory listings in `nemweb-mirror/`. 2549 listings contained files; 217772 filenames analyzed. **367 distinct datasets** across 4 of 4 repositories, 2347 (dataset, tier, path, pattern) rows.

**Taxonomy** (per `reference/NEMWEB-STRUCTURE.md` §1):

- **Repo** ∈ {`Reports`, `MMSDM`, `NEMDE`, `FCAS_Causer_Pays`} — exactly four.
- **Dataset** = `(repo, intra_repo_id)`. Cross-repo identity is **default-separate** — two entries with the same `intra_repo_id` under different repos are distinct catalog keys and are NOT merged (see NEMWEB-STRUCTURE.md §4).
- **Retention / view tier** depends on repo: Reports has CURRENT/ARCHIVE; MMSDM uses the SQLLoader view name (CTL, DATA, BCP_FMT, BCP_DATA, MYSQL, INDEX, UTILITIES, LOGS, P5MIN_ALL_DATA, PREDISP_ALL_DATA, DOCUMENTATION) plus MONTHLY_BULK and MTPASA_DATA_EXPORT; NEMDE uses NEMDE_Files or File_Readers; FCAS_Causer_Pays is single-tier.

**Field split: stable vs snapshot.** The fields `repo`, `retention_tier`, `intra_repo_id`, `path_template`, `filename_template`, `filename_regex`, and `anomaly` are **stable** — they are byte-deterministic across mirror re-runs. The `file_count_snapshot`, `first_seen_snapshot`, and `last_seen_snapshot` columns are **volatile** — they drift every time the walker runs because `/Reports/CURRENT/` rolls daily. Stable fields are the catalog; snapshot fields are provenance-of-the-walk.

**Known limitation — table-name evolution is NOT resolved here.** When AEMO renames a table (e.g. an MMSDM table's name string changes across MMS Data Model versions), the old name and new name appear here as two separate `(repo, intra_repo_id)` datasets. Merging them requires either parsing the `MMS Data Model/v*/` HTML docs inside the mirror, or supplying an alias map externally — both are out of scope for this script.

## Repo: `Reports`  (96 datasets, 610 rows)

### `Reports` · `ANCILLARY_SERVICES_REPORTS`

_1 pattern row, 7 files (snapshot), observed 2026-03-03 → 2026-04-14 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/ANCILLARY_SERVICES_REPORTS/` | `PUBLIC_ANCILLARY_SERVICES_{date}.zip` | `PUBLIC_ANCILLARY_SERVICES_\d{8}\.zip` | `PUBLIC_ANCILLARY_SERVICES_20260303.zip` | 7 | 2026-03-03 | 2026-04-14 |

### `Reports` · `Adjusted_Prices_Reports`

_2 pattern rows, 3618 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Adjusted_Prices_Reports/` | `PUBLIC_PRICE_REVISION_DISPATCH_{date}.zip` | `PUBLIC_PRICE_REVISION_DISPATCH_\d{8}\.zip` | `PUBLIC_PRICE_REVISION_DISPATCH_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Adjusted_Prices_Reports/` | `PUBLIC_PRICE_REVISION_DISPATCH_{datetime}_{aemo_id}.zip` | `PUBLIC_PRICE_REVISION_DISPATCH_\d{14}_\d{16}\.zip` | `PUBLIC_PRICE_REVISION_DISPATCH_20260223143431_0000000504787407.zip` | 3606 | 2026-02-23 | 2026-04-20 |

### `Reports` · `Alt_Limits`

_1 pattern row, 1 files (snapshot), observed 2026-04-17 → 2026-04-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Alt_Limits/` | `PUBLIC_TER_DAILY.zip` | `PUBLIC_TER_DAILY\.zip` | `PUBLIC_TER_DAILY.zip` | 1 | 2026-04-17 | 2026-04-17 |

### `Reports` · `Ancillary_Services_Payments`

_6 pattern rows, 34 files (snapshot), observed 2016-12-02 → 2026-04-18 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Ancillary_Services_Payments/` | `AS_ACE_RECOVERY_RATES.PNG` | `AS_ACE_RECOVERY_RATES\.PNG` | `AS_ACE_RECOVERY_RATES.PNG` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/Ancillary_Services_Payments/` | `AS_ASOE_RECOVERY_RATES.PNG` | `AS_ASOE_RECOVERY_RATES\.PNG` | `AS_ASOE_RECOVERY_RATES.PNG` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/Ancillary_Services_Payments/` | `AS_CUST_RECOVERY_RATES.PNG` | `AS_CUST_RECOVERY_RATES\.PNG` | `AS_CUST_RECOVERY_RATES.PNG` | 1 | 2025-06-06 | 2025-06-06 |
| `CURRENT` | `/Reports/CURRENT/Ancillary_Services_Payments/` | `AS_GEN_RECOVERY_RATES.PNG` | `AS_GEN_RECOVERY_RATES\.PNG` | `AS_GEN_RECOVERY_RATES.PNG` | 1 | 2025-06-06 | 2025-06-06 |
| `CURRENT` | `/Reports/CURRENT/Ancillary_Services_Payments/` | `AS_PAYMENTS_SUMMARY_{year}.CSV` | `AS_PAYMENTS_SUMMARY_\d{4}\.CSV` | `AS_PAYMENTS_SUMMARY_2012.CSV` | 15 | 2016-12-02 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/Ancillary_Services_Payments/` | `AS_RECOVERY_SUMMARY_{year}.CSV` | `AS_RECOVERY_SUMMARY_\d{4}\.CSV` | `AS_RECOVERY_SUMMARY_2012.CSV` | 15 | 2016-12-02 | 2026-04-18 |

### `Reports` · `Auction_Units_Reports`

_1 pattern row, 224 files (snapshot), observed 2025-03-25 → 2026-04-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Auction_Units_Reports/` | `AUCUNITS_{date}.R{d3}` | `AUCUNITS_\d{8}\.R\d{3}` | `AUCUNITS_20240825.R015` | 224 | 2025-03-25 | 2026-04-17 |

### `Reports` · `Bidmove_Complete`

_2 pattern rows, 72 files (snapshot), observed 2025-05-02 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Bidmove_Complete/` | `PUBLIC_BIDMOVE_COMPLETE_{date}.zip` | `PUBLIC_BIDMOVE_COMPLETE_\d{8}\.zip` | `PUBLIC_BIDMOVE_COMPLETE_20250302.zip` | 12 | 2025-05-02 | 2026-04-02 |
| `CURRENT` | `/Reports/CURRENT/Bidmove_Complete/` | `PUBLIC_BIDMOVE_COMPLETE_{date}_{aemo_id}.zip` | `PUBLIC_BIDMOVE_COMPLETE_\d{8}_\d{16}\.zip` | `PUBLIC_BIDMOVE_COMPLETE_20260219_0000000504277195.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Billing`

_5 pattern rows, 544 files (snapshot), observed 2017-02-02 → 2026-04-02 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Billing/` | `PUBLIC_BILLING_{date}.zip` | `PUBLIC_BILLING_\d{8}\.zip` | `PUBLIC_BILLING_20250302.zip` | 12 | 2025-05-02 | 2026-04-02 |
| `CURRENT` | `/Reports/CURRENT/Billing/` | `PUBLIC_BILLING_DIRECT_FINAL_RECON_{year}Week{d1}REVISE_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_FINAL_RECON_\d{4}Week\d{1}REVISE_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_FINAL_RECON_2020Week1REVISE_20200519132635.zip` | 1 | 2020-05-19 | 2020-05-19 |
| `CURRENT` | `/Reports/CURRENT/Billing/` | `PUBLIC_BILLING_DIRECT_PROV_CRA_SPLIT_CAT_REG_{year}Week{d2}_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_PROV_CRA_SPLIT_CAT_REG_\d{4}Week\d{2}_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_PROV_CRA_SPLIT_CAT_REG_2021Week17_20210519110609.zip` | 1 | 2021-05-19 | 2021-05-19 |
| `CURRENT` | `/Reports/CURRENT/Billing/` | `PUBLIC_BILLING_DIRECT_PROV_RECON_{year}Week{d2}FINAL_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_PROV_RECON_\d{4}Week\d{2}FINAL_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_PROV_RECON_2020Week45FINAL_20201202104406.zip` | 2 | 2020-12-02 | 2021-06-09 |
| `CURRENT` | `/Reports/CURRENT/Billing/` | `PUBLIC_BILLING_{datetime}_{aemo_id}.zip` | `PUBLIC_BILLING_\d{14}_\d{16}\.zip` | `PUBLIC_BILLING_20170202011133_0000000280585170.zip` | 528 | 2017-02-02 | 2018-01-03 |

### `Reports` · `CDEII`

_5 pattern rows, 12 files (snapshot), observed 2026-02-20 → 2026-04-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/CDEII/` | `CO{d1}EII_AVAILABLE_GENERATORS.CSV` | `CO\d{1}EII_AVAILABLE_GENERATORS\.CSV` | `CO2EII_AVAILABLE_GENERATORS.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/CDEII/` | `CO{d11}EII_AVAILABLE_GENERATORS_{year}_{d12}_{datetime}.CSV` | `CO\d{1}EII_AVAILABLE_GENERATORS_\d{4}_\d{1}_\d{14}\.CSV` | `CO2EII_AVAILABLE_GENERATORS_2026_7_20260220083314.CSV` | 3 | 2026-02-20 | 2026-03-06 |
| `CURRENT` | `/Reports/CURRENT/CDEII/` | `CO{d1}EII_AVAILABLE_GENERATORS_{year}_{d2}_{datetime}.CSV` | `CO\d{1}EII_AVAILABLE_GENERATORS_\d{4}_\d{2}_\d{14}\.CSV` | `CO2EII_AVAILABLE_GENERATORS_2026_10_20260313111124.CSV` | 6 | 2026-03-13 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/CDEII/` | `CO{d1}EII_SUMMARY_RESULTS.CSV` | `CO\d{1}EII_SUMMARY_RESULTS\.CSV` | `CO2EII_SUMMARY_RESULTS.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/CDEII/` | `CO{d1}EII_SUMMARY_RESULTS_{year}.CSV` | `CO\d{1}EII_SUMMARY_RESULTS_\d{4}\.CSV` | `CO2EII_SUMMARY_RESULTS_2026.CSV` | 1 | 2026-04-17 | 2026-04-17 |

### `Reports` · `CSC_CSP_Settlements`

_5 pattern rows, 33 files (snapshot), observed 2026-02-20 → 2026-04-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/CSC_CSP_Settlements/` | `PUBLIC_BILLINGCSP_{year}WEEK{d1}FINAL_{datetime}_{aemo_id}.zip` | `PUBLIC_BILLINGCSP_\d{4}WEEK\d{1}FINAL_\d{14}_\d{16}\.zip` | `PUBLIC_BILLINGCSP_2026WEEK5FINAL_20260225111834_0000000505071174.zip` | 5 | 2026-02-25 | 2026-03-25 |
| `CURRENT` | `/Reports/CURRENT/CSC_CSP_Settlements/` | `PUBLIC_BILLINGCSP_{year}WEEK{d1}PRELIM_{datetime}_{aemo_id}.zip` | `PUBLIC_BILLINGCSP_\d{4}WEEK\d{1}PRELIM_\d{14}_\d{16}\.zip` | `PUBLIC_BILLINGCSP_2026WEEK7PRELIM_20260220082904_0000000504301075.zip` | 3 | 2026-02-20 | 2026-03-06 |
| `CURRENT` | `/Reports/CURRENT/CSC_CSP_Settlements/` | `PUBLIC_BILLINGCSP_{year}WEEK{d2}FINAL_{datetime}_{aemo_id}.zip` | `PUBLIC_BILLINGCSP_\d{4}WEEK\d{2}FINAL_\d{14}_\d{16}\.zip` | `PUBLIC_BILLINGCSP_2026WEEK10FINAL_20260401110532_0000000510763856.zip` | 3 | 2026-04-01 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/CSC_CSP_Settlements/` | `PUBLIC_BILLINGCSP_{year}WEEK{d2}PRELIM_{datetime}_{aemo_id}.zip` | `PUBLIC_BILLINGCSP_\d{4}WEEK\d{2}PRELIM_\d{14}_\d{16}\.zip` | `PUBLIC_BILLINGCSP_2026WEEK10PRELIM_20260313110702_0000000507657613.zip` | 6 | 2026-03-13 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/CSC_CSP_Settlements/` | `PUBLIC_BILLINGCSP_{year}WEEK{d2}REVISE_{datetime}_{aemo_id}.zip` | `PUBLIC_BILLINGCSP_\d{4}WEEK\d{2}REVISE_\d{14}_\d{16}\.zip` | `PUBLIC_BILLINGCSP_2025WEEK31REVISE_20260226112035_0000000505237166.zip` | 16 | 2026-02-24 | 2026-04-16 |

### `Reports` · `Causer_Pays_Elements`

_1 pattern row, 31 files (snapshot), observed 2020-03-04 → 2025-04-15 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Causer_Pays_Elements/` | `Elements_FCAS_{timestamp}.csv` | `Elements_FCAS_\d{12}\.csv` | `Elements_FCAS_201912121110.csv` | 31 | 2020-03-04 | 2025-04-15 |

### `Reports` · `Causer_Pays_Scada`

_1 pattern row, 24 files (snapshot), observed 2025-04-14 → 2025-09-22 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Causer_Pays_Scada/` | `PUBLIC_CAUSER_PAYS_SCADA_{date}.zip` | `PUBLIC_CAUSER_PAYS_SCADA_\d{8}\.zip` | `PUBLIC_CAUSER_PAYS_SCADA_20250331.zip` | 24 | 2025-04-14 | 2025-09-22 |

### `Reports` · `DAILYOCD`

_1 pattern row, 45 files (snapshot), observed 2025-04-05 → 2026-04-01 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/DAILYOCD/` | `PUBLIC_DAILYOCD_{timestamp}_{datetime}.zip` | `PUBLIC_DAILYOCD_\d{12}_\d{14}\.zip` | `PUBLIC_DAILYOCD_202504040000_20250405040500.zip` | 45 | 2025-04-05 | 2026-04-01 |

### `Reports` · `DISPATCHFCST`

_2 pattern rows, 1300 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/DISPATCHFCST/` | `PUBLIC_DISPATCHFCST_{date}.zip` | `PUBLIC_DISPATCHFCST_\d{8}\.zip` | `PUBLIC_DISPATCHFCST_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/DISPATCHFCST/` | `PUBLIC_DISPATCHFCST_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCHFCST_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCHFCST_202604181445_0000000513537618.zip` | 925 | 2026-04-18 | 2026-04-20 |

### `Reports` · `DISPATCHIS_PRICE_REVISIONS`

_1 pattern row, 4681 files (snapshot), observed 2025-09-17 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/DISPATCHIS_PRICE_REVISIONS/` | `PUBLIC_PRICE_REVISION_DISPATCHIS_{datetime}_{aemo_id}.zip` | `PUBLIC_PRICE_REVISION_DISPATCHIS_\d{14}_\d{16}\.zip` | `PUBLIC_PRICE_REVISION_DISPATCHIS_20250301163013_0000000453111936.zip` | 4681 | 2025-09-17 | 2026-04-20 |

### `Reports` · `DISPATCH_NEGATIVE_RESIDUE`

_2 pattern rows, 578 files (snapshot), observed 2026-03-03 → 2026-04-20 (snapshot) · **anomaly:** casing_mismatch_vs_sibling_tier_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/DISPATCH_NEGATIVE_RESIDUE/` | `PUBLIC_DISPATCH_NEGATIVE_RESIDUE_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCH_NEGATIVE_RESIDUE_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCH_NEGATIVE_RESIDUE_202604181445_0000000513537055.zip` | 577 | 2026-04-18 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/DISPATCH_NEGATIVE_RESIDUE/DUPLICATE/` | `PUBLIC_DISPATCH_NEGATIVE_RESIDUE_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCH_NEGATIVE_RESIDUE_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCH_NEGATIVE_RESIDUE_202603031345_0000000506102388.zip` | 1 | 2026-03-03 | 2026-03-03 |

### `Reports` · `DWGM`

_2 pattern rows, 2 files (snapshot), observed 2016-09-29 → 2016-09-29 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/DWGM/MOS Estimates/` | `MOS_Estimates_Jun_{year1}-Aug_{year2}-Supporting_Data.xlsx` | `MOS_Estimates_Jun_\d{4}\-Aug_\d{4}\-Supporting_Data\.xlsx` | `MOS_Estimates_Jun_2016-Aug_2016-Supporting_Data.xlsx` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/DWGM/MOS Estimates/` | `MOS_Period_Jun_{year1}-Aug_{year2}-MOS_Estimates_Report.pdf` | `MOS_Period_Jun_\d{4}\-Aug_\d{4}\-MOS_Estimates_Report\.pdf` | `MOS_Period_Jun_2016-Aug_2016-MOS_Estimates_Report.pdf` | 1 | 2016-09-29 | 2016-09-29 |

### `Reports` · `Daily_Reports`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Daily_Reports/` | `PUBLIC_DAILY_{date}.zip` | `PUBLIC_DAILY_\d{8}\.zip` | `PUBLIC_DAILY_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Daily_Reports/` | `PUBLIC_DAILY_{timestamp}_{datetime}.zip` | `PUBLIC_DAILY_\d{12}_\d{14}\.zip` | `PUBLIC_DAILY_202602190000_20260220040503.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Directions_Reconciliation`

_5 pattern rows, 32 files (snapshot), observed 2026-02-24 → 2026-04-14 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Directions_Reconciliation/` | `PUBLIC_BILLING_DIRECT_FINAL_CRA_SPLIT_CAT_REG_{year}Week{d2}_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_FINAL_CRA_SPLIT_CAT_REG_\d{4}Week\d{2}_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_FINAL_CRA_SPLIT_CAT_REG_2025Week31_20260226115204.zip` | 10 | 2026-02-24 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/Directions_Reconciliation/` | `PUBLIC_BILLING_DIRECT_FINAL_RECON_{year}Week{d2}REVISE_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_FINAL_RECON_\d{4}Week\d{2}REVISE_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_FINAL_RECON_2025Week31REVISE_20260226111908.zip` | 10 | 2026-02-24 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/Directions_Reconciliation/` | `PUBLIC_BILLING_DIRECT_PROV_CRA_SPLIT_CAT_REG_{year}Week{d2}_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_PROV_CRA_SPLIT_CAT_REG_\d{4}Week\d{2}_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_PROV_CRA_SPLIT_CAT_REG_2025Week41_20260224113329.zip` | 6 | 2026-02-24 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/Directions_Reconciliation/` | `PUBLIC_BILLING_DIRECT_PROV_RECON_{year}Week{d2}FINAL_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_PROV_RECON_\d{4}Week\d{2}FINAL_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_PROV_RECON_2026Week11FINAL_20260410114716.zip` | 1 | 2026-04-10 | 2026-04-10 |
| `CURRENT` | `/Reports/CURRENT/Directions_Reconciliation/` | `PUBLIC_BILLING_DIRECT_PROV_RECON_{year}Week{d2}REVISE_{datetime}.zip` | `PUBLIC_BILLING_DIRECT_PROV_RECON_\d{4}Week\d{2}REVISE_\d{14}\.zip` | `PUBLIC_BILLING_DIRECT_PROV_RECON_2025Week41REVISE_20260224110940.zip` | 5 | 2026-02-24 | 2026-04-14 |

### `Reports` · `DispatchIS_Reports`

_2 pattern rows, 952 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/DispatchIS_Reports/` | `PUBLIC_DISPATCHIS_{date}.zip` | `PUBLIC_DISPATCHIS_\d{8}\.zip` | `PUBLIC_DISPATCHIS_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/DispatchIS_Reports/` | `PUBLIC_DISPATCHIS_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCHIS_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCHIS_202604181445_0000000513537596.zip` | 577 | 2026-04-18 | 2026-04-20 |

### `Reports` · `Dispatch_IRSR`

_3 pattern rows, 953 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Dispatch_IRSR/` | `PUBLIC_DISPATCH_IRSR_{date}.zip` | `PUBLIC_DISPATCH_IRSR_\d{8}\.zip` | `PUBLIC_DISPATCH_IRSR_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Dispatch_IRSR/` | `PUBLIC_DISPATCH_IRSR_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCH_IRSR_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCH_IRSR_202604181445_0000000513537804.zip` | 577 | 2026-04-18 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Dispatch_IRSR/DUPLICATE/` | `PUBLIC_DISPATCH_IRSR_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCH_IRSR_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCH_IRSR_202511281730_0000000491450210.zip` | 1 | 2025-11-28 | 2025-11-28 |

### `Reports` · `Dispatch_Negative_Residue`

_1 pattern row, 375 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot) · **anomaly:** casing_mismatch_vs_sibling_tier_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Dispatch_Negative_Residue/` | `DISPATCH_NEGATIVE_RESIDUE_{date}.zip` | `DISPATCH_NEGATIVE_RESIDUE_\d{8}\.zip` | `DISPATCH_NEGATIVE_RESIDUE_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |

### `Reports` · `Dispatch_Reports`

_2 pattern rows, 952 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Dispatch_Reports/` | `PUBLIC_DISPATCH_{date}.zip` | `PUBLIC_DISPATCH_\d{8}\.zip` | `PUBLIC_DISPATCH_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Dispatch_Reports/` | `PUBLIC_DISPATCH_{timestamp}_{datetime}_LEGACY.zip` | `PUBLIC_DISPATCH_\d{12}_\d{14}_LEGACY\.zip` | `PUBLIC_DISPATCH_202604181445_20260418144016_LEGACY.zip` | 577 | 2026-04-18 | 2026-04-20 |

### `Reports` · `Dispatch_SCADA`

_3 pattern rows, 953 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Dispatch_SCADA/` | `PUBLIC_DISPATCHSCADA_{date}.zip` | `PUBLIC_DISPATCHSCADA_\d{8}\.zip` | `PUBLIC_DISPATCHSCADA_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Dispatch_SCADA/` | `PUBLIC_DISPATCHSCADA_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCHSCADA_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCHSCADA_202604181445_0000000513537601.zip` | 577 | 2026-04-18 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Dispatch_SCADA/DUPLICATE/` | `PUBLIC_DISPATCHSCADA_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCHSCADA_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCHSCADA_202508121115_0000000475994495.zip` | 1 | 2025-08-12 | 2025-08-12 |

### `Reports` · `Dispatchprices_PRE_AP`

_3 pattern rows, 953 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Dispatchprices_PRE_AP/` | `PUBLIC_DISPATCHPRICES_PRE_AP_{date}.zip` | `PUBLIC_DISPATCHPRICES_PRE_AP_\d{8}\.zip` | `PUBLIC_DISPATCHPRICES_PRE_AP_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Dispatchprices_PRE_AP/` | `PUBLIC_DISPATCHPRICES_PRE_AP_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCHPRICES_PRE_AP_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCHPRICES_PRE_AP_202604181445_0000000513537600.zip` | 577 | 2026-04-18 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Dispatchprices_PRE_AP/DUPLICATE/` | `PUBLIC_DISPATCHPRICES_PRE_AP_{timestamp}_{aemo_id}.zip` | `PUBLIC_DISPATCHPRICES_PRE_AP_\d{12}_\d{16}\.zip` | `PUBLIC_DISPATCHPRICES_PRE_AP_202508121115_0000000475994494.zip` | 1 | 2025-08-12 | 2025-08-12 |

### `Reports` · `ECGS`

_14 pattern rows, 15 files (snapshot), observed 2026-03-10 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/ECGS/` | `INT{d3}_V{d11}_ECGS_CONTACTS_{d12}.CSV` | `INT\d{3}_V\d{1}_ECGS_CONTACTS_\d{1}\.CSV` | `INT934_V4_ECGS_CONTACTS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/` | `INT{d3}A_V{d11}_SYSTEM_NOTICES_{d12}.csv` | `INT\d{3}A_V\d{1}_SYSTEM_NOTICES_\d{1}\.csv` | `INT929A_V4_SYSTEM_NOTICES_1.csv` | 1 | 2026-03-10 | 2026-03-10 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - AEMO ECGS GSAR Minutes {d2} November {year}.pdf` | `\d{14}\ \-\ AEMO\ ECGS\ GSAR\ Minutes\ \d{2}\ November\ \d{4}\.pdf` | `20251126170617 - AEMO ECGS GSAR Minutes 26 November 2025.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - Direction Revocation Notice, QGP Failure Event.pdf` | `\d{14}\ \-\ Direction\ Revocation\ Notice,\ QGP\ Failure\ Event\.pdf` | `20241210093730 - Direction Revocation Notice, QGP Failure Event.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - ECGS Industry Conference Attendance List {d1} March {year}.pdf` | `\d{14}\ \-\ ECGS\ Industry\ Conference\ Attendance\ List\ \d{1}\ March\ \d{4}\.pdf` | `20240307131831 - ECGS Industry Conference Attendance List 5 March 2024.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - ECGS Market Notice of Claim Request.pdf` | `\d{14}\ \-\ ECGS\ Market\ Notice\ of\ Claim\ Request\.pdf` | `20241210110638 - ECGS Market Notice of Claim Request.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - ECGS Test Platform.pdf` | `\d{14}\ \-\ ECGS\ Test\ Platform\.pdf` | `20230516121257 - ECGS Test Platform.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - East Coast Gas System Industry Conference Minutes of Meeting {d2} June {year}.pdf` | `\d{14}\ \-\ East\ Coast\ Gas\ System\ Industry\ Conference\ Minutes\ of\ Meeting\ \d{2}\ June\ \d{4}\.pdf` | `20240621094802 - East Coast Gas System Industry Conference Minutes of Meeting 20 June 2024.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - East Coast Gas System Risk or Threat Notice {d2} June {year}.pdf` | `\d{14}\ \-\ East\ Coast\ Gas\ System\ Risk\ or\ Threat\ Notice\ \d{2}\ June\ \d{4}\.pdf` | `20240619180058 - East Coast Gas System Risk or Threat Notice 19 June 2024.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - East Coast Gas System reforms Workshop {d1} - {d2} January {year}.pdf` | `\d{14}\ \-\ East\ Coast\ Gas\ System\ reforms\ Workshop\ \d{1}\ \-\ \d{2}\ January\ \d{4}\.pdf` | `20230428180528 - East Coast Gas System reforms Workshop 1 - 18 January 2023.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - Industry Conference Minutes {d21}.{d22}.{year1} Published {d23}.{d24}.{year2}.pdf` | `\d{14}\ \-\ Industry\ Conference\ Minutes\ \d{2}\.\d{2}\.\d{4}\ Published\ \d{2}\.\d{2}\.\d{4}\.pdf` | `20240308131215 - Industry Conference Minutes 07.03.2024 Published 08.03.2024.pdf` | 2 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - Industry conference meeting notes and attendance list {d21}.{d22}.{year1} Published {d23}.{d24}.{year2}.pdf` | `\d{14}\ \-\ Industry\ conference\ meeting\ notes\ and\ attendance\ list\ \d{2}\.\d{2}\.\d{4}\ Published\ \d{2}\.\d{2}\.\d{4}\.pdf` | `20240307140718 - Industry conference meeting notes and attendance list 05.03.2024 Published 07.03.2024.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - REVOCATION OF EAST COAST GAS SYSTEM RISK OR THREAT NOTICE {d2} AUG {year}.pdf` | `\d{14}\ \-\ REVOCATION\ OF\ EAST\ COAST\ GAS\ SYSTEM\ RISK\ OR\ THREAT\ NOTICE\ \d{2}\ AUG\ \d{4}\.pdf` | `20240823135740 - REVOCATION OF EAST COAST GAS SYSTEM RISK OR THREAT NOTICE 23 AUG 2024.pdf` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ECGS/ECGS_Notices/Attachments/` | `{datetime} - Revocation of a Risk or Threat Notice, QGP Failure Event.pdf` | `\d{14}\ \-\ Revocation\ of\ a\ Risk\ or\ Threat\ Notice,\ QGP\ Failure\ Event\.pdf` | `20241210094931 - Revocation of a Risk or Threat Notice, QGP Failure Event.pdf` | 1 | 2026-04-20 | 2026-04-20 |

### `Reports` · `FPP`

_1 pattern row, 1034 files (snapshot), observed 2024-12-14 → 2026-04-19 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/FPP/` | `PUBLIC_FPP_DCF_{timestamp}_{aemo_id}.zip` | `PUBLIC_FPP_DCF_\d{12}_\d{16}\.zip` | `PUBLIC_FPP_DCF_202412141802_0000000443338900.zip` | 1034 | 2024-12-14 | 2026-04-19 |

### `Reports` · `FPPDAILY`

_6 pattern rows, 263 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/FPPDAILY/` | `PUBLIC_NEXT_DAY_FPPMW_{d1}_{date}.zip` | `PUBLIC_NEXT_DAY_FPPMW_\d{1}_\d{8}\.zip` | `PUBLIC_NEXT_DAY_FPPMW_2_20250912.zip` | 30 | 2025-11-25 | 2026-04-17 |
| `ARCHIVE` | `/Reports/ARCHIVE/FPPDAILY/` | `PUBLIC_NEXT_DAY_FPPMW_{date}.zip` | `PUBLIC_NEXT_DAY_FPPMW_\d{8}\.zip` | `PUBLIC_NEXT_DAY_FPPMW_20250331.zip` | 41 | 2025-05-01 | 2026-04-19 |
| `ARCHIVE` | `/Reports/ARCHIVE/FPPDAILY/` | `PUBLIC_NEXT_DAY_FPP_{date}.zip` | `PUBLIC_NEXT_DAY_FPP_\d{8}\.zip` | `PUBLIC_NEXT_DAY_FPP_20250331.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/FPPDAILY/` | `PUBLIC_NEXT_DAY_FPPMW_{d1}_{datetime}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_FPPMW_\d{1}_\d{14}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_FPPMW_2_20260220070046_0000000504291041.zip` | 60 | 2026-02-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/FPPDAILY/` | `PUBLIC_NEXT_DAY_FPPMW_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_FPPMW_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_FPPMW_20260220_0000000504291040.zip` | 60 | 2026-02-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/FPPDAILY/` | `PUBLIC_NEXT_DAY_FPP_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_FPP_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_FPP_20260219_0000000504291039.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `FPPRATES`

_2 pattern rows, 952 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/FPPRATES/` | `PUBLIC_FPP_RATES_{date}.zip` | `PUBLIC_FPP_RATES_\d{8}\.zip` | `PUBLIC_FPP_RATES_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/FPPRATES/` | `PUBLIC_FPP_RATES_{timestamp}_{aemo_id}.zip` | `PUBLIC_FPP_RATES_\d{12}_\d{16}\.zip` | `PUBLIC_FPP_RATES_202604181435_0000000513537497.zip` | 577 | 2026-04-18 | 2026-04-20 |

### `Reports` · `FPPRUN`

_2 pattern rows, 952 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/FPPRUN/` | `PUBLIC_FPP_RUN_{date}.zip` | `PUBLIC_FPP_RUN_\d{8}\.zip` | `PUBLIC_FPP_RUN_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/FPPRUN/` | `PUBLIC_FPP_RUN_{timestamp}_{aemo_id}.zip` | `PUBLIC_FPP_RUN_\d{12}_\d{16}\.zip` | `PUBLIC_FPP_RUN_202604181435_0000000513537494.zip` | 577 | 2026-04-18 | 2026-04-20 |

### `Reports` · `FPP_HIST_REG_PERF`

_1 pattern row, 49 files (snapshot), observed 2025-06-12 → 2026-04-18 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/FPP_HIST_REG_PERF/` | `PUBLIC_FPP_HIST_REGION_PERFORMANCE_{datetime}_{aemo_id}.zip` | `PUBLIC_FPP_HIST_REGION_PERFORMANCE_\d{14}_\d{16}\.zip` | `PUBLIC_FPP_HIST_REGION_PERFORMANCE_20250517180634_0000000463700812.zip` | 49 | 2025-06-12 | 2026-04-18 |

### `Reports` · `GBB`

_85 pattern rows, 2416 files (snapshot), observed 2019-11-20 → 2026-04-19 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBActualFlowStorageLast{d2}.CSV` | `GasBBActualFlowStorageLast\d{2}\.CSV` | `GasBBActualFlowStorageLast31.CSV` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBActualFlowStorage.zip` | `GasBBActualFlowStorage\.zip` | `GasBBActualFlowStorage.zip` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBBasins.csv` | `GasBBBasins\.csv` | `GasBBBasins.csv` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBBlendCurtailment.CSV` | `GasBBBlendCurtailment\.CSV` | `GasBBBlendCurtailment.CSV` | 1 | 2026-04-07 | 2026-04-07 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBConnectionPointNameplateRatingFuture.CSV` | `GasBBConnectionPointNameplateRatingFuture\.CSV` | `GasBBConnectionPointNameplateRatingFuture.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBContacts.CSV` | `GasBBContacts\.CSV` | `GasBBContacts.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBDemandZonesPipelineConnectionPointMapping.csv` | `GasBBDemandZonesPipelineConnectionPointMapping\.csv` | `GasBBDemandZonesPipelineConnectionPointMapping.csv` | 1 | 2026-04-15 | 2026-04-15 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBFacilitiesFull.CSV` | `GasBBFacilitiesFull\.CSV` | `GasBBFacilitiesFull.CSV` | 1 | 2026-04-14 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBFacilities.CSV` | `GasBBFacilities\.CSV` | `GasBBFacilities.CSV` | 1 | 2026-04-15 | 2026-04-15 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBFacilityDevelopments.csv` | `GasBBFacilityDevelopments\.csv` | `GasBBFacilityDevelopments.csv` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBFieldInterestInformation.csv` | `GasBBFieldInterestInformation\.csv` | `GasBBFieldInterestInformation.csv` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBGSHGasTrades.CSV` | `GasBBGSHGasTrades\.CSV` | `GasBBGSHGasTrades.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBGasFieldInterest.csv` | `GasBBGasFieldInterest\.csv` | `GasBBGasFieldInterest.csv` | 1 | 2026-04-16 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLNGShipments.CSV` | `GasBBLNGShipments\.CSV` | `GasBBLNGShipments.CSV` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLNGTransactions.csv` | `GasBBLNGTransactions\.csv` | `GasBBLNGTransactions.csv` | 1 | 2026-02-05 | 2026-02-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLateActualFlowAndStorage.zip` | `GasBBLateActualFlowAndStorage\.zip` | `GasBBLateActualFlowAndStorage.zip` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLateNominationAndForecast.zip` | `GasBBLateNominationAndForecast\.zip` | `GasBBLateNominationAndForecast.zip` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLinepackCapacityAdequacyFullList.zip` | `GasBBLinepackCapacityAdequacyFullList\.zip` | `GasBBLinepackCapacityAdequacyFullList.zip` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLinepackCapacityAdequacyFuture.CSV` | `GasBBLinepackCapacityAdequacyFuture\.CSV` | `GasBBLinepackCapacityAdequacyFuture.CSV` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLinepackZones.CSV` | `GasBBLinepackZones\.CSV` | `GasBBLinepackZones.CSV` | 1 | 2026-04-11 | 2026-04-11 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBLocationsList.CSV` | `GasBBLocationsList\.CSV` | `GasBBLocationsList.CSV` | 1 | 2026-04-10 | 2026-04-10 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBMediumTermCapacityOutlookFuture.csv` | `GasBBMediumTermCapacityOutlookFuture\.csv` | `GasBBMediumTermCapacityOutlookFuture.csv` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBMediumTermCapacityOutlook.csv` | `GasBBMediumTermCapacityOutlook\.csv` | `GasBBMediumTermCapacityOutlook.csv` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBMissingActualFlowAndStorage.CSV` | `GasBBMissingActualFlowAndStorage\.CSV` | `GasBBMissingActualFlowAndStorage.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBMissingNominationAndForecast.zip` | `GasBBMissingNominationAndForecast\.zip` | `GasBBMissingNominationAndForecast.zip` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBNTLngFlow.CSV` | `GasBBNTLngFlow\.CSV` | `GasBBNTLngFlow.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBNameplateRatingCurrent.csv` | `GasBBNameplateRatingCurrent\.csv` | `GasBBNameplateRatingCurrent.csv` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBNameplateRating.zip` | `GasBBNameplateRating\.zip` | `GasBBNameplateRating.zip` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBNodesAndConnectionPointsFull.CSV` | `GasBBNodesAndConnectionPointsFull\.CSV` | `GasBBNodesAndConnectionPointsFull.CSV` | 1 | 2026-04-13 | 2026-04-13 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBNodesAndConnectionPoints.CSV` | `GasBBNodesAndConnectionPoints\.CSV` | `GasBBNodesAndConnectionPoints.CSV` | 1 | 2026-04-10 | 2026-04-10 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBNominationAndForecastNext{d1}.CSV` | `GasBBNominationAndForecastNext\d{1}\.CSV` | `GasBBNominationAndForecastNext7.CSV` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBNominationAndForecast.zip` | `GasBBNominationAndForecast\.zip` | `GasBBNominationAndForecast.zip` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBParticipants.CSV` | `GasBBParticipants\.CSV` | `GasBBParticipants.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBPipelineConnectionFlowLast{d2}.CSV` | `GasBBPipelineConnectionFlowLast\d{2}\.CSV` | `GasBBPipelineConnectionFlowLast31.CSV` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBPipelineConnectionFlow_{year1}_{year2}.zip` | `GasBBPipelineConnectionFlow_\d{4}_\d{4}\.zip` | `GasBBPipelineConnectionFlow_2018_2023.zip` | 2 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBPipelineNilQualitySubmission.CSV` | `GasBBPipelineNilQualitySubmission\.CSV` | `GasBBPipelineNilQualitySubmission.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBReservesAndResources.csv` | `GasBBReservesAndResources\.csv` | `GasBBReservesAndResources.csv` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShippersFullList.CSV` | `GasBBShippersFullList\.CSV` | `GasBBShippersFullList.CSV` | 1 | 2026-04-14 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShippersList.CSV` | `GasBBShippersList\.CSV` | `GasBBShippersList.CSV` | 1 | 2026-04-11 | 2026-04-11 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermCapacityOutlookFuture.CSV` | `GasBBShortTermCapacityOutlookFuture\.CSV` | `GasBBShortTermCapacityOutlookFuture.CSV` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermCapacityOutlook.CSV` | `GasBBShortTermCapacityOutlook\.CSV` | `GasBBShortTermCapacityOutlook.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermSwapTransactionsNSW.CSV` | `GasBBShortTermSwapTransactionsNSW\.CSV` | `GasBBShortTermSwapTransactionsNSW.CSV` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermSwapTransactionsNT.CSV` | `GasBBShortTermSwapTransactionsNT\.CSV` | `GasBBShortTermSwapTransactionsNT.CSV` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermSwapTransactionsQLD.CSV` | `GasBBShortTermSwapTransactionsQLD\.CSV` | `GasBBShortTermSwapTransactionsQLD.CSV` | 1 | 2026-04-16 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermSwapTransactionsSA.CSV` | `GasBBShortTermSwapTransactionsSA\.CSV` | `GasBBShortTermSwapTransactionsSA.CSV` | 1 | 2026-04-16 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermSwapTransactionsTAS.CSV` | `GasBBShortTermSwapTransactionsTAS\.CSV` | `GasBBShortTermSwapTransactionsTAS.CSV` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermSwapTransactionsVIC.CSV` | `GasBBShortTermSwapTransactionsVIC\.CSV` | `GasBBShortTermSwapTransactionsVIC.CSV` | 1 | 2026-04-16 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermTransactionsNSW.CSV` | `GasBBShortTermTransactionsNSW\.CSV` | `GasBBShortTermTransactionsNSW.CSV` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermTransactionsNT.CSV` | `GasBBShortTermTransactionsNT\.CSV` | `GasBBShortTermTransactionsNT.CSV` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermTransactionsQLD.CSV` | `GasBBShortTermTransactionsQLD\.CSV` | `GasBBShortTermTransactionsQLD.CSV` | 1 | 2026-04-16 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermTransactionsSA.CSV` | `GasBBShortTermTransactionsSA\.CSV` | `GasBBShortTermTransactionsSA.CSV` | 1 | 2026-04-17 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermTransactionsTAS.CSV` | `GasBBShortTermTransactionsTAS\.CSV` | `GasBBShortTermTransactionsTAS.CSV` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBShortTermTransactionsVIC.CSV` | `GasBBShortTermTransactionsVIC\.CSV` | `GasBBShortTermTransactionsVIC.CSV` | 1 | 2026-04-16 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBUncontractedCapacityOutlookFullList.csv` | `GasBBUncontractedCapacityOutlookFullList\.csv` | `GasBBUncontractedCapacityOutlookFullList.csv` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBBUncontractedCapacityOutlookFuture.csv` | `GasBBUncontractedCapacityOutlookFuture\.csv` | `GasBBUncontractedCapacityOutlookFuture.csv` | 1 | 2026-04-18 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBB{d1}PSensitivies.csv` | `GasBB\d{1}PSensitivies\.csv` | `GasBB2PSensitivies.csv` | 1 | 2026-04-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/` | `GasBB{d1}PSensitivies_{date}.csv` | `GasBB\d{1}PSensitivies_\d{8}\.csv` | `GasBB2PSensitivies_20230705.csv` | 12 | 2023-07-05 | 2026-04-05 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBActualFlowStorageLast{d2}.CSV` | `GasBBActualFlowStorageLast\d{2}\.CSV` | `GasBBActualFlowStorageLast31.CSV` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBActualFlowStorageLast{d2}_{datetime}.CSV` | `GasBBActualFlowStorageLast\d{2}_\d{14}\.CSV` | `GasBBActualFlowStorageLast31_20250930111016.CSV` | 20 | 2025-09-30 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBActualFlowStorage.zip` | `GasBBActualFlowStorage\.zip` | `GasBBActualFlowStorage.zip` | 1 | 2025-08-28 | 2025-08-28 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBFacilityDevelopments.csv` | `GasBBFacilityDevelopments\.csv` | `GasBBFacilityDevelopments.csv` | 1 | 2026-01-23 | 2026-01-23 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBFacilityDevelopments_{datetime}.csv` | `GasBBFacilityDevelopments_\d{14}\.csv` | `GasBBFacilityDevelopments_20251028023042.csv` | 17 | 2025-10-28 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBLinepackCapacityAdequacyFuture.CSV` | `GasBBLinepackCapacityAdequacyFuture\.CSV` | `GasBBLinepackCapacityAdequacyFuture.CSV` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBLinepackCapacityAdequacyFuture_{datetime}.CSV` | `GasBBLinepackCapacityAdequacyFuture_\d{14}\.CSV` | `GasBBLinepackCapacityAdequacyFuture_20250930111729.CSV` | 20 | 2025-09-30 | 2026-01-23 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBMediumTermCapacityOutlookFuture.csv` | `GasBBMediumTermCapacityOutlookFuture\.csv` | `GasBBMediumTermCapacityOutlookFuture.csv` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBMediumTermCapacityOutlookFuture_{datetime}.csv` | `GasBBMediumTermCapacityOutlookFuture_\d{14}\.csv` | `GasBBMediumTermCapacityOutlookFuture_20250429095518.csv` | 21 | 2025-04-29 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBNameplateRatingCurrent.csv` | `GasBBNameplateRatingCurrent\.csv` | `GasBBNameplateRatingCurrent.csv` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBNameplateRatingCurrent_{datetime}.csv` | `GasBBNameplateRatingCurrent_\d{14}\.csv` | `GasBBNameplateRatingCurrent_20251028023825.csv` | 18 | 2025-10-28 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBNominationAndForecastNext{d1}.CSV` | `GasBBNominationAndForecastNext\d{1}\.CSV` | `GasBBNominationAndForecastNext7.CSV` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBNominationAndForecastNext{d1}_{datetime}.CSV` | `GasBBNominationAndForecastNext\d{1}_\d{14}\.CSV` | `GasBBNominationAndForecastNext7_20250930111730.CSV` | 18 | 2025-09-30 | 2026-01-23 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBPipelineConnectionFlowLast{d2}.CSV` | `GasBBPipelineConnectionFlowLast\d{2}\.CSV` | `GasBBPipelineConnectionFlowLast31.CSV` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBPipelineConnectionFlowLast{d2}_{datetime}.CSV` | `GasBBPipelineConnectionFlowLast\d{2}_\d{14}\.CSV` | `GasBBPipelineConnectionFlowLast31_20251028023829.CSV` | 23 | 2025-10-28 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBPipelineConnectionFlow_{year1}_{year2}.zip` | `GasBBPipelineConnectionFlow_\d{4}_\d{4}\.zip` | `GasBBPipelineConnectionFlow_2018_2023.zip` | 1 | 2024-06-15 | 2024-06-15 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBPipelineConnectionFlow_{year1}_{year2}_{datetime}.zip` | `GasBBPipelineConnectionFlow_\d{4}_\d{4}_\d{14}\.zip` | `GasBBPipelineConnectionFlow_2018_2023_20240616211808.zip` | 410 | 2024-06-16 | 2025-08-28 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBReservesAndResources.csv` | `GasBBReservesAndResources\.csv` | `GasBBReservesAndResources.csv` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBReservesAndResources_{datetime}.csv` | `GasBBReservesAndResources_\d{14}\.csv` | `GasBBReservesAndResources_20251028023045.csv` | 19 | 2025-10-28 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBShortTermCapacityOutlookFuture.CSV` | `GasBBShortTermCapacityOutlookFuture\.CSV` | `GasBBShortTermCapacityOutlookFuture.CSV` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBShortTermCapacityOutlookFuture_{datetime}.CSV` | `GasBBShortTermCapacityOutlookFuture_\d{14}\.CSV` | `GasBBShortTermCapacityOutlookFuture_20250912222127.CSV` | 19 | 2025-09-12 | 2026-01-23 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBShortTermCapacityOutlook.CSV` | `GasBBShortTermCapacityOutlook\.CSV` | `GasBBShortTermCapacityOutlook.CSV` | 1 | 2025-12-06 | 2025-12-06 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBUncontractedCapacityOutlookFuture.csv` | `GasBBUncontractedCapacityOutlookFuture\.csv` | `GasBBUncontractedCapacityOutlookFuture.csv` | 1 | 2026-03-08 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/DUPLICATE/` | `GasBBUncontractedCapacityOutlookFuture_{datetime}.csv` | `GasBBUncontractedCapacityOutlookFuture_\d{14}\.csv` | `GasBBUncontractedCapacityOutlookFuture_20251028023835.csv` | 19 | 2025-10-28 | 2026-03-08 |
| `CURRENT` | `/Reports/CURRENT/GBB/ForecastUtilisation/` | `GBB_ForecastUtilisation.CSV` | `GBB_ForecastUtilisation\.CSV` | `GBB_ForecastUtilisation.CSV` | 1 | 2026-04-19 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/GBB/ForecastUtilisation/` | `GBB_ForecastUtilisation_{date}.CSV` | `GBB_ForecastUtilisation_\d{8}\.CSV` | `GBB_ForecastUtilisation_20210804.CSV` | 1720 | 2021-08-04 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/GBB/GBB_PIPELINE_CONNECTION_FLOW/` | `GASBB_PIPELINE_CONNECTION_FLOW_{year}.zip` | `GASBB_PIPELINE_CONNECTION_FLOW_\d{4}\.zip` | `GASBB_PIPELINE_CONNECTION_FLOW_2019.zip` | 8 | 2021-07-27 | 2026-04-18 |
| `CURRENT` | `/Reports/CURRENT/GBB/GBB_PIPELINE_CONNECTION_FLOW/` | `PipelineConnectionFlow_History.csv` | `PipelineConnectionFlow_History\.csv` | `PipelineConnectionFlow_History.csv` | 1 | 2019-11-20 | 2019-11-20 |

### `Reports` · `GSH`

_26 pattern rows, 979 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/Benchmark_Price/` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_{date}.zip` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_\d{8}\.zip` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_AUCTION_CURTAILMENT_NOTICE/` | `PUBLIC_AUCTIONCURTAILMENTNOTICE _{date}.zip` | `PUBLIC_AUCTIONCURTAILMENTNOTICE\ _\d{8}\.zip` | `PUBLIC_AUCTIONCURTAILMENTNOTICE _20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_AUCTION_PRICE_VOLUME/` | `PUBLIC_AUCTIONPRICEVOLUME_{date}.zip` | `PUBLIC_AUCTIONPRICEVOLUME_\d{8}\.zip` | `PUBLIC_AUCTIONPRICEVOLUME_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_AUCTION_QUANTITIES/` | `PUBLIC_AUCTIONQUANTITIES_{date}.zip` | `PUBLIC_AUCTIONQUANTITIES_\d{8}\.zip` | `PUBLIC_AUCTIONQUANTITIES_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_CAPACITY_TRANSACTION/` | `PUBLIC_SECONDARYCAPACITYTRADES_{date}.zip` | `PUBLIC_SECONDARYCAPACITYTRADES_\d{8}\.zip` | `PUBLIC_SECONDARYCAPACITYTRADES_20260101.zip` | 1 | 2026-02-02 | 2026-02-02 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_CAPACITY_TRANSFER_AUCTION_NOTICE/` | `PUBLIC_CAPACITYTRANSFERAUCTIONNOTICE_{date}.zip` | `PUBLIC_CAPACITYTRANSFERAUCTIONNOTICE_\d{8}\.zip` | `PUBLIC_CAPACITYTRANSFERAUCTIONNOTICE_20260301.zip` | 1 | 2026-04-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_Daily_Trans_Summary/` | `PUBLIC_DAILYTRANSACTIONSUMMARY_{date}.zip` | `PUBLIC_DAILYTRANSACTIONSUMMARY_\d{8}\.zip` | `PUBLIC_DAILYTRANSACTIONSUMMARY_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_Historical_Trans_Summary/` | `PUBLIC_HISTORICALTRANSACTIONSUMMARY_{date}.zip` | `PUBLIC_HISTORICALTRANSACTIONSUMMARY_\d{8}\.zip` | `PUBLIC_HISTORICALTRANSACTIONSUMMARY_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_Participants/` | `PUBLIC_REGISTEREDPARTICIPANTS_{date}.zip` | `PUBLIC_REGISTEREDPARTICIPANTS_\d{8}\.zip` | `PUBLIC_REGISTEREDPARTICIPANTS_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_REGISTERED_FACILITIES/` | `PUBLIC_REGISTEREDFACILITIES_{date}.zip` | `PUBLIC_REGISTEREDFACILITIES_\d{8}\.zip` | `PUBLIC_REGISTEREDFACILITIES_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_REGISTERED_SERVICE_POINTS/` | `PUBLIC_REGISTEREDSERVICEPOINTS_{date}.zip` | `PUBLIC_REGISTEREDSERVICEPOINTS_\d{8}\.zip` | `PUBLIC_REGISTEREDSERVICEPOINTS_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_REVISED_AUCTION_QUANTITIES/` | `PUBLIC_REVISEDAUCTIONQUANTITIES_{date}.zip` | `PUBLIC_REVISEDAUCTIONQUANTITIES_\d{8}\.zip` | `PUBLIC_REVISEDAUCTIONQUANTITIES_20250401.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/GSH/GSH_ZONE_CURTAILMENT_INFORMATION/` | `PUBLIC_ZONECURTAILMENTINFORMATION_{date}.zip` | `PUBLIC_ZONECURTAILMENTINFORMATION_\d{8}\.zip` | `PUBLIC_ZONECURTAILMENTINFORMATION_20260301.zip` | 1 | 2026-04-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/GSH/Benchmark_Price/` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_{date}.zip` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_\d{8}\.zip` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_20260115.zip` | 96 | 2026-01-15 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/GSH/Benchmark_Price/` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_{date}_{aemo_id}.zip` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_\d{8}_\d{16}\.zip` | `PUBLIC_WALLUMBILLABENCHMARKPRICE_20260115_0000000498888759.zip` | 94 | 2026-01-15 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_AUCTION_CURTAILMENT_NOTICE/` | `PUBLIC_AUCTIONCURTAILMENTNOTICE_{date}_{aemo_id}.zip` | `PUBLIC_AUCTIONCURTAILMENTNOTICE_\d{8}_\d{16}\.zip` | `PUBLIC_AUCTIONCURTAILMENTNOTICE_20260126_0000000500497250.zip` | 161 | 2026-01-26 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_AUCTION_PRICE_VOLUME/` | `PUBLIC_AUCTIONPRICEVOLUME_{date}_{aemo_id}.zip` | `PUBLIC_AUCTIONPRICEVOLUME_\d{8}_\d{16}\.zip` | `PUBLIC_AUCTIONPRICEVOLUME_20260115_0000000498872444.zip` | 95 | 2026-01-15 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_AUCTION_QUANTITIES/` | `PUBLIC_AUCTIONQUANTITIES_{date}_{aemo_id}.zip` | `PUBLIC_AUCTIONQUANTITIES_\d{8}_\d{16}\.zip` | `PUBLIC_AUCTIONQUANTITIES_20260115_0000000498869206.zip` | 95 | 2026-01-15 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_CAPACITY_TRANSFER_AUCTION_NOTICE/` | `PUBLIC_CAPACITYTRANSFERAUCTIONNOTICE_{date}_{aemo_id}.zip` | `PUBLIC_CAPACITYTRANSFERAUCTIONNOTICE_\d{8}_\d{16}\.zip` | `PUBLIC_CAPACITYTRANSFERAUCTIONNOTICE_20260310_0000000507230799.zip` | 2 | 2026-03-10 | 2026-03-11 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_Daily_Trans_Summary/` | `PUBLIC_DAILYTRANSACTIONSUMMARY_{date}_{aemo_id}.zip` | `PUBLIC_DAILYTRANSACTIONSUMMARY_\d{8}_\d{16}\.zip` | `PUBLIC_DAILYTRANSACTIONSUMMARY_20260115_0000000498889279.zip` | 95 | 2026-01-15 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_Historical_Trans_Summary/` | `PUBLIC_HISTORICALTRANSACTIONSUMMARY_{date}_{aemo_id}.zip` | `PUBLIC_HISTORICALTRANSACTIONSUMMARY_\d{8}_\d{16}\.zip` | `PUBLIC_HISTORICALTRANSACTIONSUMMARY_20260115_0000000498889282.zip` | 95 | 2026-01-15 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_Participants/` | `PUBLIC_REGISTEREDPARTICIPANTS_{date}_{aemo_id}.zip` | `PUBLIC_REGISTEREDPARTICIPANTS_\d{8}_\d{16}\.zip` | `PUBLIC_REGISTEREDPARTICIPANTS_20260119_0000000499458542.zip` | 14 | 2026-01-19 | 2026-04-02 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_REGISTERED_FACILITIES/` | `PUBLIC_REGISTEREDFACILITIES_{date}_{aemo_id}.zip` | `PUBLIC_REGISTEREDFACILITIES_\d{8}_\d{16}\.zip` | `PUBLIC_REGISTEREDFACILITIES_20260201_0000000501355053.zip` | 3 | 2026-02-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_REGISTERED_SERVICE_POINTS/` | `PUBLIC_REGISTEREDSERVICEPOINTS_{date}_{aemo_id}.zip` | `PUBLIC_REGISTEREDSERVICEPOINTS_\d{8}_\d{16}\.zip` | `PUBLIC_REGISTEREDSERVICEPOINTS_20260201_0000000501355054.zip` | 3 | 2026-02-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_REVISED_AUCTION_QUANTITIES/` | `PUBLIC_REVISEDAUCTIONQUANTITIES_{date}_{aemo_id}.zip` | `PUBLIC_REVISEDAUCTIONQUANTITIES_\d{8}_\d{16}\.zip` | `PUBLIC_REVISEDAUCTIONQUANTITIES_20260116_0000000499005383.zip` | 95 | 2026-01-16 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/GSH/GSH_ZONE_CURTAILMENT_INFORMATION/` | `PUBLIC_ZONECURTAILMENTINFORMATION_{date}_{aemo_id}.zip` | `PUBLIC_ZONECURTAILMENTINFORMATION_\d{8}_\d{16}\.zip` | `PUBLIC_ZONECURTAILMENTINFORMATION_20260315_0000000508038113.zip` | 8 | 2026-03-15 | 2026-04-01 |

### `Reports` · `Gas_Supply_Guarantee`

_6 pattern rows, 6 files (snapshot), observed 2018-08-07 → 2022-09-30 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Gas_Supply_Guarantee/` | `Gas Supply Guarantee - Outcome Notice - {d2} Juy {year}.pdf` | `Gas\ Supply\ Guarantee\ \-\ Outcome\ Notice\ \-\ \d{2}\ Juy\ \d{4}\.pdf` | `Gas Supply Guarantee - Outcome Notice - 19 Juy 2022.pdf` | 1 | 2022-07-20 | 2022-07-20 |
| `CURRENT` | `/Reports/CURRENT/Gas_Supply_Guarantee/` | `Gas Supply Guarantee - Outcome Notice - {d2} Sept {year} .pdf` | `Gas\ Supply\ Guarantee\ \-\ Outcome\ Notice\ \-\ \d{2}\ Sept\ \d{4}\ \.pdf` | `Gas Supply Guarantee - Outcome Notice - 30 Sept 2022 .pdf` | 1 | 2022-09-30 | 2022-09-30 |
| `CURRENT` | `/Reports/CURRENT/Gas_Supply_Guarantee/` | `Gas Supply Guarantee - Trigger Notice - {d2} Juy {year}.pdf` | `Gas\ Supply\ Guarantee\ \-\ Trigger\ Notice\ \-\ \d{2}\ Juy\ \d{4}\.pdf` | `Gas Supply Guarantee - Trigger Notice - 19 Juy 2022.pdf` | 1 | 2022-07-19 | 2022-07-19 |
| `CURRENT` | `/Reports/CURRENT/Gas_Supply_Guarantee/` | `Gas Supply Shortfall Event Notification - {yearmonth}.pdf` | `Gas\ Supply\ Shortfall\ Event\ Notification\ \-\ \d{6}\.pdf` | `Gas Supply Shortfall Event Notification - 010622.pdf` | 1 | 2022-06-01 | 2022-06-01 |
| `CURRENT` | `/Reports/CURRENT/Gas_Supply_Guarantee/` | `Gas Supply Shortfall Event Outcome - {yearmonth}.pdf` | `Gas\ Supply\ Shortfall\ Event\ Outcome\ \-\ \d{6}\.pdf` | `Gas Supply Shortfall Event Outcome - 020622.pdf` | 1 | 2022-06-02 | 2022-06-02 |
| `CURRENT` | `/Reports/CURRENT/Gas_Supply_Guarantee/` | `test.txt` | `test\.txt` | `test.txt` | 1 | 2018-08-07 | 2018-08-07 |

### `Reports` · `HighImpactOutages`

_4 pattern rows, 707 files (snapshot), observed 2017-04-19 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/HighImpactOutages/` | `High_Impact_Outages_{date}.csv` | `High_Impact_Outages_\d{8}\.csv` | `High_Impact_Outages_20210830.csv` | 217 | 2021-08-30 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/HighImpactOutages/` | `High_Impact_Outages_{date}.pdf` | `High_Impact_Outages_\d{8}\.pdf` | `High_Impact_Outages_20170410.pdf` | 467 | 2017-04-19 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/HighImpactOutages/` | `High_Impact_Outages_{date}.xlsx` | `High_Impact_Outages_\d{8}\.xlsx` | `High_Impact_Outages_20220228.xlsx` | 21 | 2022-02-28 | 2025-02-24 |
| `CURRENT` | `/Reports/CURRENT/HighImpactOutages/` | `{d1}_days_High_Impact_Outages_{date}.csv` | `\d{1}_days_High_Impact_Outages_\d{8}\.csv` | `7_days_High_Impact_Outages_20230116.csv` | 2 | 2022-11-28 | 2023-01-16 |

### `Reports` · `HistDemand`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/HistDemand/` | `PUBLIC_HISTDEMAND_{date}.zip` | `PUBLIC_HISTDEMAND_\d{8}\.zip` | `PUBLIC_HISTDEMAND_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/HistDemand/` | `PUBLIC_HISTDEMAND_{date}_{aemo_id}.zip` | `PUBLIC_HISTDEMAND_\d{8}_\d{16}\.zip` | `PUBLIC_HISTDEMAND_20260219_0000000504260404.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `IBEI`

_1 pattern row, 12 files (snapshot), observed 2016-09-29 → 2026-04-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/IBEI/` | `IBEI_SUMMARY_RESULTS_{year}.CSV` | `IBEI_SUMMARY_RESULTS_\d{4}\.CSV` | `IBEI_SUMMARY_RESULTS_2015.CSV` | 12 | 2016-09-29 | 2026-04-17 |

### `Reports` · `MCCDispatch`

_3 pattern rows, 955 files (snapshot), observed 2017-03-25 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/MCCDispatch/` | `PUBLIC_MCCDISPATCH_{date}.zip` | `PUBLIC_MCCDISPATCH_\d{8}\.zip` | `PUBLIC_MCCDISPATCH_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/MCCDispatch/` | `PUBLIC_MCCDISPATCH_{timestamp}_{aemo_id}.zip` | `PUBLIC_MCCDISPATCH_\d{12}_\d{16}\.zip` | `PUBLIC_MCCDISPATCH_202604181445_0000000513537683.zip` | 577 | 2026-04-18 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/MCCDispatch/DUPLICATE/` | `PUBLIC_MCCDISPATCH_{timestamp}_{aemo_id}.zip` | `PUBLIC_MCCDISPATCH_\d{12}_\d{16}\.zip` | `PUBLIC_MCCDISPATCH_201703251930_0000000282129407.zip` | 3 | 2017-03-25 | 2026-03-03 |

### `Reports` · `MMSDataModelReport`

_82 pattern rows, 374 files (snapshot), observed 2019-04-17 → 2026-04-14 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/` | `Blue_Theme.css` | `Blue_Theme\.css` | `Blue_Theme.css` | 1 | 2019-04-18 | 2019-04-18 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/` | `Electricity Data Model Report.htm` | `Electricity\ Data\ Model\ Report\.htm` | `Electricity Data Model Report.htm` | 1 | 2025-08-01 | 2025-08-01 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/` | `Header_Blue.html` | `Header_Blue\.html` | `Header_Blue.html` | 1 | 2025-04-29 | 2025-04-29 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Blue_Theme.css` | `Blue_Theme\.css` | `Blue_Theme.css` | 1 | 2025-08-01 | 2025-08-01 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Elec{d1}.htm` | `Elec\d{1}\.htm` | `Elec1.htm` | 9 | 2025-08-01 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Elec{d1}.png` | `Elec\d{1}\.png` | `Elec0.png` | 10 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Elec{d2}.htm` | `Elec\d{2}\.htm` | `Elec10.htm` | 73 | 2025-08-01 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Elec{d2}.png` | `Elec\d{2}\.png` | `Elec10.png` | 23 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Elec{d2}_{d1}.htm` | `Elec\d{2}_\d{1}\.htm` | `Elec13_1.htm` | 48 | 2024-11-06 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Elec{d21}_{d22}.htm` | `Elec\d{2}_\d{2}\.htm` | `Elec79_10.htm` | 3 | 2024-11-06 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Electricity Data Model Report.htm` | `Electricity\ Data\ Model\ Report\.htm` | `Electricity Data Model Report.htm` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Electricity Data Model Report_toc.htm` | `Electricity\ Data\ Model\ Report_toc\.htm` | `Electricity Data Model Report_toc.htm` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Header_Blue.html` | `Header_Blue\.html` | `Header_Blue.html` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `Thumbs.db` | `Thumbs\.db` | `Thumbs.db` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `i_blank.gif` | `i_blank\.gif` | `i_blank.gif` | 1 | 2025-08-01 | 2025-08-01 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `i_colpse.gif` | `i_colpse\.gif` | `i_colpse.gif` | 1 | 2025-08-01 | 2025-08-01 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `i_corner.gif` | `i_corner\.gif` | `i_corner.gif` | 1 | 2025-08-01 | 2025-08-01 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `i_expand.gif` | `i_expand\.gif` | `i_expand.gif` | 1 | 2025-08-01 | 2025-08-01 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `i_normal.gif` | `i_normal\.gif` | `i_normal.gif` | 1 | 2025-08-01 | 2025-08-01 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/` | `menutree.js` | `menutree\.js` | `menutree.js` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `Chevron-down.png` | `Chevron\-down\.png` | `Chevron-down.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `Chevron-up.png` | `Chevron\-up\.png` | `Chevron-up.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `Thumbs.db` | `Thumbs\.db` | `Thumbs.db` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `arrow-left-inverse.png` | `arrow\-left\-inverse\.png` | `arrow-left-inverse.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `arrow-left.png` | `arrow\-left\.png` | `arrow-left.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `arrow-right-inverse.png` | `arrow\-right\-inverse\.png` | `arrow-right-inverse.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `arrow-right.png` | `arrow\-right\.png` | `arrow-right.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `browser.png` | `browser\.png` | `browser.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `buttonHover.png` | `buttonHover\.png` | `buttonHover.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `button.png` | `button\.png` | `button.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Blue_Theme_files/` | `vssver{d1}.scc` | `vssver\d{1}\.scc` | `vssver2.scc` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Header_Blue_files/` | `Thumbs.db` | `Thumbs\.db` | `Thumbs.db` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Header_Blue_files/` | `aemo-logo.svg` | `aemo\-logo\.svg` | `aemo-logo.svg` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Header_Blue_files/` | `aemo.png` | `aemo\.png` | `aemo.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Header_Blue_files/` | `aemo_logo.png` | `aemo_logo\.png` | `aemo_logo.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Header_Blue_files/` | `arches.png` | `arches\.png` | `arches.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Header_Blue_files/` | `header.png` | `header\.png` | `header.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Electricity Data Model Report_files/Header_Blue_files/` | `vssver{d1}.scc` | `vssver\d{1}\.scc` | `vssver2.scc` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `Thumbs.db` | `Thumbs\.db` | `Thumbs.db` | 1 | 2019-04-17 | 2019-04-17 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `aemo-logo.svg` | `aemo\-logo\.svg` | `aemo-logo.svg` | 1 | 2025-04-29 | 2025-04-29 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `aemo.png` | `aemo\.png` | `aemo.png` | 1 | 2019-04-17 | 2019-04-17 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `aemo_logo.png` | `aemo_logo\.png` | `aemo_logo.png` | 1 | 2019-04-17 | 2019-04-17 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `arches.png` | `arches\.png` | `arches.png` | 1 | 2025-04-29 | 2025-04-29 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `arches{d2}.png` | `arches\d{2}\.png` | `arches11.png` | 1 | 2019-04-17 | 2019-04-17 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `header.png` | `header\.png` | `header.png` | 1 | 2019-04-17 | 2019-04-17 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Electricity/Header_Blue_files/` | `vssver{d1}.scc` | `vssver\d{1}\.scc` | `vssver2.scc` | 1 | 2025-04-29 | 2025-04-29 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/` | `Gas Data Model Report.htm` | `Gas\ Data\ Model\ Report\.htm` | `Gas Data Model Report.htm` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Blue_Theme.css` | `Blue_Theme\.css` | `Blue_Theme.css` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas Data Model Report.htm` | `Gas\ Data\ Model\ Report\.htm` | `Gas Data Model Report.htm` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas Data Model Report_toc.htm` | `Gas\ Data\ Model\ Report_toc\.htm` | `Gas Data Model Report_toc.htm` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas_{d1}.htm` | `Gas_\d{1}\.htm` | `Gas_1.htm` | 9 | 2025-02-26 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas_{d1}.png` | `Gas_\d{1}\.png` | `Gas_0.png` | 2 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas_{d11}_{d12}.htm` | `Gas_\d{1}_\d{1}\.htm` | `Gas_3_1.htm` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas_{d2}.htm` | `Gas_\d{2}\.htm` | `Gas_10.htm` | 90 | 2025-02-26 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas_{d2}_{d1}.htm` | `Gas_\d{2}_\d{1}\.htm` | `Gas_67_1.htm` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas_{d3}.htm` | `Gas_\d{3}\.htm` | `Gas_100.htm` | 34 | 2025-02-26 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Gas_{d3}_{d1}.htm` | `Gas_\d{3}_\d{1}\.htm` | `Gas_133_1.htm` | 2 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `Header_Blue.html` | `Header_Blue\.html` | `Header_Blue.html` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `i_blank.gif` | `i_blank\.gif` | `i_blank.gif` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `i_colpse.gif` | `i_colpse\.gif` | `i_colpse.gif` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `i_corner.gif` | `i_corner\.gif` | `i_corner.gif` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `i_expand.gif` | `i_expand\.gif` | `i_expand.gif` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `i_normal.gif` | `i_normal\.gif` | `i_normal.gif` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/` | `menutree.js` | `menutree\.js` | `menutree.js` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `Chevron-down.png` | `Chevron\-down\.png` | `Chevron-down.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `Chevron-up.png` | `Chevron\-up\.png` | `Chevron-up.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `arrow-left-inverse.png` | `arrow\-left\-inverse\.png` | `arrow-left-inverse.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `arrow-left.png` | `arrow\-left\.png` | `arrow-left.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `arrow-right-inverse.png` | `arrow\-right\-inverse\.png` | `arrow-right-inverse.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `arrow-right.png` | `arrow\-right\.png` | `arrow-right.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `browser.png` | `browser\.png` | `browser.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `buttonHover.png` | `buttonHover\.png` | `buttonHover.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `button.png` | `button\.png` | `button.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Blue_Theme_files/` | `vssver{d1}.scc` | `vssver\d{1}\.scc` | `vssver2.scc` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Header_Blue_files/` | `aemo-logo.svg` | `aemo\-logo\.svg` | `aemo-logo.svg` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Header_Blue_files/` | `aemo.png` | `aemo\.png` | `aemo.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Header_Blue_files/` | `aemo_logo.png` | `aemo_logo\.png` | `aemo_logo.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Header_Blue_files/` | `arches.png` | `arches\.png` | `arches.png` | 1 | 2025-02-26 | 2025-02-26 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Header_Blue_files/` | `header.png` | `header\.png` | `header.png` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/Gas/Gas Data Model Report_files/Header_Blue_files/` | `vssver{d1}.scc` | `vssver\d{1}\.scc` | `vssver2.scc` | 1 | 2025-11-19 | 2025-11-19 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/PDRCONFIG/` | `PREPROD_PUBLIC_PDR_CONFIG_FULL.zip` | `PREPROD_PUBLIC_PDR_CONFIG_FULL\.zip` | `PREPROD_PUBLIC_PDR_CONFIG_FULL.zip` | 1 | 2026-04-14 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/MMSDataModelReport/PDRCONFIG/` | `PROD_PUBLIC_PDR_CONFIG_FULL.zip` | `PROD_PUBLIC_PDR_CONFIG_FULL\.zip` | `PROD_PUBLIC_PDR_CONFIG_FULL.zip` | 1 | 2025-11-19 | 2025-11-19 |

### `Reports` · `MTPASA_DUIDAvailability`

_2 pattern rows, 7429 files (snapshot), observed 2020-08-20 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/MTPASA_DUIDAvailability/` | `PUBLIC_MTPASADUIDAVAILABILITY_{date}.zip` | `PUBLIC_MTPASADUIDAVAILABILITY_\d{8}\.zip` | `PUBLIC_MTPASADUIDAVAILABILITY_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/MTPASA_DUIDAvailability/` | `PUBLIC_MTPASADUIDAVAILABILITY_{timestamp}_{aemo_id}.zip` | `PUBLIC_MTPASADUIDAVAILABILITY_\d{12}_\d{16}\.zip` | `PUBLIC_MTPASADUIDAVAILABILITY_202008201200_0000000327353179.zip` | 7417 | 2020-08-20 | 2026-04-20 |

### `Reports` · `MTPASA_RegionAvailability`

_2 pattern rows, 221 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/MTPASA_RegionAvailability/` | `PUBLIC_MTPASAREGIONAVAILABILITY_{date}.zip` | `PUBLIC_MTPASAREGIONAVAILABILITY_\d{8}\.zip` | `PUBLIC_MTPASAREGIONAVAILABILITY_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/MTPASA_RegionAvailability/` | `PUBLIC_MTPASAREGIONAVAILABILITY_{timestamp}_{aemo_id}.zip` | `PUBLIC_MTPASAREGIONAVAILABILITY_\d{12}_\d{16}\.zip` | `PUBLIC_MTPASAREGIONAVAILABILITY_202602191500_0000000504193752.zip` | 209 | 2026-02-19 | 2026-04-20 |

### `Reports` · `Marginal_Loss_Factors`

_1 pattern row, 2015 files (snapshot), observed 2020-10-14 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Marginal_Loss_Factors/` | `MLF_{datetime}.zip` | `MLF_\d{14}\.zip` | `MLF_20201014090001.zip` | 2015 | 2020-10-14 | 2026-04-20 |

### `Reports` · `Market_Notice`

_1 pattern row, 8033 files (snapshot), observed 2026-02-19 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Market_Notice/` | `NEMITWEB{d1}_MKTNOTICE_{date}.R{yearmonth}` | `NEMITWEB\d{1}_MKTNOTICE_\d{8}\.R\d{6}` | `NEMITWEB1_MKTNOTICE_20260219.R133781` | 8033 | 2026-02-19 | 2026-04-20 |

### `Reports` · `Medium_Term_PASA_Reports`

_2 pattern rows, 20 files (snapshot), observed 2025-05-01 → 2026-04-14 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Medium_Term_PASA_Reports/` | `PUBLIC_MTPASA_{date}.zip` | `PUBLIC_MTPASA_\d{8}\.zip` | `PUBLIC_MTPASA_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Medium_Term_PASA_Reports/` | `PUBLIC_MTPASA_{timestamp}_{aemo_id}.zip` | `PUBLIC_MTPASA_\d{12}_\d{16}\.zip` | `PUBLIC_MTPASA_202602230100_0000000504937712.zip` | 8 | 2026-02-24 | 2026-04-14 |

### `Reports` · `Mktsusp_Pricing`

_1 pattern row, 9 files (snapshot), observed 2026-02-21 → 2026-04-19 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Mktsusp_Pricing/` | `PUBLIC_MARKET_SUSPENSION_SCHEDULE_{datetime}_{aemo_id}.zip` | `PUBLIC_MARKET_SUSPENSION_SCHEDULE_\d{14}_\d{16}\.zip` | `PUBLIC_MARKET_SUSPENSION_SCHEDULE_20260221235515_0000000504549958.zip` | 9 | 2026-02-21 | 2026-04-19 |

### `Reports` · `NEXT_DAY_AVAIL_SUBMISS_CLUSTER`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/NEXT_DAY_AVAIL_SUBMISS_CLUSTER/` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_CLUSTER_{date}.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_CLUSTER_\d{8}\.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_CLUSTER_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/NEXT_DAY_AVAIL_SUBMISS_CLUSTER/` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_CLUSTER_{datetime}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_CLUSTER_\d{14}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_CLUSTER_20260220041111_0000000504273701.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `NEXT_DAY_AVAIL_SUBMISS_DAY`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/NEXT_DAY_AVAIL_SUBMISS_DAY/` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_DAY_{date}.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_DAY_\d{8}\.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_DAY_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/NEXT_DAY_AVAIL_SUBMISS_DAY/` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_DAY_{datetime}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_DAY_\d{14}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_AVAIL_SUBMISS_DAY_20260220041114_0000000504273703.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `NEXT_DAY_MCCDISPATCH`

_2 pattern rows, 72 files (snapshot), observed 2025-05-02 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/NEXT_DAY_MCCDISPATCH/` | `PUBLIC_NEXT_DAY_MCCDISPATCH_{date}.zip` | `PUBLIC_NEXT_DAY_MCCDISPATCH_\d{8}\.zip` | `PUBLIC_NEXT_DAY_MCCDISPATCH_20250302.zip` | 12 | 2025-05-02 | 2026-04-02 |
| `CURRENT` | `/Reports/CURRENT/NEXT_DAY_MCCDISPATCH/` | `PUBLIC_NEXT_DAY_MCCDISPATCH_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_MCCDISPATCH_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_MCCDISPATCH_20260219_0000000504277197.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Network`

_2 pattern rows, 404 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Network/` | `PUBLIC_NETWORK_{date}.zip` | `PUBLIC_NETWORK_\d{8}\.zip` | `PUBLIC_NETWORK_20250328.zip` | 54 | 2025-04-11 | 2026-04-17 |
| `CURRENT` | `/Reports/CURRENT/Network/` | `PUBLIC_NETWORK_{datetime}_{aemo_id}.zip` | `PUBLIC_NETWORK_\d{14}_\d{16}\.zip` | `PUBLIC_NETWORK_20260413150023_0000000512728647.zip` | 350 | 2026-04-13 | 2026-04-20 |

### `Reports` · `Next_Day_Actual_Gen`

_4 pattern rows, 74 files (snapshot), observed 2016-09-29 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Actual_Gen/` | `NEW TEXT DOCUMENT.TXT` | `NEW\ TEXT\ DOCUMENT\.TXT` | `NEW TEXT DOCUMENT.TXT` | 1 | 2016-09-29 | 2016-09-29 |
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Actual_Gen/` | `NEXT_DAY_ACTUAL_GEN_{date}.zip` | `NEXT_DAY_ACTUAL_GEN_\d{8}\.zip` | `NEXT_DAY_ACTUAL_GEN_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Actual_Gen/` | `_ZA{d5}` | `_ZA\d{5}` | `_ZA01492` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_Actual_Gen/` | `PUBLIC_NEXT_DAY_ACTUAL_GEN_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_ACTUAL_GEN_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_ACTUAL_GEN_20260219_0000000504273700.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Next_Day_Dispatch`

_2 pattern rows, 407 files (snapshot), observed 2025-03-22 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Dispatch/` | `PUBLIC_NEXT_DAY_DISPATCH_{date}.zip` | `PUBLIC_NEXT_DAY_DISPATCH_\d{8}\.zip` | `PUBLIC_NEXT_DAY_DISPATCH_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_Dispatch/` | `PUBLIC_NEXT_DAY_DISPATCH_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_DISPATCH_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_DISPATCH_20250321_0000000455927547.zip` | 395 | 2025-03-22 | 2026-04-20 |

### `Reports` · `Next_Day_Intermittent_DS`

_3 pattern rows, 75 files (snapshot), observed 2020-03-14 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Intermittent_DS/` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_{date}.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_\d{8}\.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_Intermittent_DS/` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_20260219_0000000504273708.zip` | 60 | 2026-02-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_Intermittent_DS/DUPLICATE/` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_DS_20200313_0000000320315048.zip` | 3 | 2020-03-14 | 2020-10-20 |

### `Reports` · `Next_Day_Intermittent_Gen_Scada`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Intermittent_Gen_Scada/` | `PUBLIC_NEXT_DAY_INTERMITTENT_GEN_SCADA_{date}.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_GEN_SCADA_\d{8}\.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_GEN_SCADA_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_Intermittent_Gen_Scada/` | `PUBLIC_NEXT_DAY_INTERMITTENT_GEN_SCADA_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_GEN_SCADA_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_INTERMITTENT_GEN_SCADA_20260219_0000000504273709.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Next_Day_Offer_Energy_SPARSE`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Offer_Energy_SPARSE/` | `PUBLIC_NEXT_DAY_OFFER_ENERGY_SPARSE_{date}.zip` | `PUBLIC_NEXT_DAY_OFFER_ENERGY_SPARSE_\d{8}\.zip` | `PUBLIC_NEXT_DAY_OFFER_ENERGY_SPARSE_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_Offer_Energy_SPARSE/` | `PUBLIC_NEXT_DAY_OFFER_ENERGY_SPARSE_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_OFFER_ENERGY_SPARSE_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_OFFER_ENERGY_SPARSE_20260219_0000000504277199.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Next_Day_Offer_FCAS_SPARSE`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_Offer_FCAS_SPARSE/` | `PUBLIC_NEXT_DAY_OFFER_FCAS_SPARSE_{date}.zip` | `PUBLIC_NEXT_DAY_OFFER_FCAS_SPARSE_\d{8}\.zip` | `PUBLIC_NEXT_DAY_OFFER_FCAS_SPARSE_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_Offer_FCAS_SPARSE/` | `PUBLIC_NEXT_DAY_OFFER_FCAS_SPARSE_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_OFFER_FCAS_SPARSE_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_OFFER_FCAS_SPARSE_20260219_0000000504277203.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Next_Day_PreDispatch`

_3 pattern rows, 78 files (snapshot), observed 2017-08-31 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_PreDispatch/` | `PUBLIC_NEXT_DAY_PREDISPATCH_{date}.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_\d{8}\.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_20250302.zip` | 12 | 2025-05-02 | 2026-04-02 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_PreDispatch/` | `PUBLIC_NEXT_DAY_PREDISPATCH_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_20260219_0000000504277206.zip` | 60 | 2026-02-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_PreDispatch/DUPLICATE/` | `PUBLIC_NEXT_DAY_PREDISPATCH_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_20170830_0000000286881960.zip` | 6 | 2017-08-31 | 2020-08-23 |

### `Reports` · `Next_Day_PreDispatchD`

_2 pattern rows, 72 files (snapshot), observed 2025-05-02 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Next_Day_PreDispatchD/` | `PUBLIC_NEXT_DAY_PREDISPATCH_D_{date}.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_D_\d{8}\.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_D_20250302.zip` | 12 | 2025-05-02 | 2026-04-02 |
| `CURRENT` | `/Reports/CURRENT/Next_Day_PreDispatchD/` | `PUBLIC_NEXT_DAY_PREDISPATCH_D_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_D_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_PREDISPATCH_D_20260219_0000000504277207.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `Next_Day_Trading`

_1 pattern row, 1703 files (snapshot), observed 2017-02-02 → 2021-10-01 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Next_Day_Trading/` | `PUBLIC_NEXT_DAY_TRADING_{date}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_TRADING_\d{8}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_TRADING_20170201_0000000280588679.zip` | 1703 | 2017-02-02 | 2021-10-01 |

### `Reports` · `Operational_Demand`

_13 pattern rows, 11926 files (snapshot), observed 2025-04-13 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand/ACTUAL_DAILY/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_{date}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_\d{8}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand/ACTUAL_DAILY_AREA/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_AREA_{date}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_AREA_\d{8}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_AREA_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand/ACTUAL_HH/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_{date}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_\d{8}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_20250330.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand/ACTUAL_HH_AREA/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_AREA_{date}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_AREA_\d{8}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_AREA_20250401.zip` | 53 | 2025-04-15 | 2026-04-14 |
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand/FORECAST_HH/` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_{date}.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_\d{8}\.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_20250330.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand/FORECAST_HH_AREA/` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_AREA_{date}.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_AREA_\d{8}\.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_AREA_20250401.zip` | 53 | 2025-04-15 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand/ACTUAL_{d1}MIN/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_{d1}MIN_{timestamp}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_\d{1}MIN_\d{12}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_5MIN_202604191435_20260419150543.zip` | 48 | 2026-04-19 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand/ACTUAL_DAILY/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_{date}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_\d{8}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_20260219_20260220044001.zip` | 60 | 2026-02-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand/ACTUAL_DAILY_AREA/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_AREA_{timestamp}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_AREA_\d{12}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_DAILY_AREA_202602190400_20260220044001.zip` | 60 | 2026-02-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand/ACTUAL_HH/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_{timestamp}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_\d{12}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_202602191500_20260219150017.zip` | 2880 | 2026-02-19 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand/ACTUAL_HH_AREA/` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_AREA_{timestamp}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_AREA_\d{12}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEMAND_HH_AREA_202602191500_20260219150017.zip` | 2880 | 2026-02-19 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand/FORECAST_HH/` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_{timestamp}_{datetime}.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_\d{12}_\d{14}\.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_202602191530_20260219150220.zip` | 2880 | 2026-02-19 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand/FORECAST_HH_AREA/` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_AREA_{timestamp}_{datetime}.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_AREA_\d{12}_\d{14}\.zip` | `PUBLIC_FORECAST_OPERATIONAL_DEMAND_HH_AREA_202602191530_20260219150220.zip` | 2880 | 2026-02-19 | 2026-04-20 |

### `Reports` · `Operational_Demand_Less_SNSG`

_5 pattern rows, 21900 files (snapshot), observed 2025-01-30 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand_Less_SNSG/ACTUAL_DAILY/` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_DAILY_{date}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_DAILY_\d{8}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_DAILY_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `ARCHIVE` | `/Reports/ARCHIVE/Operational_Demand_Less_SNSG/ACTUAL_HH/` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_HH_{date}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_HH_\d{8}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_HH_20250401.zip` | 53 | 2025-04-15 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand_Less_SNSG/ACTUAL_DAILY/` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_DAILY_{timestamp}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_DAILY_\d{12}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_DAILY_202501300400_20250131044000.zip` | 445 | 2025-01-31 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand_Less_SNSG/ACTUAL_HH/` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_HH_{timestamp}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_HH_\d{12}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_HH_202501301100_20250130110005.zip` | 21389 | 2025-01-30 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Operational_Demand_Less_SNSG/ACTUAL_UPDATE/` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_UPDATE_{timestamp}_{datetime}.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_UPDATE_\d{12}_\d{14}\.zip` | `PUBLIC_ACTUAL_OPERATIONAL_DEM_LESS_SNSG_UPDATE_202501310900_20250131115609.zip` | 1 | 2025-01-31 | 2025-01-31 |

### `Reports` · `P5MINFCST`

_3 pattern rows, 953 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/P{d1}MINFCST/` | `PUBLIC_P{d1}MINFCST_{date}.zip` | `PUBLIC_P\d{1}MINFCST_\d{8}\.zip` | `PUBLIC_P5MINFCST_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/P{d1}MINFCST/` | `PUBLIC_P{d1}MINFCST_{timestamp}_{aemo_id}.zip` | `PUBLIC_P\d{1}MINFCST_\d{12}_\d{16}\.zip` | `PUBLIC_P5MINFCST_202604181442_0000000513537812.zip` | 577 | 2026-04-18 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/P{d1}MINFCST/DUPLICATE/` | `PUBLIC_P{d1}MINFCST_{timestamp}_{aemo_id}.zip` | `PUBLIC_P\d{1}MINFCST_\d{12}_\d{16}\.zip` | `PUBLIC_P5MINFCST_202603031336_0000000506102444.zip` | 1 | 2026-03-03 | 2026-03-03 |

### `Reports` · `P5_Reports`

_3 pattern rows, 952 files (snapshot), observed 2025-04-11 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/P{d1}_Reports/` | `PUBLIC_P{d1}MIN_{date}.zip` | `PUBLIC_P\d{1}MIN_\d{8}\.zip` | `PUBLIC_P5MIN_20250409.zip` | 375 | 2025-04-11 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/P{d1}_Reports/` | `PUBLIC_P{d1}MIN_{timestamp}_{datetime}.zip` | `PUBLIC_P\d{1}MIN_\d{12}_\d{14}\.zip` | `PUBLIC_P5MIN_202604181445_20260418144212.zip` | 576 | 2026-04-18 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/P{d1}_Reports/DUPLICATE/` | `PUBLIC_P{d1}MIN_{timestamp}_{datetime}.zip` | `PUBLIC_P\d{1}MIN_\d{12}_\d{14}\.zip` | `PUBLIC_P5MIN_202603031345_20260303134116.zip` | 1 | 2026-03-03 | 2026-03-03 |

### `Reports` · `PD7Day`

_1 pattern row, 180 files (snapshot), observed 2026-02-19 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/PD{d1}Day/` | `PUBLIC_PD{d1}DAY_{datetime}_{aemo_id}.zip` | `PUBLIC_PD\d{1}DAY_\d{14}_\d{16}\.zip` | `PUBLIC_PD7DAY_20260219174025_0000000504209569.zip` | 180 | 2026-02-19 | 2026-04-20 |

### `Reports` · `PDPASA`

_2 pattern rows, 726 files (snapshot), observed 2025-04-17 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/PDPASA/` | `PUBLIC_PDPASA_{date}.zip` | `PUBLIC_PDPASA_\d{8}\.zip` | `PUBLIC_PDPASA_20250403.zip` | 53 | 2025-04-17 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/PDPASA/` | `PUBLIC_PDPASA_{timestamp}_{aemo_id}.zip` | `PUBLIC_PDPASA_\d{12}_\d{16}\.zip` | `PUBLIC_PDPASA_202604061500_0000000511603075.zip` | 673 | 2026-04-06 | 2026-04-20 |

### `Reports` · `PDPASA_DUIDAVAILABILITY`

_1 pattern row, 8 files (snapshot), observed 2025-09-01 → 2026-04-01 (snapshot) · **anomaly:** casing_mismatch_vs_sibling_tier_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/PDPASA_DUIDAVAILABILITY/` | `PUBLIC_PDPASA_DUIDAVAILABILITY_{date}.zip` | `PUBLIC_PDPASA_DUIDAVAILABILITY_\d{8}\.zip` | `PUBLIC_PDPASA_DUIDAVAILABILITY_20250701.zip` | 8 | 2025-09-01 | 2026-04-01 |

### `Reports` · `PDPASA_DUIDAvailability`

_1 pattern row, 2880 files (snapshot), observed 2026-02-19 → 2026-04-20 (snapshot) · **anomaly:** casing_mismatch_vs_sibling_tier_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/PDPASA_DUIDAvailability/` | `PUBLIC_PDPASA_DUIDAVAILABILITY_{timestamp}_{aemo_id}.zip` | `PUBLIC_PDPASA_DUIDAVAILABILITY_\d{12}_\d{16}\.zip` | `PUBLIC_PDPASA_DUIDAVAILABILITY_202602191530_0000000504191990.zip` | 2880 | 2026-02-19 | 2026-04-20 |

### `Reports` · `PREDISPATCHFCST`

_2 pattern rows, 726 files (snapshot), observed 2025-04-13 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/PREDISPATCHFCST/` | `PUBLIC_PREDISPATCHFCST_{date}.zip` | `PUBLIC_PREDISPATCHFCST_\d{8}\.zip` | `PUBLIC_PREDISPATCHFCST_20250330.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/PREDISPATCHFCST/` | `PUBLIC_PREDISPATCHFCST_{timestamp}_{aemo_id}.zip` | `PUBLIC_PREDISPATCHFCST_\d{12}_\d{16}\.zip` | `PUBLIC_PREDISPATCHFCST_202604061530_0000000511606184.zip` | 672 | 2026-04-06 | 2026-04-20 |

### `Reports` · `PasaSnap`

_1 pattern row, 1 files (snapshot), observed 2016-09-29 → 2016-09-29 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/PasaSnap/` | `LATEST{d1}DAYOUTLOOK.PDF` | `LATEST\d{1}DAYOUTLOOK\.PDF` | `LATEST7DAYOUTLOOK.PDF` | 1 | 2016-09-29 | 2016-09-29 |

### `Reports` · `PredispatchIS_Reports`

_3 pattern rows, 736 files (snapshot), observed 2016-10-23 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/PredispatchIS_Reports/` | `PUBLIC_PREDISPATCHIS_{date1}_{date2}.zip` | `PUBLIC_PREDISPATCHIS_\d{8}_\d{8}\.zip` | `PUBLIC_PREDISPATCHIS_20250330_20250405.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/PredispatchIS_Reports/` | `PUBLIC_PREDISPATCHIS_{timestamp}_{datetime}.zip` | `PUBLIC_PREDISPATCHIS_\d{12}_\d{14}\.zip` | `PUBLIC_PREDISPATCHIS_202604061500_20260406143242.zip` | 673 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/PredispatchIS_Reports/DUPLICATE/` | `PUBLIC_PREDISPATCHIS_{timestamp}_{datetime}.zip` | `PUBLIC_PREDISPATCHIS_\d{12}_\d{14}\.zip` | `PUBLIC_PREDISPATCHIS_201610231430_20161023140222.zip` | 9 | 2016-10-23 | 2019-07-11 |

### `Reports` · `Predispatch_IRSR`

_2 pattern rows, 726 files (snapshot), observed 2025-04-13 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Predispatch_IRSR/` | `PUBLIC_PREDISPATCH_IRSR_{date1}_{date2}.zip` | `PUBLIC_PREDISPATCH_IRSR_\d{8}_\d{8}\.zip` | `PUBLIC_PREDISPATCH_IRSR_20250330_20250405.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/Predispatch_IRSR/` | `PUBLIC_PREDISPATCH_IRSR_{timestamp}_{aemo_id}.zip` | `PUBLIC_PREDISPATCH_IRSR_\d{12}_\d{16}\.zip` | `PUBLIC_PREDISPATCH_IRSR_202604061530_0000000511606148.zip` | 672 | 2026-04-06 | 2026-04-20 |

### `Reports` · `Predispatch_Reports`

_2 pattern rows, 726 files (snapshot), observed 2025-04-13 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Predispatch_Reports/` | `PUBLIC_PREDISPATCH_{date1}_{date2}.zip` | `PUBLIC_PREDISPATCH_\d{8}_\d{8}\.zip` | `PUBLIC_PREDISPATCH_20250330_20250405.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/Predispatch_Reports/` | `PUBLIC_PREDISPATCH_{timestamp}_{datetime}_LEGACY.zip` | `PUBLIC_PREDISPATCH_\d{12}_\d{14}_LEGACY\.zip` | `PUBLIC_PREDISPATCH_202604061530_20260406150239_LEGACY.zip` | 672 | 2026-04-06 | 2026-04-20 |

### `Reports` · `Predispatch_Sensitivities`

_3 pattern rows, 727 files (snapshot), observed 2025-04-16 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Predispatch_Sensitivities/` | `PUBLIC_PREDISPATCH_SENSITIVITIES_{date1}_{date2}.zip` | `PUBLIC_PREDISPATCH_SENSITIVITIES_\d{8}_\d{8}\.zip` | `PUBLIC_PREDISPATCH_SENSITIVITIES_20250402_20250408.zip` | 53 | 2025-04-16 | 2026-04-15 |
| `CURRENT` | `/Reports/CURRENT/Predispatch_Sensitivities/` | `PUBLIC_PREDISPATCH_SENSITIVITIES_{datetime}_{aemo_id}.zip` | `PUBLIC_PREDISPATCH_SENSITIVITIES_\d{14}_\d{16}\.zip` | `PUBLIC_PREDISPATCH_SENSITIVITIES_20260406144127_0000000511603692.zip` | 673 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Predispatch_Sensitivities/DUPLICATE/` | `PUBLIC_PREDISPATCH_SENSITIVITIES_{datetime}_{aemo_id}.zip` | `PUBLIC_PREDISPATCH_SENSITIVITIES_\d{14}_\d{16}\.zip` | `PUBLIC_PREDISPATCH_SENSITIVITIES_20260303134002_0000000506103520.zip` | 1 | 2026-03-03 | 2026-03-03 |

### `Reports` · `Public_Prices`

_2 pattern rows, 72 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Public_Prices/` | `PUBLIC_PRICES_{date}.zip` | `PUBLIC_PRICES_\d{8}\.zip` | `PUBLIC_PRICES_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Public_Prices/` | `PUBLIC_PRICES_{timestamp}_{datetime}.zip` | `PUBLIC_PRICES_\d{12}_\d{14}\.zip` | `PUBLIC_PRICES_202602190000_20260220040502.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `ROOFTOP_PV`

_12 pattern rows, 4350 files (snapshot), observed 2025-04-15 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/ROOFTOP_PV/ACTUAL/` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_{date}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_\d{8}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_20250403.zip` | 53 | 2025-04-17 | 2026-04-16 |
| `ARCHIVE` | `/Reports/ARCHIVE/ROOFTOP_PV/ACTUAL/` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_{date}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_\d{8}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_20250403.zip` | 53 | 2025-04-17 | 2026-04-16 |
| `ARCHIVE` | `/Reports/ARCHIVE/ROOFTOP_PV/ACTUAL_AREA/` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_AREA_{date}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_AREA_\d{8}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_AREA_20250401.zip` | 53 | 2025-04-15 | 2026-04-14 |
| `ARCHIVE` | `/Reports/ARCHIVE/ROOFTOP_PV/ACTUAL_AREA/` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_AREA_{date}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_AREA_\d{8}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_AREA_20250401.zip` | 53 | 2025-04-15 | 2026-04-14 |
| `ARCHIVE` | `/Reports/ARCHIVE/ROOFTOP_PV/FORECAST/` | `PUBLIC_ROOFTOP_PV_FORECAST_{date}.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_\d{8}\.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_20250403.zip` | 53 | 2025-04-17 | 2026-04-16 |
| `ARCHIVE` | `/Reports/ARCHIVE/ROOFTOP_PV/FORECAST_AREA/` | `PUBLIC_ROOFTOP_PV_FORECAST_AREA_{date}.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_AREA_\d{8}\.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_AREA_20250401.zip` | 53 | 2025-04-15 | 2026-04-14 |
| `CURRENT` | `/Reports/CURRENT/ROOFTOP_PV/ACTUAL/` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_{datetime}_{aemo_id}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_\d{14}_\d{16}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_20260406150000_0000000511605825.zip` | 672 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ROOFTOP_PV/ACTUAL/` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_{datetime}_{aemo_id}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_\d{14}_\d{16}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_20260406150000_0000000511605827.zip` | 672 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ROOFTOP_PV/ACTUAL_AREA/` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_AREA_{datetime}_{aemo_id}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_AREA_\d{14}_\d{16}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_MEASUREMENT_AREA_20260406150000_0000000511605826.zip` | 672 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ROOFTOP_PV/ACTUAL_AREA/` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_AREA_{datetime}_{aemo_id}.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_AREA_\d{14}_\d{16}\.zip` | `PUBLIC_ROOFTOP_PV_ACTUAL_SATELLITE_AREA_20260406150000_0000000511605828.zip` | 672 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ROOFTOP_PV/FORECAST/` | `PUBLIC_ROOFTOP_PV_FORECAST_{datetime}_{aemo_id}.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_\d{14}_\d{16}\.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_20260406150000_0000000511605823.zip` | 672 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/ROOFTOP_PV/FORECAST_AREA/` | `PUBLIC_ROOFTOP_PV_FORECAST_AREA_{datetime}_{aemo_id}.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_AREA_\d{14}_\d{16}\.zip` | `PUBLIC_ROOFTOP_PV_FORECAST_AREA_20260406150000_0000000511605824.zip` | 672 | 2026-04-06 | 2026-04-20 |

### `Reports` · `Regional_Summary_Report`

_1 pattern row, 224 files (snapshot), observed 2025-03-25 → 2026-04-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Regional_Summary_Report/` | `RSR_{date}.R{d3}` | `RSR_\d{8}\.R\d{3}` | `RSR_20240825.R015` | 224 | 2025-03-25 | 2026-04-17 |

### `Reports` · `SEVENDAYOUTLOOK_FULL`

_3 pattern rows, 2928 files (snapshot), observed 2017-02-06 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/SEVENDAYOUTLOOK_FULL/` | `PUBLIC_SEVENDAYOUTLOOK_FULL_{date}.zip` | `PUBLIC_SEVENDAYOUTLOOK_FULL_\d{8}\.zip` | `PUBLIC_SEVENDAYOUTLOOK_FULL_20250330.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/SEVENDAYOUTLOOK_FULL/` | `PUBLIC_SEVENDAYOUTLOOK_FULL_{datetime}_{aemo_id}.zip` | `PUBLIC_SEVENDAYOUTLOOK_FULL_\d{14}_\d{16}\.zip` | `PUBLIC_SEVENDAYOUTLOOK_FULL_20260219150518_0000000504192437.zip` | 2873 | 2026-02-19 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/SEVENDAYOUTLOOK_FULL/DUPLICATE/` | `PUBLIC_SEVENDAYOUTLOOK_FULL_{datetime}_{aemo_id}.zip` | `PUBLIC_SEVENDAYOUTLOOK_FULL_\d{14}_\d{16}\.zip` | `PUBLIC_SEVENDAYOUTLOOK_FULL_20170206123430_0000000280715734.zip` | 1 | 2017-02-06 | 2017-02-06 |

### `Reports` · `SEVENDAYOUTLOOK_PEAK`

_2 pattern rows, 2927 files (snapshot), observed 2025-04-13 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/SEVENDAYOUTLOOK_PEAK/` | `PUBLIC_SEVENDAYOUTLOOK_PEAK_{date}.zip` | `PUBLIC_SEVENDAYOUTLOOK_PEAK_\d{8}\.zip` | `PUBLIC_SEVENDAYOUTLOOK_PEAK_20250330.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/SEVENDAYOUTLOOK_PEAK/` | `PUBLIC_SEVENDAYOUTLOOK_PEAK_{datetime}_{aemo_id}.zip` | `PUBLIC_SEVENDAYOUTLOOK_PEAK_\d{14}_\d{16}\.zip` | `PUBLIC_SEVENDAYOUTLOOK_PEAK_20260219150518_0000000504192438.zip` | 2873 | 2026-02-19 | 2026-04-20 |

### `Reports` · `SRA_Bids`

_1 pattern row, 4 files (snapshot), observed 2025-06-16 → 2026-03-16 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/SRA_Bids/` | `PUBLIC_SRBID_A{yearmonth}_{datetime}.CSV` | `PUBLIC_SRBID_A\d{6}_\d{14}\.CSV` | `PUBLIC_SRBID_A202506_20250616142639.CSV` | 4 | 2025-06-16 | 2026-03-16 |

### `Reports` · `SRA_NSR_RECONCILIATION`

_1 pattern row, 4 files (snapshot), observed 2025-04-22 → 2026-01-21 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/SRA_NSR_RECONCILIATION/` | `PUBLIC_SRAFINANCIALS_RECONCILIATION_{year}_{d1}_{datetime}.zip` | `PUBLIC_SRAFINANCIALS_RECONCILIATION_\d{4}_\d{1}_\d{14}\.zip` | `PUBLIC_SRAFINANCIALS_RECONCILIATION_2025_2_20250422111540.zip` | 4 | 2025-04-22 | 2026-01-21 |

### `Reports` · `SRA_Offers`

_1 pattern row, 26 files (snapshot), observed 2019-12-17 → 2026-03-16 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/SRA_Offers/` | `PUBLIC_SROFFER_A{yearmonth}_{datetime}.CSV` | `PUBLIC_SROFFER_A\d{6}_\d{14}\.CSV` | `PUBLIC_SROFFER_A201912_20191216151208.CSV` | 26 | 2019-12-17 | 2026-03-16 |

### `Reports` · `SRA_Results`

_1 pattern row, 48 files (snapshot), observed 2025-06-16 → 2026-03-16 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/SRA_Results/` | `PUBLIC_SRRES_C{year}Q{d1}T{d2}_{d15}.csv` | `PUBLIC_SRRES_C\d{4}Q\d{1}T\d{2}_\d{15}\.csv` | `PUBLIC_SRRES_C2025Q3T12_120250616142640.csv` | 48 | 2025-06-16 | 2026-03-16 |

### `Reports` · `SSM_ENABLEMENT_COSTS`

_1 pattern row, 123 files (snapshot), observed 2025-12-02 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/SSM_ENABLEMENT_COSTS/` | `PUBLIC_NEXT_DAY_ENABLEMENT_COSTS_{date}_{yearmonth}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_ENABLEMENT_COSTS_\d{8}_\d{6}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_ENABLEMENT_COSTS_20251202_120016_0000000492027787.zip` | 123 | 2025-12-02 | 2026-04-20 |

### `Reports` · `SSM_ENABLEMENT_PERIOD`

_1 pattern row, 123 files (snapshot), observed 2025-12-02 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/SSM_ENABLEMENT_PERIOD/` | `PUBLIC_NEXT_DAY_ENABLEMENT_PERIOD_{date}_{yearmonth}_{aemo_id}.zip` | `PUBLIC_NEXT_DAY_ENABLEMENT_PERIOD_\d{8}_\d{6}_\d{16}\.zip` | `PUBLIC_NEXT_DAY_ENABLEMENT_PERIOD_20251202_120016_0000000492027788.zip` | 123 | 2025-12-02 | 2026-04-20 |

### `Reports` · `STPASA_DUIDAVAILABILITY`

_1 pattern row, 8 files (snapshot), observed 2025-09-01 → 2026-04-01 (snapshot) · **anomaly:** casing_mismatch_vs_sibling_tier_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/STPASA_DUIDAVAILABILITY/` | `PUBLIC_STPASA_DUIDAVAILABILITY_{date}.zip` | `PUBLIC_STPASA_DUIDAVAILABILITY_\d{8}\.zip` | `PUBLIC_STPASA_DUIDAVAILABILITY_20250701.zip` | 8 | 2025-09-01 | 2026-04-01 |

### `Reports` · `STPASA_DUIDAvailability`

_1 pattern row, 1436 files (snapshot), observed 2026-02-19 → 2026-04-20 (snapshot) · **anomaly:** casing_mismatch_vs_sibling_tier_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/STPASA_DUIDAvailability/` | `PUBLIC_STPASA_DUIDAVAILABILITY_{timestamp}_{aemo_id}.zip` | `PUBLIC_STPASA_DUIDAVAILABILITY_\d{12}_\d{16}\.zip` | `PUBLIC_STPASA_DUIDAVAILABILITY_202602191500_0000000504191689.zip` | 1436 | 2026-02-19 | 2026-04-20 |

### `Reports` · `STTM`

_94 pattern rows, 174 files (snapshot), observed 2016-09-29 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/STTM/` | `CURRENTDAY.ZIP` | `CURRENTDAY\.ZIP` | `CURRENTDAY.ZIP` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `DAY{d2}.ZIP` | `DAY\d{2}\.ZIP` | `DAY01.ZIP` | 31 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}B_V{d1}_STTM_PRICES_RPT_{d2}.CSV` | `INT\d{3}B_V\d{1}_STTM_PRICES_RPT_\d{2}\.CSV` | `INT685B_V1_STTM_PRICES_RPT_13.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_ALLOCATION_WARNING_LIMIT_THRESHOLDS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_ALLOCATION_WARNING_LIMIT_THRESHOLDS_RPT_\d{1}\.CSV` | `INT688_V1_ALLOCATION_WARNING_LIMIT_THRESHOLDS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_BID_OFFER_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_BID_OFFER_RPT_\d{1}\.CSV` | `INT659_V1_BID_OFFER_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_CONTINGENCY_GAS_BIDS_AND_OFFERS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_CONTINGENCY_GAS_BIDS_AND_OFFERS_RPT_\d{1}\.CSV` | `INT660_V1_CONTINGENCY_GAS_BIDS_AND_OFFERS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_CUMULATIVE_PRICE_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_CUMULATIVE_PRICE_RPT_\d{1}\.CSV` | `INT672_V1_CUMULATIVE_PRICE_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_DAILY_PROVISIONAL_CAPACITY_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_DAILY_PROVISIONAL_CAPACITY_RPT_\d{1}\.CSV` | `INT681_V1_DAILY_PROVISIONAL_CAPACITY_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_DAILY_PROVISIONAL_MOS_ALLOCATION_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_DAILY_PROVISIONAL_MOS_ALLOCATION_RPT_\d{1}\.CSV` | `INT664_V1_DAILY_PROVISIONAL_MOS_ALLOCATION_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_DEFAULT_ALLOCATION_NOTICE_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_DEFAULT_ALLOCATION_NOTICE_RPT_\d{1}\.CSV` | `INT675_V1_DEFAULT_ALLOCATION_NOTICE_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_DEVIATION_PRICE_DATA_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_DEVIATION_PRICE_DATA_RPT_\d{1}\.CSV` | `INT690_V1_DEVIATION_PRICE_DATA_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_DP_FLAG_DATA_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_DP_FLAG_DATA_RPT_\d{1}\.CSV` | `INT680_V1_DP_FLAG_DATA_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_EXPOST_FACILITY_ALLOCATION_QUANTITY_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_EXPOST_FACILITY_ALLOCATION_QUANTITY_RPT_\d{1}\.CSV` | `INT689_V1_EXPOST_FACILITY_ALLOCATION_QUANTITY_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_EX_ANTE_MARKET_PRICE_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_EX_ANTE_MARKET_PRICE_RPT_\d{1}\.CSV` | `INT651_V1_EX_ANTE_MARKET_PRICE_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_EX_ANTE_PIPELINE_PRICE_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_EX_ANTE_PIPELINE_PRICE_RPT_\d{1}\.CSV` | `INT653_V3_EX_ANTE_PIPELINE_PRICE_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_EX_ANTE_SCHEDULE_QUANTITY_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_EX_ANTE_SCHEDULE_QUANTITY_RPT_\d{1}\.CSV` | `INT652_V1_EX_ANTE_SCHEDULE_QUANTITY_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_EX_POST_MARKET_DATA_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_EX_POST_MARKET_DATA_RPT_\d{1}\.CSV` | `INT657_V2_EX_POST_MARKET_DATA_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_FACILITY_HUB_CAPACITY_DATA_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_FACILITY_HUB_CAPACITY_DATA_RPT_\d{1}\.CSV` | `INT687_V1_FACILITY_HUB_CAPACITY_DATA_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_HUB_FACILITY_DEFINITION_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_HUB_FACILITY_DEFINITION_RPT_\d{1}\.CSV` | `INT671_V1_HUB_FACILITY_DEFINITION_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_LATEST_ALLOCATION_QUANTITY_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_LATEST_ALLOCATION_QUANTITY_RPT_\d{1}\.CSV` | `INT658_V1_LATEST_ALLOCATION_QUANTITY_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_MARKET_NOTICE_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_MARKET_NOTICE_RPT_\d{1}\.CSV` | `INT666_V1_MARKET_NOTICE_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_MARKET_PARAMETERS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_MARKET_PARAMETERS_RPT_\d{1}\.CSV` | `INT667_V1_MARKET_PARAMETERS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_MOS_STACK_DATA_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_MOS_STACK_DATA_RPT_\d{1}\.CSV` | `INT665_V1_MOS_STACK_DATA_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_NET_MARKET_BALANCE_DAILY_AMOUNTS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_NET_MARKET_BALANCE_DAILY_AMOUNTS_RPT_\d{1}\.CSV` | `INT678_V1_NET_MARKET_BALANCE_DAILY_AMOUNTS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_NET_MARKET_BALANCE_SETTLEMENT_AMOUNTS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_NET_MARKET_BALANCE_SETTLEMENT_AMOUNTS_RPT_\d{1}\.CSV` | `INT679_V1_NET_MARKET_BALANCE_SETTLEMENT_AMOUNTS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_PROVISIONAL_DEVIATION_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_PROVISIONAL_DEVIATION_RPT_\d{1}\.CSV` | `INT662_V1_PROVISIONAL_DEVIATION_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_PROVISIONAL_MARKET_PRICE_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_PROVISIONAL_MARKET_PRICE_RPT_\d{1}\.CSV` | `INT654_V1_PROVISIONAL_MARKET_PRICE_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_PROVISIONAL_PIPELINE_DATA_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_PROVISIONAL_PIPELINE_DATA_RPT_\d{1}\.CSV` | `INT656_V2_PROVISIONAL_PIPELINE_DATA_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_PROVISIONAL_SCHEDULE_QUANTITY_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_PROVISIONAL_SCHEDULE_QUANTITY_RPT_\d{1}\.CSV` | `INT655_V1_PROVISIONAL_SCHEDULE_QUANTITY_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_PROVISIONAL_USED_MOS_STEPS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_PROVISIONAL_USED_MOS_STEPS_RPT_\d{1}\.CSV` | `INT683_V1_PROVISIONAL_USED_MOS_STEPS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_PROVISIONAL_VARIATION_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_PROVISIONAL_VARIATION_RPT_\d{1}\.CSV` | `INT663_V1_PROVISIONAL_VARIATION_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_REGISTERED_PARTICIPANTS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_REGISTERED_PARTICIPANTS_RPT_\d{1}\.CSV` | `INT670_V1_REGISTERED_PARTICIPANTS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_ROLLING_AVERAGE_PRICE_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_ROLLING_AVERAGE_PRICE_RPT_\d{1}\.CSV` | `INT676_V1_ROLLING_AVERAGE_PRICE_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_SCHEDULE_LOG_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_SCHEDULE_LOG_RPT_\d{1}\.CSV` | `INT668_V1_SCHEDULE_LOG_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_SETTLEMENT_MOS_AND_CAPACITY_DATA_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_SETTLEMENT_MOS_AND_CAPACITY_DATA_RPT_\d{1}\.CSV` | `INT682_V1_SETTLEMENT_MOS_AND_CAPACITY_DATA_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_SETTLEMENT_USED_MOS_STEPS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_SETTLEMENT_USED_MOS_STEPS_RPT_\d{1}\.CSV` | `INT684_V1_SETTLEMENT_USED_MOS_STEPS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_SETTLEMENT_VERSION_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_SETTLEMENT_VERSION_RPT_\d{1}\.CSV` | `INT669_V1_SETTLEMENT_VERSION_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_STTM_CTP_REGISTER_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_STTM_CTP_REGISTER_RPT_\d{1}\.CSV` | `INT691_V1_STTM_CTP_REGISTER_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d1}_STTM_PRICES_RPT_{d2}.CSV` | `INT\d{3}_V\d{1}_STTM_PRICES_RPT_\d{2}\.CSV` | `INT685_V1_STTM_PRICES_RPT_13.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `INT{d3}_V{d11}_TOTAL_CONTINGENCY_BID_OFFER_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_TOTAL_CONTINGENCY_BID_OFFER_RPT_\d{1}\.CSV` | `INT673_V1_TOTAL_CONTINGENCY_BID_OFFER_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_sttm_prices.htm` | `int\d{3}_sttm_prices\.htm` | `int685_sttm_prices.htm` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_sttm_prices_original.htm` | `int\d{3}_sttm_prices_original\.htm` | `int685_sttm_prices_original.htm` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_v{d11}_allocation_quantity_rpt_{d12}.csv` | `int\d{3}_v\d{1}_allocation_quantity_rpt_\d{1}\.csv` | `int658_v1_allocation_quantity_rpt_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d31}_v{d11}_bid_offer_-&#x{d12}b;{yearmonth}CC-BDB{d13}-{d21}B{d14}-B{d32}-A{d22}ADA{d15}AB{d33}&#x{d16}d;-v{d7}.csv` | `int\d{3}_v\d{1}_bid_offer_\-\&\#x\d{1}b;\d{6}CC\-BDB\d{1}\-\d{2}B\d{1}\-B\d{3}\-A\d{2}ADA\d{1}AB\d{3}\&\#x\d{1}d;\-v\d{7}\.csv` | `int659_v1_bid_offer_-&#x7b;703546CC-BDB3-47B6-B705-A29ADA3AB466&#x7d;-v5318095.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_v{d11}_contingency_gas_called_scheduled_bid_offer_rpt_{d12}.csv` | `int\d{3}_v\d{1}_contingency_gas_called_scheduled_bid_offer_rpt_\d{1}\.csv` | `int661_v1_contingency_gas_called_scheduled_bid_offer_rpt_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_v{d11}_contingency_gas_price_rpt_{d12}.csv` | `int\d{3}_v\d{1}_contingency_gas_price_rpt_\d{1}\.csv` | `int677_v1_contingency_gas_price_rpt_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_v{d11}_ex_ante_pipeline_price_rpt_{d12}.csv` | `int\d{3}_v\d{1}_ex_ante_pipeline_price_rpt_\d{1}\.csv` | `int653_v1_ex_ante_pipeline_price_rpt_1.csv` | 2 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_v{d11}_ex_post_market_data_rpt_{d12}.csv` | `int\d{3}_v\d{1}_ex_post_market_data_rpt_\d{1}\.csv` | `int657_v1_ex_post_market_data_rpt_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_v{d11}_provisional_pipeline_data_rpt_{d12}.csv` | `int\d{3}_v\d{1}_provisional_pipeline_data_rpt_\d{1}\.csv` | `int656_v1_provisional_pipeline_data_rpt_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}_v{d11}_total_contingency_gas_schedules_rpt_{d12}.csv` | `int\d{3}_v\d{1}_total_contingency_gas_schedules_rpt_\d{1}\.csv` | `int674_v1_total_contingency_gas_schedules_rpt_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}b_sttm_prices.xml` | `int\d{3}b_sttm_prices\.xml` | `int685b_sttm_prices.xml` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/` | `int{d3}b_sttm_prices_original.xml` | `int\d{3}b_sttm_prices_original\.xml` | `int685b_sttm_prices_original.xml` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM CG Determination (revised) {yearmonth}.pdf` | `STTM\ CG\ Determination\ \(revised\)\ \d{6}\.pdf` | `STTM CG Determination (revised) 230715.pdf` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM CG Determination {yearmonth}.pdf` | `STTM\ CG\ Determination\ \d{6}\.pdf` | `STTM CG Determination 011016.pdf` | 5 | 2016-09-29 | 2016-11-09 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM CG Trigger Notification {yearmonth}.docx` | `STTM\ CG\ Trigger\ Notification\ \d{6}\.docx` | `STTM CG Trigger Notification 101116.docx` | 1 | 2016-11-09 | 2016-11-09 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM CG Trigger Notification {yearmonth}.pdf` | `STTM\ CG\ Trigger\ Notification\ \d{6}\.pdf` | `STTM CG Trigger Notification 011016.pdf` | 4 | 2016-09-29 | 2016-11-09 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM CG Trigger Notification {date}.pdf` | `STTM\ CG\ Trigger\ Notification\ \d{8}\.pdf` | `STTM CG Trigger Notification 24112016.pdf` | 1 | 2016-11-24 | 2016-11-24 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM Contingency Gas Determination - SYD - GD {d21}-{d22}-{year}.pdf` | `STTM\ Contingency\ Gas\ Determination\ \-\ SYD\ \-\ GD\ \d{2}\-\d{2}\-\d{4}\.pdf` | `STTM Contingency Gas Determination - SYD - GD 29-10-2023.pdf` | 1 | 2023-10-28 | 2023-10-28 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM Contingency Gas Determination - Sydney Hub - GD {d21}-{d22}-{year} .pdf` | `STTM\ Contingency\ Gas\ Determination\ \-\ Sydney\ Hub\ \-\ GD\ \d{2}\-\d{2}\-\d{4}\ \.pdf` | `STTM Contingency Gas Determination - Sydney Hub - GD 25-05-2022 .pdf` | 1 | 2022-05-25 | 2022-05-25 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM Contingency Gas Trigger Notification - SYD - GD {d21}-{d22}-{year}.pdf` | `STTM\ Contingency\ Gas\ Trigger\ Notification\ \-\ SYD\ \-\ GD\ \d{2}\-\d{2}\-\d{4}\.pdf` | `STTM Contingency Gas Trigger Notification - SYD - GD 29-10-2023.pdf` | 1 | 2023-10-28 | 2023-10-28 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM Contingency Gas Trigger Notification - Sydney Hub - GD {d21}-{d22}-{d23}.pdf` | `STTM\ Contingency\ Gas\ Trigger\ Notification\ \-\ Sydney\ Hub\ \-\ GD\ \d{2}\-\d{2}\-\d{2}\.pdf` | `STTM Contingency Gas Trigger Notification - Sydney Hub - GD 25-05-22.pdf` | 1 | 2022-05-25 | 2022-05-25 |
| `CURRENT` | `/Reports/CURRENT/STTM/Contingency_Gas/` | `STTM_CG_Determination_{yearmonth}.pdf` | `STTM_CG_Determination_\d{6}\.pdf` | `STTM_CG_Determination_241116.pdf` | 1 | 2016-11-24 | 2016-11-24 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOSEstimates_{d1}Mar_{d2}May_{year}.pdf` | `MOSEstimates_\d{1}Mar_\d{2}May_\d{4}\.pdf` | `MOSEstimates_1Mar_31May_2016.pdf` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimate Supporting_Data_Mar{d21}_to_May{d22}.xlsx` | `MOS\ Estimate\ Supporting_Data_Mar\d{2}_to_May\d{2}\.xlsx` | `MOS Estimate Supporting_Data_Mar22_to_May22.xlsx` | 1 | 2021-06-07 | 2021-06-07 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimates Data and Report - Dec {year1} to Feb {year2}.xlsx` | `MOS\ Estimates\ Data\ and\ Report\ \-\ Dec\ \d{4}\ to\ Feb\ \d{4}\.xlsx` | `MOS Estimates Data and Report - Dec 2022 to Feb 2023.xlsx` | 4 | 2022-07-28 | 2025-05-20 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimates Data and Report - Jun {year1} to Aug {year2}.xlsx` | `MOS\ Estimates\ Data\ and\ Report\ \-\ Jun\ \d{4}\ to\ Aug\ \d{4}\.xlsx` | `MOS Estimates Data and Report - Jun 2022 to Aug 2022.xlsx` | 3 | 2021-12-09 | 2025-12-24 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimates Data and Report - June {year1} to Aug {year2}.xlsx` | `MOS\ Estimates\ Data\ and\ Report\ \-\ June\ \d{4}\ to\ Aug\ \d{4}\.xlsx` | `MOS Estimates Data and Report - June 2023 to Aug 2023.xlsx` | 1 | 2022-10-28 | 2022-10-28 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimates Data and Report - June {year1} to August {year2}.xlsx` | `MOS\ Estimates\ Data\ and\ Report\ \-\ June\ \d{4}\ to\ August\ \d{4}\.xlsx` | `MOS Estimates Data and Report - June 2024 to August 2024.xlsx` | 1 | 2023-10-13 | 2023-10-13 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimates Data and Report - Mar {year1} to May {year2}.xlsx` | `MOS\ Estimates\ Data\ and\ Report\ \-\ Mar\ \d{4}\ to\ May\ \d{4}\.xlsx` | `MOS Estimates Data and Report - Mar 2023 to May 2023.xlsx` | 4 | 2022-07-28 | 2025-10-06 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimates Data and Report - Sep {year1} to Nov {year2}.xlsx` | `MOS\ Estimates\ Data\ and\ Report\ \-\ Sep\ \d{4}\ to\ Nov\ \d{4}\.xlsx` | `MOS Estimates Data and Report - Sep 2023 to Nov 2023.xlsx` | 4 | 2023-03-03 | 2026-03-06 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS Estimates Data and Report - Sept {year1} to Nov {year2}.xlsx` | `MOS\ Estimates\ Data\ and\ Report\ \-\ Sept\ \d{4}\ to\ Nov\ \d{4}\.xlsx` | `MOS Estimates Data and Report - Sept 2022 to Nov 2022.xlsx` | 1 | 2021-12-09 | 2021-12-09 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Jun_{year1}-Aug_{year2}-Supporting_Data.xlsx` | `MOS_Estimates_Jun_\d{4}\-Aug_\d{4}\-Supporting_Data\.xlsx` | `MOS_Estimates_Jun_2016-Aug_2016-Supporting_Data.xlsx` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_Dec{d21}_to_Feb{d22}.pdf` | `MOS_Estimates_Report_Dec\d{2}_to_Feb\d{2}\.pdf` | `MOS_Estimates_Report_Dec17_to_Feb18.pdf` | 1 | 2017-05-11 | 2017-05-11 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_Dec_{year1}_to_Feb_{year2}.pdf` | `MOS_Estimates_Report_Dec_\d{4}_to_Feb_\d{4}\.pdf` | `MOS_Estimates_Report_Dec_2016_to_Feb_2017.pdf` | 5 | 2016-11-04 | 2021-03-25 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_Jun_{year1}_to_Aug_{year2}.pdf` | `MOS_Estimates_Report_Jun_\d{4}_to_Aug_\d{4}\.pdf` | `MOS_Estimates_Report_Jun_2018_to_Aug_2018.pdf` | 4 | 2017-09-26 | 2020-09-24 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_June_{year1}_to_Aug_{year2}.pdf` | `MOS_Estimates_Report_June_\d{4}_to_Aug_\d{4}\.pdf` | `MOS_Estimates_Report_June_2017_to_Aug_2017.pdf` | 1 | 2016-11-11 | 2016-11-11 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_Mar{d21}_to_May{d22}.pdf` | `MOS_Estimates_Report_Mar\d{2}_to_May\d{2}\.pdf` | `MOS_Estimates_Report_Mar18_to_May18.pdf` | 1 | 2017-06-26 | 2017-06-26 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_Mar_{year1}_to_May_{year2}.pdf` | `MOS_Estimates_Report_Mar_\d{4}_to_May_\d{4}\.pdf` | `MOS_Estimates_Report_Mar_2017_to_May_2017.pdf` | 5 | 2016-11-11 | 2021-06-07 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_Sep{d21}_to_Nov{d22}.pdf` | `MOS_Estimates_Report_Sep\d{2}_to_Nov\d{2}\.pdf` | `MOS_Estimates_Report_Sep17_to_Nov17.pdf` | 1 | 2016-12-08 | 2016-12-08 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Report_Sep_{year1}_to_Nov_{year2}.pdf` | `MOS_Estimates_Report_Sep_\d{4}_to_Nov_\d{4}\.pdf` | `MOS_Estimates_Report_Sep_2018_to_Nov_2018.pdf` | 4 | 2017-12-06 | 2021-01-05 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Sep_{year1}-Nov_{year2}-Supporting_Data.xlsx` | `MOS_Estimates_Sep_\d{4}\-Nov_\d{4}\-Supporting_Data\.xlsx` | `MOS_Estimates_Sep_2016-Nov_2016-Supporting_Data.xlsx` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting Data_Dec_{year1}_to_Feb_{year2}.xlsx` | `MOS_Estimates_Supporting\ Data_Dec_\d{4}_to_Feb_\d{4}\.xlsx` | `MOS_Estimates_Supporting Data_Dec_2016_to_Feb_2017.xlsx` | 1 | 2016-11-04 | 2016-11-04 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting_Data_Dec{d21}_to_Feb{d22}.xlsx` | `MOS_Estimates_Supporting_Data_Dec\d{2}_to_Feb\d{2}\.xlsx` | `MOS_Estimates_Supporting_Data_Dec17_to_Feb18.xlsx` | 5 | 2017-05-11 | 2021-03-25 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting_Data_Jun{d21}_to_Aug{d22}.xlsx` | `MOS_Estimates_Supporting_Data_Jun\d{2}_to_Aug\d{2}\.xlsx` | `MOS_Estimates_Supporting_Data_Jun18_to_Aug18.xlsx` | 4 | 2017-09-26 | 2020-09-24 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting_Data_Jun_{year1}_to_Aug_{year2}.xlsx` | `MOS_Estimates_Supporting_Data_Jun_\d{4}_to_Aug_\d{4}\.xlsx` | `MOS_Estimates_Supporting_Data_Jun_2017_to_Aug_2017.xlsx` | 1 | 2016-11-11 | 2016-11-11 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting_Data_Mar{d21}_to_May{d22}.xlsx` | `MOS_Estimates_Supporting_Data_Mar\d{2}_to_May\d{2}\.xlsx` | `MOS_Estimates_Supporting_Data_Mar18_to_May18.xlsx` | 4 | 2017-06-26 | 2020-06-26 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting_Data_Mar_{year1}-May_{year2}.xlsx` | `MOS_Estimates_Supporting_Data_Mar_\d{4}\-May_\d{4}\.xlsx` | `MOS_Estimates_Supporting_Data_Mar_2017-May_2017.xlsx` | 1 | 2016-11-11 | 2016-11-11 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting_Data_Sep{d21}_to_Nov{d22}.xlsx` | `MOS_Estimates_Supporting_Data_Sep\d{2}_to_Nov\d{2}\.xlsx` | `MOS_Estimates_Supporting_Data_Sep18_to_Nov18.xlsx` | 4 | 2017-12-06 | 2021-01-05 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_Supporting_Data_Sep_{d21}_to_Nov_{d22}.xlsx` | `MOS_Estimates_Supporting_Data_Sep_\d{2}_to_Nov_\d{2}\.xlsx` | `MOS_Estimates_Supporting_Data_Sep_17_to_Nov_17.xlsx` | 1 | 2016-12-08 | 2016-12-08 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_and_Support_Data_{d1}Mar{year1}_to_{d2}Feb{year2}.zip` | `MOS_Estimates_and_Support_Data_\d{1}Mar\d{4}_to_\d{2}Feb\d{4}\.zip` | `MOS_Estimates_and_Support_Data_1Mar2014_to_28Feb2015.zip` | 2 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Estimates_and_Supporting_Data_{d1}Mar{year1}_to_{d2}Feb{year2}.zip` | `MOS_Estimates_and_Supporting_Data_\d{1}Mar\d{4}_to_\d{2}Feb\d{4}\.zip` | `MOS_Estimates_and_Supporting_Data_1Mar2011_to_29Feb2012.zip` | 4 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Period_Jun_{year1}-Aug_{year2}-MOS_Estimates_Report.pdf` | `MOS_Period_Jun_\d{4}\-Aug_\d{4}\-MOS_Estimates_Report\.pdf` | `MOS_Period_Jun_2016-Aug_2016-MOS_Estimates_Report.pdf` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `MOS_Period_Sep_{year1}-Nov_{year2}-MOS_Estimates_Report.pdf` | `MOS_Period_Sep_\d{4}\-Nov_\d{4}\-MOS_Estimates_Report\.pdf` | `MOS_Period_Sep_2016-Nov_2016-MOS_Estimates_Report.pdf` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/STTM/MOS Estimates/` | `SupportingData_{d21}Mar_{d22}May_{year}.xlsx` | `SupportingData_\d{2}Mar_\d{2}May_\d{4}\.xlsx` | `SupportingData_01Mar_31May_2016.xlsx` | 1 | 2016-09-29 | 2016-09-29 |

### `Reports` · `Settlements`

_3 pattern rows, 5321 files (snapshot), observed 2017-02-02 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Settlements/` | `PUBLIC_SETTLEMENTS_{date}.zip` | `PUBLIC_SETTLEMENTS_\d{8}\.zip` | `PUBLIC_SETTLEMENTS_20250302.zip` | 12 | 2025-05-02 | 2026-04-02 |
| `CURRENT` | `/Reports/CURRENT/Settlements/` | `PUBLIC_SETTLEMENTS_EXTN_{datetime}_{aemo_id}.zip` | `PUBLIC_SETTLEMENTS_EXTN_\d{14}_\d{16}\.zip` | `PUBLIC_SETTLEMENTS_EXTN_20260205085710_0000000501995342.zip` | 20 | 2026-02-05 | 2026-04-16 |
| `CURRENT` | `/Reports/CURRENT/Settlements/` | `PUBLIC_SETTLEMENTS_{datetime}_{aemo_id}.zip` | `PUBLIC_SETTLEMENTS_\d{14}_\d{16}\.zip` | `PUBLIC_SETTLEMENTS_20170202011150_0000000280585184.zip` | 5289 | 2017-02-02 | 2026-04-20 |

### `Reports` · `Short_Term_PASA_Reports`

_2 pattern rows, 1452 files (snapshot), observed 2025-05-01 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Short_Term_PASA_Reports/` | `PUBLIC_STPASA_{date}.zip` | `PUBLIC_STPASA_\d{8}\.zip` | `PUBLIC_STPASA_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/Short_Term_PASA_Reports/` | `PUBLIC_STPASA_{timestamp}_{aemo_id}.zip` | `PUBLIC_STPASA_\d{12}_\d{16}\.zip` | `PUBLIC_STPASA_202602191500_0000000504193048.zip` | 1440 | 2026-02-19 | 2026-04-20 |

### `Reports` · `SupplyDemand`

_4 pattern rows, 4 files (snapshot), observed 2016-09-29 → 2016-09-29 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/SupplyDemand/` | `NSW SUMMER OUTLOOK.PDF` | `NSW\ SUMMER\ OUTLOOK\.PDF` | `NSW SUMMER OUTLOOK.PDF` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/SupplyDemand/` | `QLD SUMMER OUTLOOK.PDF` | `QLD\ SUMMER\ OUTLOOK\.PDF` | `QLD SUMMER OUTLOOK.PDF` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/SupplyDemand/` | `TAS SUMMER OUTLOOK.PDF` | `TAS\ SUMMER\ OUTLOOK\.PDF` | `TAS SUMMER OUTLOOK.PDF` | 1 | 2016-09-29 | 2016-09-29 |
| `CURRENT` | `/Reports/CURRENT/SupplyDemand/` | `VIC_SA SUMMER OUTLOOK.PDF` | `VIC_SA\ SUMMER\ OUTLOOK\.PDF` | `VIC_SA SUMMER OUTLOOK.PDF` | 1 | 2016-09-29 | 2016-09-29 |

### `Reports` · `TradingIS_Reports`

_3 pattern rows, 4088 files (snapshot), observed 2025-04-13 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/TradingIS_Reports/` | `PUBLIC_TRADINGIS_{date1}_{date2}.zip` | `PUBLIC_TRADINGIS_\d{8}_\d{8}\.zip` | `PUBLIC_TRADINGIS_20250330_20250405.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/TradingIS_Reports/` | `PUBLIC_TRADINGIS_{timestamp}_{aemo_id}.zip` | `PUBLIC_TRADINGIS_\d{12}_\d{16}\.zip` | `PUBLIC_TRADINGIS_202604061445_0000000511603572.zip` | 4033 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/TradingIS_Reports/DUPLICATE/` | `PUBLIC_TRADINGIS_{timestamp}_{aemo_id}.zip` | `PUBLIC_TRADINGIS_\d{12}_\d{16}\.zip` | `PUBLIC_TRADINGIS_202603031345_0000000506103565.zip` | 1 | 2026-03-03 | 2026-03-03 |

### `Reports` · `Trading_Cumulative_Price`

_3 pattern rows, 4089 files (snapshot), observed 2020-08-23 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Trading_Cumulative_Price/` | `PUBLIC_TRADING_CUMULATIVE_PRICE_{date1}_{date2}.zip` | `PUBLIC_TRADING_CUMULATIVE_PRICE_\d{8}_\d{8}\.zip` | `PUBLIC_TRADING_CUMULATIVE_PRICE_20250330_20250405.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/Trading_Cumulative_Price/` | `PUBLIC_TRADING_CUMULATIVE_PRICE_{timestamp}_{aemo_id}.zip` | `PUBLIC_TRADING_CUMULATIVE_PRICE_\d{12}_\d{16}\.zip` | `PUBLIC_TRADING_CUMULATIVE_PRICE_202604061445_0000000511603574.zip` | 4033 | 2026-04-06 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/Trading_Cumulative_Price/DUPLICATE/` | `PUBLIC_TRADING_CUMULATIVE_PRICE_{timestamp}_{aemo_id}.zip` | `PUBLIC_TRADING_CUMULATIVE_PRICE_\d{12}_\d{16}\.zip` | `PUBLIC_TRADING_CUMULATIVE_PRICE_202008230200_0000000327476381.zip` | 2 | 2020-08-23 | 2025-08-12 |

### `Reports` · `Trading_IRSR`

_2 pattern rows, 4087 files (snapshot), observed 2025-04-13 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/Trading_IRSR/` | `PUBLIC_TRADING_IRSR_{date1}_{date2}.zip` | `PUBLIC_TRADING_IRSR_\d{8}_\d{8}\.zip` | `PUBLIC_TRADING_IRSR_20250330_20250405.zip` | 54 | 2025-04-13 | 2026-04-19 |
| `CURRENT` | `/Reports/CURRENT/Trading_IRSR/` | `PUBLIC_TRADING_IRSR_{timestamp}_{aemo_id}.zip` | `PUBLIC_TRADING_IRSR_\d{12}_\d{16}\.zip` | `PUBLIC_TRADING_IRSR_202604061445_0000000511603684.zip` | 4033 | 2026-04-06 | 2026-04-20 |

### `Reports` · `VicGas`

_91 pattern rows, 126 files (snapshot), observed 2026-04-20 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `CURRENTDAY.ZIP` | `CURRENTDAY\.ZIP` | `CURRENTDAY.ZIP` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}A_V{d11}_DAILY_ZONAL_HEATING_{d12}.CSV` | `INT\d{3}A_V\d{1}_DAILY_ZONAL_HEATING_\d{1}\.CSV` | `INT139A_V4_DAILY_ZONAL_HEATING_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}A_V{d11}_DAILY_ZONAL_HV_{d12}.CSV` | `INT\d{3}A_V\d{1}_DAILY_ZONAL_HV_\d{1}\.CSV` | `INT839A_V1_DAILY_ZONAL_HV_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}A_V{d11}_EST_ANCILLARY_PAYMENTS_{d12}.CSV` | `INT\d{3}A_V\d{1}_EST_ANCILLARY_PAYMENTS_\d{1}\.CSV` | `INT117A_V4_EST_ANCILLARY_PAYMENTS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}A_V{d11}_SYSTEM_NOTICES_{d12}.CSV` | `INT\d{3}A_V\d{1}_SYSTEM_NOTICES_\d{1}\.CSV` | `INT029A_V4_SYSTEM_NOTICES_1.CSV` | 2 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}A_V{d11}_UPLIFT_BREAKDOWN_SETT_{d12}.CSV` | `INT\d{3}A_V\d{1}_UPLIFT_BREAKDOWN_SETT_\d{1}\.CSV` | `INT322A_V4_UPLIFT_BREAKDOWN_SETT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}B_V{d11}_ANCILLARY_PAYMENTS_{d12}.CSV` | `INT\d{3}B_V\d{1}_ANCILLARY_PAYMENTS_\d{1}\.CSV` | `INT117B_V4_ANCILLARY_PAYMENTS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}B_V{d11}_INDICATIVE_LOCATIONAL_PRICE_{d12}.CSV` | `INT\d{3}B_V\d{1}_INDICATIVE_LOCATIONAL_PRICE_\d{1}\.CSV` | `INT039B_V4_INDICATIVE_LOCATIONAL_PRICE_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}B_V{d11}_INDICATIVE_MKT_PRICE_{d12}.CSV` | `INT\d{3}B_V\d{1}_INDICATIVE_MKT_PRICE_\d{1}\.CSV` | `INT037B_V4_INDICATIVE_MKT_PRICE_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}B_V{d11}_NFTC_{d12}.CSV` | `INT\d{3}B_V\d{1}_NFTC_\d{1}\.CSV` | `INT112B_V4_NFTC_1.CSV` | 2 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}B_V{d11}_UPLIFT_BREAKDOWN_PRUD_{d12}.CSV` | `INT\d{3}B_V\d{1}_UPLIFT_BREAKDOWN_PRUD_\d{1}\.CSV` | `INT322B_V4_UPLIFT_BREAKDOWN_PRUD_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}C_V{d11}_INDICATIVE_PRICE_{d12}.CSV` | `INT\d{3}C_V\d{1}_INDICATIVE_PRICE_\d{1}\.CSV` | `INT037C_V4_INDICATIVE_PRICE_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}C_V{d11}_SSC_{d12}.CSV` | `INT\d{3}C_V\d{1}_SSC_\d{1}\.CSV` | `INT112C_V4_SSC_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}D_V{d11}_ZFTC_{d12}.CSV` | `INT\d{3}D_V\d{1}_ZFTC_\d{1}\.CSV` | `INT112D_V4_ZFTC_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_ACTUAL_LINEPACK_{d12}.CSV` | `INT\d{3}_V\d{1}_ACTUAL_LINEPACK_\d{1}\.CSV` | `INT128_V4_ACTUAL_LINEPACK_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_AGG_AMDQ_TRANSFERRED_{d12}.CSV` | `INT\d{3}_V\d{1}_AGG_AMDQ_TRANSFERRED_\d{1}\.CSV` | `INT261_V4_AGG_AMDQ_TRANSFERRED_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_ALLOCATED_INJECTIONS_WITHDRAWALS_{d12}.CSV` | `INT\d{3}_V\d{1}_ALLOCATED_INJECTIONS_WITHDRAWALS_\d{1}\.CSV` | `INT313_V4_ALLOCATED_INJECTIONS_WITHDRAWALS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_BIDS_AT_BID_CUTOFF_TIMES_PREV_{d12}_{d13}.CSV` | `INT\d{3}_V\d{1}_BIDS_AT_BID_CUTOFF_TIMES_PREV_\d{1}_\d{1}\.CSV` | `INT131_V4_BIDS_AT_BID_CUTOFF_TIMES_PREV_2_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_BID_STACK_{d12}.CSV` | `INT\d{3}_V\d{1}_BID_STACK_\d{1}\.CSV` | `INT314_V4_BID_STACK_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_BMP_VERSION_NON_PTS_{d12}.CSV` | `INT\d{3}_V\d{1}_BMP_VERSION_NON_PTS_\d{1}\.CSV` | `INT438_V4_BMP_VERSION_NON_PTS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCAUCTION_AUCTION_QTY_{d12}.CSV` | `INT\d{3}_V\d{1}_CCAUCTION_AUCTION_QTY_\d{1}\.CSV` | `INT343_V4_CCAUCTION_AUCTION_QTY_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCAUCTION_BID_STACK_{d12}.CSV` | `INT\d{3}_V\d{1}_CCAUCTION_BID_STACK_\d{1}\.CSV` | `INT339_V4_CCAUCTION_BID_STACK_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCAUCTION_QTY_WON_ALL_{d12}.CSV` | `INT\d{3}_V\d{1}_CCAUCTION_QTY_WON_ALL_\d{1}\.CSV` | `INT353_V4_CCAUCTION_QTY_WON_ALL_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCAUCTION_QTY_WON_{d12}.CSV` | `INT\d{3}_V\d{1}_CCAUCTION_QTY_WON_\d{1}\.CSV` | `INT353_V4_CCAUCTION_QTY_WON_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCAUCTION_SYS_CAPABILITY_{d12}.CSV` | `INT\d{3}_V\d{1}_CCAUCTION_SYS_CAPABILITY_\d{1}\.CSV` | `INT342_V4_CCAUCTION_SYS_CAPABILITY_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCAUCTION_ZONE_{d12}.CSV` | `INT\d{3}_V\d{1}_CCAUCTION_ZONE_\d{1}\.CSV` | `INT345_V4_CCAUCTION_ZONE_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCREGISTRY_SUMMARY_{d12}.CSV` | `INT\d{3}_V\d{1}_CCREGISTRY_SUMMARY_\d{1}\.CSV` | `INT351_V4_CCREGISTRY_SUMMARY_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CCTRANSFER_{d12}.CSV` | `INT\d{3}_V\d{1}_CCTRANSFER_\d{1}\.CSV` | `INT348_V4_CCTRANSFER_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_COMPRESSOR_CHAR_{d12}.CSV` | `INT\d{3}_V\d{1}_COMPRESSOR_CHAR_\d{1}\.CSV` | `INT260_V4_COMPRESSOR_CHAR_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CTM_TO_HV_ZONE_MAPPING_{d12}.CSV` | `INT\d{3}_V\d{1}_CTM_TO_HV_ZONE_MAPPING_\d{1}\.CSV` | `INT188_V4_CTM_TO_HV_ZONE_MAPPING_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CUMULATIVE_PRICE_{d12}.CSV` | `INT\d{3}_V\d{1}_CUMULATIVE_PRICE_\d{1}\.CSV` | `INT199_V4_CUMULATIVE_PRICE_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_CUSTOMER_TRANSFERS_{d12}.CSV` | `INT\d{3}_V\d{1}_CUSTOMER_TRANSFERS_\d{1}\.CSV` | `INT311_V5_CUSTOMER_TRANSFERS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_DAILY_ZONAL_HV_{d12}.CSV` | `INT\d{3}_V\d{1}_DAILY_ZONAL_HV_\d{1}\.CSV` | `INT539_V4_DAILY_ZONAL_HV_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_DECLARED_DAILY_STATE_HEATING_VALUE_{d12}.CSV` | `INT\d{3}_V\d{1}_DECLARED_DAILY_STATE_HEATING_VALUE_\d{1}\.CSV` | `INT139_V4_DECLARED_DAILY_STATE_HEATING_VALUE_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_DEMAND_FORECAST_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_DEMAND_FORECAST_RPT_\d{1}\.CSV` | `INT153_V4_DEMAND_FORECAST_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_DETAILS_OF_ORGANISATIONS_{d12}.CSV` | `INT\d{3}_V\d{1}_DETAILS_OF_ORGANISATIONS_\d{1}\.CSV` | `INT125_V8_DETAILS_OF_ORGANISATIONS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_DFPC_{d12}.CSV` | `INT\d{3}_V\d{1}_DFPC_\d{1}\.CSV` | `INT112_V4_DFPC_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_DFS_DATA_{d12}.CSV` | `INT\d{3}_V\d{1}_DFS_DATA_\d{1}\.CSV` | `INT126_V4_DFS_DATA_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_ECGS_CONTACTS_{d12}.CSV` | `INT\d{3}_V\d{1}_ECGS_CONTACTS_\d{1}\.CSV` | `INT934_V4_ECGS_CONTACTS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_EDDACT_{d12}.CSV` | `INT\d{3}_V\d{1}_EDDACT_\d{1}\.CSV` | `INT091_V4_EDDACT_1.CSV` | 2 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_ERFTDAILYNSLRPT_{d12}.CSV` | `INT\d{3}_V\d{1}_ERFTDAILYNSLRPT_\d{1}\.CSV` | `INT871_V1_ERFTDAILYNSLRPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_GAS_COMPOSITION_DATA_{d12}.CSV` | `INT\d{3}_V\d{1}_GAS_COMPOSITION_DATA_\d{1}\.CSV` | `INT176_V4_GAS_COMPOSITION_DATA_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_GAS_CONSUMPTION_{d12}.CSV` | `INT\d{3}_V\d{1}_GAS_CONSUMPTION_\d{1}\.CSV` | `INT287_V4_GAS_CONSUMPTION_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_GAS_QUALITY_DATA_{d12}.CSV` | `INT\d{3}_V\d{1}_GAS_QUALITY_DATA_\d{1}\.CSV` | `INT140_V5_GAS_QUALITY_DATA_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_HEATING_VALUES_{d12}.CSV` | `INT\d{3}_V\d{1}_HEATING_VALUES_\d{1}\.CSV` | `INT047_V4_HEATING_VALUES_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_HOURLY_SCADA_PRESSURES_AT_MCE_NODES_{d12}.CSV` | `INT\d{3}_V\d{1}_HOURLY_SCADA_PRESSURES_AT_MCE_NODES_\d{1}\.CSV` | `INT276_V4_HOURLY_SCADA_PRESSURES_AT_MCE_NODES_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_INJECTION_SCALING_FACTORS_{d12}.CSV` | `INT\d{3}_V\d{1}_INJECTION_SCALING_FACTORS_\d{1}\.CSV` | `INT597_V4_INJECTION_SCALING_FACTORS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_LATEST_NSL_NON_PTS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_LATEST_NSL_NON_PTS_RPT_\d{1}\.CSV` | `INT471_V4_LATEST_NSL_NON_PTS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_LATEST_NSL_{d12}.CSV` | `INT\d{3}_V\d{1}_LATEST_NSL_\d{1}\.CSV` | `INT171_V4_LATEST_NSL_1.CSV` | 2 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_LATEST_TOTAL_HOURLY_NSL_{d12}.CSV` | `INT\d{3}_V\d{1}_LATEST_TOTAL_HOURLY_NSL_\d{1}\.CSV` | `INT271_V4_LATEST_TOTAL_HOURLY_NSL_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_LINEPACK_BALANCE_{d12}.CSV` | `INT\d{3}_V\d{1}_LINEPACK_BALANCE_\d{1}\.CSV` | `INT089_V4_LINEPACK_BALANCE_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_LINEPACK_WITH_ZONES_{d12}.CSV` | `INT\d{3}_V\d{1}_LINEPACK_WITH_ZONES_\d{1}\.CSV` | `INT257_V4_LINEPACK_WITH_ZONES_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_LNG_MONITOR_{d12}.CSV` | `INT\d{3}_V\d{1}_LNG_MONITOR_\d{1}\.CSV` | `INT263_V4_LNG_MONITOR_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_MARKET_AND_REFERENCE_PRICES_{d12}.CSV` | `INT\d{3}_V\d{1}_MARKET_AND_REFERENCE_PRICES_\d{1}\.CSV` | `INT041_V4_MARKET_AND_REFERENCE_PRICES_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_MCE_FACTOR_{d12}.CSV` | `INT\d{3}_V\d{1}_MCE_FACTOR_\d{1}\.CSV` | `INT256_V4_MCE_FACTOR_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_MCE_NODES_{d12}.CSV` | `INT\d{3}_V\d{1}_MCE_NODES_\d{1}\.CSV` | `INT258_V4_MCE_NODES_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_MONTHLY_CUMULATIVE_IMB_POS_{d12}.CSV` | `INT\d{3}_V\d{1}_MONTHLY_CUMULATIVE_IMB_POS_\d{1}\.CSV` | `INT583_V4_MONTHLY_CUMULATIVE_IMB_POS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_NEWSTREETLISTING_{d12}.CSV` | `INT\d{3}_V\d{1}_NEWSTREETLISTING_\d{1}\.CSV` | `INT898_V1_NEWSTREETLISTING_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_OPERATIONAL_GAS_{d12}.CSV` | `INT\d{3}_V\d{1}_OPERATIONAL_GAS_\d{1}\.CSV` | `INT316_V4_OPERATIONAL_GAS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_OPERATIONAL_METER_READINGS_{d12}.CSV` | `INT\d{3}_V\d{1}_OPERATIONAL_METER_READINGS_\d{1}\.CSV` | `INT236_V4_OPERATIONAL_METER_READINGS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_OUT_OF_MERIT_ORDER_GAS_{d12}.CSV` | `INT\d{3}_V\d{1}_OUT_OF_MERIT_ORDER_GAS_\d{1}\.CSV` | `INT291_V4_OUT_OF_MERIT_ORDER_GAS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_PIPE_SEGMENT_{d12}.CSV` | `INT\d{3}_V\d{1}_PIPE_SEGMENT_\d{1}\.CSV` | `INT259_V4_PIPE_SEGMENT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_PRICE_AND_WITHDRAWALS_RPT_{d12}.CSV` | `INT\d{3}_V\d{1}_PRICE_AND_WITHDRAWALS_RPT_\d{1}\.CSV` | `INT310_V1_PRICE_AND_WITHDRAWALS_RPT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_PRICE_AND_WITHDRAWALS_{d12}.CSV` | `INT\d{3}_V\d{1}_PRICE_AND_WITHDRAWALS_\d{1}\.CSV` | `INT310_V4_PRICE_AND_WITHDRAWALS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_PUBLIC_METERING_DATA_{d12}.CSV` | `INT\d{3}_V\d{1}_PUBLIC_METERING_DATA_\d{1}\.CSV` | `INT150_V4_PUBLIC_METERING_DATA_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_PUBLISHED_DAILY_HEATING_VALUE_NON_PTS_{d12}.CSV` | `INT\d{3}_V\d{1}_PUBLISHED_DAILY_HEATING_VALUE_NON_PTS_\d{1}\.CSV` | `INT439_V4_PUBLISHED_DAILY_HEATING_VALUE_NON_PTS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SCHEDULED_RUN_LOG_{d12}_{d13}.CSV` | `INT\d{3}_V\d{1}_SCHEDULED_RUN_LOG_\d{1}_\d{1}\.CSV` | `INT108_V4_SCHEDULED_RUN_LOG_7_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SCHED_MIN_QTY_LINEPACK_{d12}.CSV` | `INT\d{3}_V\d{1}_SCHED_MIN_QTY_LINEPACK_\d{1}\.CSV` | `INT152_V4_SCHED_MIN_QTY_LINEPACK_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SCHED_SYSTEM_TOTAL_{d12}.CSV` | `INT\d{3}_V\d{1}_SCHED_SYSTEM_TOTAL_\d{1}\.CSV` | `INT235_V4_SCHED_SYSTEM_TOTAL_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SCHED_WITHDRAWALS_{d12}.CSV` | `INT\d{3}_V\d{1}_SCHED_WITHDRAWALS_\d{1}\.CSV` | `INT050_V4_SCHED_WITHDRAWALS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SDPC_{d12}.CSV` | `INT\d{3}_V\d{1}_SDPC_\d{1}\.CSV` | `INT111_V5_SDPC_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SETTLEMENTS_ACTIVITY_{d12}.CSV` | `INT\d{3}_V\d{1}_SETTLEMENTS_ACTIVITY_\d{1}\.CSV` | `INT312_V4_SETTLEMENTS_ACTIVITY_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SETTLEMENT_VERSIONS_{d12}.CSV` | `INT\d{3}_V\d{1}_SETTLEMENT_VERSIONS_\d{1}\.CSV` | `INT538_V4_SETTLEMENT_VERSIONS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SETTLEMENT_VERSION_{d12}.CSV` | `INT\d{3}_V\d{1}_SETTLEMENT_VERSION_\d{1}\.CSV` | `INT138_V4_SETTLEMENT_VERSION_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_SPARE_CAPACITY_LIMITS_{d12}.CSV` | `INT\d{3}_V\d{1}_SPARE_CAPACITY_LIMITS_\d{1}\.CSV` | `INT262_V4_SPARE_CAPACITY_LIMITS_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_TIE_BREAKING_EVENT_{d12}.CSV` | `INT\d{3}_V\d{1}_TIE_BREAKING_EVENT_\d{1}\.CSV` | `INT381_V4_TIE_BREAKING_EVENT_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_TOTAL_GAS_WITHDRAWN_{d12}.CSV` | `INT\d{3}_V\d{1}_TOTAL_GAS_WITHDRAWN_\d{1}\.CSV` | `INT079_V4_TOTAL_GAS_WITHDRAWN_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_TUOS_ZONE_POSTCODE_MAP_{d12}.CSV` | `INT\d{3}_V\d{1}_TUOS_ZONE_POSTCODE_MAP_\d{1}\.CSV` | `INT284_V4_TUOS_ZONE_POSTCODE_MAP_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_UPLIFT_CAP_{d12}.CSV` | `INT\d{3}_V\d{1}_UPLIFT_CAP_\d{1}\.CSV` | `INT135_V4_UPLIFT_CAP_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `INT{d3}_V{d11}_WEIGHTED_AVERAGE_DAILY_PRICES_{d12}.CSV` | `INT\d{3}_V\d{1}_WEIGHTED_AVERAGE_DAILY_PRICES_\d{1}\.CSV` | `INT042_V4_WEIGHTED_AVERAGE_DAILY_PRICES_1.CSV` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `PUBLICRPTS{d2}.ZIP` | `PUBLICRPTS\d{2}\.ZIP` | `PUBLICRPTS01.ZIP` | 31 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d2}_linepack_{d1}.csv` | `int\d{2}_linepack_\d{1}\.csv` | `int89_linepack_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_{d2}.csv` | `int\d{3}_\d{2}\.csv` | `int157_13.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_ancillary_payments_rpt_{d1}.csv` | `int\d{3}_ancillary_payments_rpt_\d{1}\.csv` | `int117_ancillary_payments_rpt_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_v{d11}_actual_linepack_{d12}~{datetime}.csv` | `int\d{3}_v\d{1}_actual_linepack_\d{1}\~\d{14}\.csv` | `int128_v4_actual_linepack_1~20120908043621.csv` | 2 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_v{d11}_customer_transfers_{d12}.csv` | `int\d{3}_v\d{1}_customer_transfers_\d{1}\.csv` | `int311_v4_customer_transfers_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_v{d11}_details_of_organisations_{d12}.csv` | `int\d{3}_v\d{1}_details_of_organisations_\d{1}\.csv` | `int125_v7_details_of_organisations_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_v{d1}_op_sched_{d2}.csv` | `int\d{3}_v\d{1}_op_sched_\d{2}\.csv` | `int180_v4_op_sched_77.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_v{d11}_sdpc_{d12}.csv` | `int\d{3}_v\d{1}_sdpc_\d{1}\.csv` | `int111_v4_sdpc_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_v{d11}_settlements_activity_report_{d12}.csv` | `int\d{3}_v\d{1}_settlements_activity_report_\d{1}\.csv` | `int312_v1_settlements_activity_report_1.csv` | 1 | 2026-04-20 | 2026-04-20 |
| `CURRENT` | `/Reports/CURRENT/VicGas/` | `int{d3}_v{d1}_uplift_cap~{datetime}.csv` | `int\d{3}_v\d{1}_uplift_cap\~\d{14}\.csv` | `int135_v4_uplift_cap~20100817153329.csv` | 1 | 2026-04-20 | 2026-04-20 |

### `Reports` · `Vwa_Fcas_Prices`

_1 pattern row, 60 files (snapshot), observed 2026-02-20 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Vwa_Fcas_Prices/` | `PUBLIC_VWAFCASPRICES_{timestamp}_{datetime}.zip` | `PUBLIC_VWAFCASPRICES_\d{12}_\d{14}\.zip` | `PUBLIC_VWAFCASPRICES_202602190000_20260220040503.zip` | 60 | 2026-02-20 | 2026-04-20 |

### `Reports` · `WDR_CAPACITY_NO_SCADA`

_2 pattern rows, 1654 files (snapshot), observed 2021-10-22 → 2026-04-20 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ARCHIVE` | `/Reports/ARCHIVE/WDR_CAPACITY_NO_SCADA/` | `PUBLIC_WDR_CAPACITY_NO_SCADA_{date}.zip` | `PUBLIC_WDR_CAPACITY_NO_SCADA_\d{8}\.zip` | `PUBLIC_WDR_CAPACITY_NO_SCADA_20250301.zip` | 12 | 2025-05-01 | 2026-04-01 |
| `CURRENT` | `/Reports/CURRENT/WDR_CAPACITY_NO_SCADA/` | `PUBLIC_WDR_CAPACITY_NO_SCADA_{date}_{aemo_id}.zip` | `PUBLIC_WDR_CAPACITY_NO_SCADA_\d{8}_\d{16}\.zip` | `PUBLIC_WDR_CAPACITY_NO_SCADA_20211021_0000000351232024.zip` | 1642 | 2021-10-22 | 2026-04-20 |

### `Reports` · `Weekly_Constraint_Reports`

_2 pattern rows, 2 files (snapshot), observed 2026-04-13 → 2026-04-13 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Weekly_Constraint_Reports/` | `Current_CCR.xlsx` | `Current_CCR\.xlsx` | `Current_CCR.xlsx` | 1 | 2026-04-13 | 2026-04-13 |
| `CURRENT` | `/Reports/CURRENT/Weekly_Constraint_Reports/` | `{year}.zip` | `\d{4}\.zip` | `2026.zip` | 1 | 2026-04-13 | 2026-04-13 |

### `Reports` · `Yesterdays_Bids_Reports`

_1 pattern row, 1 files (snapshot), observed 2016-12-23 → 2016-12-23 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `CURRENT` | `/Reports/CURRENT/Yesterdays_Bids_Reports/DUPLICATE/` | `PUBLIC_YESTBID_{timestamp}_{datetime}.zip` | `PUBLIC_YESTBID_\d{12}_\d{14}\.zip` | `PUBLIC_YESTBID_201612220000_20161223040519.zip` | 1 | 2016-12-23 | 2016-12-23 |

## Repo: `MMSDM`  (263 datasets, 1700 rows)

### `MMSDM` · `ADG_DETAIL`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#ADG_DETAIL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#ADG_DETAIL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#ADG_DETAIL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#ADG_DETAIL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#ADG_DETAIL#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `AGGREGATE_DISPATCH_GROUP`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#AGGREGATE_DISPATCH_GROUP\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#AGGREGATE_DISPATCH_GROUP\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#AGGREGATE_DISPATCH_GROUP\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#AGGREGATE_DISPATCH_GROUP\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#AGGREGATE_DISPATCH_GROUP#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `ANCILLARY_RECOVERY_SPLIT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#ANCILLARY_RECOVERY_SPLIT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#ANCILLARY_RECOVERY_SPLIT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#ANCILLARY_RECOVERY_SPLIT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#ANCILLARY_RECOVERY_SPLIT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#ANCILLARY_RECOVERY_SPLIT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `APEVENT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#APEVENT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#APEVENT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#APEVENT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#APEVENT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#APEVENT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#APEVENT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#APEVENT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#APEVENT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#APEVENT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#APEVENT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#APEVENT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#APEVENT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `APEVENTREGION`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#APEVENTREGION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#APEVENTREGION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#APEVENTREGION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#APEVENTREGION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#APEVENTREGION#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `AUCTION`

_4 pattern rows, 52 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#AUCTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#AUCTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#AUCTION#FILE01#202409.fmt` | 13 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#AUCTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#AUCTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#AUCTION#FILE01#202409.ctl` | 13 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#AUCTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#AUCTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#AUCTION#FILE01#202409010000.zip` | 13 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#AUCTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#AUCTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#AUCTION#FILE01#202409.sql` | 13 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `AUCTION_CALENDAR`

_4 pattern rows, 28 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#AUCTION_CALENDAR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE01#202409.fmt` | 7 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#AUCTION_CALENDAR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE01#202409.ctl` | 7 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#AUCTION_CALENDAR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE01#202409010000.zip` | 7 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#AUCTION_CALENDAR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#AUCTION_CALENDAR#FILE01#202409.sql` | 7 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `AUCTION_IC_ALLOCATIONS`

_4 pattern rows, 56 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#AUCTION_IC_ALLOCATIONS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE01#202408.fmt` | 14 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#AUCTION_IC_ALLOCATIONS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE01#202408.ctl` | 14 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#AUCTION_IC_ALLOCATIONS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE01#202408010000.zip` | 14 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#AUCTION_IC_ALLOCATIONS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#AUCTION_IC_ALLOCATIONS#FILE01#202408.sql` | 14 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `AUCTION_TRANCHE`

_4 pattern rows, 28 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#AUCTION_TRANCHE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE01#202409.fmt` | 7 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#AUCTION_TRANCHE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE01#202409.ctl` | 7 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#AUCTION_TRANCHE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE01#202409010000.zip` | 7 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#AUCTION_TRANCHE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#AUCTION_TRANCHE#FILE01#202409.sql` | 7 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `AVERAGEPRICE30`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#AVERAGEPRICE{d21}#FILE{d22}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#AVERAGEPRICE\d{2}\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#AVERAGEPRICE30#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#AVERAGEPRICE{d21}#FILE{d22}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#AVERAGEPRICE\d{2}\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#AVERAGEPRICE30#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#AVERAGEPRICE{d21}#FILE{d22}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#AVERAGEPRICE\d{2}\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#AVERAGEPRICE30#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#AVERAGEPRICE{d21}#FILE{d22}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#AVERAGEPRICE\d{2}\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#AVERAGEPRICE30#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDDAYOFFER`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDDAYOFFER\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDDAYOFFER\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDDAYOFFER\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDDAYOFFER\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDDAYOFFER#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDDAYOFFER_D`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDDAYOFFER_D\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDDAYOFFER_D\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDDAYOFFER_D\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDDAYOFFER_D\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDDAYOFFER_D#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDDUIDDETAILS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDDUIDDETAILS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDDUIDDETAILSTRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILSTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILSTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILSTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDDUIDDETAILSTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDDUIDDETAILSTRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDOFFERPERIOD`

_4 pattern rows, 3480 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDOFFERPERIOD\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE01#202408.fmt` | 870 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDOFFERPERIOD\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE01#202408.ctl` | 870 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDOFFERPERIOD\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE01#202408010000.zip` | 870 | 2024-09-12 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDOFFERPERIOD\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDOFFERPERIOD#FILE01#202408.sql` | 870 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDPEROFFER_D`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDPEROFFER_D\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDPEROFFER_D\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDPEROFFER_D\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDPEROFFER_D\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDPEROFFER_D#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDTYPES`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDTYPES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDTYPES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDTYPES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDTYPES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDTYPES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDTYPES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDTYPES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDTYPES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDTYPES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDTYPES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDTYPES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDTYPES#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BIDTYPESTRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BIDTYPESTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BIDTYPESTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BIDTYPESTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BIDTYPESTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BIDTYPESTRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLINGCALENDAR`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLINGCALENDAR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLINGCALENDAR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLINGCALENDAR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLINGCALENDAR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLINGCALENDAR#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLINGDAYTRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLINGDAYTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLINGDAYTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLINGDAYTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLINGDAYTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLINGDAYTRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLINGREGIONEXPORTS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLINGREGIONEXPORTS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLINGREGIONEXPORTS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLINGREGIONEXPORTS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLINGREGIONEXPORTS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLINGREGIONEXPORTS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLINGREGIONFIGURES`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLINGREGIONFIGURES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLINGREGIONFIGURES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLINGREGIONFIGURES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLINGREGIONFIGURES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLINGREGIONFIGURES#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLINGREGIONIMPORTS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLINGREGIONIMPORTS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLINGREGIONIMPORTS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLINGREGIONIMPORTS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLINGREGIONIMPORTS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLINGREGIONIMPORTS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLINGRUNTRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLINGRUNTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLINGRUNTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLINGRUNTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLINGRUNTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLINGRUNTRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLING_CO2E_PUBLICATION`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLING_CO2E_PUBLICATION_TRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION_TRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION_TRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION_TRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLING_CO{d1}E_PUBLICATION_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLING_CO\d{1}E_PUBLICATION_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLING_CO2E_PUBLICATION_TRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLING_DIRECTION_RECON_OTHER`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLING_DIRECTION_RECON_OTHER\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLING_DIRECTION_RECON_OTHER\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLING_DIRECTION_RECON_OTHER\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLING_DIRECTION_RECON_OTHER\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLING_DIRECTION_RECON_OTHER#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `BILLING_NMAS_TST_RECVRY_RBF`

_4 pattern rows, 56 files (snapshot), observed 2024-11-11 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_RBF\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE01#202410.fmt` | 14 | 2024-11-11 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_RBF\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE01#202410.ctl` | 14 | 2024-11-11 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_RBF\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE01#202410010000.zip` | 14 | 2024-11-11 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_RBF\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_RBF#FILE01#202410.sql` | 14 | 2024-11-11 | 2026-04-08 |

### `MMSDM` · `BILLING_NMAS_TST_RECVRY_TRK`

_4 pattern rows, 44 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE01#202412.fmt` | 11 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE01#202412.ctl` | 11 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE01#202412010000.zip` | 11 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#BILLING_NMAS_TST_RECVRY_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#BILLING_NMAS_TST_RECVRY_TRK#FILE01#202412.sql` | 11 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `CONSTRAINTRELAXATION_OCD`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#CONSTRAINTRELAXATION_OCD\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#CONSTRAINTRELAXATION_OCD\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#CONSTRAINTRELAXATION_OCD\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#CONSTRAINTRELAXATION_OCD\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#CONSTRAINTRELAXATION_OCD#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DAYTRACK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DAYTRACK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DAYTRACK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DAYTRACK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DAYTRACK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DAYTRACK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DAYTRACK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DAYTRACK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DAYTRACK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DAYTRACK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DAYTRACK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DAYTRACK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DAYTRACK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DEMANDOPERATIONALACTUAL`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALACTUAL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALACTUAL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALACTUAL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALACTUAL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALACTUAL#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DEMANDOPERATIONALFORECAST`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALFORECAST\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALFORECAST\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALFORECAST\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DEMANDOPERATIONALFORECAST\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DEMANDOPERATIONALFORECAST#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHABLEUNIT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHABLEUNIT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHABLEUNIT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHABLEUNIT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHABLEUNIT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHABLEUNIT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHBLOCKEDCONSTRAINT`

_4 pattern rows, 44 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE01#202409.fmt` | 11 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE01#202409.ctl` | 11 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE01#202409010000.zip` | 11 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHBLOCKEDCONSTRAINT#FILE01#202409.sql` | 11 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `DISPATCHCASESOLUTION`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHCASESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHCASESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHCASESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHCASESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHCASESOLUTION#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHCONSTRAINT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHCONSTRAINT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHINTERCONNECTORRES`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHINTERCONNECTORRES#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHLOAD`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHLOAD\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHLOAD\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHLOAD\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHLOAD\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHLOAD#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHOFFERTRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHOFFERTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHOFFERTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHOFFERTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHOFFERTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHOFFERTRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHPRICE`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHPRICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHPRICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHPRICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHPRICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHPRICE#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCHREGIONSUM`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCHREGIONSUM\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCHREGIONSUM\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCHREGIONSUM\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCHREGIONSUM\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCHREGIONSUM#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCH_CONSTRAINT_FCAS_OCD`

_4 pattern rows, 20 files (snapshot), observed 2024-11-11 → 2026-03-10 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_CONSTRAINT_FCAS_OCD\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE01#202410.fmt` | 5 | 2024-11-11 | 2026-03-10 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_CONSTRAINT_FCAS_OCD\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE01#202410.ctl` | 5 | 2024-11-11 | 2026-03-10 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_CONSTRAINT_FCAS_OCD\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE01#202410010000.zip` | 5 | 2024-11-11 | 2026-03-09 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_CONSTRAINT_FCAS_OCD\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_CONSTRAINT_FCAS_OCD#FILE01#202410.sql` | 5 | 2024-11-11 | 2026-03-10 |

### `MMSDM` · `DISPATCH_FCAS_REQ`

_4 pattern rows, 40 files (snapshot), observed 2024-09-12 → 2025-10-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE01#202408.fmt` | 10 | 2024-09-12 | 2025-10-17 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE01#202408.ctl` | 10 | 2024-09-12 | 2025-10-17 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE01#202408010000.zip` | 10 | 2024-09-12 | 2025-10-17 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ#FILE01#202408.sql` | 10 | 2024-09-13 | 2025-10-17 |

### `MMSDM` · `DISPATCH_FCAS_REQ_CONSTRAINT`

_4 pattern rows, 100 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE01#202412.fmt` | 25 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE01#202412.ctl` | 25 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE01#202412010000.zip` | 25 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_CONSTRAINT#FILE01#202412.sql` | 25 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `DISPATCH_FCAS_REQ_RUN`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_RUN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_FCAS_REQ_RUN#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `DISPATCH_INTERCONNECTION`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_INTERCONNECTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_INTERCONNECTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_INTERCONNECTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_INTERCONNECTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_INTERCONNECTION#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCH_LOCAL_PRICE`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_LOCAL_PRICE#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCH_MNSPBIDTRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_MNSPBIDTRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DISPATCH_PRICE_REVISION`

_4 pattern rows, 12 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_PRICE_REVISION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE01#202409.fmt` | 3 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_PRICE_REVISION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE01#202409.ctl` | 3 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_PRICE_REVISION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE01#202409010000.zip` | 3 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_PRICE_REVISION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_PRICE_REVISION#FILE01#202409.sql` | 3 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `DISPATCH_UNIT_SCADA`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DISPATCH_UNIT_SCADA\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DISPATCH_UNIT_SCADA\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DISPATCH_UNIT_SCADA\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DISPATCH_UNIT_SCADA\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DISPATCH_UNIT_SCADA#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DOCUMENTATION_AUX`

_6 pattern rows, 682 files (snapshot), observed 2009-12-30 → 2025-10-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/` | `Participant_Monthly_DVD.doc` | `Participant_Monthly_DVD\.doc` | `Participant_Monthly_DVD.doc` | 135 | 2009-12-30 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/` | `Participant_Monthly_DVD.pdf` | `Participant_Monthly_DVD\.pdf` | `Participant_Monthly_DVD.pdf` | 135 | 2009-12-30 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/` | `README.txt` | `README\.txt` | `README.txt` | 135 | 2009-12-30 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 27 | 2017-02-06 | 2018-04-20 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/` | `marketnoticedata_{yearmonth}.par` | `marketnoticedata_\d{6}\.par` | `marketnoticedata_201106.par` | 135 | 2011-07-08 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/` | `monthlydvd_tables.bat` | `monthlydvd_tables\.bat` | `monthlydvd_tables.bat` | 115 | 2011-07-08 | 2024-08-15 |

### `MMSDM` · `DUALLOC`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DUALLOC#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DUALLOC\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DUALLOC#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DUALLOC#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DUALLOC\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DUALLOC#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DUALLOC#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DUALLOC\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DUALLOC#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DUALLOC#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DUALLOC\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DUALLOC#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DUDETAIL`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DUDETAIL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DUDETAIL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DUDETAIL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DUDETAIL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DUDETAIL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DUDETAIL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DUDETAIL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DUDETAIL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DUDETAIL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DUDETAIL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DUDETAIL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DUDETAIL#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `DUDETAILSUMMARY`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#DUDETAILSUMMARY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#DUDETAILSUMMARY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#DUDETAILSUMMARY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#DUDETAILSUMMARY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#DUDETAILSUMMARY#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `EMSMASTER`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#EMSMASTER#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#EMSMASTER\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#EMSMASTER#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#EMSMASTER#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#EMSMASTER\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#EMSMASTER#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#EMSMASTER#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#EMSMASTER\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#EMSMASTER#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#EMSMASTER#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#EMSMASTER\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#EMSMASTER#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `FCAS_REGU_USAGE_FACTORS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `FCAS_REGU_USAGE_FACTORS_TRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FCAS_REGU_USAGE_FACTORS_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FCAS_REGU_USAGE_FACTORS_TRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `FPP_CONSTRAINT_FREQ_MEASURE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_CONSTRAINT_FREQ_MEASURE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_CONSTRAINT_FREQ_MEASURE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_CONSTRAINT_FREQ_MEASURE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_CONSTRAINT_FREQ_MEASURE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_CONSTRAINT_FREQ_MEASURE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_CONTRIBUTION_FACTOR`

_4 pattern rows, 120 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_CONTRIBUTION_FACTOR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE01#202412.fmt` | 30 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_CONTRIBUTION_FACTOR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE01#202412.ctl` | 30 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_CONTRIBUTION_FACTOR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE01#202412010000.zip` | 30 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_CONTRIBUTION_FACTOR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_CONTRIBUTION_FACTOR#FILE01#202412.sql` | 30 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_EST_PERF_COST_RATE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_EST_PERF_COST_RATE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_EST_PERF_COST_RATE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_EST_PERF_COST_RATE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_EST_PERF_COST_RATE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_EST_PERF_COST_RATE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_EST_RESIDUAL_COST_RATE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_EST_RESIDUAL_COST_RATE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_EST_RESIDUAL_COST_RATE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_EST_RESIDUAL_COST_RATE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_EST_RESIDUAL_COST_RATE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_EST_RESIDUAL_COST_RATE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_FCAS_SUMMARY`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_FCAS_SUMMARY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_FCAS_SUMMARY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_FCAS_SUMMARY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_FCAS_SUMMARY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_FCAS_SUMMARY#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_FORECAST_DEFAULT_CF`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_FORECAST_DEFAULT_CF\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_FORECAST_DEFAULT_CF\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_FORECAST_DEFAULT_CF\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_FORECAST_DEFAULT_CF\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_FORECAST_DEFAULT_CF#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_FORECAST_RESIDUAL_DCF`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_FORECAST_RESIDUAL_DCF\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_FORECAST_RESIDUAL_DCF\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_FORECAST_RESIDUAL_DCF\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_FORECAST_RESIDUAL_DCF\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_FORECAST_RESIDUAL_DCF#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_HIST_PERFORMANCE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_HIST_PERFORMANCE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_HIST_PERFORMANCE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_HIST_PERFORMANCE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_HIST_PERFORMANCE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_HIST_PERFORMANCE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_HIST_REGION_PERFORMANCE`

_4 pattern rows, 48 files (snapshot), observed 2025-05-17 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_HIST_REGION_PERFORMANCE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE01#202504.fmt` | 12 | 2025-05-17 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_HIST_REGION_PERFORMANCE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE01#202504.ctl` | 12 | 2025-05-17 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_HIST_REGION_PERFORMANCE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE01#202504010000.zip` | 12 | 2025-05-17 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_HIST_REGION_PERFORMANCE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_HIST_REGION_PERFORMANCE#FILE01#202504.sql` | 12 | 2025-05-17 | 2026-04-08 |

### `MMSDM` · `FPP_P5_FWD_EST_RESIDUALRATE`

_4 pattern rows, 60 files (snapshot), observed 2025-02-20 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_P{d1}_FWD_EST_RESIDUALRATE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_P\d{1}_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_P5_FWD_EST_RESIDUALRATE#FILE01#202501.fmt` | 15 | 2025-02-20 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_P{d1}_FWD_EST_RESIDUALRATE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_P\d{1}_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_P5_FWD_EST_RESIDUALRATE#FILE01#202501.ctl` | 15 | 2025-02-20 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_P{d1}_FWD_EST_RESIDUALRATE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_P\d{1}_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_P5_FWD_EST_RESIDUALRATE#FILE01#202501010000.zip` | 15 | 2025-02-20 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_P{d1}_FWD_EST_RESIDUALRATE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_P\d{1}_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_P5_FWD_EST_RESIDUALRATE#FILE01#202501.sql` | 15 | 2025-02-20 | 2026-04-08 |

### `MMSDM` · `FPP_PD_FWD_EST_RESIDUALRATE`

_4 pattern rows, 60 files (snapshot), observed 2025-02-20 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_PD_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE01#202501.fmt` | 15 | 2025-02-20 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_PD_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE01#202501.ctl` | 15 | 2025-02-20 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_PD_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE01#202501010000.zip` | 15 | 2025-02-20 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_PD_FWD_EST_RESIDUALRATE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_PD_FWD_EST_RESIDUALRATE#FILE01#202501.sql` | 15 | 2025-02-20 | 2026-04-08 |

### `MMSDM` · `FPP_PERFORMANCE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_PERFORMANCE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_PERFORMANCE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_PERFORMANCE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_PERFORMANCE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_PERFORMANCE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_RCR`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_RCR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_RCR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_RCR#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_RCR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_RCR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_RCR#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_RCR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_RCR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_RCR#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_RCR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_RCR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_RCR#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_REGION_FREQ_MEASURE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_REGION_FREQ_MEASURE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_REGION_FREQ_MEASURE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_REGION_FREQ_MEASURE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_REGION_FREQ_MEASURE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_REGION_FREQ_MEASURE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_RESIDUAL_CF`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_CF\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_CF\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_CF\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_CF\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_CF#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_RESIDUAL_PERFORMANCE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_PERFORMANCE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_PERFORMANCE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_PERFORMANCE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_RESIDUAL_PERFORMANCE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_RESIDUAL_PERFORMANCE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_RUN`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_RUN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_RUN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_RUN#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_RUN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_RUN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_RUN#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_RUN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_RUN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_RUN#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_RUN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_RUN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_RUN#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `FPP_UNIT_MW`

_4 pattern rows, 4 files (snapshot), observed 2025-01-10 → 2025-01-10 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_UNIT_MW\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE01#202412.fmt` | 1 | 2025-01-10 | 2025-01-10 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_UNIT_MW\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE01#202412.ctl` | 1 | 2025-01-10 | 2025-01-10 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_UNIT_MW\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE01#202412010000.zip` | 1 | 2025-01-10 | 2025-01-10 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_UNIT_MW\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_UNIT_MW#FILE01#202412.sql` | 1 | 2025-01-10 | 2025-01-10 |

### `MMSDM` · `FPP_USAGE`

_4 pattern rows, 64 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#FPP_USAGE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#FPP_USAGE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#FPP_USAGE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#FPP_USAGE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#FPP_USAGE#FILE01#202412.sql` | 16 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `GDINSTRUCT`

_4 pattern rows, 44 files (snapshot), observed 2025-06-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GDINSTRUCT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE01#202505.fmt` | 11 | 2025-06-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GDINSTRUCT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE01#202505.ctl` | 11 | 2025-06-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GDINSTRUCT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE01#202505010000.zip` | 11 | 2025-06-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GDINSTRUCT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GDINSTRUCT#FILE01#202505.sql` | 11 | 2025-06-10 | 2026-04-08 |

### `MMSDM` · `GENCONDATA`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENCONDATA#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENCONDATA\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENCONDATA#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENCONDATA#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENCONDATA\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENCONDATA#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENCONDATA#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENCONDATA\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENCONDATA#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENCONDATA#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENCONDATA\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENCONDATA#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENCONSET`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENCONSET#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENCONSET\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENCONSET#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENCONSET#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENCONSET\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENCONSET#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENCONSET#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENCONSET\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENCONSET#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENCONSET#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENCONSET\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENCONSET#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENCONSETINVOKE`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENCONSETINVOKE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENCONSETINVOKE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENCONSETINVOKE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENCONSETINVOKE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENCONSETINVOKE#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENCONSETTRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENCONSETTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENCONSETTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENCONSETTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENCONSETTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENCONSETTRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENERICCONSTRAINTRHS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENERICCONSTRAINTRHS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENERICCONSTRAINTRHS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENERICCONSTRAINTRHS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENERICCONSTRAINTRHS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENERICCONSTRAINTRHS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENERICEQUATIONDESC`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENERICEQUATIONDESC\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENERICEQUATIONDESC\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENERICEQUATIONDESC\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENERICEQUATIONDESC\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENERICEQUATIONDESC#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENERICEQUATIONRHS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENERICEQUATIONRHS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENERICEQUATIONRHS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENERICEQUATIONRHS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENERICEQUATIONRHS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENERICEQUATIONRHS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENUNITS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENUNITS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENUNITS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENUNITS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENUNITS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENUNITS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENUNITS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENUNITS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENUNITS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENUNITS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENUNITS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENUNITS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENUNITS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GENUNITS_UNIT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GENUNITS_UNIT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GENUNITS_UNIT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GENUNITS_UNIT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GENUNITS_UNIT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GENUNITS_UNIT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GST_BAS_CLASS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GST_BAS_CLASS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GST_BAS_CLASS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GST_BAS_CLASS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GST_BAS_CLASS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GST_BAS_CLASS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GST_RATE`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GST_RATE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GST_RATE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GST_RATE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GST_RATE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GST_RATE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GST_RATE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GST_RATE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GST_RATE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GST_RATE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GST_RATE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GST_RATE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GST_RATE#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GST_TRANSACTION_CLASS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_CLASS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_CLASS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_CLASS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_CLASS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GST_TRANSACTION_CLASS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `GST_TRANSACTION_TYPE`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_TYPE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_TYPE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_TYPE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#GST_TRANSACTION_TYPE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#GST_TRANSACTION_TYPE#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INSTRUCTIONSUBTYPE`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INSTRUCTIONSUBTYPE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INSTRUCTIONSUBTYPE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INSTRUCTIONSUBTYPE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INSTRUCTIONSUBTYPE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INSTRUCTIONSUBTYPE#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INSTRUCTIONTYPE`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INSTRUCTIONTYPE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INSTRUCTIONTYPE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INSTRUCTIONTYPE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INSTRUCTIONTYPE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INSTRUCTIONTYPE#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERCONNECTOR`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERCONNECTOR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERCONNECTOR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERCONNECTOR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERCONNECTOR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERCONNECTOR#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERCONNECTORCONSTRAINT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERCONNECTORCONSTRAINT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_CLUSTER_AVAIL`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_CLUSTER_AVAIL_DAY`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL_DAY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL_DAY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL_DAY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_CLUSTER_AVAIL_DAY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_CLUSTER_AVAIL_DAY#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_DS_PRED`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_PRED\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_PRED\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_PRED\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_PRED\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_PRED#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_DS_RUN`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_RUN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_RUN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_RUN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE01#202408010000.zip` | 20 | 2024-09-14 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_DS_RUN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_DS_RUN#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_FORECAST_TRK`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_FORECAST_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_FORECAST_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_FORECAST_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_FORECAST_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_FORECAST_TRK#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_GEN_LIMIT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_GEN_LIMIT_DAY`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT_DAY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT_DAY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT_DAY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_LIMIT_DAY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_LIMIT_DAY#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `INTERMITTENT_GEN_SCADA`

_4 pattern rows, 68 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_SCADA\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE01#202412.fmt` | 17 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_SCADA\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE01#202412.ctl` | 17 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_SCADA\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE01#202412010000.zip` | 17 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#INTERMITTENT_GEN_SCADA\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#INTERMITTENT_GEN_SCADA#FILE01#202412.sql` | 17 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `IRFMAMOUNT`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#IRFMAMOUNT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#IRFMAMOUNT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#IRFMAMOUNT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#IRFMAMOUNT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#IRFMAMOUNT#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `IRFMEVENTS`

_4 pattern rows, 80 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#IRFMEVENTS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#IRFMEVENTS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#IRFMEVENTS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#IRFMEVENTS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#IRFMEVENTS#FILE01#202408.sql` | 20 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `LOSSFACTORMODEL`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#LOSSFACTORMODEL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#LOSSFACTORMODEL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#LOSSFACTORMODEL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#LOSSFACTORMODEL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#LOSSFACTORMODEL#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `LOSSMODEL`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#LOSSMODEL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#LOSSMODEL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#LOSSMODEL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#LOSSMODEL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#LOSSMODEL#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKETFEE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKETFEE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKETFEE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKETFEE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKETFEE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKETFEE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKETFEE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKETFEE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKETFEE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKETFEE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKETFEE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKETFEE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKETFEE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKETFEEDATA`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKETFEEDATA\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKETFEEDATA\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKETFEEDATA\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKETFEEDATA\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKETFEEDATA#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKETFEETRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKETFEETRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKETFEETRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKETFEETRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKETFEETRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKETFEETRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKETNOTICETYPE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKETNOTICETYPE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKETNOTICETYPE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKETNOTICETYPE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKETNOTICETYPE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKETNOTICETYPE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKETSUSPENSION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKETSUSPENSION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKETSUSPENSION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKETSUSPENSION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKETSUSPENSION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKETSUSPENSION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKETSUSREGION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKETSUSREGION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKETSUSREGION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKETSUSREGION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKETSUSREGION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKETSUSREGION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKET_PRICE_THRESHOLDS`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKET_PRICE_THRESHOLDS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKET_PRICE_THRESHOLDS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKET_PRICE_THRESHOLDS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKET_PRICE_THRESHOLDS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKET_PRICE_THRESHOLDS#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKET_SUSPEND_REGIME_SUM`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGIME_SUM\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGIME_SUM\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGIME_SUM\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGIME_SUM\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGIME_SUM#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKET_SUSPEND_REGION_SUM`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGION_SUM\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGION_SUM\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGION_SUM\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_REGION_SUM\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_REGION_SUM#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKET_SUSPEND_SCHEDULE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MARKET_SUSPEND_SCHEDULE_TRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MARKET_SUSPEND_SCHEDULE_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MARKET_SUSPEND_SCHEDULE_TRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MCC_CASESOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MCC_CASESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MCC_CASESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MCC_CASESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MCC_CASESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MCC_CASESOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MCC_CONSTRAINTSOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MCC_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MCC_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MCC_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MCC_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MCC_CONSTRAINTSOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `METERDATA_INTERCONNECTOR`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#METERDATA_INTERCONNECTOR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#METERDATA_INTERCONNECTOR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#METERDATA_INTERCONNECTOR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#METERDATA_INTERCONNECTOR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#METERDATA_INTERCONNECTOR#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MMS_DATA_MODEL_v4.26`

_20 pattern rows, 276 files (snapshot), observed 2014-10-26 → 2017-11-01 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `Concise Guide to Data Interchange.pdf` | `Concise\ Guide\ to\ Data\ Interchange\.pdf` | `Concise Guide to Data Interchange.pdf` | 13 | 2016-10-19 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `Data Model Installation Note.pdf` | `Data\ Model\ Installation\ Note\.pdf` | `Data Model Installation Note.pdf` | 1 | 2017-11-01 | 2017-11-01 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `EMMS Release Schedule and Technical Specification June {year}.zip` | `EMMS\ Release\ Schedule\ and\ Technical\ Specification\ June\ \d{4}\.zip` | `EMMS Release Schedule and Technical Specification June 2017.zip` | 1 | 2017-06-22 | 2017-06-22 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `Guide to Troubleshooting Data Interchange.pdf` | `Guide\ to\ Troubleshooting\ Data\ Interchange\.pdf` | `Guide to Troubleshooting Data Interchange.pdf` | 13 | 2016-10-19 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `Guide to Upgrading a Standard Data Interchange Environment.pdf` | `Guide\ to\ Upgrading\ a\ Standard\ Data\ Interchange\ Environment\.pdf` | `Guide to Upgrading a Standard Data Interchange Environment.pdf` | 13 | 2016-10-19 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `Guide to setting up a standard Data Interchange environment.pdf` | `Guide\ to\ setting\ up\ a\ standard\ Data\ Interchange\ environment\.pdf` | `Guide to setting up a standard Data Interchange environment.pdf` | 13 | 2016-10-19 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_CLI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_MSSQLServer2008_v4.26.zip` | 28 | 2016-11-02 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle12c_v4.26.zip` | 14 | 2016-11-02 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle11g_v4.26.zip` | 14 | 2016-11-02 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_GUI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_MSSQLServer2008_v4.26.zip` | 28 | 2016-11-02 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle12c_v4.26.zip` | 14 | 2016-11-02 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle11g_v4.26.zip` | 14 | 2016-11-02 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model GUI Installer Guide.pdf` | `MMS\ Data\ Model\ GUI\ Installer\ Guide\.pdf` | `MMS Data Model GUI Installer Guide.pdf` | 14 | 2016-12-06 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Installation Note.pdf` | `MMS\ Data\ Model\ Installation\ Note\.pdf` | `MMS Data Model Installation Note.pdf` | 13 | 2014-10-26 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 14 | 2016-10-28 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 14 | 2016-10-28 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Table to File to Report Relationships_v{d1}.{d2}.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships_v\d{1}\.\d{2}\.xlsx` | `MMS Data Model Table to File to Report Relationships_v4.26.xlsx` | 14 | 2016-12-06 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 14 | 2016-10-28 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d1}.{d2}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{2}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v4.26.zip` | 14 | 2016-12-01 | 2017-07-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `Wholesale Systems Technical Specification - November {year}.pdf` | `Wholesale\ Systems\ Technical\ Specification\ \-\ November\ \d{4}\.pdf` | `Wholesale Systems Technical Specification - November 2016.pdf` | 13 | 2016-11-02 | 2017-07-14 |

### `MMSDM` · `MMS_DATA_MODEL_v4.27`

_15 pattern rows, 213 files (snapshot), observed 2016-12-06 → 2018-12-21 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `Data Model Installation Note.pdf` | `Data\ Model\ Installation\ Note\.pdf` | `Data Model Installation Note.pdf` | 13 | 2017-11-01 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `EMMS Release October to December {year}.zip` | `EMMS\ Release\ October\ to\ December\ \d{4}\.zip` | `EMMS Release October to December 2017.zip` | 13 | 2017-11-20 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_CLI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_MSSQLServer2012_v4.27.zip` | 26 | 2017-11-14 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle12c_v4.27.zip` | 13 | 2017-11-14 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle11g_v4.27.zip` | 13 | 2017-11-14 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_GUI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_MSSQLServer2012_v4.27.zip` | 26 | 2017-11-15 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle12c_v4.27.zip` | 13 | 2017-11-15 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle11g_v4.27.zip` | 13 | 2017-11-15 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model GUI Installer Guide.pdf` | `MMS\ Data\ Model\ GUI\ Installer\ Guide\.pdf` | `MMS Data Model GUI Installer Guide.pdf` | 13 | 2016-12-06 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 13 | 2017-11-10 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 13 | 2017-11-10 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Table to File to Report Relationships.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships\.xlsx` | `MMS Data Model Table to File to Report Relationships.xlsx` | 5 | 2018-08-21 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Table to File to Report Relationships_v{d1}.{d2}.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships_v\d{1}\.\d{2}\.xlsx` | `MMS Data Model Table to File to Report Relationships_v4.27.xlsx` | 13 | 2017-11-14 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 13 | 2017-11-10 | 2018-12-21 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS_Data_Model_pdrLoader_Configuration_Production_v{d1}.{d2}.zip` | `MMS_Data_Model_pdrLoader_Configuration_Production_v\d{1}\.\d{2}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_Production_v4.27.zip` | 13 | 2017-12-08 | 2018-12-21 |

### `MMSDM` · `MMS_DATA_MODEL_v4.28`

_14 pattern rows, 144 files (snapshot), observed 2019-03-09 → 2019-09-11 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `EMMS Release Schedule and Technical Specification - Jan {year} - Data Model v{d1}.{d2}.pdf` | `EMMS\ Release\ Schedule\ and\ Technical\ Specification\ \-\ Jan\ \d{4}\ \-\ Data\ Model\ v\d{1}\.\d{2}\.pdf` | `EMMS Release Schedule and Technical Specification - Jan 2019 - Data Model v4.28.pdf` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `EMMS - Release FAQ - January {year}.pdf` | `EMMS\ \-\ Release\ FAQ\ \-\ January\ \d{4}\.pdf` | `EMMS - Release FAQ - January 2019.pdf` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_CLI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_MSSQLServer2012_v4.28.zip` | 18 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle12c_v4.28.zip` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle11g_v4.28.zip` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_GUI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_MSSQLServer2012_v4.28.zip` | 18 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle12c_v4.28.zip` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle11g_v4.28.zip` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model GUI Installer Guide.pdf` | `MMS\ Data\ Model\ GUI\ Installer\ Guide\.pdf` | `MMS Data Model GUI Installer Guide.pdf` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Table to File to Report Relationships_v{d1}.{d2}.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships_v\d{1}\.\d{2}\.xlsx` | `MMS Data Model Table to File to Report Relationships_v4.28.xlsx` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 9 | 2019-03-09 | 2019-09-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS_Data_Model_pdrLoader_Configuration_Production_v{d1}.{d2}.zip` | `MMS_Data_Model_pdrLoader_Configuration_Production_v\d{1}\.\d{2}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_Production_v4.28.zip` | 9 | 2019-03-09 | 2019-09-11 |

### `MMSDM` · `MMS_DATA_MODEL_v4.29`

_13 pattern rows, 90 files (snapshot), observed 2019-10-11 → 2020-03-11 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `EMMS - Release Schedule and Technical Specification - SRA - October {year}.pdf` | `EMMS\ \-\ Release\ Schedule\ and\ Technical\ Specification\ \-\ SRA\ \-\ October\ \d{4}\.pdf` | `EMMS - Release Schedule and Technical Specification - SRA - October 2019.pdf` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_CLI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_MSSQLServer2014_v4.29.zip` | 12 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle12c_v4.29.zip` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle11g_v4.29.zip` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_GUI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_MSSQLServer2014_v4.29.zip` | 12 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle12c_v4.29.zip` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle11g_v4.29.zip` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model GUI Installer Guide.pdf` | `MMS\ Data\ Model\ GUI\ Installer\ Guide\.pdf` | `MMS Data Model GUI Installer Guide.pdf` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Table to File to Report Relationships_{d1}.{d2}.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships_\d{1}\.\d{2}\.xlsx` | `MMS Data Model Table to File to Report Relationships_4.29.xlsx` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 6 | 2019-10-11 | 2020-03-11 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d1}.{d2}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{2}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v4.29.zip` | 6 | 2019-10-11 | 2020-03-11 |

### `MMSDM` · `MMS_DATA_MODEL_v4.30`

_16 pattern rows, 210 files (snapshot), observed 2020-04-10 → 2021-03-23 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `EMMS Technical Specification {d1}MS Reallocations.pdf` | `EMMS\ Technical\ Specification\ \d{1}MS\ Reallocations\.pdf` | `EMMS Technical Specification 5MS Reallocations.pdf` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_CLI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_MSSQLServer2014_v4.30.zip` | 24 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle12c_v4.30.zip` | 24 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_CLI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_CLI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_CLI_Oracle11g_v4.30.zip` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_MSSQLServer{year}_v{d1}.{d2}.zip` | `MMSDM_GUI_MSSQLServer\d{4}_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_MSSQLServer2014_v4.30.zip` | 24 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}c_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}c_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle12c_v4.30.zip` | 24 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMSDM_GUI_Oracle{d21}g_v{d1}.{d22}.zip` | `MMSDM_GUI_Oracle\d{2}g_v\d{1}\.\d{2}\.zip` | `MMSDM_GUI_Oracle11g_v4.30.zip` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model GUI Installer Guide.pdf` | `MMS\ Data\ Model\ GUI\ Installer\ Guide\.pdf` | `MMS Data Model GUI Installer Guide.pdf` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Table to File to Report Relationships.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships\.xlsx` | `MMS Data Model Table to File to Report Relationships.xlsx` | 1 | 2020-04-10 | 2020-04-10 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Table to File to Report Relationships_v{d1}.{d2}.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships_v\d{1}\.\d{2}\.xlsx` | `MMS Data Model Table to File to Report Relationships_v4.30.xlsx` | 11 | 2020-05-11 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d1}.{d2}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{2}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v4.30.zip` | 12 | 2020-04-10 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `MSSQLSERVER_PATCH_GENUNITS_UNIT.sql` | `MSSQLSERVER_PATCH_GENUNITS_UNIT\.sql` | `MSSQLSERVER_PATCH_GENUNITS_UNIT.sql` | 3 | 2021-02-03 | 2021-03-23 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d2}/` | `ORACLE_PATCH_GENUNITS_UNIT.sql` | `ORACLE_PATCH_GENUNITS_UNIT\.sql` | `ORACLE_PATCH_GENUNITS_UNIT.sql` | 3 | 2021-02-03 | 2021-03-23 |

### `MMSDM` · `MMS_DATA_MODEL_v5.0`

_17 pattern rows, 147 files (snapshot), observed 2021-04-17 → 2021-10-12 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS Release FAQ - October {year} - Data Model v{d1}.{d2}.pdf` | `EMMS\ Release\ FAQ\ \-\ October\ \d{4}\ \-\ Data\ Model\ v\d{1}\.\d{2}\.pdf` | `EMMS Release FAQ - October 2020 - Data Model v5.00.pdf` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS Technical Specification - {d11}MS - Data Model v{d12}.{d2}.pdf` | `EMMS\ Technical\ Specification\ \-\ \d{1}MS\ \-\ Data\ Model\ v\d{1}\.\d{2}\.pdf` | `EMMS Technical Specification - 5MS - Data Model v5.00.pdf` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_CLI_MSSQLServer{year}_v{d11}.{d12}.zip` | `MMSDM_CLI_MSSQLServer\d{4}_v\d{1}\.\d{1}\.zip` | `MMSDM_CLI_MSSQLServer2014_v5.0.zip` | 14 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_CLI_Oracle{d2}c_v{d11}.{d12}.zip` | `MMSDM_CLI_Oracle\d{2}c_v\d{1}\.\d{1}\.zip` | `MMSDM_CLI_Oracle12c_v5.0.zip` | 14 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_GUI_MSSQLServer{year}_v{d11}.{d12}.zip` | `MMSDM_GUI_MSSQLServer\d{4}_v\d{1}\.\d{1}\.zip` | `MMSDM_GUI_MSSQLServer2014_v5.0.zip` | 14 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_GUI_Oracle{d2}c_v{d11}.{d12}.zip` | `MMSDM_GUI_Oracle\d{2}c_v\d{1}\.\d{1}\.zip` | `MMSDM_GUI_Oracle12c_v5.0.zip` | 14 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model GUI Installer Guide.pdf` | `MMS\ Data\ Model\ GUI\ Installer\ Guide\.pdf` | `MMS Data Model GUI Installer Guide.pdf` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Table to File to Report Relationships.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships\.xlsx` | `MMS Data Model Table to File to Report Relationships.xlsx` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model v{d11}.{d12} Release Notes.pdf` | `MMS\ Data\ Model\ v\d{1}\.\d{1}\ Release\ Notes\.pdf` | `MMS Data Model v5.0 Release Notes.pdf` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d11}.{d12}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{1}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v5.0.zip` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MSSQLSERVER_PATCH_GENUNITS_UNIT.sql` | `MSSQLSERVER_PATCH_GENUNITS_UNIT\.sql` | `MSSQLSERVER_PATCH_GENUNITS_UNIT.sql` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MSSQLSERVER_PATCH_SETTLEMENTS.sql` | `MSSQLSERVER_PATCH_SETTLEMENTS\.sql` | `MSSQLSERVER_PATCH_SETTLEMENTS.sql` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `ORACLE_PATCH_GENUNITS_UNIT.sql` | `ORACLE_PATCH_GENUNITS_UNIT\.sql` | `ORACLE_PATCH_GENUNITS_UNIT.sql` | 7 | 2021-04-17 | 2021-10-12 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `ORACLE_PATCH_SETTLEMENTS.sql` | `ORACLE_PATCH_SETTLEMENTS\.sql` | `ORACLE_PATCH_SETTLEMENTS.sql` | 7 | 2021-04-17 | 2021-10-12 |

### `MMSDM` · `MMS_DATA_MODEL_v5.1`

_15 pattern rows, 232 files (snapshot), observed 2021-11-10 → 2023-05-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS Release Schedule and Technical Specification - October {year}.pdf` | `EMMS\ Release\ Schedule\ and\ Technical\ Specification\ \-\ October\ \d{4}\.pdf` | `EMMS Release Schedule and Technical Specification - October 2021.pdf` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_CLI_MSSQLServer_v{d11}.{d12}.zip` | `MMSDM_CLI_MSSQLServer_v\d{1}\.\d{1}\.zip` | `MMSDM_CLI_MSSQLServer_v5.1.zip` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_CLI_Oracle_v{d11}.{d12}.zip` | `MMSDM_CLI_Oracle_v\d{1}\.\d{1}\.zip` | `MMSDM_CLI_Oracle_v5.1.zip` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_GUI_MSSQLServer_v{d11}.{d12}.zip` | `MMSDM_GUI_MSSQLServer_v\d{1}\.\d{1}\.zip` | `MMSDM_GUI_MSSQLServer_v5.1.zip` | 11 | 2021-11-10 | 2022-09-10 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_GUI_Oracle_v{d11}.{d12}.zip` | `MMSDM_GUI_Oracle_v\d{1}\.\d{1}\.zip` | `MMSDM_GUI_Oracle_v5.1.zip` | 11 | 2021-11-10 | 2022-09-10 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_create_v{d11}.{d12}.zip` | `MMSDM_create_v\d{1}\.\d{1}\.zip` | `MMSDM_create_v5.1.zip` | 7 | 2022-10-09 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_upgrade_v{d11}.{d12}.zip` | `MMSDM_upgrade_v\d{1}\.\d{1}\.zip` | `MMSDM_upgrade_v5.1.zip` | 7 | 2022-10-09 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Release Notes v{d11}.{d12}.pdf` | `MMS\ Data\ Model\ Release\ Notes\ v\d{1}\.\d{1}\.pdf` | `MMS Data Model Release Notes v5.1.pdf` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Table to File to Report Relationships.xlsx` | `MMS\ Data\ Model\ Table\ to\ File\ to\ Report\ Relationships\.xlsx` | `MMS Data Model Table to File to Report Relationships.xlsx` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d11}.{d12}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{1}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v5.1.zip` | 18 | 2021-11-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `ORACLE_PATCH_VOLTAGE_INSTRUCTION.sql` | `ORACLE_PATCH_VOLTAGE_INSTRUCTION\.sql` | `ORACLE_PATCH_VOLTAGE_INSTRUCTION.sql` | 17 | 2021-12-10 | 2023-05-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `SQLSERVER_PATCH_VOLTAGE_INSTRUCTION.sql` | `SQLSERVER_PATCH_VOLTAGE_INSTRUCTION\.sql` | `SQLSERVER_PATCH_VOLTAGE_INSTRUCTION.sql` | 17 | 2021-12-10 | 2023-05-17 |

### `MMSDM` · `MMS_DATA_MODEL_v5.2`

_8 pattern rows, 80 files (snapshot), observed 2023-06-12 → 2024-03-09 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS - Technical Specification - Data Model v{d11}.{d12} - May {year} comparison.pdf` | `EMMS\ \-\ Technical\ Specification\ \-\ Data\ Model\ v\d{1}\.\d{1}\ \-\ May\ \d{4}\ comparison\.pdf` | `EMMS - Technical Specification - Data Model v5.2 - May 2023 comparison.pdf` | 10 | 2023-06-12 | 2024-03-09 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS - Technical Specification - Data Model v{d11}.{d12} - May {year}.pdf` | `EMMS\ \-\ Technical\ Specification\ \-\ Data\ Model\ v\d{1}\.\d{1}\ \-\ May\ \d{4}\.pdf` | `EMMS - Technical Specification - Data Model v5.2 - May 2023.pdf` | 10 | 2023-06-12 | 2024-03-09 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_create_v{d11}.{d12}.zip` | `MMSDM_create_v\d{1}\.\d{1}\.zip` | `MMSDM_create_v5.2.zip` | 10 | 2023-06-12 | 2024-03-09 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_upgrade_v{d11}.{d12}.zip` | `MMSDM_upgrade_v\d{1}\.\d{1}\.zip` | `MMSDM_upgrade_v5.2.zip` | 10 | 2023-06-12 | 2024-03-09 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 10 | 2023-06-12 | 2024-03-09 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 10 | 2023-06-12 | 2024-03-09 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 10 | 2023-06-12 | 2024-03-09 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d11}.{d12}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{1}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v5.2.zip` | 10 | 2023-06-12 | 2024-03-09 |

### `MMSDM` · `MMS_DATA_MODEL_v5.3`

_9 pattern rows, 63 files (snapshot), observed 2024-02-27 → 2024-09-13 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS Technical Specification - Data Model v{d11}.{d12} - April {year} markedup.pdf` | `EMMS\ Technical\ Specification\ \-\ Data\ Model\ v\d{1}\.\d{1}\ \-\ April\ \d{4}\ markedup\.pdf` | `EMMS Technical Specification - Data Model v5.3 - April 2024 markedup.pdf` | 7 | 2024-03-13 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS Technical Specification - Data Model v{d11}.{d12} - April {year}.pdf` | `EMMS\ Technical\ Specification\ \-\ Data\ Model\ v\d{1}\.\d{1}\ \-\ April\ \d{4}\.pdf` | `EMMS Technical Specification - Data Model v5.3 - April 2024.pdf` | 7 | 2024-03-13 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_create_v{d11}.{d12}.zip` | `MMSDM_create_v\d{1}\.\d{1}\.zip` | `MMSDM_create_v5.3.zip` | 7 | 2024-02-27 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_upgrade_v{d11}.{d12}.zip` | `MMSDM_upgrade_v\d{1}\.\d{1}\.zip` | `MMSDM_upgrade_v5.3.zip` | 7 | 2024-02-27 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Package Summary.pdf` | `MMS\ Data\ Model\ Package\ Summary\.pdf` | `MMS Data Model Package Summary.pdf` | 7 | 2024-03-06 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Report.pdf` | `MMS\ Data\ Model\ Report\.pdf` | `MMS Data Model Report.pdf` | 7 | 2024-03-06 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model Upgrade Report.pdf` | `MMS\ Data\ Model\ Upgrade\ Report\.pdf` | `MMS Data Model Upgrade Report.pdf` | 7 | 2024-03-07 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS Data Model v{d11}.{d12} Release Notes.pdf` | `MMS\ Data\ Model\ v\d{1}\.\d{1}\ Release\ Notes\.pdf` | `MMS Data Model v5.3 Release Notes.pdf` | 7 | 2024-03-13 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d11}.{d12}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{1}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v5.3.zip` | 7 | 2024-04-10 | 2024-09-13 |

### `MMSDM` · `MMS_DATA_MODEL_v5.3_PreRelease`

_6 pattern rows, 48 files (snapshot), observed 2024-01-22 → 2024-09-13 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}_PreRelease/` | `EMMS - Technical Specification Data Model v{d11}.{d12} - April {year}.pdf` | `EMMS\ \-\ Technical\ Specification\ Data\ Model\ v\d{1}\.\d{1}\ \-\ April\ \d{4}\.pdf` | `EMMS - Technical Specification Data Model v5.3 - April 2024.pdf` | 8 | 2024-01-22 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}_PreRelease/` | `MMSDM_Bidoffer_Transition.zip` | `MMSDM_Bidoffer_Transition\.zip` | `MMSDM_Bidoffer_Transition.zip` | 8 | 2024-02-02 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}_PreRelease/` | `MMSDM_Switch_Bidoffer_Table_Names_v{d11}.{d12}.zip` | `MMSDM_Switch_Bidoffer_Table_Names_v\d{1}\.\d{1}\.zip` | `MMSDM_Switch_Bidoffer_Table_Names_v1.1.zip` | 8 | 2024-02-05 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}_PreRelease/` | `MMSDM_upgrade_v{d11}.{d12}_PRE.zip` | `MMSDM_upgrade_v\d{1}\.\d{1}_PRE\.zip` | `MMSDM_upgrade_v5.3_PRE.zip` | 8 | 2024-02-05 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}_PreRelease/` | `MMS Data Model v{d11}.{d12}_PreRelease Release Notes.pdf` | `MMS\ Data\ Model\ v\d{1}\.\d{1}_PreRelease\ Release\ Notes\.pdf` | `MMS Data Model v5.3_PreRelease Release Notes.pdf` | 8 | 2024-02-02 | 2024-09-13 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}_PreRelease/` | `MMS_Data_Model_pdrLoader_Configuration_Production_v{d11}.{d12}_PreRelease.zip` | `MMS_Data_Model_pdrLoader_Configuration_Production_v\d{1}\.\d{1}_PreRelease\.zip` | `MMS_Data_Model_pdrLoader_Configuration_Production_v5.3_PreRelease.zip` | 8 | 2024-02-02 | 2024-09-13 |

### `MMSDM` · `MMS_DATA_MODEL_v5.4`

_7 pattern rows, 42 files (snapshot), observed 2024-09-23 → 2025-10-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS - Technical Specification - Data Model v{d11}.{d12} - November {year}.pdf` | `EMMS\ \-\ Technical\ Specification\ \-\ Data\ Model\ v\d{1}\.\d{1}\ \-\ November\ \d{4}\.pdf` | `EMMS - Technical Specification - Data Model v5.4 - November 2024.pdf` | 6 | 2024-10-08 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Package Summary.pdf` | `Electricity\ Data\ Model\ Package\ Summary\.pdf` | `Electricity Data Model Package Summary.pdf` | 6 | 2024-10-07 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Report.pdf` | `Electricity\ Data\ Model\ Report\.pdf` | `Electricity Data Model Report.pdf` | 6 | 2024-10-07 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Upgrade Report.pdf` | `Electricity\ Data\ Model\ Upgrade\ Report\.pdf` | `Electricity Data Model Upgrade Report.pdf` | 6 | 2024-10-07 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_create_v{d11}.{d12}.zip` | `MMSDM_create_v\d{1}\.\d{1}\.zip` | `MMSDM_create_v5.4.zip` | 6 | 2024-09-23 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_upgrade_v{d11}.{d12}.zip` | `MMSDM_upgrade_v\d{1}\.\d{1}\.zip` | `MMSDM_upgrade_v5.4.zip` | 6 | 2024-09-23 | 2025-10-17 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d11}.{d12}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{1}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v5.4.zip` | 6 | 2024-11-07 | 2025-10-17 |

### `MMSDM` · `MMS_DATA_MODEL_v5.5`

_7 pattern rows, 49 files (snapshot), observed 2025-03-24 → 2025-04-29 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS DMv{d11}.{d12} Apr{d2}.pdf` | `EMMS\ DMv\d{1}\.\d{1}\ Apr\d{2}\.pdf` | `EMMS DMv5.5 Apr25.pdf` | 7 | 2025-04-29 | 2025-04-29 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Package Summary.pdf` | `Electricity\ Data\ Model\ Package\ Summary\.pdf` | `Electricity Data Model Package Summary.pdf` | 7 | 2025-03-24 | 2025-03-24 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Report.pdf` | `Electricity\ Data\ Model\ Report\.pdf` | `Electricity Data Model Report.pdf` | 7 | 2025-03-24 | 2025-03-24 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Upgrade Report.pdf` | `Electricity\ Data\ Model\ Upgrade\ Report\.pdf` | `Electricity Data Model Upgrade Report.pdf` | 7 | 2025-03-24 | 2025-03-24 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_create_v{d11}.{d12}.zip` | `MMSDM_create_v\d{1}\.\d{1}\.zip` | `MMSDM_create_v5.5.zip` | 7 | 2025-04-29 | 2025-04-29 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_upgrade_v{d11}.{d12}.zip` | `MMSDM_upgrade_v\d{1}\.\d{1}\.zip` | `MMSDM_upgrade_v5.5.zip` | 7 | 2025-04-29 | 2025-04-29 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d11}.{d12}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{1}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v5.5.zip` | 7 | 2025-04-29 | 2025-04-29 |

### `MMSDM` · `MMS_DATA_MODEL_v5.6`

_7 pattern rows, 42 files (snapshot), observed 2025-10-14 → 2025-11-26 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `EMMS DM{d11}.{d12} Nov{year}.pdf` | `EMMS\ DM\d{1}\.\d{1}\ Nov\d{4}\.pdf` | `EMMS DM5.6 Nov2025.pdf` | 6 | 2025-11-18 | 2025-11-26 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Package Summary.pdf` | `Electricity\ Data\ Model\ Package\ Summary\.pdf` | `Electricity Data Model Package Summary.pdf` | 6 | 2025-10-14 | 2025-10-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Report.pdf` | `Electricity\ Data\ Model\ Report\.pdf` | `Electricity Data Model Report.pdf` | 6 | 2025-10-14 | 2025-10-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `Electricity Data Model Upgrade Report.pdf` | `Electricity\ Data\ Model\ Upgrade\ Report\.pdf` | `Electricity Data Model Upgrade Report.pdf` | 6 | 2025-10-14 | 2025-10-14 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_create_v{d11}.{d12}.zip` | `MMSDM_create_v\d{1}\.\d{1}\.zip` | `MMSDM_create_v5.6.zip` | 6 | 2025-11-19 | 2025-11-19 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMSDM_upgrade_{d11}.{d12}.zip` | `MMSDM_upgrade_\d{1}\.\d{1}\.zip` | `MMSDM_upgrade_5.6.zip` | 6 | 2025-11-19 | 2025-11-19 |
| `DOCUMENTATION` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/MMS Data Model/v{d1}.{d1}/` | `MMS_Data_Model_pdrLoader_Configuration_production_v{d11}.{d12}.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v\d{1}\.\d{1}\.zip` | `MMS_Data_Model_pdrLoader_Configuration_production_v5.6.zip` | 6 | 2025-11-19 | 2025-11-19 |

### `MMSDM` · `MNSP_BIDOFFERPERIOD`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MNSP_BIDOFFERPERIOD\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MNSP_BIDOFFERPERIOD\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MNSP_BIDOFFERPERIOD\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MNSP_BIDOFFERPERIOD\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MNSP_BIDOFFERPERIOD#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MNSP_DAYOFFER`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MNSP_DAYOFFER\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MNSP_DAYOFFER\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MNSP_DAYOFFER\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MNSP_DAYOFFER\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MNSP_DAYOFFER#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MNSP_INTERCONNECTOR`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MNSP_INTERCONNECTOR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MNSP_INTERCONNECTOR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MNSP_INTERCONNECTOR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MNSP_INTERCONNECTOR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MNSP_INTERCONNECTOR#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MNSP_PARTICIPANT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MNSP_PARTICIPANT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MNSP_PARTICIPANT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MNSP_PARTICIPANT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MNSP_PARTICIPANT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MNSP_PARTICIPANT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_CASERESULT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_CASERESULT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_CASERESULT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_CASERESULT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_CASERESULT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_CASERESULT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_CONSTRAINTRESULT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTRESULT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTRESULT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTRESULT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTRESULT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTRESULT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_CONSTRAINTSUMMARY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTSUMMARY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTSUMMARY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTSUMMARY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_CONSTRAINTSUMMARY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_CONSTRAINTSUMMARY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_DATA_EXPORT`

_2 pattern rows, 7 files (snapshot), observed 2019-10-23 → 2019-10-24 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `MTPASA_DATA_EXPORT` | `/Data_Archive/Wholesale_Electricity/MMSDM/MTPASA_DATA_EXPORT/` | `PUBLIC_MTPASA_REGIONAVAIL_TRK_{datetime}_NEM{d2}.zip` | `PUBLIC_MTPASA_REGIONAVAIL_TRK_\d{14}_NEM\d{2}\.zip` | `PUBLIC_MTPASA_REGIONAVAIL_TRK_20191024093822_NEM02.zip` | 1 | 2019-10-24 | 2019-10-24 |
| `MTPASA_DATA_EXPORT` | `/Data_Archive/Wholesale_Electricity/MMSDM/MTPASA_DATA_EXPORT/` | `{year}_DATA_EXPORT_MTPASA_REGIONAVAILABILITY.zip` | `\d{4}_DATA_EXPORT_MTPASA_REGIONAVAILABILITY\.zip` | `2014_DATA_EXPORT_MTPASA_REGIONAVAILABILITY.zip` | 6 | 2019-10-23 | 2019-10-23 |

### `MMSDM` · `MTPASA_DUIDAVAILABILITY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_DUIDAVAILABILITY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_INTERCONNECTORRESULT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_INTERCONNECTORRESULT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_INTERCONNECTORRESULT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_INTERCONNECTORRESULT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_INTERCONNECTORRESULT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_INTERCONNECTORRESULT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_LOLPRESULT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_LOLPRESULT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_LOLPRESULT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_LOLPRESULT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_LOLPRESULT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_LOLPRESULT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_REGIONAVAILABILITY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAILABILITY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAILABILITY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAILABILITY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAILABILITY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAILABILITY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_REGIONAVAIL_TRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAIL_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAIL_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAIL_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_REGIONAVAIL_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_REGIONAVAIL_TRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_REGIONITERATION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_REGIONITERATION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_REGIONITERATION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_REGIONITERATION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_REGIONITERATION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_REGIONITERATION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_REGIONRESULT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_REGIONRESULT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_REGIONRESULT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_REGIONRESULT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_REGIONRESULT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_REGIONRESULT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_REGIONSUMMARY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_REGIONSUMMARY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_REGIONSUMMARY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_REGIONSUMMARY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_REGIONSUMMARY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_REGIONSUMMARY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_RESERVELIMIT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_RESERVELIMIT_REGION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_REGION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_REGION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_REGION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_REGION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_REGION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `MTPASA_RESERVELIMIT_SET`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_SET\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_SET\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_SET\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#MTPASA_RESERVELIMIT_SET\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#MTPASA_RESERVELIMIT_SET#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NEGATIVE_RESIDUE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NEGATIVE_RESIDUE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NEGATIVE_RESIDUE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NEGATIVE_RESIDUE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NEGATIVE_RESIDUE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NEGATIVE_RESIDUE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NETWORK_EQUIPMENTDETAIL`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-14 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NETWORK_EQUIPMENTDETAIL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NETWORK_EQUIPMENTDETAIL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NETWORK_EQUIPMENTDETAIL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-14 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NETWORK_EQUIPMENTDETAIL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NETWORK_EQUIPMENTDETAIL#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NETWORK_OUTAGECONSTRAINTSET`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGECONSTRAINTSET\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGECONSTRAINTSET\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGECONSTRAINTSET\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGECONSTRAINTSET\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NETWORK_OUTAGECONSTRAINTSET#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NETWORK_OUTAGEDETAIL`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGEDETAIL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGEDETAIL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGEDETAIL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGEDETAIL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NETWORK_OUTAGEDETAIL#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NETWORK_OUTAGESTATUSCODE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGESTATUSCODE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGESTATUSCODE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGESTATUSCODE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NETWORK_OUTAGESTATUSCODE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NETWORK_OUTAGESTATUSCODE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NETWORK_RATING`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NETWORK_RATING\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NETWORK_RATING\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NETWORK_RATING\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NETWORK_RATING\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NETWORK_RATING#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NETWORK_STATICRATING`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NETWORK_STATICRATING\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NETWORK_STATICRATING\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NETWORK_STATICRATING\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NETWORK_STATICRATING\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NETWORK_STATICRATING#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `NETWORK_SUBSTATIONDETAIL`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#NETWORK_SUBSTATIONDETAIL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#NETWORK_SUBSTATIONDETAIL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#NETWORK_SUBSTATIONDETAIL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#NETWORK_SUBSTATIONDETAIL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#NETWORK_SUBSTATIONDETAIL#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `OVERRIDERRP`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#OVERRIDERRP\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#OVERRIDERRP\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#OVERRIDERRP\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#OVERRIDERRP\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#OVERRIDERRP#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `P5MIN_BLOCKEDCONSTRAINT`

_4 pattern rows, 43 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_BLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_BLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_BLOCKEDCONSTRAINT#FILE01#202409.fmt` | 11 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_BLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_BLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_BLOCKEDCONSTRAINT#FILE01#202409.ctl` | 11 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_BLOCKEDCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_BLOCKEDCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_BLOCKEDCONSTRAINT#FILE01#202409010000.zip` | 11 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_BLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_BLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_BLOCKEDCONSTRAINT#FILE01#202409.sql` | 10 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `P5MIN_CASESOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_CASESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CASESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_CASESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_CASESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CASESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_CASESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_CASESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CASESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_CASESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_CASESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CASESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_CASESOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `P5MIN_CONSTRAINTSOLUTION`

_5 pattern rows, 297 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_CONSTRAINTSOLUTION#FILE01#202408.fmt` | 60 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_CONSTRAINTSOLUTION#FILE01#202408.ctl` | 60 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_CONSTRAINTSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_CONSTRAINTSOLUTION#FILE01#202408010000.zip` | 60 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_CONSTRAINTSOLUTION#FILE01#202408.sql` | 57 | 2024-09-13 | 2026-04-08 |
| `P5MIN_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/P{d1}MIN_ALL_DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_CONSTRAINTSOLUTION#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_CONSTRAINTSOLUTION\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_CONSTRAINTSOLUTION#ALL#FILE01#202408010000.zip` | 60 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `P5MIN_FCAS_REQ_CONSTRAINT`

_4 pattern rows, 775 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_CONSTRAINT#FILE01#202412.fmt` | 197 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_CONSTRAINT#FILE01#202412.ctl` | 197 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_CONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_CONSTRAINT#FILE01#202412010000.zip` | 197 | 2025-01-10 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_CONSTRAINT#FILE01#202412.sql` | 184 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `P5MIN_FCAS_REQ_RUN`

_4 pattern rows, 63 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_RUN#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_RUN#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_RUN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_RUN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_RUN#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_FCAS_REQ_RUN#FILE01#202412.sql` | 15 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `P5MIN_INTERCONNECTORSOLN`

_5 pattern rows, 99 files (snapshot), observed 2024-09-12 → 2026-04-14 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_INTERCONNECTORSOLN#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_INTERCONNECTORSOLN#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERCONNECTORSOLN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERCONNECTORSOLN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_INTERCONNECTORSOLN#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-14 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_INTERCONNECTORSOLN#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |
| `P5MIN_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/P{d1}MIN_ALL_DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERCONNECTORSOLN#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERCONNECTORSOLN\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_INTERCONNECTORSOLN#ALL#FILE01#202408010000.zip` | 20 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `P5MIN_INTERSENSITIVITIES`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERSENSITIVITIES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERSENSITIVITIES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_INTERSENSITIVITIES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERSENSITIVITIES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERSENSITIVITIES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_INTERSENSITIVITIES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERSENSITIVITIES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERSENSITIVITIES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_INTERSENSITIVITIES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_INTERSENSITIVITIES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_INTERSENSITIVITIES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_INTERSENSITIVITIES#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `P5MIN_LOCAL_PRICE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_LOCAL_PRICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_LOCAL_PRICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_LOCAL_PRICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_LOCAL_PRICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_LOCAL_PRICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_LOCAL_PRICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_LOCAL_PRICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_LOCAL_PRICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_LOCAL_PRICE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `P5MIN_PRICESENSITIVITIES`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_PRICESENSITIVITIES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_PRICESENSITIVITIES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_PRICESENSITIVITIES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_PRICESENSITIVITIES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_PRICESENSITIVITIES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_PRICESENSITIVITIES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_PRICESENSITIVITIES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_PRICESENSITIVITIES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_PRICESENSITIVITIES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_PRICESENSITIVITIES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_PRICESENSITIVITIES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_PRICESENSITIVITIES#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `P5MIN_REGIONSOLUTION`

_5 pattern rows, 99 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_REGIONSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_REGIONSOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_REGIONSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_REGIONSOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_REGIONSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_REGIONSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_REGIONSOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_REGIONSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_REGIONSOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |
| `P5MIN_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/P{d1}MIN_ALL_DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_REGIONSOLUTION#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_REGIONSOLUTION\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_REGIONSOLUTION#ALL#FILE01#202408010000.zip` | 20 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `P5MIN_SCENARIODEMAND`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMAND#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMAND\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMAND#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMAND#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMAND\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMAND#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMAND#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMAND\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMAND#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMAND#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMAND\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMAND#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `P5MIN_SCENARIODEMANDTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMANDTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMANDTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMANDTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMANDTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMANDTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMANDTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMANDTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMANDTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMANDTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#P{d1}MIN_SCENARIODEMANDTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#P\d{1}MIN_SCENARIODEMANDTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#P5MIN_SCENARIODEMANDTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PARTICIPANT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PARTICIPANT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PARTICIPANT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PARTICIPANT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PARTICIPANT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PARTICIPANT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PARTICIPANTCATEGORY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PARTICIPANTCATEGORYALLOC`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORYALLOC\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORYALLOC\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORYALLOC\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PARTICIPANTCATEGORYALLOC\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PARTICIPANTCATEGORYALLOC#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PARTICIPANTCLASS`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PARTICIPANTCLASS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PARTICIPANTCLASS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PARTICIPANTCLASS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PARTICIPANTCLASS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PARTICIPANTCLASS#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PD7DAY_CASESOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CASESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CASESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PD7DAY_CASESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CASESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CASESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PD7DAY_CASESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CASESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CASESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PD7DAY_CASESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CASESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CASESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PD7DAY_CASESOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PD7DAY_CONSTRAINTSOLUTION`

_4 pattern rows, 528 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PD7DAY_CONSTRAINTSOLUTION#FILE01#202408.fmt` | 134 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PD7DAY_CONSTRAINTSOLUTION#FILE01#202408.ctl` | 134 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CONSTRAINTSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PD7DAY_CONSTRAINTSOLUTION#FILE01#202408010000.zip` | 134 | 2024-09-13 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PD7DAY_CONSTRAINTSOLUTION#FILE01#202408.sql` | 126 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PD7DAY_INTERCONNECTORSOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PD{d1}DAY_INTERCONNECTORSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_INTERCONNECTORSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PD7DAY_INTERCONNECTORSOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_INTERCONNECTORSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_INTERCONNECTORSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PD7DAY_INTERCONNECTORSOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PD{d1}DAY_INTERCONNECTORSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_INTERCONNECTORSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PD7DAY_INTERCONNECTORSOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_INTERCONNECTORSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_INTERCONNECTORSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PD7DAY_INTERCONNECTORSOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PD7DAY_MARKET_SUMMARY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PD{d1}DAY_MARKET_SUMMARY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_MARKET_SUMMARY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PD7DAY_MARKET_SUMMARY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_MARKET_SUMMARY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_MARKET_SUMMARY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PD7DAY_MARKET_SUMMARY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PD{d1}DAY_MARKET_SUMMARY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_MARKET_SUMMARY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PD7DAY_MARKET_SUMMARY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_MARKET_SUMMARY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_MARKET_SUMMARY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PD7DAY_MARKET_SUMMARY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PD7DAY_PRICESOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PD{d1}DAY_PRICESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_PRICESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PD7DAY_PRICESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_PRICESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_PRICESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PD7DAY_PRICESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PD{d1}DAY_PRICESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_PRICESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PD7DAY_PRICESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PD{d1}DAY_PRICESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PD\d{1}DAY_PRICESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PD7DAY_PRICESOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PDPASA_CASESOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PDPASA_CASESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PDPASA_CASESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PDPASA_CASESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PDPASA_CASESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PDPASA_CASESOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PDPASA_CONSTRAINTSOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PDPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PDPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PDPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PDPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PDPASA_CONSTRAINTSOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PDPASA_DUIDAVAILABILITY`

_4 pattern rows, 118 files (snapshot), observed 2025-08-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PDPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE01#202507.fmt` | 30 | 2025-08-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PDPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE01#202507.ctl` | 30 | 2025-08-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PDPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE01#202507010000.zip` | 30 | 2025-08-08 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PDPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PDPASA_DUIDAVAILABILITY#FILE01#202507.sql` | 28 | 2025-08-08 | 2026-04-08 |

### `MMSDM` · `PDPASA_INTERCONNECTORSOLN`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PDPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PDPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PDPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PDPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PDPASA_INTERCONNECTORSOLN#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PDPASA_REGIONSOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PDPASA_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PDPASA_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PDPASA_REGIONSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PDPASA_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PDPASA_REGIONSOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PD_FCAS_REQ_CONSTRAINT`

_4 pattern rows, 641 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE01#202412.fmt` | 163 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE01#202412.ctl` | 163 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE01#202412010000.zip` | 163 | 2025-01-10 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_CONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_CONSTRAINT#FILE01#202412.sql` | 152 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `PD_FCAS_REQ_RUN`

_4 pattern rows, 63 files (snapshot), observed 2025-01-10 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE01#202412.fmt` | 16 | 2025-01-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE01#202412.ctl` | 16 | 2025-01-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_RUN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE01#202412010000.zip` | 16 | 2025-01-10 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PD_FCAS_REQ_RUN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PD_FCAS_REQ_RUN#FILE01#202412.sql` | 15 | 2025-01-10 | 2026-04-08 |

### `MMSDM` · `PERDEMAND`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PERDEMAND#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PERDEMAND\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PERDEMAND#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PERDEMAND#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PERDEMAND\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PERDEMAND#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PERDEMAND#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PERDEMAND\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PERDEMAND#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PERDEMAND#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PERDEMAND\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PERDEMAND#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PMS_GROUP`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PMS_GROUP\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PMS_GROUP\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PMS_GROUP\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PMS_GROUP\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PMS_GROUP#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PMS_GROUPSERVICE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PMS_GROUPSERVICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PMS_GROUPSERVICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PMS_GROUPSERVICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PMS_GROUPSERVICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PMS_GROUPSERVICE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PREDISPATCHBLOCKEDCONSTRAINT`

_4 pattern rows, 35 files (snapshot), observed 2025-06-10 → 2026-03-10 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE01#202502.fmt` | 9 | 2025-06-10 | 2026-03-10 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE01#202502.ctl` | 9 | 2025-06-10 | 2026-03-10 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE01#202502010000.zip` | 9 | 2025-06-10 | 2026-03-09 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHBLOCKEDCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHBLOCKEDCONSTRAINT#FILE01#202502.sql` | 8 | 2025-06-10 | 2026-03-10 |

### `MMSDM` · `PREDISPATCHCASESOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHCASESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHCASESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHCASESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHCASESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHCASESOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PREDISPATCHCONSTRAINT`

_5 pattern rows, 121 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHCONSTRAINT\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHCONSTRAINT#ALL#FILE01#202408010000.zip` | 42 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `PREDISPATCHINTERCONNECTORRES`

_5 pattern rows, 99 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHINTERCONNECTORRES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHINTERCONNECTORRES\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHINTERCONNECTORRES#ALL#FILE01#202408010000.zip` | 20 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `PREDISPATCHLOAD`

_5 pattern rows, 99 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHLOAD\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHLOAD\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHLOAD\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHLOAD\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHLOAD\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHLOAD#ALL#FILE01#202408010000.zip` | 20 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `PREDISPATCHOFFERTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHOFFERTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHOFFERTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHOFFERTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHOFFERTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHOFFERTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PREDISPATCHPRICE`

_5 pattern rows, 99 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICE\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHPRICE#ALL#FILE01#202408010000.zip` | 20 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `PREDISPATCHPRICESENSITIVITIES`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICESENSITIVITIES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICESENSITIVITIES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICESENSITIVITIES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHPRICESENSITIVITIES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHPRICESENSITIVITIES#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PREDISPATCHREGIONSUM`

_5 pattern rows, 99 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHREGIONSUM\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHREGIONSUM\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHREGIONSUM\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHREGIONSUM\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#ALL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHREGIONSUM\#ALL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHREGIONSUM#ALL#FILE01#202408010000.zip` | 20 | 2024-09-13 | 2026-04-07 |

### `MMSDM` · `PREDISPATCHSCENARIODEMAND`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMAND\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMAND\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMAND\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMAND\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMAND#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PREDISPATCHSCENARIODEMANDTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMANDTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMANDTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMANDTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCHSCENARIODEMANDTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCHSCENARIODEMANDTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PREDISPATCH_FCAS_REQ`

_4 pattern rows, 40 files (snapshot), observed 2024-09-12 → 2025-10-17 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCH_FCAS_REQ\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE01#202408.fmt` | 10 | 2024-09-12 | 2025-10-17 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCH_FCAS_REQ\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE01#202408.ctl` | 10 | 2024-09-12 | 2025-10-17 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCH_FCAS_REQ\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE01#202408010000.zip` | 10 | 2024-09-12 | 2025-10-17 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCH_FCAS_REQ\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCH_FCAS_REQ#FILE01#202408.sql` | 10 | 2024-09-13 | 2025-10-17 |

### `MMSDM` · `PREDISPATCH_LOCAL_PRICE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCH_LOCAL_PRICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCH_LOCAL_PRICE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PREDISPATCH_MNSPBIDTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PREDISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PREDISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PREDISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PREDISPATCH_MNSPBIDTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PREDISPATCH_MNSPBIDTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `PRUDENTIALRUNTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#PRUDENTIALRUNTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#PRUDENTIALRUNTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#PRUDENTIALRUNTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#PRUDENTIALRUNTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#PRUDENTIALRUNTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `REGION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#REGION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#REGION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#REGION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#REGION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#REGION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#REGION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#REGION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#REGION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#REGION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#REGION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#REGION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#REGION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `REGIONAPC`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#REGIONAPC#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#REGIONAPC\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#REGIONAPC#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#REGIONAPC#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#REGIONAPC\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#REGIONAPC#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#REGIONAPC#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#REGIONAPC\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#REGIONAPC#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#REGIONAPC#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#REGIONAPC\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#REGIONAPC#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `REGIONAPCINTERVALS`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#REGIONAPCINTERVALS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#REGIONAPCINTERVALS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#REGIONAPCINTERVALS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#REGIONAPCINTERVALS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#REGIONAPCINTERVALS#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `REGIONSTANDINGDATA`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#REGIONSTANDINGDATA\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#REGIONSTANDINGDATA\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#REGIONSTANDINGDATA\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#REGIONSTANDINGDATA\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#REGIONSTANDINGDATA#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `RESDEMANDTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#RESDEMANDTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#RESDEMANDTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#RESDEMANDTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#RESDEMANDTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#RESDEMANDTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `RESIDUE_CONTRACTS`

_4 pattern rows, 51 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#RESIDUE_CONTRACTS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE01#202409.fmt` | 13 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#RESIDUE_CONTRACTS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE01#202409.ctl` | 13 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#RESIDUE_CONTRACTS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE01#202409010000.zip` | 13 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#RESIDUE_CONTRACTS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#RESIDUE_CONTRACTS#FILE01#202409.sql` | 12 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `RESIDUE_CON_FUNDS`

_4 pattern rows, 24 files (snapshot), observed 2024-11-11 → 2026-02-10 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#RESIDUE_CON_FUNDS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE01#202410.fmt` | 6 | 2024-11-11 | 2026-02-10 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#RESIDUE_CON_FUNDS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE01#202410.ctl` | 6 | 2024-11-11 | 2026-02-10 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#RESIDUE_CON_FUNDS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE01#202410010000.zip` | 6 | 2024-11-11 | 2026-02-09 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#RESIDUE_CON_FUNDS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#RESIDUE_CON_FUNDS#FILE01#202410.sql` | 6 | 2024-11-11 | 2026-02-10 |

### `MMSDM` · `RESIDUE_PRICE_FUNDS_BID`

_4 pattern rows, 27 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#RESIDUE_PRICE_FUNDS_BID\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE01#202409.fmt` | 7 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#RESIDUE_PRICE_FUNDS_BID\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE01#202409.ctl` | 7 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#RESIDUE_PRICE_FUNDS_BID\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE01#202409010000.zip` | 7 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#RESIDUE_PRICE_FUNDS_BID\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#RESIDUE_PRICE_FUNDS_BID#FILE01#202409.sql` | 6 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `RESIDUE_PUBLIC_DATA`

_4 pattern rows, 27 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#RESIDUE_PUBLIC_DATA\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE01#202409.fmt` | 7 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#RESIDUE_PUBLIC_DATA\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE01#202409.ctl` | 7 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#RESIDUE_PUBLIC_DATA\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE01#202409010000.zip` | 7 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#RESIDUE_PUBLIC_DATA\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#RESIDUE_PUBLIC_DATA#FILE01#202409.sql` | 6 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `RESIDUE_TRK`

_4 pattern rows, 27 files (snapshot), observed 2024-10-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#RESIDUE_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE01#202409.fmt` | 7 | 2024-10-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#RESIDUE_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE01#202409.ctl` | 7 | 2024-10-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#RESIDUE_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE01#202409010000.zip` | 7 | 2024-10-08 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#RESIDUE_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#RESIDUE_TRK#FILE01#202409.sql` | 6 | 2024-10-08 | 2026-04-08 |

### `MMSDM` · `ROOFTOP_PV_ACTUAL`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_ACTUAL\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_ACTUAL\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_ACTUAL\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_ACTUAL\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#ROOFTOP_PV_ACTUAL#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `ROOFTOP_PV_FORECAST`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_FORECAST\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_FORECAST\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_FORECAST\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#ROOFTOP_PV_FORECAST\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#ROOFTOP_PV_FORECAST#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SECDEPOSIT_INTEREST_RATE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SECDEPOSIT_INTEREST_RATE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SECDEPOSIT_INTEREST_RATE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SECDEPOSIT_INTEREST_RATE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SECDEPOSIT_INTEREST_RATE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SECDEPOSIT_INTEREST_RATE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETCFG_PARTICIPANT_MPF`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPF\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPF\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPF\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPF\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPF#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETCFG_PARTICIPANT_MPFTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPFTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPFTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPFTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETCFG_PARTICIPANT_MPFTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETCFG_PARTICIPANT_MPFTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETCFG_SAPS_SETT_PRICE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETCFG_SAPS_SETT_PRICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETCFG_SAPS_SETT_PRICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETCFG_SAPS_SETT_PRICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETCFG_SAPS_SETT_PRICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETCFG_SAPS_SETT_PRICE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETCFG_WDRRR_CALENDAR`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETCFG_WDRRR_CALENDAR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETCFG_WDRRR_CALENDAR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETCFG_WDRRR_CALENDAR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETCFG_WDRRR_CALENDAR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETCFG_WDRRR_CALENDAR#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETCFG_WDR_REIMBURSE_RATE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETCFG_WDR_REIMBURSE_RATE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETCFG_WDR_REIMBURSE_RATE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETCFG_WDR_REIMBURSE_RATE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETCFG_WDR_REIMBURSE_RATE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETCFG_WDR_REIMBURSE_RATE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETCPDATAREGION`

_4 pattern rows, 20 files (snapshot), observed 2024-09-12 → 2025-01-10 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETCPDATAREGION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE01#202408.fmt` | 5 | 2024-09-12 | 2025-01-10 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETCPDATAREGION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE01#202408.ctl` | 5 | 2024-09-12 | 2025-01-10 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETCPDATAREGION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE01#202408010000.zip` | 5 | 2024-09-12 | 2025-01-10 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETCPDATAREGION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETCPDATAREGION#FILE01#202408.sql` | 5 | 2024-09-13 | 2025-01-10 |

### `MMSDM` · `SETFCASREGIONRECOVERY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETFCASREGIONRECOVERY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETFCASREGIONRECOVERY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETFCASREGIONRECOVERY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETFCASREGIONRECOVERY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETFCASREGIONRECOVERY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETGENDATAREGION`

_4 pattern rows, 20 files (snapshot), observed 2024-09-12 → 2025-01-10 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETGENDATAREGION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE01#202408.fmt` | 5 | 2024-09-12 | 2025-01-10 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETGENDATAREGION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE01#202408.ctl` | 5 | 2024-09-12 | 2025-01-10 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETGENDATAREGION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE01#202408010000.zip` | 5 | 2024-09-12 | 2025-01-10 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETGENDATAREGION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETGENDATAREGION#FILE01#202408.sql` | 5 | 2024-09-13 | 2025-01-10 |

### `MMSDM` · `SETINTRAREGIONRESIDUES`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETINTRAREGIONRESIDUES\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETINTRAREGIONRESIDUES\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETINTRAREGIONRESIDUES\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETINTRAREGIONRESIDUES\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETINTRAREGIONRESIDUES#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETIRSURPLUS`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETIRSURPLUS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETIRSURPLUS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETIRSURPLUS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETIRSURPLUS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETIRSURPLUS#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETLOCALAREAENERGY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETLOCALAREAENERGY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETLOCALAREAENERGY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETLOCALAREAENERGY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETLOCALAREAENERGY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETLOCALAREAENERGY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SETLOCALAREATNI`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SETLOCALAREATNI\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SETLOCALAREATNI\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SETLOCALAREATNI\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SETLOCALAREATNI\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SETLOCALAREATNI#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SET_ANCILLARY_SUMMARY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SET_ANCILLARY_SUMMARY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SET_ANCILLARY_SUMMARY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SET_ANCILLARY_SUMMARY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SET_ANCILLARY_SUMMARY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SET_ANCILLARY_SUMMARY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SET_ENERGY_REGION_SUMMARY`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SET_ENERGY_REGION_SUMMARY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SET_ENERGY_REGION_SUMMARY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SET_ENERGY_REGION_SUMMARY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SET_ENERGY_REGION_SUMMARY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SET_ENERGY_REGION_SUMMARY#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SET_FCAS_CLAWBACK_REQ`

_4 pattern rows, 12 files (snapshot), observed 2026-02-09 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_REQ\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE01#202601.fmt` | 3 | 2026-02-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_REQ\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE01#202601.ctl` | 3 | 2026-02-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_REQ\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE01#202601010000.zip` | 3 | 2026-02-09 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_REQ\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_REQ#FILE01#202601.sql` | 3 | 2026-02-10 | 2026-04-08 |

### `MMSDM` · `SET_FCAS_CLAWBACK_RUN_TRK`

_4 pattern rows, 12 files (snapshot), observed 2026-02-09 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_RUN_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE01#202601.fmt` | 3 | 2026-02-10 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_RUN_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE01#202601.ctl` | 3 | 2026-02-10 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_RUN_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE01#202601010000.zip` | 3 | 2026-02-09 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SET_FCAS_CLAWBACK_RUN_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SET_FCAS_CLAWBACK_RUN_TRK#FILE01#202601.sql` | 3 | 2026-02-10 | 2026-04-08 |

### `MMSDM` · `SET_FCAS_REGULATION_TRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SET_FCAS_REGULATION_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SET_FCAS_REGULATION_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SET_FCAS_REGULATION_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SET_FCAS_REGULATION_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SET_FCAS_REGULATION_TRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SET_NMAS_RECOVERY_RBF`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SET_NMAS_RECOVERY_RBF\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SET_NMAS_RECOVERY_RBF\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SET_NMAS_RECOVERY_RBF\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SET_NMAS_RECOVERY_RBF\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SET_NMAS_RECOVERY_RBF#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SPDCONNECTIONPOINTCONSTRAINT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SPDCONNECTIONPOINTCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SPDCONNECTIONPOINTCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SPDCONNECTIONPOINTCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SPDCONNECTIONPOINTCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SPDCONNECTIONPOINTCONSTRAINT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SPDINTERCONNECTORCONSTRAINT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SPDINTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SPDINTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SPDINTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SPDINTERCONNECTORCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SPDINTERCONNECTORCONSTRAINT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SPDREGIONCONSTRAINT`

_4 pattern rows, 75 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SPDREGIONCONSTRAINT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE01#202408.fmt` | 19 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SPDREGIONCONSTRAINT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE01#202408.ctl` | 19 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SPDREGIONCONSTRAINT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE01#202408010000.zip` | 19 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SPDREGIONCONSTRAINT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SPDREGIONCONSTRAINT#FILE01#202408.sql` | 18 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SRA_FINANCIAL_RUNTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SRA_FINANCIAL_RUNTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SRA_FINANCIAL_RUNTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SRA_FINANCIAL_RUNTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SRA_FINANCIAL_RUNTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SRA_FINANCIAL_RUNTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SRA_PRUDENTIAL_RUN`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SRA_PRUDENTIAL_RUN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SRA_PRUDENTIAL_RUN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SRA_PRUDENTIAL_RUN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SRA_PRUDENTIAL_RUN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SRA_PRUDENTIAL_RUN#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `SSM_ENABLEMENT_COSTS`

_4 pattern rows, 20 files (snapshot), observed 2025-12-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_COSTS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE01#202511.fmt` | 5 | 2025-12-09 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_COSTS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE01#202511.ctl` | 5 | 2025-12-09 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_COSTS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE01#202511010000.zip` | 5 | 2025-12-08 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_COSTS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_COSTS#FILE01#202511.sql` | 5 | 2025-12-09 | 2026-04-08 |

### `MMSDM` · `SSM_ENABLEMENT_PERIOD`

_4 pattern rows, 20 files (snapshot), observed 2025-12-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_PERIOD\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE01#202511.fmt` | 5 | 2025-12-09 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_PERIOD\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE01#202511.ctl` | 5 | 2025-12-09 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_PERIOD\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE01#202511010000.zip` | 5 | 2025-12-08 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#SSM_ENABLEMENT_PERIOD\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#SSM_ENABLEMENT_PERIOD#FILE01#202511.sql` | 5 | 2025-12-09 | 2026-04-08 |

### `MMSDM` · `STADUALLOC`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STADUALLOC#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STADUALLOC\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STADUALLOC#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STADUALLOC#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STADUALLOC\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STADUALLOC#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STADUALLOC#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STADUALLOC\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STADUALLOC#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STADUALLOC#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STADUALLOC\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STADUALLOC#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STATION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STATION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STATION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STATION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STATION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STATION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STATION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STATION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STATION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STATION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STATION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STATION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STATION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STATIONOPERATINGSTATUS`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STATIONOPERATINGSTATUS\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STATIONOPERATINGSTATUS\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STATIONOPERATINGSTATUS\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STATIONOPERATINGSTATUS\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STATIONOPERATINGSTATUS#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STATIONOWNER`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STATIONOWNER\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STATIONOWNER\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STATIONOWNER\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STATIONOWNER\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STATIONOWNER#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STATIONOWNERTRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STATIONOWNERTRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STATIONOWNERTRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STATIONOWNERTRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STATIONOWNERTRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STATIONOWNERTRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STPASA_CASESOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STPASA_CASESOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STPASA_CASESOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STPASA_CASESOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STPASA_CASESOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STPASA_CASESOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STPASA_CONSTRAINTSOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STPASA_CONSTRAINTSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STPASA_CONSTRAINTSOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STPASA_DUIDAVAILABILITY`

_4 pattern rows, 284 files (snapshot), observed 2025-08-08 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE01#202507.fmt` | 72 | 2025-08-08 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE01#202507.ctl` | 72 | 2025-08-08 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE01#202507010000.zip` | 72 | 2025-08-08 | 2026-04-08 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STPASA_DUIDAVAILABILITY\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STPASA_DUIDAVAILABILITY#FILE01#202507.sql` | 68 | 2025-08-08 | 2026-04-08 |

### `MMSDM` · `STPASA_INTERCONNECTORSOLN`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STPASA_INTERCONNECTORSOLN\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STPASA_INTERCONNECTORSOLN#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `STPASA_REGIONSOLUTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#STPASA_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#STPASA_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#STPASA_REGIONSOLUTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#STPASA_REGIONSOLUTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#STPASA_REGIONSOLUTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `TRADINGINTERCONNECT`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#TRADINGINTERCONNECT\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#TRADINGINTERCONNECT\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#TRADINGINTERCONNECT\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#TRADINGINTERCONNECT\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#TRADINGINTERCONNECT#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `TRADINGPRICE`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#TRADINGPRICE\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#TRADINGPRICE\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#TRADINGPRICE\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#TRADINGPRICE\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#TRADINGPRICE#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `TRANSMISSIONLOSSFACTOR`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#TRANSMISSIONLOSSFACTOR\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#TRANSMISSIONLOSSFACTOR\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#TRANSMISSIONLOSSFACTOR\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#TRANSMISSIONLOSSFACTOR\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#TRANSMISSIONLOSSFACTOR#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `UNKNOWN`

_9 pattern rows, 652 files (snapshot), observed 1996-10-08 → 2026-04-13 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/` | `MMSDM_{year}_{d2}.zip` | `MMSDM_\d{4}_\d{2}\.zip` | `MMSDM_2009_07.zip` | 201 | 2017-02-06 | 2026-04-13 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `AUTORUN.INF` | `AUTORUN\.INF` | `AUTORUN.INF` | 135 | 2017-01-12 | 2026-04-13 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `Back.gif` | `Back\.gif` | `Back.gif` | 50 | 1999-05-23 | 2019-03-14 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 38 | 2017-05-11 | 2019-03-14 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `background{d1}.gif` | `background\d{1}\.gif` | `background1.gif` | 13 | 2018-03-19 | 2019-03-14 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `disclaimer.htm` | `disclaimer\.htm` | `disclaimer.htm` | 38 | 2017-02-07 | 2019-03-14 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `file.gif` | `file\.gif` | `file.gif` | 50 | 1999-05-23 | 2019-03-14 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `nemlogo{d1}.gif` | `nemlogo\d{1}\.gif` | `nemlogo1.gif` | 100 | 2009-08-17 | 2019-03-14 |
| `OTHER` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/` | `shelexec.exe` | `shelexec\.exe` | `shelexec.exe` | 27 | 1996-10-08 | 2019-03-14 |

### `MMSDM` · `UNPARSED`

_537 pattern rows, 53084 files (snapshot), observed 1999-05-23 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_DATA/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 123 | 2017-02-06 | 2025-10-17 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_{yearmonth}.fmt` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_\d{6}\.fmt` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_APEVENTREGION_{yearmonth}.fmt` | `PUBLIC_DVD_APEVENTREGION_\d{6}\.fmt` | `PUBLIC_DVD_APEVENTREGION_201510.fmt` | 13 | 2019-09-06 | 2024-06-12 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_APEVENT_{yearmonth}.fmt` | `PUBLIC_DVD_APEVENT_\d{6}\.fmt` | `PUBLIC_DVD_APEVENT_201510.fmt` | 13 | 2019-09-06 | 2024-06-12 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_AUCTION_CALENDAR_{yearmonth}.fmt` | `PUBLIC_DVD_AUCTION_CALENDAR_\d{6}\.fmt` | `PUBLIC_DVD_AUCTION_CALENDAR_201501.fmt` | 53 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_{yearmonth}.fmt` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_\d{6}\.fmt` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_201501.fmt` | 78 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_AUCTION_TRANCHE_{yearmonth}.fmt` | `PUBLIC_DVD_AUCTION_TRANCHE_\d{6}\.fmt` | `PUBLIC_DVD_AUCTION_TRANCHE_201501.fmt` | 41 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_AUCTION_{yearmonth}.fmt` | `PUBLIC_DVD_AUCTION_\d{6}\.fmt` | `PUBLIC_DVD_AUCTION_201503.fmt` | 79 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDDAYOFFER_D_{yearmonth}.fmt` | `PUBLIC_DVD_BIDDAYOFFER_D_\d{6}\.fmt` | `PUBLIC_DVD_BIDDAYOFFER_D_201501.fmt` | 74 | 2019-09-05 | 2021-03-22 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDDAYOFFER_{yearmonth}.fmt` | `PUBLIC_DVD_BIDDAYOFFER_\d{6}\.fmt` | `PUBLIC_DVD_BIDDAYOFFER_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_{yearmonth}.fmt` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_\d{6}\.fmt` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDDUIDDETAILS_{yearmonth}.fmt` | `PUBLIC_DVD_BIDDUIDDETAILS_\d{6}\.fmt` | `PUBLIC_DVD_BIDDUIDDETAILS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDPEROFFER{d1}_{yearmonth}.fmt` | `PUBLIC_DVD_BIDPEROFFER\d{1}_\d{6}\.fmt` | `PUBLIC_DVD_BIDPEROFFER1_202206.fmt` | 52 | 2022-07-20 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDPEROFFER_D_{yearmonth}.fmt` | `PUBLIC_DVD_BIDPEROFFER_D_\d{6}\.fmt` | `PUBLIC_DVD_BIDPEROFFER_D_201501.fmt` | 74 | 2019-09-05 | 2021-03-22 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDPEROFFER_{yearmonth}.fmt` | `PUBLIC_DVD_BIDPEROFFER_\d{6}\.fmt` | `PUBLIC_DVD_BIDPEROFFER_201501.fmt` | 87 | 2019-09-05 | 2022-06-09 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDTYPESTRK_{yearmonth}.fmt` | `PUBLIC_DVD_BIDTYPESTRK_\d{6}\.fmt` | `PUBLIC_DVD_BIDTYPESTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BIDTYPES_{yearmonth}.fmt` | `PUBLIC_DVD_BIDTYPES_\d{6}\.fmt` | `PUBLIC_DVD_BIDTYPES_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLINGCALENDAR_{yearmonth}.fmt` | `PUBLIC_DVD_BILLINGCALENDAR_\d{6}\.fmt` | `PUBLIC_DVD_BILLINGCALENDAR_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLINGDAYTRK_{yearmonth}.fmt` | `PUBLIC_DVD_BILLINGDAYTRK_\d{6}\.fmt` | `PUBLIC_DVD_BILLINGDAYTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_{yearmonth}.fmt` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_\d{6}\.fmt` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLINGREGIONFIGURES_{yearmonth}.fmt` | `PUBLIC_DVD_BILLINGREGIONFIGURES_\d{6}\.fmt` | `PUBLIC_DVD_BILLINGREGIONFIGURES_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_{yearmonth}.fmt` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_\d{6}\.fmt` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLINGRUNTRK_{yearmonth}.fmt` | `PUBLIC_DVD_BILLINGRUNTRK_\d{6}\.fmt` | `PUBLIC_DVD_BILLINGRUNTRK_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLING_CO{d1}E_PUBLICATION_TRK_{yearmonth}.fmt` | `PUBLIC_DVD_BILLING_CO\d{1}E_PUBLICATION_TRK_\d{6}\.fmt` | `PUBLIC_DVD_BILLING_CO2E_PUBLICATION_TRK_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLING_CO{d1}E_PUBLICATION_{yearmonth}.fmt` | `PUBLIC_DVD_BILLING_CO\d{1}E_PUBLICATION_\d{6}\.fmt` | `PUBLIC_DVD_BILLING_CO2E_PUBLICATION_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_BILLSMELTERRATE_{yearmonth}.fmt` | `PUBLIC_DVD_BILLSMELTERRATE_\d{6}\.fmt` | `PUBLIC_DVD_BILLSMELTERRATE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DAYTRACK_{yearmonth}.fmt` | `PUBLIC_DVD_DAYTRACK_\d{6}\.fmt` | `PUBLIC_DVD_DAYTRACK_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHABLEUNIT_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHABLEUNIT_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHABLEUNIT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHCASESOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHCASESOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHCASESOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHCONSTRAINT_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHCONSTRAINT_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHCONSTRAINT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHLOAD_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHLOAD_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHLOAD_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHOFFERTRK_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHOFFERTRK_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHOFFERTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHPRICE_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHPRICE_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHPRICE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCHREGIONSUM_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCHREGIONSUM_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCHREGIONSUM_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_201502.fmt` | 25 | 2019-09-06 | 2024-03-09 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_{yearmonth}.fmt` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_\d{6}\.fmt` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DUALLOC_{yearmonth}.fmt` | `PUBLIC_DVD_DUALLOC_\d{6}\.fmt` | `PUBLIC_DVD_DUALLOC_202010.fmt` | 46 | 2020-11-12 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DUDETAILSUMMARY_{yearmonth}.fmt` | `PUBLIC_DVD_DUDETAILSUMMARY_\d{6}\.fmt` | `PUBLIC_DVD_DUDETAILSUMMARY_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_DUDETAIL_{yearmonth}.fmt` | `PUBLIC_DVD_DUDETAIL_\d{6}\.fmt` | `PUBLIC_DVD_DUDETAIL_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_EMSMASTER_{yearmonth}.fmt` | `PUBLIC_DVD_EMSMASTER_\d{6}\.fmt` | `PUBLIC_DVD_EMSMASTER_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GDINSTRUCT_{yearmonth}.fmt` | `PUBLIC_DVD_GDINSTRUCT_\d{6}\.fmt` | `PUBLIC_DVD_GDINSTRUCT_201501.fmt` | 24 | 2019-09-09 | 2019-09-16 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENCONDATA_{yearmonth}.fmt` | `PUBLIC_DVD_GENCONDATA_\d{6}\.fmt` | `PUBLIC_DVD_GENCONDATA_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENCONSETINVOKE_{yearmonth}.fmt` | `PUBLIC_DVD_GENCONSETINVOKE_\d{6}\.fmt` | `PUBLIC_DVD_GENCONSETINVOKE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENCONSETTRK_{yearmonth}.fmt` | `PUBLIC_DVD_GENCONSETTRK_\d{6}\.fmt` | `PUBLIC_DVD_GENCONSETTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENCONSET_{yearmonth}.fmt` | `PUBLIC_DVD_GENCONSET_\d{6}\.fmt` | `PUBLIC_DVD_GENCONSET_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_{yearmonth}.fmt` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_\d{6}\.fmt` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENERICEQUATIONDESC_{yearmonth}.fmt` | `PUBLIC_DVD_GENERICEQUATIONDESC_\d{6}\.fmt` | `PUBLIC_DVD_GENERICEQUATIONDESC_201501.fmt` | 105 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENERICEQUATIONRHS_{yearmonth}.fmt` | `PUBLIC_DVD_GENERICEQUATIONRHS_\d{6}\.fmt` | `PUBLIC_DVD_GENERICEQUATIONRHS_201501.fmt` | 109 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GENUNITS_{yearmonth}.fmt` | `PUBLIC_DVD_GENUNITS_\d{6}\.fmt` | `PUBLIC_DVD_GENUNITS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GST_BAS_CLASS_{yearmonth}.fmt` | `PUBLIC_DVD_GST_BAS_CLASS_\d{6}\.fmt` | `PUBLIC_DVD_GST_BAS_CLASS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GST_RATE_{yearmonth}.fmt` | `PUBLIC_DVD_GST_RATE_\d{6}\.fmt` | `PUBLIC_DVD_GST_RATE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_{yearmonth}.fmt` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_\d{6}\.fmt` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_{yearmonth}.fmt` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_\d{6}\.fmt` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_{yearmonth}.fmt` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_\d{6}\.fmt` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_INSTRUCTIONTYPE_{yearmonth}.fmt` | `PUBLIC_DVD_INSTRUCTIONTYPE_\d{6}\.fmt` | `PUBLIC_DVD_INSTRUCTIONTYPE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_{yearmonth}.fmt` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_\d{6}\.fmt` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_INTERCONNECTOR_{yearmonth}.fmt` | `PUBLIC_DVD_INTERCONNECTOR_\d{6}\.fmt` | `PUBLIC_DVD_INTERCONNECTOR_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_INTERCONNMWFLOW_{yearmonth}.fmt` | `PUBLIC_DVD_INTERCONNMWFLOW_\d{6}\.fmt` | `PUBLIC_DVD_INTERCONNMWFLOW_201501.fmt` | 77 | 2019-09-05 | 2021-07-03 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_IRFMAMOUNT_{yearmonth}.fmt` | `PUBLIC_DVD_IRFMAMOUNT_\d{6}\.fmt` | `PUBLIC_DVD_IRFMAMOUNT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_IRFMEVENTS_{yearmonth}.fmt` | `PUBLIC_DVD_IRFMEVENTS_\d{6}\.fmt` | `PUBLIC_DVD_IRFMEVENTS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_LOSSFACTORMODEL_{yearmonth}.fmt` | `PUBLIC_DVD_LOSSFACTORMODEL_\d{6}\.fmt` | `PUBLIC_DVD_LOSSFACTORMODEL_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_LOSSMODEL_{yearmonth}.fmt` | `PUBLIC_DVD_LOSSMODEL_\d{6}\.fmt` | `PUBLIC_DVD_LOSSMODEL_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKETFEEDATA_{yearmonth}.fmt` | `PUBLIC_DVD_MARKETFEEDATA_\d{6}\.fmt` | `PUBLIC_DVD_MARKETFEEDATA_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKETFEETRK_{yearmonth}.fmt` | `PUBLIC_DVD_MARKETFEETRK_\d{6}\.fmt` | `PUBLIC_DVD_MARKETFEETRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKETFEE_{yearmonth}.fmt` | `PUBLIC_DVD_MARKETFEE_\d{6}\.fmt` | `PUBLIC_DVD_MARKETFEE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKETNOTICEDATA_{yearmonth}.fmt` | `PUBLIC_DVD_MARKETNOTICEDATA_\d{6}\.fmt` | `PUBLIC_DVD_MARKETNOTICEDATA_201501.fmt` | 101 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKETNOTICETYPE_{yearmonth}.fmt` | `PUBLIC_DVD_MARKETNOTICETYPE_\d{6}\.fmt` | `PUBLIC_DVD_MARKETNOTICETYPE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKETSUSPENSION_{yearmonth}.fmt` | `PUBLIC_DVD_MARKETSUSPENSION_\d{6}\.fmt` | `PUBLIC_DVD_MARKETSUSPENSION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKETSUSREGION_{yearmonth}.fmt` | `PUBLIC_DVD_MARKETSUSREGION_\d{6}\.fmt` | `PUBLIC_DVD_MARKETSUSREGION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_{yearmonth}.fmt` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_\d{6}\.fmt` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MCC_CASESOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_MCC_CASESOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_MCC_CASESOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MNSP_DAYOFFER_{yearmonth}.fmt` | `PUBLIC_DVD_MNSP_DAYOFFER_\d{6}\.fmt` | `PUBLIC_DVD_MNSP_DAYOFFER_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_{yearmonth}.fmt` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_\d{6}\.fmt` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MNSP_OFFERTRK_{yearmonth}.fmt` | `PUBLIC_DVD_MNSP_OFFERTRK_\d{6}\.fmt` | `PUBLIC_DVD_MNSP_OFFERTRK_201501.fmt` | 73 | 2019-09-05 | 2021-03-22 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MNSP_PARTICIPANT_{yearmonth}.fmt` | `PUBLIC_DVD_MNSP_PARTICIPANT_\d{6}\.fmt` | `PUBLIC_DVD_MNSP_PARTICIPANT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MNSP_PEROFFER_{yearmonth}.fmt` | `PUBLIC_DVD_MNSP_PEROFFER_\d{6}\.fmt` | `PUBLIC_DVD_MNSP_PEROFFER_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_CASERESULT_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_CASERESULT_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_CASERESULT_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_CASESOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_CASESOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_CASESOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_201501.fmt` | 41 | 2019-09-09 | 2019-09-16 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_201501.fmt` | 41 | 2019-09-09 | 2019-09-16 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_LOLPRESULT_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_LOLPRESULT_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_LOLPRESULT_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_REGIONITERATION_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_REGIONITERATION_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_REGIONITERATION_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_REGIONRESULT_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_REGIONRESULT_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_REGIONRESULT_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_201501.fmt` | 41 | 2019-09-09 | 2019-09-16 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_201501.fmt` | 41 | 2019-09-09 | 2019-09-16 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_{yearmonth}.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_\d{6}\.fmt` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_OVERRIDERRP_{yearmonth}.fmt` | `PUBLIC_DVD_OVERRIDERRP_\d{6}\.fmt` | `PUBLIC_DVD_OVERRIDERRP_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_{yearmonth}.fmt` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_\d{6}\.fmt` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PARTICIPANTCATEGORY_{yearmonth}.fmt` | `PUBLIC_DVD_PARTICIPANTCATEGORY_\d{6}\.fmt` | `PUBLIC_DVD_PARTICIPANTCATEGORY_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PARTICIPANTCLASS_{yearmonth}.fmt` | `PUBLIC_DVD_PARTICIPANTCLASS_\d{6}\.fmt` | `PUBLIC_DVD_PARTICIPANTCLASS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PARTICIPANT_{yearmonth}.fmt` | `PUBLIC_DVD_PARTICIPANT_\d{6}\.fmt` | `PUBLIC_DVD_PARTICIPANT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PDPASA_CASESOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_PDPASA_CASESOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_PDPASA_CASESOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_202104.fmt` | 40 | 2021-05-12 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_{yearmonth}.fmt` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_\d{6}\.fmt` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_202104.fmt` | 40 | 2021-05-12 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PERDEMAND_{yearmonth}.fmt` | `PUBLIC_DVD_PERDEMAND_\d{6}\.fmt` | `PUBLIC_DVD_PERDEMAND_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT{d1}_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT\d{1}_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT2_201803.fmt` | 1 | 2019-09-09 | 2019-09-09 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHLOAD_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHLOAD_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHLOAD_D_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHPRICE_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHPRICE_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHPRICE_D_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_202210.fmt` | 22 | 2022-11-09 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_{yearmonth}.fmt` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_\d{6}\.fmt` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_PRUDENTIALRUNTRK_{yearmonth}.fmt` | `PUBLIC_DVD_PRUDENTIALRUNTRK_\d{6}\.fmt` | `PUBLIC_DVD_PRUDENTIALRUNTRK_201501.fmt` | 77 | 2019-09-05 | 2021-07-03 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_P{d1}MINSCENARIODEMANDTRK_{yearmonth}.fmt` | `PUBLIC_DVD_P\d{1}MINSCENARIODEMANDTRK_\d{6}\.fmt` | `PUBLIC_DVD_P5MINSCENARIODEMANDTRK_202106.fmt` | 38 | 2021-07-13 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_P{d1}MINSCENARIODEMAND_{yearmonth}.fmt` | `PUBLIC_DVD_P\d{1}MINSCENARIODEMAND_\d{6}\.fmt` | `PUBLIC_DVD_P5MINSCENARIODEMAND_202106.fmt` | 38 | 2021-07-13 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_P{d1}MIN_CASESOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_P\d{1}MIN_CASESOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_P5MIN_CASESOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_P{d11}MIN_CONSTRAINTSOLUTION{d12}_{yearmonth}.fmt` | `PUBLIC_DVD_P\d{1}MIN_CONSTRAINTSOLUTION\d{1}_\d{6}\.fmt` | `PUBLIC_DVD_P5MIN_CONSTRAINTSOLUTION1_201501.fmt` | 459 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_P{d1}MIN_INTERCONNECTORSOLN_{yearmonth}.fmt` | `PUBLIC_DVD_P\d{1}MIN_INTERCONNECTORSOLN_\d{6}\.fmt` | `PUBLIC_DVD_P5MIN_INTERCONNECTORSOLN_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_P{d1}MIN_REGIONSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_P\d{1}MIN_REGIONSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_P5MIN_REGIONSOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_P{d1}MIN_UNITSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_P\d{1}MIN_UNITSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_P5MIN_UNITSOLUTION_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_REGIONAPCINTERVALS_{yearmonth}.fmt` | `PUBLIC_DVD_REGIONAPCINTERVALS_\d{6}\.fmt` | `PUBLIC_DVD_REGIONAPCINTERVALS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_REGIONAPC_{yearmonth}.fmt` | `PUBLIC_DVD_REGIONAPC_\d{6}\.fmt` | `PUBLIC_DVD_REGIONAPC_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_REGIONSTANDINGDATA_{yearmonth}.fmt` | `PUBLIC_DVD_REGIONSTANDINGDATA_\d{6}\.fmt` | `PUBLIC_DVD_REGIONSTANDINGDATA_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_REGION_{yearmonth}.fmt` | `PUBLIC_DVD_REGION_\d{6}\.fmt` | `PUBLIC_DVD_REGION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_RESDEMANDTRK_{yearmonth}.fmt` | `PUBLIC_DVD_RESDEMANDTRK_\d{6}\.fmt` | `PUBLIC_DVD_RESDEMANDTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_RESERVE_{yearmonth}.fmt` | `PUBLIC_DVD_RESERVE_\d{6}\.fmt` | `PUBLIC_DVD_RESERVE_201501.fmt` | 27 | 2019-09-09 | 2019-09-16 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_RESIDUE_CONTRACTS_{yearmonth}.fmt` | `PUBLIC_DVD_RESIDUE_CONTRACTS_\d{6}\.fmt` | `PUBLIC_DVD_RESIDUE_CONTRACTS_201503.fmt` | 79 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_{yearmonth}.fmt` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_\d{6}\.fmt` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_201505.fmt` | 39 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_{yearmonth}.fmt` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_\d{6}\.fmt` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_201503.fmt` | 42 | 2019-09-06 | 2024-07-23 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_{yearmonth}.fmt` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_\d{6}\.fmt` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_201503.fmt` | 46 | 2019-09-06 | 2024-07-23 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_RESIDUE_TRK_{yearmonth}.fmt` | `PUBLIC_DVD_RESIDUE_TRK_\d{6}\.fmt` | `PUBLIC_DVD_RESIDUE_TRK_201503.fmt` | 47 | 2019-09-06 | 2024-07-23 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_{yearmonth}.fmt` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_\d{6}\.fmt` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_{yearmonth}.fmt` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_\d{6}\.fmt` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_201910.fmt` | 58 | 2019-11-18 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_{yearmonth}.fmt` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_\d{6}\.fmt` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_{yearmonth}.fmt` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_\d{6}\.fmt` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SETCPDATAREGION_{yearmonth}.fmt` | `PUBLIC_DVD_SETCPDATAREGION_\d{6}\.fmt` | `PUBLIC_DVD_SETCPDATAREGION_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_{yearmonth}.fmt` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_\d{6}\.fmt` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SETGENDATAREGION_{yearmonth}.fmt` | `PUBLIC_DVD_SETGENDATAREGION_\d{6}\.fmt` | `PUBLIC_DVD_SETGENDATAREGION_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_{yearmonth}.fmt` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_\d{6}\.fmt` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SETIRSURPLUS_{yearmonth}.fmt` | `PUBLIC_DVD_SETIRSURPLUS_\d{6}\.fmt` | `PUBLIC_DVD_SETIRSURPLUS_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_{yearmonth}.fmt` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_\d{6}\.fmt` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_{yearmonth}.fmt` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_\d{6}\.fmt` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_201501.fmt` | 114 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_{yearmonth}.fmt` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_\d{6}\.fmt` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_{yearmonth}.fmt` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_\d{6}\.fmt` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_{yearmonth}.fmt` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_\d{6}\.fmt` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_201501.fmt` | 79 | 2019-09-06 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STADUALLOC_{yearmonth}.fmt` | `PUBLIC_DVD_STADUALLOC_\d{6}\.fmt` | `PUBLIC_DVD_STADUALLOC_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_{yearmonth}.fmt` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_\d{6}\.fmt` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STATIONOWNERTRK_{yearmonth}.fmt` | `PUBLIC_DVD_STATIONOWNERTRK_\d{6}\.fmt` | `PUBLIC_DVD_STATIONOWNERTRK_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STATIONOWNER_{yearmonth}.fmt` | `PUBLIC_DVD_STATIONOWNER_\d{6}\.fmt` | `PUBLIC_DVD_STATIONOWNER_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STATION_{yearmonth}.fmt` | `PUBLIC_DVD_STATION_\d{6}\.fmt` | `PUBLIC_DVD_STATION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STPASA_CASESOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_STPASA_CASESOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_STPASA_CASESOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_{yearmonth}.fmt` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_\d{6}\.fmt` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_{yearmonth}.fmt` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_\d{6}\.fmt` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_TRADINGINTERCONNECT_{yearmonth}.fmt` | `PUBLIC_DVD_TRADINGINTERCONNECT_\d{6}\.fmt` | `PUBLIC_DVD_TRADINGINTERCONNECT_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_TRADINGLOAD_{yearmonth}.fmt` | `PUBLIC_DVD_TRADINGLOAD_\d{6}\.fmt` | `PUBLIC_DVD_TRADINGLOAD_201501.fmt` | 81 | 2019-09-05 | 2021-10-11 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_TRADINGPRICE_{yearmonth}.fmt` | `PUBLIC_DVD_TRADINGPRICE_\d{6}\.fmt` | `PUBLIC_DVD_TRADINGPRICE_201501.fmt` | 115 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_TRADINGREGIONSUM_{yearmonth}.fmt` | `PUBLIC_DVD_TRADINGREGIONSUM_\d{6}\.fmt` | `PUBLIC_DVD_TRADINGREGIONSUM_201501.fmt` | 81 | 2019-09-05 | 2021-10-11 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_{yearmonth}.fmt` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_\d{6}\.fmt` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_201501.fmt` | 110 | 2019-09-05 | 2024-08-15 |
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 81 | 2017-02-15 | 2025-10-17 |
| `Back.gif` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/` | `Back.gif` | `Back\.gif` | `Back.gif` | 50 | 1999-05-23 | 2019-03-14 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_{yearmonth}.ctl` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_\d{6}\.ctl` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_APEVENTREGION_{yearmonth}.ctl` | `PUBLIC_DVD_APEVENTREGION_\d{6}\.ctl` | `PUBLIC_DVD_APEVENTREGION_201510.ctl` | 13 | 2017-01-15 | 2024-06-12 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_APEVENT_{yearmonth}.ctl` | `PUBLIC_DVD_APEVENT_\d{6}\.ctl` | `PUBLIC_DVD_APEVENT_201510.ctl` | 13 | 2017-01-15 | 2024-06-12 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_AUCTION_CALENDAR_{yearmonth}.ctl` | `PUBLIC_DVD_AUCTION_CALENDAR_\d{6}\.ctl` | `PUBLIC_DVD_AUCTION_CALENDAR_201501.ctl` | 53 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_{yearmonth}.ctl` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_\d{6}\.ctl` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_201501.ctl` | 78 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_AUCTION_TRANCHE_{yearmonth}.ctl` | `PUBLIC_DVD_AUCTION_TRANCHE_\d{6}\.ctl` | `PUBLIC_DVD_AUCTION_TRANCHE_201501.ctl` | 41 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_AUCTION_{yearmonth}.ctl` | `PUBLIC_DVD_AUCTION_\d{6}\.ctl` | `PUBLIC_DVD_AUCTION_201503.ctl` | 79 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDDAYOFFER_D_{yearmonth}.ctl` | `PUBLIC_DVD_BIDDAYOFFER_D_\d{6}\.ctl` | `PUBLIC_DVD_BIDDAYOFFER_D_201501.ctl` | 74 | 2017-01-14 | 2021-03-22 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDDAYOFFER_{yearmonth}.ctl` | `PUBLIC_DVD_BIDDAYOFFER_\d{6}\.ctl` | `PUBLIC_DVD_BIDDAYOFFER_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_{yearmonth}.ctl` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_\d{6}\.ctl` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDDUIDDETAILS_{yearmonth}.ctl` | `PUBLIC_DVD_BIDDUIDDETAILS_\d{6}\.ctl` | `PUBLIC_DVD_BIDDUIDDETAILS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDPEROFFER{d1}_{yearmonth}.ctl` | `PUBLIC_DVD_BIDPEROFFER\d{1}_\d{6}\.ctl` | `PUBLIC_DVD_BIDPEROFFER1_202206.ctl` | 52 | 2022-07-20 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDPEROFFER_D_{yearmonth}.ctl` | `PUBLIC_DVD_BIDPEROFFER_D_\d{6}\.ctl` | `PUBLIC_DVD_BIDPEROFFER_D_201501.ctl` | 74 | 2017-01-14 | 2021-03-22 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDPEROFFER_{yearmonth}.ctl` | `PUBLIC_DVD_BIDPEROFFER_\d{6}\.ctl` | `PUBLIC_DVD_BIDPEROFFER_201501.ctl` | 87 | 2017-01-14 | 2022-06-09 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDTYPESTRK_{yearmonth}.ctl` | `PUBLIC_DVD_BIDTYPESTRK_\d{6}\.ctl` | `PUBLIC_DVD_BIDTYPESTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BIDTYPES_{yearmonth}.ctl` | `PUBLIC_DVD_BIDTYPES_\d{6}\.ctl` | `PUBLIC_DVD_BIDTYPES_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLINGCALENDAR_{yearmonth}.ctl` | `PUBLIC_DVD_BILLINGCALENDAR_\d{6}\.ctl` | `PUBLIC_DVD_BILLINGCALENDAR_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLINGDAYTRK_{yearmonth}.ctl` | `PUBLIC_DVD_BILLINGDAYTRK_\d{6}\.ctl` | `PUBLIC_DVD_BILLINGDAYTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_{yearmonth}.ctl` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_\d{6}\.ctl` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLINGREGIONFIGURES_{yearmonth}.ctl` | `PUBLIC_DVD_BILLINGREGIONFIGURES_\d{6}\.ctl` | `PUBLIC_DVD_BILLINGREGIONFIGURES_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_{yearmonth}.ctl` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_\d{6}\.ctl` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLINGRUNTRK_{yearmonth}.ctl` | `PUBLIC_DVD_BILLINGRUNTRK_\d{6}\.ctl` | `PUBLIC_DVD_BILLINGRUNTRK_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLING_CO{d1}E_PUBLICATION_TRK_{yearmonth}.ctl` | `PUBLIC_DVD_BILLING_CO\d{1}E_PUBLICATION_TRK_\d{6}\.ctl` | `PUBLIC_DVD_BILLING_CO2E_PUBLICATION_TRK_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLING_CO{d1}E_PUBLICATION_{yearmonth}.ctl` | `PUBLIC_DVD_BILLING_CO\d{1}E_PUBLICATION_\d{6}\.ctl` | `PUBLIC_DVD_BILLING_CO2E_PUBLICATION_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_BILLSMELTERRATE_{yearmonth}.ctl` | `PUBLIC_DVD_BILLSMELTERRATE_\d{6}\.ctl` | `PUBLIC_DVD_BILLSMELTERRATE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DAYTRACK_{yearmonth}.ctl` | `PUBLIC_DVD_DAYTRACK_\d{6}\.ctl` | `PUBLIC_DVD_DAYTRACK_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHABLEUNIT_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHABLEUNIT_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHABLEUNIT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHCASESOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHCASESOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHCASESOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHCONSTRAINT_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHCONSTRAINT_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHCONSTRAINT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHLOAD_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHLOAD_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHLOAD_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHOFFERTRK_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHOFFERTRK_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHOFFERTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHPRICE_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHPRICE_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHPRICE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCHREGIONSUM_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCHREGIONSUM_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCHREGIONSUM_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_201502.ctl` | 25 | 2017-01-15 | 2024-03-09 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_{yearmonth}.ctl` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_\d{6}\.ctl` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DUALLOC_{yearmonth}.ctl` | `PUBLIC_DVD_DUALLOC_\d{6}\.ctl` | `PUBLIC_DVD_DUALLOC_202010.ctl` | 46 | 2020-11-12 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DUDETAILSUMMARY_{yearmonth}.ctl` | `PUBLIC_DVD_DUDETAILSUMMARY_\d{6}\.ctl` | `PUBLIC_DVD_DUDETAILSUMMARY_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_DUDETAIL_{yearmonth}.ctl` | `PUBLIC_DVD_DUDETAIL_\d{6}\.ctl` | `PUBLIC_DVD_DUDETAIL_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_EMSMASTER_{yearmonth}.ctl` | `PUBLIC_DVD_EMSMASTER_\d{6}\.ctl` | `PUBLIC_DVD_EMSMASTER_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GDINSTRUCT_{yearmonth}.ctl` | `PUBLIC_DVD_GDINSTRUCT_\d{6}\.ctl` | `PUBLIC_DVD_GDINSTRUCT_201501.ctl` | 24 | 2017-01-14 | 2018-07-09 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENCONDATA_{yearmonth}.ctl` | `PUBLIC_DVD_GENCONDATA_\d{6}\.ctl` | `PUBLIC_DVD_GENCONDATA_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENCONSETINVOKE_{yearmonth}.ctl` | `PUBLIC_DVD_GENCONSETINVOKE_\d{6}\.ctl` | `PUBLIC_DVD_GENCONSETINVOKE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENCONSETTRK_{yearmonth}.ctl` | `PUBLIC_DVD_GENCONSETTRK_\d{6}\.ctl` | `PUBLIC_DVD_GENCONSETTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENCONSET_{yearmonth}.ctl` | `PUBLIC_DVD_GENCONSET_\d{6}\.ctl` | `PUBLIC_DVD_GENCONSET_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_{yearmonth}.ctl` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_\d{6}\.ctl` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENERICEQUATIONDESC_{yearmonth}.ctl` | `PUBLIC_DVD_GENERICEQUATIONDESC_\d{6}\.ctl` | `PUBLIC_DVD_GENERICEQUATIONDESC_201501.ctl` | 105 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENERICEQUATIONRHS_{yearmonth}.ctl` | `PUBLIC_DVD_GENERICEQUATIONRHS_\d{6}\.ctl` | `PUBLIC_DVD_GENERICEQUATIONRHS_201501.ctl` | 109 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GENUNITS_{yearmonth}.ctl` | `PUBLIC_DVD_GENUNITS_\d{6}\.ctl` | `PUBLIC_DVD_GENUNITS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GST_BAS_CLASS_{yearmonth}.ctl` | `PUBLIC_DVD_GST_BAS_CLASS_\d{6}\.ctl` | `PUBLIC_DVD_GST_BAS_CLASS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GST_RATE_{yearmonth}.ctl` | `PUBLIC_DVD_GST_RATE_\d{6}\.ctl` | `PUBLIC_DVD_GST_RATE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_{yearmonth}.ctl` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_\d{6}\.ctl` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_{yearmonth}.ctl` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_\d{6}\.ctl` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_{yearmonth}.ctl` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_\d{6}\.ctl` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_INSTRUCTIONTYPE_{yearmonth}.ctl` | `PUBLIC_DVD_INSTRUCTIONTYPE_\d{6}\.ctl` | `PUBLIC_DVD_INSTRUCTIONTYPE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_{yearmonth}.ctl` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_\d{6}\.ctl` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_INTERCONNECTOR_{yearmonth}.ctl` | `PUBLIC_DVD_INTERCONNECTOR_\d{6}\.ctl` | `PUBLIC_DVD_INTERCONNECTOR_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_INTERCONNMWFLOW_{yearmonth}.ctl` | `PUBLIC_DVD_INTERCONNMWFLOW_\d{6}\.ctl` | `PUBLIC_DVD_INTERCONNMWFLOW_201501.ctl` | 77 | 2017-01-14 | 2021-07-03 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_IRFMAMOUNT_{yearmonth}.ctl` | `PUBLIC_DVD_IRFMAMOUNT_\d{6}\.ctl` | `PUBLIC_DVD_IRFMAMOUNT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_IRFMEVENTS_{yearmonth}.ctl` | `PUBLIC_DVD_IRFMEVENTS_\d{6}\.ctl` | `PUBLIC_DVD_IRFMEVENTS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_LOSSFACTORMODEL_{yearmonth}.ctl` | `PUBLIC_DVD_LOSSFACTORMODEL_\d{6}\.ctl` | `PUBLIC_DVD_LOSSFACTORMODEL_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_LOSSMODEL_{yearmonth}.ctl` | `PUBLIC_DVD_LOSSMODEL_\d{6}\.ctl` | `PUBLIC_DVD_LOSSMODEL_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETFEEDATA_{yearmonth}.ctl` | `PUBLIC_DVD_MARKETFEEDATA_\d{6}\.ctl` | `PUBLIC_DVD_MARKETFEEDATA_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETFEETRK_{yearmonth}.ctl` | `PUBLIC_DVD_MARKETFEETRK_\d{6}\.ctl` | `PUBLIC_DVD_MARKETFEETRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETFEE_{yearmonth}.ctl` | `PUBLIC_DVD_MARKETFEE_\d{6}\.ctl` | `PUBLIC_DVD_MARKETFEE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETNOTICEDATA_{yearmonth}.ctl` | `PUBLIC_DVD_MARKETNOTICEDATA_\d{6}\.ctl` | `PUBLIC_DVD_MARKETNOTICEDATA_201506.ctl` | 38 | 2017-01-15 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETNOTICEDATA_{yearmonth}.ctlBak` | `PUBLIC_DVD_MARKETNOTICEDATA_\d{6}\.ctlBak` | `PUBLIC_DVD_MARKETNOTICEDATA_201511.ctlBak` | 1 | 2017-01-15 | 2017-01-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETNOTICEDATA_{yearmonth}.ctlbak` | `PUBLIC_DVD_MARKETNOTICEDATA_\d{6}\.ctlbak` | `PUBLIC_DVD_MARKETNOTICEDATA_201501.ctlbak` | 14 | 2017-01-14 | 2017-01-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETNOTICETYPE_{yearmonth}.ctl` | `PUBLIC_DVD_MARKETNOTICETYPE_\d{6}\.ctl` | `PUBLIC_DVD_MARKETNOTICETYPE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETSUSPENSION_{yearmonth}.ctl` | `PUBLIC_DVD_MARKETSUSPENSION_\d{6}\.ctl` | `PUBLIC_DVD_MARKETSUSPENSION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKETSUSREGION_{yearmonth}.ctl` | `PUBLIC_DVD_MARKETSUSREGION_\d{6}\.ctl` | `PUBLIC_DVD_MARKETSUSREGION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_{yearmonth}.ctl` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_\d{6}\.ctl` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MCC_CASESOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_MCC_CASESOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_MCC_CASESOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MNSP_DAYOFFER_{yearmonth}.ctl` | `PUBLIC_DVD_MNSP_DAYOFFER_\d{6}\.ctl` | `PUBLIC_DVD_MNSP_DAYOFFER_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_{yearmonth}.ctl` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_\d{6}\.ctl` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MNSP_OFFERTRK_{yearmonth}.ctl` | `PUBLIC_DVD_MNSP_OFFERTRK_\d{6}\.ctl` | `PUBLIC_DVD_MNSP_OFFERTRK_201501.ctl` | 73 | 2017-01-14 | 2021-03-22 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MNSP_PARTICIPANT_{yearmonth}.ctl` | `PUBLIC_DVD_MNSP_PARTICIPANT_\d{6}\.ctl` | `PUBLIC_DVD_MNSP_PARTICIPANT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MNSP_PEROFFER_{yearmonth}.ctl` | `PUBLIC_DVD_MNSP_PEROFFER_\d{6}\.ctl` | `PUBLIC_DVD_MNSP_PEROFFER_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_CASERESULT_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_CASERESULT_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_CASERESULT_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_CASESOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_CASESOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_CASESOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_201501.ctl` | 41 | 2017-01-14 | 2018-06-13 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_201501.ctl` | 41 | 2017-01-14 | 2018-06-13 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_LOLPRESULT_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_LOLPRESULT_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_LOLPRESULT_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_REGIONITERATION_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_REGIONITERATION_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_REGIONITERATION_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_REGIONRESULT_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_REGIONRESULT_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_REGIONRESULT_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_201501.ctl` | 41 | 2017-01-14 | 2018-06-13 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_201501.ctl` | 41 | 2017-01-14 | 2018-06-13 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_{yearmonth}.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_\d{6}\.ctl` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_OVERRIDERRP_{yearmonth}.ctl` | `PUBLIC_DVD_OVERRIDERRP_\d{6}\.ctl` | `PUBLIC_DVD_OVERRIDERRP_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_{yearmonth}.ctl` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_\d{6}\.ctl` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PARTICIPANTCATEGORY_{yearmonth}.ctl` | `PUBLIC_DVD_PARTICIPANTCATEGORY_\d{6}\.ctl` | `PUBLIC_DVD_PARTICIPANTCATEGORY_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PARTICIPANTCLASS_{yearmonth}.ctl` | `PUBLIC_DVD_PARTICIPANTCLASS_\d{6}\.ctl` | `PUBLIC_DVD_PARTICIPANTCLASS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PARTICIPANT_{yearmonth}.ctl` | `PUBLIC_DVD_PARTICIPANT_\d{6}\.ctl` | `PUBLIC_DVD_PARTICIPANT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PDPASA_CASESOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_PDPASA_CASESOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_PDPASA_CASESOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_202104.ctl` | 40 | 2021-05-12 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_{yearmonth}.ctl` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_\d{6}\.ctl` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_202104.ctl` | 40 | 2021-05-12 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PERDEMAND_{yearmonth}.ctl` | `PUBLIC_DVD_PERDEMAND_\d{6}\.ctl` | `PUBLIC_DVD_PERDEMAND_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT{d1}_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT\d{1}_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT2_201803.ctl` | 1 | 2018-04-20 | 2018-04-20 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHLOAD_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHLOAD_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHLOAD_D_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHPRICE_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHPRICE_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHPRICE_D_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_202210.ctl` | 22 | 2022-11-09 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_{yearmonth}.ctl` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_\d{6}\.ctl` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_PRUDENTIALRUNTRK_{yearmonth}.ctl` | `PUBLIC_DVD_PRUDENTIALRUNTRK_\d{6}\.ctl` | `PUBLIC_DVD_PRUDENTIALRUNTRK_201501.ctl` | 77 | 2017-01-14 | 2021-07-03 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_P{d1}MINSCENARIODEMANDTRK_{yearmonth}.ctl` | `PUBLIC_DVD_P\d{1}MINSCENARIODEMANDTRK_\d{6}\.ctl` | `PUBLIC_DVD_P5MINSCENARIODEMANDTRK_202106.ctl` | 38 | 2021-07-13 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_P{d1}MINSCENARIODEMAND_{yearmonth}.ctl` | `PUBLIC_DVD_P\d{1}MINSCENARIODEMAND_\d{6}\.ctl` | `PUBLIC_DVD_P5MINSCENARIODEMAND_202106.ctl` | 38 | 2021-07-13 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_P{d1}MIN_CASESOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_P\d{1}MIN_CASESOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_P5MIN_CASESOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_P{d11}MIN_CONSTRAINTSOLUTION{d12}_{yearmonth}.ctl` | `PUBLIC_DVD_P\d{1}MIN_CONSTRAINTSOLUTION\d{1}_\d{6}\.ctl` | `PUBLIC_DVD_P5MIN_CONSTRAINTSOLUTION1_201501.ctl` | 459 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_P{d1}MIN_INTERCONNECTORSOLN_{yearmonth}.ctl` | `PUBLIC_DVD_P\d{1}MIN_INTERCONNECTORSOLN_\d{6}\.ctl` | `PUBLIC_DVD_P5MIN_INTERCONNECTORSOLN_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_P{d1}MIN_REGIONSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_P\d{1}MIN_REGIONSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_P5MIN_REGIONSOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_P{d1}MIN_UNITSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_P\d{1}MIN_UNITSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_P5MIN_UNITSOLUTION_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_REGIONAPCINTERVALS_{yearmonth}.ctl` | `PUBLIC_DVD_REGIONAPCINTERVALS_\d{6}\.ctl` | `PUBLIC_DVD_REGIONAPCINTERVALS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_REGIONAPC_{yearmonth}.ctl` | `PUBLIC_DVD_REGIONAPC_\d{6}\.ctl` | `PUBLIC_DVD_REGIONAPC_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_REGIONSTANDINGDATA_{yearmonth}.ctl` | `PUBLIC_DVD_REGIONSTANDINGDATA_\d{6}\.ctl` | `PUBLIC_DVD_REGIONSTANDINGDATA_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_REGION_{yearmonth}.ctl` | `PUBLIC_DVD_REGION_\d{6}\.ctl` | `PUBLIC_DVD_REGION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_RESDEMANDTRK_{yearmonth}.ctl` | `PUBLIC_DVD_RESDEMANDTRK_\d{6}\.ctl` | `PUBLIC_DVD_RESDEMANDTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_RESERVE_{yearmonth}.ctl` | `PUBLIC_DVD_RESERVE_\d{6}\.ctl` | `PUBLIC_DVD_RESERVE_201501.ctl` | 27 | 2017-01-14 | 2018-06-13 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_RESIDUE_CONTRACTS_{yearmonth}.ctl` | `PUBLIC_DVD_RESIDUE_CONTRACTS_\d{6}\.ctl` | `PUBLIC_DVD_RESIDUE_CONTRACTS_201503.ctl` | 79 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_{yearmonth}.ctl` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_\d{6}\.ctl` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_201505.ctl` | 39 | 2017-01-15 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_{yearmonth}.ctl` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_\d{6}\.ctl` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_201503.ctl` | 42 | 2017-01-14 | 2024-07-23 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_{yearmonth}.ctl` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_\d{6}\.ctl` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_201503.ctl` | 46 | 2017-01-14 | 2024-07-23 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_RESIDUE_TRK_{yearmonth}.ctl` | `PUBLIC_DVD_RESIDUE_TRK_\d{6}\.ctl` | `PUBLIC_DVD_RESIDUE_TRK_201503.ctl` | 47 | 2017-01-14 | 2024-07-23 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_{yearmonth}.ctl` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_\d{6}\.ctl` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_{yearmonth}.ctl` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_\d{6}\.ctl` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_201910.ctl` | 58 | 2019-11-18 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_{yearmonth}.ctl` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_\d{6}\.ctl` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_{yearmonth}.ctl` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_\d{6}\.ctl` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SETCPDATAREGION_{yearmonth}.ctl` | `PUBLIC_DVD_SETCPDATAREGION_\d{6}\.ctl` | `PUBLIC_DVD_SETCPDATAREGION_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_{yearmonth}.ctl` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_\d{6}\.ctl` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SETGENDATAREGION_{yearmonth}.ctl` | `PUBLIC_DVD_SETGENDATAREGION_\d{6}\.ctl` | `PUBLIC_DVD_SETGENDATAREGION_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_{yearmonth}.ctl` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_\d{6}\.ctl` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SETIRSURPLUS_{yearmonth}.ctl` | `PUBLIC_DVD_SETIRSURPLUS_\d{6}\.ctl` | `PUBLIC_DVD_SETIRSURPLUS_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_{yearmonth}.ctl` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_\d{6}\.ctl` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_{yearmonth}.ctl` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_\d{6}\.ctl` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_201501.ctl` | 114 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_{yearmonth}.ctl` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_\d{6}\.ctl` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_{yearmonth}.ctl` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_\d{6}\.ctl` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_{yearmonth}.ctl` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_\d{6}\.ctl` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_201501.ctl` | 79 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STADUALLOC_{yearmonth}.ctl` | `PUBLIC_DVD_STADUALLOC_\d{6}\.ctl` | `PUBLIC_DVD_STADUALLOC_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_{yearmonth}.ctl` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_\d{6}\.ctl` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STATIONOWNERTRK_{yearmonth}.ctl` | `PUBLIC_DVD_STATIONOWNERTRK_\d{6}\.ctl` | `PUBLIC_DVD_STATIONOWNERTRK_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STATIONOWNER_{yearmonth}.ctl` | `PUBLIC_DVD_STATIONOWNER_\d{6}\.ctl` | `PUBLIC_DVD_STATIONOWNER_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STATION_{yearmonth}.ctl` | `PUBLIC_DVD_STATION_\d{6}\.ctl` | `PUBLIC_DVD_STATION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STPASA_CASESOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_STPASA_CASESOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_STPASA_CASESOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_{yearmonth}.ctl` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_\d{6}\.ctl` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_{yearmonth}.ctl` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_\d{6}\.ctl` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_TRADINGINTERCONNECT_{yearmonth}.ctl` | `PUBLIC_DVD_TRADINGINTERCONNECT_\d{6}\.ctl` | `PUBLIC_DVD_TRADINGINTERCONNECT_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_TRADINGLOAD_{yearmonth}.ctl` | `PUBLIC_DVD_TRADINGLOAD_\d{6}\.ctl` | `PUBLIC_DVD_TRADINGLOAD_201501.ctl` | 81 | 2017-01-14 | 2021-10-11 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_TRADINGPRICE_{yearmonth}.ctl` | `PUBLIC_DVD_TRADINGPRICE_\d{6}\.ctl` | `PUBLIC_DVD_TRADINGPRICE_201501.ctl` | 115 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_TRADINGREGIONSUM_{yearmonth}.ctl` | `PUBLIC_DVD_TRADINGREGIONSUM_\d{6}\.ctl` | `PUBLIC_DVD_TRADINGREGIONSUM_201501.ctl` | 81 | 2017-01-14 | 2021-10-11 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_{yearmonth}.ctl` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_\d{6}\.ctl` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_201501.ctl` | 110 | 2017-01-14 | 2024-08-15 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 27 | 2017-02-06 | 2018-04-20 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_{timestamp}.zip` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_\d{12}\.zip` | `PUBLIC_DVD_ANCILLARY_RECOVERY_SPLIT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_APEVENTREGION_{timestamp}.zip` | `PUBLIC_DVD_APEVENTREGION_\d{12}\.zip` | `PUBLIC_DVD_APEVENTREGION_201510010000.zip` | 13 | 2017-01-15 | 2024-06-12 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_APEVENT_{timestamp}.zip` | `PUBLIC_DVD_APEVENT_\d{12}\.zip` | `PUBLIC_DVD_APEVENT_201510010000.zip` | 13 | 2017-01-15 | 2024-06-12 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_AUCTION_CALENDAR_{timestamp}.zip` | `PUBLIC_DVD_AUCTION_CALENDAR_\d{12}\.zip` | `PUBLIC_DVD_AUCTION_CALENDAR_201501010000.zip` | 53 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_{timestamp}.zip` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_\d{12}\.zip` | `PUBLIC_DVD_AUCTION_IC_ALLOCATIONS_201501010000.zip` | 78 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_AUCTION_TRANCHE_{timestamp}.zip` | `PUBLIC_DVD_AUCTION_TRANCHE_\d{12}\.zip` | `PUBLIC_DVD_AUCTION_TRANCHE_201501010000.zip` | 41 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_AUCTION_{timestamp}.zip` | `PUBLIC_DVD_AUCTION_\d{12}\.zip` | `PUBLIC_DVD_AUCTION_201503010000.zip` | 79 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDDAYOFFER_D_{timestamp}.zip` | `PUBLIC_DVD_BIDDAYOFFER_D_\d{12}\.zip` | `PUBLIC_DVD_BIDDAYOFFER_D_201501010000.zip` | 74 | 2017-01-14 | 2021-03-22 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDDAYOFFER_{timestamp}.zip` | `PUBLIC_DVD_BIDDAYOFFER_\d{12}\.zip` | `PUBLIC_DVD_BIDDAYOFFER_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_{timestamp}.zip` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_\d{12}\.zip` | `PUBLIC_DVD_BIDDUIDDETAILSTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDDUIDDETAILS_{timestamp}.zip` | `PUBLIC_DVD_BIDDUIDDETAILS_\d{12}\.zip` | `PUBLIC_DVD_BIDDUIDDETAILS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDPEROFFER{d1}_{timestamp}.zip` | `PUBLIC_DVD_BIDPEROFFER\d{1}_\d{12}\.zip` | `PUBLIC_DVD_BIDPEROFFER1_202206010000.zip` | 52 | 2022-07-21 | 2024-08-16 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDPEROFFER_D_{timestamp}.zip` | `PUBLIC_DVD_BIDPEROFFER_D_\d{12}\.zip` | `PUBLIC_DVD_BIDPEROFFER_D_201501010000.zip` | 74 | 2017-01-14 | 2021-03-22 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDPEROFFER_{timestamp}.zip` | `PUBLIC_DVD_BIDPEROFFER_\d{12}\.zip` | `PUBLIC_DVD_BIDPEROFFER_201501010000.zip` | 88 | 2017-01-14 | 2022-06-09 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDTYPESTRK_{timestamp}.zip` | `PUBLIC_DVD_BIDTYPESTRK_\d{12}\.zip` | `PUBLIC_DVD_BIDTYPESTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BIDTYPES_{timestamp}.zip` | `PUBLIC_DVD_BIDTYPES_\d{12}\.zip` | `PUBLIC_DVD_BIDTYPES_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLINGCALENDAR_{timestamp}.zip` | `PUBLIC_DVD_BILLINGCALENDAR_\d{12}\.zip` | `PUBLIC_DVD_BILLINGCALENDAR_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLINGDAYTRK_{timestamp}.zip` | `PUBLIC_DVD_BILLINGDAYTRK_\d{12}\.zip` | `PUBLIC_DVD_BILLINGDAYTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_{timestamp}.zip` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_\d{12}\.zip` | `PUBLIC_DVD_BILLINGREGIONEXPORTS_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLINGREGIONFIGURES_{timestamp}.zip` | `PUBLIC_DVD_BILLINGREGIONFIGURES_\d{12}\.zip` | `PUBLIC_DVD_BILLINGREGIONFIGURES_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_{timestamp}.zip` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_\d{12}\.zip` | `PUBLIC_DVD_BILLINGREGIONIMPORTS_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLINGRUNTRK_{timestamp}.zip` | `PUBLIC_DVD_BILLINGRUNTRK_\d{12}\.zip` | `PUBLIC_DVD_BILLINGRUNTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLING_CO{d1}E_PUBLICATION_TRK_{timestamp}.zip` | `PUBLIC_DVD_BILLING_CO\d{1}E_PUBLICATION_TRK_\d{12}\.zip` | `PUBLIC_DVD_BILLING_CO2E_PUBLICATION_TRK_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLING_CO{d1}E_PUBLICATION_{timestamp}.zip` | `PUBLIC_DVD_BILLING_CO\d{1}E_PUBLICATION_\d{12}\.zip` | `PUBLIC_DVD_BILLING_CO2E_PUBLICATION_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_BILLSMELTERRATE_{timestamp}.zip` | `PUBLIC_DVD_BILLSMELTERRATE_\d{12}\.zip` | `PUBLIC_DVD_BILLSMELTERRATE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DAYTRACK_{timestamp}.zip` | `PUBLIC_DVD_DAYTRACK_\d{12}\.zip` | `PUBLIC_DVD_DAYTRACK_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHABLEUNIT_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHABLEUNIT_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHABLEUNIT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHCASESOLUTION_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHCASESOLUTION_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHCASESOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHCONSTRAINT_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHCONSTRAINT_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHCONSTRAINT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHINTERCONNECTORRES_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHLOAD_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHLOAD_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHLOAD_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHOFFERTRK_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHOFFERTRK_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHOFFERTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHPRICE_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHPRICE_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHPRICE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCHREGIONSUM_{timestamp}.zip` | `PUBLIC_DVD_DISPATCHREGIONSUM_\d{12}\.zip` | `PUBLIC_DVD_DISPATCHREGIONSUM_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_{timestamp}.zip` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_\d{12}\.zip` | `PUBLIC_DVD_DISPATCH_FCAS_REQ_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_{timestamp}.zip` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_\d{12}\.zip` | `PUBLIC_DVD_DISPATCH_MNSPBIDTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_{timestamp}.zip` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_\d{12}\.zip` | `PUBLIC_DVD_DISPATCH_PRICE_REVISION_201502010000.zip` | 25 | 2017-01-15 | 2024-03-09 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_{timestamp}.zip` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_\d{12}\.zip` | `PUBLIC_DVD_DISPATCH_UNIT_SCADA_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DUALLOC_{timestamp}.zip` | `PUBLIC_DVD_DUALLOC_\d{12}\.zip` | `PUBLIC_DVD_DUALLOC_202010010000.zip` | 46 | 2020-11-12 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DUDETAILSUMMARY_{timestamp}.zip` | `PUBLIC_DVD_DUDETAILSUMMARY_\d{12}\.zip` | `PUBLIC_DVD_DUDETAILSUMMARY_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_DUDETAIL_{timestamp}.zip` | `PUBLIC_DVD_DUDETAIL_\d{12}\.zip` | `PUBLIC_DVD_DUDETAIL_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_EMSMASTER_{timestamp}.zip` | `PUBLIC_DVD_EMSMASTER_\d{12}\.zip` | `PUBLIC_DVD_EMSMASTER_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GDINSTRUCT_{timestamp}.zip` | `PUBLIC_DVD_GDINSTRUCT_\d{12}\.zip` | `PUBLIC_DVD_GDINSTRUCT_201501010000.zip` | 24 | 2017-01-14 | 2018-07-09 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENCONDATA_{timestamp}.zip` | `PUBLIC_DVD_GENCONDATA_\d{12}\.zip` | `PUBLIC_DVD_GENCONDATA_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENCONSETINVOKE_{timestamp}.zip` | `PUBLIC_DVD_GENCONSETINVOKE_\d{12}\.zip` | `PUBLIC_DVD_GENCONSETINVOKE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENCONSETTRK_{timestamp}.zip` | `PUBLIC_DVD_GENCONSETTRK_\d{12}\.zip` | `PUBLIC_DVD_GENCONSETTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENCONSET_{timestamp}.zip` | `PUBLIC_DVD_GENCONSET_\d{12}\.zip` | `PUBLIC_DVD_GENCONSET_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_{timestamp}.zip` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_\d{12}\.zip` | `PUBLIC_DVD_GENERICCONSTRAINTRHS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENERICEQUATIONDESC_{timestamp}.zip` | `PUBLIC_DVD_GENERICEQUATIONDESC_\d{12}\.zip` | `PUBLIC_DVD_GENERICEQUATIONDESC_201501010000.zip` | 105 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENERICEQUATIONRHS_{timestamp}.zip` | `PUBLIC_DVD_GENERICEQUATIONRHS_\d{12}\.zip` | `PUBLIC_DVD_GENERICEQUATIONRHS_201501010000.zip` | 109 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GENUNITS_{timestamp}.zip` | `PUBLIC_DVD_GENUNITS_\d{12}\.zip` | `PUBLIC_DVD_GENUNITS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GST_BAS_CLASS_{timestamp}.zip` | `PUBLIC_DVD_GST_BAS_CLASS_\d{12}\.zip` | `PUBLIC_DVD_GST_BAS_CLASS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GST_RATE_{timestamp}.zip` | `PUBLIC_DVD_GST_RATE_\d{12}\.zip` | `PUBLIC_DVD_GST_RATE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_{timestamp}.zip` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_\d{12}\.zip` | `PUBLIC_DVD_GST_TRANSACTION_CLASS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_{timestamp}.zip` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_\d{12}\.zip` | `PUBLIC_DVD_GST_TRANSACTION_TYPE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_{timestamp}.zip` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_\d{12}\.zip` | `PUBLIC_DVD_INSTRUCTIONSUBTYPE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_INSTRUCTIONTYPE_{timestamp}.zip` | `PUBLIC_DVD_INSTRUCTIONTYPE_\d{12}\.zip` | `PUBLIC_DVD_INSTRUCTIONTYPE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_{timestamp}.zip` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_\d{12}\.zip` | `PUBLIC_DVD_INTERCONNECTORCONSTRAINT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_INTERCONNECTOR_{timestamp}.zip` | `PUBLIC_DVD_INTERCONNECTOR_\d{12}\.zip` | `PUBLIC_DVD_INTERCONNECTOR_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_INTERCONNMWFLOW_{timestamp}.zip` | `PUBLIC_DVD_INTERCONNMWFLOW_\d{12}\.zip` | `PUBLIC_DVD_INTERCONNMWFLOW_201501010000.zip` | 77 | 2017-01-14 | 2021-07-03 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_IRFMAMOUNT_{timestamp}.zip` | `PUBLIC_DVD_IRFMAMOUNT_\d{12}\.zip` | `PUBLIC_DVD_IRFMAMOUNT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_IRFMEVENTS_{timestamp}.zip` | `PUBLIC_DVD_IRFMEVENTS_\d{12}\.zip` | `PUBLIC_DVD_IRFMEVENTS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_LOSSFACTORMODEL_{timestamp}.zip` | `PUBLIC_DVD_LOSSFACTORMODEL_\d{12}\.zip` | `PUBLIC_DVD_LOSSFACTORMODEL_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_LOSSMODEL_{timestamp}.zip` | `PUBLIC_DVD_LOSSMODEL_\d{12}\.zip` | `PUBLIC_DVD_LOSSMODEL_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKETFEEDATA_{timestamp}.zip` | `PUBLIC_DVD_MARKETFEEDATA_\d{12}\.zip` | `PUBLIC_DVD_MARKETFEEDATA_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKETFEETRK_{timestamp}.zip` | `PUBLIC_DVD_MARKETFEETRK_\d{12}\.zip` | `PUBLIC_DVD_MARKETFEETRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKETFEE_{timestamp}.zip` | `PUBLIC_DVD_MARKETFEE_\d{12}\.zip` | `PUBLIC_DVD_MARKETFEE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKETNOTICEDATA_{timestamp}.zip` | `PUBLIC_DVD_MARKETNOTICEDATA_\d{12}\.zip` | `PUBLIC_DVD_MARKETNOTICEDATA_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKETNOTICETYPE_{timestamp}.zip` | `PUBLIC_DVD_MARKETNOTICETYPE_\d{12}\.zip` | `PUBLIC_DVD_MARKETNOTICETYPE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKETSUSPENSION_{timestamp}.zip` | `PUBLIC_DVD_MARKETSUSPENSION_\d{12}\.zip` | `PUBLIC_DVD_MARKETSUSPENSION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKETSUSREGION_{timestamp}.zip` | `PUBLIC_DVD_MARKETSUSREGION_\d{12}\.zip` | `PUBLIC_DVD_MARKETSUSREGION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_{timestamp}.zip` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_\d{12}\.zip` | `PUBLIC_DVD_MARKET_PRICE_THRESHOLDS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MCC_CASESOLUTION_{timestamp}.zip` | `PUBLIC_DVD_MCC_CASESOLUTION_\d{12}\.zip` | `PUBLIC_DVD_MCC_CASESOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_MCC_CONSTRAINTSOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MNSP_DAYOFFER_{timestamp}.zip` | `PUBLIC_DVD_MNSP_DAYOFFER_\d{12}\.zip` | `PUBLIC_DVD_MNSP_DAYOFFER_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_{timestamp}.zip` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_\d{12}\.zip` | `PUBLIC_DVD_MNSP_INTERCONNECTOR_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MNSP_OFFERTRK_{timestamp}.zip` | `PUBLIC_DVD_MNSP_OFFERTRK_\d{12}\.zip` | `PUBLIC_DVD_MNSP_OFFERTRK_201501010000.zip` | 73 | 2017-01-14 | 2021-03-22 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MNSP_PARTICIPANT_{timestamp}.zip` | `PUBLIC_DVD_MNSP_PARTICIPANT_\d{12}\.zip` | `PUBLIC_DVD_MNSP_PARTICIPANT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MNSP_PEROFFER_{timestamp}.zip` | `PUBLIC_DVD_MNSP_PEROFFER_\d{12}\.zip` | `PUBLIC_DVD_MNSP_PEROFFER_201501010000.zip` | 114 | 2017-01-14 | 2024-08-16 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_CASERESULT_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_CASERESULT_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_CASERESULT_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_CASESOLUTION_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_CASESOLUTION_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_CASESOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_CONSTRAINTRESULT_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_CONSTRAINTSOLUTION_201501010000.zip` | 41 | 2017-01-14 | 2018-06-13 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_CONSTRAINTSUMMARY_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_INTERCONNECTORRESULT_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_INTERCONNECTORSOLUTION_201501010000.zip` | 41 | 2017-01-14 | 2018-06-13 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_LOLPRESULT_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_LOLPRESULT_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_LOLPRESULT_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_REGIONITERATION_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_REGIONITERATION_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_REGIONITERATION_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_REGIONRESULT_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_REGIONRESULT_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_REGIONRESULT_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_REGIONSOLUTION_201501010000.zip` | 41 | 2017-01-14 | 2018-06-13 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_REGIONSUMMARY_201805010000.zip` | 75 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMITSOLUTION_201501010000.zip` | 41 | 2017-01-14 | 2018-06-13 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_REGION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_SET_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_{timestamp}.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_\d{12}\.zip` | `PUBLIC_DVD_MTPASA_RESERVELIMIT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_OVERRIDERRP_{timestamp}.zip` | `PUBLIC_DVD_OVERRIDERRP_\d{12}\.zip` | `PUBLIC_DVD_OVERRIDERRP_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_{timestamp}.zip` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_\d{12}\.zip` | `PUBLIC_DVD_PARTICIPANTCATEGORYALLOC_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PARTICIPANTCATEGORY_{timestamp}.zip` | `PUBLIC_DVD_PARTICIPANTCATEGORY_\d{12}\.zip` | `PUBLIC_DVD_PARTICIPANTCATEGORY_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PARTICIPANTCLASS_{timestamp}.zip` | `PUBLIC_DVD_PARTICIPANTCLASS_\d{12}\.zip` | `PUBLIC_DVD_PARTICIPANTCLASS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PARTICIPANT_{timestamp}.zip` | `PUBLIC_DVD_PARTICIPANT_\d{12}\.zip` | `PUBLIC_DVD_PARTICIPANT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PDPASA_CASESOLUTION_{timestamp}.zip` | `PUBLIC_DVD_PDPASA_CASESOLUTION_\d{12}\.zip` | `PUBLIC_DVD_PDPASA_CASESOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_PDPASA_CONSTRAINTSOLUTION_202102010000.zip` | 42 | 2021-03-22 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_{timestamp}.zip` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_\d{12}\.zip` | `PUBLIC_DVD_PDPASA_INTERCONNECTORSOLN_202102010000.zip` | 42 | 2021-03-22 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_PDPASA_REGIONSOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PERDEMAND_{timestamp}.zip` | `PUBLIC_DVD_PERDEMAND_\d{12}\.zip` | `PUBLIC_DVD_PERDEMAND_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHCASESOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT{d1}_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT\d{1}_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT2_201803010000.zip` | 1 | 2018-04-26 | 2018-04-26 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT_D_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_D_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTR_SENS_D_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHLOAD_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHLOAD_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHLOAD_D_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHOFFERTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHPRICESENSITIVITIE_D_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHPRICE_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHPRICE_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHPRICE_D_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_D_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMANDTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHSCENARIODEMAND_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCH_FCAS_REQ_D_202204010000.zip` | 28 | 2022-11-03 | 2024-08-16 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCH_MNSPBIDTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_PRUDENTIALRUNTRK_{timestamp}.zip` | `PUBLIC_DVD_PRUDENTIALRUNTRK_\d{12}\.zip` | `PUBLIC_DVD_PRUDENTIALRUNTRK_201501010000.zip` | 77 | 2017-01-14 | 2021-07-03 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_P{d1}MINSCENARIODEMANDTRK_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MINSCENARIODEMANDTRK_\d{12}\.zip` | `PUBLIC_DVD_P5MINSCENARIODEMANDTRK_202106010000.zip` | 38 | 2021-07-13 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_P{d1}MINSCENARIODEMAND_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MINSCENARIODEMAND_\d{12}\.zip` | `PUBLIC_DVD_P5MINSCENARIODEMAND_202106010000.zip` | 38 | 2021-07-13 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_P{d1}MIN_CASESOLUTION_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_CASESOLUTION_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_CASESOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_P{d11}MIN_CONSTRAINTSOLUTION{d12}_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_CONSTRAINTSOLUTION\d{1}_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_CONSTRAINTSOLUTION1_201501010000.zip` | 460 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_P{d1}MIN_INTERCONNECTORSOLN_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_INTERCONNECTORSOLN_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_INTERCONNECTORSOLN_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_P{d1}MIN_REGIONSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_REGIONSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_REGIONSOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_P{d1}MIN_UNITSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_UNITSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_UNITSOLUTION_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_REGIONAPCINTERVALS_{timestamp}.zip` | `PUBLIC_DVD_REGIONAPCINTERVALS_\d{12}\.zip` | `PUBLIC_DVD_REGIONAPCINTERVALS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_REGIONAPC_{timestamp}.zip` | `PUBLIC_DVD_REGIONAPC_\d{12}\.zip` | `PUBLIC_DVD_REGIONAPC_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_REGIONSTANDINGDATA_{timestamp}.zip` | `PUBLIC_DVD_REGIONSTANDINGDATA_\d{12}\.zip` | `PUBLIC_DVD_REGIONSTANDINGDATA_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_REGION_{timestamp}.zip` | `PUBLIC_DVD_REGION_\d{12}\.zip` | `PUBLIC_DVD_REGION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_RESDEMANDTRK_{timestamp}.zip` | `PUBLIC_DVD_RESDEMANDTRK_\d{12}\.zip` | `PUBLIC_DVD_RESDEMANDTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_RESERVE_{timestamp}.zip` | `PUBLIC_DVD_RESERVE_\d{12}\.zip` | `PUBLIC_DVD_RESERVE_201501010000.zip` | 27 | 2017-01-14 | 2018-06-13 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_RESIDUE_CONTRACTS_{timestamp}.zip` | `PUBLIC_DVD_RESIDUE_CONTRACTS_\d{12}\.zip` | `PUBLIC_DVD_RESIDUE_CONTRACTS_201503010000.zip` | 79 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_{timestamp}.zip` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_\d{12}\.zip` | `PUBLIC_DVD_RESIDUE_CON_FUNDS_201505010000.zip` | 39 | 2017-01-15 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_{timestamp}.zip` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_\d{12}\.zip` | `PUBLIC_DVD_RESIDUE_PRICE_FUNDS_BID_201503010000.zip` | 42 | 2017-01-14 | 2024-07-23 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_{timestamp}.zip` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_\d{12}\.zip` | `PUBLIC_DVD_RESIDUE_PUBLIC_DATA_201503010000.zip` | 46 | 2017-01-14 | 2024-07-23 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_RESIDUE_TRK_{timestamp}.zip` | `PUBLIC_DVD_RESIDUE_TRK_\d{12}\.zip` | `PUBLIC_DVD_RESIDUE_TRK_201503010000.zip` | 47 | 2017-01-14 | 2024-07-23 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_{timestamp}.zip` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_\d{12}\.zip` | `PUBLIC_DVD_ROOFTOP_PV_ACTUAL_201608010000.zip` | 96 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_{timestamp}.zip` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_\d{12}\.zip` | `PUBLIC_DVD_ROOFTOP_PV_FORECAST_201608010000.zip` | 96 | 2019-10-18 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_{timestamp}.zip` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_\d{12}\.zip` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPFTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_{timestamp}.zip` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_\d{12}\.zip` | `PUBLIC_DVD_SETCFG_PARTICIPANT_MPF_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SETCPDATAREGION_{timestamp}.zip` | `PUBLIC_DVD_SETCPDATAREGION_\d{12}\.zip` | `PUBLIC_DVD_SETCPDATAREGION_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_{timestamp}.zip` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_\d{12}\.zip` | `PUBLIC_DVD_SETFCASREGIONRECOVERY_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SETGENDATAREGION_{timestamp}.zip` | `PUBLIC_DVD_SETGENDATAREGION_\d{12}\.zip` | `PUBLIC_DVD_SETGENDATAREGION_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_{timestamp}.zip` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_\d{12}\.zip` | `PUBLIC_DVD_SETINTRAREGIONRESIDUES_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SETIRSURPLUS_{timestamp}.zip` | `PUBLIC_DVD_SETIRSURPLUS_\d{12}\.zip` | `PUBLIC_DVD_SETIRSURPLUS_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_{timestamp}.zip` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_\d{12}\.zip` | `PUBLIC_DVD_SET_ANCILLARY_SUMMARY_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_{timestamp}.zip` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_\d{12}\.zip` | `PUBLIC_DVD_SET_FCAS_REGULATION_TRK_201501010000.zip` | 114 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_{timestamp}.zip` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_\d{12}\.zip` | `PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_{timestamp}.zip` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_\d{12}\.zip` | `PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_{timestamp}.zip` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_\d{12}\.zip` | `PUBLIC_DVD_SPDREGIONCONSTRAINT_201501010000.zip` | 79 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STADUALLOC_{timestamp}.zip` | `PUBLIC_DVD_STADUALLOC_\d{12}\.zip` | `PUBLIC_DVD_STADUALLOC_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_{timestamp}.zip` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_\d{12}\.zip` | `PUBLIC_DVD_STATIONOPERATINGSTATUS_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STATIONOWNERTRK_{timestamp}.zip` | `PUBLIC_DVD_STATIONOWNERTRK_\d{12}\.zip` | `PUBLIC_DVD_STATIONOWNERTRK_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STATIONOWNER_{timestamp}.zip` | `PUBLIC_DVD_STATIONOWNER_\d{12}\.zip` | `PUBLIC_DVD_STATIONOWNER_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STATION_{timestamp}.zip` | `PUBLIC_DVD_STATION_\d{12}\.zip` | `PUBLIC_DVD_STATION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STPASA_CASESOLUTION_{timestamp}.zip` | `PUBLIC_DVD_STPASA_CASESOLUTION_\d{12}\.zip` | `PUBLIC_DVD_STPASA_CASESOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_STPASA_CONSTRAINTSOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_{timestamp}.zip` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_\d{12}\.zip` | `PUBLIC_DVD_STPASA_INTERCONNECTORSOLN_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_{timestamp}.zip` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_\d{12}\.zip` | `PUBLIC_DVD_STPASA_REGIONSOLUTION_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_TRADINGINTERCONNECT_{timestamp}.zip` | `PUBLIC_DVD_TRADINGINTERCONNECT_\d{12}\.zip` | `PUBLIC_DVD_TRADINGINTERCONNECT_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_TRADINGLOAD_{timestamp}.zip` | `PUBLIC_DVD_TRADINGLOAD_\d{12}\.zip` | `PUBLIC_DVD_TRADINGLOAD_201501010000.zip` | 81 | 2017-01-14 | 2021-10-11 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_TRADINGPRICE_{timestamp}.zip` | `PUBLIC_DVD_TRADINGPRICE_\d{12}\.zip` | `PUBLIC_DVD_TRADINGPRICE_201501010000.zip` | 115 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_TRADINGREGIONSUM_{timestamp}.zip` | `PUBLIC_DVD_TRADINGREGIONSUM_\d{12}\.zip` | `PUBLIC_DVD_TRADINGREGIONSUM_201501010000.zip` | 81 | 2017-01-14 | 2021-10-11 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_{timestamp}.zip` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_\d{12}\.zip` | `PUBLIC_DVD_TRANSMISSIONLOSSFACTOR_201501010000.zip` | 110 | 2017-01-14 | 2024-08-15 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_MARKETNOTICEDATA_{yearmonth}.DMP` | `PUBLIC_MARKETNOTICEDATA_\d{6}\.DMP` | `PUBLIC_MARKETNOTICEDATA_201501.DMP` | 115 | 2017-01-14 | 2024-08-16 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_RUN_SQLLDR_{yearmonth}.bat` | `PUBLIC_RUN_SQLLDR_\d{6}\.bat` | `PUBLIC_RUN_SQLLDR_201501.bat` | 135 | 2017-01-14 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 27 | 2017-02-06 | 2018-04-20 |
| `INDEX` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/INDEX/` | `PUBLIC_MONTHLY_DVD_INDEX_{yearmonth}.TXT` | `PUBLIC_MONTHLY_DVD_INDEX_\d{6}\.TXT` | `PUBLIC_MONTHLY_DVD_INDEX_201501.TXT` | 115 | 2017-01-14 | 2024-08-16 |
| `INDEX` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/INDEX/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 27 | 2017-02-06 | 2018-04-20 |
| `LOGS` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/LOGS/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 27 | 2017-02-06 | 2018-04-20 |
| `P5MIN_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/P{d1}MIN_ALL_DATA/` | `PUBLIC_DVD_P{d11}MIN_CONSTRAINTSOLUTION{d12}_ALL_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_CONSTRAINTSOLUTION\d{1}_ALL_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_CONSTRAINTSOLUTION1_ALL_201903010000.zip` | 260 | 2019-05-15 | 2024-08-16 |
| `P5MIN_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/P{d1}MIN_ALL_DATA/` | `PUBLIC_DVD_P{d1}MIN_INTERCONNECTORSOLN_ALL_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_INTERCONNECTORSOLN_ALL_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_INTERCONNECTORSOLN_ALL_201903010000.zip` | 65 | 2019-05-15 | 2024-08-16 |
| `P5MIN_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/P{d1}MIN_ALL_DATA/` | `PUBLIC_DVD_P{d1}MIN_REGIONSOLUTION_ALL_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_REGIONSOLUTION_ALL_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_REGIONSOLUTION_ALL_201903010000.zip` | 65 | 2019-05-15 | 2024-08-16 |
| `P5MIN_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/P{d1}MIN_ALL_DATA/` | `PUBLIC_DVD_P{d1}MIN_UNITSOLUTION_ALL_{timestamp}.zip` | `PUBLIC_DVD_P\d{1}MIN_UNITSOLUTION_ALL_\d{12}\.zip` | `PUBLIC_DVD_P5MIN_UNITSOLUTION_ALL_201903010000.zip` | 65 | 2019-05-15 | 2024-08-16 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT{d1}_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT\d{1}_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHCONSTRAINT1_201501010000.zip` | 228 | 2017-01-14 | 2024-08-16 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHINTERCONNECTORRES_201501010000.zip` | 114 | 2017-01-14 | 2024-08-16 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_DVD_PREDISPATCHLOAD{d1}_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHLOAD\d{1}_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHLOAD1_201501010000.zip` | 228 | 2017-01-14 | 2024-08-16 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_DVD_PREDISPATCHPRICE_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHPRICE_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHPRICE_201501010000.zip` | 114 | 2017-01-14 | 2024-08-16 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_{timestamp}.zip` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_\d{12}\.zip` | `PUBLIC_DVD_PREDISPATCHREGIONSUM_201501010000.zip` | 114 | 2017-01-14 | 2024-08-16 |
| `PREDISP_ALL_DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/PREDISP_ALL_DATA/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 27 | 2017-02-06 | 2018-04-20 |
| `Readme.htm` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 38 | 2017-02-07 | 2019-03-14 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `BCPTransform.log` | `BCPTransform\.log` | `BCPTransform.log` | 41 | 2022-12-11 | 2025-10-17 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `CRLF.TXT` | `CRLF\.TXT` | `CRLF.TXT` | 134 | 2019-09-05 | 2025-10-17 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `Crlf.exe` | `Crlf\.exe` | `Crlf.exe` | 134 | 2019-09-05 | 2025-10-17 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `ICSharpCode.SharpZipLib.dll` | `ICSharpCode\.SharpZipLib\.dll` | `ICSharpCode.SharpZipLib.dll` | 93 | 2019-09-17 | 2022-10-09 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `PUBLIC_CONVERT_BCP.bat` | `PUBLIC_CONVERT_BCP\.bat` | `PUBLIC_CONVERT_BCP.bat` | 134 | 2019-09-05 | 2025-10-17 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `PUBLIC_RUN_BCP_{yearmonth}.bat` | `PUBLIC_RUN_BCP_\d{6}\.bat` | `PUBLIC_RUN_BCP_201501.bat` | 134 | 2019-09-05 | 2026-04-08 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `PUBLIC_RUN_MYSQL_{yearmonth}.bat` | `PUBLIC_RUN_MYSQL_\d{6}\.bat` | `PUBLIC_RUN_MYSQL_202408.bat` | 20 | 2024-09-13 | 2026-04-08 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `bcpt.dll` | `bcpt\.dll` | `bcpt.dll` | 41 | 2022-12-11 | 2025-10-17 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `bcpt.exe` | `bcpt\.exe` | `bcpt.exe` | 134 | 2019-09-17 | 2025-10-17 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `bcpt.ini` | `bcpt\.ini` | `bcpt.ini` | 134 | 2019-09-17 | 2025-10-17 |
| `UTILITIES` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/UTILITIES/` | `bcpt.runtimeconfig.json` | `bcpt\.runtimeconfig\.json` | `bcpt.runtimeconfig.json` | 41 | 2022-12-11 | 2025-10-17 |
| `background1.gif` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/` | `background{d1}.gif` | `background\d{1}\.gif` | `background1.gif` | 13 | 2018-03-19 | 2019-03-14 |
| `disclaimer.htm` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/` | `disclaimer.htm` | `disclaimer\.htm` | `disclaimer.htm` | 38 | 2017-02-07 | 2019-03-14 |
| `file.gif` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/` | `file.gif` | `file\.gif` | `file.gif` | 50 | 1999-05-23 | 2019-03-14 |
| `nemlogo1.gif` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/` | `nemlogo{d1}.gif` | `nemlogo\d{1}\.gif` | `nemlogo1.gif` | 50 | 2009-08-17 | 2019-03-14 |
| `nemlogo2.gif` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/` | `nemlogo{d1}.gif` | `nemlogo\d{1}\.gif` | `nemlogo2.gif` | 50 | 2009-08-17 | 2019-03-14 |

### `MMSDM` · `VOLTAGE_INSTRUCTION`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

### `MMSDM` · `VOLTAGE_INSTRUCTION_TRK`

_4 pattern rows, 79 files (snapshot), observed 2024-09-12 → 2026-04-08 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `BCP_FMT` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/BCP_FMT/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE{d2}#{yearmonth}.fmt` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION_TRK\#FILE\d{2}\#\d{6}\.fmt` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE01#202408.fmt` | 20 | 2024-09-12 | 2026-04-08 |
| `CTL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/CTL/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE{d2}#{yearmonth}.ctl` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION_TRK\#FILE\d{2}\#\d{6}\.ctl` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE01#202408.ctl` | 20 | 2024-09-12 | 2026-04-08 |
| `DATA` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/DATA/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE{d2}#{timestamp}.zip` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION_TRK\#FILE\d{2}\#\d{12}\.zip` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE01#202408010000.zip` | 20 | 2024-09-12 | 2026-04-07 |
| `MYSQL` | `/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{d2}/MMSDM_Historical_Data_SQLLoader/MYSQL/` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE{d2}#{yearmonth}.sql` | `PUBLIC_ARCHIVE\#VOLTAGE_INSTRUCTION_TRK\#FILE\d{2}\#\d{6}\.sql` | `PUBLIC_ARCHIVE#VOLTAGE_INSTRUCTION_TRK#FILE01#202408.sql` | 19 | 2024-09-13 | 2026-04-08 |

## Repo: `NEMDE`  (7 datasets, 36 rows)

### `NEMDE` · `NEMDE 1-18 File Readers`

_1 pattern row, 201 files (snapshot), observed 2004-05-13 → 2024-09-13 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `File_Readers` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/File_Readers/` | `NEMDE {d1}-{d2} File Readers.zip` | `NEMDE\ \d{1}\-\d{2}\ File\ Readers\.zip` | `NEMDE 1-18 File Readers.zip` | 201 | 2004-05-13 | 2024-09-13 |

### `NEMDE` · `NEMSPDOutputs`

_6 pattern rows, 8 files (snapshot), observed 2017-01-12 → 2022-07-21 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NEMSPDOutputs_{d11}_OCD_RESOLVED{d2}_OCD.zip` | `NEMSPDOutputs_\d{11}_OCD_RESOLVED\d{2}_OCD\.zip` | `NEMSPDOutputs_20220604167_OCD_RESOLVED00_OCD.zip` | 1 | 2022-07-21 | 2022-07-21 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NEMSPDOutputs_{d13}_OCD.zip` | `NEMSPDOutputs_\d{13}_OCD\.zip` | `NEMSPDOutputs_2011110909700_OCD.zip` | 2 | 2017-01-13 | 2017-01-13 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NEMSPDOutputs_{date}_Manual_OCD.zip` | `NEMSPDOutputs_\d{8}_Manual_OCD\.zip` | `NEMSPDOutputs_20100810_Manual_OCD.zip` | 2 | 2017-01-12 | 2017-01-14 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NEMSPDOutputs_{date}_OCD.zip` | `NEMSPDOutputs_\d{8}_OCD\.zip` | `NEMSPDOutputs_20150213_OCD.zip` | 1 | 2017-01-15 | 2017-01-15 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NEMSPDOutputs_{date}_{d1}_loaded_OCD.zip` | `NEMSPDOutputs_\d{8}_\d{1}_loaded_OCD\.zip` | `NEMSPDOutputs_20161130_1_loaded_OCD.zip` | 1 | 2017-01-15 | 2017-01-15 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NEMSPDOutputs_{date}_loaded_OCD.zip` | `NEMSPDOutputs_\d{8}_loaded_OCD\.zip` | `NEMSPDOutputs_20161201_loaded_OCD.zip` | 1 | 2017-03-13 | 2017-03-13 |

### `NEMDE` · `NemPriceSetter`

_1 pattern row, 6118 files (snapshot), observed 2017-01-12 → 2026-04-01 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NemPriceSetter_{date}_xml.zip` | `NemPriceSetter_\d{8}_xml\.zip` | `NemPriceSetter_20090701_xml.zip` | 6118 | 2017-01-12 | 2026-04-01 |

### `NEMDE` · `NemSpdOutputs`

_6 pattern rows, 6123 files (snapshot), observed 2017-01-12 → 2026-04-01 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NemSpdOutputs_{d11}_ManualOCD{year}.zip` | `NemSpdOutputs_\d{11}_ManualOCD\d{4}\.zip` | `NemSpdOutputs_20091103139_ManualOCD0100.zip` | 1 | 2017-01-12 | 2017-01-12 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NemSpdOutputs_{d11}_ManualOCD{year}_OCD.zip` | `NemSpdOutputs_\d{11}_ManualOCD\d{4}_OCD\.zip` | `NemSpdOutputs_20090911185_ManualOCD0000_OCD.zip` | 1 | 2017-01-12 | 2017-01-12 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NemSpdOutputs_{date}_OCD_Resolved.zip` | `NemSpdOutputs_\d{8}_OCD_Resolved\.zip` | `NemSpdOutputs_20200201_OCD_Resolved.zip` | 1 | 2020-03-10 | 2020-03-10 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NemSpdOutputs_{date}_OCD_loaded.zip` | `NemSpdOutputs_\d{8}_OCD_loaded\.zip` | `NemSpdOutputs_20101102_OCD_loaded.zip` | 1 | 2017-01-13 | 2017-01-13 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NemSpdOutputs_{date}_loaded.zip` | `NemSpdOutputs_\d{8}_loaded\.zip` | `NemSpdOutputs_20090701_loaded.zip` | 6118 | 2017-01-12 | 2026-04-01 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `NemSpdOutputs_{date}_loaded_OCD.zip` | `NemSpdOutputs_\d{8}_loaded_OCD\.zip` | `NemSpdOutputs_20161130_loaded_OCD.zip` | 1 | 2017-01-15 | 2017-01-15 |

### `NEMDE` · `ROOT_AUX`

_18 pattern rows, 2445 files (snapshot), observed 1996-10-08 → 2026-04-13 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/` | `NEMDE_{year}_{d2}.zip` | `NEMDE_\d{4}_\d{2}\.zip` | `NEMDE_2009_07.zip` | 201 | 2017-02-06 | 2026-04-13 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `AUTORUN.INF` | `AUTORUN\.INF` | `AUTORUN.INF` | 201 | 2017-01-12 | 2026-04-13 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `Back.gif` | `Back\.gif` | `Back.gif` | 116 | 1999-05-23 | 2019-03-14 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 115 | 2017-02-07 | 2019-03-14 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `Thumbs.db` | `Thumbs\.db` | `Thumbs.db` | 1 | 2017-01-12 | 2017-01-12 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `background{d1}.gif` | `background\d{1}\.gif` | `background1.gif` | 13 | 2018-03-19 | 2019-03-14 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `disclaimer.htm` | `disclaimer\.htm` | `disclaimer.htm` | 116 | 2017-02-07 | 2019-03-14 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `file.gif` | `file\.gif` | `file.gif` | 116 | 1999-05-23 | 2019-03-14 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `nemlogo{d1}.gif` | `nemlogo\d{1}\.gif` | `nemlogo1.gif` | 232 | 2009-08-17 | 2019-03-14 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `readme.htm` | `readme\.htm` | `readme.htm` | 1 | 2017-02-07 | 2017-02-07 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/` | `shelexec.exe` | `shelexec\.exe` | `shelexec.exe` | 27 | 1996-10-08 | 2019-03-14 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/` | `Back.gif` | `Back\.gif` | `Back.gif` | 201 | 1999-05-23 | 2024-09-13 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 201 | 2017-02-07 | 2024-09-13 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/` | `Thumbs.db` | `Thumbs\.db` | `Thumbs.db` | 2 | 2017-01-12 | 2017-01-12 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/` | `background{d1}.gif` | `background\d{1}\.gif` | `background1.gif` | 98 | 1999-05-23 | 2024-09-13 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/` | `disclaimer.htm` | `disclaimer\.htm` | `disclaimer.htm` | 201 | 2017-02-07 | 2024-09-13 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/` | `file.gif` | `file\.gif` | `file.gif` | 201 | 1999-05-23 | 2024-09-13 |
| `ROOT_AUX` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/` | `nemlogo{d1}.gif` | `nemlogo\d{1}\.gif` | `nemlogo1.gif` | 402 | 2009-08-17 | 2024-09-13 |

### `NEMDE` · `Readme`

_2 pattern rows, 400 files (snapshot), observed 2017-02-06 → 2024-09-13 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `File_Readers` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/File_Readers/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 200 | 2017-02-06 | 2024-09-13 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `Readme.htm` | `Readme\.htm` | `Readme.htm` | 200 | 2017-02-06 | 2024-09-13 |

### `NEMDE` · `Readme (1)`

_2 pattern rows, 2 files (snapshot), observed 2017-01-15 → 2017-01-15 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `File_Readers` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/File_Readers/` | `Readme ({d1}).htm` | `Readme\ \(\d{1}\)\.htm` | `Readme (1).htm` | 1 | 2017-01-15 | 2017-01-15 |
| `NEMDE_Files` | `/Data_Archive/Wholesale_Electricity/NEMDE/{year}/NEMDE_{year}_{d2}/NEMDE_Market_Data/NEMDE_Files/` | `Readme ({d1}).htm` | `Readme\ \(\d{1}\)\.htm` | `Readme (1).htm` | 1 | 2017-01-15 | 2017-01-15 |

## Repo: `FCAS_Causer_Pays`  (1 dataset, 1 rows)

### `FCAS_Causer_Pays` · `CAUSER_PAYS`

_1 pattern row, 1 files (snapshot), observed 2026-02-11 → 2026-02-11 (snapshot)_

| Tier | Path template | Filename template | Regex | Sample | Files (snap) | First seen (snap) | Last seen (snap) |
|---|---|---|---|---|---:|---|---|
| `ANNUAL` | `/Data_Archive/Wholesale_Electricity/FCAS_Causer_Pays/{year}/` | `{year}.txt` | `\d{4}\.txt` | `2011.txt` | 1 | 2026-02-11 | 2026-02-11 |

## Appendix: directory-level anomalies

Directories observed on NEMWeb that exist and return HTTP 200 but contain zero files. These do not appear in the pattern rows above (no filenames to group), but they are real URLs under the `Reports` repo and must be called out for catalog completeness.

| URL path | Reason |
|---|---|
| `/Reports/ARCHIVE/NEXT_DAY_OFFER_ENERGY)SPARSE/` | aemo_url_typo (directory exists with no files) |

See `reference/NEMWEB-STRUCTURE.md` §3.2 for the canonical AEMO URL-typo finding and §3.1 for the related casing-mismatch anomalies (those DO appear in pattern rows above because their directories contain files).
