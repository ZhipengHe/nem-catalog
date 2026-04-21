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

Policy-driven refetch:
    Load a freshness-policy YAML to skip ``static`` paths and limit
    ``rolling`` / ``append_only`` fetches to the budget.  Can be combined
    with ``--threads`` and ``--gaps`` for the canonical weekly-refresh
    workflow:

        POLICY=patterns/curated/freshness-policy.yaml
        python3 scripts/nemweb_download.py --policy $POLICY [MAX_FETCHES]
        python3 scripts/nemweb_download.py --threads 8 --gaps \
            --policy $POLICY 10000
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

if __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.policy import Policy, PolicyLoadError

BASE = "https://nemweb.com.au"
OUT = Path("nemweb-mirror")
UA = "nem-catalog-survey (+https://github.com/ZhipengHe/nem-catalog; directory-listing downloads only)"  # noqa: E501
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


class HREFExtractionShiftError(RuntimeError):
    """Raised when HREF_RE extracts < 50% of the cached HREF count from a
    refetched listing, indicating AEMO likely changed the HTML template.

    The refetched bytes are written to disk for forensic inspection before
    raising, so a P0 investigator can diff the template. main() catches and
    exits 2; the workflow's on-failure step opens a P0 issue."""

    def __init__(self, url_path: str, before: int, after: int) -> None:
        super().__init__(
            f"HREF extraction shift: {url_path} before={before} after={after}. "
            "AEMO may have changed the HTML template; HREF_RE needs review."
        )
        self.url_path = url_path
        self.before = before
        self.after = after


def save_listing(url_path: str, data: bytes) -> None:
    """Content-aware write with template-shift guard.

    AEMO's IIS 8.5 server renders filesystem mtimes into directory listings,
    so refetched HTML bytes often differ even when the listed HREFs are
    identical. This function:
      1. Compares the HREF set from the cached file (if any) against the set
         extracted from the new bytes.
      2. If identical, skips the write (preserves mtime + byte identity, so
         git stays clean for AEMO maintenance churn).
      3. If the new set is empty or drops >=50% vs. cached (and cached was
         non-empty), writes the new bytes for forensics but raises
         HREFExtractionShiftError so the workflow can open a P0.
      4. Otherwise writes the new bytes.

    Empty-cache first-crawl falls through to an unconditional write.
    """
    p = OUT / url_path.lstrip("/")
    p.mkdir(parents=True, exist_ok=True)
    idx = p / "index.html"
    if idx.is_file():
        try:
            cached_bytes = idx.read_bytes()
        except OSError as e:
            print(f"  WARN {url_path}: {type(e).__name__}: {e}", file=sys.stderr)
            cached_bytes = None
        if cached_bytes is not None:
            old = frozenset(m.group(1) for m in HREF_RE.finditer(cached_bytes))
            new = frozenset(m.group(1) for m in HREF_RE.finditer(data))
            template_shift = bool(old) and (not new or len(new) * 2 <= len(old))
            if template_shift:
                idx.write_bytes(data)  # forensic write, then raise
                raise HREFExtractionShiftError(url_path, before=len(old), after=len(new))
            if old == new:
                return
    idx.write_bytes(data)


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


def parse_args(
    argv: list[str],
) -> tuple[bool, bool, str | None, int, int]:
    gaps = False
    force = False
    policy_path: str | None = None
    threads = 1
    max_fetches = 10_000
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--gaps":
            gaps = True
        elif a == "--force":
            force = True
        elif a == "--policy":
            if i + 1 >= len(argv):
                raise SystemExit("--policy requires a value")
            policy_path = argv[i + 1]
            if not policy_path:
                raise SystemExit("--policy requires a non-empty path")
            i += 1
        elif a.startswith("--policy="):
            policy_path = a.split("=", 1)[1]
            if not policy_path:
                raise SystemExit("--policy requires a non-empty path")
        elif a == "--threads":
            if i + 1 >= len(argv):
                raise SystemExit("--threads requires a value")
            raw = argv[i + 1]
            try:
                threads = int(raw)
            except ValueError:
                raise SystemExit(f"--threads must be a positive integer, got: {raw}") from None
            if threads < 1:
                raise SystemExit(f"--threads must be >= 1, got: {threads}")
            i += 1
        elif a.startswith("--threads="):
            raw = a.split("=", 1)[1]
            try:
                threads = int(raw)
            except ValueError:
                raise SystemExit(f"--threads must be a positive integer, got: {raw}") from None
            if threads < 1:
                raise SystemExit(f"--threads must be >= 1, got: {threads}")
        elif a.isdigit():
            max_fetches = int(a)
        else:
            raise SystemExit(f"Unknown argument: {a}")
        i += 1
    return gaps, force, policy_path, threads, max_fetches


def _should_refetch(path: str, force: bool, policy: Policy | None) -> bool:
    """Decide whether a cached file should be bypassed.

    Returns True if the walker must fetch the path from the network.
    Returns False if the walker may reuse the cached file.
    """
    if force:
        return True
    if policy is None:
        return False
    cls = policy.class_for(path)
    # static paths reuse cache; everything else refetches when the policy
    # is supplied. unclassified errs on the side of refetch (conservative).
    return cls != "static"


