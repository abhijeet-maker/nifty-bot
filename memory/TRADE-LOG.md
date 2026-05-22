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

## 2026-05-22 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.02% | **Alpha today:** +0.02%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Week closes flat — zero trades, zero positions, full cash. Pre-market scan
rejected all candidates on DMA/pullback gates (VEDL/BEL/TITAN/HEROMOTOCO fail "above
both DMAs"; ADANIPOWER not in 2-7% pullback zone). Nifty 50 closed 23,654.70 (-0.02%
vs prev close 23,659.00) — a quiet Friday tape; the gap-down bias suggested by GIFT
Nifty (-199 pts) did not materialize at close. Bank Nifty close not reliably sourced.
Weekly review (Friday) is the next routine: must rebuild UNIVERSE (last rebuilt
2026-05-06, 16 days stale) and reconcile VEDL DMA divergence (suspected unadjusted
split/bonus in history feed inflating 12-1 momentum). Monday pre-market watchlist:
SUNPHARMA + EICHERMOT (results today post-market) for potential PEAD if both rev/EPS
beat AND close +3% on results day; check filings over the weekend.
