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

## 2026-05-07 — Pre-market

### Macro
- Nifty 50: 24,330.95 (May 6 close, +1.24%, +298 pts); Nifty futures (May 26) ₹24,466 (+1.49%) → bullish open expected. Support 24,100/23,800; resistance 24,500/24,800.
- Bank Nifty: consolidating near highs; support 54,300-54,500; resistance 55,500-55,600.
- Hot sectors (1m): Banks/Financials, Consumer/FMCG (lower input costs), IT stabilizing. FII rotation into India from AI-heavy markets supportive.
- Cold/rolling over: Midcap IT (faded post-Jan), select smallcaps weakening; Bharat Forge (auto component) flagged sell — but core auto OEMs remain strong (HEROMOTOCO, EICHERMOT, BAJAJ-AUTO all positive 12-1).
- Today's events: No FOMC/RBI. Q4 results today (post-market) for PIDILITIND, DABUR, BAJAJHLDNG (per Perplexity) — none currently held.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week: 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
1. **BAJAJ-AUTO** (Auto) — **PEAD** — Q4 FY26 reported 2026-05-06 post-market: revenue ₹16,006 cr (+32% YoY) vs consensus ₹15,422-15,539 cr; PAT ₹2,746 cr (+34% YoY) vs consensus ₹2,541-2,585 cr; EBITDA margin 20.8% (+60bps); record volumes 13.71L (+24% YoY); ₹150/share dividend. **Beat both rev AND PAT.** Today: last ₹10,390, +3.42% vs prev close ₹10,046 (held the gain, near intraday high). Above 50DMA ₹9,515 and 200DMA ₹9,122 (mom +15.72%). In UNIVERSE.md. Sector OK (auto OEMs leading, only Bharat Forge — a component maker, not in UNIVERSE — flagged weak). **Decision: TRADE.**
2. **GODREJCP** (FMCG) — PEAD — Q4 reported 2026-05-06: revenue ₹3,885 cr (+11% YoY), PAT ₹452 cr (+10%); aligned with pre-quarter guidance, no clear consensus beat documented; price faded -0.34% today. **REJECT** — fails beat criterion AND fails ">3% on results day" rule.
3. PIDILITIND, DABUR, BAJAJHLDNG — report today post-market → revisit tomorrow's pre-market.

### Decision
**TRADE — PAPER BUY BAJAJ-AUTO**
- Trigger: PEAD post Q4 FY26 beat + strong reaction (+3.42%)
- Entry range: ₹10,250-10,400 (limit; reject if open gaps >2% above 10,400)
- Quantity: 9 shares (= ~₹93,510 = 18.7% of paper equity, under 20% cap)
- Stop: ₹9,560 (-8% from ₹10,390 reference)
- Target (first trail-tighten): ₹12,470 (+20%)
- R:R: ~2.50:1
- Thesis tag: PEAD-Q4FY26-beat
- Sector cap after entry: Auto = 1 of 2

### Notes for market-open routine
- Confirm BAJAJ-AUTO opens within ₹10,250-10,400 limit. If gaps >2% above ₹10,400 (i.e., > ₹10,608) — SKIP, do not chase (LESSONS-style risk).
- Use `paper.sh buy BAJAJ-AUTO 9 <fill_price>` after confirming fill price from quote.
- Place stop at ₹9,560 immediately after fill (paper-simulated).
- Update PORTFOLIO.md with fill, stop, target, deployed %.
- Stock at 52w high (₹10,477.50) — be tight on entry discipline; if it gaps and runs, walk away.

