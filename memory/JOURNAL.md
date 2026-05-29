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

## 2026-05-29 — Pre-market

### Macro
- Nifty 50: 23,907.15 (prev close 23,913.70, ~flat); GIFT Nifty ≈ 23,584 (-261 / -1.09%) → gap-down bias expected at open (third-party quote, treat cautiously)
- Bank Nifty: live level not in sources today; recent session showed Nifty Bank -1.30%, Financial Services -1.65% → financials under pressure
- Hot sectors (thematic, not 1w/1m relative-strength): BFSI, defence, renewable/green power, consumer durables, healthcare, IT — no clean live sector heatmap from sources
- Cold/rolling over: defence and green-energy names cited as valuation-stretched (inference, not confirmed read)
- Today's events: Q4 results for ASIANPAINT, TITAN, INDIGO, TATACONSUM (Nifty 100 + UNIVERSE), plus NMDC, GLENMARK, SWIGGY, BANKBARODA, SBIN, BANKINDIA, OBEROI, HYUNDAI, ABB, MCX. No FOMC / RBI / budget. Not a market blackout, but TITAN/ASIANPAINT/INDIGO/TATACONSUM are blackout for entries today (results day rule).

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-05-25 → Fri 2026-05-29)
- Concerns: none (no open positions). 7-day gap since 2026-05-22 journal entry — pre-market did not run Mon-Thu this week.

### Wrapper health
- `nse.sh quote` returning null payload for RELIANCE and TITAN this morning — endpoint appears broken or pre-market data not populated. `momentum` and `history` and `earnings` wrappers all working. Health checks done from `momentum.last` and `history` instead. Flag for investigation in weekly review.

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-05-28` returned empty. No PEAD candidates from yesterday's tape. EICHERMOT/SUNPHARMA (results 2026-05-22) now 5 trading days past print → outside 1-2 day PEAD window. **REJECT** for PEAD.
2. VEDL (Metals) — momentum — last ₹354.7, mom +75.80%, but 50DMA ₹555.53 / 200DMA ₹553.18 → below BOTH. **REJECT** — DMA gate fails. Same unadjusted-corporate-action divergence flagged 2026-05-06 / 05-19 / 05-22; STILL OPEN. UNIVERSE.md not rebuilt for 23 days; VEDL keeps ranking #1 falsely.
3. BEL (Capital Goods) — momentum — last ₹419.1, mom +14.0%, 50DMA ₹431.25 (below) / 200DMA ₹415.8 (above). **REJECT** — fails "above BOTH DMAs". Momentum decayed from +35% to +14% over the month.
4. ADANIPOWER (Power) — momentum — last ₹248.91, mom +98.19%, above both DMAs (195.89 / 155.48), 20DMA ₹225.05 → stock is +10.60% ABOVE 20DMA, RSI14 ≈ 62.9. **REJECT** — extended, not pullback. Broke out from ₹219 → ₹249 over Mon-Wed (+13.5%); this is a chase, not the pullback we waited for.
5. HEROMOTOCO (Auto) — momentum — last ₹5,075, mom +18.7%, below both DMAs (5,145.76 / 5,454.25). **REJECT** — DMA gate fails.
6. EICHERMOT (Auto) — momentum — last ₹7,419, mom +33.14%, above both DMAs (7,044.91 / 7,025.83), 20DMA ₹7,143.25 → +3.86% above 20DMA, RSI14 ≈ 53.7. **REJECT** — extended, not in 2-7% below 20DMA pullback zone. Post-results rally (May 22 → May 27: ₹6,981 → ₹7,419, +6.3%); the PEAD window has already played out and momentum-pullback rule does not apply at this level.
7. COALINDIA (Oil/Gas/Fuels) — last ₹463.05, mom +19.53%, above both DMAs (456.57 / 414.06), 20DMA ₹464.42 → -0.29% (essentially AT 20DMA), RSI14 ≈ 46.8. **REJECT** — RSI < 50 and not in 2-7% pullback zone; sideways at 20DMA.
8. HINDZINC (Metals) — last ₹648.85, mom +37.13%, above both DMAs (585.84 / 543.63), 20DMA ₹632.54 → +2.58% above, RSI14 ≈ 55.6. **REJECT** — extended above 20DMA.
9. DRREDDY (Healthcare) — last ₹1,319.0, mom +8.11%, above both DMAs (1,279.2 / 1,261.76), 20DMA ₹1,308.23 → +0.82% above, RSI14 ≈ 53.0. **REJECT** — sitting at 20DMA, not pullback; also momentum < 18% top-quartile threshold.
10. BAJAJ-AUTO (Auto) — last ₹10,808.5, mom +9.18%, above both DMAs (9,743.21 / 9,293.12), 20DMA ₹10,392.98 → +4.00% above, RSI14 ≈ 55.2. **REJECT** — extended; also momentum < 18% threshold.
11. CGPOWER (Capital Goods) — last ₹934.8, mom +18.54%, above both DMAs, 20DMA ₹846.83 → +10.39% above, RSI14 ≈ 66.1. **REJECT** — extended, very stretched above 20DMA.
12. DIVISLAB (Healthcare) — last ₹6,797.5, mom -1.61%, 20DMA ₹6,747.5 → +0.74% above. **REJECT** — fails 18% top-quartile momentum gate (negative 12-1).
13. TITAN — Q-results TODAY → blackout (no pre-results entries).

### Decision
**HOLD.** Zero candidates passed entry gates. All UNIVERSE names that pass the DMA gate are either extended above 20DMA (ADANIPOWER +10.6%, EICHERMOT +3.9%, HINDZINC +2.6%, BAJAJ-AUTO +4.0%, CGPOWER +10.4%) or sitting on/at 20DMA without a real pullback (COALINDIA -0.3%, DRREDDY +0.8%, DIVISLAB +0.7%). No 2-7% pullback setups in the universe today. Default action per STRATEGY.md. Patience > activity. Week ends with 0 trades.

### Notes for market-open routine
- No action expected at open.
- ASIANPAINT, TITAN, INDIGO, TATACONSUM report TODAY (post-market expected) → check filings tonight; PEAD candidates for Monday 2026-06-01 pre-market scan if they beat both rev and EPS AND close +3% on results day.
- ADANIPOWER broke higher this week (+13.5% Mon-Wed) — DO NOT chase. Re-enter pullback watch only if it retraces to ₹215-225 zone (2-7% under 20DMA). Sector "Power" not explicitly hot in today's sector read.
- EICHERMOT post-earnings gap already played out — past PEAD window, monitor for momentum-pullback into ₹6,800-7,000 zone (2-7% under 20DMA ₹7,143).
- VEDL DMA-divergence OPEN across 4 cycles (2026-05-06, 05-19, 05-22, 05-29). UNIVERSE.md not rebuilt for 23 days. Weekly review TODAY (Friday) is OVERDUE and MUST: (a) rebuild UNIVERSE.md, (b) reconcile VEDL split/bonus history adjustment.
- `nse.sh quote` wrapper returning null — flag for investigation. Workaround used: `momentum.last` for price reads.


