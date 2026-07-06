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


## 2026-06-29 — Pre-market

### Macro
- Nifty 50: 24,056.00 (Jun 25 close, +0.14%); GIFT Nifty pre-open not cleanly sourced — possible flat-to-slight-gap-down bias near 23,960
- Bank Nifty: ~55,177 (week-end ref, +0.9% on the truncated 4-day week)
- Hot sectors (1w): Pharma +2.1%, Realty +1.8%, Auto +1.5%
- Cold / weakening: Oil & Gas -0.87%, Nifty Mid Select rolling over (-1.3% wk), Nifty 50 ~-8% YTD
- Today's events: No Nifty 100 Q1 FY27 results today; reporting season starts in earnest July 9 (TCS). No FOMC / RBI / budget. Not a blackout day.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-06-29 → Fri 2026-07-03)
- Concerns: none (no open positions)

### Data feed outage (CRITICAL — operational)
- `bash scripts/nse.sh quote <SYM>` returns all-null JSON for every tested symbol (RELIANCE, HDFCBANK, ADANIPOWER). nsepython is silently failing — likely NSE cookie/auth or upstream-API change.
- `bash scripts/nse.sh history|momentum <SYM>` returns Yahoo Finance HTTP 429 across 3 retries spaced 90s apart. Yahoo `query1.finance.yahoo.com/v8/finance/chart/<SYM>.NS` is durably rate-limited from this container.
- `bash scripts/universe-cache.sh get <SYM>` works — Screener fundamentals snapshot still available, but it does NOT give live price/DMAs/RSI.
- `bash scripts/perplexity.sh "..."` works.
- Net: I have macro context + cached fundamentals, but ZERO live technicals. Cannot evaluate momentum DMAs / pullback zone / RSI today. PEAD trigger also moot (no earnings).

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-06-26` returned `[]`; Perplexity confirms no Nifty 100 names reported Friday. **REJECT — no PEAD candidates.**
2. Momentum scan — Yahoo history endpoint 429-throttled; cannot compute 50/200 DMA, 12-1 momentum, 20-DMA pullback %, or RSI for any UNIVERSE name. **REJECT ALL — no live technical data.**
3. ADANIPOWER (from 2026-06-18 watchlist) — Screener snapshot price ₹226. Last journal entry had it in the 2-7% pullback zone but blocked by FOMC. Today FOMC is moot, but I cannot independently verify the technical gates without live history. **REJECT — gate-data unavailable; will not trade on stale 11-day-old technicals.**

### Decision
**HOLD.** Forced HOLD: (a) zero PEAD candidates (no Friday Nifty 100 prints); (b) momentum gate unevaluable due to Yahoo-429 + NSE-nullquote outage. Default action per STRATEGY.md. Patience > activity.

### Notes for market-open routine
- **Data feed fix is the top priority.** Until `nse.sh quote` returns real prices AND `nse.sh history` clears the Yahoo 429, no entries can be vetted. Likely fixes:
  - nsepython: bump version, or switch to direct NSE cookie-priming as in the BSE workaround. The all-null output suggests `nse_eq()` is catching an exception and returning `{}`; instrument it.
  - Yahoo 429: container IP may be flagged. Options — add a `User-Agent` + `Cookie` from a fresh browser session, route through `query2.finance.yahoo.com`, or swap to `yfinance` Python lib (uses session cookies), or switch history source to NSE bhav files.
- ADANIPOWER remains the only live candidate from the prior cycle. Once feeds are back, re-run momentum gate on it FIRST; if still in pullback zone (₹212-225 vs 20DMA) and Power sector confirms, this is the tradeable setup the routine has been waiting on.
- UNIVERSE.md is now **54 days stale** (last rebuild 2026-05-06). Once feeds are back, run weekly-review / rebuild-universe BEFORE any entry decision. Stale ranking risk is now compounding the data-outage risk.
- VEDL data divergence — still open across 5 cycles. Resolution depends on the same Yahoo history endpoint that is currently 429'd.
- No action expected at open.

## 2026-07-06 — Pre-market

### Macro
- Nifty 50: 24,270.85 (Fri Jul 3 close, +0.39%); Sensex 77,763.91 (+0.34%)
- GIFT Nifty pre-open: not cleanly sourced; setup bias moderately bullish; support 24,200 / resistance 24,350
- Bank Nifty: Friday close not explicitly sourced; ref 57,800 area cited
- Hot sectors (Fri / 1w): **Nifty IT +3% Friday** (extended gains 2nd session), on softer US jobs → cooler Fed-hike odds + lower crude
- Cold / lagging: **PSU Banks -1% Friday**, Auto and Consumer Durables lower; Auto also under pressure into Q1 result season
- Today's events: **No Nifty 100 Q1 FY27 results today**. Big-cap reporting starts July 13 (HCLTECH), July 23 (INFY), and staggered through the month. No FOMC / RBI / Budget. **Not a blackout day.**

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-07-06 → Fri 2026-07-10)
- Concerns: none (no open positions to health-check)

### Data feed outage (STILL OPEN — 8 days now)
- `bash scripts/nse.sh quote RELIANCE` → still returns all-null JSON. Same nsepython silent-failure mode as 2026-06-29.
- `bash scripts/nse.sh momentum <SYM>` → still Yahoo Finance HTTP 429 across retries. `query1.finance.yahoo.com` remains durably rate-limited from this container.
- `bash scripts/nse.sh earnings 2026-07-05|06` → returns `[]` (yesterday was Sunday anyway; today confirmed no Nifty 100 prints via Perplexity — feed answer is at least directionally correct).
- `bash scripts/perplexity.sh "..."` → working.
- Net: macro narrative available; ZERO live technical data for 8 consecutive days. Cannot evaluate momentum (DMAs / pullback / RSI) or PEAD gap-and-hold today.

### Candidates considered
1. **PEAD scan** — Yesterday (2026-07-05) was Sunday; NSE closed. `nse.sh earnings 2026-07-05` returned `[]`. Perplexity confirms zero Nifty 100 Q1 FY27 prints on Fri Jul 3 or over the weekend — earliest big print is HCLTECH on Jul 13. **REJECT — no PEAD candidates.**
2. **Momentum scan** — Yahoo history 429-throttled for 8 straight days; cannot compute 12-1 momentum, 50/200 DMA, 20-DMA pullback %, or RSI for any UNIVERSE name. UNIVERSE.md is now **61 days stale** (last rebuild 2026-05-06); rankings there are unreliable (VEDL divergence proven; ADANIPOWER cached +29.9% vs live +92.9% on 2026-06-18). **REJECT ALL — technical gate unevaluable; will not enter on stale rankings.**
3. **ADANIPOWER** (only live-vetted candidate from 2026-06-18: was in the 2-7% pullback window) — still cannot re-vet without live DMAs. Power sector also not confirmed hot in today's read (Perplexity source-limited on sector momentum). **REJECT — gate-data unavailable + sector confirm missing.**
4. **IT sector opportunistic thought** — Friday IT +3% is a *breakout*, not a pullback; UNIVERSE names TECHM/HCLTECH/INFY/WIPRO/TCS were all below both DMAs at last rebuild. Even if the rebound persists, no live technicals to confirm the DMA cross. **REJECT — chase, not pullback; also cannot verify.**

### Decision
**HOLD.** Forced HOLD, 2nd consecutive cycle: (a) zero PEAD candidates (no prints); (b) momentum gate unevaluable (Yahoo 429 + NSE null-quote outage entering day 8). Default action per STRATEGY.md. Patience > activity. Paper equity unchanged at ₹5,00,000; zero trades this week (week Mon Jul 6).

### Notes for market-open routine
- **Data feed fix remains blocker #1.** Recap of fix candidates from 2026-06-29 (none actioned yet):
  - nsepython: bump version or instrument `nse_eq()` — silent `{}` return implies a caught exception path.
  - Yahoo 429: swap to `yfinance` Python lib (session cookies), route via `query2.finance.yahoo.com`, or replace history source with NSE bhav files (`/products/content/equities/equities/bhavcopy.htm`).
  - Blocker #2 is the UNIVERSE rebuild (61 days stale) — depends on the same history endpoint being fixed.
- **No new entries today**; PEAD trigger is dormant until Jul 13 HCLTECH print (first live Q1 FY27 catalyst in UNIVERSE).
- Once feeds are back, run rebuild-universe BEFORE any entry decision.
- ADANIPOWER remains the queued momentum candidate from the June cycle. Re-vet DMAs + 20DMA pullback + Power sector confirm as soon as history feed unthrottles.
- Sector map to hold for market-open: IT rebounding on softer US jobs; PSU Banks weak; Auto weak into results. Nothing actionable without live technicals; use only for reject-side sector-drawdown checks.
- VEDL data divergence: still open (6th cycle), same Yahoo dependency.
