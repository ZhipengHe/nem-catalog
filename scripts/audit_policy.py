"""Stateless monthly audit of patterns/curated/freshness-policy.yaml.

Compares HREF-level changes between the cached mirror and a freshly-fetched
refetch (provided by the caller) against each path's classified
freshness_class. Findings:

- reclassify_up: path classified `static` but fresh refetch produced a
  different HREF set. Candidate for promotion to `append_only` or `rolling`.
- reclassify_down: path classified `rolling` but fresh refetch HREFs are
  identical to cached. Candidate for demotion; weaker signal (AEMO may have
  paused publication temporarily), so reviewer decides per reading.
- new_path: path fresh-fetched but not matched by any policy rule. Needs a
  new rule or is a genuine AEMO addition.

Intended usage (from .github/workflows/policy-audit.yml):

    python scripts/audit_policy.py --policy patterns/curated/freshness-policy.yaml \
        --mirror-root nemweb-mirror \
        --fresh-dir /tmp/fresh-refetch

where --fresh-dir contains a parallel index.html tree from a preceding
force-refetch into an alternate OUT directory. The script writes
audit-report.md to stdout and exits non-zero if any finding was emitted.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from scripts.policy import Policy

HREF_RE = re.compile(rb'<A HREF="([^"]+)"', re.IGNORECASE)


@dataclass(frozen=True)
class AuditFinding:
    kind: str  # "reclassify_up" | "reclassify_down" | "new_path"
    path: str
    current_class: str
    added_hrefs: int
    removed_hrefs: int


def _hrefs(data: bytes) -> frozenset[str]:
    return frozenset(m.group(1).decode("ascii", "ignore") for m in HREF_RE.finditer(data))


def run_audit(
    policy_path: Path | str,
    mirror_root: Path | str,
    fresh: dict[str, bytes],
) -> list[AuditFinding]:
    """Compare fresh-refetch HREFs vs. cached mirror HREFs, classified against policy.

    ``fresh`` is a dict mapping URL path (e.g. "/Reports/CURRENT/x/") to the
    bytes of the freshly-refetched index.html. Cached mirror bytes are read
    from ``<mirror_root>/<path>/index.html``.
    """
    policy = Policy.load(policy_path)
    mirror_root = Path(mirror_root)
    findings: list[AuditFinding] = []

    for url_path, fresh_bytes in fresh.items():
        cached_file = mirror_root / url_path.lstrip("/") / "index.html"
        cached_hrefs = _hrefs(cached_file.read_bytes()) if cached_file.is_file() else frozenset()
        fresh_hrefs = _hrefs(fresh_bytes)
        added = len(fresh_hrefs - cached_hrefs)
        removed = len(cached_hrefs - fresh_hrefs)
        changed = added + removed

        cls = policy.class_for(url_path)

        if cls == "unclassified":
            findings.append(
                AuditFinding(
                    kind="new_path",
                    path=url_path,
                    current_class=cls,
                    added_hrefs=added,
                    removed_hrefs=removed,
                )
            )
            continue

        if cls == "static" and changed > 0:
            findings.append(
                AuditFinding(
                    kind="reclassify_up",
                    path=url_path,
                    current_class=cls,
                    added_hrefs=added,
                    removed_hrefs=removed,
                )
            )
            continue

        if cls == "rolling" and changed == 0:
            findings.append(
                AuditFinding(
                    kind="reclassify_down",
                    path=url_path,
                    current_class=cls,
                    added_hrefs=added,
                    removed_hrefs=removed,
                )
            )
            continue

    return findings


def format_report(findings: Iterable[AuditFinding]) -> str:
    findings = list(findings)
    if not findings:
        return "# Policy Audit — clean\n\nAll classified paths behaved as expected.\n"
    lines: list[str] = [
        "# Policy Audit — findings",
        "",
        f"{len(findings)} findings.",
        "",
    ]
    groups: dict[str, list[AuditFinding]] = {}
    for f in findings:
        groups.setdefault(f.kind, []).append(f)
    for kind in ("reclassify_up", "reclassify_down", "new_path"):
        items = groups.get(kind, [])
        if not items:
            continue
        lines.append(f"## {kind} ({len(items)})")
        lines.append("")
        for f in items:
            lines.append(
                f"- `{f.path}` (class={f.current_class}, +{f.added_hrefs} -{f.removed_hrefs} HREFs)"
            )
        lines.append("")
    return "\n".join(lines)


def _load_fresh(fresh_dir: Path) -> dict[str, bytes]:
    """Load freshly-refetched index.html files from a parallel mirror tree."""
    out: dict[str, bytes] = {}
    for idx in fresh_dir.rglob("index.html"):
        rel = idx.parent.relative_to(fresh_dir).as_posix()
        url = "/" + rel + "/" if rel and rel != "." else "/"
        out[url] = idx.read_bytes()
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--policy", required=True)
    p.add_argument("--mirror-root", required=True)
    p.add_argument("--fresh-dir", required=True)
    args = p.parse_args(argv)

    fresh = _load_fresh(Path(args.fresh_dir))
    findings = run_audit(args.policy, args.mirror_root, fresh)
    print(format_report(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
