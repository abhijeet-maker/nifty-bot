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

## 2026-05-01 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** N/A (feed down) | **Alpha today:** N/A
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

**Trades today:** none
**Notes:** Day 1 — no pre-market routine ran, book unchanged from seed. NSE feed returned 403 and Perplexity API key absent; index close unavailable. All-cash. Watching for first PEAD or momentum-pullback setup on next pre-market.
