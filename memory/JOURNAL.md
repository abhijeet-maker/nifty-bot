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

## 2026-07-10 — EOD

### EOD 2026-07-10
- Equity ₹5,00,000.00 (day 0.00%, phase 0.00%)
- vs Nifty 50 (+0.93%): alpha -0.93% (cash drag)
- Bank Nifty +0.90%. Zero positions, zero trades. No pre-market/midday routine fired between 2026-06-29 and today (11 calendar days silent) — scheduled cycles broken since the data-feed outage.
- Data-feed outage still active: `nse.sh quote` returns all-null, `nse.sh history` HTTP 429 from Yahoo. Verified this EOD run. Blocking all entry-gate evaluation.
- UNIVERSE.md now ~65 days stale (last rebuild 2026-05-06). ADANIPOWER pullback setup from 2026-06-18 still unactioned.
- Tomorrow (2026-07-13 Mon) watchlist: fix data feeds FIRST, then rebuild UNIVERSE, then re-scan ADANIPOWER pullback. TCS reports 2026-07-09 (already passed with no PEAD signal captured due to outage). Broader Q1 FY27 reporting season now live — PEAD scan window opens with every trading day.

## 2026-07-13 — Pre-market

### Macro
- Nifty 50: 24,206.90 (Jul 10 close, +1.02%, +244 pts); Sensex 77,569 (+1.08%); India VIX 13.36 (-9%). Nifty reclaimed 200DMA for first time since Feb — supports/resistances 24,165/24,055 vs 24,300/24,420.
- Bank Nifty: 58,046 (+1.39%). GIFT Nifty bias: positive/bullish carry-over.
- Hot sectors (1w): Realty (+3.5% Fri), PSU Banks (+3%), IT (+2%, TCS-lift); Financial Services strongest 1-month (SBI Life +4.42% weekly, HDFC Bank Q1 update strong).
- Cold / rolling over: no clear sector breakdown per weekend reads; broad recovery tape.
- Today's events: **HCLTECH reports Q1 FY27 post-market (~post 3:30 PM IST)** — sole Nifty 100 print today. No FOMC / RBI / budget. Not a blackout day.
- Q1 FY27 heavy week ahead: Tue Tata Elxsi/LTTS; Wed Wipro/TechM/BHEL/Polycab/JIOFIN; Thu RIL/Tata Tech/JSWSTEEL/HAVELLS; Fri HDFCBANK/ICICIBANK/AXISBANK/KOTAKBANK.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-07-13 → Fri 2026-07-17)
- Concerns: none (no open positions). 14th consecutive silent cycle — routine has been unable to trade since inception due to (a) rules-driven HOLDs in May/Jun, and (b) data-feed outage since 2026-06-29.

### Data feed outage (CRITICAL — 15 days active, still unresolved)
- Re-verified this cycle: `nse.sh quote RELIANCE` → all-null JSON (nsepython silently failing, likely NSE cookie/API drift). `nse.sh history/momentum` → Yahoo HTTP 429 on `query1.finance.yahoo.com/v8/finance/chart/*.NS` from this container IP.
- `nse.sh earnings 2026-07-09` and `2026-07-10` return `[]` — earnings calendar feed also stale (missed TCS Jul 9 print; Perplexity confirms TCS did report).
- Working: `perplexity.sh` (macro/narrative), `universe-cache.sh get` (Screener fundamentals only — no prices, no DMAs).
- Impact: BOTH triggers unevaluable. PEAD needs live prices to confirm ">+3% on results day + held gain". Momentum needs 50/200/20-DMA, RSI, 12-1 momentum. All fail without live technicals.
- **This is now blocking the entire Q1 FY27 PEAD window.** 4 mega-cap results days this week (Wed, Thu, Fri × 2) — each represents 2-4 potential PEAD candidates in UNIVERSE. Every day of continued outage forfeits the strategy's primary alpha source.

