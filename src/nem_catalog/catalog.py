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
# (dt_from, dt_to) pair. Anything outside this set in a selected tier's
# filename_template or path_template causes resolve() to raise
# NonResolvableTemplateError. Keep in sync with _placeholders() below.
_TEMPORAL_TOKENS: frozenset[str] = frozenset({
    "date", "yyyymmdd",
    "timestamp", "yyyymmddHHMM", "yyyymmddhhmm",
    "yyyymm",
    "year", "yyyy",
    "month",
})

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

    def resolve(
        self, key: str, from_: str, to_: str, *, view: str | None = None
    ) -> list[str]:
        """Expand a dataset to candidate URLs covering the date range.

        Tier routing (for Reports:* with a rolling CURRENT + ARCHIVE split):
          retention_cutoff = catalog.as_of − retention_hint_unverified_days
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

        # STRICT pre-flight: every selected tier's template must use only
        # temporal placeholders. Fail fast before building any URL so callers
        # never see a URL string with unsubstituted `{token}` literals.
        for tier_name, tier in selected.items():
            leftover = _non_temporal_tokens(tier)
            if leftover:
                raise NonResolvableTemplateError(
                    dataset_key=key, tier=tier_name, tokens=leftover
                )

        if pre_retention:
            warnings.warn(
                f"resolve({key!r}, {from_!r}, {to_!r}): from_ is older than "
                f"catalog.as_of − retention_hint_unverified_days; reachability is "
                f"likely to fail for those URLs.",
                stacklevel=2,
            )

        # Rolling-tier records skip observed_range filtering: the retention
        # warning already communicates near-live reachability risk, and ARCHIVE
        # observed_range upper bound lags CURRENT by design.
        #
        # B5: when a straddle selects both tiers, partition the range at cutoff
        # so CURRENT covers [cutoff, dt_to] and ARCHIVE covers [dt_from, cutoff).
        # Previously both tiers expanded over the full (dt_from, dt_to) range
        # and produced overlapping URLs for every date in the intersection.
        urls: list[str] = []
        if rolling_name is not None:
            for n, t in selected.items():
                if n == rolling_name:
                    tier_from = max(dt_from, cutoff)
                    urls.extend(_expand_tier(t, tier_from, dt_to))
                else:
                    tier_to = min(dt_to, cutoff - timedelta(days=1))
                    if tier_to >= dt_from:
                        urls.extend(_expand_tier(t, dt_from, tier_to))
            return urls

        any_overlap = False
        for n, t in selected.items():
            obs = t.get("observed_range")
            if obs and not _overlaps(dt_from, dt_to, obs):
                continue
            if obs:
                any_overlap = True
            urls.extend(_expand_tier(t, dt_from, dt_to))
        if selected and not any_overlap:
            warnings.warn(
                f"resolve({key!r}, {from_!r}, {to_!r}): requested range is outside "
                f"observed_range for all selected tiers — returning empty list.",
                stacklevel=2,
            )
            return []
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


def _infer_granularity(template: str) -> str:
    for g in ("yyyymmddHHMM", "yyyymmddhhmm", "timestamp", "yyyymmdd", "date", "yyyymm", "month", "yyyy", "year"):
        if "{" + g + "}" in template:
            return g
    return "yyyymmdd"


def _iterate_dates(dt_from: datetime, dt_to: datetime, granularity: str) -> Iterator[datetime]:
    if granularity in {"yyyy", "year"}:
        for y in range(dt_from.year, dt_to.year + 1):
            yield datetime(y, 1, 1)
    elif granularity in {"yyyymm", "month"}:
        y, m = dt_from.year, dt_from.month
        while (y, m) <= (dt_to.year, dt_to.month):
            yield datetime(y, m, 1)
            y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    elif granularity in {"yyyymmddhhmm", "timestamp"}:
        cur = dt_from
        while cur <= dt_to:
            yield cur
            cur += timedelta(minutes=5)
    else:
        cur = dt_from
        while cur <= dt_to:
            yield cur
            cur += timedelta(days=1)


def _placeholders(dt: datetime) -> dict[str, str]:
    ymd = dt.strftime("%Y%m%d")
    ts = dt.strftime("%Y%m%d%H%M")
    return {
        "date": ymd, "yyyymmdd": ymd,
        "timestamp": ts, "yyyymmddHHMM": ts, "yyyymmddhhmm": ts,
        "yyyymm": dt.strftime("%Y%m"),
        "year": dt.strftime("%Y"), "yyyy": dt.strftime("%Y"),
        "month": dt.strftime("%m"),
    }


def _format(template: str, vars_: dict[str, str]) -> str:
    """Substitute {placeholder} tokens; unknown placeholders remain as '{name}'."""
    out = template
    for k, v in vars_.items():
        out = out.replace("{" + k + "}", v)
    return out
