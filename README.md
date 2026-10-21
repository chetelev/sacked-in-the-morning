# Sacked in the Morning

Who r/PremierLeague and r/FantasyPL are turning on, and who they love, every gameweek. Every comment that names a
Premier League player is read and labelled, and the site updates every 15 minutes. Fan-made; no link to the
Premier League, Fantasy Premier League or Reddit.

## How it works

`.github/workflows/update.yml` runs `update.py` every 15 minutes:

1. New comments from both subreddits (`reddit.py`), read-only through Reddit's official API with an approved app.
   Quotes whose comments were later deleted or removed are taken off the site on the next run.
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
| `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` | a Reddit "script" app (reddit.com/prefs/apps), approved for API access |
| `REDDIT_USER_AGENT` | e.g. `linux:sacked-in-the-morning:0.1 (by /u/yourname)` |
| `VOTER_KEY` | a random secret; commenters are counted by a fingerprint keyed with it, so no fingerprint can be traced to a username |

## Running it here

```
JEV_API_KEY=... REDDIT_CLIENT_ID=... REDDIT_CLIENT_SECRET=... VOTER_KEY=... python3 update.py --state state --site site
python3 -m http.server -d site 8000
```

Reddit's data is used only as its Responsible Builder Policy allows: read-only, two subreddits, no usernames published,
nothing sold or used to train models, deleted comments removed. The counts start from the first run with API access.

Design: `PRODUCT.md` (what it is for) and `DESIGN.md` (the visual system).