### Candidates considered
1. PEAD scan — `nse.sh earnings 2026-07-10` returned `[]`; Perplexity confirms no Nifty 100 names reported Friday. TCS reported Thu 2026-07-09 (still within 1-2 trading day PEAD window). **REJECT TCS** — Perplexity reports: revenue MISSED consensus (flat QoQ USD vs. expected sequential growth), EPS MATCHED (not beat). Per STRATEGY.md must beat BOTH — fails PEAD gate on beat criterion. Separately, TCS 12-1 momentum -28.23% in stale UNIVERSE (worst-ranked). No PEAD candidates today.
2. Momentum scan — Yahoo 429 durably blocks 50/200/20-DMA, RSI, and live 12-1 momentum for every UNIVERSE name. **REJECT ALL** — gate-data unavailable.
3. ADANIPOWER (carry-over watchlist) — Screener snapshot price ₹226 (Jun 25 vintage). Cannot re-verify pullback zone (2-7% below 20DMA) without live history. **REJECT** — stale technicals; will not enter blind.

### Decision
**HOLD.** Forced HOLD for the third consecutive cycle: (a) zero valid PEAD (TCS fails beat gate; no Fri prints); (b) momentum gate unevaluable due to persistent Yahoo 429 + NSE null-quote outage. Default action per STRATEGY.md.

### Notes for market-open routine
- **Fix data feeds — TOP PRIORITY, blocking everything.** Concrete next steps for operator:
  - Yahoo 429: this container's egress IP is flagged. Try (1) yfinance Python lib with a session cookie primed from a real browser, (2) route history via NSE bhavcopy (`https://www.nseindia.com/api/reports?archives=daily-reports`), (3) alt provider (Kite Connect, Zerodha, or Screener price API).
  - NSE null-quote: `nsepython.nse_eq()` is returning `{}` — likely swallowing a 401/403. Instrument the wrapper to log the raw HTTP status; likely needs cookie priming via `nse_get_top_gainers()` warm-up as documented in nsepython issues.
  - Earnings calendar: `nse.sh earnings` also stale — same NSE cookie issue is likely upstream cause.
- **Once feeds are back**, execute IN ORDER: (a) `rebuild-universe` (68 days stale — top priority), (b) re-run ADANIPOWER momentum gate, (c) scan for PEAD from any of this week's Q1 heavyweights (HCLTECH tonight; Wipro/TechM/JIOFIN Wed; RIL/JSWSTEEL/HAVELLS Thu; HDFCBANK/ICICIBANK/AXISBANK/KOTAKBANK Fri) at T+1 open using the live intraday reaction on results day.
- **HCLTECH is in UNIVERSE (IT, mom -8.33% stale but sector now hot on TCS-driven rerating)**. If it beats revenue+EPS tonight AND opens Tue with +3% gap holding, it's this week's first PEAD candidate.
- VEDL data divergence — still open across 6 cycles. Resolution gated on same Yahoo history feed being restored.
- Blackout note: no held-position results conflict this week (0 positions), so results-day blackout inactive.


## 2026-07-15 — Pre-market

### Macro
- Nifty 50: 24,052.05 (Jul 14 close, **-0.66%**, -158.95 pts); GIFT Nifty pre-open not sourced, but Tue's -0.68% GIFT bias flagged the risk-off tape.
- Bank Nifty: 57,507.10 (**-1.07%**, -624 pts) — worse than Nifty; PSU/private bank pressure.
- Hot sectors (YTD & recent): **Metal +14.80%**, **Pharma +12.91%**, **Energy +9.94%**. Recent weekly IT rebounded (+2.4-2.86% wk ended Jul 3) on TCS-driven rerating but HCLTECH's -3.19% Tue reaction reversed that lift.
- Cold / rolling over: **IT -27.49% YTD** (weakest), PSU Bank pressure, Capital Market -1.51% and Defence -1.65% intraday Tue.
- Today's events: **NO Nifty 100 Q1 FY27 print scheduled today.** Big-4 IT split: HCLTECH Mon (done, missed price gate), Wipro Thu, TechM Thu. RIL Fri, HDFCBANK/ICICIBANK Fri. Not a blackout day. **NO FOMC / RBI / budget.**
- Backdrop drag: US-Iran / West Asia escalation → **Brent >$86**, FII selling ₹3,062 cr Mon, rupee **96.22/$** (weak on higher-than-expected Jun retail inflation).

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max (week Mon 2026-07-13 → Fri 2026-07-17)
- Concerns: none (no open positions). **15th consecutive silent cycle.**

