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

## 2026-06-10 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.51% | **Alpha today:** −0.51%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none — fully in cash_ | | | | | | | |

**Trades today:** none.
**This week (Mon 2026-06-08 → today):** 0 of 2 max.
**Notes:** Book is 100% cash; day P&L is flat by construction. Nifty 50 closed +0.51% at 23,242.10, Bank Nifty +2.09% at 55,194.50 — broad-based up day led by financials. Negative alpha today (−0.51%) is the cost of staying flat through an up tape; acceptable while UNIVERSE leaders fail entry gates. No pre-market routine fired today (last journal entry 2026-05-22), so no fresh candidate scan was done — flag for tomorrow's pre-market to rebuild context. Watchlist tomorrow: ADANIPOWER still the cleanest momentum setup pending a 2-7% pullback into ₹205-215 zone; VEDL DMA-divergence issue still open across multiple cycles, needs weekly review to reconcile suspected unadjusted corporate action in history feed.
