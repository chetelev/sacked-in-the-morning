# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Football fans who follow the Premier League and read r/PremierLeague or r/FantasyPL. They open the site for fun, mostly on a phone and often from a link shared in a thread or a group chat, to see which players the two subreddits are turning on and which they love this week. FPL managers checking who r/FantasyPL wants sold or bought are part of this audience, not its centre. Both subreddits matter equally.

## Product Purpose

Shows how two Reddit communities feel about each Premier League player right now, and how that changed through the season. Every comment that names a player is read and labelled; the site turns the labels into rankings and per-player stories. Success: a fan sees in seconds who is being slated and who is loved, trusts the numbers enough to share them, and can read the comments behind any verdict.

## Positioning

It reads every comment rather than a sample or a poll, refreshes every 15 minutes, and shows the words behind each number. The two subreddits are read in their own terms: r/PremierLeague as how a comment feels about a player (negative, neutral, positive), r/FantasyPL as what it tells managers to do (sell, hold, buy).

## Operating Context

- New comments come from Reddit's official API; the season before launch is filled from an archive download.
- Players, clubs, prices, ownership and gameweek deadlines come from the official FPL API.
- Jev (TypeSafe System One, pinned at jev-1.13.0) labels each comment once per player it names, with a confidence; it can also answer that a comment is not about that player.
- Time is counted in FPL gameweeks: a comment belongs to the gameweek whose deadline comes next.
- A scheduled GitHub job runs every 15 minutes, keeps its counts on a `data` branch and publishes the static site to GitHub Pages.
- Visitors arrive from Reddit threads and chats, on phones.

## Capabilities and Constraints

- Views built so far, all to be redesigned: a leaderboard per subreddit (most hated, loved and discussed; most sold, bought and debated), a player page (now and season, mood per gameweek, the comments behind it), a club overview, week-by-week winners, and a team of the week on a pitch. A season "race" was tried and rejected.
- Comments appear as short excerpts (up to 300 characters) linking to Reddit. Brand-new comments have no votes yet, so the comments shown are the ones with the clearest view, not the most upvoted.
- Rankings by share need a minimum number of comments, and every number shows how many comments it rests on.
- No official Premier League or FPL identity: no crests, player photos, kit designs, sponsor logos, the league's colours or fonts, and nothing that suggests the site is official. Clubs appear as plain shirts in their home colours.
- Static site in plain HTML, CSS and JavaScript with no build step; data as JSON files under `site/data/`, written by `update.py`.
- Undecided: whether r/FantasyPL's "no view" comments are shown anywhere; the minimum-comment thresholds, to be tuned on real volumes.

## Brand Commitments

- Name: **Sacked in the Morning**, after the terrace chant aimed at a struggling manager. The owner asked for old-school UK football slang that is easy to remember.
- Address: **sackedinthemorning.live** (chosen; free when checked, not yet registered).
- "Terrace" was rejected as a name.

## Evidence on Hand

- Real comments: `data/raw/FantasyPL.jsonl` (archive download from 1 August 2026, still filling); r/PremierLeague's download is queued behind it.
- A tested pipeline (`update.py`) that writes `site/data/summary.json` and one comments file per subreddit and gameweek.
- No published numbers yet, and no testimonials, traffic figures or press. Invented figures are never shown as real.

## Product Principles

1. Every number shows how many comments it rests on.
2. The comment is the proof: any verdict leads to the words behind it.
3. Both subreddits stand equally; neither is a footnote to the other.
4. Phone first: a fan gets the week's story one-handed in a few seconds.
5. Fan-made and clearly unofficial.