### Data feed outage (CRITICAL — 17 days active, still unresolved)
- Re-verified this cycle: `nse.sh quote RELIANCE` → all-null JSON (nsepython silently failing). `nse.sh history RELIANCE 5` → curl 22 / HTTP 429 from Yahoo. `nse.sh momentum HCLTECH` → same 429. `nse.sh earnings 2026-07-14` → `[]` (missed Tata Elxsi/LTTS prints; those are not Nifty 100 anyway).
- Working: `perplexity.sh` (macro/narrative), `universe-cache.sh get` (Screener fundamentals).
- Impact unchanged: PEAD needs live price on results day; momentum needs DMAs/RSI. Both gates unevaluable from raw feeds. **Only Perplexity narrative on price reaction saves the PEAD gate today** (see HCLTECH below).

### Candidates considered
1. **HCLTECH — PEAD (Q1 FY27, Mon 2026-07-13 post-market)** — Beat BOTH gates: revenue ₹34,579 cr (+13.9% YoY), net profit ₹4,624 cr (+20.3%), EPS ₹66.90 — Street polls exceeded. Guidance retained unchanged (revenue 1-4% CC, EBIT 17.5-18.5%). AI bookings record, AI rev +62%. Nomura raised TP to ₹1,290, reiterated Buy. **BUT: stock fell -3.19% Tue on results reaction (open ₹1,204.80, low ₹1,182.60, close ~₹1,185-1,190). Per STRATEGY.md PEAD trigger: "Gapped up >3% on results day and held the gain" — FAILED. Beat-but-fade is the anti-PEAD signature (guidance not raised + risk-off tape absorbed the beat).** REJECT PEAD.
2. **Other Nifty 100 PEAD** — No Nifty 100 results Mon-Tue beyond HCLTECH. Tata Elxsi + LTTS reported Tue but are Nifty IT mid-caps, NOT Nifty 100 — off-universe, no PEAD signal for us. REJECT — no other candidates.
3. **Momentum scan** — Yahoo 429 still durably blocks 50/200/20-DMA, RSI, and live 12-1 momentum for every UNIVERSE name. Sector filter would favor VEDL/HINDZINC (Metals hot), DRREDDY/DIVISLAB (Pharma hot), ADANIPOWER/COALINDIA (Energy hot) — but I cannot verify the 2-7% below 20DMA pullback gate or RSI 50-70 gate on any of them without live data. REJECT ALL — gate-data unavailable.
4. **ADANIPOWER carry-over** — Screener snapshot price ₹226 (Jun 25 vintage, now 20 days stale). Cannot re-verify pullback zone. REJECT — stale technicals; will not enter blind.

### Decision
**HOLD.** Fourth consecutive HOLD in a row (routine has run four times since 2026-06-29 with same outcome). Today's forced HOLD is doubly justified: (a) the ONE actionable PEAD candidate (HCLTECH) explicitly failed the price-reaction gate — a rule-correct rejection, not a data-shortage rejection; (b) momentum gate remains unevaluable due to persistent 429 outage; (c) risk-off macro backdrop (oil spike, weak rupee, FII outflows) argues for patience regardless. Default action per STRATEGY.md.

