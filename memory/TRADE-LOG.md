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

## 2026-06-29 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.14% | **Alpha today:** -0.14%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none. Pre-market routine fired and forced HOLD — zero PEAD candidates (no Nifty 100 prints Friday) and momentum gate unevaluable due to live-data outage (`nse.sh quote` returning all-null, Yahoo history 429-throttled).

**Notes:** Sixth consecutive cash session (7 calendar days, 4 trading days since last EOD on 2026-06-22). Nifty 50 +0.14% / Sensex +0.14% — flat green tape, opportunity-cost drag ≈ -₹700 today, ≈ -₹2,600 cumulative since launch. The book has not moved, but the operational risk surface has grown:
1. **Data feed outage is now blocking entries.** NSE quote endpoint returns nulls; Yahoo history is rate-limited. No live DMA / 12-1 momentum / 20-DMA pullback can be computed. Until both feeds are restored, the momentum trigger is inoperable and only PEAD entries (from cached fundamentals + Perplexity narrative) could fire — and the next earnings window doesn't open until July 9 (TCS).
2. **UNIVERSE.md is 54 days stale** (last rebuild 2026-05-06, ~7-8 Friday reviews missed). Stale ranking compounds the data outage — even if quotes return, rankings can't be trusted.
3. **ADANIPOWER** remains the only live pullback setup from 2026-06-18 — Screener snapshot price ₹226, but cannot independently confirm pullback zone or DMA gates without live history. Frozen on watchlist.
4. **VEDL data divergence** still open across 5 cycles (Yahoo unadjusted corporate action likely) — dependent on the same throttled history endpoint.

Tomorrow's priority: fix data feeds before evaluating any entry. No Nifty 100 results expected; reporting season starts in earnest 2026-07-09 (TCS).
