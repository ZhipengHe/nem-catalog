"""Freshness policy loader and pattern matcher for nem-catalog.

Loads patterns/curated/freshness-policy.yaml and classifies URL paths into one
of {rolling, append_only, static, parent_index}. Unmatched paths become
`unclassified` (walker treats as force-refetch — conservative over skip).

Pattern syntax: ant-style. `*` matches one path segment (no `/`); `**` matches
zero or more segments. Anchored at both ends. Precedence: longest pattern wins
by character count; tie-breaker is order-in-file.

Malformed policy files raise PolicyLoadError. Callers should translate to
exit-code 2 so weekly-refresh.yml's failure step opens a P0 issue.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

VALID_CLASSES = frozenset({"rolling", "append_only", "static", "parent_index"})


class PolicyLoadError(Exception):
    """Raised when freshness-policy.yaml is missing or malformed."""


@dataclass(frozen=True)
class _Rule:
    pattern: str
    class_: str
    regex: re.Pattern[str]


@dataclass
class Policy:
    version: int
    last_reviewed: str
    reviewer: str
    rules: list[_Rule]

    @classmethod
    def load(cls, path: Path | str) -> Policy:
        p = Path(path)
        if not p.is_file():
            raise PolicyLoadError(f"policy file not found: {p}")
        try:
            raw: Any = yaml.safe_load(p.read_text())
        except yaml.YAMLError as e:
            raise PolicyLoadError(f"YAML parse failed in {p}: {e}") from e
        if not isinstance(raw, dict):
            raise PolicyLoadError(f"policy root must be a mapping in {p}")
        if "rules" not in raw:
            raise PolicyLoadError(f"policy missing required key 'rules' in {p}")
        if not isinstance(raw["rules"], list) or not raw["rules"]:
            raise PolicyLoadError(f"policy 'rules' must be a non-empty list in {p}")

        raw_version = raw.get("version", 0)
        # Strict type check: YAML can deliver bool, float, str, list, null —
        # `int(...)` would silently coerce bool/float (int(True)=1, int(1.5)=1),
        # letting malformed schemas pass as v1. Accept only Python int, and
        # exclude bool explicitly since `isinstance(True, int)` is True.
        if isinstance(raw_version, bool) or not isinstance(raw_version, int):
            raise PolicyLoadError(f"{p}: policy version must be an integer, got {raw_version!r}")
        version = raw_version
        if version != 1:
            raise PolicyLoadError(f"{p}: unsupported policy version {version}, expected 1")

        rules: list[_Rule] = []
        for i, entry in enumerate(raw["rules"]):
            if not isinstance(entry, dict):
                raise PolicyLoadError(f"rule #{i} must be a mapping in {p}")
            pattern = entry.get("pattern")
            cls_name = entry.get("class")
            if not isinstance(pattern, str) or not pattern.startswith("/"):
                raise PolicyLoadError(
                    f"rule #{i} pattern must be a string starting with '/': {entry!r}"
                )
            if cls_name not in VALID_CLASSES:
                raise PolicyLoadError(
                    f"rule #{i} class must be one of {sorted(VALID_CLASSES)}: {entry!r}"
                )
            rules.append(_Rule(pattern=pattern, class_=cls_name, regex=_compile(pattern)))

        return cls(
            version=version,
            last_reviewed=str(raw.get("last_reviewed", "")),
            reviewer=str(raw.get("reviewer", "")),
            rules=rules,
        )

    def class_for(self, path: str) -> str:
        """Return classification for a URL path. Unmatched → 'unclassified'."""
        best_len = -1
        best_class = "unclassified"
        for rule in self.rules:
            if rule.regex.fullmatch(path) and len(rule.pattern) > best_len:
                best_len = len(rule.pattern)
                best_class = rule.class_
        return best_class


def _compile(pattern: str) -> re.Pattern[str]:
    """Compile an ant-style glob into an anchored regex.

    `*`  → [^/]*      (one segment, no slash)
    `**` → .*         (any depth, including empty)
    """
    # Tokenize, replacing `**` with a sentinel before escaping.
    sentinel_double = "\x00DOUBLESTAR\x00"
    sentinel_single = "\x00SINGLESTAR\x00"
    tmp = pattern.replace("**", sentinel_double).replace("*", sentinel_single)
    escaped = re.escape(tmp)
    escaped = escaped.replace(re.escape(sentinel_double), ".*")
    escaped = escaped.replace(re.escape(sentinel_single), "[^/]*")
    return re.compile(f"^{escaped}$")
