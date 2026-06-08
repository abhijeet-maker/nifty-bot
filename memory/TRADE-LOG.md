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

## 2026-06-08 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** ~-0.7% (intraday; final close not yet on NSE EOD feed) | **Alpha today:** N/A (no positions)
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** First EOD snapshot since Day 0 baseline. 100% cash, no positions opened in the
launch window (pre-markets on 2026-05-06, 2026-05-19, 2026-05-22 all returned HOLD — every
UNIVERSE momentum leader failed the "above both DMAs" gate or was outside the 2-7% pullback
zone, and the PEAD scan returned empty). Index closed weak today (~-0.7% based on 10:50 IST
print of 23,204.25 vs Friday 23,366.70; final NSE EOD feed not yet posted at snapshot time).
Open issues carried forward: (i) VEDL DMA-divergence from UNIVERSE still unreconciled across
3 pre-market cycles — suspected unadjusted split/bonus in nse.sh history feed inflating
12-1 momentum and stale-DMAs; (ii) UNIVERSE.md last rebuilt 2026-05-06, well overdue; weekly
rebuild required. Watch tomorrow: any post-close earnings tonight (TBD via earnings calendar),
ADANIPOWER 20DMA pullback into ₹205-215 zone (still cleanest momentum setup, not yet in
window). No held names → no thesis-break or stop-trigger risk overnight.
