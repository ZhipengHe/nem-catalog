"""nem-catalog: Machine-readable URL catalog for AEMO NEMWEB.

Primary API:
    >>> import nem_catalog
    >>> catalog = nem_catalog.load("catalog.json")
    >>> urls = catalog.resolve("Reports:DispatchIS_Reports", from_="2025-04-01", to_="2025-04-02")

Convenience:
    >>> catalog = nem_catalog.fetch_latest()

See https://zhipenghe.github.io/nem-catalog/ for docs.
"""

from nem_catalog.catalog import Catalog
from nem_catalog.errors import (
    IncompatibleCatalogError,
    NemCatalogError,
    NemCatalogFetchError,
    UnresolvableDatasetError,
)
from nem_catalog.loader import fetch_latest, load

__version__ = "0.1.0"

__all__ = [
    "Catalog",
    "IncompatibleCatalogError",
    "NemCatalogError",
    "NemCatalogFetchError",
    "UnresolvableDatasetError",
    "__version__",
    "fetch_latest",
    "load",
]
