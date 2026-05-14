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

## 2026-05-14 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** N/A | **Alpha today:** N/A
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Flat book, no trades. Last research entry in JOURNAL is 2026-05-06
pre-market (HOLD — zero candidates passed entry gates); no JOURNAL entries
2026-05-07 through 2026-05-14, so no daily DoD snapshots logged. Equity
unchanged at seed. Nifty 50 day-change unverifiable — perplexity returned
contradictory levels (23,412 vs 24,666); per STRATEGY rule, no narrative
fallback for numerical index data. Tomorrow: re-run pre-market scan; weekly
UNIVERSE refresh due Friday — investigate VEDL DMA discrepancy flagged
2026-05-06.
