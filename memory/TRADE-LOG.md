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

## 2026-06-22 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.38% | **Alpha today:** -0.38%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none. Pre-market routine did not fire today (last journal entry 2026-06-18).

**Notes:** First live EOD snapshot. Book sat in 100% cash through a +0.38% Nifty 50 / +0.61% Bank Nifty session — opportunity-cost drag of -₹1,900 vs a fully-deployed index proxy, but consistent with STRATEGY.md (no candidate has cleared all gates since launch). ADANIPOWER remains the only live pullback setup flagged 2026-06-18; sector confirm and live pullback zone need re-checking in tomorrow's pre-market. UNIVERSE.md is 47 days stale — rebuild is overdue and is the single biggest process risk going into the next entry decision.

---

## 2026-07-06 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** ~+0.73% (intraday last 24,447 vs Fri close 24,270.85; final tick not yet indexed) | **Alpha today:** ~-0.73% (cash drag)
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none. No pre-market routine fired today; no market-open or midday actions logged in JOURNAL for 2026-07-06. Book has been 100% cash since launch.

**Notes:** Second live EOD snapshot (14 calendar days since 2026-06-22). Cash-drag against a ~+0.7% Nifty 50 tape today — small, but the pattern is now persistent: the routine has not opened a single position since Day 0 and has skipped ~9 EOD writes in that window, so this snapshot is effectively re-anchoring the ledger, not tracking day-over-day P&L. Root cause is unchanged from 2026-06-29: (a) `nse.sh quote` still returns all-null JSON (nsepython broken); (b) Yahoo history feed durably 429-throttled from this container IP; (c) UNIVERSE.md is 61 days stale (last rebuild 2026-05-06); (d) no PEAD candidates through Jul 3 — Q1 FY27 season starts with TCS on Jul 9. Fixing the two feed wrappers is now blocking every downstream decision. Nifty 50 close cited from Perplexity intraday last (~24,447, +0.73%) because I could not pull an authoritative post-3:30 PM IST print; treat with the standard ±5-10 bp caveat for the closing auction. Bank Nifty close not sourced this cycle.
