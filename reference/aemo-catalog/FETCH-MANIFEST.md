# AEMO Visualisations Catalog Capture

**Purpose.** Frozen local mirror of AEMO's authoritative machine-readable NEMWEB
catalog — master dataset list, per-dataset URL manifests, and per-dataset field
definitions. Used as the ground-truth spec for the v0.1.2+ mirror-structure
reconnaissance (diff this against empirical mirror walks to surface undocumented
directories, DUPLICATE subtrees, and schema drift).

**Do not hand-edit.** This directory is byte-preserved source-of-truth, equivalent
in role to `reference/URL-CONVENTIONS.md`. If you add this directory under a
formatter or linter, also add it to the pre-commit global-exclude list (see
`feedback_protect_source_of_truth` in memory).

---

## Capture metadata

| Field | Value |
|---|---|
| Captured (UTC) | `2026-04-20T09:41:49Z` |
| Captured (local) | `2026-04-20 19:41:49 AEST` |
| Base URL | `https://visualisations.aemo.com.au/aemo/nemweb/` |
| User-Agent | `nem-catalog-recon/0.1 (+https://github.com/ZhipengHe/nem-catalog) curl` |
| Total files | 198 (1 master + 97 manifests + 97 definitions + 3 SPA source) |
| Total bytes | 2125824 |
| HTTP status distribution | 194/194 manifests+definitions returned 200; 4/4 SPA source returned 200 |

## AEMO regen window

AEMO's own `generatedAt` timestamps (embedded in each manifest) show the catalog
was regenerated in a ~4-minute sweep:

- **Earliest:** `Tue Apr 14 15:09:29 AEST 2026`
- **Latest:**   `Tue Apr 14 15:13:07 AEST 2026`
- **Unique timestamps:** 97 (one per manifest)

This suggests AEMO runs a daily / weekly catalog regeneration job. Re-capturing
this directory more than ~weekly is probably wasted work.

## Master catalog structure

15 top-level `!dataset` groups containing 97 `!file` entries:

| Group | Direct files | Submenu files |
|---|---:|---:|
| Bids | 3 | 0 |
| Data Model | 3 | 0 |
| Demand and Forecasts | 0 | 19 |
| Dispatch | 9 | 0 |
| FPP | 7 | 0 |
| Gas Supply Hub | 13 | 0 |
| NEMDE | 1 | 0 |
| Network | 3 | 0 |
| Other | 4 | 0 |
| PASA | 9 | 0 |
| Pre-Dispatch | 7 | 0 |
| Prices | 7 | 0 |
| Settlement Residues | 7 | 0 |
| Settlements | 3 | 0 |
| Trading | 2 | 0 |
| **Total** | **78** | **19** |

Sum: 97 datasets.

## Directory layout

```
reference/aemo-catalog/
├── FETCH-MANIFEST.md              # this file
├── dataset-list.yaml              # master catalog (97 datasets, 15 groups)
├── source/                        # SPA origin (provenance)
│   ├── index.html
│   ├── index_page.js
│   └── helpers.js
├── datasets/                      # 97 field-schema YAMLs (!field entries with DB types)
│   └── <slug>-definition.yaml
└── manifests/                     # 97 URL manifests (!Source entries with CURRENT/ARCHIVE URLs)
    └── <slug>.yaml
```

## File inventory (HTTP status / size in bytes / SHA256)

