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

## 2026-07-07 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.04% | **Alpha today:** +0.04%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none. Pre-market and market-open routines did not fire today (last journal entry 2026-06-29 — 8 trading days stale).

**Notes:** Second live EOD snapshot; book still 100% cash. Nifty 50 finished 24,420.20 (-0.04% vs 24,430.35), Bank Nifty 48,765.20 — a flat-red index session, so cash carries a +4 bp alpha today (trivial, but the sign flipped vs 2026-06-22). Cumulative opportunity-cost drag since launch remains real: Nifty 50 has round-tripped roughly flat over the 11 trading-day gap. Data-feed outage flagged 2026-06-29 is **still unresolved** — `nse.sh quote` returns all-nulls (nsepython broken) and `nse.sh history/momentum` gets Yahoo HTTP 429 across retries. Zero live technicals means the momentum-gate half of STRATEGY is unevaluable; any new entry decision is blocked until a feed engineer touches this. Perplexity remains functional for macro/narrative. Q1 FY27 reporting season starts 2026-07-09 (TCS pre-market) — the first real PEAD candidate flow of this phase is 48 hours away, and the feed outage will kneecap any post-print momentum-confirm math unless fixed by then. UNIVERSE.md is now 62 days stale (last rebuild 2026-05-06) — process risk still compounding.
