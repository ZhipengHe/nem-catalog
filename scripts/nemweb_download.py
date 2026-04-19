"""Download NEMWeb directory-listing HTML pages to local disk.

Walks nemweb.com.au starting from seed paths (or disk-discovered gaps).
Saves each HTML listing to nemweb-mirror/<url-path>/index.html (URL path
mirrored byte-exact). Follows byte-exact HREFs only; no case normalization.
Skips data files (ZIPs, CSVs, etc.) and off-host links. Global 1 req/s
throttle across all threads.

Modes
-----
Default (full walk):
    python3 scripts/nemweb_download.py [MAX_FETCHES]

Gap-fill only (scan existing mirror, fetch only referenced-but-missing paths,
then recurse into their children — reuses on-disk files without re-fetching):
    python3 scripts/nemweb_download.py --gaps [MAX_FETCHES]

Multi-threaded (hides per-request latency; aggregate rate still ≤1 req/s):
    python3 scripts/nemweb_download.py --threads 8 --gaps

Force-refresh all cached listings (bypass the cached-file shortcut so rolling
``Reports/CURRENT/*`` directories pick up new content):
    python3 scripts/nemweb_download.py --force [MAX_FETCHES]

Force-refresh a specific path only: delete its index.html on disk, then run
the default walk or ``--gaps`` mode.
"""

from __future__ import annotations

import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = "https://nemweb.com.au"
OUT = Path("nemweb-mirror")
UA = "nem-catalog-survey (+https://github.com/nem-catalog; directory-listing downloads only)"
SEEDS = ("/Reports/", "/Data_Archive/")
MIN_DELAY_S = 1.0

HREF_RE = re.compile(rb'<A HREF="([^"]+)">', re.IGNORECASE)

DATA_SUFFIXES = (
    ".zip",
    ".csv",
    ".xml",
    ".pdf",
    ".xls",
    ".xlsx",
    ".doc",
    ".docx",
    ".txt",
    ".7z",
    ".gz",
    ".json",
    ".log",
    ".inf",
    ".dat",
    ".sql",
)


# ----- HTTP with global rate limit -----

_rate_lock = threading.Lock()
_last_req = 0.0


def throttled_fetch(url: str) -> tuple[bytes | None, int]:
    global _last_req
    with _rate_lock:
        wait = MIN_DELAY_S - (time.monotonic() - _last_req)
        if wait > 0:
            time.sleep(wait)
        _last_req = time.monotonic()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read(), resp.status
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception as e:
        print(f"  ERR {url}: {type(e).__name__}: {e}", file=sys.stderr)
        return None, 0


# ----- Path helpers -----


def local_path(url_path: str) -> Path:
    return OUT / url_path.lstrip("/") / "index.html"


def url_path_from_local(index_file: Path) -> str:
    rel = index_file.parent.relative_to(OUT).as_posix()
    return "/" + rel + "/" if rel else "/"


def is_data_file(path: str) -> bool:
    lower = path.lower()
    return any(lower.endswith(suf) for suf in DATA_SUFFIXES)


def save_listing(url_path: str, data: bytes) -> None:
    p = OUT / url_path.lstrip("/")
    p.mkdir(parents=True, exist_ok=True)
    (p / "index.html").write_bytes(data)


def extract_children(parent_path: str, data: bytes) -> list[str]:
    """Byte-exact HREF extraction with filtering. Returns directory paths only."""
    out: list[str] = []
    for match in HREF_RE.finditer(data):
        try:
            href = match.group(1).decode("ascii")
        except UnicodeDecodeError:
            continue
        if href.startswith("http"):
            parsed = urllib.parse.urlparse(href)
            if parsed.netloc and parsed.netloc != "nemweb.com.au":
                continue
            new_path = parsed.path
        else:
            new_path = urllib.parse.urljoin(parent_path, href)
        if not new_path.endswith("/"):
            continue
        if is_data_file(new_path):
            continue
        # Parent-directory link (any proper prefix of current path)
        if parent_path.startswith(new_path) and new_path != parent_path:
            continue
        out.append(new_path)
    return out


# ----- Gap scan -----