def _process_one_for_test(
    path: str, force: bool, policy: object | None
) -> tuple[str, str, list[str]]:
    """Test harness: exposes the process_one decision logic without the
    closure state (budget, visited). Only used by unit tests."""
    cached = local_path(path)
    if cached.is_file() and not _should_refetch(path, force, policy):
        try:
            data = cached.read_bytes()
        except OSError:
            return (path, "skip", [])
        return (path, "reuse", extract_children(path, data))
    url = urllib.parse.urljoin(BASE, path)
    data, status = throttled_fetch(url)
    if data is None or status != 200:
        return (path, "skip", [])
    # Mark outcome as fetch_noop if content-aware write short-circuits
    # by catching the early return in save_listing without mtime change.
    before_mtime = cached.stat().st_mtime_ns if cached.is_file() else None
    save_listing(path, data)
    after_mtime = cached.stat().st_mtime_ns if cached.is_file() else None
    outcome = "fetch_noop" if before_mtime == after_mtime else "fetch"
    return (path, outcome, extract_children(path, data))


def walk(
    seeds: list[str],
    threads: int,
    max_fetches: int,
    force: bool = False,
    policy: object | None = None,
) -> tuple[int, int, int, int]:
    """Wave-batched BFS. Each wave dispatches current frontier to a thread pool;
    children discovered become the next wave. Terminates when frontier is empty or
    max_fetches budget exhausted.

    When ``force`` is True, every path is re-fetched regardless of policy.
    When ``policy`` is non-None, paths classified `static` with an on-disk
    cached file are reused; all other paths are re-fetched.
    When ``policy`` is None and ``force`` is False, all cached paths are
    reused (legacy behaviour — matches original --gaps semantics).

    Returns: (fetched, fetched_noop, reused, skipped)
      fetched      — paths where save_listing wrote new or changed content (mtime changed).
      fetched_noop — paths fetched from the network but whose content was identical to the
                     cached copy; save_listing's content-aware dedup short-circuited
                     (mtime unchanged).
      reused       — paths served entirely from the on-disk cache without a network fetch.
      skipped      — paths skipped due to exhausted budget or non-200 response.
    """
    visited: set[str] = set()
    fetched = fetched_noop = reused = skipped = 0
    frontier: list[str] = [s for s in seeds if s.endswith("/")]

    budget_lock = threading.Lock()
    budget = {"remaining": max_fetches}

    def process_one(path: str) -> tuple[str, str, list[str]]:
        """Returns (path, outcome, children). Outcome: 'fetch' | 'fetch_noop' | 'reuse' | 'skip'."""
        cached = local_path(path)
        if cached.is_file() and not _should_refetch(path, force, policy):
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
        before_mtime = cached.stat().st_mtime_ns if cached.is_file() else None
        save_listing(path, data)
        after_mtime = cached.stat().st_mtime_ns if cached.is_file() else None
        outcome = "fetch_noop" if before_mtime == after_mtime else "fetch"
        return (path, outcome, extract_children(path, data))

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
                    print(f"  fetch     [{fetched:4d}]  {path}")
                elif outcome == "fetch_noop":
                    fetched_noop += 1
                    print(f"  fetch_noop[{fetched_noop:4d}]  {path}")
                elif outcome == "reuse":
                    reused += 1
                elif outcome == "skip":
                    skipped += 1
                for c in children:
                    if c not in visited:
                        frontier.append(c)
    return fetched, fetched_noop, reused, skipped


# ----- CLI -----


def main(argv: list[str]) -> int:
    gaps_mode, force, policy_path, threads, max_fetches = parse_args(argv)
    OUT.mkdir(parents=True, exist_ok=True)

    policy = None
    if policy_path:
        try:
            policy = Policy.load(policy_path)
        except PolicyLoadError as e:
            print(f"ERROR: policy load failed: {e}", file=sys.stderr)
            return 2

    if gaps_mode:
        print("Scanning mirror for gaps…")
        seeds = find_gaps()
        print(f"  found {len(seeds)} referenced-but-missing paths")
        if not seeds:
            print("No gaps. Nothing to do.")
            return 0
    else:
        seeds = list(SEEDS)

    if force:
        mode_str = "force-refresh"
    elif policy is not None:
        mode_str = f"policy-driven (v{policy.version})"
    elif gaps_mode:
        mode_str = "gap-fill"
    else:
        mode_str = "walk"
    print(f"Seeds: {len(seeds)}  threads: {threads}  max_fetches: {max_fetches}  mode: {mode_str}")

    try:
        fetched, fetched_noop, reused, skipped = walk(
            seeds, threads, max_fetches, force=force, policy=policy
        )
    except HREFExtractionShiftError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    print(
        f"\nDone. fetched={fetched}  fetch_noop={fetched_noop}"
        f"  reused={reused}  skipped={skipped}  under {OUT}/"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
