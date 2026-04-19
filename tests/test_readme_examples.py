"""Execute the Python code blocks in README.md against the sample fixture.

Keeps README examples from rotting when APIs change.
"""

from pathlib import Path

import nem_catalog

REPO_ROOT = Path(__file__).parent.parent
FIXTURE = REPO_ROOT / "tests" / "fixtures" / "sample_catalog.json"


def test_load_example():
    catalog = nem_catalog.load(str(FIXTURE))
    assert catalog.schema_version == "1.0.0"


def test_resolve_example():
    catalog = nem_catalog.load(str(FIXTURE))
    urls = catalog.resolve(
        "Reports:DispatchIS_Reports",
        from_="2025-04-01",
        to_="2025-04-02",
    )
    assert len(urls) > 0
    assert all(u.startswith("https://nemweb.com.au/") for u in urls)


def test_count_example():
    catalog = nem_catalog.load(str(FIXTURE))
    n = catalog.count("Reports:DispatchIS_Reports", from_="2024-01-01", to_="2024-12-31")
    assert isinstance(n, int)
    assert n >= 0


def test_readme_strict_raise_example():
    """The README documents that resolve() raises on CURRENT tier filenames
    with non-temporal placeholders. Keep that claim honest."""
    from nem_catalog.errors import NonResolvableTemplateError
    catalog = nem_catalog.load(str(FIXTURE))
    import pytest
    with pytest.raises(NonResolvableTemplateError):
        catalog.resolve(
            "Reports:DispatchIS_Reports",
            from_="2026-04-17",
            to_="2026-04-18",
        )
