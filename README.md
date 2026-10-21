# Sacked in the Morning

Who r/PremierLeague and r/FantasyPL are turning on, and who they love, every gameweek. Every comment that names a
Premier League player is read and labelled, and the site updates every 15 minutes. Fan-made; no link to the
Premier League, Fantasy Premier League or Reddit.

## How it works

`.github/workflows/update.yml` runs `update.py` every 15 minutes:

1. New comments from both subreddits (`reddit.py`): Reddit's official API when the app keys are set, otherwise the
   Arctic Shift archive, which runs one to two hours behind.
2. The players each comment names (`mentions.py`), from the official FPL player list (`fpl.py`).
3. One question to Jev per player named (`jev.py`): sell, hold or buy on r/FantasyPL; negative, neutral or positive
   on r/PremierLeague; or "not about him".
4. The answers are added to the counts on the `data` branch, and `site/data/` is written for the page.
5. The site in `site/` is published to GitHub Pages.

A comment counts toward the gameweek whose FPL deadline comes next.

## Settings (repository secrets)

| Secret | What it is |
|---|---|
| `JEV_API_KEY` | TypeSafe System One key |
| `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` | a Reddit "script" app (reddit.com/prefs/apps); optional, without them the archive is used |
| `REDDIT_USER_AGENT` | e.g. `linux:sacked-in-the-morning:0.1 (by /u/yourname)` |

## Running it here

```
JEV_API_KEY=... python3 update.py --state state --site site
python3 -m http.server -d site 8000
```

`scripts/download.py` downloads a subreddit's past comments from the archive; `update.py --archive <file> --subreddit <name>`
adds them to the counts, for the part of the season before the first live run.

Design: `PRODUCT.md` (what it is for) and `DESIGN.md` (the visual system).
