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

## 2026-05-05 — EOD Snapshot

**Equity:** ₹5,00,000 | **Cash:** ₹5,00,000 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** N/A (data unavailable) | **Alpha today:** N/A
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

**Trades today:** none
**Notes:** Day 1. No pre-market routine fired; no positions entered. Full cash. Nifty 50 close unavailable from live data sources (NSE wrapper returned nulls; Perplexity latest is May 4 at 24,027.60). Tomorrow: pre-market must run full universe screen — PEAD scan on recent earnings beats, 12-1 momentum pullback scan.
