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

## 2026-06-03 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.43% | **Alpha today:** -0.43%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none.

**Notes:** Flat book, no positions held. Nifty 50 closed 23,483.55 (+0.43%) — book underperformed by 43 bps simply by being uninvested. No pre-market routine fired today (last journal entry 2026-05-22); week-to-date trade count 0 of 2 max. UNIVERSE last rebuilt 2026-05-06 — overdue for a refresh. ADANIPOWER, VEDL DMA-divergence flag, and post-results PEAD candidates from late May still pending the next pre-market scan. Tomorrow: re-engage the pre-market routine; if any UNIVERSE name reports tonight, check filings before open.
