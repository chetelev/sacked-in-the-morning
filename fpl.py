"""Players, clubs and gameweek deadlines from the official Fantasy Premier League API."""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime

BOOTSTRAP = "https://fantasy.premierleague.com/api/bootstrap-static/"
POSITIONS = {1: "GKP", 2: "DEF", 3: "MID", 4: "FWD"}


def display_name(e: dict) -> str:
    """'Erling Haaland', 'Bruno Fernandes'; the FPL short name when the full name is not what people call him."""
    tail = e["web_name"].rstrip(".").split(".")[-1]   # 'B.Fernandes' -> 'Fernandes'; 'Bruno G.' stays whole
    return f"{e['first_name'].split()[0]} {tail}" if tail and tail in e["second_name"] else e["web_name"]


def current(e: dict) -> bool:
    """Still at a Premier League club; departed and loaned-out players stay in the FPL list as unselectable."""
    return e.get("can_select", True) and e["status"] != "u"


def load() -> dict:
    request = urllib.request.Request(BOOTSTRAP, headers={"User-Agent": "SackedInTheMorning/0.1"})
    with urllib.request.urlopen(request, timeout=60) as r:
        data = json.load(r)
    clubs = {t["id"]: t["short_name"] for t in data["teams"]}
    players = [{"id": e["id"], "short": e["web_name"], "name": display_name(e), "second": e["second_name"],
                "club": clubs[e["team"]], "pos": POSITIONS[e["element_type"]], "price": e["now_cost"] / 10,
                "owned": float(e["selected_by_percent"])} for e in data["elements"] if current(e)]
    deadlines = [int(datetime.fromisoformat(ev["deadline_time"].replace("Z", "+00:00")).timestamp()) for ev in data["events"]]
    return {"players": players, "clubs": {t["short_name"]: t["name"] for t in data["teams"]}, "deadlines": deadlines}


def gameweek(ts: int, deadlines: list) -> int:
    """A comment counts toward the gameweek whose deadline comes next; after the last deadline, the last gameweek."""
    for i, deadline in enumerate(deadlines):
        if ts < deadline:
            return i + 1
    return len(deadlines)
