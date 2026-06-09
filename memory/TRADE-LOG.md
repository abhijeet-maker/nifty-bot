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

## 2026-06-09 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.43% | **Alpha today:** -0.43%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** No positions, no trades. Book is flat cash. Nifty 50 closed 23,223 (+0.43%) — index up, cash drag = -0.43% alpha (expected for 0% deployed). Last pre-market entry in JOURNAL was 2026-05-22; multi-week gap in routine firings. Universe last rebuilt 2026-05-06 (34 days, severely overdue per 7-day refresh rule in STRATEGY). Tomorrow's priority: rebuild UNIVERSE.md before any candidate scan. VEDL DMA-divergence still open across 3 cycles, unresolved.
