"""One update: take new comments, find the players they name, ask Jev what each comment says about each of them,
add the answers to the saved state and write the site's data files.

  python3 update.py          new comments from Reddit's API (an approved app), both subreddits

Settings come from the environment: JEV_API_KEY, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT and
VOTER_KEY, the secret that makes commenter fingerprints impossible to trace back to usernames.

Saved state (the `data` branch on GitHub; a folder here):
  cursor.json                 per subreddit, the newest comment read ("last")
  <subreddit>/gw<N>.json      per player: each commenter's latest view (one vote per person, by a short fingerprint)
                              and the clearest few comments of each answer
Site data, written to <site>/data/:
  summary.json                players, deadlines and every count; one small download
  <fpl|pl>-gw<N>.json         the clearest comments of one gameweek, fetched when a player page opens
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import fpl
import jev
import mentions
import reddit

SUBREDDITS = {
    "FantasyPL": {"key": "fpl", "ask": "What does this comment say Fantasy Premier League managers should do with {player}?",
                  "answers": {"sell": "Sell him, transfer him out, bench him or avoid him",
                              "hold": "Keep him, do not sell yet, or wait and see",
                              "buy": "Buy him, bring him in, start him or captain him",
                              "none": "Names him without saying what to do: a question, a fact, a team list or a joke"}},
    "PremierLeague": {"key": "pl", "ask": "How does this comment feel about {player}?",
                      "answers": {"negative": "Criticises him, mocks him or is unhappy with him",
                                  "neutral": "Mixed, or a plain fact or question about him with no feeling either way",
                                  "positive": "Praises him, defends him or is happy with him"}},
}
ELSEWHERE = {"elsewhere": "The comment is not about this footballer (someone else, or the word means something else)"}
POSITIONS = {"GKP": "goalkeeper", "DEF": "defender", "MID": "midfielder", "FWD": "forward"}
SKIP_AUTHORS = {"AutoModerator", "[deleted]"}
KEEP = 3          # clearest comments kept per player, gameweek and answer
TEXT = 300        # characters of a comment kept for the site
WORKERS = 8       # Jev requests at once
MAX_FAILED = 0.2  # above this share of failed Jev requests nothing is saved, so the next run reads the same comments


def clean(body: str) -> str:
    """The commenter's own words: quoted lines dropped, whitespace collapsed."""
    own = [line for line in body.splitlines() if not line.lstrip().startswith(">")]
    return re.sub(r"\s+", " ", " ".join(own)).strip()


def judge(sub: str, comment: dict, players: list, clubs: dict):
    """[(player id, answer, confidence)] for one comment, or None when Jev could not answer."""
    config = SUBREDDITS[sub]
    criteria = {**config["answers"], **ELSEWHERE}
    questions = {f"p{p['id']}": {"type": "choice", "criteria": criteria, "instructions": config["ask"].format(
        player=f"{p['name']} ({clubs[p['club']]} {POSITIONS[p['pos']]})")} for p in players}
    state = {"subreddit": f"r/{sub}", "thread": comment["thread"], "comment": comment["text"][:1500]}
    try:
        answers = jev.ask(state, questions)["answers"]
    except Exception as error:   # one comment's failure is counted, not fatal
        print(f"  jev could not answer {comment['id']}: {error}", file=sys.stderr)
        return None
    return [(p["id"], answers[f"p{p['id']}"]["choice"], answers[f"p{p['id']}"]["confidence"]) for p in players]


def book(books: dict, state_dir: Path, sub: str, gw: int) -> dict:
    if (sub, gw) not in books:
        path = state_dir / sub / f"gw{gw}.json"
        books[sub, gw] = json.loads(path.read_text()) if path.exists() else {"players": {}}
    return books[sub, gw]


def voter(author: str) -> str:
    """A short keyed fingerprint of the commenter: repeat posts are recognised, and without the secret key nobody can
    match a fingerprint to a username."""
    return hashlib.blake2b(author.encode(), digest_size=6, key=os.environ["VOTER_KEY"].encode()[:64]).hexdigest()


def add(entry: dict, answer: str, confidence: float, comment: dict) -> None:
    if answer == "none":   # a comment with no view leaves the commenter's earlier view standing
        return
    entry["votes"][voter(comment["author"])] = answer   # comments arrive oldest first, so the latest view wins
    kept = entry["top"].setdefault(answer, [])
    kept.append({"id": comment["id"], "text": comment["text"][:TEXT], "at": comment["created_utc"],
                 "conf": round(confidence, 3), "link": "https://www.reddit.com" + comment["permalink"]})
    kept.sort(key=lambda c: (-c["conf"], -c["at"]))
    del kept[KEEP:]


