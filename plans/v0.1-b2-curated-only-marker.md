# B2 — curated_only Marker + Orphan Rule Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let the `patterns/curated/` YAML distinguish intentional placeholder entries (e.g., AEMO directory-anomalies we want in the catalog even though no files exist on the mirror) from real dataset overrides. Remove the broken `.github/orphan-fail-count.txt` 2-run tolerance dance — with the disambiguation in place, every orphan override IS a real AEMO deletion and should fail immediately.

**Architecture:** Add a boolean `curated_only: true` marker to the curated YAML schema. When the merge script encounters a curated entry with this marker, it inserts the entry into the output catalog as-is (requires `tiers` in YAML; `repo`/`intra_repo_id` are derived from the `{repo}:{intra_repo_id}` key). Unmarked curated entries remain overrides — they require an existing auto entry, and `merge()` now fails immediately (no counter, no commit-dance) if the auto base is missing.

**Tech Stack:** Python 3.11+ (stdlib + pyyaml + jsonschema), pytest via `uv run`. No new deps.

---

## Design Context (Load-Bearing — Quoted Inline)

This plan is self-contained. The gstack design doc at `~/.gstack/projects/ZhipengHe-nem-catalog/zhipenghe-worktree-v0.1-implementation-b2-eng-review-20260419-162415.md` is **provenance only** — every load-bearing decision is quoted below. A machine without `~/.gstack/` can still execute this plan from the text alone.

### Problem (quoted from design doc)

> `merge_catalog.py` overloads two distinct semantics onto "curated key not in auto catalog":
> 1. Intentional placeholder — we deliberately describe a dataset AEMO published without crawlable files (e.g., the `NEXT_DAY_OFFER_ENERGY)SPARSE` typo directory) so users see it in the catalog.
> 2. Suspected deletion — AEMO removed a dataset we previously overrode; the curated override is now stale and should trigger an alert.
>
> Today both cases emit an "orphan" warning and trigger a 2-run fail counter. Result: every weekly run warns about the 2 intentional placeholders; the fail counter state file (`/.github/orphan-fail-count.txt`) exists but can't be reliably updated because the workflow uses `continue-on-error: true` on merge and never commits the counter file back before `exit 1`. The whole apparatus is broken.

### Ground-truth facts (verified during plan authoring)

- `nemweb-mirror/Reports/ARCHIVE/NEXT_DAY_OFFER_ENERGY)SPARSE/` — directory exists, zero files (only parent-dir link in `index.html`). Classic AEMO typo directory.
- `nemweb-mirror/Reports/ARCHIVE/DispatchIS_FCAS_Fix/` — directory exists, zero files (also only parent-dir link). Same pattern.
- `.github/orphan-fail-count.txt` — does NOT exist in the repo. The workflow references a file that isn't tracked. The counter always reads as 0.

Both curated placeholder YAML entries are legitimately empty-directory placeholders. Both should become `curated_only: true` + full `tiers` block.

### Decision semantics (quoted from design doc)

> ```
> Curated YAML entry
>       │
>       ├── curated_only: true  (intentional placeholder)
>       │      │
>       │      ├── key in auto?  →  WARN (curated_only shadows auto)
>       │      └── key not in auto?  →  INSERT as-is into catalog (happy path)
>       │
>       └── curated_only: false / absent  (override)
>              │
>              ├── key in auto?  →  MERGE fields (curated wins on overlap)
>              └── key not in auto?  →  FAIL immediately (AEMO deleted it)
> ```

### Counter elimination (quoted from design doc)

> **Eureka:** the `.github/orphan-fail-count.txt` exists ONLY because placeholder and deletion were conflated. Once disambiguated, every orphan (override whose auto base vanished) is a real deletion. Fail-on-first is correct. No counter needed. No `.github/orphan-fail-count.txt`. No commit-dance before `exit 1`. No `continue-on-error: true` racing with the counter-update step.

### Not in scope (quoted from design doc)

- Extractor enhancement to emit empty-listing records into the JSON catalog. (Curated YAML stays the home for anomalies.)
- Schema version bump. `curated_only` is YAML-layer only, never appears in emitted catalog.json.
- Backward compat for `--prior-fail-count`. v0.1 has no external users; CLI break is free.

---

## File Structure

| File | Nature | Responsibility |
|---|---|---|
| `scripts/merge_catalog.py` | Modified | Split orphan branch: `curated_only: true` inserts, unmarked override orphan fails immediately. Drop `--prior-fail-count` CLI arg and its handling. |
| `patterns/curated/reports.yaml` | Modified | Add `curated_only: true` + full `tiers` block to the 2 placeholder entries. |
| `patterns/curated/README.md` | Modified | Update "Merge semantics" section: rule 4 reworded, new rule for `curated_only`. |
| `.github/workflows/weekly-refresh.yml` | Modified | Remove `Track orphan-key prior fail count` and `Update orphan-key fail counter` steps. Remove `continue-on-error: true` from Merge step. Drop `--prior-fail-count` arg. |
| `tests/test_merge_catalog.py` | Modified | Add 4 new tests; update existing tests that pass `prior_fail_count` if any. |
| `catalog.json` | Modified | Regenerated after changes. Will now contain the 2 placeholder entries. |

