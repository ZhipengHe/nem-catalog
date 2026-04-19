"""Emit a markdown dataset-diff summary comparing old catalog.json (HEAD) to new (working tree).

Writes to stdout. Called by weekly-refresh.yml to populate the PR body.
"""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

# Threshold for "significant" diff per test plan line 55. Configurable via CLI.
THRESHOLD_PCT = 5

def load_old_catalog() -> dict:
    """Load the catalog.json from HEAD (pre-refresh). Returns {} if missing (first run)."""
    try:
        raw = subprocess.check_output(["git", "show", "HEAD:catalog.json"], stderr=subprocess.DEVNULL)
        return json.loads(raw)
    except subprocess.CalledProcessError:
        return {}

def load_new_catalog() -> dict:
    return json.loads(Path("catalog.json").read_text())

def main() -> int:
    old = load_old_catalog()
    new = load_new_catalog()
    old_keys = set(old.get("datasets", {}).keys())
    new_keys = set(new.get("datasets", {}).keys())
    added = sorted(new_keys - old_keys)
    removed = sorted(old_keys - new_keys)
    total_old = len(old_keys) or 1
    pct_change = 100 * (len(added) + len(removed)) / total_old
    lines = [
        f"### Dataset-level diff ({pct_change:.1f}% change, threshold {THRESHOLD_PCT}%)",
        "",
        f"- **Added** ({len(added)}): {', '.join(f'`{k}`' for k in added[:20])}{' ...' if len(added) > 20 else ''}" if added else "- **Added**: none",
        f"- **Removed** ({len(removed)}): {', '.join(f'`{k}`' for k in removed[:20])}{' ...' if len(removed) > 20 else ''}" if removed else "- **Removed**: none",
        "",
    ]
    if pct_change >= THRESHOLD_PCT:
        lines.append(f":warning: **Dataset-level change exceeds {THRESHOLD_PCT}% threshold.** Review curated/ for matching updates.")
        lines.append("")
    print("\n".join(lines))
    return 0

if __name__ == "__main__":
    sys.exit(main())
