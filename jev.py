"""The smallest TypeSafe System One client this site needs (docs.typesafe.ai/api).

Jev answers closed questions about a piece of state with probabilities and writes no text: here, one option of a
set ("choice") per player a comment names. One POST per call, retried on 429 and 529. The key stays in the
environment (JEV_API_KEY).
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-1.13.0"   # pinned: a new version can answer differently, so it is changed on purpose
TIMEOUT = 20
RETRIES = 4


def enabled() -> bool:
    return bool(os.environ.get("JEV_API_KEY"))


def ask(state, questions: dict, timeout: int = TIMEOUT) -> dict:
    """{"answers": {id: answer}, "tokens": n}; raises when the service cannot answer."""
    body = json.dumps({"model": MODEL, "state": state, "questions": questions}).encode()
    headers = {"Authorization": "Bearer " + os.environ["JEV_API_KEY"], "Content-Type": "application/json",
               "User-Agent": "SackedInTheMorning/0.1"}
    for attempt in range(RETRIES + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(ENDPOINT, data=body, headers=headers), timeout=timeout) as r:
                reply = json.loads(r.read().decode())
            return {"answers": reply["answers"], "tokens": (reply.get("usage") or {}).get("input_tokens", 0)}
        except urllib.error.HTTPError as error:
            if error.code not in (429, 529) or attempt == RETRIES:
                raise
            time.sleep(0.5 * 2 ** attempt)
