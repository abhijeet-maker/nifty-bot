# Research Journal

Daily pre-market research, midday scans, EOD closing notes, all appended here
in reverse-chronological reading order (newest at bottom — append only).

Each trading day gets one top-level `## YYYY-MM-DD` section with subsections
added by each routine:

```markdown
## YYYY-MM-DD — Pre-market
### Macro
### Portfolio health
### Candidates considered
### Decision
### Notes for market-open routine

### Market-open execution YYYY-MM-DD
(only present if a trade happened)

### Midday YYYY-MM-DD
(only present if action was taken)

### EOD YYYY-MM-DD
(always present — closing note)
```

The **tail of this file** is what subsequent routines read. Keep entries tight —
under 40 lines per day typical. Long-form analysis goes in the Decision block,
not every block.

---

_(Seed — first entry will be written by the first pre-market routine firing.)_

## 2026-05-06 — Pre-market

### Macro
- Nifty 50: 24,032 (May 5 close, -0.36%); GIFT Nifty 24,279 (+0.71%, ~+170 pts) → mildly positive open expected
- Bank Nifty: 54,547 (flat); support 54,200-54,400
- Hot sectors (1m): Pharma/Healthcare, Financials, Consumer Durables/FMCG, Capital Goods
- Cold: Oil & Gas, Hospitality
- Today's events: BAJAJ-AUTO and GODREJCP Q4 results (post-market). No FOMC/RBI today.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
1. VEDL (Metals) — momentum — UNIVERSE shows +56.75% mom and above both DMAs as of 2026-04-24, but live: last ₹303.9 vs 50DMA ₹677.94 / 200DMA ₹562.58. **REJECT** — below both DMAs (likely corporate action or major drawdown; needs UNIVERSE re-screen Friday).
2. BEL (Capital Goods) — momentum — last ₹433.35, 50DMA ₹438.9, 200DMA ₹413.43, mom +35.99%. **REJECT** — below 50DMA, fails STRATEGY gate (must be above BOTH).
3. ADANIPOWER (Power) — momentum — last ₹229.96, mom +53.43%, above 50/200 DMA. 20DMA ≈ ₹202.3 → +13.7% above 20DMA. **REJECT** — extended, not 2-7% below 20DMA pullback per rule.
4. PEAD scan — `nse.sh earnings 2026-05-05` returned empty. No PEAD candidates.

### Decision
**HOLD.** Zero candidates passed the entry gates. Default action per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- BAJAJ-AUTO + GODREJCP report today (post-market) → potential PEAD candidates for tomorrow's pre-market scan if they beat. Both are in UNIVERSE.md.
- VEDL DMA divergence between UNIVERSE.md (Yes/Yes on 2026-04-24) and live (No/No on 2026-05-05) is suspicious — flag for Friday weekly review to investigate (corporate action? data issue?).
- No action expected at open.

## 2026-05-13 — Pre-market

### Macro
- Nifty 50: 23,722.60 (May 12 close, -1.83%); GIFT Nifty level not retrievable. Sharp risk-off session.
- Bank Nifty: ~54,000 area (May 11 close 54,478, May 12 weak with banks contributing to selloff).
- Hot sectors (1w/1m): Energy/Oil & Gas, Pharma/Healthcare, Metals (defensive + commodity tilt).
- Cold/rolling over: IT (-4%, AI-disruption fears), Realty (-4%), Banks, Consumer Durables, Capital Goods (BEL -3.5%), Auto, Aviation, Paints. FMCG resilient.
- Today's events: Moody's cut India 2026 GDP forecast 0.8pp to 6.0%; rupee 95.63/USD, Brent >$100, FII selling continuing. No RBI/FOMC. Nifty 100 results scheduled today (post-market): BHARTIARTL, PFC, TVSMOTOR.
- NSE quote endpoint (nsepython) returning null payloads — fell back to Yahoo Finance history for all live price/momentum work. Wrappers otherwise green.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week (Mon-Wed): 0 of 2 max
- Concerns: none (no open positions); broad risk-off environment raises the bar for new entries.

### Candidates considered
1. **PEAD scan**: `nse.sh earnings` for 2026-05-11 and 2026-05-12 both returned `[]`. Perplexity confirms no Nifty 100 names reported May 12. **No PEAD candidates.**
2. VEDL (Metals, mom +84.86%) — last ₹305.05, DMA50 ₹640.12, DMA200 ₹559.00. **REJECT** — below BOTH DMAs (confirms last week's flag; still in deep drawdown, likely corporate action).
3. ADANIPOWER (Power, mom +74.31%) — last ₹209.63, above both DMAs, -2.49% vs 20DMA (pullback zone ✓). **REJECT** — RSI(14) 44 (need 50-70); high-volume -5.6% breakdown on May 12 suggests trend turning, not a healthy pullback.
4. BEL (Capital Goods, mom +43.76%) — last ₹416.50, below 50DMA ₹438.23. **REJECT** — fails DMA gate + sector cold.
5. HEROMOTOCO (Auto, mom +38.06%) — last ₹5,082.50 vs DMA50 ₹5,276.69, DMA200 ₹5,417.16. **REJECT** — below both DMAs + auto sector cold.
6. HINDZINC (Metals, mom +37.43%) — last ₹641.90, above both DMAs ✓, RSI 68.3 (top of band). **REJECT** — +5.47% ABOVE 20DMA, fails 2-7%-below pullback rule (extended).
7. COALINDIA (Energy, mom +12.88%) — above both DMAs ✓, sector hot. **REJECT** — 12-1 momentum below ~18% top-quartile threshold.
8. DRREDDY (Pharma, mom +7.66%) — below 50DMA ✗. **REJECT** — DMA gate + momentum too low.
9. DIVISLAB (Pharma, mom -0.51%) — **REJECT** — momentum negative.
10. TITAN (Consumer Durables) — sector in sharp decline per macro. **REJECT** — sector gate.

### Decision
**HOLD.** Zero candidates passed the entry gates. Default action per STRATEGY.md. Risk-off macro (Moody's GDP cut, FII selling, rupee/oil pressure) further raises the bar — patience > activity.

### Notes for market-open routine
- Re-verify NSE quote wrapper at open; if still nulling out, flag for fix and use Yahoo Finance fallback only.
- Watch BHARTIARTL, PFC, TVSMOTOR results post-market today → potential PEAD setups for tomorrow's scan. None are currently held. None are in the current filtered UNIVERSE.md, so they would need to clear quality screen at Friday's rebuild before becoming PEAD-tradable.
- VEDL drawdown still unexplained — keep flag for Friday review.
- No action expected at open. Sit in cash.

