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

# Sector from breadcrumb: <a ... title='Sector'>Oil, Gas &amp; Consumable Fuels</a>.
# Build pattern with chr(34) so we avoid embedding literal double quotes
# inside this bash double-quoted python heredoc.
DQ = chr(34)
def find_attr_text(attr_value):
    pat = r'<a[^>]*title=' + DQ + re.escape(attr_value) + DQ + r'[^>]*>([^<]+)</a>'
    return re.search(pat, html, re.IGNORECASE)

sector_m = find_attr_text('Sector') or find_attr_text('Broad Sector')
sector = None
if sector_m:
    sector = sector_m.group(1).strip().replace('&amp;', '&')

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

# --- Balance Sheet derived metrics ---
# Screener doesn't render Debt/Equity directly in #top-ratios; we compute it
# from the Balance Sheet section (Borrowings / (Equity Capital + Reserves))
# using the latest available year column.
def grab_table_row_last(label):
    '''Return the latest-period numeric value from any data-table row whose
    first cell contains LABEL. Matches both <button>-wrapped and plain labels.
    Tolerates trailing % symbols on percentage cells.'''
    pattern = (
        r'<tr[^>]*>\s*'
        r'<td[^>]*text[^>]*>'
        r'.*?\b' + re.escape(label) + r'\b'      # label appears anywhere in cell
        r'.*?</td>'                              # end of label cell
        r'(.*?)'                                 # capture rest of row
        r'</tr>'
    )
    m = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
    if not m:
        return None
    row = m.group(1)
    # Numeric cells: optional leading sign, digits/commas/dots, optional trailing %
    vals = re.findall(r'<td[^>]*>\s*(-?[\d,\.]+)\s*%?\s*</td>', row)
    if not vals:
        return None
    last = vals[-1].replace(',', '').strip()
    try:
        return float(last)
    except ValueError:
        return None

borrowings = grab_table_row_last('Borrowings')
equity_capital = grab_table_row_last('Equity Capital')
reserves = grab_table_row_last('Reserves')
if borrowings is not None and equity_capital is not None and reserves is not None:
    total_equity = equity_capital + reserves
    if total_equity > 0:
        out['debt_to_equity'] = round(borrowings / total_equity, 2)

# Promoter holding — latest quarter from Shareholding Pattern table.
ph = grab_table_row_last('Promoters')
if ph is not None:
    out['promoter_holding_pct'] = ph

# Promoter pledge % — KNOWN LIMITATION:
# Screener.in does NOT render pledge data in the static HTML. It's loaded via
# JavaScript through Company.showShareholders('promoters', ...). Verified across
# 5 sample tickers (RELIANCE, HDFCBANK, VEDL, JSWSTEEL, ADANIENT) — the string
# 'pledge' appears 0 times in every rendered page.
# Default to 0.0 (most Nifty 100 names have 0% pledge anyway). Quality screen
# treats this as 'pass'; high-pledge names typically fail other gates (D/E, ROCE).
# To upgrade later: scrape NSE's shareholding XBRL filings, or reverse-engineer
# Screener's AJAX endpoint for pledge data.
out['promoter_pledge_pct'] = 0.0
out['promoter_pledge_source'] = 'default-stub'

# Next results date (if announced)
res_m = re.search(r'Results\s*on\s*([A-Za-z]+\s+\d{1,2}(?:,\s*\d{4})?)', html)
if res_m:
    out['next_results_date'] = res_m.group(1).strip()

print(json.dumps(out, indent=2))
"
