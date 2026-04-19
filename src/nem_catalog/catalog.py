"""Catalog class and query methods.

Immutable Catalog object. Queries are pure functions over loaded data.
resolve() warns + returns [] when the request window is entirely outside
observed_range (non-rolling records). It raises UnresolvableDatasetError for
records with resolvable=false (directory-level anomalies).
"""

from __future__ import annotations

import difflib
import re
import warnings
from collections.abc import Iterator
from datetime import datetime, timedelta
from typing import Any

from nem_catalog.errors import NonResolvableTemplateError, UnresolvableDatasetError

_NEMWEB_BASE = "https://nemweb.com.au"

# The complete set of placeholder names v0.1 resolve() can compute from a
# (dt_from, dt_to) pair. Anything outside this set in a SELECTED tier's
# filename_template or path_template causes resolve() to raise
# NonResolvableTemplateError for THAT tier only. Other tiers continue to
# expand normally.
#
# Keep in sync with _placeholders() and _infer_granularity() below, AND
# with the token vocabulary the extractor emits (scripts/extract_patterns.py
# DIGIT_LABELS + _BASE_LABEL_REGEX). Missing a name here silently strands
# datasets that would otherwise resolve.
_TEMPORAL_TOKENS: frozenset[str] = frozenset(
    {
        "date",
        "yyyymmdd",
        "timestamp",
        "yyyymmddHHMM",
        "yyyymmddhhmm",
        "datetime",
        "yyyymmddhh",
        "yearmonth",
        "yyyymm",
        "year",
        "yyyy",
        "month",
    }
)

_TOKEN_RE = re.compile(r"\{(\w+)\}")


