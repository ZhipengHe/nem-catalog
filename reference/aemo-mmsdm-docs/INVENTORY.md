# MMSDM DOCUMENTATION/ Capture Inventory

**Captured:** 2026-04-20 (local time AEST).

**Source:** `https://nemweb.com.au/Data_Archive/Wholesale_Electricity/MMSDM/{year}/MMSDM_{year}_{month}/MMSDM_Historical_Data_SQLLoader/DOCUMENTATION/`

**User agent:** `nem-catalog-recon/0.1 curl`

Per-version `DOCUMENTATION/MMS Data Model/v{X.Y}/` subtrees for every MMSDM schema version v4.26 through v5.6 (13 versions, including `v5.3_PreRelease`). Each version captured from the first month it appeared on the mirror.

**What's skipped:** DB-engine-specific GUI installer zips (`MMSDM_GUI_*.zip`) — 2+ MB each, Java/GUI client binary only. DB-engine-version-specific CLI zips (v5.0 had 4 variants: MSSQLServer2014/2017 + Oracle12c/19c) — redundant installer payloads. Kept: all PDFs, xlsx, .sql patches, .par files, pdrLoader config zips, `_create.zip` and `_upgrade.zip` DDL bundles, v5.1 generic CLI zips.

**Top-level shared files:**

- `INVENTORY.md` (7,682 bytes)
- `Participant_Monthly_DVD.pdf` (525,113 bytes)
- `README.txt` (2,586 bytes)

---

## Schema version timeline

| Version | First month | Last month | Months live | Release context |
|---|---|---|---:|---|
| **v4.26** | MMSDM_2016_09 | MMSDM_2017_10 | 14 | earliest walked — Nov 2016 Wholesale Systems Tech Spec release |
| **v4.27** | MMSDM_2017_11 | MMSDM_2018_11 | 13 | Oct–Dec 2017 EMMS release |
| **v4.28** | MMSDM_2018_12 | MMSDM_2019_08 | 9 | Jan 2019 |
| **v4.29** | MMSDM_2019_09 | MMSDM_2020_02 | 6 | Oct 2019 SRA release |
| **v4.30** | MMSDM_2020_03 | MMSDM_2021_02 | 12 | last v4.x — 5MS Reallocations tech spec |
| **v5.0** | MMSDM_2021_03 | MMSDM_2021_09 | 7 | 5-minute settlement design release (Oct 2020 FAQ) |
| **v5.1** | MMSDM_2021_10 | MMSDM_2023_04 | 18 | 5-minute settlement goes live (Oct 2021) — longest-running version |
| **v5.2** | MMSDM_2023_05 | MMSDM_2024_02 | 10 | May 2023 |
| **v5.3_PreRelease** | MMSDM_2024_02 | MMSDM_2024_09 | 8 | BidOffer table rename prep — transition scripts |
| **v5.3** | MMSDM_2024_03 | MMSDM_2024_09 | 7 | April 2024 — DVD→ARCHIVE filename cutover happens mid-lifecycle at 2024-08 |
| **v5.4** | MMSDM_2024_10 | MMSDM_2025_03 | 6 | November 2024 — doc-naming switches to "Electricity Data Model …" |
| **v5.5** | MMSDM_2025_04 | MMSDM_2025_10 | 7 | April 2025 — FPP (Frequency Performance Payments) Settlements |
| **v5.6** | MMSDM_2025_10 | MMSDM_2026_03 | 6 | November 2025 — SSM + ISF; GA 2025-11-19 |

Pre-2015 MMSDM months exist on AEMO but were not walked. v4.0 through v4.25 likely live there.

---

## Per-version file inventory

SHA256 truncated to first 16 chars.

