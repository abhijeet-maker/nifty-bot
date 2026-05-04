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

## 2026-05-04 — Pre-market

### Macro
- Nifty 50: ~23,998 (last close Thu); GIFT Nifty: 24,229.5 (+0.34%) — positive open
- Bank Nifty: neutral-bearish, support 55,200, resistance 56,000-56,500
- VIX: >20 (risk-off tone)
- Hot sectors: Defence, Capital Goods, Auto (improving)
- Cold sectors: FMCG, Realty, Energy, Metals, Media, PSE
- Today's events: Q4 FY26 results (AMBUJACEM, BHEL, KOTAKBANK) — none in filtered UNIVERSE
- No RBI MPC, FOMC, or Budget event today

### Portfolio health
- Total positions: 0 of 5 max (first session, paper trading begins today)
- Paper equity: ₹5,00,000, Cash: ₹5,00,000, Deployed: 0%
- Concerns: none

### Candidates considered
- PEAD: No earnings on 2026-05-02 or 2026-05-03 in universe — zero PEAD candidates
- Momentum scan (top 5 by 12-1 mom in UNIVERSE.md):
  1. VEDL (Metals, +58%) — REJECT: last ₹271 vs 50DMA ₹701 / 200DMA ₹565 — far below both DMAs; Metals sector cold
  2. BEL (Defence, +35%) — REJECT: last ₹431 vs 50DMA ₹439 (-1.8%) — below 50DMA by 1.8%; fails DMA filter; WATCH: hot sector, reclaim of ₹439 would make this a candidate
  3. ADANIPOWER (Energy, +37%) — REJECT: passes both DMAs (last ₹222 vs 50DMA ₹164 / 200DMA ₹145), >18% momentum, but Energy sector is rolling over — fails sector criterion
  4. HEROMOTOCO (Auto, +30%) — REJECT: below both 50DMA (₹5,330) and 200DMA (₹5,384)
  5. TVSMOTOR (Auto, +23%) — REJECT: below 50DMA (₹3,647); 200DMA borderline pass

### Decision
HOLD — No candidate clears all gates. Best near-miss is BEL: defence sector hot, momentum strong, but fails the above-50DMA filter by 1.8%. Will reassess if BEL reclaims ₹439.

### Notes for market-open routine
- Monitor BEL intraday: if it closes convincingly above ₹440, flag for tomorrow's pre-market as momentum-pullback candidate — check 20DMA distance and RSI at that point
- ADANIPOWER structurally fine on price, but sector must turn before entry is valid
- VEDL: apparent massive breakdown vs universe snapshot (₹271 vs DMAs near ₹700) — flag for universe rebuild this Friday to verify data or re-screen