class Catalog:
    """A loaded nem-catalog."""

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data

    @property
    def schema_version(self) -> str:
        return str(self._data["schema_version"])

    @property
    def catalog_version(self) -> str:
        return str(self._data["catalog_version"])

    @property
    def as_of(self) -> datetime:
        return datetime.fromisoformat(str(self._data["as_of"]).replace("Z", "+00:00"))

    @property
    def datasets(self) -> dict[str, dict[str, Any]]:
        return dict(self._data["datasets"])

    def dataset_keys(self) -> list[str]:
        return list(self._data["dataset_keys"])

    def raw_keys(self) -> list[str]:
        return list(self._data["raw_keys"])

    def list_datasets(self, filter: str | None = None, *, include_raw: bool = False) -> list[str]:
        """Return dataset keys, optionally case-insensitive substring-filtered."""
        keys = self.raw_keys() if include_raw else self.dataset_keys()
        if filter is None:
            return keys
        needle = filter.lower()
        return [k for k in keys if needle in k.lower()]

    def resolve(self, key: str, from_: str, to_: str, *, view: str | None = None) -> list[str]:
        """Expand a dataset to candidate URLs covering the date range.

        Tier routing (for Reports:* with a rolling CURRENT + ARCHIVE split):
          retention_cutoff = catalog.as_of - retention_hint_unverified_days
          - from_ >= cutoff           → rolling tier only
          - to_   <  cutoff           → non-rolling tiers + pre-retention warning
          - straddles cutoff          → both + pre-retention warning
        Records with no rolling tier (MMSDM / NEMDE / FCAS / anomalies) use
        every tier. observed_range is then applied per tier for non-rolling
        records as a safety filter (empty + warning if no tier overlaps).
        """
        record = self._get_record(key)
        if not record.get("resolvable", True):
            raise UnresolvableDatasetError(
                f"dataset {key!r} is resolvable=false (directory-level anomaly)"
            )

        dt_from = _parse_date(from_)
        dt_to = _parse_date(to_)
        if dt_to < dt_from:
            raise ValueError(f"to_ ({to_}) must be >= from_ ({from_})")

        tiers: dict[str, dict[str, Any]] = record["tiers"]
        rolling_name: str | None = next(
            (n for n, t in tiers.items() if t.get("retention_hint_unverified_days") is not None),
            None,
        )
        selected: dict[str, dict[str, Any]]
        pre_retention = False

        if rolling_name is None:
            selected = dict(tiers)
        else:
            days = int(tiers[rolling_name]["retention_hint_unverified_days"])
            cutoff = self.as_of.replace(tzinfo=None) - timedelta(days=days)
            if dt_from >= cutoff:
                selected = {rolling_name: tiers[rolling_name]}
            elif dt_to < cutoff:
                selected = {n: t for n, t in tiers.items() if n != rolling_name}
                pre_retention = True
            else:
                selected = dict(tiers)
                pre_retention = True

        if view is not None:
            selected = {n: t for n, t in selected.items() if n == view}

        if pre_retention:
            warnings.warn(
                f"resolve({key!r}, {from_!r}, {to_!r}): from_ is older than "
                f"catalog.as_of - retention_hint_unverified_days; reachability is "
                f"likely to fail for those URLs.",
                stacklevel=2,
            )

        # STRICT is applied per-tier at expansion time, AFTER observed_range
        # and straddle-partition filtering. If a tier has non-temporal tokens
        # AND that tier would actually emit URLs for this range, skip it with
        # a warning. If every candidate tier was skipped, raise. Rationale: a
        # request that falls entirely in a pure-temporal ARCHIVE window must
        # not be denied because the rolling CURRENT tier has {aemo_id}.
        urls: list[str] = []
        skipped_tiers: list[tuple[str, frozenset[str]]] = []

        if rolling_name is not None:
            for n, t in selected.items():
                if n == rolling_name:
                    tier_from = max(dt_from, cutoff)
                    if tier_from > dt_to:
                        continue
                    expand_from, expand_to = tier_from, dt_to
                else:
                    tier_to = min(dt_to, cutoff - timedelta(days=1))
                    if tier_to < dt_from:
                        continue
                    expand_from, expand_to = dt_from, tier_to
                leftover = _non_temporal_tokens(t)
                if leftover:
                    skipped_tiers.append((n, leftover))
                    continue
                urls.extend(_expand_tier(t, expand_from, expand_to))
            _warn_skipped_tiers(key, skipped_tiers)
            if not urls and skipped_tiers:
                n, leftover = skipped_tiers[0]
                raise NonResolvableTemplateError(dataset_key=key, tier=n, tokens=leftover)
            return urls

        any_overlap = False
        for n, t in selected.items():
            obs = t.get("observed_range")
            if obs and not _overlaps(dt_from, dt_to, obs):
                continue
            if obs:
                any_overlap = True
            leftover = _non_temporal_tokens(t)
            if leftover:
                skipped_tiers.append((n, leftover))
                continue
            urls.extend(_expand_tier(t, dt_from, dt_to))
        _warn_skipped_tiers(key, skipped_tiers)
        if selected and not any_overlap:
            warnings.warn(
                f"resolve({key!r}, {from_!r}, {to_!r}): requested range is outside "
                f"observed_range for all selected tiers — returning empty list.",
                stacklevel=2,
            )
            return []
        if not urls and skipped_tiers:
            n, leftover = skipped_tiers[0]
            raise NonResolvableTemplateError(dataset_key=key, tier=n, tokens=leftover)
        return urls

    def count(self, key: str, from_: str, to_: str, *, view: str | None = None) -> int:
        """Return the number of URLs resolve() would produce."""
        return len(self.resolve(key, from_, to_, view=view))

    def _get_record(self, key: str) -> dict[str, Any]:
        datasets = self._data["datasets"]
        if key not in datasets:
            close = difflib.get_close_matches(key, list(datasets.keys()), n=3, cutoff=0.6)
            msg = f"unknown dataset key {key!r}"
            if close:
                msg += f". Did you mean: {', '.join(repr(c) for c in close)}?"
            raise KeyError(msg)
        record: dict[str, Any] = datasets[key]
        return record


# ---- module-level helpers ------------------------------------------------


def _non_temporal_tokens(tier: dict[str, Any]) -> frozenset[str]:
    """Return the set of non-temporal placeholder names in a tier's templates.

    Scans both `filename_template` and `path_template` for `{name}` tokens
    and returns any name not in `_TEMPORAL_TOKENS`. Returns an empty frozenset
    when the tier is pure-temporal (resolve() can build concrete URLs).
    """
    tokens: set[str] = set()
    for key in ("filename_template", "path_template"):
        value = tier.get(key) or ""
        tokens.update(_TOKEN_RE.findall(value))
    return frozenset(tokens - _TEMPORAL_TOKENS)


def _parse_date(s: str) -> datetime:
    s = s.strip()
    if "T" in s:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).replace(tzinfo=None)
    return datetime.fromisoformat(s + "T00:00:00")


def _parse_lenient(s: str) -> datetime:
    """Parse observed_range values: 'YYYY', 'YYYY-MM', 'YYYY-MM-DD', or full ISO."""
    s = s.strip()
    if len(s) == 4:
        return datetime.fromisoformat(f"{s}-01-01T00:00:00")
    if len(s) == 7:
        return datetime.fromisoformat(f"{s}-01T00:00:00")
    if "T" not in s:
        return datetime.fromisoformat(s + "T00:00:00")
    return datetime.fromisoformat(s.replace("Z", "+00:00")).replace(tzinfo=None)


