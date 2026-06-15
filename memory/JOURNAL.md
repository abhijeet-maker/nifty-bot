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

## 2026-05-22 — Pre-market

### Macro
- Nifty 50: 23,654.70 (prev close 23,659.00, ~flat); GIFT Nifty ≈ -199 pts → gap-down bias near 23,450-23,460 expected at open
- Bank Nifty: live level not reliably sourced this morning; treat as neutral
- Hot sectors (1m, RRG read): Auto, Metals, Pharma improving; PSU Bank / Infra / IT / Financial Services in leading quadrant
- Cold/lagging: FMCG, Realty, Consumption, Commodities; Energy/PSE/Media lagging-but-improving
- Today's events: SUNPHARMA (board mtg post-mkt, call 6:30 PM IST), EICHERMOT, NAUKRI, TORNTPHARMA Q-results today. SUNPHARMA + EICHERMOT are in UNIVERSE → blackout for those names today (no entries pre-print). No FOMC / RBI / budget. Not a blackout day for the market.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-05-18 → Fri 2026-05-22)
- Concerns: none (no open positions)

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-05-21` returned empty. No PEAD candidates from yesterday's tape. BEL/BPCL (results 2026-05-19) now 3 trading days past print → outside the 1-2 day PEAD window per STRATEGY. **REJECT** for PEAD.
2. VEDL (Metals) — momentum — last ₹329.75, mom +66.41%, but 50DMA ₹585.74 / 200DMA ₹554.95 → below BOTH. **REJECT** — DMA gate fails. Same unadjusted-corporate-action divergence flagged 2026-05-06 and 2026-05-19; still open for weekly review tonight.
3. BEL (Capital Goods) — momentum — last ₹420.4, mom +23.7%, 50DMA ₹434.27 (below) / 200DMA ₹415.1 (above). **REJECT** — fails "above BOTH DMAs" gate. Also post-results day — separate PEAD-window question, not momentum.
4. ADANIPOWER (Power) — momentum — last ₹219.33, mom +90.47%, above 50/200 DMA (188.29 / 153.08). 20DMA from last 20 closes = ₹221.42 → stock is -0.94% vs 20DMA. **REJECT** — not in 2-7% pullback zone (same as 2026-05-19; sitting at the 20DMA, sideways). Sector "Power" also not explicitly hot in today's sector read.
5. HEROMOTOCO (Auto) — momentum — last ₹4,969.5, below both 50DMA (5,188.92) and 200DMA (5,441.04). **REJECT** — DMA gate fails despite Auto sector being in improving quadrant.
6. TITAN (Cons Durables) — momentum — last ₹4,083.1, below 50DMA (4,247.13), above 200DMA (3,930.16). **REJECT** — fails "above BOTH DMAs". Also Consumption sector lagging.

### Decision
**HOLD.** Zero candidates passed entry gates. Top-momentum UNIVERSE names remain below their 50DMA; ADANIPOWER is the only technical uptrend leader and it is still not in the pullback window. Default action per STRATEGY.md. Patience > activity. Week closes with 0 trades — valid outcome.

### Notes for market-open routine
- No action expected at open.
- SUNPHARMA + EICHERMOT report TODAY (post-market) → check filings tonight; potential PEAD candidates for Monday's pre-market scan if they beat both rev and EPS AND close +3% on results day.
- ADANIPOWER still the cleanest momentum setup pending a real pullback into ₹205-215 (i.e. 2-7% under 20DMA ~₹221). Do not chase a breakout above ₹225 — rule is pullback only.
- VEDL DMA-divergence STILL open across 3 cycles (2026-05-06, 2026-05-19, 2026-05-22). Weekly review TODAY (Friday) MUST reconcile or VEDL stays falsely ranked #1 in UNIVERSE; suspected unadjusted split/bonus in history feed driving the inflated 12-1 momentum and stale DMAs.
- Universe last rebuilt 2026-05-06 (16 days ago, overdue) — weekly review tonight should rebuild.


## 2026-06-15 — Pre-market

### Macro
- Nifty 50: 23,622.90 (Fri 06-12 close, broad risk-on rally on Mid-East de-escalation); GIFT Nifty level not reliably sourced pre-open
- Bank Nifty: 56,814.80 (Fri close) — strongest sector; private + PSU banks led the week, fresh RBI guidelines on FX inflows cited as tailwind
- Hot sectors (1w/1m): Banks, Financial Services, Auto (near 52w highs, may be late-cycle), Metals, Pharma (recovering)
- Cold/value: IT (WIPRO -9% on buyback exit), FMCG, Realty; ONGC -7% on Brent crude collapse
- Today's events: No Nifty 100 results confirmed for 2026-06-15. No FOMC/RBI/budget. Not a blackout day.
- Note: New week (Mon 2026-06-15 → Fri 2026-06-19). Trades-this-week counter resets to 0/2.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions). Note 24-day gap since last journal entry (2026-05-22 → 2026-06-15); routine cadence drift to flag in weekly review.

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-06-14` and `2026-06-12` both returned empty. **No PEAD candidates.**
2. VEDL (Metals) — momentum — last ₹309.65, mom_12_1 now -28.27% (vs UNIVERSE table's stale +56.75%), below both DMAs. **REJECT** — fails momentum and DMA gates. *Earlier divergence (flagged 05-06/05-19/05-22) appears RESOLVED: history feed has caught up with corporate action; UNIVERSE row is simply stale.*
3. BEL (Capital Goods) — last ₹406.5, mom +6.61%, below both DMAs. **REJECT** — fails DMA + momentum top-quartile gates.
4. ADANIPOWER (Power) — last ₹223.07, mom +85.66%, above 50DMA (214.71) AND 200DMA (162.26), 20DMA ₹229.55 → stock is -2.82% vs 20DMA (✅ pullback window). RSI ≈ 42.58 (❌ below 50). Power sector at best neutral per Perplexity sector read (no momentum-leader status). **REJECT** — fails RSI gate and sector momentum gate.
5. HEROMOTOCO (Auto) — last ₹4,962.6, mom +15.65%, below both DMAs. **REJECT** — fails DMA gate (Auto sector hot but technical setup absent).
6. TITAN (Cons Durables) — last ₹4,184.0, mom +18.30%, below 50DMA, above 200DMA. **REJECT** — fails "above BOTH DMAs".
7. EICHERMOT (Auto) — last ₹7,312.0, mom +30.44%, above both DMAs (50: 7127.6 / 200: 7110.1). 20DMA ≈ ₹7,142 → stock is +2.38% ABOVE 20DMA (❌ not in 2-7% below pullback window — it's extended, not pulled back). **REJECT** — fails pullback gate. Worth re-checking later in the week if it pulls back to ₹6,930-7,000 zone (2-3% below 20DMA).
8. BAJAJ-AUTO (Auto) — last ₹10,063, mom +20.3%, below 50DMA (10,064.7), above 200DMA. **REJECT** — fails DMA gate.
9. DRREDDY, DIVISLAB (Pharma) — both mom <2% → below top quartile. **REJECT** — fail momentum gate despite hot Pharma sector read.
10. HINDZINC (Metals) — last ₹559.9, mom +19.43% (top quartile), below 50DMA (603.0), above 200DMA. **REJECT** — fails DMA gate.

### Decision
**HOLD.** Zero candidates passed entry gates. Top-momentum UNIVERSE names are largely below their 50DMA after Q1FY27 corrections. Only ADANIPOWER is in technical uptrend WITH a pullback, but RSI is in the 40s (post-correction, not setup-quality) and Power is not a leading sector. Default action per STRATEGY.md. Patience > activity. 4th consecutive pre-market HOLD — gates working as designed; no rule changes warranted.

### Notes for market-open routine
- No action expected at open.
- Watch EICHERMOT — if it pulls back to ₹6,930-7,070 (2-5% under 20DMA ₹7,142) AND RSI stays 50-70, it becomes the cleanest momentum-pullback setup in the universe (Auto is hot, DMAs aligned, mom +30%). Do NOT chase a breakout above ₹7,400.
- Watch ADANIPOWER for RSI recovery into 50+. If price holds ₹215-225 zone and RSI lifts, setup re-qualifies (though sector confirm still needed).
- **For weekly review (Friday 2026-06-19):**
  - UNIVERSE is 40 days stale (last rebuild 2026-05-06) — MUST rebuild this week.
  - UNIVERSE contains ZERO bank names despite Banks being the #1 hot sector this week. Verify D/E < 2.0 financial-sector exemption is actually being applied in the rebuild script (HDFCBANK, ICICIBANK, AXISBANK, KOTAKBANK, SBIN should all clear quality on every metric except D/E which needs the bank carve-out).
  - VEDL data divergence appears self-resolved — close the flag.
  - 24-day journal gap suggests cron didn't fire on multiple weekdays — confirm scheduler is healthy.
