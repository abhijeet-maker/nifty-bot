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

## 2026-05-18 — Pre-market

### Macro
- Nifty 50: ~23,643 (last close ref); GIFT Nifty 23,769 (+0.06%) → flat open expected
- Bank Nifty: ~53,710
- Hot sectors (1w/1m): Defence/Capital Goods, Pharma/Healthcare, Power/Utilities
- Cold: broad market rolling over (Nifty failing to reclaim 20W EMA), pockets of financial weakness
- Today's events: IOC Q-results today (not in our filtered UNIVERSE). No FOMC/RBI.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-05-15` and `2026-05-17` both returned []. **No PEAD candidates.**
2. VEDL (Metals) — momentum — last ₹331.05, mom +80.87%, below 50DMA (₹616.31) & 200DMA (₹557.17). **REJECT** — fails DMA gate (still anomalous vs UNIVERSE.md; corp-action suspected, flagged for Friday rebuild).
3. BEL (Capital Goods) — momentum — last ₹423.65, mom +37.83%, below 50DMA (₹437.19), above 200DMA. **REJECT** — must be above BOTH DMAs.
4. ADANIPOWER (Power) — momentum — last ₹221.33, mom +84.22%, above 50DMA (₹181.83) & 200DMA (₹151.01). Computed 20DMA ≈ ₹219.21 → +0.97% ABOVE 20DMA. **REJECT** — fails 2-7% below-20DMA pullback rule.
5. HEROMOTOCO (Auto) — momentum — last ₹5,064.5, mom +28.72%, below both DMAs. **REJECT** — fails DMA gate.
6. TITAN (Consumer Durables) — momentum — last ₹4,169.1, mom +27.02%, below 50DMA (₹4,257.8), above 200DMA. **REJECT** — must be above BOTH DMAs.

### Decision
**HOLD.** Zero candidates passed entry gates. Default per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- No action expected at open.
- Top-5 momentum names all failed DMA or pullback gates; tape is rolling over (Defence/Pharma/Power lead while broad market weakens). Wait for clean setups.
- Friday weekly review must investigate VEDL DMA divergence — UNIVERSE.md shows Yes/Yes but live data shows price ~₹331 vs DMAs ~₹557-616 (likely corporate action / split / demerger).
- IOC reports today (not in UNIVERSE); ignore.

