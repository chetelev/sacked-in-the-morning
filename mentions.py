"""Which tracked players a comment names.

A player is found by the names fans write: the FPL short name ('Haaland', 'Fernandes' from 'B.Fernandes'), the full
name, the surname and a few nicknames, ignoring case and accents. A name that is also an everyday word ('Rice',
'Hall') counts only with a capital letter. A wrong guess costs little: Jev is asked about every candidate and can
answer that the comment is not about him.
"""
from __future__ import annotations

import re
import unicodedata

MAX_NAMES = 6   # a comment naming more players is nearly always a team list, not a view on any of them
NICKNAMES = {"B.Fernandes": ["bruno"], "Alexander-Arnold": ["trent", "taa"], "Calvert-Lewin": ["dcl"],
             "Gibbs-White": ["mgw"], "Groß": ["gross"], "Ødegaard": ["odegaard"]}
COMMON = {"rice", "hall", "white", "wood", "king", "hill", "pope", "young", "bell", "gray", "gross", "cash", "stones",
          "mount", "burn", "ward", "page", "may", "little", "rose", "moore", "lamb", "bird", "west", "long", "son",
          "post", "sharp", "walker", "holding", "fry", "lowe", "dunk", "mings", "baldock", "case", "grant", "guess"}
SPECIAL = {"ø": "o", "đ": "d", "ł": "l", "ı": "i"}


def fold(text: str) -> str:
    """Lower case without accents, one character for one, so positions still match the original text."""
    return "".join(SPECIAL.get(c, unicodedata.normalize("NFKD", c)[0]) for c in text.lower())


def build(players: list) -> tuple:
    names = {}
    for p in players:
        surname = p["second"].split()[-1] if p["second"] else ""
        for name in {p["short"].rstrip(".").split(".")[-1], p["name"], p["second"], surname, *NICKNAMES.get(p["short"], [])}:
            key = fold(name).strip()
            if len(key) >= 3:
                names.setdefault(key, set()).add(p["id"])
    alternatives = "|".join(sorted(map(re.escape, names), key=len, reverse=True))
    return names, re.compile(rf"(?<![\w'])({alternatives})(?![\w'])")


def find(text: str, index: tuple) -> set:
    names, pattern = index
    found = set()
    for match in pattern.finditer(fold(text)):
        key = match.group(1)
        if key in COMMON and not text[match.start():match.start() + 1].isupper():
            continue
        found |= names[key]
    return found