### v4.26

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `Concise_Guide_to_Data_Interchange.pdf` | 2,114,757 | `f86349ddde91a83e` | Consumer guide (v4.26 only) |
| `Guide_to_Troubleshooting_Data_Interchange.pdf` | 2,355,363 | `9088c513a40e7252` | Troubleshooting guide (v4.26 only) |
| `Guide_to_Upgrading_a_Standard_Data_Interchange_Environment.pdf` | 1,830,598 | `1324a0a91d7ca1c4` | Upgrade guide (v4.26 only) |
| `Guide_to_setting_up_a_standard_Data_Interchange_environment.pdf` | 1,872,447 | `80055bce75f2d356` | Setup guide (v4.26 only) |
| `MMS_Data_Model_GUI_Installer_Guide.pdf` | 486,728 | `6f925ca796ec93e9` | GUI installer manual |
| `MMS_Data_Model_Installation_Note.pdf` | 524,313 | `182891e37155d0ed` | Install note |
| `MMS_Data_Model_Package_Summary.pdf` | 1,267,266 | `c5595fe94b93948c` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 11,645,516 | `69780d1482013d2d` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 532,406 | `b43725c40dff8476` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v4.26.zip` | 187,703 | `90b374c47e40dd5f` | PDR loader config bundle |
| `Table_File_Report_Relationships.xlsx` | 33,874 | `fc66f6f23416d039` | Cross-boundary mapping xlsx (MMSDM table ↔ Reports stream) |
| `Wholesale_Systems_Technical_Specification_-_November_2016.pdf` | 2,201,366 | `4643673f50471e1e` | EMMS technical spec |
| `table-file-report-mapping.csv` | 58,136 | `2979a86bd33240fe` | Cross-boundary mapping CSV (extracted from xlsx) |

### v4.27

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `Data_Model_Installation_Note.pdf` | 467,457 | `687110984c842a95` | Install note |
| `EMMS_Release_October_to_December_2017.zip` | 1,967,115 | `fdbc098042b62d87` | EMMS technical specification |
| `MMS_Data_Model_GUI_Installer_Guide.pdf` | 486,728 | `6f925ca796ec93e9` | GUI installer manual |
| `MMS_Data_Model_Package_Summary.pdf` | 1,362,891 | `d1103af668d51cf2` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 12,859,682 | `80eb5b4129d505a2` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 1,105,613 | `75d285b826103fd4` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_Production_v4.27.zip` | 187,926 | `a75f6e86cc94aa7b` | PDR loader config bundle |
| `Table_File_Report_Relationships.xlsx` | 35,189 | `6a903cd60591b1eb` | Cross-boundary mapping xlsx (MMSDM table ↔ Reports stream) |
| `table-file-report-mapping.csv` | 63,565 | `4cbe750fd6efaa1d` | Cross-boundary mapping CSV (extracted from xlsx) |

### v4.28

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_-_Release_FAQ_-_January_2019.pdf` | 568,364 | `0f99adde2bc1a4d9` | Participant-facing FAQ |
| `EMMS_Release_Schedule_and_Technical_Specification_-_Jan_2019_-_Data_Model_v4.28.pdf` | 1,553,238 | `c6c2989707dd0955` | Timeline + tech spec combined |
| `MMS_Data_Model_GUI_Installer_Guide.pdf` | 486,728 | `6f925ca796ec93e9` | GUI installer manual |
| `MMS_Data_Model_Package_Summary.pdf` | 932,926 | `23e5698d22ee9044` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 8,966,122 | `3c9317518c89eb33` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 912,265 | `ed99c93ca7ec6938` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_Production_v4.28.zip` | 189,174 | `13aa6c6c419f711e` | PDR loader config bundle |
| `Table_File_Report_Relationships.xlsx` | 37,237 | `23505fdc06fd1574` | Cross-boundary mapping xlsx (MMSDM table ↔ Reports stream) |
| `table-file-report-mapping.csv` | 65,167 | `4335975dc94e8dc8` | Cross-boundary mapping CSV (extracted from xlsx) |

