# Nifty Bot — Autonomous Indian Equity Research Agent

An autonomous research and journaling agent for Nifty 100 swing trading, powered
by Claude Opus 4.7 running on scheduled cloud routines. Currently in **PAPER
TRADING MODE** — the agent researches and recommends, you execute manually on
Kite, the agent logs paper fills and grades its own performance weekly.

## What it does

Five scheduled routines per week:

| Routine | Schedule | What it does |
|---|---|---|
| Pre-market | Mon-Fri 8:15 AM IST | Research PEAD + momentum candidates, write trade plan |
| Market-open | Mon-Fri 9:20 AM IST | Validate plan with live data, send BUY alert to Telegram |
| Midday | Mon-Fri 12:30 PM IST | Check stops, tighten trails, flag thesis breaks |
| EOD | Mon-Fri 4:00 PM IST | Mark-to-market, log snapshot, send daily summary |
| Weekly review | Fri 5:00 PM IST | Grade the week, update LESSONS, rebuild UNIVERSE |

All routines read/write seven markdown files in `memory/` which are the agent's
entire brain. The repo IS the database.

## Prerequisites

| Service | What for | Cost |
|---|---|---|
| GitHub account + private repo | Code + memory storage | Free |
| Claude Code cloud routines | Agent runtime | Included with Claude Pro/Max |
| Perplexity API (`sonar` model) | Market research with citations | ~₹400/mo |
| Telegram Bot | Notifications to your phone | Free |
| Screener.in | Fundamental data (scraped) | Free (optional ₹1,999/yr) |
| Zerodha Kite | Manual paper-trade execution | Free (CNC delivery) |

Total cost: **~₹400-₹550/month** (Perplexity only).

## Setup — first hour

### 1. Create Telegram bot (5 minutes)
- Open Telegram, message `@BotFather`
- Send `/newbot`, pick a name and username (e.g. `niftybot_yours`)
- Save the HTTP API token it gives you
- Message your new bot something (say hi)
- Visit `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` in a browser
- Find `"chat":{"id":123456789}` — that's your `TELEGRAM_CHAT_ID`

### 2. Get Perplexity API key (3 minutes)
- Sign up at https://www.perplexity.ai/settings/api
- Add ~$10 credit (lasts ~3 months at this query volume)
- Copy the `pplx-...` key

### 3. Clone this repo
```bash
git clone <your-github-url> nifty-bot
cd nifty-bot
cp env.template .env
# Edit .env and fill in: PERPLEXITY_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
```

### 4. Local smoke test
Open the repo in Claude Code (desktop or CLI) and run:
```
/smoke-test
```

All 9 checks must PASS before you touch cloud routines. Common failures:
- NSE quote fails → often transient, retry in 1 minute
- Screener fails → Screener's rate limiter; wait 10 minutes, it's not broken
- Telegram fails → wrong chat_id; re-check `getUpdates`

### 5. Build the first universe
```
/rebuild-universe
```
This takes 4-8 minutes on first run (populates the cache). Subsequent rebuilds
only refresh stale entries (30-day TTL). Verify `memory/UNIVERSE.md` has ~30-45
names in the filtered table.

Commit:
```bash
git add -A
git commit -m "initial setup"
git push origin main
```

### 6. Set up cloud routines (once per routine — 5 routines)

Prereqs:
- Install the Claude GitHub App on your private repo
- In routine settings, enable **"Allow unrestricted branch pushes"** — this is the #1 thing that silently breaks first-time setups

For each of the 5 routines:
1. Claude Code cloud → **Routines** → **New routine**
2. Name: e.g. "Nifty pre-market"
3. Repository: your nifty-bot repo, branch `main`
4. Environment variables (paste these exactly, NOT in a .env file):
   - `PERPLEXITY_API_KEY`
   - `PERPLEXITY_MODEL=sonar`
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
5. Schedule (timezone: **Asia/Kolkata**):
   - Pre-market: `15 8 * * 1-5`
   - Market-open: `20 9 * * 1-5`
   - Midday: `30 12 * * 1-5`
   - EOD: `0 16 * * 1-5`
   - Weekly review: `0 17 * * 5`
6. **Paste the prompt verbatim** from the matching `routines/*.md` file.
   Do NOT paraphrase. The env-var block and commit-push step are load-bearing.
7. Click **Run now** once to test.

After first successful run of each routine, verify:
- A new commit appears on `main` with an appropriate message
- Telegram message received (for routines that always send)
- `memory/` files were updated correctly

## How to use the system day-to-day

You do almost nothing. Each morning:

