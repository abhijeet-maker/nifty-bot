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

## 2026-05-15 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%  
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.21% | **Alpha today:** -0.21%  
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Flat day — no positions, no trades. Nifty 50 closed 23,740.50 (+0.21%); Bank Nifty in recovery mode, resistance 55,000. No pre-market routine fired this morning so no candidates were evaluated; weekly review (Friday) should re-screen UNIVERSE since the last live data showed several names (VEDL, BEL) failing DMA gates that the cached file said passed. Paper book has been idle since the 2026-05-06 pre-market HOLD — patience is fine, but verify the cron schedule is still firing pre-market and that UNIVERSE staleness isn't the reason no triggers have been generated.
