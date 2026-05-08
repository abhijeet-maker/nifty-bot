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

## 2026-05-08 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.66% | **Alpha today:** +0.66%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Flat book, all cash. Nifty 50 closed at 24,167.30 (-0.66%) reversing yesterday's near-flat session and testing support near 24,100-24,150. Zero exposure means we sidestepped today's drawdown — pure cash alpha. Pre-market on 2026-05-06 found no qualifying entries (VEDL/BEL failed DMA gate, ADANIPOWER too extended, empty PEAD calendar). No trades on 2026-05-07 either (no journal entry — likely no candidates). Tomorrow's focus: Friday weekly review will re-screen UNIVERSE and investigate the VEDL DMA divergence flagged Wednesday. Patience continues to be the right call when the universe isn't producing setups.
