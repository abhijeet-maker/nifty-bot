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

## 2026-06-15 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.90% | **Alpha today:** -0.90%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** No EOD routine has fired since the Day 0 seed; portfolio is 100% cash and was so on every prior pre-market scan (last journal entry 2026-05-22). Nifty 50 closed 23,622.90 (+0.90%), a strong up day, so sitting in cash cost -0.90% of relative performance. No positions to mark, no trades to log. Capital preservation intact; opportunity cost mounting. Tomorrow's pre-market scan should re-check whether any UNIVERSE leaders (notably ADANIPOWER) have rotated into the 12-1 pullback window after this rally, and whether VEDL DMA-divergence has been reconciled by the weekly review.
