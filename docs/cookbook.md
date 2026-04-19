# nem-catalog cookbook (shell, R, Julia)

## Shell — expand a date range to URLs

```bash
# Given a dataset key and a date range, produce URLs for wget/curl.
CATALOG=$(curl -s https://zhipenghe.me/nem-catalog/catalog.json)
KEY="Reports:DispatchIS_Reports"

PATH_TMPL=$(echo "$CATALOG" | jq -r ".datasets[\"$KEY\"].tiers.ARCHIVE.path_template")
FILE_TMPL=$(echo "$CATALOG" | jq -r ".datasets[\"$KEY\"].tiers.ARCHIVE.filename_template")

for d in $(seq -f "%g" $(date -j -f "%Y-%m-%d" "2025-04-01" "+%s") 86400 $(date -j -f "%Y-%m-%d" "2025-04-07" "+%s")); do
  date_str=$(date -r $d "+%Y%m%d")
  echo "https://nemweb.com.au${PATH_TMPL}${FILE_TMPL//\{date\}/$date_str}"
done
```

## Shell — discover datasets by substring

```bash
curl -s https://zhipenghe.me/nem-catalog/catalog.json \
  | jq -r '.dataset_keys[] | select(. | ascii_downcase | contains("dispatch"))'
```

## Shell — check schema and catalog versions

```bash
curl -s https://zhipenghe.me/nem-catalog/catalog.json \
  | jq '{schema: .schema_version, catalog: .catalog_version, as_of}'
```

## R (no installed package) — use jsonlite

```r
library(jsonlite)
catalog <- fromJSON("https://zhipenghe.me/nem-catalog/catalog.json")
tier <- catalog$datasets$`Reports:DispatchIS_Reports`$tiers$ARCHIVE

dates <- seq(as.Date("2025-04-01"), as.Date("2025-04-07"), by="day")
urls <- sprintf(
  "https://nemweb.com.au%s%s",
  tier$path_template,
  sub("\\{date\\}", format(dates, "%Y%m%d"), tier$filename_template)
)
```

## Julia (no installed package) — use JSON3

```julia
using JSON3, HTTP
catalog = JSON3.read(String(HTTP.get("https://zhipenghe.me/nem-catalog/catalog.json").body))
tier = catalog.datasets["Reports:DispatchIS_Reports"].tiers.ARCHIVE

dates = collect(Date("2025-04-01"):Day(1):Date("2025-04-07"))
urls = ["https://nemweb.com.au" * tier.path_template *
        replace(tier.filename_template, "{date}" => Dates.format(d, "yyyymmdd"))
        for d in dates]
```

## Parallel download with xargs (shell)

```bash
# Build URL list, then download 4 at a time with wget.
curl -s https://zhipenghe.me/nem-catalog/catalog.json \
  | jq -r '.datasets["Reports:DispatchIS_Reports"].tiers.ARCHIVE | .path_template + .filename_template' \
  | head -1 \
  | while read tmpl; do
      for d in $(seq -f "%08g" 20250401 20250407); do
        echo "https://nemweb.com.au${tmpl//\{date\}/$d}"
      done
    done \
  | xargs -P 4 -n 1 wget -q
```
