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

## 2026-05-21 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.17% | **Alpha today:** -0.17%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Flat day on a cash-only book. Nifty 50 closed 23,659 (+0.17%); Bank Nifty close unverifiable from sources. Negative alpha by construction — sitting in cash on an up tape. No journal entries logged for 2026-05-20 (routine likely missed). No candidates passed entry gates at the last pre-market scan (2026-05-19); UNIVERSE leaders broadly remain below 50DMA. Watching ADANIPOWER for a 2-7% pullback under its 20DMA and post-results PEAD setups from BEL/BPCL (results May 19). VEDL DMA-history divergence remains open for Friday weekly review.
