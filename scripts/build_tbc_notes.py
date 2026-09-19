#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_tbc_notes.py — Harvest The Building Coder into Note / Pitfall nodes.

Source: jeremytammik/tbc (MIT), 2081 posts, 2008-08 .. 2026-02.

Strategy (no 2 GB clone required):
  1. Fetch `a/toc/chrono-data.json` (407 KB) — every post's num/file/title/date.
  2. Filter by theme keywords applied to post TITLES.
     (NB: tbc's own `toc-data.json` topic taxonomy is legacy 2013-era and
      contains none of the modern themes, so title+body filtering is used.)
  3. Fetch only the matched posts from GitHub Pages (no API rate limit).
  4. Grep each fetched body for "hard" migration terms to tag Pitfalls.
  5. Emit data/tbc_notes.json.

Usage:
    python scripts/build_tbc_notes.py --out-dir data
    python scripts/build_tbc_notes.py --out-dir data --max-posts 60   # smoke test
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as _dt
import json
import logging
import os
import re
import sys
from typing import Dict, List, Optional
from urllib.request import Request, urlopen

LOG = logging.getLogger("build_tbc_notes")

SITE = "https://jeremytammik.github.io/tbc/a"
CHRONO = "https://api.github.com/repos/jeremytammik/tbc/contents/a/toc/chrono-data.json"
USER_AGENT = "revit-api-kb/1.0 (+knowledge base builder)"

# Theme -> title regex. Grouped so a post can match several themes.
THEMES: Dict[str, str] = {
    "ElementId": r"element\s*id|elementid|64\s*bit",
    "Parameter": r"forgetypeid|parameter|built-in param|shared param|\bbip\b|specid|unittypeid",
    "Toposolid": r"toposolid|topograph|graded region",
    "Transaction": r"transaction",
    "DynamoPython": r"dynamo|python|ironpython|cpython|pyrevit|revitservices",
    "LinkedModel": r"linked|revitlink|copy.?monitor|worksharing",
    "Geometry": r"geometry|solid|boolean|intersect|transform|curve|face|boundingbox",
    "MEP": r"\bmep\b|duct|pipe|conduit|cable tray|hvac|plumbing|sprinkler",
    "Schedule": r"schedul|material takeoff",
    "Units": r"\bunit|units",
    "VersionMigration": r"what.?s new|api changes|migration|deprecat|20(1[5-9]|2\d)",
}

# Body-level markers that turn a matched post into a migration Pitfall.
# (canonical label, pattern) — the label is stored, not the raw matched text,
# otherwise filenames end up as junk like "ElementId) As Long".
PITFALL_TERMS = [
    ("ForgeTypeId", r"ForgeTypeId"),
    ("Toposolid", r"Toposolid"),
    ("ElementId64Bit", r"ElementId[^.\n]{0,24}(?:64|Int64|long)"),
    ("UnitTypeId", r"UnitTypeId"),
    ("SpecTypeId", r"SpecTypeId"),
    ("DisplayUnitType", r"DisplayUnitType"),
    ("DotNet8", r"(?:\.NET\s*(?:Core\s*)?8|net8\.0)"),
    ("ObsoleteApi", r"obsolete"),
    ("DeprecatedApi", r"deprecated"),
]
PITFALL_RE = re.compile(
    "(?P<lbl>" + "|".join(f"(?:{pat})" for _, pat in PITFALL_TERMS) + ")", re.I
)

_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")
_SCRIPT_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)
_PRE_RE = re.compile(r"<pre[^>]*>(.*?)</pre>", re.S | re.I)
_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)


def _get(url: str, timeout: int = 60) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
    return raw.decode("utf-8", errors="replace")


def _text(fragment: str) -> str:
    fragment = _SCRIPT_RE.sub(" ", fragment)
    return _WS_RE.sub(" ", re.sub(r"<[^>]+>", " ", fragment)).strip()


def fetch_chrono() -> List[dict]:
    """Fetch the post index via the contents API with the raw media type."""
    req = Request(
        CHRONO,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github.raw",
        },
    )
    with urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read().decode("utf-8", errors="replace"))
    posts = data.get("posts") or []
    LOG.info("chrono index: %d posts", len(posts))
    return posts


