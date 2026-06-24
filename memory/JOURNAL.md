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

## 2026-06-18 — Pre-market

### Macro
- Nifty 50: 24,085.70 (Jun 17 close); GIFT Nifty ≈ 24,089–24,098 → flat-to-slightly-positive open
- Bank Nifty: 56,814.80 (Jun 17 close)
- Hot sectors (1m, qualitative read): Banks/Financials, Auto, Capital Goods; Pharma constructive but stock-specific
- Cold / lagging: IT, FMCG, Metals (mixed)
- Today's events: **US FOMC decision landed last night IST** (held at 3.50–3.75% per Jun 17 US announcement). Indian tape digests it this morning → treat as FOMC-impact day. Mid-June is between Q4 FY26 and Q1 FY27 reporting; no Nifty 100 names confirmed to report today. No RBI / budget.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-06-15 → Fri 2026-06-19)
- Concerns: none (no open positions)

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-06-17` returned empty. nse_results feed last broadcast date is 2026-06-05; mid-June is a quiet earnings window between Q4 FY26 (reported May) and Q1 FY27 (starts late July). **REJECT** — no PEAD candidates.
2. VEDL (Metals) — momentum — live: last ₹306.5, 12-1 mom -27.14%, 50DMA ₹448.57 / 200DMA ₹544.17 → below BOTH. UNIVERSE still ranks it #1 from the 2026-05-06 rebuild (43 days stale). **REJECT** — DMA gate fails. Unadjusted split/bonus in Yahoo history feed almost certainly still distorting DMAs (50 < 200 with price near 306 confirms discontinuity). Flagged Apr-May 3x, still open.
3. BEL (Capital Goods) — momentum — last ₹419.85, mom +4.85%, 50DMA ₹427.39 (below) / 200DMA ₹418.01 (above). **REJECT** — fails "above BOTH DMAs". Sector strong but stock is consolidating below 50DMA.
4. ADANIPOWER (Power) — momentum — last ₹220.4, mom +92.89%, above 50/200 DMA (218.25 / 163.78). 20DMA ₹229.79 → stock is **-4.09% vs 20DMA — in the 2-7% pullback zone**. First time this setup actually qualifies on the pullback gate. **REJECT THIS CYCLE** — (a) FOMC-impact day blackout per STRATEGY (US FOMC decided Jun 17 US → Indian tape reacts today); (b) sector confirm weak: today's read describes Power as "selective" not a broad-momentum sector. Watch list, not action.
5. HEROMOTOCO (Auto) — momentum — last ₹5,016.4, below 50DMA (5,061.24) and below 200DMA (5,460.01). **REJECT** — DMA gate fails despite Auto sector being strong.
6. TITAN (Cons Durables) — momentum — last ₹4,380.5, above both DMAs (4,274.55 / 3,993.71), mom +20.0%. 20DMA ₹4,150.6 → stock is **+5.54% ABOVE 20DMA — extended, not pullback**. **REJECT** — chase, not pullback.
7. EICHERMOT (Auto) — momentum — last ₹7,509, above both DMAs (7,184.49 / 7,133.21), mom +28.77%. 20DMA ₹7,244.43 → stock is **+3.65% ABOVE 20DMA — extended**. **REJECT** — not in pullback zone; Auto sector strong but entry rule is pullback only.

### Decision
**HOLD.** Zero candidates cleared all gates. ADANIPOWER finally meets the technical pullback gate after weeks of waiting, but FOMC-impact day blackout + weak sector confirm rule it out today. Default action per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- **No new entries today** (FOMC-impact blackout for Indian tape).
- **ADANIPOWER is the live pullback setup**: ₹220.4 close, in the 2-7% pullback window vs ₹229.79 20DMA. If tomorrow's pre-market still has it in the ₹212-225 zone AND sector-momentum sources upgrade Power to a clearer momentum signal, it becomes a tradeable PEAD/momentum candidate Friday. Stop would sit at ~₹202.8 (-8% from a ₹220.4 fill); target ~₹264.5 (+20%). Position size: 20% of ₹5L = ₹1,00,000 → ~454 shares. Wait for Friday.
- Do NOT enter ADANIPOWER on any gap-up >2% above ₹220 — that's a breakout chase, not pullback.
- **Process risk**: UNIVERSE.md last rebuilt 2026-05-06 — now 43 days stale, ~5 Friday reviews missed. Weekly-review routine has not been running. Universe rankings (esp. VEDL at #1, BEL/HEROMOTOCO/TITAN) are out of date and should be regenerated ASAP via `rebuild-universe` before next entry decision. The 12-1 momentum live for ADANIPOWER (+92.89%) is much higher than UNIVERSE's stale +29.91 — confirms staleness.
- VEDL data divergence (4th cycle now) — Yahoo history likely missing a corporate-action adjustment. Either drop VEDL from universe or switch its history fetch to a split-adjusted source.

## 2026-06-22 — EOD

### EOD 2026-06-22
- Equity ₹5,00,000.00 (day 0.00%, phase 0.00%)
- vs Nifty 50 (+0.38%): alpha -0.38% (cash drag)
- Bank Nifty +0.61%. No positions, no trades today; pre-market routine did not fire.
- Tomorrow watchlist: ADANIPOWER — re-check pullback zone (₹212-225 vs 20DMA) and Power sector momentum. UNIVERSE rebuild (47 days stale) is blocking quality of all entry decisions — prioritize before any new entry.


## 2026-06-24 — Pre-market

### Macro
- Nifty 50: 23,824.10 (Jun 23 close, -1.16% / -278.80 pts) — broke decisively below 24,000; that level now resistance, S1 ≈ 23,750. GIFT Nifty not cleanly sourced this morning; sentiment cautious.
- Bank Nifty: **expiry day today** (June monthly), analyst band 56,800–57,200 (~57,000 ±200).
- India VIX: 14.23 (+10.83%) — meaningful jump, signals elevated uncertainty into expiry.
- Hot sectors (1w/1m): Defence, Capital Goods (record budget capex driving BEL/HAL/L&T/Siemens breakouts), Green Energy / EV (selective).
- Cold / rolling over: IT (-2.23% Jun 23), Metals (-3.23%), Basic Materials. Pharma defensive (+0.92% Jun 23, stable). Power "selective" not broad-momentum.
- Today's events: no Nifty 100 results (Q1 FY27 window starts late July — June is between-quarters quiet zone). No FOMC / RBI / budget. Bank Nifty expiry → elevated intraday vol.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-06-22 → Fri 2026-06-26)
- Concerns: none (flat). Cash drag continues — alpha tracking negative-but-small (-0.38% on 2026-06-22 vs Nifty +0.38%).

### Data-source health (this run)
- `nse.sh quote` returning null fields across symbols (RELIANCE, ADANIPOWER) — nsepython upstream issue or NSE block, not transient.
- `nse.sh history` → Yahoo v8 chart returning HTTP 429 (rate-limited) for every symbol attempted; `nse.sh momentum` therefore fails.
- Result: cannot freshly verify DMA / pullback / 12-1 momentum gates this cycle. All technical reads below are inferred from 2026-06-18 journal (6 trading days stale).
- Perplexity working; PEAD calendar `nse.sh earnings 2026-06-23` → [] (returned empty cleanly — that path uses NSE directly, not Yahoo, suggests the nse_results endpoint is fine but `nse_eq`/yahoo are throttled).

### Candidates considered
1. **PEAD scan** — `nse.sh earnings 2026-06-23` → empty. Mid-June is between Q4 FY26 (May) and Q1 FY27 (late July). No Nifty 100 PEAD candidates available structurally for at least 3–4 weeks. **REJECT — no setups exist.**
2. **VEDL** (Metals) — momentum — UNIVERSE-stale rank #1 still suspect (4th cycle of unresolved Yahoo-history corp-action distortion); metals sector in active rolldown per macro read (-3.23% Jun 23). **REJECT** — sector cold + data unreliable.
3. **BEL** (Capital Goods) — momentum — Defence/CapGoods sector hot per Perplexity (BEL named in 52-week-high breakout list). Live DMA/pullback gates cannot be verified this cycle (Yahoo 429). 2026-06-18 read: last ₹419.85, below 50DMA, above 200DMA → fails "above BOTH DMAs". Even if sector-strong now, can't confirm gates. **REJECT** — data unverifiable + last known DMA-fail.
4. **ADANIPOWER** (Power) — momentum — 2026-06-18 read had it as the live pullback setup (last ₹220.4, in 2-7% pullback zone vs 20DMA ₹229.79, above both DMAs). 6 trading days later, no live data available this cycle. Power sector now described as "selective" not broad-momentum (weak sector confirm). Even if technicals still qualify, entering on a Bank-Nifty-expiry day with VIX +10.83% and Nifty just broke 24,000 support = entering into a tape break. **REJECT** — adverse macro (broken support + VIX spike + expiry vol) overrides a clean setup; sector confirm weak.
5. **HEROMOTOCO** (Auto) — momentum — Auto sector improving in RRG but stock failed DMA gate on 2026-06-18 (below both 50/200 DMA). No fresh data. **REJECT** — last known DMA-fail.
6. **TITAN** (Cons Durables) — momentum — 2026-06-18: above both DMAs but +5.54% extended above 20DMA → chase, not pullback. Consumption sector not in hot-list today. **REJECT** — extended + sector cold.

### Decision
**HOLD.** Default action. Three converging reasons: (a) live data unavailable for any technical re-verification (Yahoo 429 + NSE quote nulls); (b) macro tape just broke 24,000 with VIX +10.83% into a Bank Nifty expiry — wrong day to deploy fresh capital even with a clean setup; (c) PEAD pipeline is structurally empty until late July. Patience > activity. Cash drag is acceptable cost.

### Notes for market-open routine
- **No new entries today.** Bank Nifty expiry day + VIX spike + S1 at 23,750 → if Nifty 50 gaps further down below 23,750, treat as confirmed breakdown and stay defensive. Do NOT chase any reversal bounce.
- ADANIPOWER remains the only live pullback candidate from prior reads. If `nse.sh momentum` recovers from 429 by midday, re-verify: needs last in ₹212-225 zone, 2-7% under 20DMA, above both DMAs, Power sector still constructive. Entry only if all four hold AND macro stabilizes (Nifty reclaims 24,000 on close).
- **Process risk — UNIVERSE.md is now 49 days stale** (last rebuild 2026-05-06). Friday weekly review has missed ~7 cycles. `rebuild-universe` MUST run before any next entry — current UNIVERSE rankings are unreliable (VEDL at #1 is provably wrong; live ADANIPOWER mom was +92.89 on Jun 18 vs UNIVERSE's +29.91, etc.).
- **Wrapper degradation worth a separate fix-cycle**: Yahoo v8 chart 429s blocking all momentum calls; nsepython `nse_eq` returning nulls for valid symbols. Either rotate to a different price source (Stooq, NSEpy direct, or screener) or add caching/throttling to the wrappers. Flag for off-routine engineering work.
- VEDL Yahoo-history corp-action distortion now flagged across 5 cycles unresolved. If Yahoo stays 429 or stays unadjusted, drop VEDL from UNIVERSE on next rebuild.
