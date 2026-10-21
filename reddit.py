"""Comments, newest from Reddit's official API or older ones from an archive download.

The API is read with application-only OAuth: a Reddit 'script' app's ID and secret (REDDIT_CLIENT_ID,
REDDIT_CLIENT_SECRET), no account password. Reddit asks for a User-Agent naming the app and its owner
(REDDIT_USER_AGENT, e.g. 'linux:sacked-in-the-morning:0.1 (by /u/name)'). It lists at most the newest 1,000
comments of a subreddit, far more than either one writes between two runs. Without the app's ID, new comments
come from the Arctic Shift archive instead, which runs one to two hours behind Reddit.
"""
from __future__ import annotations

import base64
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

PAGES = 10   # 100 comments a page
ARCHIVE = "https://arctic-shift.photon-reddit.com/api/comments/search"
ARCHIVE_FIELDS = "id,body,created_utc,link_id,author"
ARCHIVE_HOURS = 6   # how far back the archive is read when there is no API access


def _agent() -> str:
    return os.environ.get("REDDIT_USER_AGENT", "linux:sacked-in-the-morning:0.1")


def _token() -> str:
    pair = f"{os.environ['REDDIT_CLIENT_ID']}:{os.environ['REDDIT_CLIENT_SECRET']}".encode()
    request = urllib.request.Request("https://www.reddit.com/api/v1/access_token", data=b"grant_type=client_credentials",
                                     headers={"Authorization": "Basic " + base64.b64encode(pair).decode(), "User-Agent": _agent()})
    with urllib.request.urlopen(request, timeout=30) as r:
        return json.load(r)["access_token"]


def _comment(c: dict) -> dict:
    return {"id": c["id"], "body": c.get("body") or "", "author": c.get("author") or "", "created_utc": int(c["created_utc"]),
            "permalink": c["permalink"], "thread": c.get("link_title") or ""}


def new_comments(subreddit: str, since: str) -> list:
    """Comments written after the comment `since` (a base-36 id; '' for the newest page), oldest first."""
    if not os.environ.get("REDDIT_CLIENT_ID"):
        return _recent_from_archive(subreddit, since)
    token, found, after = _token(), [], None
    for _ in range(PAGES):
        query = {"limit": 100, "raw_json": 1, **({"after": after} if after else {})}
        request = urllib.request.Request(f"https://oauth.reddit.com/r/{subreddit}/comments?{urllib.parse.urlencode(query)}",
                                         headers={"Authorization": "Bearer " + token, "User-Agent": _agent()})
        with urllib.request.urlopen(request, timeout=30) as r:
            listing = json.load(r)["data"]
        page = [child["data"] for child in listing["children"]]
        fresh = [c for c in page if not since or int(c["id"], 36) > int(since, 36)]
        found += fresh
        if not since or len(fresh) < len(page) or not listing.get("after"):
            break
        after = listing["after"]
    return [_comment(c) for c in reversed(found)]


def _archive_comment(c: dict, subreddit: str) -> dict:
    return _comment({**c, "permalink": f"/r/{subreddit}/comments/{c['link_id'][3:]}/_/{c['id']}/"})


def _recent_from_archive(subreddit: str, since: str) -> list:
    """The archive's comments from the last few hours that are newer than `since`, oldest first."""
    now = int(time.time())
    after, found = now - ARCHIVE_HOURS * 3600, {}
    while after < now:
        query = urllib.parse.urlencode({"subreddit": subreddit, "after": after, "before": now, "limit": "auto",
                                        "sort": "asc", "fields": ARCHIVE_FIELDS})
        for attempt in range(4):   # the archive refuses requests when it is busy
            try:
                with urllib.request.urlopen(urllib.request.Request(f"{ARCHIVE}?{query}", headers={"User-Agent": _agent()}), timeout=60) as r:
                    page = json.load(r).get("data")
            except (urllib.error.URLError, TimeoutError):
                page = None
            if page is not None:
                break
            time.sleep(20)
        if not page:
            break
        found.update({c["id"]: c for c in page})
        if page[-1]["created_utc"] <= after:   # a whole page in one second; step past it
            after += 1
        else:
            after = page[-1]["created_utc"]
        if len(page) < 100:
            break
    fresh = [c for c in found.values() if not since or int(c["id"], 36) > int(since, 36)]
    return sorted((_archive_comment(c, subreddit) for c in fresh), key=lambda c: int(c["id"], 36))


def from_archive(path: str, subreddit: str) -> list:
    """An Arctic Shift download (scripts/download.py), oldest first; it has no thread titles."""
    comments = []
    with open(path) as f:
        for line in f:
            comments.append(_archive_comment(json.loads(line), subreddit))
    return sorted(comments, key=lambda c: int(c["id"], 36))
