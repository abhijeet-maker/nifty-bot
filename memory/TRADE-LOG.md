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

## 2026-06-01 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%  
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.17% | **Alpha today:** +0.17%  
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Flat book, flat P&L. Nifty 50 closed 23,508.45 (-0.17%). No pre-market run today and no positions to mark; alpha is mechanical (cash beats a down tape). Week opens with 0/2 trade budget used. UNIVERSE.md last rebuilt 2026-05-06 (26 days, stale); VEDL DMA-divergence still unresolved across multiple cycles — Friday weekly review must rebuild UNIVERSE and reconcile VEDL history-feed issue. Tomorrow's watch: re-run pre-market scan; ADANIPOWER pullback into ₹205-215 remains the cleanest setup if it materializes.
