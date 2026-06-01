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

## 2026-06-01 — Pre-market

### Macro
- Nifty 50: 23,649.95 (May 29 close); GIFT Nifty 23,860 (+201 / +0.85%) → gap-up bias at open near 23,750-23,850
- Bank Nifty: ~53,537; described as under pressure, more sensitive to intraday profit-taking
- Hot sectors (1w/1m): IT (TECHM/HCLTECH/WIPRO/INFY rel-strength), Defense, Pharma/Healthcare
- Cold / rolling over: Financials (Nifty Fin Svc -1.55%), Power (POWERGRID -4.11%), Autos (EICHERMOT -2.78%), Consumer/FMCG, Metals (JSWSTEEL -2.47%)
- Today's events: No Nifty 100 results confirmed for 2026-06-01 (Moneycontrol calendar shows 0; NSE filing calendar shows only RPEL/SOTL — non-Nifty 100). IMD monsoon update + FII flow data are the day's macro watch-items. No FOMC / RBI / budget. Not a blackout day.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-06-01 → Fri 2026-06-05)
- Concerns: none (no open positions). 10-day gap since last journal (2026-05-22 → 2026-06-01) — Friday weekly-review routine appears to have been skipped; UNIVERSE is 26 days stale (last rebuild 2026-05-06, target weekly).

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-05-31` (Sun) and `2026-05-29` (Fri) both returned empty. Also checked 2026-05-28 (Thu) = empty. **No PEAD candidates** this window.
2. VEDL (Metals) — momentum — last ₹352.6, mom_12_1 **-39.39%** (UNIVERSE stale value +56.75% is wrong), 50DMA ₹542.17 / 200DMA ₹552.32 → below BOTH. **REJECT** — fails DMA gate; momentum has fully unwound. The DMA-divergence flagged 3x previously (2026-05-06, 05-19, 05-22) is resolving on the wrong side. Sector cold too.
3. BEL (Capital Goods) — momentum — last ₹410.75, mom +11.91%, 50DMA ₹430.47 (below) / 200DMA ₹416.07 (below). **REJECT** — fails "above BOTH DMAs" and momentum (+11.9%) is well under the +18% top-quartile threshold.
4. ADANIPOWER (Power) — momentum — last ₹243.37, mom +100.75%, above 50/200 DMA (199.73 / 156.80). 20DMA from last 20 closes = ₹231.51 → stock is **+5.12% ABOVE** 20DMA. **REJECT** — wrong side of pullback gate (rule is 2-7% BELOW 20DMA, not above). Stock just had a 3-day rally from ₹219 → ₹249 → 243 (breakout extension, not pullback). Sector "Power" also in cold/rolling-over bucket today.
5. HEROMOTOCO (Auto) — momentum — last ₹4,903, below both DMAs (5,139.7 / 5,456.0). **REJECT** — fails DMA gate; Auto sector cold.
6. TITAN (Consumer Durables) — momentum — last ₹4,074.9, below 50DMA (4,243.84), above 200DMA (3,948.88). **REJECT** — fails "above BOTH DMAs"; Consumer also cold.
7. DRREDDY (Healthcare, hot sector) — extra check — last ₹1,303.5, mom +6.61%, above both DMAs (1,279.4 / 1,262.2). **REJECT** — +6.6% momentum is below the +18% top-quartile gate. Hot sector but base-rate too weak.
8. DIVISLAB (Healthcare) — extra — last ₹6,667, mom **-3.48%**. **REJECT** — fails momentum gate.
9. SUNPHARMA (Healthcare) — extra — last ₹1,799.2, mom +7.89%, above both DMAs. **REJECT** — below +18% momentum gate.

### Decision
**HOLD.** Zero candidates passed entry gates. Top universe by momentum is either below DMAs (VEDL, BEL, HEROMOTOCO, TITAN) or extended above 20DMA (ADANIPOWER). Hot-sector pharma names lack momentum strength. Default action per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- No action expected at open.
- ADANIPOWER is the cleanest uptrend leader and the rule-eligible re-entry window opens if it pulls back into ₹215-227 (i.e. 2-7% under 20DMA ~₹231.5). Do NOT chase if it breaks higher — rule is pullback only.
- VEDL "false rank" issue is now self-resolving (live momentum -39.4% vs UNIVERSE stale +56.75%) — UNIVERSE rebuild on Friday must refresh; suspected stale corporate-action adjustment is no longer producing inflated momentum.
- UNIVERSE.md is 26 days stale (last rebuild 2026-05-06). Friday's weekly-review routine MUST rebuild this week, or rotation candidates risk being mis-ranked.
- Watch IT (TECHM/HCLTECH/WIPRO/INFY) and Pharma for sector-strength + momentum convergence in coming days; none qualify on current numbers but the sector tailwind is the place to look first.

