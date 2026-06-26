# Universe — Quality-Filtered Nifty 100

This file is rebuilt every Friday by the weekly-review routine. Between rebuilds,
it is the ONLY tradable watchlist. If a ticker is not in the filtered table
below, it is NOT tradable this week, no matter how attractive it looks.

**Last rebuild:** 2026-06-26 (fundamentals fresh from cache, 22-day-old; momentum/DMA columns STALE from 2026-05-06 — Yahoo Finance returned 429 on all momentum calls during this rebuild).
**Last momentum/DMA refresh:** 2026-05-06. Treat the Mom/DMA columns as **advisory only** — pre-market routine MUST recompute momentum + DMAs live for any candidate before applying the entry gate.

**Quality screen pass count:** 38 of 95 names with parseable Screener data (was 37 prior — LODHA newly added).

## Filtered tradable universe (passes quality screen)

Ranked by 12-1 month momentum where available (snapshot from 2026-05-06 — see staleness note above).
Skipped (no Screener data parsed): LTIM, TATAMOTORS, TORNTPHARMA, ZOMATO + BFSI subset where Screener parser does not extract ROCE/ROE/D/E (AXISBANK, BAJFINANCE, BANKBARODA, CANBK, CHOLAFIN, HDFCBANK, ICICIBANK, ICICIGI, IDBI, INDUSINDBK, IOB, IRFC, KOTAKBANK, PFC, PNB, RECLTD, SBILIFE, SBIN, SHRIRAMFIN, UNIONBANK). The BFSI gap is a known parser limitation — flag for `scripts/screener.sh` review.

**Excluded (data-suspect):** VEDL — 4 cycles of unresolved DMA divergence (50DMA ₹448 vs live ~₹306). Listed at the bottom of the table for visibility but **NOT tradable** until momentum source reconciled.

| Symbol | Sector | ROCE% | ROE% | D/E | Pledge% | Mom 12-1% (stale) | Above 50DMA (stale) | Above 200DMA (stale) | Next Results |
|---|---|---|---|---|---|---|---|---|---|
| BEL | Capital Goods | 38.9 | 29.2 | 0.0 | 0.0 | +35.19 | Yes | Yes | - |
| ADANIPOWER | Power | 17.3 | 21.2 | 0.84 | 0.0 | +29.91 | Yes | Yes | - |
| HEROMOTOCO | Automobile and Auto Components | 35.8 | 28.5 | 0.04 | 0.0 | +29.31 | No | No | - |
| TITAN | Consumer Durables | 19.1 | 31.8 | 0.97 | 0.0 | +15.50 | Yes | Yes | - |
| EICHERMOT | Automobile and Auto Components | 29.8 | 24.1 | 0.02 | 0.0 | +14.99 | No | Yes | - |
| COALINDIA | Oil, Gas & Consumable Fuels | 35.3 | 28.5 | 0.12 | 0.0 | +13.67 | Yes | Yes | - |
| HINDZINC | Metals & Mining | 69.6 | 76.8 | 0.39 | 0.0 | +7.78 | Yes | Yes | - |
| DRREDDY | Healthcare | 22.7 | 18.0 | 0.16 | 0.0 | +6.45 | Yes | Yes | - |
| BAJAJ-AUTO | Automobile and Auto Components | 28.1 | 22.8 | 0.58 | 0.0 | +6.41 | Yes | Yes | - |
| BOSCHLTD | Automobile and Auto Components | 21.1 | 15.6 | 0.01 | 0.0 | +4.80 | Yes | No | - |
| CGPOWER | Capital Goods | 37.5 | 27.7 | 0.02 | 0.0 | +2.08 | Yes | Yes | - |
| DIVISLAB | Healthcare | 20.4 | 15.4 | 0.01 | 0.0 | +2.07 | Yes | Yes | - |
| BRITANNIA | Fast Moving Consumer Goods | 53.0 | 52.9 | 0.59 | 0.0 | +1.79 | No | No | - |
| SUNPHARMA | Healthcare | 20.2 | 16.9 | 0.07 | 0.0 | +0.77 | No | No | - |
| TECHM | Information Technology | 23.1 | 17.6 | 0.07 | 0.0 | +0.76 | No | No | - |
| APOLLOHOSP | Healthcare | 16.6 | 18.4 | 0.88 | 0.0 | +0.04 | Yes | Yes | - |
| NESTLEIND | Fast Moving Consumer Goods | 85.4 | 74.3 | 0.09 | 0.0 | -2.74 | Yes | Yes | - |
| HCLTECH | Information Technology | 30.6 | 24.0 | 0.07 | 0.0 | -8.33 | No | No | - |
| LICI | Financial Services | 53.1 | 45.7 | 0.0 | 0.0 | -9.48 | No | No | - |
| BPCL | Oil, Gas & Consumable Fuels | 16.2 | 17.3 | 0.56 | 0.0 | -10.77 | No | No | - |
| DABUR | Fast Moving Consumer Goods | 20.2 | 17.0 | 0.12 | 0.0 | -12.24 | No | No | - |
| HINDUNILVR | Fast Moving Consumer Goods | 28.4 | 22.3 | 0.03 | 0.0 | -12.71 | Yes | No | - |
| PIDILITIND | Chemicals | 29.8 | 23.0 | 0.05 | 0.0 | -12.90 | No | No | - |
| ASIANPAINT | Consumer Durables | 25.7 | 20.6 | 0.18 | 0.0 | -13.24 | Yes | No | - |
| INFY | Information Technology | 40.0 | 31.9 | 0.1 | 0.0 | -13.38 | No | No | - |
| HAL | Capital Goods | 33.9 | 26.1 | 0.0 | 0.0 | -15.65 | Yes | No | - |
| GODREJCP | Fast Moving Consumer Goods | 19.2 | 15.2 | 0.34 | 0.0 | -17.39 | No | No | - |
| CIPLA | Healthcare | 22.7 | 17.8 | 0.01 | 0.0 | -19.14 | Yes | No | - |
| WIPRO | Information Technology | 17.9 | 15.5 | 0.23 | 0.0 | -21.35 | No | No | - |
| HAVELLS | Consumer Durables | 24.9 | 19.4 | 0.03 | 0.0 | -25.27 | No | No | - |
| TCS | Information Technology | 63.0 | 51.8 | 0.11 | 0.0 | -28.23 | No | No | - |
| VBL | Fast Moving Consumer Goods | 19.7 | 16.2 | 0.13 | 0.0 | -30.10 | Yes | Yes | - |
| INDHOTEL | Consumer Services | 17.2 | 16.1 | 0.28 | 0.0 | -30.33 | No | No | - |
| ITC | Fast Moving Consumer Goods | 36.8 | 27.3 | 0.01 | 0.0 | -31.31 | No | No | - |
| IRCTC | Consumer Services | 49.0 | 37.1 | 0.02 | 0.0 | -34.13 | No | No | - |
| TRENT | Consumer Services | 27.8 | 27.9 | 0.37 | 0.0 | -37.38 | Yes | No | - |
| LODHA | Realty | 16.6 | 15.8 | 0.42 | 0.0 | N/A | N/A | N/A | - |
| ~~VEDL~~ | Metals & Mining | 16.5 | 19.0 | 0.56 | 0.0 | (data-suspect, excluded) | — | — | - |


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