| HTTP | Size (B) | SHA256 | Path |
|---:|---:|---|---|
| 200 | 27343 | `300342e25d942240...` | `dataset-list.yaml` |
| 200 | 16436 | `d76a0cb734857ce2...` | `datasets/adjusted-prices-reports-definition.yaml` |
| 200 | 785 | `e473351843ef5775...` | `datasets/alt-limits-definition.yaml` |
| 200 | 1842 | `9542402f2c5d8cb6...` | `datasets/ancillary-services-payments-definition.yaml` |
| 200 | 8652 | `c5a94b398b6ae1dd...` | `datasets/bidmove-complete-definition.yaml` |
| 200 | 17233 | `e12de4935359a888...` | `datasets/billing-definition.yaml` |
| 200 | 125 | `f75170973d1bfae9...` | `datasets/causer-pays-scada-definition.yaml` |
| 200 | 50782 | `d75d571c7a88dafb...` | `datasets/daily-reports-definition.yaml` |
| 200 | 649 | `24de68517d5c5d49...` | `datasets/dailyocd-definition.yaml` |
| 200 | 570 | `aa2a2242c403a09f...` | `datasets/dispatch-irsr-definition.yaml` |
| 200 | 2417 | `d469d67d6f222c50...` | `datasets/dispatch-negative-residue-definition.yaml` |
| 200 | 24351 | `5f847ed6f0a51f12...` | `datasets/dispatch-reports-definition.yaml` |
| 200 | 976 | `ce5732f311735d33...` | `datasets/dispatch-scada-definition.yaml` |
| 200 | 4736 | `62899eb46b6c00f5...` | `datasets/dispatchfcst-definition.yaml` |
| 200 | 14711 | `5d1b92e2f0dcd124...` | `datasets/dispatchis-price-revisions-definition.yaml` |
| 200 | 43677 | `a9d889f1dbb45e8b...` | `datasets/dispatchis-reports-definition.yaml` |
| 200 | 1552 | `298c895ae7e63ff7...` | `datasets/dispatchprices-pre-ap-definition.yaml` |
| 200 | 11600 | `b20e30b359089d1b...` | `datasets/fpp-definition.yaml` |
| 200 | 4719 | `f68a3d980aac4bd7...` | `datasets/fpp-hist-reg-perf-definition.yaml` |
| 200 | 8087 | `b7ab1d5e1fe607d4...` | `datasets/fppdaily-definition.yaml` |
| 200 | 9981 | `7c6669446027b2ae...` | `datasets/fpprates-definition.yaml` |
| 200 | 15509 | `8983a89558646f52...` | `datasets/fpprun-definition.yaml` |
| 200 | 641 | `eb6cce040c2f1f68...` | `datasets/gsh-benchmark-price-definition.yaml` |
| 200 | 1758 | `2e1e9c7645721253...` | `datasets/gsh-gsh-auction-curtailment-notice-definition.yaml` |
| 200 | 2080 | `f232ecf18b91f8be...` | `datasets/gsh-gsh-auction-price-volume-definition.yaml` |
| 200 | 2191 | `711c979010dd38b3...` | `datasets/gsh-gsh-auction-quantities-definition.yaml` |
| 200 | 4651 | `6893ad115608d38e...` | `datasets/gsh-gsh-capacity-transaction-definition.yaml` |
| 200 | 1622 | `863d7fbe4b8da281...` | `datasets/gsh-gsh-capacity-transfer-auction-notice-definition.yaml` |
| 200 | 2356 | `ab6263cc3d627964...` | `datasets/gsh-gsh-daily-trans-summary-definition.yaml` |
| 200 | 1593 | `31efe636e35f8dd5...` | `datasets/gsh-gsh-historical-trans-summary-definition.yaml` |
| 200 | 3844 | `24fbaf3eeeac3140...` | `datasets/gsh-gsh-participants-definition.yaml` |
| 200 | 1496 | `792378ca7acac9bb...` | `datasets/gsh-gsh-registered-facilities-definition.yaml` |
| 200 | 8963 | `0a54c2f3b2a31721...` | `datasets/gsh-gsh-registered-service-points-definition.yaml` |
| 200 | 1939 | `36ca37ebcbdd5bff...` | `datasets/gsh-gsh-revised-auction-quantities-definition.yaml` |
| 200 | 1975 | `a479a68f85e29676...` | `datasets/gsh-gsh-zone-curtailment-information-definition.yaml` |
| 200 | 570 | `be3ea916ada8f47b...` | `datasets/ibei-definition.yaml` |
| 200 | 812 | `751253af914c1ce5...` | `datasets/marginal-loss-factors-definition.yaml` |
| 200 | 1328 | `ec7c560257e86400...` | `datasets/mccdispatch-definition.yaml` |
| 200 | 22656 | `43cc88262b4b3824...` | `datasets/medium-term-pasa-reports-definition.yaml` |
| 200 | 3733 | `03c569903f84fd3f...` | `datasets/mktsusp-pricing-definition.yaml` |
| 200 | 1955 | `3c9f76c33cbcceac...` | `datasets/mms-data-model-definition.yaml` |
| 200 | 112 | `7613e230fec6599c...` | `datasets/mmsdatamodelreport-electricity-definition.yaml` |
| 200 | 88 | `68bdb0822ffb8aa4...` | `datasets/mmsdatamodelreport-gas-definition.yaml` |
| 200 | 1814 | `252c3bac43c79529...` | `datasets/mtpasa-duidavailability-definition.yaml` |
| 200 | 4214 | `aa9d99b837b8a319...` | `datasets/mtpasa-regionavailability-definition.yaml` |
| 200 | 1943 | `d1ee733cac57ead7...` | `datasets/nemde-definition.yaml` |
| 200 | 4282 | `f350d27e20f2f1f1...` | `datasets/network-definition.yaml` |
| 200 | 549 | `93a02d5668ae0d50...` | `datasets/next-day-actual-gen-definition.yaml` |
| 200 | 2860 | `4e1dbdf7ce58edad...` | `datasets/next-day-avail-submiss-cluster-definition.yaml` |
| 200 | 2479 | `fc0e31f13b63d730...` | `datasets/next-day-avail-submiss-day-definition.yaml` |
| 200 | 15717 | `bdf63ccedd54c51a...` | `datasets/next-day-dispatch-definition.yaml` |
| 200 | 5266 | `85d8586bd17142e7...` | `datasets/next-day-intermittent-ds-definition.yaml` |
| 200 | 1598 | `2ccc63f3cc3c1787...` | `datasets/next-day-intermittent-gen-scada-definition.yaml` |
| 200 | 1384 | `649779ff5e1f60de...` | `datasets/next-day-mccdispatch-definition.yaml` |
| 200 | 16052 | `8c91bd239a9e67be...` | `datasets/next-day-offer-energy-sparse-definition.yaml` |
| 200 | 9315 | `d1668d8a514e8baa...` | `datasets/next-day-offer-fcas-sparse-definition.yaml` |
| 200 | 11751 | `bb95634672a18016...` | `datasets/next-day-predispatch-definition.yaml` |
| 200 | 16813 | `6f1412c1b82e18bc...` | `datasets/next-day-predispatchd-definition.yaml` |
| 200 | 2593 | `519286b55f972828...` | `datasets/next-day-trading-definition.yaml` |
| 200 | 758 | `f424f9b6efa7ab0c...` | `datasets/operational-demand-actual-daily-area-definition.yaml` |
| 200 | 680 | `9cac5b86f4138a13...` | `datasets/operational-demand-actual-daily-definition.yaml` |
| 200 | 731 | `012ecb627eb93245...` | `datasets/operational-demand-actual-hh-area-definition.yaml` |
| 200 | 1339 | `c1f99e400be43e21...` | `datasets/operational-demand-actual-hh-definition.yaml` |
| 200 | 257 | `62012fff36b87ff3...` | `datasets/operational-demand-actual-update-area-definition.yaml` |
| 200 | 1337 | `c3eae4987e4073d4...` | `datasets/operational-demand-actual-update-definition.yaml` |
| 200 | 812 | `921df38d095b1fc9...` | `datasets/operational-demand-forecast-hh-area-definition.yaml` |
| 200 | 1329 | `410f0e7fbbcfb3d1...` | `datasets/operational-demand-forecast-hh-definition.yaml` |
| 200 | 768 | `1acf8e8a4452ab05...` | `datasets/operational-demand-less-snsg-actual-daily-definition.yaml` |
| 200 | 779 | `239649936fabb061...` | `datasets/operational-demand-less-snsg-actual-hh-definition.yaml` |
| 200 | 777 | `a9bfcf313319567a...` | `datasets/operational-demand-less-snsg-actual-update-definition.yaml` |
| 200 | 30559 | `50a1bbe146fffc6f...` | `datasets/p5-reports-definition.yaml` |
| 200 | 4902 | `3518b74a63311fe2...` | `datasets/p5minfcst-definition.yaml` |
| 200 | 9771 | `a5c1352522e99630...` | `datasets/pd7day-definition.yaml` |
| 200 | 18636 | `341885ee1cf7a37a...` | `datasets/pdpasa-definition.yaml` |
| 200 | 2247 | `4847f9e521732c46...` | `datasets/pdpasa-duidavailability-definition.yaml` |
| 200 | 656 | `3f4a4cbcd6cd1ef0...` | `datasets/predispatch-irsr-definition.yaml` |
| 200 | 18515 | `baca41107cf46c39...` | `datasets/predispatch-reports-definition.yaml` |
| 200 | 13902 | `49387d34c8c692ad...` | `datasets/predispatch-sensitivities-definition.yaml` |
| 200 | 5338 | `a06a9132ea94654f...` | `datasets/predispatchfcst-definition.yaml` |
| 200 | 36948 | `7be7870a835969c6...` | `datasets/predispatchis-reports-definition.yaml` |
| 200 | 40606 | `da76ccbff14d3b5c...` | `datasets/public-prices-definition.yaml` |
| 200 | 671 | `b6585b7e1b38915d...` | `datasets/rooftop-pv-actual-area-definition.yaml` |
| 200 | 1444 | `0f4a6f73e2720c41...` | `datasets/rooftop-pv-actual-definition.yaml` |
| 200 | 779 | `1b903a0f20b76e8b...` | `datasets/rooftop-pv-forecast-area-definition.yaml` |
| 200 | 1506 | `13cc85fa0a4fa606...` | `datasets/rooftop-pv-forecast-definition.yaml` |
| 200 | 23952 | `2ffb4829ed1df805...` | `datasets/settlements-definition.yaml` |
| 200 | 828 | `f2376ed3cec5acb2...` | `datasets/sevendayoutlook-full-definition.yaml` |
| 200 | 599 | `cf56f4dc71bde01e...` | `datasets/sevendayoutlook-peak-definition.yaml` |
| 200 | 19431 | `0610e6b5ebdde463...` | `datasets/short-term-pasa-reports-definition.yaml` |
| 200 | 726 | `2779479a40481fed...` | `datasets/sra-bids-definition.yaml` |
| 200 | 1967 | `6fe069e059102117...` | `datasets/sra-nsr-reconciliation-definition.yaml` |
| 200 | 689 | `5bd996dfe962eca4...` | `datasets/sra-offers-definition.yaml` |
| 200 | 2237 | `052dc0d1014713dd...` | `datasets/stpasa-duidavailability-definition.yaml` |
| 200 | 1291 | `2b71008ad12511da...` | `datasets/trading-cumulative-price-definition.yaml` |
| 200 | 573 | `db94eb24e7e4a317...` | `datasets/trading-irsr-definition.yaml` |
| 200 | 19224 | `421327437241d15e...` | `datasets/tradingis-reports-definition.yaml` |
| 200 | 2062 | `f51ec1c1b9d03152...` | `datasets/vwa-fcas-prices-definition.yaml` |
| 200 | 550 | `f1c70a6a4e0bea5e...` | `datasets/wdr-capacity-no-scada-definition.yaml` |
| 200 | 288 | `938d5ae9a0ea6f46...` | `manifests/adjusted-prices-reports.yaml` |
| 200 | 131 | `dfbf5ea82a224706...` | `manifests/alt-limits.yaml` |
| 200 | 148 | `c31c91728c1ba19a...` | `manifests/ancillary-services-payments.yaml` |
| 200 | 274 | `ac819ff6ea43dd8e...` | `manifests/bidmove-complete.yaml` |
| 200 | 256 | `b7282ddbae36ec17...` | `manifests/billing.yaml` |
| 200 | 276 | `127ad78bdb329e30...` | `manifests/causer-pays-scada.yaml` |
| 200 | 268 | `d622d11f12001dec...` | `manifests/daily-reports.yaml` |
| 200 | 258 | `1bfa77b4eb140ce1...` | `manifests/dailyocd.yaml` |
| 200 | 268 | `da20a310212989f9...` | `manifests/dispatch-irsr.yaml` |
| 200 | 292 | `99daecdae9563978...` | `manifests/dispatch-negative-residue.yaml` |
| 200 | 274 | `b29becad72d6324e...` | `manifests/dispatch-reports.yaml` |
| 200 | 270 | `03463f0b12075703...` | `manifests/dispatch-scada.yaml` |
| 200 | 266 | `640c6d50065f810f...` | `manifests/dispatchfcst.yaml` |
| 200 | 147 | `0a4b330ee6d954b0...` | `manifests/dispatchis-price-revisions.yaml` |
| 200 | 278 | `2d0b67766614f740...` | `manifests/dispatchis-reports.yaml` |
| 200 | 284 | `83715f225ab54577...` | `manifests/dispatchprices-pre-ap.yaml` |
| 200 | 138 | `d48f23ccf484cf75...` | `manifests/fpp-hist-reg-perf.yaml` |
| 200 | 124 | `e277144a27b63612...` | `manifests/fpp.yaml` |
| 200 | 258 | `33b0fb6b79cd3983...` | `manifests/fppdaily.yaml` |
| 200 | 258 | `6429bb93efb4982c...` | `manifests/fpprates.yaml` |
| 200 | 254 | `3145859ebcc66317...` | `manifests/fpprun.yaml` |
| 200 | 280 | `84b5b12392b7860d...` | `manifests/gsh-benchmark-price.yaml` |
| 200 | 310 | `e93d35ab31d0d3d6...` | `manifests/gsh-gsh-auction-curtailment-notice.yaml` |
| 200 | 298 | `11b249278980f8cc...` | `manifests/gsh-gsh-auction-price-volume.yaml` |
| 200 | 294 | `ec5579544dd43c62...` | `manifests/gsh-gsh-auction-quantities.yaml` |
| 200 | 298 | `e8ae1ea7b0be71f1...` | `manifests/gsh-gsh-capacity-transaction.yaml` |
| 200 | 322 | `e77f05d5fef3df33...` | `manifests/gsh-gsh-capacity-transfer-auction-notice.yaml` |
| 200 | 296 | `8ea1c84067af79c0...` | `manifests/gsh-gsh-daily-trans-summary.yaml` |
| 200 | 306 | `0ef28147727b16e2...` | `manifests/gsh-gsh-historical-trans-summary.yaml` |
| 200 | 282 | `3e8eb95b7105866c...` | `manifests/gsh-gsh-participants.yaml` |
| 200 | 300 | `2334fdaf5a6d6458...` | `manifests/gsh-gsh-registered-facilities.yaml` |
| 200 | 308 | `d19587083ee76f71...` | `manifests/gsh-gsh-registered-service-points.yaml` |
| 200 | 310 | `a17c8bf650dfb71e...` | `manifests/gsh-gsh-revised-auction-quantities.yaml` |
| 200 | 314 | `5f80fa7d7c55e4a5...` | `manifests/gsh-gsh-zone-curtailment-information.yaml` |
| 200 | 125 | `c9ef66daa1d2f605...` | `manifests/ibei.yaml` |
| 200 | 142 | `6366b5fd01d44b1d...` | `manifests/marginal-loss-factors.yaml` |
| 200 | 264 | `0543adbd0a50373e...` | `manifests/mccdispatch.yaml` |
| 200 | 290 | `960795148baf8e45...` | `manifests/medium-term-pasa-reports.yaml` |
| 200 | 136 | `e6ab92054541800f...` | `manifests/mktsusp-pricing.yaml` |
| 200 | 41580 | `fe76ae37607ac99c...` | `manifests/mms-data-model.yaml` |
| 200 | 190 | `b43c865e5243f539...` | `manifests/mmsdatamodelreport-electricity.yaml` |
| 200 | 174 | `9790e967a25a309c...` | `manifests/mmsdatamodelreport-gas.yaml` |
| 200 | 288 | `a13e8268f11c85dc...` | `manifests/mtpasa-duidavailability.yaml` |
| 200 | 292 | `23a30139e0abb530...` | `manifests/mtpasa-regionavailability.yaml` |
| 200 | 60501 | `650c92ab1989b57c...` | `manifests/nemde.yaml` |
| 200 | 256 | `66db161d545ffa32...` | `manifests/network.yaml` |
| 200 | 280 | `3eddc8af10fc2bf7...` | `manifests/next-day-actual-gen.yaml` |
| 200 | 302 | `20f22a2e10b9fd70...` | `manifests/next-day-avail-submiss-cluster.yaml` |
| 200 | 294 | `9d7d79cdb6f051da...` | `manifests/next-day-avail-submiss-day.yaml` |
| 200 | 276 | `1def65dadaccffcc...` | `manifests/next-day-dispatch.yaml` |
| 200 | 290 | `c97a4ab98cac913d...` | `manifests/next-day-intermittent-ds.yaml` |
| 200 | 304 | `17696b78ddb5cab1...` | `manifests/next-day-intermittent-gen-scada.yaml` |
| 200 | 282 | `2cc1e5d66e6a3bac...` | `manifests/next-day-mccdispatch.yaml` |
| 200 | 298 | `3166f07a3e6af1ea...` | `manifests/next-day-offer-energy-sparse.yaml` |
| 200 | 294 | `6cbe8e0c7b068d83...` | `manifests/next-day-offer-fcas-sparse.yaml` |
| 200 | 282 | `bb7ec4561d988bef...` | `manifests/next-day-predispatch.yaml` |
| 200 | 284 | `6077d9d3f7f58747...` | `manifests/next-day-predispatchd.yaml` |
| 200 | 274 | `00fe537ca6a9b437...` | `manifests/next-day-trading.yaml` |
| 200 | 314 | `7c30834243e7a723...` | `manifests/operational-demand-actual-daily-area.yaml` |
| 200 | 304 | `78f14a8ad94b286e...` | `manifests/operational-demand-actual-daily.yaml` |
| 200 | 308 | `5a3371566f01d780...` | `manifests/operational-demand-actual-hh-area.yaml` |
| 200 | 298 | `16931bbc58bd30ea...` | `manifests/operational-demand-actual-hh.yaml` |
| 200 | 158 | `bfeb9c3b4994038d...` | `manifests/operational-demand-actual-update-area.yaml` |
| 200 | 153 | `768dc2c7ba0b8b04...` | `manifests/operational-demand-actual-update.yaml` |
| 200 | 312 | `1201ca763a9bc4d6...` | `manifests/operational-demand-forecast-hh-area.yaml` |
| 200 | 302 | `19d7a146b5c0a558...` | `manifests/operational-demand-forecast-hh.yaml` |
| 200 | 324 | `f79223541013c1ba...` | `manifests/operational-demand-less-snsg-actual-daily.yaml` |
| 200 | 318 | `4a18bfdc3afddea3...` | `manifests/operational-demand-less-snsg-actual-hh.yaml` |
| 200 | 163 | `e4bfe479906dfbb7...` | `manifests/operational-demand-less-snsg-actual-update.yaml` |
| 200 | 262 | `63a2c4cabb87d954...` | `manifests/p5-reports.yaml` |
| 200 | 260 | `2a4ffc0e6adca549...` | `manifests/p5minfcst.yaml` |
| 200 | 127 | `99c71d195c6c8f9b...` | `manifests/pd7day.yaml` |
| 200 | 288 | `c16129e654e03cf3...` | `manifests/pdpasa-duidavailability.yaml` |
| 200 | 254 | `7505511dfd0c712d...` | `manifests/pdpasa.yaml` |
| 200 | 274 | `78eff7aea9b57ce1...` | `manifests/predispatch-irsr.yaml` |
| 200 | 280 | `5f796d468c3a97d9...` | `manifests/predispatch-reports.yaml` |
| 200 | 292 | `1e00be03e89b2807...` | `manifests/predispatch-sensitivities.yaml` |
| 200 | 272 | `0c65b2c49037fbec...` | `manifests/predispatchfcst.yaml` |
| 200 | 284 | `6495da81293d90c9...` | `manifests/predispatchis-reports.yaml` |
| 200 | 268 | `552019bb916826fb...` | `manifests/public-prices.yaml` |
| 200 | 286 | `9bdea0e57642d3df...` | `manifests/rooftop-pv-actual-area.yaml` |
| 200 | 276 | `b3ba9820783b115e...` | `manifests/rooftop-pv-actual.yaml` |
| 200 | 290 | `9877a0c5c8caee89...` | `manifests/rooftop-pv-forecast-area.yaml` |
| 200 | 280 | `ca4a9d728b06d170...` | `manifests/rooftop-pv-forecast.yaml` |
| 200 | 264 | `649ed097ded348ae...` | `manifests/settlements.yaml` |
| 200 | 282 | `e3ec2ec4edccddc2...` | `manifests/sevendayoutlook-full.yaml` |
| 200 | 282 | `18962afbfba83ceb...` | `manifests/sevendayoutlook-peak.yaml` |
| 200 | 288 | `5afb42ea7d07512f...` | `manifests/short-term-pasa-reports.yaml` |
| 200 | 129 | `8d95eb32acb6703e...` | `manifests/sra-bids.yaml` |
| 200 | 143 | `db1f669a055664a0...` | `manifests/sra-nsr-reconciliation.yaml` |
| 200 | 131 | `fbfad90c6a2c7fa0...` | `manifests/sra-offers.yaml` |
| 200 | 288 | `85dd12cffb13318f...` | `manifests/stpasa-duidavailability.yaml` |
| 200 | 290 | `5775bdc161cca766...` | `manifests/trading-cumulative-price.yaml` |
| 200 | 266 | `fe9e94643f6963d6...` | `manifests/trading-irsr.yaml` |
| 200 | 276 | `c88a81da47663a7b...` | `manifests/tradingis-reports.yaml` |
| 200 | 136 | `999b02b69e50e6e6...` | `manifests/vwa-fcas-prices.yaml` |
| 200 | 284 | `2181e6c2e3695004...` | `manifests/wdr-capacity-no-scada.yaml` |
| 200 | 1116 | `04f565b7f3485762...` | `source/helpers.js` |
| 200 | 651858 | `65b9fcd265631f70...` | `source/index_page.js` |
| 200 | 19400 | `c2209b38df8fed7d...` | `source/index.html` |

