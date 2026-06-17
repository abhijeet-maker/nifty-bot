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

## 2026-06-17 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.19% | **Alpha today:** -0.19%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Book remains 100% cash. No pre-market routine fired today (last journal entry 2026-05-22 — 26-day gap; cron/scheduler likely missed runs). Nifty 50 closed 24,035.70 (+0.19%); flat book = -0.19% relative for the session, immaterial in absolute terms. Open agent housekeeping still pending: (1) VEDL DMA-divergence (3 cycles unresolved, suspected unadjusted corp action in nse.sh history), (2) UNIVERSE last rebuilt 2026-05-06, now 42 days stale — overdue. Tomorrow watchlist empty pending a fresh pre-market scan.
