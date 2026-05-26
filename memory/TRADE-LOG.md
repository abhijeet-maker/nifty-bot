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

## 2026-05-26 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%  
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.21% | **Alpha today:** +0.21%  
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none. No pre-market routine fired today (no journal entry for 2026-05-26); no open positions to manage.

**Notes:** Tuesday session. Cash-only book, so day P&L is zero by definition; Nifty 50 closed near 23,980 (-0.21% vs Monday's 24,031), giving the idle book +0.21% notional alpha. Week-to-date (week of Mon 2026-05-25): 0 trades. UNIVERSE.md last rebuilt 2026-05-06 — still overdue per Friday weekly-review note. VEDL DMA-divergence remains open across 3+ cycles (suspected unadjusted corp action in nse.sh history). Tomorrow: pre-market routine should resume; check 2026-05-26 results calendar for any post-mkt PEAD candidates before Wednesday open.
