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

## 2026-05-02 — EOD Snapshot

**Equity:** ₹5,00,000 | **Cash:** ₹5,00,000 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day (Fri 01-May):** +0.49% | **Alpha today:** -0.49%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

**Trades today:** none

**Notes:** Saturday — NSE closed. No open positions; book is 100% cash at seed value ₹5,00,000. Nifty 50 rose +0.49% on Friday (last trading day), Bank Nifty was flat (-0.04%). Cash drag produced -0.49% alpha vs index today. Pre-market routine fires Monday 09-May; first live watch for PEAD or momentum-pullback setups begins then.
