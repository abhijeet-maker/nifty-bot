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

## 2026-05-07 — PAPER BUY BAJAJ-AUTO
- Shares: 9  Fill: ₹10,605.89 (quoted ₹10,590.00, slippage 0.15%)
- Cost incl. fees: ₹95,505.51 (gross ₹95,453.01 + costs ₹52.50)
- Stop: ₹9,757.42 (-8%)  Target: ₹12,727.07 (+20%)
- R:R: 2.50:1
- Catalyst: Q4 FY26 beat — revenue ₹16,006 cr +32% YoY (consensus ~₹15,500 cr),
  PAT ₹2,746 cr +34% YoY (consensus ~₹2,560 cr), EBITDA margin 20.8% (+60 bps),
  record volumes 13.71L (+24% YoY), ₹150/sh dividend. Price +2.63% on next-session
  open (gapped up from prev close ₹10,319 to open ₹10,582).
- Sector: Auto (auto OEMs leading 1-mo momentum; Bharat Forge component-side
  weakness only — not in UNIVERSE; not in sector drawdown)
- Fill JSON:
  ```json
  {"timestamp":"2026-05-07 19:30 IST","side":"buy","symbol":"BAJAJ-AUTO","qty":9,
   "quoted_price":10590.0,"fill_price":10605.89,"slippage_pct":0.15,
   "gross_inr":95453.01,"costs_inr":52.5,"net_inr":95505.51,"mode":"PAPER"}
  ```
- Note: filled retroactively in same session — pre-market routine spec is being
  updated to auto-execute going forward.
