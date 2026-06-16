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

## 2026-06-16 — Pre-market

### Macro
- Nifty 50: 23,853.90 (2026-06-15 close); GIFT Nifty pre-market level not verifiable from sources today
- Bank Nifty: 56,814.80 (2026-06-15 close)
- Hot sectors (1w/1m): Nifty IT (+3.88% / +5.40%), Nifty Bank (+4.20% / +1.33%), Nifty Financial Services (+3.48% / +4.90%), Nifty Auto (+1.49% / +5.43%), Nifty Consumer Durables (+0.40% / +11.24%)
- Cold/rolling over: Nifty Healthcare (under pressure), Nifty Oil & Gas (low 1m mom)
- Today's events: NO FOMC / RBI / budget. Not a blackout day. Mid-June is between Q4 FY26 and Q1 FY27 earnings seasons — no Nifty 100 results today or yesterday (Infosys leads Q1 FY27 on 2026-07-23).

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-06-15 → Fri 2026-06-19)
- Concerns: none (no open positions). Note 25-day gap since last journal entry (2026-05-22 → 2026-06-16) — routine appears not to have run between.

### Wrapper / data health (operational)
- `nse.sh quote <SYM>` returns all-null JSON for every symbol tested (RELIANCE, HDFCBANK). `nse_eq()` from nsepython is returning an empty dict — NSE quote API path broken. **Live quotes unavailable this cycle.** Yahoo-backed `nse.sh history` and derived `nse.sh momentum` both work — used those for the scan.
- `nse.sh earnings 2026-06-15` returned `[]` — consistent with no Nifty 100 prints mid-June (between earnings seasons), so plausibly correct rather than a wrapper failure; cannot fully distinguish.
- UNIVERSE.md last rebuilt 2026-05-06 — now **41 days stale** (rebuild cadence is weekly). VEDL DMA-divergence noted across prior 3 cycles has resolved naturally: fresh `nse.sh momentum VEDL` returns mom -30.32% (vs UNIVERSE-stale +56.75%) with stock below both DMAs — confirms the prior cycles' suspicion that stale data was driving false rank-1. UNIVERSE rebuild remains overdue and material.

### Candidates considered
PEAD scan — `nse.sh earnings 2026-06-15` returned empty. No PEAD candidates.

Momentum scan — fresh `nse.sh momentum` on UNIVERSE top-5 by stale mom_12_1, plus next 7 (given staleness of UNIVERSE rankings):

1. VEDL (Metals) — last ₹302.5, fresh mom **-30.32%**, below both DMAs (50: 464.51 / 200: 545.53). **REJECT** — mom gate + DMA gate fail. (Resolves the 3-cycle data divergence: UNIVERSE rank-1 was a stale-data artifact.)
2. BEL (Capital Goods) — last ₹409.55, mom +8.58%, below both DMAs. **REJECT** — DMA + mom < 18%.
3. ADANIPOWER (Power) — last ₹220.52, mom +86.78%, above 50DMA (215.92) + 200DMA (162.77). 20DMA = ₹229.61 → stock is **-3.96% below 20DMA** (in pullback zone ✓). RSI(14) ≈ **30** (computed from last 15 closes: 6 gains avg 1.32 / 8 losses avg 3.03 → RS 0.43 → RSI 30.3). **REJECT** — RSI below 50-70 band; stock is in heavy selling, not a healthy pullback. Power sector also not on today's hot list.
4. HEROMOTOCO (Auto) — last ₹5,024, mom +12.4%, below both DMAs (5,063 / 5,460). **REJECT** — DMA + mom.
5. TITAN (Cons Durables) — last ₹4,283.5, mom +17.73% (just under 18%), above 50DMA (4,269.72) + 200DMA (3,986.34). 20DMA = ₹4,125.10 → stock is **+3.84% above 20DMA**. **REJECT** — extended above 20DMA, not in 2-7% pullback zone. Cons Durables sector hot but entry rule fails.
6. EICHERMOT (Auto) — last ₹7,624.5, mom +29.17% ✓, above 50DMA (7,147) + 200DMA (7,119) ✓, Auto sector hot ✓. 20DMA = ₹7,177.55 → stock is **+6.23% above 20DMA**, and gapped +4.27% on 2026-06-15. **REJECT** — breakout move, not a pullback entry; rule is pullback only.
7. COALINDIA (Oil/Gas) — mom +14.92%, below 50DMA. **REJECT** — DMA + mom + cold sector.
8. HINDZINC (Metals) — mom +22.27% ✓, below 50DMA (603.95). **REJECT** — DMA.
9. DRREDDY (Healthcare) — mom -1.47%, below 50DMA, sector cold. **REJECT.**
10. BAJAJ-AUTO (Auto) — mom +16.97%, below 50DMA. **REJECT** — DMA + mom < 18%.
11. BOSCHLTD (Auto) — mom +17.78% (under 18%), above both DMAs, sector hot. **REJECT** — mom under threshold by a hair.
12. CGPOWER (Capital Goods) — mom +16.24%, above both DMAs. **REJECT** — mom under 18%.

### Decision
**HOLD.** Zero candidates passed all entry gates. ADANIPOWER is the only name in the proper pullback zone but its RSI ~30 signals distribution, not a healthy dip. EICHERMOT and TITAN have the right sector + DMA setup but are extended above the 20DMA, not in pullback. Default action per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- No action expected at open.
- **Operational: `nse.sh quote` is broken** (nsepython `nse_eq` returns empty dict). Midday and EOD routines will be hobbled — they rely on quote for live marks. Workaround: use `nse.sh history <SYM> 2` and take the last close as a same-day fallback (will be 1 day stale intraday; acceptable for EOD mark-to-market once today's close lands tonight). A real fix likely needs an nsepython upgrade or a switch to a Yahoo-backed `quote` path inside the wrapper.
- **Operational: UNIVERSE.md is 41 days stale.** Weekly review must rebuild — current ranking misleads (e.g. VEDL was rank-1 on stale +56.75% mom but fresh mom is -30%). Several names currently in UNIVERSE are unlikely to still pass the quality screen; new high-momentum Nifty 100 names probably missing from the watchlist.
- **Operational: 25-day journal gap (2026-05-22 → 2026-06-16)** — pre-market routine apparently didn't fire on the schedule. Worth confirming the cron / trigger configuration is healthy.
- Watch EICHERMOT for a pullback into the ₹7,180–7,400 zone (2-7% under fresh 20DMA ~₹7,178); would qualify on next pullback if Auto stays hot.
- ADANIPOWER — pullback zone intact but needs RSI to recover into 50+ before a momentum entry would qualify.

