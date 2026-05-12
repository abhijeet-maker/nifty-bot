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

## 2026-05-12 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -1.04% | **Alpha today:** +1.04%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Quiet book — zero positions, zero trades. Nifty 50 closed 23,569.50 (-1.04%), a broad risk-off session; staying in cash delivered +1.04% relative alpha by default. Pre-market scan on 2026-05-06 rejected all candidates (VEDL/BEL below DMAs, ADANIPOWER extended, empty earnings calendar). Universe needs a Friday re-screen — the VEDL DMA discrepancy is still unexplained. Watching for fresh PEAD set-ups from Q4 prints (BAJAJ-AUTO/GODREJCP reported post-market 2026-05-06) and any high-quality 12-1 names pulling back to 20DMA after today's drawdown.
