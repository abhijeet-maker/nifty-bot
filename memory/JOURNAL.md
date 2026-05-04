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
- Not assessed (no pre-market routine ran before market-open)

### Portfolio health
- 0 open positions, ₹5,00,000 cash, 0 trades this week

### Candidates considered
- None — pre-market routine had not run before market-open fired

### Decision
- HOLD — no candidate to evaluate

### Notes for market-open routine
- Market-open ran at ~9:20 AM; found no pre-market entry in JOURNAL.md (seed state)
- No STEP 2–5 actions taken; nothing to validate, no trade to simulate

### Market-open execution 2026-05-04
- No pre-market candidate found → no trade executed
- Portfolio remains: 0 positions, ₹5,00,000 cash
