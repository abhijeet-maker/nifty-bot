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

## 2026-05-29 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.03% | **Alpha today:** +0.03%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Flat day at the index level — Nifty 50 closed 23,907.15 (-0.03%), Bank Nifty 54,853.85 (-0.43%). Book remains 100% cash; no positions to mark. Week closes with 0 trades — all UNIVERSE candidates failed entry gates across this week's pre-market scans (most leaders below 50DMA; ADANIPOWER sitting at 20DMA, not in pullback zone). Weekend weekly-review routine should rebuild UNIVERSE (last refreshed 2026-05-06, now 23 days stale) and reconcile the long-running VEDL DMA-divergence flag. Monday watch: any post-results PEAD candidates from Friday filings.