### v4.29

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_-_Release_Schedule_and_Technical_Specification_-_SRA_-_October_2019.pdf` | 1,891,682 | `14838789f57b5785` | Timeline + tech spec combined |
| `MMS_Data_Model_GUI_Installer_Guide.pdf` | 486,728 | `6f925ca796ec93e9` | GUI installer manual |
| `MMS_Data_Model_Package_Summary.pdf` | 835,948 | `9f48159c680fd5b7` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 7,657,477 | `c5e090cad4b824eb` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 1,003,949 | `8d9c2eb2dbb1e34d` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v4.29.zip` | 190,306 | `3ebe3b715aa0ffa6` | PDR loader config bundle |
| `Table_File_Report_Relationships.xlsx` | 36,641 | `ce78a8db0aa3c747` | Cross-boundary mapping xlsx (MMSDM table ↔ Reports stream) |
| `table-file-report-mapping.csv` | 66,388 | `b7fd8c0f10276f01` | Cross-boundary mapping CSV (extracted from xlsx) |

### v4.30

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_Technical_Specification_5MS_Reallocations.pdf` | 1,831,488 | `43c8c4720f868b90` | EMMS technical specification |
| `MMS_Data_Model_GUI_Installer_Guide.pdf` | 486,728 | `6f925ca796ec93e9` | GUI installer manual |
| `MMS_Data_Model_Package_Summary.pdf` | 827,654 | `22c0754c46e37a32` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 7,684,963 | `76c5ba25c0619fc0` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 287,814 | `d7f4e8e54bb31f0e` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v4.30.zip` | 189,783 | `07a1f372ce330df8` | PDR loader config bundle |
| `Table_File_Report_Relationships.xlsx` | 36,641 | `043794b97f36eff5` | Cross-boundary mapping xlsx (MMSDM table ↔ Reports stream) |
| `table-file-report-mapping.csv` | 66,388 | `a4cf4ec7c3d9f924` | Cross-boundary mapping CSV (extracted from xlsx) |

### v5.0

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_Release_FAQ_-_October_2020_-_Data_Model_v5.00.pdf` | 1,002,641 | `735be5191555521f` | Participant-facing FAQ |
| `EMMS_Technical_Specification_-_5MS_-_Data_Model_v5.00.pdf` | 1,677,105 | `147a899a552929c4` | EMMS technical specification |
| `MMS_Data_Model_GUI_Installer_Guide.pdf` | 486,728 | `6f925ca796ec93e9` | GUI installer manual |
| `MMS_Data_Model_Package_Summary.pdf` | 865,853 | `1f396b9ee38feb59` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 7,589,410 | `656df47d6f2b8a20` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 935,699 | `432c469e9be9418c` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v5.0.zip` | 188,568 | `695e24682162f934` | PDR loader config bundle |
| `MMS_Data_Model_v5.0_Release_Notes.pdf` | 371,972 | `7279089cd6ff5b17` | Per-version release changelog |
| `MSSQLSERVER_PATCH_GENUNITS_UNIT.sql` | 809 | `f758ed3a2cfc4519` | Per-engine patch SQL for specific table |
| `MSSQLSERVER_PATCH_SETTLEMENTS.sql` | 1,802 | `635404deabf51d71` | Per-engine patch SQL for specific table |
| `ORACLE_PATCH_GENUNITS_UNIT.sql` | 797 | `67a4f0f2e31b855d` | Per-engine patch SQL for specific table |
| `ORACLE_PATCH_SETTLEMENTS.sql` | 802 | `d9725ad81d100902` | Per-engine patch SQL for specific table |
| `Table_File_Report_Relationships.xlsx` | 40,240 | `f2816c1daf1bc19a` | Cross-boundary mapping xlsx (MMSDM table ↔ Reports stream) |
| `table-file-report-mapping.csv` | 69,875 | `f94348e900ab6445` | Cross-boundary mapping CSV (extracted from xlsx) |

