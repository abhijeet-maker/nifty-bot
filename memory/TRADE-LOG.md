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

## 2026-06-19 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.88% | **Alpha today:** +0.88%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

**Trades today:** none.

**Notes:** Flat-cash day. Pre-market HOLD verdict (FOMC-impact blackout for Indian tape + no qualifying setups). Nifty 50 closed -0.88% at 23,954.65 on broad-based selling after the FOMC hold digestion; cash position outperformed by +0.88%. First real EOD snapshot — baseline for tomorrow's day-over-day math. ADANIPOWER stays on the watchlist for Friday's pre-market scan; if it remains in the ₹212-225 pullback zone vs 20DMA and sector confirm strengthens, it becomes the live candidate. UNIVERSE.md is now 44 days stale — weekly review tonight should rebuild before next entry decision.
