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

## 2026-05-25 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.27% | **Alpha today:** -0.27%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none. No pre-market routine fired (no journal entry for 2026-05-25). Book sat in cash through the session.
**Notes:** Nifty 50 closed 23,719.30 (+0.27%), Bank Nifty 54,055.35 (+1.15%) — financials led on the day. We held 100% cash, so we underperformed by the index gain (-0.27% alpha). Acceptable in context: entry gates have rejected every UNIVERSE candidate for the last three pre-market scans (2026-05-06, 05-19, 05-22), and chasing without a setup violates STRATEGY. Open watch items for tomorrow: SUNPHARMA + EICHERMOT post-results PEAD scan (reports filed Friday post-mkt 2026-05-22), and ADANIPOWER pullback into ₹205-215 zone. VEDL DMA-divergence + UNIVERSE staleness still flagged for the next weekly review.
