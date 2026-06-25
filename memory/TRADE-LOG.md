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

## 2026-06-25 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** ≈+0.4% (per Perplexity; exact official close unverified) | **Alpha today:** ≈-0.4%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none. Pre-market routine did not fire today (last journal entry 2026-06-18; no Jun 23/24 EOD snapshots either — cron skipped Tue/Wed).

**Notes:** Book sat in 100% cash for a 3rd consecutive recorded session. Nifty 50 closed up roughly +0.4% (sources disagreed on exact figure; intraday read showed +0.96% at 12:13 PM IST then a fade — official close not cleanly available from `perplexity.sh` yet). Cumulative cash drag since 2026-06-22 EOD now ~-1.2% to -1.5% of equity vs Nifty proxy. ADANIPOWER (the only live pullback setup) hasn't been re-checked since 2026-06-18 — 7 calendar / 5 trading days ago — pullback zone may have decayed in either direction. **Two process failures compounding:** (a) UNIVERSE.md now 50 days stale; (b) pre-market routine has not fired since 2026-06-18, so no candidate scan ran Tue/Wed/Thu of this week. Next pre-market firing must rebuild UNIVERSE before any entry decision, and EOD cron should be audited for the missing Jun 23-24 fires.
