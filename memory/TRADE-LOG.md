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

## 2026-05-11 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%  
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** ~-1.0% (intraday proxy; same-day close not yet indexed by sources) | **Alpha today:** ~+1.0%  
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Monday open of a new trading week. Zero positions, 100% cash. Nifty 50 traded heavy through the session (intraday reads ~-0.9% to -1.2% off Friday's ₹24,176.15 close) — same-day close not yet indexed by Perplexity sources at run time, so the alpha figure is approximate; will be reconciled in Friday's weekly review. Cash position benefits relatively from a down-tape day. Tomorrow's focus: re-run pre-market scan against fresh UNIVERSE.md to find PEAD or 12-1 momentum-pullback setups; no positions to mark or trail.