def _overlaps(dt_from: datetime, dt_to: datetime, observed: dict[str, Any]) -> bool:
    obs_from = _parse_lenient(str(observed["from"]))
    obs_to = _parse_lenient(str(observed["to"]))
    return not (dt_to < obs_from or dt_from > obs_to)


def _expand_tier(tier: dict[str, Any], dt_from: datetime, dt_to: datetime) -> list[str]:
    fname_t = tier.get("filename_template")
    if not fname_t:
        return []
    path_t = tier["path_template"]
    granularity = (tier.get("time_granularity") or _infer_granularity(fname_t)).lower()
    urls: list[str] = []
    for dt in _iterate_dates(dt_from, dt_to, granularity):
        vars_ = _placeholders(dt)
        urls.append(f"{_NEMWEB_BASE}{_format(path_t, vars_)}{_format(fname_t, vars_)}")
    return urls


def _warn_skipped_tiers(key: str, skipped: list[tuple[str, frozenset[str]]]) -> None:
    """Emit one UserWarning per tier skipped due to non-temporal placeholders.

    A tier is skipped when it was a router candidate but its template contains
    tokens the SDK cannot compute from a date range. The warning tells the
    caller which tier was bypassed and which tokens were unresolvable — so
    they know the returned URL set is partial.
    """
    for tier_name, tokens in skipped:
        tok_str = ", ".join(sorted(tokens))
        warnings.warn(
            f"resolve({key!r}): skipped tier {tier_name!r} — template contains "
            f"non-temporal placeholder(s) {{{tok_str}}} that v0.1 cannot substitute. "
            f"Inspect catalog.datasets[{key!r}]['tiers'][{tier_name!r}] for the raw "
            f"template.",
            stacklevel=3,
        )


def _infer_granularity(template: str) -> str:
    # Order matters: check longer/more-specific token names first so, e.g.,
    # "{datetime}" isn't matched by the "{date}" substring test.
    for g in (
        "yyyymmddHHMM",
        "yyyymmddhhmm",
        "timestamp",
        "datetime",
        "yyyymmddhh",
        "yyyymmdd",
        "date",
        "yearmonth",
        "yyyymm",
        "month",
        "yyyy",
        "year",
    ):
        if "{" + g + "}" in template:
            return g
    return "yyyymmdd"


def _iterate_dates(dt_from: datetime, dt_to: datetime, granularity: str) -> Iterator[datetime]:
    if granularity in {"yyyy", "year"}:
        for y in range(dt_from.year, dt_to.year + 1):
            yield datetime(y, 1, 1)
    elif granularity in {"yyyymm", "month", "yearmonth"}:
        y, m = dt_from.year, dt_from.month
        while (y, m) <= (dt_to.year, dt_to.month):
            yield datetime(y, m, 1)
            y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    elif granularity in {"yyyymmddhhmm", "timestamp", "datetime"}:
        cur = dt_from
        while cur <= dt_to:
            yield cur
            cur += timedelta(minutes=5)
    elif granularity == "yyyymmddhh":
        cur = dt_from
        while cur <= dt_to:
            yield cur
            cur += timedelta(hours=1)
    else:
        cur = dt_from
        while cur <= dt_to:
            yield cur
            cur += timedelta(days=1)


def _placeholders(dt: datetime) -> dict[str, str]:
    ymd = dt.strftime("%Y%m%d")
    ts = dt.strftime("%Y%m%d%H%M")
    ym = dt.strftime("%Y%m")
    y4 = dt.strftime("%Y")
    return {
        "date": ymd,
        "yyyymmdd": ymd,
        "timestamp": ts,
        "yyyymmddHHMM": ts,
        "yyyymmddhhmm": ts,
        # 14-digit yyyymmddhhmmss — AEMO dispatch files publish with ss=00;
        # seconds-level cadence isn't observed in any shipped dataset.
        "datetime": dt.strftime("%Y%m%d%H%M%S"),
        "yyyymmddhh": dt.strftime("%Y%m%d%H"),
        "yearmonth": ym,
        "yyyymm": ym,
        "year": y4,
        "yyyy": y4,
        "month": dt.strftime("%m"),
    }


def _format(template: str, vars_: dict[str, str]) -> str:
    """Substitute {placeholder} tokens; unknown placeholders remain as '{name}'."""
    out = template
    for k, v in vars_.items():
        out = out.replace("{" + k + "}", v)
    return out
