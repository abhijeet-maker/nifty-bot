#!/usr/bin/env bash
# NSE + Yahoo Finance wrapper for Indian equity price data.
# Usage:
#   bash scripts/nse.sh quote RELIANCE         -> last price, OHLC, delivery %
#   bash scripts/nse.sh history RELIANCE 250   -> 250 days of closes (for 12-1 momentum)
#   bash scripts/nse.sh earnings 2026-04-21    -> companies reporting on that date
#
# NSE endpoints require cookie priming (they 401 on first request).
# Yahoo Finance is used for history because NSE limits historical depth.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
COOKIE_JAR="/tmp/nse-cookies-$$.txt"
trap 'rm -f "$COOKIE_JAR"' EXIT

nse_prime() {
  # Hit the homepage first to get cookies NSE requires for API calls.
  curl -fsS -c "$COOKIE_JAR" -A "$UA" \
    -H "Accept: text/html,application/xhtml+xml" \
    -H "Accept-Language: en-US,en;q=0.9" \
    "https://www.nseindia.com/" > /dev/null
}

cmd="${1:-}"
shift || true

case "$cmd" in
  quote)
    sym="${1:?usage: quote SYMBOL}"
    nse_prime
    curl -fsS -b "$COOKIE_JAR" -A "$UA" \
      -H "Accept: application/json" \
      -H "Referer: https://www.nseindia.com/get-quotes/equity?symbol=${sym}" \
      "https://www.nseindia.com/api/quote-equity?symbol=${sym}" \
    | python3 -c "
import json, sys
d = json.load(sys.stdin)
p = d.get('priceInfo', {})
m = d.get('metadata', {})
print(json.dumps({
  'symbol': sym := d.get('info', {}).get('symbol'),
  'name': d.get('info', {}).get('companyName'),
  'sector': m.get('industry'),
  'last': p.get('lastPrice'),
  'open': p.get('open'),
  'high': p.get('intraDayHighLow', {}).get('max'),
  'low': p.get('intraDayHighLow', {}).get('min'),
  'close_prev': p.get('previousClose'),
  'change_pct': p.get('pChange'),
  'vwap': p.get('vwap'),
  'week52_high': p.get('weekHighLow', {}).get('max'),
  'week52_low': p.get('weekHighLow', {}).get('min'),
  'lower_circuit': p.get('lowerCP'),
  'upper_circuit': p.get('upperCP'),
}, indent=2))
"
    ;;

  history)
    sym="${1:?usage: history SYMBOL DAYS}"
    days="${2:-300}"
    # Yahoo Finance is more reliable for history. NSE's own historical API is rate-limited.
    # Add .NS suffix for NSE stocks.
    period2=$(date +%s)
    period1=$(( period2 - days * 86400 ))
    curl -fsS -A "$UA" \
      "https://query1.finance.yahoo.com/v7/finance/download/${sym}.NS?period1=${period1}&period2=${period2}&interval=1d&events=history" \
    | python3 -c "
import sys, csv, json
rows = list(csv.DictReader(sys.stdin))
out = [{'date': r['Date'], 'close': float(r['Close']), 'volume': int(float(r['Volume']))}
       for r in rows if r.get('Close') and r['Close'] != 'null']
print(json.dumps(out[-int('$days'):]))
"
    ;;

  earnings)
    date_arg="${1:-$(date +%Y-%m-%d)}"
    nse_prime
    # NSE results calendar - returns all companies reporting on a given date
    curl -fsS -b "$COOKIE_JAR" -A "$UA" \
      -H "Accept: application/json" \
      -H "Referer: https://www.nseindia.com/companies-listing/corporate-filings-financial-results" \
      "https://www.nseindia.com/api/corporates-financial-results?index=equities&from_date=${date_arg}&to_date=${date_arg}&period=Quarterly" \
    | python3 -c "
import json, sys
try:
  d = json.load(sys.stdin)
  out = [{'symbol': r.get('symbol'), 'company': r.get('companyName'),
          'period': r.get('period'), 'broadcast': r.get('broadcastTimestamp')}
         for r in d if r.get('symbol')]
  print(json.dumps(out, indent=2))
except Exception as e:
  print('[]')
"
    ;;

  momentum)
    # Compute 12-1 month momentum (return over past year, excluding last month).
    # Classic Jegadeesh-Titman signal. Used to rank the universe.
    sym="${1:?usage: momentum SYMBOL}"
    bash "$0" history "$sym" 260 | python3 -c "
import json, sys
h = json.load(sys.stdin)
if len(h) < 252:
    print(json.dumps({'symbol': '$sym', 'mom_12_1': None, 'reason': 'insufficient history'}))
    sys.exit(0)
# Price 252 days ago (12 months), price 21 days ago (1 month)
p_12m = h[-252]['close']
p_1m  = h[-21]['close']
mom = (p_1m - p_12m) / p_12m
# Also 50/200 DMA from today
import statistics
dma50  = statistics.mean(c['close'] for c in h[-50:])
dma200 = statistics.mean(c['close'] for c in h[-200:])
last = h[-1]['close']
print(json.dumps({
  'symbol': '$sym',
  'last': last,
  'mom_12_1_pct': round(mom*100, 2),
  'dma50': round(dma50, 2),
  'dma200': round(dma200, 2),
  'above_50dma': last > dma50,
  'above_200dma': last > dma200,
}, indent=2))
"
    ;;

  *)
    echo "Usage: bash scripts/nse.sh <quote|history|earnings|momentum> [args]" >&2
    exit 1
    ;;
esac
echo
