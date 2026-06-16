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

## 2026-06-16 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.98% | **Alpha today:** -0.98%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Empty book carried into today; no positions to mark. Nifty 50 closed 23,853.90 (+0.98%) — a green tape, and we sat in cash, giving up the day to the index. That's the cost of the entry-gate discipline: no PEAD or 12-1 pullback setup has triggered since the last pre-market run on 2026-05-22 (25 calendar days ago). Long gap in routines is the real flag — pre-market and universe-refresh cadence has slipped; tomorrow's pre-market should rebuild UNIVERSE.md (last build 2026-05-06, ~6 weeks stale) and re-scan for setups against the new tape. Phase P&L unchanged at ₹0.