1. **7:30 AM IST**: Wake up. Check Telegram.
2. **8:30 AM IST**: Agent has posted pre-market research (only if urgent).
3. **9:20 AM IST**: If a trade was recommended, agent Telegrams: `✅ PAPER BUY HDFCBANK × 60 @ ~₹1650`
4. **Paper-mode**: You *don't* actually execute — the agent already logged the paper fill. Just acknowledge you saw it.
5. **12:30 PM IST**: Usually silent. If you get a `🛑` message, a stop hit.
6. **4:00 PM IST**: Daily summary lands — equity, day P&L, tomorrow's watchlist.
7. **Friday 5:00 PM**: Weekly grade. Read the `memory/WEEKLY-REVIEW.md` entry.

Your real job during the 90-day paper phase:
- **Read the journal** every day. Understand why the agent recommended what it did.
- **Track the grade trend.** Bs or better for 8+ weeks → consider going live with small capital.
- **Don't override the agent.** If you find yourself wanting to ignore its HOLDs and trade on gut, the agent is doing its job — you have the impulse it's protecting you from.

## Directory layout

```
nifty-bot/
├── CLAUDE.md                  # Auto-loaded agent persona + rules quick-ref
├── README.md                  # This file
├── env.template               # Copy to .env for local dev (gitignored)
├── .gitignore                 # Excludes .env
├── .claude/commands/          # Local slash commands
│   ├── portfolio.md
│   ├── smoke-test.md
│   └── rebuild-universe.md
├── routines/                  # Cloud routine prompts (paste into Claude Code cloud)
│   ├── pre-market.md
│   ├── market-open.md
│   ├── midday.md
│   ├── eod.md
│   └── weekly-review.md
├── scripts/                   # Bash wrappers — the ONLY way the agent touches the outside world
│   ├── nse.sh                 # Live prices, history, earnings calendar, momentum
│   ├── screener.sh            # Fundamental data from Screener.in
│   ├── perplexity.sh          # Narrative research
│   ├── telegram.sh            # Notifications
│   ├── paper.sh               # Paper fill simulator with slippage
│   └── universe-cache.sh      # 30-day TTL cache for fundamentals
└── memory/                    # Agent's brain — committed to git every run
    ├── STRATEGY.md            # Rulebook (quasi-immutable)
    ├── UNIVERSE.md            # Quality-filtered watchlist (rebuilt weekly)
    ├── PORTFOLIO.md           # Current paper positions
    ├── TRADE-LOG.md           # Every trade + daily EOD snapshots
    ├── JOURNAL.md             # Daily research log
    ├── WEEKLY-REVIEW.md       # Friday reviews with letter grades
    ├── LESSONS.md             # Distilled mistakes (capped at 20)
    └── .fundamentals-cache/   # Screener cache per symbol
```

## Realistic expectations

**What this system is good at:**
- Not letting you skip research before a trade
- Catching thesis breaks within 3 hours instead of 3 days
- Tightening stops on winners you'd otherwise get greedy with
- Producing an honest weekly grade that tells you if you're actually good

**What it will NOT do:**
- Pick 10-baggers. It will not find the next big multibagger — that's not the strategy.
- Beat Nifty every week. Expect 45-55% weekly win rate. The edge compounds monthly, not daily.
- Save you in a bear market. If Nifty drops 20%, you drop 12-16%. The edge is relative, not absolute.

**Realistic return targets (after costs):**
- Paper phase (90 days): Beat Nifty by +2-5% cumulative
- Year 1 live: Nifty + 3-6% annualized
- Max drawdown expected: -18 to -25% at some point

If you aren't prepared to see your ₹5L become ₹4L at some point over a year, this
is not a strategy for you. Anyone promising steadier returns is lying or
hasn't lived through a bad year.

## Troubleshooting

See `routines/*.md` — each prompt has a "first-run" failure mode documented inline.
The #1 issue on first setup is forgetting to enable "Allow unrestricted branch pushes"
on the cloud routine. Symptom: git push fails with a proxy error. Fix: toggle it on.

**If Screener breaks** (they change HTML every 6-18 months): the weekly-review
routine will send a `🚨 UNIVERSE COLLAPSE` Telegram alert if fewer than 15 names
pass the quality screen. That's your signal to update the parser in `scripts/screener.sh`.
Until fixed, no new trades — stale universe means no candidates — but existing
positions continue to be managed normally (midday stops, EOD marks still work via
`nse.sh` which is independent).

**Data separation (important):** Screener is the sole source for fundamentals
(ROCE, D/E, pledge). Perplexity is the sole source for narrative (news,
consensus beats, management commentary). The agent is instructed to NEVER
substitute Perplexity for fundamental numbers, because LLMs hallucinate rates
when source data is missing.

## License

Private use only. Not financial advice. You take your own risk.
