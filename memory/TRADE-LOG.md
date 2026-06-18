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

## 2026-06-18 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.34% | **Alpha today:** -0.34%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none (FOMC-impact blackout per pre-market decision).
**This week:** 0 of 2 max (week Mon 2026-06-15 → Fri 2026-06-19).

**Notes:** Indian tape digested last night's Fed hold (3.50–3.75%) with a hawkish lean; Nifty 50 finished +0.34% at 24,168.00 on lower crude and a rupee-weakness backdrop. Book sat in 100% cash by design — FOMC-impact day blackout ruled out the only technically-qualified setup (ADANIPOWER, in the 2-7% pullback zone vs its 20DMA). Cost of sitting out: -0.34% of relative drag for one day, acceptable per process. Tomorrow (Fri 2026-06-19): re-scan ADANIPOWER; if it holds ₹212-225 and sector-momentum sources upgrade Power, it is the live pullback candidate. Friday is also the weekly-review window — UNIVERSE.md is 43 days stale and must be rebuilt before the next entry. No Nifty 100 names confirmed reporting tomorrow.
