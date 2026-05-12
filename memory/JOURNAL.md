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

## 2026-05-12 — Pre-market

### Macro
- Nifty 50: ~23,800-24,000 zone, mildly soft tape; GIFT Nifty indicated -0.4% open
- Bank Nifty: ~54,000 (sitting on key support; below = 53,650)
- Hot sectors (1m): Pharma, Defence (per Perplexity narrative)
- Cold / no recovery signal: broad market still below 20-week EMA; weak undercurrent
- Today's events: DRREDDY, TATAPOWER, BPCL Q4 results post-market (Nifty 100). No FOMC/RBI/Budget today.
- **Ops note:** `nse.sh quote` and `nse.sh earnings` return null/empty — nsepython blocked. Yahoo (history, momentum) works. Earnings calendar reconstructed from Perplexity narrative cross-checked with Yahoo close data.

### Portfolio health
- Total positions: 0 of 5 max
- Paper equity: ₹5,00,000.00, Cash: ₹5,00,000.00, Deployed: 0%
- Trades this week (Mon 05-11 onwards): 0 of 2 max
- Concerns: none (no open positions)

### Candidates considered
**PEAD scan (results Fri 05-08 / Mon 05-11, names in UNIVERSE):**
1. TITAN (Cons Durables) — PEAD — close 05-07 ₹4307.5 → 05-08 ₹4509.0 (+4.68%, met gap) → 05-11 ₹4205.6 (-6.73%, **faded through pre-results level**). **REJECT** — failed "held the gain" rule. Also now below 50DMA.
2. BRITANNIA (FMCG) — PEAD — 05-08 close ₹5520 vs 05-07 ₹5814 = **-5.06% on results day**. **REJECT** — results-day reaction negative.
3. PIDILITIND (Chemicals) — PEAD — 05-08 +1.77% only; faded to ₹1437.2 on 05-11. **REJECT** — gap below +3% threshold and faded.

**Momentum scan (top-of-UNIVERSE by 12-1):**
4. VEDL (Metals) — last ₹298.4 vs 50DMA ₹647.9 / 200DMA ₹559.7. **REJECT** — below both DMAs (still suspected corporate action; flagged 05-06).
5. BEL (Cap Goods) — last ₹431.95, 50DMA ₹438.6 → -1.5% below 50DMA. **REJECT** — below 50DMA.
6. ADANIPOWER (Power) — last ₹222.03, above both DMAs ✓, mom +65.25% ✓, but **+5.1% ABOVE 20DMA** and **RSI-14 = 70.7** (overbought). **REJECT** — extended, not 2-7% below 20DMA, RSI outside 50-70 band.
7. HEROMOTOCO (Auto) — below both DMAs. **REJECT**.
8. EICHERMOT (Auto) — above both DMAs ✓, mom +35.3% ✓, RSI 51, but **-0.07% vs 20DMA** (at 20DMA, not in 2-7% pullback band). **REJECT** — no pullback entry.
9. HINDZINC (Metals) — above both DMAs ✓, mom +33.6% ✓, but **+4.31% ABOVE 20DMA**, RSI 62.5. **REJECT** — extended, not in pullback zone.

### Decision
**HOLD.** Zero candidates passed the entry gates. PEAD names all failed reaction/drift; momentum leaders all extended above 20DMA or below DMA gate. Patience > activity per STRATEGY.md default.

### Notes for market-open routine
- No action at open.
- DRREDDY reports tonight — already in UNIVERSE; potential PEAD candidate for tomorrow's pre-market if both beats + >3% reaction the day after.
- BPCL also reports tonight (in UNIVERSE), but BPCL is in the cold Oil/Gas sector and well below DMAs — even a beat would fail sector confirm.
- Watch ADANIPOWER and HINDZINC for a 20DMA pullback into the 2-7% band — they remain best momentum setups if/when they pull back.
- Re-test `nse.sh quote` and `nse.sh earnings` at next routine; if still null after 24h, escalate (nsepython upstream issue).
