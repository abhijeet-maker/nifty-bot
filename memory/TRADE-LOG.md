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

## 2026-05-04 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.74% | **Alpha today:** +0.74%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

**Trades today:** none
**Notes:** First EOD — Day 0 launch. No positions initiated yet; pre-market routine fires tomorrow. Market was risk-off (Nifty -0.74%, breadth 15/50 advances). Being flat all-cash on a down day gives +0.74% alpha. Watch for pre-market screening tomorrow to identify first PEAD or momentum-pullback candidates.
