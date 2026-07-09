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

## 2026-07-09 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.57% (est., see notes) | **Alpha today:** -0.57%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none. Pre-market routine did not fire (last journal entry 2026-06-29).

**Notes:** 17 calendar days since last EOD snapshot (2026-06-22) — the routine cadence has broken down. Book still 100% cash through what looks like a modest Nifty 50 recovery day (~+0.57% intraday reference; sources conflicted, could not confirm the settled close tick). Yesterday (Jul 8) Nifty crashed -2.12% and Bank Nifty -2.51% on Iran-ceasefire-collapse crude spike — that drawdown was entirely avoided by being flat. Cumulative cash-drag vs Nifty over the missed 17 days is unquantified without daily prints, but is directionally negative given the index is roughly flat over the window with a large intraday round-trip. **Data-feed outage remains unresolved** (nse.sh quote → all-null, Yahoo history 429) per 2026-06-29 pre-market — this is now the dominant operational risk and the reason no entries can be vetted. **Three compounding process risks**: (1) data feeds down 10+ days, (2) UNIVERSE.md now ~64 days stale, (3) pre-market/EOD cadence has been missing. Fix feeds first, then rebuild universe, then resume routines.