def find_gaps() -> list[str]:
    """Scan on-disk mirror. Return paths referenced by any index.html that are not on disk."""
    saved: set[str] = set()
    index_files: list[Path] = []
    for idx in OUT.rglob("index.html"):
        saved.add(url_path_from_local(idx))
        index_files.append(idx)
    gaps: set[str] = set()
    for idx in index_files:
        parent = url_path_from_local(idx)
        for child in extract_children(parent, idx.read_bytes()):
            if child not in saved:
                gaps.add(child)
    return sorted(gaps)


# ----- Walk (BFS, wave-batched, threaded) -----


def walk(
    seeds: list[str], threads: int, max_fetches: int, force: bool = False
) -> tuple[int, int, int]:
    """Wave-batched BFS. Each wave dispatches current frontier to a thread pool;
    children discovered become the next wave. Terminates when frontier is empty or
    max_fetches budget exhausted.

    When ``force`` is True, cached listings are bypassed and re-fetched from the
    live server. This is required for rolling directories (``Reports/CURRENT/*``)
    whose contents roll over independently of the mirror.

    Returns: (fetched, reused, skipped)
    """
    visited: set[str] = set()
    fetched = reused = skipped = 0
    frontier: list[str] = [s for s in seeds if s.endswith("/")]

    budget_lock = threading.Lock()
    budget = {"remaining": max_fetches}

    def process_one(path: str) -> tuple[str, str, list[str]]:
        """Returns (path, outcome, children). Outcome: 'fetch' | 'reuse' | 'skip'."""
        cached = local_path(path)
        if cached.is_file() and not force:
            try:
                data = cached.read_bytes()
            except OSError:
                return (path, "skip", [])
            return (path, "reuse", extract_children(path, data))
        # Network fetch — honour budget
        with budget_lock:
            if budget["remaining"] <= 0:
                return (path, "skip", [])
            budget["remaining"] -= 1
        url = urllib.parse.urljoin(BASE, path)
        data, status = throttled_fetch(url)
        if data is None or status != 200:
            print(f"  skip {path} status={status}")
            return (path, "skip", [])
        save_listing(path, data)
        return (path, "fetch", extract_children(path, data))

    wave_n = 0
    while frontier and budget["remaining"] > 0:
        wave_n += 1
        wave = [p for p in frontier if p not in visited]
        for p in wave:
            visited.add(p)
        frontier = []
        print(
            f"\n── wave {wave_n}: {len(wave)} paths, "
            f"budget={budget['remaining']}, threads={threads} ──"
        )
        with ThreadPoolExecutor(max_workers=threads) as ex:
            for path, outcome, children in ex.map(process_one, wave):
                if outcome == "fetch":
                    fetched += 1
                    print(f"  fetch[{fetched:4d}]  {path}")
                elif outcome == "reuse":
                    reused += 1
                elif outcome == "skip":
                    skipped += 1
                for c in children:
                    if c not in visited:
                        frontier.append(c)
    return fetched, reused, skipped


# ----- CLI -----


def parse_args(argv: list[str]) -> tuple[bool, bool, int, int]:
    gaps = False
    force = False
    threads = 1
    max_fetches = 10_000
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--gaps":
            gaps = True
        elif a == "--force":
            force = True
        elif a == "--threads":
            threads = int(argv[i + 1])
            i += 1
        elif a.startswith("--threads="):
            threads = int(a.split("=", 1)[1])
        elif a.isdigit():
            max_fetches = int(a)
        else:
            raise SystemExit(f"Unknown argument: {a}")
        i += 1
    return gaps, force, threads, max_fetches


def main(argv: list[str]) -> int:
    gaps_mode, force, threads, max_fetches = parse_args(argv)
    OUT.mkdir(parents=True, exist_ok=True)

    if gaps_mode:
        print("Scanning mirror for gaps…")
        seeds = find_gaps()
        print(f"  found {len(seeds)} referenced-but-missing paths")
        if not seeds:
            print("No gaps. Nothing to do.")
            return 0
    else:
        seeds = list(SEEDS)

    mode_str = "force-refresh" if force else ("gap-fill" if gaps_mode else "walk")
    print(f"Seeds: {len(seeds)}  threads: {threads}  max_fetches: {max_fetches}  mode: {mode_str}")
    fetched, reused, skipped = walk(seeds, threads, max_fetches, force=force)
    print(f"\nDone. fetched={fetched}  reused={reused}  skipped={skipped}  under {OUT}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
