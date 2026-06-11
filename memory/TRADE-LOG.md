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

## 2026-06-11 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.04% | **Alpha today:** -0.04%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none.

**Notes:** First EOD snapshot since Day 0 seed; bot dormant 20 trading days (last journal entry 2026-05-22). Book remains 100% cash, zero positions opened. Nifty 50 closed 23,223.30, ~flat (+0.04%); Bank Nifty close not reliably sourced. No entries this week (0 of 2 max). Strategy gate continues to reject: top UNIVERSE momentum leaders (VEDL, BEL, HEROMOTOCO, TITAN, EICHERMOT) have been below 50DMA across recent scans, and ADANIPOWER — the one technical leader — has stayed sitting at its 20DMA rather than pulling back into the 2-7% entry zone. UNIVERSE.md was last rebuilt 2026-05-06 and is overdue; weekly review must rebuild and reconcile the VEDL DMA-divergence (suspected unadjusted corporate action in history feed) before next pre-market scan can trust the rankings.
