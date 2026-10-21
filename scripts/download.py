"""Download this season's comments for one subreddit from the Arctic Shift archive.

Usage: python3 scripts/download.py FantasyPL
Writes data/raw/<subreddit>.jsonl, one comment per line. Safe to stop and rerun:
it picks up after the newest comment already saved.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://arctic-shift.photon-reddit.com/api/comments/search"
FIELDS = "id,body,score,created_utc,link_id,parent_id,author,author_flair_text"
SEASON_START = 1785542400  # 2026-08-01 00:00 UTC
PAUSE = 1.0  # seconds between requests, to stay polite
DAY = 86400  # the archive rejects open-ended searches, so each request covers one day


def fetch(subreddit, after):
    query = urllib.parse.urlencode({
        "subreddit": subreddit, "after": after, "before": after + DAY, "limit": "auto",
        "sort": "asc", "fields": FIELDS,
    })
    req = urllib.request.Request(f"{API}?{query}", headers={"User-Agent": "reddit-pl-mood/0.1"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.load(resp)


def main(subreddit):
    out = Path(__file__).resolve().parent.parent / "data" / "raw" / f"{subreddit}.jsonl"
    seen, after = set(), SEASON_START
    if out.exists():
        for line in out.open():
            c = json.loads(line)
            seen.add(c["id"])
            after = max(after, c["created_utc"])

    now = int(time.time())
    with out.open("a") as f:
        while after < now:
            try:
                rows = fetch(subreddit, after).get("data")
            except Exception as e:
                rows = None
                print(f"retrying after error: {e}", flush=True)
            if rows is None:  # rate limited or timed out: wait and try again
                time.sleep(30)
                continue
            new = [c for c in rows if c["id"] not in seen]
            if not new:  # nothing left in this day, move to the next
                after += DAY
                continue
            for c in new:
                seen.add(c["id"])
                f.write(json.dumps(c) + "\n")
            # step past the newest timestamp unless the whole page shared one second
            last = rows[-1]["created_utc"]
            after = last if len(new) == len(rows) else last + 1
            print(f"{subreddit}: {len(seen):,} comments, up to {time.strftime('%Y-%m-%d %H:%M', time.gmtime(last))}", flush=True)
            time.sleep(PAUSE)
    print(f"{subreddit}: done, {len(seen):,} comments", flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
