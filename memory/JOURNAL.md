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

## 2026-05-14 — Pre-market

### Macro
- Nifty 50: ~23,413 (May 13 close, down vs 24,032 on May 6 — ~-2.6% week-on-week). Support 23,200/23,000; resistance 23,500/23,800.
- Bank Nifty: support 53,000/52,500; resistance 54,000/54,500 (no clean print in source).
- GIFT Nifty pre-market: not available in sources.
- Hot 1w sectors: PSU Bank (+47.7%w but -6.9%m — sharp rebound off weakness, not durable), Defence (+42.2%w / -0.7%m), Transportation/Logistics, Mobility (1w bounce only).
- Rolling over: Consumer Durables (-3.4%w/-7.7%m), Smallcap 100, Smallcap250 MomQuality.
- Today's events: No FOMC, no RBI MPC. No Nifty 100 results confirmed for today by sources or `nse.sh earnings` cache.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week (Mon-Thu): 0 of 2 max
- Concerns: none (no open positions). Broad-market correction (~-2.6% week) — patience preferred.

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-05-13` returned `[]`; Perplexity could not confirm Nifty 100 results on 2026-05-14 either. **0 PEAD candidates.**
2. VEDL (Metals) — momentum — live: last ₹323.35, 50DMA ₹632.03, 200DMA ₹558.35. **REJECT** — below both DMAs (pattern persists from last week; awaiting Friday rebuild to investigate).
3. BEL (Capital Goods) — momentum — last ₹428.25, 50DMA ₹438.01, 200DMA ₹414.29. **REJECT** — below 50DMA, fails STRATEGY DMA gate.
4. ADANIPOWER (Power) — momentum — last ₹213.87, 50DMA ₹178.54, 200DMA ₹149.96, above both DMAs ✓, 12-1 mom +79%. Computed 20DMA ≈ ₹216.50 → currently -1.2% vs 20DMA. RSI ≈ 51. **REJECT** — pullback shallow (<2%), fails 2-7% below-20DMA window. Power not in confirmed hot-sector list either.
5. HEROMOTOCO (Auto) — momentum — last ₹4,995, 50DMA ₹5,261.8, 200DMA ₹5,420.1. **REJECT** — below both DMAs.
6. TITAN (Consumer Durables) — momentum — last ₹4,090.7, 50DMA ₹4,265.1, 200DMA ₹3,909.6. **REJECT** — below 50DMA, and Consumer Durables sector rolling over (-7.7% 1m) → sector gate fails.

### Decision
**HOLD.** Zero candidates passed entry gates. Default action per STRATEGY.md. Broad market in 1m drawdown; most NSE sectoral indices weak; only Defence and PSU Bank show 1w spikes (neither durable, neither cleanly mapped to UNIVERSE). Patience > activity.

### Notes for market-open routine
- No fills expected at open.
- Watch ADANIPOWER: if it drifts down 1-2% more toward ₹208-210 (~3-4% below 20DMA) and RSI holds 50-60, it becomes a clean momentum-pullback candidate for the next pre-market — but sector confirmation for Power is still needed.
- VEDL "above both DMAs" in UNIVERSE.md (2026-04-24) vs live "below both" (2026-05-13) remains unresolved — Friday weekly review must investigate (corp action / data quality).
- HEROMOTOCO has dropped further below both DMAs (vs 2026-05-06) — Friday rebuild should likely drop it from tradable list.