### Notes for market-open routine
- **HCLTECH: DO NOT chase.** Tuesday's beat-fade is a clean STRATEGY.md rejection. Any bounce today is not a PEAD entry (window has closed on the price-gate criterion). If it becomes a momentum-pullback candidate later, that's a separate gate — but IT is the weakest YTD sector, so even a re-qualify would fail the "sector positive 1-month momentum" gate.
- **Fix data feeds — TOP OPERATIONAL PRIORITY (17-day outage now).** Concrete next steps unchanged from 2026-07-13 note: (1) Yahoo 429 — swap to yfinance with session cookies, or NSE bhavcopy, or Kite Connect; (2) NSE null-quote — instrument nsepython to log HTTP status, add cookie warm-up via `nse_get_top_gainers()`; (3) NSE earnings calendar — likely same cookie issue.
- **Q1 FY27 heavy calendar this week — every day without feeds is forfeited PEAD alpha.** Big prints landing: Thu Wipro + TechM (IT — cold sector, but PEAD trigger is beat-agnostic to sector cold if reaction is strong); Fri RIL, HDFCBANK, ICICIBANK, AXISBANK, KOTAKBANK (Financial Services — sector strong per weekly). Fri's bank print cluster is the single biggest PEAD opportunity of the quarter for this strategy. **Must have live prices by Friday open** to catch it.
- **UNIVERSE.md is 70 days stale (last 2026-05-06).** Once feeds are back, rebuild-universe BEFORE any entry. Stale ranking compounds outage risk.
- **VEDL data divergence — still open across 7 cycles.** Blocked on same Yahoo history feed.
- No held-position concerns (0 positions). No Telegram alert warranted — nothing urgent.


## 2026-07-17 — Market-open

### State on wake
- No pre-market entry logged for 2026-07-17 (Fri). Pre-market routine did NOT fire this morning — 16th silent cycle in a row.
- Last pre-market decision (2026-07-15) was HOLD. Per market-open workflow STEP 1: HOLD → skip to STEP 6, exit clean, silence.
- 0 open positions, ₹5,00,000 cash, 0 trades this week. No candidate ticker to re-validate at 9:20 AM.

### Feed re-check at 9:20 IST
- `nse.sh quote RELIANCE` → all-null (nsepython still silently failing).
- `nse.sh momentum HDFCBANK` → curl 22 / HTTP 429 (Yahoo still throttled).
- `nse.sh earnings 2026-07-17` → `[]` (calendar feed stale — Friday IS heavy PEAD day with RIL/HDFCBANK/ICICIBANK/AXISBANK/KOTAKBANK scheduled; the empty return is a feed failure, not a truly empty calendar).
- 19-day data outage now. No change from 2026-07-15 diagnosis.

### Missed opportunity — flagged for the record
- **Today is the single biggest scheduled PEAD day of Q1 FY27 for this strategy**: HDFCBANK, ICICIBANK, AXISBANK, KOTAKBANK all reporting (Financial Services was the strongest 1-mo sector per Mon's macro read). Also RIL (Energy — hot YTD).
- With the outage active, none of these PEAD candidates can be evaluated at T+1 open (Mon 2026-07-20). This is the specific alpha-forfeiture scenario Wed's pre-market note called out ("must have live prices by Friday open").
- No action possible; documenting so post-outage review can attribute the gap correctly.

### Decision
**No-op.** No pre-market plan to execute, no live feeds to re-scan against, no held positions to manage. Silent exit per STRATEGY.md default.

### Notes for midday / EOD routines
- If feeds return before EOD, run `rebuild-universe` FIRST (72 days stale), then scan Friday's earnings prints (RIL/HDFCBANK/ICICIBANK/AXISBANK/KOTAKBANK) for T+1 PEAD setups Monday morning.
- Do NOT send Telegram on this cycle — pre-market was implicit HOLD, no trade attempted, no operational change. Notification rule: silence on no-op.
- Data-feed remediation remains the top operational priority. Unchanged next-steps from 2026-07-15 note.

