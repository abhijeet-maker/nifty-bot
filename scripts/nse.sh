#!/usr/bin/env bash
# NSE + Yahoo Finance wrapper for Indian equity price data.
# Usage:
#   bash scripts/nse.sh quote RELIANCE         -> last price, OHLC, delivery %
#   bash scripts/nse.sh history RELIANCE 250   -> 250 days of closes (for 12-1 momentum)
#   bash scripts/nse.sh earnings 2026-04-21    -> companies reporting on that date
#
# quote/earnings use nsepython (handles NSE cookie auth internally).
# history uses Yahoo Finance v8 chart API (v7 download is deprecated).

set -euo pipefail
ROOT="$(dirname "$(git -C "$(dirname "$0")" rev-parse --git-common-dir)")"
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

PYTHON="${PYTHON:-python}"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

cmd="${1:-}"
shift || true

case "$cmd" in
  quote)
    sym="${1:?usage: quote SYMBOL}"
    "$PYTHON" - "$sym" <<'PYEOF'
import sys, json
from nsepython import nse_eq
sym = sys.argv[1]
d = nse_eq(sym)
p = d.get('priceInfo', {})
info = d.get('info', {})
ind = d.get('industryInfo', {})
print(json.dumps({
  'symbol': info.get('symbol'),
  'name': info.get('companyName'),
  'sector': ind.get('industry'),
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
PYEOF
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
    date_arg="${1:-$(date +%Y-%m-%d)}"
    "$PYTHON" - "$date_arg" <<'PYEOF'
import sys, json
from nsepython import nse_results
date_arg = sys.argv[1]  # YYYY-MM-DD
# nse_results returns a DataFrame of all filed results; filter by broadCastDate
df = nse_results('equities', 'Quarterly')
# broadCastDate format: "DD-Mon-YYYY HH:MM:SS"
import datetime
try:
    target = datetime.datetime.strptime(date_arg, '%Y-%m-%d').date()
except Exception:
    print('[]'); sys.exit(0)

out = []
for _, row in df.iterrows():
    try:
        bd = datetime.datetime.strptime(str(row.get('broadCastDate', '')).strip(), '%d-%b-%Y %H:%M:%S').date()
    except Exception:
        continue
    if bd == target:
        out.append({
            'symbol': row.get('symbol'),
            'company': row.get('companyName'),
            'period': row.get('period'),
            'broadcast': str(row.get('broadCastDate', '')),
        })
print(json.dumps(out, indent=2))
PYEOF
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