def write_site(state_dir: Path, site_dir: Path, data: dict) -> None:
    out = site_dir / "data"
    out.mkdir(parents=True, exist_ok=True)
    counts, talked = {}, set()
    for sub, config in SUBREDDITS.items():
        answers = [a for a in config["answers"] if a != "none"]
        counts[config["key"]] = {}
        for path in sorted((state_dir / sub).glob("gw*.json")):
            gw, players = int(path.stem[2:]), json.loads(path.read_text())["players"]
            counts[config["key"]][gw] = {pid: [list(e["votes"].values()).count(a) for a in answers] for pid, e in players.items() if e["votes"]}
            talked |= set(counts[config["key"]][gw])
            clearest = {pid: e["top"] for pid, e in players.items() if e["top"]}
            (out / f"{config['key']}-gw{gw}.json").write_text(json.dumps(clearest, ensure_ascii=False, separators=(",", ":")))
    players = [[p["id"], p["short"], p["name"], p["club"], p["pos"], p["price"], p["owned"]]
               for p in data["players"] if str(p["id"]) in talked]
    summary = {"updated": int(time.time()), "deadlines": data["deadlines"], "clubs": data["clubs"], "players": players, "counts": counts}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, separators=(",", ":")))


def prune(books: dict, state_dir: Path, gws: list) -> None:
    """Drop saved quotes whose comments were deleted or removed on Reddit since they were read."""
    for sub in SUBREDDITS:
        for gw in gws:
            players = book(books, state_dir, sub, gw)["players"]
            ids = [c["id"] for e in players.values() for kept in e["top"].values() for c in kept]
            if not ids:
                continue
            alive = reddit.still_there(ids)
            for e in players.values():
                for answer, kept in e["top"].items():
                    e["top"][answer] = [c for c in kept if c["id"] in alive]
            if len(alive) < len(ids):
                print(f"r/{sub} gameweek {gw}: {len(ids) - len(alive)} deleted comments taken off the site")


def load_fpl(state_dir: Path) -> dict:
    """The official FPL list, saved with the state so one refused request does not stop an update."""
    saved = state_dir / "fpl.json"
    try:
        data = fpl.load()
    except Exception as error:
        if not saved.exists():
            raise
        print(f"the FPL API did not answer ({error}); using the copy saved with the state", file=sys.stderr)
        return json.loads(saved.read_text())
    saved.parent.mkdir(parents=True, exist_ok=True)
    saved.write_text(json.dumps(data, ensure_ascii=False))
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--state", default="state", help="folder of the saved state")
    parser.add_argument("--site", default="site", help="folder of the site")
    parser.add_argument("--limit", type=int, help="read at most this many comments per subreddit (for trying it out)")
    args = parser.parse_args()
    if not jev.enabled():
        sys.exit("JEV_API_KEY is not set")
    if not os.environ.get("VOTER_KEY"):
        sys.exit("VOTER_KEY is not set: fingerprints would be traceable to usernames")

    state_dir, site_dir = Path(args.state), Path(args.site)
    data = load_fpl(state_dir)
    index, by_id = mentions.build(data["players"]), {p["id"]: p for p in data["players"]}
    cursor_path = state_dir / "cursor.json"
    cursor = json.loads(cursor_path.read_text()) if cursor_path.exists() else {}
    books, failed_any = {}, False

    for sub in SUBREDDITS:
        mark = cursor.setdefault(sub, {})
        comments = reddit.new_comments(sub, mark.get("last", ""))
        comments = comments[:args.limit] if args.limit else comments

        work = []
        for c in comments:
            text = clean(c["body"])
            if c["author"] in SKIP_AUTHORS or not text or text in ("[deleted]", "[removed]"):
                continue
            ids = mentions.find(text, index)
            if ids and len(ids) <= mentions.MAX_NAMES:
                work.append(({**c, "text": text}, [by_id[i] for i in sorted(ids)]))
        with ThreadPoolExecutor(WORKERS) as pool:
            results = list(pool.map(lambda w: judge(sub, w[0], w[1], data["clubs"]), work))

        failed = sum(r is None for r in results)
        print(f"r/{sub}: {len(comments)} comments, {len(work)} name a player, {failed} Jev could not answer")
        if work and failed / len(work) > MAX_FAILED:
            failed_any = True
            continue   # this subreddit's comments are read again next time
        for (comment, _), result in zip(work, results):
            gw = fpl.gameweek(comment["created_utc"], data["deadlines"])
            players = book(books, state_dir, sub, gw)["players"]
            for pid, answer, confidence in result or []:
                if answer != "elsewhere":
                    add(players.setdefault(str(pid), {"votes": {}, "top": {}}), answer, confidence, comment)
        if comments:
            mark["last"] = max((mark.get("last") or "0", comments[-1]["id"]), key=lambda i: int(i, 36))

    live = fpl.gameweek(int(time.time()), data["deadlines"])
    prune(books, state_dir, sorted({max(1, live - 1), live}))
    for (sub, gw), saved in books.items():
        path = state_dir / sub / f"gw{gw}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(saved, ensure_ascii=False, separators=(",", ":")))
    state_dir.mkdir(parents=True, exist_ok=True)
    cursor_path.write_text(json.dumps(cursor, indent=1))
    write_site(state_dir, site_dir, data)
    if failed_any:
        sys.exit("Jev could not answer too many comments; those were left for the next run")


if __name__ == "__main__":
    main()