Sequential implementation: everything flows through `scripts/merge_catalog.py`; tests before code (TDD); YAML and workflow after tests pass.

---

### Task 1: Verify starting state

**Files:**
- Check: `scripts/merge_catalog.py`, `tests/test_merge_catalog.py`, `.github/workflows/weekly-refresh.yml`

- [ ] **Step 1: Confirm worktree is clean and on the right branch**

Run:
```bash
cd ~/GitHub/nem-catalog/.claude/worktrees/v0.1-implementation
git status
git branch --show-current
uv run pytest tests/ 2>&1 | tail -3
```

Expected: working tree clean; branch `worktree-v0.1-implementation`; `78 passed` (or current count) — establishes the green baseline before B2.

- [ ] **Step 2: Confirm the 2 orphan YAML entries still exist**

Run:
```bash
grep -n "curated_only\|NEXT_DAY_OFFER_ENERGY\|DispatchIS_FCAS_Fix" patterns/curated/reports.yaml
```

Expected: `NEXT_DAY_OFFER_ENERGY)SPARSE` and `DispatchIS_FCAS_Fix` appear; `curated_only` does NOT appear yet (pre-B2 state).

---

### Task 2: RED — test curated_only inserts placeholder entry

**Files:**
- Modify: `tests/test_merge_catalog.py`

- [ ] **Step 1: Add the failing test at the end of `tests/test_merge_catalog.py`**

```python
def test_curated_only_inserts_placeholder_entry(tmp_path: Path) -> None:
    """B2: curated_only: true entries insert into catalog without needing an auto base."""
    auto = _write_auto(tmp_path, {})  # empty auto catalog
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:FakePlaceholder": {
                "curated_only": True,
                "resolvable": False,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/Reports/ARCHIVE/FakePlaceholder/",
                        "filename_template": None,
                        "filename_regex": None,
                        "example": "",
                        "cadence": "none",
                        "observed_range": None,
                    }
                },
                "anomaly_note": "Empty directory on AEMO; fixture test.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0, r.stderr
    data = json.loads(out.read_text())
    assert "Reports:FakePlaceholder" in data["datasets"]
    ds = data["datasets"]["Reports:FakePlaceholder"]
    assert ds["repo"] == "Reports"
    assert ds["intra_repo_id"] == "FakePlaceholder"
    assert ds["resolvable"] is False
    assert "curated_only" not in ds, "curated_only is a YAML-layer marker; must not leak into catalog.json"
```

Note: `_write_auto(tmp_path, {})` produces an auto catalog with zero datasets. The existing `merge_catalog.py:188` prints a warning for empty catalog — that's OK for this test; we're testing the curated_only insert path.

- [ ] **Step 2: Run the new test and confirm it fails**

Run: `uv run pytest tests/test_merge_catalog.py::test_curated_only_inserts_placeholder_entry -v`

Expected: test fails. Either because (a) the merge script treats `Reports:FakePlaceholder` as an orphan (pre-B2 behavior prints `ORPHAN CURATED KEY` and does NOT insert the entry), or (b) schema validation fails because the auto catalog is empty. Note which failure mode so Step 3's fix can address both.

---

### Task 3: RED — test override missing auto fails immediately

**Files:**
- Modify: `tests/test_merge_catalog.py`

- [ ] **Step 1: Add the failing test**

```python
def test_override_missing_auto_key_fails_immediately(tmp_path: Path) -> None:
    """B2: unmarked curated entry (override) whose key is not in auto catalog → FAIL on
    first run. No --prior-fail-count tolerance. This replaces the pre-B2 2-run counter.
    """
    auto = _write_auto(tmp_path, {})  # empty auto
    _write_curated(
        tmp_path,
        "reports",
        {
            # No curated_only → treated as override
            "Reports:DeletedByAemo": {
                "anomaly_note": "We used to override this but AEMO removed the dir.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode != 0, "override for missing auto key must fail"
    assert "ORPHAN" in r.stderr or "AEMO deletion" in r.stderr
    assert not out.exists() or json.loads(out.read_text()).get("datasets", {}) == {}
```

- [ ] **Step 2: Run and confirm failure**

Run: `uv run pytest tests/test_merge_catalog.py::test_override_missing_auto_key_fails_immediately -v`

Expected: test fails because pre-B2 behavior requires `prior_fail_count >= 1` for a SystemExit(1); the single-run case only prints warnings and returns 0.

---

### Task 4: RED — test curated_only shadows auto with warning

**Files:**
- Modify: `tests/test_merge_catalog.py`

- [ ] **Step 1: Add the failing test**

