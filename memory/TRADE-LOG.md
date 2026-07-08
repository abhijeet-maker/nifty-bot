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

## 2026-07-08 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** ~-0.5% (intraday ref, final close not reliably sourced) | **Alpha today:** ~+0.5%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none. Pre-market routine did not fire today (last journal entry 2026-06-29). No prior EOD since 2026-06-22 (16 calendar days / ~11 trading days of missed snapshots).

**Notes:** Second live EOD snapshot; book still 100% cash. Pre-market did NOT run today, so no entry evaluation happened — this is a process failure (routine dormancy), not a HOLD decision. Data-feed outage flagged 2026-06-29 appears unresolved: `nse.sh quote NIFTY` still returns all-null; Perplexity returned mutually inconsistent Nifty closes across calls today (24,398.70 flat vs 23,853.20 -2.29% vs 24,251 -0.60% intraday). Best-effort mid-session reading Nifty 50 -0.60% at 12pm IST + intraday drift down on US-Iran/oil headlines → estimating -0.5% for the day; alpha is only qualitative today. Book sat out another down-tape session — cash drag negligible when index is red, but the cumulative miss (0 trades since paper launch May 2026) is now the dominant risk. **Top priorities blocking next entry:** (1) fix `nse.sh quote` + `nse.sh history` (NSE nullquote + Yahoo 429); (2) rebuild UNIVERSE.md (now 63 days stale, last 2026-05-06); (3) get the pre-market routine firing daily again. ADANIPOWER still the standing setup from 2026-06-18 pending live technicals.
