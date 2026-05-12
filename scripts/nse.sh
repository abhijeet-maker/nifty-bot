#!/usr/bin/env bash
# NSE + Yahoo Finance wrapper for Indian equity price data.
# Usage:
#   bash scripts/nse.sh quote RELIANCE         -> last price, OHLC, delivery %
#   bash scripts/nse.sh history RELIANCE 250   -> 250 days of closes (for 12-1 momentum)
#   bash scripts/nse.sh earnings 2026-04-21    -> companies reporting on that date
#
# quote uses Yahoo Finance v8 chart (NSE API is Akamai-blocked in this environment).
# earnings is unavailable; pre-market routine must use Perplexity for the earnings calendar.
# history/momentum use Yahoo Finance v8 chart API (v7 download is deprecated).

set -euo pipefail
ROOT="$(dirname "$(git -C "$(dirname "$0")" rev-parse --git-common-dir)")"
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

PYTHON="${PYTHON:-python3}"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

cmd="${1:-}"
shift || true

case "$cmd" in
  quote)
    # Yahoo Finance v8 chart (NSE API is Akamai-blocked; Yahoo covers all strategy-critical fields).
    # Fields not available via Yahoo: vwap, circuit limits, delivery % (not used in any gate check).
    sym="${1:?usage: quote SYMBOL}"
    curl -fsS -A "$UA" -H "Accept: application/json" \
      "https://query1.finance.yahoo.com/v8/finance/chart/${sym}.NS?interval=1d&range=5d" \
    | "$PYTHON" -c "
import sys, json
d = json.load(sys.stdin)
r = d['chart']['result'][0]
m = r['meta']
q = r['indicators']['quote'][0]
last = m.get('regularMarketPrice')
prev = m.get('chartPreviousClose')
change_pct = round((last - prev) / prev * 100, 2) if prev else None
print(json.dumps({
  'symbol': m.get('symbol', '').replace('.NS', ''),
  'name': m.get('longName') or m.get('shortName'),
  'sector': None,
  'last': last,
  'open': q['open'][-1] if q.get('open') else None,
  'high': m.get('regularMarketDayHigh'),
  'low': m.get('regularMarketDayLow'),
  'close_prev': prev,
  'change_pct': change_pct,
  'vwap': None,
  'week52_high': m.get('fiftyTwoWeekHigh'),
  'week52_low': m.get('fiftyTwoWeekLow'),
  'lower_circuit': None,
  'upper_circuit': None,
}, indent=2))
"
    ;;

  history)
    sym="${1:?usage: history SYMBOL DAYS}"
    days="${2:-300}"
    # Yahoo Finance v8 chart API (v7 /download is deprecated/auth-gated).
    # Request 2x calendar days to ensure we get enough trading days (markets closed ~30% of days).
    period2=$(date +%s)
    period1=$(( period2 - days * 2 * 86400 ))
    curl -fsS -A "$UA" \
      -H "Accept: application/json" \
      "https://query1.finance.yahoo.com/v8/finance/chart/${sym}.NS?interval=1d&period1=${period1}&period2=${period2}" \
    | python3 -c "
import json, sys, datetime
d = json.load(sys.stdin)
result = d['chart']['result'][0]
timestamps = result['timestamp']
closes = result['indicators']['quote'][0]['close']
volumes = result['indicators']['quote'][0]['volume']
out = []
for ts, c, v in zip(timestamps, closes, volumes):
    if c is None:
        continue
    date = datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
    out.append({'date': date, 'close': round(float(c), 2), 'volume': int(v or 0)})
print(json.dumps(out[-int('$days'):]))
"
    ;;

  earnings)
    # NSE API is Akamai-blocked in this environment — cannot fetch the results calendar.
    # Returns [] with a stderr warning. The pre-market routine must use Perplexity (query 3)
    # to get the earnings calendar: bash scripts/perplexity.sh "Q-results scheduled for $DATE..."
    date_arg="${1:-$(date +%Y-%m-%d)}"
    echo "WARN: nse.sh earnings is unavailable (NSE API blocked). Use Perplexity for earnings calendar on ${date_arg}." >&2
    echo "[]"
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
