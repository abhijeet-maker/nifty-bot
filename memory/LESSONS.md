# Lessons Learned

Durable mistakes, codified. Read by EVERY routine, so this file must stay short.

## Cap: 20 bullets max.

If a 21st is added during weekly review, the oldest/least-actionable gets pruned.
A bullet that is fully absorbed into STRATEGY.md can also be removed (with a note
in that week's review).

## Format

```
- YYYY-MM-DD: [what happened in one clause]. [Why it was wrong]. **Rule: [the lesson as a rule]**.
```

Every lesson should end with a crisp rule the agent can apply in pre-market's
candidate gate. If you can't phrase it as a rule, it's not ready to be a lesson —
let it mature another week.

## Examples of what belongs here (once earned by real mistakes)

- Entering on a sector catalyst without checking sector momentum first
- Sizing up after a win (hot-hand fallacy)
- Holding past a thesis break because "stop hasn't hit yet"
- Trading on results day itself instead of day after
- Chasing gap-ups more than 3% above planned entry

## Examples of what does NOT belong

- Generic market wisdom ("don't average down") — that's already in STRATEGY.md
- One-off bad luck outcomes where the process was correct
- Anything phrased as advice to a human trader (this is for an LLM agent)

---

_(Seed — empty. Lessons are earned, not assumed.)_

- 2026-07-03: Rejected candidates weekly across 4+ pre-market cycles on "DMA gate fails" while the underlying Yahoo history feed was either 429-throttled or serving unadjusted corporate-action data (VEDL). Silent-stale rejects look identical to legitimate rejects in the journal but produce zero learning. **Rule: before writing any "REJECT — gate fails" verdict, verify feed health with `nse.sh momentum RELIANCE` (or any known-live symbol). If that returns non-null with a plausible DMA, feeds are good and the reject stands. If it 429s or returns null, downgrade the day's verdict to "DATA-BLOCKED HOLD" and Telegram-alert the failure mode. Do not silently REJECT on unverifiable data.**

