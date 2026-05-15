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

## 2026-05-15 — Pre-market

### Macro
- Nifty 50: 23,689.60 (May 14 close, +1.18%, bounce off oversold low 23,379 on May 13). GIFT Nifty mildly positive into open.
- Bank Nifty: not cleanly reported in sources today.
- Hot sectors (1w): Pharma/Healthcare, Metals (TATASTEEL results catalyst), PSU Banks, Private Banks.
- Cold: IT (-2.03% BSE IT, worst performer), Oil & Gas (selling pressure).
- Today's events: TATASTEEL, NHPC, POWERGRID Q4 results (none held, none in UNIVERSE). No FOMC/RBI.
- Data note: `nse.sh quote` returning null payloads (NSE endpoint blocked/empty). History + momentum (Yahoo) still functional. Flag for tooling fix.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week (Mon 2026-05-11 → today): 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-05-14` returned empty. Perplexity could not confirm specific Nifty 100 names with verifiable beat/miss for yesterday. **No PEAD candidates.**
2. VEDL (Metals) — momentum — last ₹338.9, 50DMA ₹624.05, 200DMA ₹557.79, mom +79.53%. **REJECT** — below both DMAs (same suspected corp-action issue from May 6; still unresolved — escalate to Friday weekly review today).
3. BEL (Capital Goods) — momentum — last ₹428.85, 50DMA ₹437.61 (below), 200DMA ₹414.42 (above), mom +41.16%. **REJECT** — fails "above BOTH DMAs" gate.
4. ADANIPOWER (Power) — momentum — last ₹224.49, above 50/200 DMA, mom +76.74%, RSI 59.3. 20DMA ₹218.07 → currently **+2.95% ABOVE 20DMA**. **REJECT** — extended, not in 2-7% below-20DMA pullback zone.
5. HEROMOTOCO (Auto) — momentum — last ₹5077, 50DMA ₹5247.64, 200DMA ₹5423.77, mom +29.48%. **REJECT** — below both DMAs.
6. TITAN (Consumer Durables) — momentum — last ₹4135.2, 50DMA ₹4260.97 (below), 200DMA ₹3912.96 (above), mom +25.22%. **REJECT** — fails "above BOTH DMAs" gate.

### Decision
**HOLD.** Zero candidates passed the entry gates. Default action per STRATEGY.md. Patience > activity. Notably 4 of top-5 momentum names are below 50DMA — broad sign that the prior momentum cohort has rolled over since UNIVERSE was built (2026-05-06).

### Notes for market-open routine
- No entry intended today. No held positions to monitor.
- Weekly review fires this evening (Friday) — UNIVERSE rebuild should resolve VEDL DMA anomaly (likely a corporate action/split skewing the historical series Yahoo serves) and flush the top-end names that have broken trend (BEL, HEROMOTOCO, TITAN below 50DMA).
- Tooling: NSE `quote` returning all-nulls — investigate nsepython during weekly maintenance window. Doesn't block research today (history + momentum + screener all OK).

