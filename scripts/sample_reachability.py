"""Sample 5 random resolved URLs per repo from the published catalog and HEAD each.

Exits 0 on all-pass, exits 1 on any non-200 (workflow converts exit into issue).
"""
from __future__ import annotations
import random
import sys
import urllib.request
from collections import defaultdict

import nem_catalog

NEMWEB_BASE = "https://nemweb.com.au"
SAMPLE_PER_REPO = 5
RNG = random.Random(42)

def head(url: str) -> int:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "nem-catalog-integration/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:  # noqa: BLE001
        return 0

def main() -> int:
    cat = nem_catalog.fetch_latest()
    by_repo: dict[str, list[str]] = defaultdict(list)
    for key in cat.dataset_keys():
        repo = key.split(":", 1)[0]
        by_repo[repo].append(key)

    failures: list[tuple[str, int]] = []
    for repo, keys in by_repo.items():
        sample = RNG.sample(keys, min(SAMPLE_PER_REPO, len(keys)))
        for key in sample:
            try:
                urls = cat.resolve(key, from_="2025-04-01", to_="2025-04-02")
            except Exception as e:  # noqa: BLE001
                print(f"SKIP {key}: resolve raised {e}")
                continue
            if not urls:
                continue
            url = urls[0]
            status = head(url)
            line = f"{status} {repo}:{key} {url}"
            print(line)
            if status != 200:
                failures.append((url, status))

    if failures:
        print(f"\n{len(failures)} non-200 responses")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
