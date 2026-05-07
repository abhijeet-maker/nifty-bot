# Trade Log

Append-only ledger of every paper trade and every EOD portfolio snapshot.
Day-over-day P&L math depends on the most recent EOD snapshot in this file.

Format has two kinds of entries:
1. **Trade entries** — one per buy/sell. Full thesis + fill details.
2. **EOD snapshots** — one per trading day. Equity + open-positions table.

---

## Day 0 — Pre-launch baseline snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%  
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** N/A | **Alpha today:** N/A  
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Notes:** Seed state. Paper trading launches on the next pre-market routine firing.
The agent must treat this as "yesterday's equity" for its first day-over-day calculation.

---

## 2026-05-07 — EOD Snapshot
**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.34% | **Alpha today:** -0.34%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _no open positions_ | | | | | | | |

**Trades today:** none. Pre-market scan rejected all candidates (VEDL/BEL/ADANIPOWER failed DMA gate; PEAD scan returned empty).

**Notes:** Flat day for the book — 100% cash, missed Nifty's +0.34% session, so -0.34% relative. Acceptable: STRATEGY default is HOLD when no entry passes gates. BAJAJ-AUTO and GODREJCP reported Q4 post-market today (May 6) — tomorrow's pre-market must scan for PEAD setups on both. Also re-screen VEDL DMA divergence flagged yesterday. Nifty 50 close estimated at ~24,412 from intraday 3:30 PM tick (Perplexity post-close data not yet available); revise tomorrow if NSE official differs materially.