```python
def test_curated_only_shadows_auto_emits_warning(tmp_path: Path) -> None:
    """B2: curated_only: true for a key that ALSO exists in auto → curated wins, but
    emit a warning so maintainers notice the unusual overlap."""
    auto = _write_auto(
        tmp_path,
        {
            "Reports:Collision": {
                "repo": "Reports",
                "intra_repo_id": "Collision",
                "resolvable": True,
                "tiers": {
                    "CURRENT": {
                        "path_template": "/Reports/CURRENT/Collision/",
                        "filename_template": "collision_{date}.zip",
                        "filename_regex": r"^collision_\d{8}\.zip$",
                        "example": "collision_20240101.zip",
                        "cadence": "5min",
                        "observed_range": None,
                    }
                },
                "query_shape": None,
                "schema_source": None,
                "anomaly_note": None,
            }
        },
    )
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:Collision": {
                "curated_only": True,
                "resolvable": False,
                "tiers": {
                    "ARCHIVE": {
                        "path_template": "/Reports/ARCHIVE/Collision/",
                        "filename_template": None,
                        "filename_regex": None,
                        "example": "",
                        "cadence": "none",
                        "observed_range": None,
                    }
                },
                "anomaly_note": "Curated wins here.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode == 0, r.stderr
    assert "shadows" in r.stderr.lower() or "curated_only" in r.stderr.lower(), (
        "must warn when curated_only entry overwrites an auto record"
    )
    data = json.loads(out.read_text())
    ds = data["datasets"]["Reports:Collision"]
    assert ds["resolvable"] is False  # curated won
    assert list(ds["tiers"].keys()) == ["ARCHIVE"]  # auto's CURRENT tier is replaced
```

- [ ] **Step 2: Run and confirm failure**

Run: `uv run pytest tests/test_merge_catalog.py::test_curated_only_shadows_auto_emits_warning -v`

Expected: test fails — pre-B2 merge treats `curated_only` as just another field and merges tier records instead of replacing them.

---

### Task 5: RED — test curated_only with missing tiers fails schema validation

**Files:**
- Modify: `tests/test_merge_catalog.py`

- [ ] **Step 1: Add the failing test**

```python
def test_curated_only_without_tiers_fails_schema_validation(tmp_path: Path) -> None:
    """B2: curated_only: true entries must declare tiers (schema requires it).
    If YAML omits tiers, the inserted record fails validate() → SystemExit(1).
    """
    auto = _write_auto(tmp_path, {})
    _write_curated(
        tmp_path,
        "reports",
        {
            "Reports:BrokenPlaceholder": {
                "curated_only": True,
                "resolvable": False,
                # Intentionally no tiers — should fail schema validation
                "anomaly_note": "Oops, forgot tiers.",
            }
        },
    )
    out = tmp_path / "catalog.json"
    r = _run_merge(auto, tmp_path / "curated", out)
    assert r.returncode != 0, "malformed curated_only entry must fail"
    # The schema validator reports the missing required field:
    assert "tiers" in r.stderr
```

- [ ] **Step 2: Run and confirm failure**

Run: `uv run pytest tests/test_merge_catalog.py::test_curated_only_without_tiers_fails_schema_validation -v`

Expected: test fails — pre-B2 merge doesn't insert `curated_only` entries at all, so schema validation never runs on them.

---

### Task 6: GREEN — rewrite merge() orphan branch

**Files:**
- Modify: `scripts/merge_catalog.py:84-127` (the `merge()` function)
- Modify: `scripts/merge_catalog.py:171-201` (the `main()` CLI — drop `--prior-fail-count`)

- [ ] **Step 1: Rewrite the `merge()` function**

Replace the existing `merge()` function (lines 84-127) with this version. It splits the pre-B2 "orphan" branch into two paths (`curated_only` insert vs override missing-auto fail) and drops the `prior_fail_count` parameter.

```python
def merge(
    auto: dict[str, Any],
    overlays: dict[str, dict[str, Any]],
    defaults: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Apply curated overlays to the auto catalog. Returns merged catalog.

    Curated YAML entries are one of two kinds:

    - Override (no curated_only flag): merges fields into an existing auto
      entry. If the auto entry is missing, that means AEMO deleted a dataset
      we used to describe. Fail immediately — the curator should either
      restore the entry in AEMO or remove the YAML line.
    - Placeholder (curated_only: true): inserts into the catalog as-is.
      Requires a complete record shape (tiers in particular). Never
      orphan. If the key ALSO exists in auto, the curated record wins and
      a warning is emitted so the collision is visible.
    """
    merged: dict[str, Any] = copy.deepcopy(auto)
    datasets: dict[str, Any] = merged["datasets"]
    warnings: list[str] = []
    missing_auto_orphans: list[str] = []

    for key, overlay in overlays.items():
        if overlay.get("curated_only") is True:
            _insert_curated_only(key, overlay, merged, warnings)
            continue
        # Override path
        if key not in datasets:
            missing_auto_orphans.append(key)
            continue
        _merge_record(key, datasets[key], overlay, warnings)

    # Apply per-repo defaults only where the field is currently None/absent.
    for ds in datasets.values():
        repo = ds["repo"]
        default = defaults.get(repo, {})
        for field, value in default.items():
            if ds.get(field) is None:
                ds[field] = value

    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)

    if missing_auto_orphans:
        for key in missing_auto_orphans:
            print(
                f"ORPHAN CURATED KEY: {key} (override has no matching auto entry "
                f"— suspected AEMO deletion)",
                file=sys.stderr,
            )
        raise SystemExit(1)

    return merged


def _insert_curated_only(
    key: str,
    overlay: dict[str, Any],
    merged: dict[str, Any],
    warnings: list[str],
) -> None:
    """Insert a curated_only entry into the catalog. Derive ONLY repo and
    intra_repo_id from the key; all other fields come from the YAML overlay
    as-is. Missing required fields (resolvable, tiers) are caught by schema
    validate() after merge completes — intentionally, so malformed YAML
    surfaces as a validation error instead of being silently backfilled.

    Also appends the key to merged["raw_keys"] so placeholder entries are
    discoverable via list_datasets(include_raw=True). Without this, a user
    searching for "NEXT_DAY_OFFER" variants would not see the anomaly
    entry even though it's in datasets.
    """
    datasets: dict[str, Any] = merged["datasets"]
    if key in datasets:
        warnings.append(
            f"curated_only: {key} shadows an auto entry "
            f"(curated record wins, auto entry discarded)"
        )
    if ":" not in key:
        raise SystemExit(
            f"FAIL: curated_only key {key!r} is not in 'Repo:intra_repo_id' form"
        )
    repo, intra_repo_id = key.split(":", 1)
    record = {k: v for k, v in overlay.items() if k != "curated_only"}
    # Derive ONLY the key-encoded fields. Everything else is from YAML.
    # Schema validate() at the end of merge catches missing required fields.
    record.setdefault("repo", repo)
    record.setdefault("intra_repo_id", intra_repo_id)
    datasets[key] = record
    # Make the placeholder discoverable via list_datasets(include_raw=True).
    # dataset_keys is the curated user-facing subset; raw_keys is "everything
    # the catalog knows about." Placeholders belong in raw_keys.
    raw_keys: list[str] = merged["raw_keys"]
    if key not in raw_keys:
        raw_keys.append(key)
        raw_keys.sort()
```

