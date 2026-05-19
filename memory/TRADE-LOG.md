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

## 2026-05-19 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** +0.03% | **Alpha today:** -0.03%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none — pre-market HOLD (zero candidates passed entry gates).
**Notes:** Flat day. Nifty 50 closed 23,649.95 (+6.45 / +0.03%) — essentially unchanged. Bank Nifty close not reliably sourced from Perplexity at write time. BEL and BPCL Q-results expected post-market — tomorrow's pre-market must check filings for PEAD candidates (beat + close-day +3%). ADANIPOWER still the only UNIVERSE name in clean uptrend; sitting at 20DMA, watch for 2-7% pullback into ₹204-215 zone. VEDL DMA-divergence still open for Friday weekly review.
