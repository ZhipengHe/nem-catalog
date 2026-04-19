# AEMO crawl coordination

`nem-catalog` mirrors public NEMWEB directory listings weekly for the express purpose of deriving URL patterns for research and tool-building use. This document explains what the crawler does, how to contact us, and how to request adjustments.

## What the crawler does

- Fetches **directory listings only** (HTML `index.html` pages), not data files.
- Throttles to **1 request per second globally** across all threads (see `scripts/nemweb_download.py::MIN_DELAY_S`).
- Uses `--gaps` incremental mode weekly and a full recrawl monthly as a cross-check.
- User-Agent: `nem-catalog-survey (+https://github.com/ZhipengHe/nem-catalog; directory-listing downloads only)`.
- Source IP: GitHub Actions hosted-runner IP range (variable; published at https://api.github.com/meta).

## What the crawler does NOT do

- No data file downloads (no zips, no CSVs, no XML).
- No repeated pathological polling.
- No authentication or credentialed access.

## Contact

To request a rate-limit adjustment, allowlist, or ask the crawler to stop:
- Open a GitHub issue at https://github.com/ZhipengHe/nem-catalog/issues
- Tag it `aemo-coordination`.
- The repo maintainer (Zhipeng He) will pause the weekly workflow within 48 hours if requested.

## If we are blocked by the WAF

The weekly workflow auto-opens a GitHub issue when more than 5% of listings return non-200 responses. Catalog keeps serving the last-good version; the README badge reflects the last successful crawl date.
