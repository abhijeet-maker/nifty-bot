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

## 2026-06-12 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.23% | **Alpha today:** +0.23%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none.
**Trades this week (Mon 2026-06-08 → Fri 2026-06-12):** 0 of 2 max.

**Notes:** No pre-market routine fired today; portfolio remains at seed state.
Nifty 50 closed 23,161.60 (-0.23%), Bank Nifty 55,176.75 (+0.14%). Holding cash
through a soft tape generated +0.23% relative alpha — but this is bookkeeping,
not skill. UNIVERSE was last rebuilt 2026-05-06 and is now 37 days stale; the
VEDL DMA-divergence flagged across three May cycles is still unresolved.
Weekend rebuild + reconciliation is the priority before Monday's pre-market.
