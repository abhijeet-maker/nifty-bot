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

## 2026-05-02 — Pre-market

### Status: Weekend — no research

- NSE closed (Saturday). Confirmed via null RELIANCE quote.
- Exiting silently per procedure.

### ⚠️ Env var alert (action required before next weekday run)

The following environment variables were NOT set in this container:
- `PERPLEXITY_API_KEY` — MISSING
- `TELEGRAM_BOT_TOKEN` — MISSING
- `TELEGRAM_CHAT_ID` — MISSING

Perplexity queries and Telegram notifications will fail on next weekday (Mon 2026-05-04)
unless these are injected into the container env before the routine fires.
Check your container/cron env config and ensure all three are exported.
