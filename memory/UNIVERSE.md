# Universe — Quality-Filtered Nifty 100

This file is rebuilt every Friday by the weekly-review routine. Between rebuilds,
it is the ONLY tradable watchlist. If a ticker is not in the filtered table
below, it is NOT tradable this week, no matter how attractive it looks.

**Last rebuild:** 2026-04-24 (fundamentals fresh; momentum NOT refreshed 2026-05-01 — NSE API 403 on all endpoints)
**Quality screen pass count:** 40 of 95 (normal range 25-50 ✓ — no universe collapse)

## Filtered tradable universe (passes quality screen)

Ranked by 12-1 month momentum. Regenerated weekly from screener.sh + nse.sh momentum.
Skipped (no Screener data): LTIM, TATAMOTORS, TORNTPHARMA, ZOMATO

| Symbol | Sector | ROCE% | ROE% | D/E | Pledge% | Mom 12-1% | Above 50DMA | Above 200DMA | Next Results |
|---|---|---|---|---|---|---|---|---|---|
| VEDL | - | 25.3 | 38.5 | - | - | +56.75 | Yes | Yes | - |
| BEL | - | 38.9 | 29.2 | - | - | +35.19 | Yes | Yes | - |
| ADANIPOWER | - | 22.5 | 26.1 | - | - | +29.91 | Yes | Yes | - |
| HEROMOTOCO | - | 30.3 | 23.1 | - | - | +29.31 | No | No | - |
| TVSMOTOR | - | 15.4 | 28.4 | - | - | +24.74 | No | Yes | - |
| TITAN | - | 19.1 | 31.8 | - | - | +15.50 | Yes | Yes | - |
| EICHERMOT | - | 29.8 | 24.1 | - | - | +14.99 | No | Yes | - |
| COALINDIA | - | 48.0 | 38.9 | - | - | +13.67 | Yes | Yes | - |
| HINDZINC | - | 69.6 | 76.8 | - | - | +7.78 | Yes | Yes | - |
| DRREDDY | - | 22.7 | 18.0 | - | - | +6.45 | Yes | Yes | - |
| BAJAJ-AUTO | - | 28.1 | 22.8 | - | - | +6.41 | Yes | Yes | - |
| MARUTI | - | 21.7 | 15.9 | - | - | +5.19 | No | No | - |
| BOSCHLTD | - | 21.1 | 15.6 | - | - | +4.80 | Yes | No | - |
| CGPOWER | - | 37.5 | 27.7 | - | - | +2.08 | Yes | Yes | - |
| DIVISLAB | - | 20.4 | 15.4 | - | - | +2.07 | Yes | Yes | - |
| BRITANNIA | - | 53.0 | 52.9 | - | - | +1.79 | No | No | - |
| SUNPHARMA | - | 20.2 | 16.9 | - | - | +0.77 | No | No | - |
| TECHM | - | 23.1 | 17.6 | - | - | +0.76 | No | No | - |
| APOLLOHOSP | - | 16.6 | 18.4 | - | - | +0.04 | Yes | Yes | - |
| NESTLEIND | - | 85.4 | 74.3 | - | - | -2.74 | Yes | Yes | - |
| HCLTECH | - | 30.6 | 24.0 | - | - | -8.33 | No | No | - |
| LICI | - | 53.1 | 45.7 | - | - | -9.48 | No | No | - |
| BPCL | - | 16.2 | 17.3 | - | - | -10.77 | No | No | - |
| DABUR | - | 20.2 | 17.0 | - | - | -12.24 | No | No | - |
| HINDUNILVR | - | 27.8 | 20.7 | - | - | -12.71 | Yes | No | - |
| PIDILITIND | - | 29.8 | 23.0 | - | - | -12.90 | No | No | - |
| ASIANPAINT | - | 25.7 | 20.6 | - | - | -13.24 | Yes | No | - |
| INFY | - | 40.3 | 32.2 | - | - | -13.38 | No | No | - |
| HAL | - | 33.9 | 26.1 | - | - | -15.65 | Yes | No | - |
| GODREJCP | - | 19.2 | 15.2 | - | - | -17.39 | No | No | - |
| CIPLA | - | 22.7 | 17.8 | - | - | -19.14 | Yes | No | - |
| WIPRO | - | 17.9 | 15.5 | - | - | -21.35 | No | No | - |
| HAVELLS | - | 24.9 | 19.4 | - | - | -25.27 | No | No | - |
| INDIGO | - | 17.3 | 103.0 | - | - | -28.22 | No | No | - |
| TCS | - | 63.0 | 51.8 | - | - | -28.23 | No | No | - |
| VBL | - | 19.7 | 16.2 | - | - | -30.10 | Yes | Yes | - |
| INDHOTEL | - | 17.2 | 16.1 | - | - | -30.33 | No | No | - |
| ITC | - | 36.8 | 27.3 | - | - | -31.31 | No | No | - |
| IRCTC | - | 49.0 | 37.1 | - | - | -34.13 | No | No | - |
| TRENT | - | 27.8 | 27.9 | - | - | -37.38 | Yes | No | - |

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
