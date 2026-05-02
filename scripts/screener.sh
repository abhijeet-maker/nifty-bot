#!/usr/bin/env bash
# Screener.in wrapper for fundamental data. Scrapes the public HTML pages.
# If scraping fails, the agent should fall back to perplexity.sh with a
# specific structured query (see FALLBACK_HINT output).
#
# Usage:
#   bash scripts/screener.sh RELIANCE    -> JSON of key fundamentals
#
# Exits with code 4 if the page cannot be fetched or parsed, so callers
# can fall back to Perplexity.

set -euo pipefail
ROOT="$(dirname "$(git -C "$(dirname "$0")" rev-parse --git-common-dir)")"
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

sym="${1:-}"
if [[ -z "$sym" ]]; then
  echo "usage: bash scripts/screener.sh SYMBOL" >&2
  exit 1
fi

UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# Prefer consolidated (group-level) numbers over standalone.
URL="https://www.screener.in/company/${sym}/consolidated/"

COOKIE_ARG=""
if [[ -n "${SCREENER_SESSION:-}" ]]; then
  COOKIE_ARG="-H Cookie:sessionid=${SCREENER_SESSION}"
fi

HTML=$(curl -fsS -A "$UA" $COOKIE_ARG "$URL" 2>/dev/null || true)

if [[ -z "$HTML" ]] || [[ "$HTML" != *"company-ratios"* ]]; then
  # Try standalone as backup
  URL="https://www.screener.in/company/${sym}/"
  HTML=$(curl -fsS -A "$UA" $COOKIE_ARG "$URL" 2>/dev/null || true)
fi

if [[ -z "$HTML" ]] || [[ "$HTML" != *"company-ratios"* ]]; then
  echo "SCREENER_PARSE_FAILED symbol=$sym" >&2
  echo "This symbol will be excluded from the universe until Screener returns valid data." >&2
  echo "If many symbols fail in one run, the scraper parser is likely broken — check screener.sh." >&2
  exit 4
fi

# Extract the ratios block. Screener.in renders key ratios in a #top-ratios <ul>.
# We grep for the standard labels and extract the value text next to each.
echo "$HTML" | python3 -c "
import sys, re, json
html = sys.stdin.read()

def grab(label_pattern):
    # Screener structure: <li class='flex flex-space-between'><span class='name'>Label</span><span class='nowrap value'>...<span class='number'>VALUE</span>...</span></li>
    m = re.search(
        r'<li[^>]*>\s*<span[^>]*name[^>]*>\s*(?:' + label_pattern + r')\s*</span>.*?<span[^>]*number[^>]*>([^<]+)</span>',
        html, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip().replace(',', '')
    return None

def to_num(s):
    if s is None:
        return None
    s = s.replace('%', '').replace('₹','').replace(',','').strip()
    try:
        return float(s)
    except Exception:
        return None

# Sector from page header
sector_m = re.search(r'<small[^>]*>\s*<a[^>]*/company/compare/[^/]+/([^/]+)/\s*[^<]*</a>', html)
sector = sector_m.group(1).replace('-', ' ').title() if sector_m else None

out = {
    'symbol': '$sym',
    'source': 'screener.in',
    'url': '$URL',
    'market_cap_cr': to_num(grab(r'Market Cap')),
    'current_price': to_num(grab(r'Current Price')),
    'pe': to_num(grab(r'Stock P/E')),
    'book_value': to_num(grab(r'Book Value')),
    'dividend_yield_pct': to_num(grab(r'Dividend Yield')),
    'roce_pct': to_num(grab(r'ROCE')),
    'roe_pct': to_num(grab(r'ROE')),
    'face_value': to_num(grab(r'Face Value')),
    'sector': sector,
}

# Debt/Equity from the ratios section (may not be in top ratios for all companies)
de_m = re.search(r'Debt\s*/\s*Equity.*?<span[^>]*number[^>]*>([^<]+)</span>', html, re.DOTALL | re.IGNORECASE)
if de_m:
    out['debt_to_equity'] = to_num(de_m.group(1))

# Promoter holding
ph_m = re.search(r'>Promoters?\s*</td>.*?<td[^>]*>([^<]+)</td>', html, re.DOTALL | re.IGNORECASE)
if ph_m:
    out['promoter_holding_pct'] = to_num(ph_m.group(1))

# Pledged percentage (critical for quality screen)
pl_m = re.search(r'Pledg(?:ed)?\s*(?:percentage|%).*?<span[^>]*number[^>]*>([^<]+)</span>', html, re.DOTALL | re.IGNORECASE)
if pl_m:
    out['promoter_pledge_pct'] = to_num(pl_m.group(1))

# Next results date (if announced)
res_m = re.search(r'Results\s*on\s*([A-Za-z]+\s+\d{1,2}(?:,\s*\d{4})?)', html)
if res_m:
    out['next_results_date'] = res_m.group(1).strip()

print(json.dumps(out, indent=2))
"
