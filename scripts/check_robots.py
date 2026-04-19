"""Verify NEMWEB robots.txt permits the paths our crawler will visit.

Exits 0 and prints OK on permit.
Exits 1 and prints a diagnostic on disallow — the workflow then opens an issue.
"""
from __future__ import annotations
import sys
import urllib.request
import urllib.robotparser

NEMWEB = "https://nemweb.com.au"
USER_AGENT = "nem-catalog-crawler/0.1"
PATHS_WE_FETCH = [
    "/Reports/CURRENT/",
    "/Reports/ARCHIVE/",
    "/Data_Archive/Wholesale_Electricity/MMSDM/",
    "/Data_Archive/Wholesale_Electricity/NEMDE/",
    "/Data_Archive/Wholesale_Electricity/FCAS_Causer_Pays/",
]

def main() -> int:
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(f"{NEMWEB}/robots.txt")
    try:
        rp.read()
    except Exception as e:  # noqa: BLE001
        print(f"robots.txt fetch failed: {e}", file=sys.stderr)
        return 1
    disallowed = [p for p in PATHS_WE_FETCH if not rp.can_fetch(USER_AGENT, f"{NEMWEB}{p}")]
    if disallowed:
        print(f"robots.txt disallows: {disallowed}", file=sys.stderr)
        return 1
    print("robots.txt OK — all crawled paths allowed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
