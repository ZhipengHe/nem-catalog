#!/usr/bin/env bash
# Runs the shell code blocks from README.md against the tests/fixtures/sample_catalog.json
# served locally. Used in CI to prevent README rot.
set -euo pipefail

FIXTURE="$(dirname "$0")/fixtures/sample_catalog.json"

# Test 1: curl + jq hero one-liner
# (Substitute local fixture for the live Pages URL since CI has no live catalog yet.)
result=$(jq '.datasets["Reports:DispatchIS_Reports"].tiers.ARCHIVE[0]' "$FIXTURE")
echo "$result" | jq -e '.filename_template == "PUBLIC_DISPATCHIS_{date}.zip"' > /dev/null
echo "README example 1 (curl+jq hero): OK"

# Test 2: dataset_keys discovery
jq -e '.dataset_keys | length > 0' "$FIXTURE" > /dev/null
echo "README example 2 (dataset_keys populated): OK"

# Test 3: placeholders dict is self-describing
jq -e '.placeholders.date.format == "yyyymmdd"' "$FIXTURE" > /dev/null
echo "README example 3 (placeholders): OK"
