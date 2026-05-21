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

## 2026-05-21 — Pre-market

### Macro
- Nifty 50: 23,659 (May 20 close, +0.17%); GIFT Nifty 23,830 (+0.78%) → positive open expected
- Bank Nifty: 53,002 (May 20 close, -0.76%) — diverging weak
- Hot sectors (1m): Pharma (~+16% 1M), Healthcare/defensives, IT (intraday strength)
- Cold / rolling over: Tata Group (-16.8% 1M), Mahindra Group, Railways PSU, Waves; PSU Bank & Auto cooling 1W but still +1M
- Today's events: ITC, GAIL, Aurobindo Pharma, Prestige, Page Industries Q-results today (post-market). ITC is in UNIVERSE. No FOMC / RBI / budget. Not a blackout day. Backdrop: Trump-Iran headlines cited as risk.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week (Mon 05-18 → today): 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
1. **PEAD scan (May 19–20 results)**:
   - **BEL** (Capital Goods) — reported May 19. Revenue ₹10,177 cr (+12% YoY, marginal beat); EPS-vs-consensus unverified; PAT +5% YoY. Stock closed **-0.86% on results day** (₹422.95 vs ₹426.6), then -2.28% on May 20 to ₹413.3. **REJECT** — fails ">+3% on results day" PEAD gate; live below both DMAs (50: 435.23, 200: 414.94).
   - **BPCL** (Oil & Gas) — May 19 report unverified by Perplexity; price action ₹280.8 → ₹286.45 (+2.01%) → ₹293.75. **REJECT** — fails ">+3% on results day"; sector cold; UNIVERSE shows below both DMAs.
   - `nse.sh earnings 2026-05-19` and `2026-05-20` both returned []; relied on prior-day journal + Perplexity for reporter list.

2. **Momentum scan — top 5 by mom_12_1_pct in UNIVERSE**:
   - **VEDL** (+71.58% mom; last ₹333.75) — DMA50 ₹593.56 / DMA200 ₹555.50, **below both**. **REJECT** — fails DMA gate. Chronic divergence (3rd consecutive flag); weekly review must reconcile suspected unadjusted corporate action.
   - **BEL** (+23.30%) — see PEAD above. Below both DMAs post-results. **REJECT**.
   - **ADANIPOWER** (Power, +90.67%) — last ₹220.24; above 50DMA ₹186.68 and 200DMA ₹152.58. Computed 20DMA = ₹221.17 → only **-0.42% below 20DMA** (rule: 2-7% pullback). 14-day RSI ≈ **48** (rule: 50-70). **REJECT** — at 20DMA, not in pullback zone; RSI just below window. Same verdict as May 19.
   - **HEROMOTOCO** (+19.42%) — last ₹4,968; DMA50 ₹5,200 / DMA200 ₹5,438, **below both**. **REJECT**.
   - **TITAN** (+22.59%) — last ₹4,106; below 50DMA ₹4,250, above 200DMA. **REJECT** — fails "above BOTH DMAs".

### Decision
**HOLD.** Zero candidates passed entry gates. PEAD reporters both failed the +3% reaction filter (BEL down, BPCL only +2%). Top-5 momentum: 4 of 5 are below at least one DMA; only ADANIPOWER is in clean uptrend but is sitting at its 20DMA, not in a pullback. Default action per STRATEGY.md. Cash remains 100%. Patience > activity.

### Notes for market-open routine
- ITC reports today (post-market). Note for tomorrow's PEAD scan — ITC is in UNIVERSE (FMCG, -31.31% mom but quality-passing); only triggers PEAD if it beats BOTH rev & EPS AND closes +3% on results day.
- ADANIPOWER worth re-checking if it pulls back to **₹205-216 zone** (2-7% below current 20DMA ~₹221) AND RSI recovers above 50. Do NOT chase a breakout.
- Watch BEL: now -3.1% over 2 sessions on a "beat" — sentiment is rejecting the print. May warrant universe re-rank Friday.
- VEDL DMA-divergence is **3 sessions overdue** for resolution — escalate in Friday weekly review.
- Geopolitical tail: Trump-Iran headlines flagged in macro; if oil spikes, BPCL/IOC/ONGC become noise — ignore the move, the PEAD rules already gated them out.
- No action expected at open.

