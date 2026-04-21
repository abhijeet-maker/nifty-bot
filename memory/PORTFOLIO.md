# Portfolio — Current Open Positions

**Mode:** PAPER TRADING  
**Started:** [SET ON DAY 0 FIRST RUN]  
**Starting capital:** ₹5,00,000.00

## Account state

| Field | Value |
|---|---|
| Paper equity (total) | ₹5,00,000.00 |
| Cash available | ₹5,00,000.00 |
| Deployed | ₹0.00 (0%) |
| Open positions | 0 of 5 max |
| Trades this week | 0 of 2 max |
| Week-start (Monday) | [updated weekly] |

## Open positions

| Symbol | Sector | Qty | Entry fill | Stop | Target | Entry date | Thesis tag |
|---|---|---|---|---|---|---|---|
| _none — paper trading begins on first pre-market after seed commit_ | | | | | | | |

## Format notes for the agent

- **Entry fill** is the slippage-adjusted fill price from `paper.sh`, NOT the quoted price
- **Stop** is 8% below entry_fill initially. Tightened at midday per STRATEGY.md
- **Target** is the first trail-tighten trigger level (entry × 1.20)
- **Thesis tag** is one of: `PEAD-<quarter>-beat`, `MOM-<sector>-pullback`, or
  a specific catalyst shortcode
- Update the **account state** table at every write (market-open fill, midday exit, EOD close)
- Recompute `Paper equity` = Cash + Σ(qty × current_close) every EOD
- Recompute `Deployed %` = (equity - cash) / equity

## Sector cap tracker

To enforce the max-2-per-sector rule, quick reference:

| Sector | Current count |
|---|---|
| Financials | 0 |
| IT | 0 |
| FMCG | 0 |
| Auto | 0 |
| Pharma | 0 |
| Metals | 0 |
| Energy | 0 |
| Cement | 0 |
| Consumer Discretionary | 0 |
| Industrials | 0 |
| Telecom | 0 |
| Utilities | 0 |
| Real Estate | 0 |
