"""Catalog class and query methods.

Primary API surface: Catalog.resolve, Catalog.count, Catalog.list_datasets.
Methods are implemented incrementally in Tasks 8 and 9.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any


class Catalog:
    """A loaded nem-catalog. Immutable. Queries are pure functions over the data."""

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
        """Curated subset of dataset keys."""
        return list(self._data["dataset_keys"])

    def raw_keys(self) -> list[str]:
        """Full set of dataset keys, including AUX."""
        return list(self._data["raw_keys"])
