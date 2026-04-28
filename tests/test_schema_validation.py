"""Validate the sample catalog fixture against the JSON Schema."""

import json
import re
from pathlib import Path

import jsonschema
import pytest

_TOKEN_RE = re.compile(r"\{(\w+)\}")

REPO_ROOT = Path(__file__).parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "catalog.schema.json"
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "sample_catalog.json"


@pytest.fixture
def schema():
    return json.loads(SCHEMA_PATH.read_text())


@pytest.fixture
def sample():
    return json.loads(FIXTURE_PATH.read_text())


def test_schema_is_valid_draft_2020_12(schema):
    validator_cls = jsonschema.validators.validator_for(schema)
    validator_cls.check_schema(schema)


def test_sample_validates(schema, sample):
    jsonschema.validate(instance=sample, schema=schema)


def test_sample_has_required_top_level_fields(sample):
    required = {
        "schema_version",
        "catalog_version",
        "as_of",
        "placeholders",
        "dataset_keys",
        "raw_keys",
        "datasets",
    }
    assert required.issubset(sample.keys())


def test_all_dataset_keys_index_into_datasets(sample):
    for key in sample["dataset_keys"]:
        assert key in sample["datasets"], f"dataset_keys entry {key!r} missing from datasets map"


def test_all_raw_keys_index_into_datasets(sample):
    for key in sample["raw_keys"]:
        assert key in sample["datasets"], f"raw_keys entry {key!r} missing from datasets map"


def test_dataset_keys_is_curated_subset_of_raw_keys(sample):
    dataset_keys = set(sample["dataset_keys"])
    raw_keys = set(sample["raw_keys"])
    assert dataset_keys.issubset(raw_keys), "dataset_keys must be a subset of raw_keys"
    aux_keys = {k for k in raw_keys - dataset_keys}
    assert any("AUX" in k or k.endswith("_AUX") for k in aux_keys), (
        f"Expected at least one AUX entry in raw_keys not in dataset_keys; got {aux_keys}"
    )


def test_unresolvable_record_has_null_filename(sample):
    ds = sample["datasets"]["Reports:NEXT_DAY_OFFER_ENERGY)SPARSE"]
    assert ds["resolvable"] is False
    for tier_name, tier_list in ds["tiers"].items():
        for tier in tier_list:
            assert tier["filename_template"] is None, (
                f"tier {tier_name} should have null filename_template"
            )


def test_mmsdm_dispatchprice_has_multiple_tiers_with_different_granularity(sample):
    ds = sample["datasets"]["MMSDM:DISPATCHPRICE"]
    tiers = ds["tiers"]
    assert "DATA" in tiers
    assert "CTL" in tiers
    assert tiers["DATA"][0]["time_granularity"] == "yyyymmddHHMM"
    assert tiers["CTL"][0]["time_granularity"] == "yyyymm"


def test_schema_validator_is_draft_2020_12(schema):
    validator_cls = jsonschema.validators.validator_for(schema)
    assert validator_cls is jsonschema.Draft202012Validator


def test_template_tokens_are_defined_in_placeholders(sample):
    placeholders = set(sample["placeholders"].keys())
    missing = []
    for key, ds in sample["datasets"].items():
        for tier_name, tier_list in ds["tiers"].items():
            for tier in tier_list:
                for field in ("path_template", "filename_template"):
                    template = tier.get(field)
                    if template is None:
                        continue
                    for token in _TOKEN_RE.findall(template):
                        if token not in placeholders:
                            missing.append(f"{key}.tiers.{tier_name}.{field}: {{{token}}}")
    assert not missing, f"Templates reference tokens not in placeholders: {missing}"


def test_filename_template_and_regex_null_together(sample):
    for key, ds in sample["datasets"].items():
        for tier_name, tier_list in ds["tiers"].items():
            for tier in tier_list:
                tmpl = tier.get("filename_template")
                regex = tier.get("filename_regex")
                assert (tmpl is None) == (regex is None), (
                    f"{key}.tiers.{tier_name}: filename_template and filename_regex "
                    f"must both be null or both be non-null; got tmpl={tmpl!r} regex={regex!r}"
                )
