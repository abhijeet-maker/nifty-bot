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

## 2026-05-11 — Pre-market

### Macro
- Nifty 50: 24,176.15 (Fri May 8 close, -0.62%); GIFT Nifty ~24,571 → mildly positive open expected
- Bank Nifty: 55,310.55 (Fri close, -1.31%); broad PSU weakness — SBIN -6.74%, HDFCBANK -1.89%, AXISBANK -1.76%
- Hot sectors (1m): Auto, Realty, Healthcare/Pharma, Defence (Capital Goods)
- Cold/rolling over: Banking (PSU), Metal, FMCG, IT, Consumer Durables
- Today's events: Canara Bank, JSW Energy, Nuvama report (none held, none in UNIVERSE). No FOMC/RBI/Budget.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
1. TITAN (Consumer Durables) — PEAD — Q4 revenue +46% YoY (~₹20,300cr) but net profit ₹1,179cr vs IBE consensus ₹1,392cr (EPS MISS). Stock +4.68% Fri (₹4307.5→₹4509.0) on 4.7x volume. **REJECT** — PEAD requires beat BOTH revenue AND EPS; EPS missed. Sector also rolling over.
2. VEDL (Metals) — momentum — last ₹296.45 vs 50DMA ₹655.57 / 200DMA ₹560.44, mom +79.34%. **REJECT** — below both DMAs (corporate-action / data anomaly persists from last week; flag for Friday rebuild).
3. BEL (Capital Goods) — momentum — last ₹439.70, 50DMA ₹438.76, 200DMA ₹413.90, mom +41.63%. 20DMA ₹442.90 → only -0.72% below 20DMA. RSI(14) 58. Sector (Defence) strong. **REJECT** — not in 2-7% pullback band (sitting at 20DMA, not pulled back).
4. ADANIPOWER (Power) — momentum — last ₹225.33, mom +60.74%, +29.3% above 50DMA, +6.66% above 20DMA, RSI(14) 74.7. **REJECT** — extended (above 20DMA) and overbought (RSI > 70).
5. HEROMOTOCO (Auto) — momentum — last ₹5322, above 50DMA but BELOW 200DMA (₹5409.81), mom +36.45%. **REJECT** — fails STRATEGY DMA gate (must be above BOTH).

### Decision
**HOLD.** Zero candidates passed the entry gates. PEAD failed on EPS-beat requirement; momentum names either below DMAs, not in pullback band, or overbought. Default action per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- Pre-open NSE quote endpoint returned nulls at 08:16 IST (expected — pre-open opens at 09:00). Re-verify at open with `nse.sh quote RELIANCE`.
- No trades planned. No need to re-scan unless a held-name event occurs (none held).
- Friday weekly review to investigate VEDL DMA anomaly (now 2 weeks running) and consider whether TITAN's revenue-beat-but-EPS-miss should add a finer PEAD lesson.
