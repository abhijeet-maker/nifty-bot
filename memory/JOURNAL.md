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

## 2026-05-08 — Pre-market

### Macro
- Nifty 50: ~24,326 (May 7 close); GIFT Nifty -0.65% pre-mkt → weak open expected
- Bank Nifty: weak, -2.19% on the week (high 56,475 → low 54,440); support 55,000-55,500
- Hot sectors (1m): Pharma/Healthcare, Defense, Capital Goods, Renewables/Power
- Cold/rolling over: Banking (BankNifty -2.19% wk, PNB sell call), Auto/Forge (Bharat Forge double-top)
- Today's events: TITAN, TATACONSUM, SBIN Q4 results (Nifty 100). FII heavy selling May 7 (-₹5,835 cr). No FOMC/RBI today.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
1. BAJAJ-AUTO (Auto) — PEAD — Q4FY26 BEAT both rev (₹16,006cr vs ₹15,665cr est) and EPS (PAT +34% YoY). Buyback announced ₹12,000/share. Results 05-06 post-mkt; 05-07 close ₹10,605 vs 05-06 close ₹10,319 = +2.77% (per history series). **REJECT** — results-day move <3% (just under threshold) AND Auto sector rolling over per macro read.
2. GODREJCP (FMCG) — PEAD — reported 05-06 post-mkt; 05-07 close ₹1094.1, today (05-08) -5.26% to ₹1036.5 near 52-wk low ₹967. **REJECT** — clearly negative results reaction.
3. VEDL (Metals) — momentum — mom +71.97%, but live last ₹305.4 vs 50DMA ₹663.29 / 200DMA ₹561.19 (still below both). **REJECT** — corporate-action divergence persists; awaiting Friday UNIVERSE rebuild to clean.
4. BEL (Capital Goods) — momentum — mom +37.36%, just barely above 50DMA (₹439.45 vs ₹438.79 = +0.15%) and above 200DMA. 20DMA ≈ ₹442.90 → -0.78% below 20DMA. **REJECT** — not in 2-7% pullback range (essentially at 20DMA, no pullback).
5. ADANIPOWER (Power) — momentum — mom +52.13%, well above 50DMA (₹230.19 vs ₹172.56 = +33%). 20DMA ≈ ₹208.61 → +10.34% ABOVE 20DMA. **REJECT** — extended, not pullback.
6. HEROMOTOCO (Auto) — momentum — UNIVERSE flags below both DMAs; Auto sector rolling over. **REJECT** — fails DMA gate, sector cold.
7. TITAN (Consumer Durables) — momentum — reports Q4 today. **DEFER** — never trade on results day (LESSONS guideline + STRATEGY blackout for held names; for new entries, await results-day reaction tomorrow as potential PEAD).

### Decision
**HOLD.** PEAD scan: BAJAJ-AUTO closest call but +2.77% results-day < +3% threshold and Auto sector rolling over. Momentum scan: top-5 names all fail (VEDL data issue, BEL not in pullback, ADANIPOWER extended, HEROMOTOCO below DMAs, TITAN reports today). Default action per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- TITAN/TATACONSUM/SBIN report today — re-evaluate post-results for tomorrow's PEAD scan.
- BAJAJ-AUTO at ₹10,590 testing 52-wk high ₹10,740 with active ₹12,000 buyback — if pulls back -2-7% off 20DMA over coming days AND auto sector recovers, may re-qualify on momentum trigger.
- Weak GIFT Nifty (-0.65%); FII selling pressure → expect intraday volatility. No held positions = no defensive action needed.
- Friday weekly-review routine should rebuild UNIVERSE.md and resolve VEDL DMA anomaly.