- [ ] **Step 2: Update the module docstring (lines 1-19) to reflect the new semantics**

Replace the current merge-semantics comment block with:

```python
"""Merge patterns/auto/catalog.json with patterns/curated/*.yaml overlays.

Merge semantics (see docs/architecture.md):

1. Curated entry with `curated_only: true` → INSERT into the catalog as-is.
   Derives `repo` and `intra_repo_id` from the `{repo}:{intra_repo_id}` key.
   Requires `tiers` in the YAML (schema validation catches omissions).
   If the key also exists in auto, warn and overwrite with the curated
   record.
2. Curated entry without `curated_only` (override):
   a. Field overlap with auto: curated wins; emit WARNING with both values.
   b. Curated-only field: accept unconditionally.
   c. Key absent from auto: FAIL immediately (suspected AEMO deletion).
3. Auto-only dataset key: pass through unchanged.

Usage:
    python scripts/merge_catalog.py --auto patterns/auto/catalog.json \\
        --curated patterns/curated/ --out catalog.json
"""
```

- [ ] **Step 3: Update `_run_merge` test helper to drop `--prior-fail-count`**

Update the helper BEFORE touching `main()` so the existing tests keep passing once `main()` loses the flag. The `_run_merge` helper at `tests/test_merge_catalog.py:77-94` currently always passes `--prior-fail-count`. Replace it with:

```python
def _run_merge(
    auto_path: Path,
    curated_dir: Path,
    out_path: Path,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(MERGE_SCRIPT),
            "--auto", str(auto_path),
            "--curated", str(curated_dir),
            "--out", str(out_path),
        ],
        capture_output=True,
        text=True,
    )
```

Remove the `prior_fail_count=0` default from the signature and from every caller that passed it explicitly (grep for `prior_fail_count` in `tests/test_merge_catalog.py`; update each site).

- [ ] **Step 4: Update `main()` to drop `--prior-fail-count`**

Replace `main()` (lines 171-201) with:

```python
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", required=True, type=Path)
    parser.add_argument("--curated", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    auto = load_auto(args.auto)
    overlays, defaults = load_curated(args.curated)
    merged = merge(auto, overlays, defaults)

    if not merged.get("datasets"):
        print("WARNING: empty catalog — auto catalog contained zero datasets")

    try:
        validate(merged)
    except jsonschema.ValidationError as e:
        print(f"FAIL: merged catalog does not validate: {e.message}", file=sys.stderr)
        return 1
    print("schema validation: OK")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {args.out}")
    return 0
```

With Step 3 already applied, callers (helper + workflow fixed in Task 10) no longer pass the flag, so argparse won't error.

- [ ] **Step 5: Run the merge_catalog test suite**

Run: `uv run pytest tests/test_merge_catalog.py -v 2>&1 | tail -20`

Expected: all 4 new B2 tests pass; all pre-existing `test_merge_catalog.py` tests still pass.

- [ ] **Step 6: Run the full test suite**

Run: `uv run pytest tests/ 2>&1 | tail -3`

Expected: `82 passed` (78 pre-B2 + 4 new). Zero regressions in unrelated tests.