def filter_posts(posts: List[dict]) -> List[dict]:
    """Attach `themes` to each post; return only posts matching >=1 theme."""
    compiled = {name: re.compile(pat, re.I) for name, pat in THEMES.items()}
    matched: List[dict] = []
    for post in posts:
        title = post.get("title") or ""
        themes = [name for name, rx in compiled.items() if rx.search(title)]
        if themes:
            post = dict(post)
            post["themes"] = themes
            matched.append(post)
    LOG.info("title-filter matched %d / %d posts", len(matched), len(posts))
    return matched


def fetch_post(post: dict) -> Optional[dict]:
    """Fetch one post page and extract plain text + code snippets."""
    url = f"{SITE}/{post['file']}"
    try:
        html_text = _get(url, timeout=60)
    except Exception as exc:  # noqa: BLE001 - network best effort
        LOG.debug("fetch failed %s: %s", url, exc)
        return None

    # The archive pages use a generic <title> ("The Building Coder"), so the
    # chrono-data index title (the real post title) always wins.
    page_title = ""
    title_match = _TITLE_RE.search(html_text)
    if title_match:
        page_title = _text(title_match.group(1))
    generic = page_title.lower() in ("", "the building coder", "the building coder archive")
    title = post.get("title", "") if (generic or not page_title) else page_title

    body_html = _SCRIPT_RE.sub(" ", html_text)
    body_text = _WS_RE.sub(" ", _TAG_RE.sub(" ", body_html)).strip()

    snippets: List[str] = []
    for match in _PRE_RE.finditer(body_html):
        snippet = _WS_RE.sub(" ", _TAG_RE.sub("", match.group(1))).strip()
        snippet = re.sub(r"^\s*\d+\s*$", "", snippet)
        if 40 <= len(snippet) <= 3000:
            snippets.append(snippet[:3000])
        if len(snippets) >= 8:
            break

    pitfall_hits = sorted(
        {label for label, pattern in PITFALL_TERMS if re.search(pattern, body_text, re.I)}
    )
    themes = list(post.get("themes", []))
    if pitfall_hits:
        themes.append("Pitfall")

    return {
        "num": post.get("num"),
        "file": post.get("file"),
        "title": title or post.get("title", ""),
        "date": post.get("date", ""),
        "year": post.get("year"),
        "url": url,
        "themes": sorted(set(themes)),
        "pitfall_terms": pitfall_hits[:10],
        "snippets": snippets,
        "text_len": len(body_text),
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", default="data")
    parser.add_argument("--max-posts", type=int, default=0, help="cap fetches (smoke test)")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )
    os.makedirs(args.out_dir, exist_ok=True)

    try:
        posts = fetch_chrono()
    except Exception as exc:  # noqa: BLE001
        LOG.error("FATAL: cannot fetch chrono index: %s", exc)
        return 1

    candidates = filter_posts(posts)
    if args.max_posts:
        # Keep a spread across themes rather than the first N chronologically.
        by_theme: Dict[str, List[dict]] = {}
        for post in candidates:
            for theme in post["themes"]:
                by_theme.setdefault(theme, []).append(post)
        picked: Dict[int, dict] = {}
        per_theme = max(1, args.max_posts // max(1, len(by_theme)))
        for theme, group in by_theme.items():
            group.sort(key=lambda p: p.get("date", ""), reverse=True)
            for post in group[:per_theme]:
                picked[post["num"]] = post
        candidates = list(picked.values())
        LOG.info("smoke test: capped to %d posts", len(candidates))

    notes: List[dict] = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch_post, p): p for p in candidates}
        done = 0
        for future in cf.as_completed(futures):
            done += 1
            if done % 50 == 0:
                LOG.info("  fetched %d / %d", done, len(candidates))
            result = future.result()
            if result:
                notes.append(result)

    notes.sort(key=lambda n: (n.get("date") or ""), reverse=True)

    payload = {
        "source": "jeremytammik/tbc (MIT) — The Building Coder archive",
        "generated": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "themes": list(THEMES),
        "counts": {
            "archive_posts": len(posts),
            "title_matched": len(candidates),
            "fetched": len(notes),
            "with_snippets": sum(1 for n in notes if n["snippets"]),
            "pitfalls": sum(1 for n in notes if "Pitfall" in n["themes"]),
        },
        "notes": notes,
    }

    out_path = os.path.join(args.out_dir, "tbc_notes.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, separators=(",", ":"))
    LOG.info("wrote %s (%.1f MB) %s", out_path,
             os.path.getsize(out_path) / 1_048_576, payload["counts"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