### v5.1

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_Release_Schedule_and_Technical_Specification_-_October_2021.pdf` | 1,323,904 | `e105809a162cdc3d` | Timeline + tech spec combined |
| `MMSDM_CLI_MSSQLServer_v5.1.zip` | 120,024 | `90aca12a0615e2d6` | CLI installer bundle (DDL + loader config) |
| `MMSDM_CLI_Oracle_v5.1.zip` | 354,748 | `d70d6d0eb31373a5` | CLI installer bundle (DDL + loader config) |
| `MMS_Data_Model_Package_Summary.pdf` | 866,275 | `c3fe556d23128f61` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Release_Notes_v5.1.pdf` | 387,896 | `f2ea87b093915b19` | Per-version release changelog |
| `MMS_Data_Model_Report.pdf` | 7,955,843 | `83d292da82cc1f9f` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 1,363,855 | `2b4e5f5aaf8cf0c2` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v5.1.zip` | 188,688 | `7c32882e5c3a736b` | PDR loader config bundle |
| `Table_File_Report_Relationships.xlsx` | 40,478 | `043504e82d596e6e` | Cross-boundary mapping xlsx (MMSDM table ↔ Reports stream) |
| `table-file-report-mapping.csv` | 70,099 | `69dec0a6364d56a4` | Cross-boundary mapping CSV (extracted from xlsx) |

### v5.2

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_-_Technical_Specification_-_Data_Model_v5.2_-_May_2023.pdf` | 1,607,191 | `ffea7dd9cd315f86` | EMMS technical specification |
| `EMMS_-_Technical_Specification_-_Data_Model_v5.2_-_May_2023_comparison.pdf` | 1,683,634 | `bb2c5fa928e838d9` | EMMS technical specification |
| `MMSDM_create_v5.2.zip` | 531,697 | `be6638157cb931f6` | DDL to create fresh schema |
| `MMSDM_upgrade_v5.2.zip` | 11,422 | `f89f591dfb3ac83f` | DDL to upgrade from prior version |
| `MMS_Data_Model_Package_Summary.pdf` | 807,074 | `d4ccf8a4124c9bfc` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 7,907,920 | `d32202ec45bcf43c` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 1,592,280 | `017270760cddb806` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v5.2.zip` | 190,273 | `891fd98872db0855` | PDR loader config bundle |

### v5.3_PreRelease

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_-_Technical_Specification_Data_Model_v5.3_-_April_2024.pdf` | 1,808,936 | `a8256a0416cb0b99` | EMMS technical specification |
| `MMSDM_Bidoffer_Transition.zip` | 183,265 | `8cec9f6cf68d6be2` | BidOffer migration transition bundle (v5.3_PreRelease) |
| `MMSDM_Switch_Bidoffer_Table_Names_v1.1.zip` | 11,111 | `783766a5afd3e65b` | BIDPEROFFER → BIDOFFERPERIOD rename SQL (v5.3_PreRelease) |
| `MMSDM_upgrade_v5.3_PRE.zip` | 8,608 | `e05a8579ef5b59de` | DDL to upgrade from prior version |
| `MMS_Data_Model_pdrLoader_Configuration_Production_v5.3_PreRelease.zip` | 655 | `a12101dc2537bf39` | PDR loader config bundle |
| `MMS_Data_Model_v5.3_PreRelease_Release_Notes.pdf` | 467,287 | `ab6e438f59947088` | Per-version release changelog |

### v5.3

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_Technical_Specification_-_Data_Model_v5.3_-_April_2024.pdf` | 2,011,745 | `a570ad1f08a9ed57` | EMMS technical specification |
| `EMMS_Technical_Specification_-_Data_Model_v5.3_-_April_2024_markedup.pdf` | 2,062,704 | `89958c12a4bad4ce` | EMMS technical specification |
| `MMSDM_create_v5.3.zip` | 561,609 | `997e0f0c42c7efba` | DDL to create fresh schema |
| `MMSDM_upgrade_v5.3.zip` | 22,711 | `04b6aab0613477c7` | DDL to upgrade from prior version |
| `MMS_Data_Model_Package_Summary.pdf` | 903,588 | `888c36240c820dc0` | Package → table hierarchy, ER diagrams |
| `MMS_Data_Model_Report.pdf` | 8,543,889 | `2f3b7be44f7d0376` | Full table-by-table schema with columns, types, PKs |
| `MMS_Data_Model_Upgrade_Report.pdf` | 1,831,861 | `81f310aea4afbf8c` | Per-table schema diff vs prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v5.3.zip` | 190,213 | `3db9f985b115bbb6` | PDR loader config bundle |
| `MMS_Data_Model_v5.3_Release_Notes.pdf` | 329,156 | `3ced8ffdb9d56216` | Per-version release changelog |