- [ ] **Step 7: Run mypy strict on src/**

Run: `uv run mypy --strict src/ 2>&1 | tail -3`

Expected: `Success: no issues found in 4 source files`. (Note: `scripts/` is not under mypy strict in this project; if mypy runs on scripts/ in CI and complains, silence those with `# type: ignore` comments only if strictly necessary — prefer clean types.)

---

### Task 7: Verify DispatchIS_FCAS_Fix state on live NEMWEB

Design doc required ground-truth verification against both the local mirror AND a live URL before committing to treating `DispatchIS_FCAS_Fix` as a curated_only placeholder. Plan-author already verified against the local mirror (zero files); add the live check here so the decision is fully grounded before the YAML edit.

**Files:** none modified — verification only.

- [ ] **Step 1: Fetch the live NEMWEB directory listing for DispatchIS_FCAS_Fix**

Run:
```bash
curl -sSL -A "nem-catalog-b2-audit/0.1" "https://nemweb.com.au/Reports/ARCHIVE/DispatchIS_FCAS_Fix/" | head -50
```

Expected outcomes and their meaning:
- **Listing returns HTML with zero `<A HREF>` file entries** (only the `[To Parent Directory]` link): directory exists, is empty → proceed to Task 8 with `curated_only: true` as planned.
- **Listing returns HTML with actual file entries**: directory has files. The extractor should have picked them up; investigate why it didn't (likely classifier bug). PAUSE — escalate to user before editing the YAML. This is a separate fix from B2.
- **HTTP 404 or connection error**: directory is gone from NEMWEB entirely. PAUSE — the curated YAML entry should be REMOVED rather than turned into a placeholder. Escalate to user.

- [ ] **Step 2: Grep for `<A HREF` entries to confirm count matches the local mirror**

Run:
```bash
curl -sSL -A "nem-catalog-b2-audit/0.1" "https://nemweb.com.au/Reports/ARCHIVE/DispatchIS_FCAS_Fix/" | grep -c "<A HREF="
```

Expected: `1` — the single parent-dir link, matching the local mirror (zero file entries). Any number > 1 means files exist on live NEMWEB that our mirror doesn't have; pause and escalate.

- [ ] **Step 3: Record the verification in the next task's commit message**

Keep the Step 1 output noted (or captured) for reference; Task 13's commit message already cites "verified 2026-04-19 against local nemweb-mirror" — update that line in the commit message at Task 13 Step 3 to also say "and live NEMWEB listing" if Step 1/2 confirmed zero files live.

---

### Task 8: Update reports.yaml with placeholder tier blocks

**Files:**
- Modify: `patterns/curated/reports.yaml`

- [ ] **Step 1: Replace the two placeholder entries with full curated_only blocks**

Open `patterns/curated/reports.yaml`. Replace the existing `Reports:NEXT_DAY_OFFER_ENERGY)SPARSE` block (lines 16-22) and `Reports:DispatchIS_FCAS_Fix` block (lines 24-27) with the versions below.

```yaml
"Reports:NEXT_DAY_OFFER_ENERGY)SPARSE":
  curated_only: true
  resolvable: false
  tiers:
    ARCHIVE:
      path_template: "/Reports/ARCHIVE/NEXT_DAY_OFFER_ENERGY)SPARSE/"
      filename_template: null
      filename_regex: null
      example: ""
      cadence: "none"
      observed_range: null
  anomaly_note: |
    Directory-level anomaly: AEMO published this stream with a malformed ')' in the name
    and the directory contains zero files. URL is correct as stated — do NOT URL-encode
    the ')' character. Entry exists for catalog completeness; do not expect file resolution.
    resolve() will raise UnresolvableDatasetError.

"Reports:DispatchIS_FCAS_Fix":
  curated_only: true
  resolvable: false
  tiers:
    ARCHIVE:
      path_template: "/Reports/ARCHIVE/DispatchIS_FCAS_Fix/"
      filename_template: null
      filename_regex: null
      example: ""
      cadence: "none"
      observed_range: null
  anomaly_note: |
    Directory exists on NEMWEB under /Reports/ARCHIVE/ but contains zero files
    (verified 2026-04-19 against local nemweb-mirror). Likely a one-off historical
    correction AEMO published and subsequently emptied. Entry exists for catalog
    completeness; resolve() will raise UnresolvableDatasetError.
```

- [ ] **Step 2: Keep the `Reports:DispatchIS_Reports` override block unchanged**

The `Reports:DispatchIS_Reports` entry at the top of the file is a real override (adds `retention_hint_unverified_days` to an auto-discovered dataset). Do NOT add `curated_only` to it.

- [ ] **Step 3: Validate YAML parses cleanly**

Run:
```bash
uv run python -c "import yaml; yaml.safe_load(open('patterns/curated/reports.yaml').read())" && echo OK
```

Expected: `OK`.

---

### Task 9: Update patterns/curated/README.md merge-semantics section

**Files:**
- Modify: `patterns/curated/README.md:22-28`

- [ ] **Step 1: Replace the "Merge semantics" section**

Replace lines 22-28 (the numbered list) with:

```markdown
## Merge semantics

See `scripts/merge_catalog.py` and `docs/architecture.md`:

1. **Placeholder entry** (`curated_only: true`): insert into the catalog as-is.
   Requires full record shape (tiers in particular). Warns and overwrites if
   the key also exists in auto. Use for AEMO directories that exist but have
   zero files (e.g., directory-level anomalies, one-off corrections).
2. **Override entry** (no `curated_only` flag):
   - Field overlap with auto: curated wins, build warns with both values.
   - Curated-only field: accept unconditionally.
   - Auto-only field: pass through.
   - Key missing from auto: FAIL immediately (suspected AEMO deletion —
     investigate the cause, then either restore the curated field or remove
     the YAML entry).
3. Auto-only key: flows through to catalog unchanged.
```

- [ ] **Step 2: Update the "What goes here" section to mention placeholders**

Append to the bullet list at lines 8-13:

```markdown
- Placeholder entries (`curated_only: true`) for datasets AEMO publishes without crawlable files — directory exists, zero content. Requires full tiers block.
```

---

### Task 10: Simplify weekly-refresh.yml workflow

**Files:**
- Modify: `.github/workflows/weekly-refresh.yml:91-118` (the orphan-counter block)

- [ ] **Step 1: Replace the orphan-counter block with a clean merge step**

Locate lines 91-118 in `.github/workflows/weekly-refresh.yml`. Replace:

```yaml
      - name: Regenerate auto patterns
        run: uv run python scripts/extract_patterns.py

      - name: Track orphan-key prior fail count
        id: orphans
        run: |
          if [ -f .github/orphan-fail-count.txt ]; then
            PRIOR=$(cat .github/orphan-fail-count.txt)
          else
            PRIOR=0
          fi
          echo "prior=$PRIOR" >> $GITHUB_OUTPUT

      - name: Merge catalog
        id: merge
        continue-on-error: true
        run: |
          uv run python scripts/merge_catalog.py \
            --auto patterns/auto/catalog.json \
            --curated patterns/curated/ \
            --out catalog.json \
            --prior-fail-count ${{ steps.orphans.outputs.prior }}

      - name: Update orphan-key fail counter
        run: |
          if [ "${{ steps.merge.outcome }}" = "failure" ]; then
            echo $(( ${{ steps.orphans.outputs.prior }} + 1 )) > .github/orphan-fail-count.txt
            exit 1
          else
            echo 0 > .github/orphan-fail-count.txt
          fi
```

With:

```yaml
      - name: Regenerate auto patterns
        run: uv run python scripts/extract_patterns.py

      - name: Merge catalog
        run: |
          uv run python scripts/merge_catalog.py \
            --auto patterns/auto/catalog.json \
            --curated patterns/curated/ \
            --out catalog.json
```

That is: remove the `Track orphan-key prior fail count` step, remove the `Update orphan-key fail counter` step, remove `continue-on-error: true`, remove `--prior-fail-count`, remove the `id: merge` / `id: orphans` wiring.

- [ ] **Step 2: Confirm the workflow file is still valid YAML**

Run:
```bash
uv run python -c "import yaml; yaml.safe_load(open('.github/workflows/weekly-refresh.yml').read())" && echo OK
```

Expected: `OK`.

- [ ] **Step 3: Confirm nothing else in the workflow references the removed surface**

Run:
```bash
grep -n "prior-fail-count\|orphan-fail-count\|steps.orphans\|steps.merge.outcome" .github/workflows/weekly-refresh.yml || echo "no stale references"
```

Expected: `no stale references`.

---

### Task 11: Regenerate catalog.json with the new placeholder entries

**Files:**
- Modify: `catalog.json` (regenerated)

- [ ] **Step 1: Run the extractor**

Run:
```bash
uv run python scripts/extract_patterns.py 2>&1 | tail -5
```

Expected: last line shows `wrote reference/URL-CONVENTIONS.md  (367 datasets, 2325 rows)` or similar.

- [ ] **Step 2: Run the merge**

Run:
```bash
uv run python scripts/merge_catalog.py \
  --auto patterns/auto/catalog.json \
  --curated patterns/curated/ \
  --out catalog.json 2>&1 | tail -5
```

Expected: ends with `schema validation: OK` and `wrote catalog.json`. NO `ORPHAN CURATED KEY` warnings for the 2 placeholder keys (they're now `curated_only: true`). NO `WARNING: curated_only ... shadows` warnings (neither key is in the auto catalog for unrelated reasons).

- [ ] **Step 3: Verify both placeholders are in the output catalog**

Run:
```bash
uv run python -c "
import json
c = json.load(open('catalog.json'))
for k in ['Reports:NEXT_DAY_OFFER_ENERGY)SPARSE', 'Reports:DispatchIS_FCAS_Fix']:
    ds = c['datasets'].get(k)
    assert ds is not None, f'missing {k}'
    assert ds['resolvable'] is False
    assert 'ARCHIVE' in ds['tiers']
    assert 'curated_only' not in ds, f'{k} leaked curated_only into catalog.json'
    print(f'{k}: OK')
"
```

Expected: both lines print `OK`.

- [ ] **Step 4: Verify the catalog still validates against the schema**

Run:
```bash
uv run python -c "
import json, jsonschema
schema = json.load(open('schemas/catalog.schema.json'))
data = json.load(open('catalog.json'))
jsonschema.validate(data, schema)
print('catalog.json: schema valid')
"
```

Expected: `catalog.json: schema valid`.

---

### Task 12: Full verification

**Files:** none modified in this task.

- [ ] **Step 1: Run the full test suite**

Run: `uv run pytest tests/ 2>&1 | tail -5`

Expected: `82 passed` (78 pre-B2 + 4 new B2 tests).

- [ ] **Step 2: Run mypy strict on src/**

Run: `uv run mypy --strict src/ 2>&1 | tail -3`

Expected: `Success: no issues found in 4 source files`.

- [ ] **Step 3: Confirm schema validation still works end-to-end**

Run: `uv run pytest tests/test_schema_validation.py -v 2>&1 | tail -10`

Expected: all schema tests pass.

- [ ] **Step 4: Confirm the catalog's `raw_keys` includes the placeholders**

Run:
```bash
uv run python -c "
import json
c = json.load(open('catalog.json'))
expected = {'Reports:NEXT_DAY_OFFER_ENERGY)SPARSE', 'Reports:DispatchIS_FCAS_Fix'}
assert all(k in c['datasets'] for k in expected), 'placeholders missing from datasets'
assert all(k in c['raw_keys'] for k in expected), 'placeholders missing from raw_keys'
# dataset_keys is the curated user-facing subset (resolvable=true only).
# Placeholders with resolvable=false are intentionally NOT in dataset_keys —
# they show up in list_datasets(include_raw=True) instead.
assert not any(k in c['dataset_keys'] for k in expected), (
    'resolvable=false placeholders should not appear in dataset_keys'
)
print('raw_keys discoverability: OK')
"
```

Expected: `raw_keys discoverability: OK`. With `_insert_curated_only` appending to `raw_keys` (Task 6 Step 1), placeholders are now discoverable via `catalog.list_datasets(include_raw=True)`. They stay out of `dataset_keys` because `resolvable: false` excludes them from the user-facing curated list — by design.

---

### Task 13: Commit

**Files:** all B2 changes staged together in one atomic commit.

- [ ] **Step 1: Stage the changes**

Run:
```bash
git add \
  scripts/merge_catalog.py \
  tests/test_merge_catalog.py \
  patterns/curated/reports.yaml \
  patterns/curated/README.md \
  .github/workflows/weekly-refresh.yml \
  catalog.json
git status --short
```

Expected: all 6 files show `M` status.

- [ ] **Step 2: Confirm no other unexpected files got staged**

Run: `git diff --cached --stat`

Expected: only the files listed in Step 1. No `patterns/auto/catalog.json` (gitignored), no `reference/URL-CONVENTIONS.*` unless they changed (they may if the extractor ran — that's fine, add them if so).

- [ ] **Step 3: Commit**

Use this commit message verbatim (HEREDOC preserves blank lines):

```bash
git commit -m "$(cat <<'EOF'
fix(merge): disambiguate placeholder vs override; drop orphan-fail counter

Before: scripts/merge_catalog.py treated every curated YAML entry whose
key was absent from the auto catalog as an "orphan." It warned on the
first run and required a 2-run tolerance via .github/orphan-fail-count.txt
before failing. The counter was broken — the workflow wrote to the file
only after continue-on-error absorbed the merge failure, and the file
was never committed back, so the counter always read as 0.

Worse, the "orphan" category silently covered two incompatible cases:
intentional placeholder entries (AEMO directories that exist with zero
files, like NEXT_DAY_OFFER_ENERGY)SPARSE and DispatchIS_FCAS_Fix) and
actual AEMO deletions of datasets we previously overrode. The merge
treated both the same, producing weekly noise for the placeholders
while giving no real signal for deletions.

After: YAML entries with `curated_only: true` are placeholders. They
insert into the catalog as-is, derive repo/intra_repo_id from the
{repo}:{intra_repo_id} key, require a full tiers block, and trigger
schema validation like any other record. If the key also exists in auto,
the curated record wins and a warning is emitted.

YAML entries without `curated_only` are overrides. If the auto entry
is missing, merge() fails immediately with a clear message naming the
key and identifying it as a suspected AEMO deletion. No counter. No
tolerance. No commit-dance.

The 2 known placeholder entries (NEXT_DAY_OFFER_ENERGY)SPARSE and
DispatchIS_FCAS_Fix) now carry curated_only: true and full ARCHIVE
tier blocks with filename_template: null. Both directories exist on
NEMWEB with zero files (verified 2026-04-19 against local
nemweb-mirror and live NEMWEB listing via curl). They ship in
catalog.json in datasets + raw_keys so users find them via
list_datasets(include_raw=True).

Workflow simplified: the orphan-tracking step, the counter-update step,
continue-on-error, and the --prior-fail-count CLI flag are all removed.
The merge step now exits non-zero on any unmarked orphan; workflow
fails; weekly PR isn't created; a human investigates.

Tests: 4 new unit tests in tests/test_merge_catalog.py cover (a)
curated_only placeholder insert, (b) override missing auto fails
immediately, (c) curated_only shadows auto with warning, (d)
curated_only missing tiers fails schema validation. _run_merge helper
updated to drop the removed --prior-fail-count flag.

82 passed, mypy strict clean on src/.

Design: /gstack-plan-eng-review (see
~/.gstack/projects/ZhipengHe-nem-catalog/zhipenghe-worktree-v0.1-implementation-b2-eng-review-20260419-162415.md)
during v0.1 pre-merge pass (B2).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 4: Confirm commit landed**

Run: `git log --oneline -5`

Expected: top commit is the B2 commit. Below it in order: `3d68931` (B5), `0fe3d3f` (B1b), `8a1611b` (B1), `a84b18e` (B4).

---

## Follow-ups (not in this plan)

These are flagged for a follow-up PR or the next milestone, NOT for this plan:

1. **Surface placeholders in `dataset_keys`.** Today they only appear in `raw_keys` (added by `_insert_curated_only` in this plan) and in `datasets`. `dataset_keys` is the user-facing curated subset and excludes anything with `resolvable: false` — that's the correct v0.1 behavior. If a future milestone wants resolvable=false entries to appear in `list_datasets()` default output, revisit the `_curate_keys` rule in `scripts/extract_patterns.py`.
2. **Extractor does not emit empty-listing records into the JSON catalog.** Today it only flags them in MD/CSV. The curated YAML is currently the sole home for placeholder entries. If AEMO adds a new empty-directory anomaly, the curator has to notice and author a YAML entry. A future improvement could have the extractor surface unknown empty listings as a warning.

---

## Traceability Matrix — Design Decisions → Tasks

Every load-bearing decision from the design doc maps to at least one task here.

| Design Decision | Quote / Source | Task(s) |
|---|---|---|
| Add `curated_only: true` marker | "Marker semantics" section | Task 2 (RED), Task 6 (GREEN) |
| Marked entries insert with repo/intra_repo_id derived from key | "merge() logic" pseudocode | Task 2, Task 6 (Step 1 — `_insert_curated_only`) |
| Marked entries require `tiers` in YAML (schema catches omissions) | "Marker semantics" required fields | Task 5 (RED), Task 6 (Step 4 — schema validation path) |
| Unmarked curated entries are overrides | "merge() logic" pseudocode | Task 6 (Step 1 — override path preserved) |
| Override + missing auto → fail immediately (no counter) | Eureka block | Task 3 (RED), Task 6 (Step 1 — SystemExit on missing_auto_orphans) |
| Fail counter eliminated (counter state file, workflow block) | Eureka block | Task 6 (Step 4 — `--prior-fail-count` dropped from main()), Task 10 (Step 1 — workflow block removed) |
| `curated_only: true` + key in auto → warn + curated wins | "merge() logic" pseudocode | Task 4 (RED), Task 6 (Step 1 — `_insert_curated_only` warn branch) |
| `curated_only` YAML marker never appears in emitted catalog.json | "Not in scope" schema decision | Task 2 (assertion), Task 6 (Step 1 — `k != "curated_only"` filter in record dict-comp) |
| Placeholders ship in catalog so users find them via search | "The 2 known curated entries" #1 | Task 6 (Step 1 — append to `raw_keys`), Task 12 (Step 4 — discoverability assertion) |
| `NEXT_DAY_OFFER_ENERGY)SPARSE` full block | "The 2 known curated entries" #1 | Task 8 (Step 1) |
| `DispatchIS_FCAS_Fix` is a legitimate placeholder (zero files, verified) | "Ground-truth facts" (mirror) + "decision here depends on ground-truth check during implementation" (live) | Task 7 (Steps 1-2 — live NEMWEB curl verification), Task 8 (Step 1 — block #2) |
| README.md merge-semantics section updated to reflect new rules | "DRY is important" user preference + changed merge surface | Task 9 |
| Workflow loses 20+ lines, becomes clean Extract → Merge | "Workflow changes" code block | Task 10 |
| Regenerated catalog.json contains both placeholders | "Acceptance criteria" | Task 11 (Step 3 — explicit assertion script) |
| No schema version bump | "Not in scope" | Schema unchanged across all tasks |
| No backward compat for `--prior-fail-count` | "Not in scope" | Task 6 (Step 4 — flag removed outright) |
| Extractor unchanged | "Not in scope" | No task touches `scripts/extract_patterns.py` |

**Gap check:** every design decision has at least one task. Every task maps to at least one design decision or is a verification step (Tasks 1, 7, 12, 13).

---

## Self-Review Notes

- **Spec coverage:** Traceability matrix above. No gaps. Plan revised after Codex alignment audit (MAJOR DRIFT → patched → re-audited).
- **Placeholder scan:** Every task has concrete code blocks and exact commands. No TBDs. The "investigate the cause" phrasing in the commit message refers to human action on merge failure, not a placeholder in the plan.
- **Type consistency:** `_insert_curated_only` signature takes `(key, overlay, merged, warnings)` — matches the call site in `merge()`. `missing_auto_orphans` uses `list[str]` consistently. `merge()` drops `prior_fail_count` parameter; `_run_merge` helper drops `--prior-fail-count` CLI arg; `main()` drops the argparse flag.
- **Execution order:** Task 6 updates the `_run_merge` test helper (Step 3) BEFORE updating `main()` (Step 4) so the test suite keeps passing across the transition. Task 7 (live NEMWEB verification) is a checkpoint before Task 8 (YAML edit) — if the live check contradicts the mirror check, Task 8 is PAUSED.
- **Linear execution:** Tasks 1 → 13 run in order. Single atomic commit at Task 13 groups the full change.
