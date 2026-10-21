"""New comments from Reddit's official API, and a check of which saved comments still exist.

Reddit's data is only used with its approval: an approved 'script' app's ID and secret (REDDIT_CLIENT_ID,
REDDIT_CLIENT_SECRET) and application-only OAuth, read-only, no account password. Reddit asks for a User-Agent
naming the app and its owner (REDDIT_USER_AGENT, e.g. 'linux:sacked-in-the-morning:0.1 (by /u/name)'). The API
lists at most the newest 1,000 comments of a subreddit, far more than either one writes between two runs.
"""
from __future__ import annotations

import base64
import json
import os
import urllib.parse
import urllib.request

PAGES = 10   # 100 comments a page
_token_cache = {}


def _agent() -> str:
    return os.environ.get("REDDIT_USER_AGENT", "linux:sacked-in-the-morning:0.1")


def _token() -> str:
    if "token" not in _token_cache:
        if not (os.environ.get("REDDIT_CLIENT_ID") and os.environ.get("REDDIT_CLIENT_SECRET")):
            raise RuntimeError("REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET are not set: Reddit's data needs an approved app")
        pair = f"{os.environ['REDDIT_CLIENT_ID']}:{os.environ['REDDIT_CLIENT_SECRET']}".encode()
        request = urllib.request.Request("https://www.reddit.com/api/v1/access_token", data=b"grant_type=client_credentials",
                                         headers={"Authorization": "Basic " + base64.b64encode(pair).decode(), "User-Agent": _agent()})
        with urllib.request.urlopen(request, timeout=30) as r:
            _token_cache["token"] = json.load(r)["access_token"]
    return _token_cache["token"]


def _get(path: str, query: dict) -> dict:
    request = urllib.request.Request(f"https://oauth.reddit.com{path}?{urllib.parse.urlencode(query)}",
                                     headers={"Authorization": "Bearer " + _token(), "User-Agent": _agent()})
    with urllib.request.urlopen(request, timeout=30) as r:
        return json.load(r)["data"]


def _comment(c: dict) -> dict:
    return {"id": c["id"], "body": c.get("body") or "", "author": c.get("author") or "", "created_utc": int(c["created_utc"]),
            "permalink": c["permalink"], "thread": c.get("link_title") or ""}


def new_comments(subreddit: str, since: str) -> list:
    """Comments written after the comment `since` (a base-36 id; '' for the newest page), oldest first."""
    found, after = [], None
    for _ in range(PAGES):
        listing = _get(f"/r/{subreddit}/comments", {"limit": 100, "raw_json": 1, **({"after": after} if after else {})})
        page = [child["data"] for child in listing["children"]]
        fresh = [c for c in page if not since or int(c["id"], 36) > int(since, 36)]
        found += fresh
        if not since or len(fresh) < len(page) or not listing.get("after"):
            break
        after = listing["after"]
    return [_comment(c) for c in reversed(found)]


def still_there(ids: list) -> set:
    """Which of these comments are still up on Reddit; a deleted or removed comment is dropped from the site."""
    alive = set()
    for start in range(0, len(ids), 100):
        batch = ids[start:start + 100]
        for child in _get("/api/info", {"id": ",".join("t1_" + i for i in batch), "raw_json": 1})["children"]:
            c = child["data"]
            if c.get("author") != "[deleted]" and c.get("body") not in ("[deleted]", "[removed]"):
                alive.add(c["id"])
    return alive
