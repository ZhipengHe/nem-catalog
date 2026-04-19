#!/usr/bin/env bash
# Updates the "last successful crawl" shields.io badge in README.md after a successful refresh.
# Idempotent — safe to run repeatedly.
set -euo pipefail

DATE=$(date -u +%Y--%m--%d)  # shields.io escapes hyphens as -- for static badges
BADGE="[![Last successful crawl](https://img.shields.io/badge/last%20crawl-${DATE}-brightgreen)](https://github.com/ZhipengHe/nem-catalog/actions/workflows/weekly-refresh.yml)"

# Match the existing badge line regardless of current date or colour
python3 -c "
import re, pathlib
readme = pathlib.Path('README.md')
text = readme.read_text()
new_line = '''${BADGE}'''
pattern = r'\[\!\[Last successful crawl\].*?\)\]\(https://github\.com/[^)]+\)'
if re.search(pattern, text):
    text = re.sub(pattern, new_line, text)
else:
    raise SystemExit('README crawl badge not found — expected placeholder from Task 11')
readme.write_text(text)
print(f'Updated crawl badge to {new_line}')
"
