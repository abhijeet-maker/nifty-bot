# Universe — Quality-Filtered Nifty 100

This file is rebuilt every Friday by the weekly-review routine. Between rebuilds,
it is the ONLY tradable watchlist. If a ticker is not in the filtered table
below, it is NOT tradable this week, no matter how attractive it looks.

**Last rebuild:** 2026-04-20 (seed, pre-launch — REBUILD ON FIRST FRIDAY)

## Filtered tradable universe (passes quality screen)

Ranked by 12-1 month momentum. Regenerated weekly from screener.sh + nse.sh momentum.

| Symbol | Sector | ROCE% | ROE% | D/E | Pledge% | Mom 12-1% | Above 50DMA | Above 200DMA | Next Results |
|---|---|---|---|---|---|---|---|---|---|
| _SEED: this table is empty on day 0; will be populated by first weekly-review_ |

## How this gets populated

The weekly-review routine:
1. Iterates over `## Full Nifty 100 roster` below
2. Calls `bash scripts/screener.sh <SYM>` for each
3. Applies quality gate (ROCE>15, ROE>15, D/E<1 or <2 for financials, pledge<20)
4. Calls `bash scripts/nse.sh momentum <SYM>` on the survivors
5. Writes them back into the table above, ranked by mom_12_1_pct descending

Expect 30-45 names to survive the quality screen in a typical week.

## Full Nifty 100 roster (as of April 2026 — check composition quarterly)

This list is maintained manually. Nifty 100 reconstitutes semi-annually (March,
September). Verify against https://www.niftyindices.com/Factsheet/ind_nifty100list.csv
during weekly review.

ADANIENT, ADANIGREEN, ADANIPORTS, ADANIPOWER, AMBUJACEM, APOLLOHOSP, ASIANPAINT,
AXISBANK, BAJAJ-AUTO, BAJAJFINSV, BAJAJHLDNG, BAJFINANCE, BANKBARODA, BEL, BHARTIARTL,
BOSCHLTD, BPCL, BRITANNIA, CANBK, CGPOWER, CHOLAFIN, CIPLA, COALINDIA, DABUR,
DIVISLAB, DLF, DMART, DRREDDY, EICHERMOT, GAIL, GODREJCP, GRASIM, HAL, HAVELLS,
HCLTECH, HDFCBANK, HDFCLIFE, HEROMOTOCO, HINDALCO, HINDUNILVR, HINDZINC, ICICIBANK,
ICICIGI, ICICIPRULI, IDBI, INDHOTEL, INDIGO, INDUSINDBK, INFY, IOB, IOC, IRCTC,
IRFC, ITC, JINDALSTEL, JIOFIN, JSWENERGY, JSWSTEEL, KOTAKBANK, LICI, LODHA, LT,
LTIM, M&M, MARUTI, MOTHERSON, NAUKRI, NESTLEIND, NTPC, ONGC, PFC, PIDILITIND,
PNB, POWERGRID, RECLTD, RELIANCE, SBILIFE, SBIN, SHREECEM, SHRIRAMFIN, SIEMENS,
SRF, SUNPHARMA, TATACONSUM, TATAMOTORS, TATAPOWER, TATASTEEL, TCS, TECHM,
TITAN, TORNTPHARMA, TRENT, TVSMOTOR, ULTRACEMCO, UNIONBANK, VEDL, VBL, WIPRO, ZOMATO

## Notes
- Financial sector symbols that get the D/E < 2.0 exemption: HDFCBANK, ICICIBANK,
  SBIN, AXISBANK, KOTAKBANK, BANKBARODA, CANBK, PNB, INDUSINDBK, IDBI, IOB, UNIONBANK,
  BAJFINANCE, BAJAJFINSV, CHOLAFIN, SHRIRAMFIN, LICI, SBILIFE, HDFCLIFE, ICICIPRULI,
  ICICIGI, PFC, RECLTD, JIOFIN, IRFC, BAJAJHLDNG
- SME and newly-listed names with <4 quarters of data: skip regardless of ratios