## Re-capture procedure

To refresh this directory (e.g. if AEMO updates the catalog):

```bash
cd /Users/zhipenghe/GitHub/nem-catalog
BASE="https://visualisations.aemo.com.au/aemo/nemweb"
UA="nem-catalog-recon/0.1 (+https://github.com/ZhipengHe/nem-catalog) curl"

# 1. Fetch master catalog
curl -sS -A "$UA" -o reference/aemo-catalog/dataset-list.yaml "$BASE/datasets/dataset-list.yaml"

# 2. Extract all definitionUrl + manifestUrl and fetch them
grep -E '^\s*(manifestUrl|definitionUrl): ' reference/aemo-catalog/dataset-list.yaml \
  | awk '{print $2}' | sort -u \
  | xargs -n1 -P6 -I{} bash -c '
      rel="$1"; ua="$2"; base="$3"
      out="reference/aemo-catalog/$rel"
      mkdir -p "$(dirname "$out")"
      curl -sS -A "$ua" --max-time 30 -o "$out" "$base/$rel"
    ' _ {} "$UA" "$BASE"

# 3. Regenerate this manifest (TODO: promote the inline bash above to scripts/fetch_aemo_catalog.py)
```

## Known deltas vs local mirror (to be resolved in recon phase)

- Our `nemweb-mirror/Reports/CURRENT/` listing has **103 dirs**; AEMO catalog has
  **97 datasets**. Delta = 6 unmapped mirror directories — candidates for
  undocumented / legacy / sunset. Not resolved here; that is the next recon output.
- Every manifest lists only `year: Current` + `year: Archive` sources. **No manifest
  references any `/DUPLICATE/` subtree.** This is the authoritative signal that
  DUPLICATE is a mirror-implementation artifact, not an AEMO-catalog concept.
- AEMO's canonical casing for archive is `/Reports/ARCHIVE/` (uppercase).
  `/Reports/Archive/` is a case-insensitive server alias.
