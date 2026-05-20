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

## 2026-05-19 — Pre-market

### Macro
- Nifty 50: 23,643.50 (May 18 close, -46.10 / -0.19%); GIFT Nifty pre-market not reliably sourced
- Bank Nifty: ~50,850; support 50,500 / resistance 51,200
- Hot sectors: not reliably ranked from sources today (commentary: IT, banking firmer; FMCG, select autos softer)
- Cold: same caveat — no clean sector heatmap available
- Today's events: BEL and BPCL Q-results today (both in UNIVERSE). No FOMC / RBI / budget. Not a blackout day.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions). Note 13-day gap since last journal entry (May 6 → May 19).

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-05-18` returned empty. No PEAD candidates.
2. VEDL (Metals) — momentum — last ₹327, mom +74.16%, but DMAs 608.4 / 556.6 → below BOTH DMAs. **REJECT** — fails DMA gate. Same divergence flagged 2026-05-06 still unresolved; weekly review must investigate (suspected unadjusted corporate action in history feed).
3. BEL (Capital Goods) — momentum — reports Q-results TODAY. **REJECT** — entering pre-results = gambling on print, not PEAD. Re-scan tomorrow.
4. ADANIPOWER (Power) — momentum — last ₹219.3, mom +86.02%, above 50/200 DMA (183.5 / 151.5). 20DMA computed from last 20 closes ≈ ₹220.13 → stock is only -0.38% vs 20DMA. **REJECT** — not in 2-7% pullback zone; sitting at the 20DMA after a sideways week.
5. HEROMOTOCO (Auto) — momentum — last ₹4,957, below both 50DMA (5,222) and 200DMA (5,431). **REJECT** — fails DMA gate.
6. TITAN (Cons Durables) — momentum — last ₹4,169.7, below 50DMA (4,256), above 200DMA (3,920). **REJECT** — fails "above BOTH DMAs" gate.
7. EICHERMOT (Auto, backup) — last ₹6,913, below both DMAs (7,089 / 6,969). **REJECT** — fails DMA gate.

### Decision
**HOLD.** Zero candidates passed entry gates. Most UNIVERSE leaders are below their 50DMA after the recent index pullback; only ADANIPOWER is technically in uptrend but it is not in the pullback window. Default action per STRATEGY.md.

### Notes for market-open routine
- BEL and BPCL report TODAY (post-market expected) → check filings tonight; potential PEAD candidates for tomorrow's pre-market if they beat both rev and EPS and close +3% on results day.
- ADANIPOWER worth re-checking later in the week IF it pulls back 2-7% under 20DMA (i.e. ~₹204–215 zone). Do NOT chase if it breaks higher — the rule is pullback, not breakout.
- VEDL DMA-divergence issue is still open — Friday weekly review must reconcile (possible split/bonus not adjusted in nse.sh history).
- No action expected at open.

## 2026-05-20 — Pre-market

### Macro
- Nifty 50: 23,618.00 (May 19 close); GIFT Nifty 23,559.50 (-0.25% / slightly negative open)
- Bank Nifty: 53,409.15 (May 19 close), live tape ~53,710 → modest bounce; support 53,200 / resistance 54,000
- Hot sectors (near-term): IT, Pharma (defensive bid)
- Cold: Banks, Energy (rolling over on latest snapshot)
- Today's events: no FOMC / RBI / budget. BEL filed results yesterday (post-market); no Nifty 100 of note reporting today. Not a blackout day.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions).
- Data note: `nse.sh quote` and `nse.sh earnings` are returning empty payloads from this container (nse_eq → {}). Yahoo-backed `history` and `momentum` are working; all price/DMA/momentum checks below use Yahoo closes. Earnings calendar substituted via Perplexity narrative + checking known scheduled names (BEL / BPCL from yesterday's pre-market).

### Candidates considered
1. BEL (Capital Goods) — PEAD — Q4/FY26 announced May 19: rev ₹10,177cr, PAT ₹2,203cr, final div ₹0.55; order book ₹73,882cr. Price action May 18→19: ₹426.60 → ₹422.95 = **-0.86%**. **REJECT** — fails PEAD gate (must close +3% on results day). Also below 50DMA (₹436).
2. BPCL (Energy) — PEAD — Perplexity could not confirm filing; price action May 18→19: ₹280.80 → ₹286.45 = **+2.01%**. **REJECT** — fails +3% PEAD gate. Also below both DMAs (50: ₹302, 200: ₹338), mom +0.33%, sector cold.
3. VEDL (Metals) — momentum — last ₹337.65, mom +72.78%, DMAs ₹601 / ₹556 → below BOTH. **REJECT** — DMA gate. Same suspected unadjusted-history issue flagged May 6 / May 19 — still pending Friday weekly review.
4. ADANIPOWER (Power) — momentum — last ₹219.09, mom +86.87%, above 50/200 DMA. 20DMA ₹220.94 → -0.84% from 20DMA, RSI14 49.8. **REJECT** — not in 2-7% pullback zone (too shallow); rolling sideways at the 20DMA.
5. HINDZINC (Metals) — momentum — last ₹632.60, mom +33.52%, above 50/200 DMA. 20DMA ₹623.59 → +1.45% (ABOVE 20DMA), RSI14 56.9. **REJECT** — no pullback, slightly extended.
6. CGPOWER (Capital Goods) — momentum — last ₹819.40, mom +18.73%, above 50/200 DMA. 20DMA ₹831.67 → -1.47%, RSI14 48.4. **REJECT** — not in 2-7% pullback zone (too shallow).
7. BAJAJ-AUTO (Auto) — momentum — last ₹10,205, mom +17.62% (borderline top-quartile), above 50/200 DMA. 20DMA ₹10,086 → +1.18% (ABOVE 20DMA), RSI14 64.8. **REJECT** — no pullback; near RSI 70 ceiling.
8. HEROMOTOCO, TITAN, EICHERMOT, DRREDDY, COALINDIA — all checked. HEROMOTOCO/EICHERMOT below both DMAs; TITAN below 50DMA; DRREDDY mom -1.27%; COALINDIA mom +9.51% (below top-quartile 18%). All **REJECT**.

### Decision
**HOLD.** Zero candidates passed all gates. PEAD targets (BEL, BPCL) failed the +3% results-day move; momentum leaders are either below the 50DMA or sitting at/above their 20DMAs with no pullback to enter on. Default per STRATEGY.md — patience > activity.

### Notes for market-open routine
- No new entries planned. Open silently.
- Watch ADANIPOWER and CGPOWER for a clean pullback into the 2-7% below 20DMA zone (~₹205-216 for ADANIPOWER, ~₹773-815 for CGPOWER). Do NOT chase breakouts.
- HINDZINC if it gives back 2-5% into ~₹593-611 with RSI > 50 — re-evaluate.
- BEL — re-check tonight's filings for full management commentary; if guidance is strong AND price closes today +3-5% on volume, treat as delayed-PEAD candidate for tomorrow's scan (allowed: STRATEGY says "results in last 1-2 trading days").
- Infra/data: investigate NSE wrapper failure during Friday weekly review — `nse_eq` returning `{}` for all symbols; likely cloud IP blocked or cookie auth needs refresh. Yahoo-backed paths still work, so non-blocking for now.
- VEDL unadjusted-history issue still open — Friday must fix.

