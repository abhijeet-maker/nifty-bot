# Data Source Migration — Akamai & Yahoo Cookie Issues Fixed

## Problem

NSE and Yahoo Finance APIs were hitting bot-detection walls:

1. **NSE** — Akamai blocks `curl` from non-browser IPs, requiring sophisticated cookie rotation and UA spoofing
2. **Yahoo Finance** — v7 download endpoint requires `crumb` + `cookie` handshake, breaks simple `curl` calls
3. **Screener.in** — HTML parsing failed occasionally; cookie authentication was fragile

## Solution

### 1. NSE Data → `nsepython` Package
- Handles Akamai bot detection automatically
- Manages cookie rotation transparently
- Covers `quote` (price, OHLC, sector), `earnings` (results calendar)

### 2. Yahoo Finance → `yfinance` Package  
- Handles crumb + cookie handshake transparently
- More reliable than direct API calls
- Used for 250-day history (12-1 momentum calculation)

### 3. Screener.in → BeautifulSoup + Requests
- Robust HTML parsing instead of fragile regex
- Proper session + cookie management
- Graceful fallback on failures (exit code 4)

## Setup

### Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `nsepython` — NSE data with Akamai handling
- `yfinance` — Yahoo Finance with cookie/crumb handling
- `requests` + `beautifulsoup4` — Screener HTML parsing
- `requests-cache` — Optional caching layer

### Optional: Screener.in Session Cookie

For richer data on Screener (e.g., higher volume limits), set `SCREENER_SESSION`:

1. Log in to [screener.in](https://www.screener.in)
2. Open DevTools (F12) → **Application** → **Cookies** → `screener.in`
3. Copy the `sessionid` value
4. Set in `.env`:
   ```
   SCREENER_SESSION=your_sessionid_here
   ```

## File Structure

```
scripts/
├── nse.sh                    # Bash wrapper (delegated to Python)
├── screener.sh               # Bash wrapper (delegated to Python)
└── lib/
    ├── nse_data.py           # NSE + Yahoo data fetcher (Python)
    └── screener_data.py      # Screener fundamentals (Python)
```

## API Reference

### NSE Data
```bash
bash scripts/nse.sh quote RELIANCE        # → JSON: last, OHLC, sector
bash scripts/nse.sh history RELIANCE 250  # → JSON: [date, close, volume, ...]
bash scripts/nse.sh earnings 2026-04-21   # → JSON: [symbol, company, period, ...]
bash scripts/nse.sh momentum RELIANCE     # → JSON: mom_12_1_pct, DMA crossovers
```

### Screener Fundamentals
```bash
bash scripts/screener.sh RELIANCE         # → JSON: PE, ROCE, ROE, D/E, sector, ...
# Exit code 4 on failure (caller falls back to Perplexity)
```

## Error Handling

### NSE Failures
- `nsepython` auto-retries with backoff
- If quota hit, waits ~30s before retry
- Logs to stderr, exits 1 on hard failure

### Yahoo Finance Failures
- Rare (but can happen if Yahoo IP-bans you)
- Falls back gracefully with "insufficient history"
- No partial data returned

### Screener Failures
- Exits with code 4 on parse error
- Caller (routines) logs and excludes symbol from universe
- Logs error details to stderr

## Troubleshooting

### `ModuleNotFoundError: No module named 'nsepython'`
```bash
pip install -r requirements.txt
# Verify: python3 -c "import nsepython; print('OK')"
```

### `nsepython` quota hit (rate-limiting)
- NSE free tier has ~10 req/min limit
- Script waits 30s and retries
- For production, consider [Upstox](https://upstox.com) or [Zerodha Kite](https://kite.trade) APIs (free tier available)

### Screener session expired
- Clear `SCREENER_SESSION` from `.env`
- Script falls back to free tier (works for most symbols)
- Update cookie if you need paid-tier richer data

### Yahoo Finance returns no data
- Usually means symbol is not found or delisted
- Script logs error and exits
- Verify symbol format: `RELIANCE`, `INFY`, etc. (NSE listing)

## Testing

```bash
# Test NSE quote
python3 scripts/lib/nse_data.py quote RELIANCE

# Test Yahoo history
python3 scripts/lib/nse_data.py history RELIANCE 250

# Test Screener
python3 scripts/lib/screener_data.py RELIANCE

# Or via bash wrappers
bash scripts/nse.sh quote INFY
bash scripts/screener.sh TCS
```

## Migration Notes

- Old `curl`-based approach removed (fragile, bot-detection prone)
- Bash wrappers preserved for compatibility
- Python modules handle all HTTP + auth
- Exit codes and JSON output format unchanged for backward compatibility
- No performance regression (Python overhead ~200ms per call, negligible)
