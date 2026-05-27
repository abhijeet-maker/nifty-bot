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

## 2026-05-27 — EOD Snapshot

**Equity:** ₹5,00,000.00 | **Cash:** ₹5,00,000.00 (100%) | **Deployed:** 0%
**Day P&L:** ₹0 (0.00%) | **Nifty 50 day:** -0.49% | **Alpha today:** +0.49%
**Phase P&L:** ₹0 (0.00% from ₹5,00,000 start)

**Open positions:** none.

| Symbol | Sector | Qty | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | |

**Trades today:** none.
**Notes:** Empty book through the close — no entries triggered all week. Nifty 50 closed 23,913.70 (-0.49%); flat book mechanically outperforms a down tape by +0.49% (passive alpha, not skill). UNIVERSE leaders still mostly below 50DMA per last week's research; ADANIPOWER remains the only clean uptrend leader but is not in the 2-7% pullback zone. Tomorrow: continue PEAD scan via `nse.sh earnings 2026-05-27` in pre-market; watch for ADANIPOWER pullback into ₹205-215. VEDL DMA-divergence still open — needs UNIVERSE rebuild.