### v5.4

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_-_Technical_Specification_-_Data_Model_v5.4_-_November_2024.pdf` | 1,099,822 | `c395dd37570c8999` | EMMS technical specification |
| `Electricity_Data_Model_Package_Summary.pdf` | 995,824 | `ea60a778368f3757` | Package → table hierarchy, ER diagrams |
| `Electricity_Data_Model_Report.pdf` | 9,166,465 | `5439cb756ef18571` | Full table-by-table schema with columns, types, PKs |
| `Electricity_Data_Model_Upgrade_Report.pdf` | 919,953 | `469fa31dd70125e1` | Per-table schema diff vs prior version |
| `MMSDM_create_v5.4.zip` | 764,106 | `5a69566638d107e4` | DDL to create fresh schema |
| `MMSDM_upgrade_v5.4.zip` | 13,888 | `78b846e3803a43b3` | DDL to upgrade from prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v5.4.zip` | 14,426 | `0cb106d08721ef19` | PDR loader config bundle |

### v5.5

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_DMv5.5_Apr25.pdf` | 1,388,276 | `08777ef1e773b120` | EMMS technical specification |
| `Electricity_Data_Model_Package_Summary.pdf` | 926,900 | `0b32b0988dba78cd` | Package → table hierarchy, ER diagrams |
| `Electricity_Data_Model_Report.pdf` | 9,471,671 | `100d27ffef8a92a6` | Full table-by-table schema with columns, types, PKs |
| `Electricity_Data_Model_Upgrade_Report.pdf` | 1,940,137 | `90aa0d3e4c83eeb9` | Per-table schema diff vs prior version |
| `MMSDM_create_v5.5.zip` | 826,976 | `48e02599a397d62a` | DDL to create fresh schema |
| `MMSDM_upgrade_v5.5.zip` | 16,038 | `f51207e5bcc72e96` | DDL to upgrade from prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v5.5.zip` | 15,423 | `b917e88b0068a6f5` | PDR loader config bundle |

### v5.6

| File | Size (B) | SHA256 (16) | Purpose |
|---|---:|---|---|
| `EMMS_DM5.6_Nov2025.pdf` | 1,323,213 | `31c5cebabf770270` | EMMS technical specification |
| `Electricity_Data_Model_Package_Summary.pdf` | 1,001,754 | `423a5ad51de8c998` | Package → table hierarchy, ER diagrams |
| `Electricity_Data_Model_Report.pdf` | 9,263,247 | `84f7485c3c24e0ce` | Full table-by-table schema with columns, types, PKs |
| `Electricity_Data_Model_Upgrade_Report.pdf` | 1,488,976 | `7c921d8bdaf00244` | Per-table schema diff vs prior version |
| `MMSDM_create_v5.6.zip` | 824,058 | `8eecb9b682da4b48` | DDL to create fresh schema |
| `MMSDM_upgrade_5.6.zip` | 19,300 | `f9f260718af90ec2` | DDL to upgrade from prior version |
| `MMS_Data_Model_pdrLoader_Configuration_production_v5.6.zip` | 15,231 | `d752ab3e2c9163d7` | PDR loader config bundle |

---

## Cross-boundary Table↔File↔Report mapping (Rosetta Stone for Reports ↔ MMSDM identity)

AEMO shipped `MMS Data Model Table to File to Report Relationships.xlsx` in every version v4.26 through v5.1, then stopped. Each xlsx maps MMSDM table → Reports/ PDR stream → filename template → transaction type. **This is AEMO's own cross-repo cross-reference — satisfies NEMWEB-STRUCTURE.md §4 proof rule #3** ("AEMO's own internal cross-reference").

Captured xlsx files have also been extracted to CSV for direct query:

| Version | Mapping rows | CSV path |
|---|---:|---|
| v4.26 | 336 | `reference/aemo-mmsdm-docs/v4.26/table-file-report-mapping.csv` |
| v4.27 | 365 | `reference/aemo-mmsdm-docs/v4.27/table-file-report-mapping.csv` |
| v4.28 | 374 | `reference/aemo-mmsdm-docs/v4.28/table-file-report-mapping.csv` |
| v4.29 | 380 | `reference/aemo-mmsdm-docs/v4.29/table-file-report-mapping.csv` |
| v4.30 | 380 | `reference/aemo-mmsdm-docs/v4.30/table-file-report-mapping.csv` |
| v5.0 | 392 | `reference/aemo-mmsdm-docs/v5.0/table-file-report-mapping.csv` |
| v5.1 | 392 | `reference/aemo-mmsdm-docs/v5.1/table-file-report-mapping.csv` |

**Not published by AEMO for v5.2 onwards** — the xlsx is absent from v5.2, v5.3, v5.4, v5.5, v5.6 version folders. For post-v5.1 schema additions (FPP_*, SSM_*, AREA, REGION_AREA, etc.) the cross-boundary mapping must be reconstructed via column-schema match (§4 rule 2).

---

## Notable version-specific artifacts

### v4.26 — consumer-manual bundle

Unique to v4.26: 4 user-facing Data Interchange guides (Concise Guide, Setup, Troubleshooting, Upgrading) + Wholesale Systems Technical Specification (Nov 2016). Other versions replaced these with a single "EMMS Technical Specification" style PDF.

### v5.0 — 5-Minute Settlement design drop

`EMMS_Technical_Specification_-_5MS_-_Data_Model_v5.00.pdf` (1.7 MB) + `EMMS_Release_FAQ_-_October_2020_-_Data_Model_v5.00.pdf` + per-engine patch SQLs (GENUNITS_UNIT, SETTLEMENTS on both MSSQLServer and Oracle). The 5MS-era schema introduction.

### v5.3_PreRelease — BidOffer table-rename prep

Unique artifacts that directly support the BIDPEROFFER → BIDOFFERPERIOD rename hypothesis in `MMSDM-TABLE-LIFECYCLE.md` §6:
- `MMSDM_Switch_Bidoffer_Table_Names_v1.1.zip` (11 KB) — table-rename SQL
- `MMSDM_Bidoffer_Transition.zip` (183 KB) — transition scripts / data

These are the pre-shipped migration artifacts AEMO provided ahead of the 2024-08 cutover. Promotes the BIDPEROFFER{1,2} → BIDOFFERPERIOD lifecycle-analysis hypothesis from HIGH confidence to AEMO-CONFIRMED.

### v5.4 — doc naming convention change

v5.4 renamed `MMS Data Model …` PDFs → `Electricity Data Model …`. Aligns with AEMO adding a separate Gas Data Model product. Our captures preserve both naming families so downstream code can handle either.

### v5.5 — FPP (Frequency Performance Payments) Settlements

`EMMS_DMv5.5_Apr25.pdf` (1.4 MB) — FPP settlement subsystem introduction. Context for the 17 `FPP_*` tables appearing in `MMSDM_2024_12` per `MMSDM-TABLE-LIFECYCLE.md` §4.3 — FPP tables shipped in v5.4 groundwork but EMMS spec formalizes them in v5.5.

### v5.6 — SSM (System Security Mechanism) + ISF

`EMMS_DM5.6_Nov2025.pdf` (1.3 MB) — introduces the SYSTEM_SECURITY_MANAGEMENT package (6 new tables: SSM_*). GA 2025-11-19. Matches SSM table observations in `MMSDM-TABLE-LIFECYCLE.md`.

---

## Not captured (available if needed)

- DB-engine-specific installer payloads (MSSQLServer2014/2017/2019, Oracle11g/12c/19c variants, GUI installers) — deliberately skipped. Available in the source URLs.
- Pre-2015 MMSDM months — not walked. v4.0 through v4.25 upgrade reports presumably live there.
- `Reports/CURRENT/MMSDataModelReport/Electricity/` HTM tree — live-served 160+ HTM files for the current data model (redundant with `v5.6/Electricity_Data_Model_Report.pdf` we already have).