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

## 2026-05-28 — EOD Snapshot (MARKET HOLIDAY — Bakri Id)

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** N/A (closed) | **Alpha today:** N/A
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none (market closed for Bakri Id).
**Notes:** NSE closed today for Bakri Id (per NSE holiday calendar). `nse.sh quote RELIANCE` returned nulls, confirming no live tape. Last known closes: Nifty 50 23,907.15 and Bank Nifty 54,853.85 (both 2026-05-27). Book is 100% cash — no marks to update. Next session Fri 2026-05-29; pre-market scan will use 27-May closes as the prior reference. Outstanding open items unchanged from 22-May journal: VEDL DMA-divergence still unresolved across 3 cycles, UNIVERSE last rebuilt 2026-05-06 (now 22 days stale) — overdue.
