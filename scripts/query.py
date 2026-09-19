#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""query.py — Look up Revit API signatures and version differences.

Data lives in the cloud (GitHub Pages) by default; a local `data/` cache is
used when present so offline lookups still work.

Usage
-----
    # find members by name (case-insensitive substring)
    python scripts/query.py member CopyModel
    python scripts/query.py member "GetAnalytical" --kind Method --since 2021

    # describe a type and list its members
    python scripts/query.py type Wall

    # what changed between two versions
    python scripts/query.py diff 2023 2024 --only added

    # force remote / local, override the remote base URL
    python scripts/query.py member ForgeTypeId --source remote
    python scripts/query.py member ForgeTypeId --base https://<user>.github.io/revit-api-kb

Exit codes: 0 found, 1 fatal, 2 nothing found.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import textwrap
from typing import Dict, List, Optional
from urllib.request import Request, urlopen

DEFAULT_BASE = "https://github.com"  # overridden via --base or REVIT_API_KB_BASE
USER_AGENT = "revit-api-kb/1.0"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
DEFAULT_DATA_DIR = os.path.join(SKILL_DIR, "data")


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------


def _local(path: str) -> Optional[dict]:
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    return None


def _remote(url: str, timeout: int = 60) -> Optional[dict]:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception as exc:  # noqa: BLE001
        print(f"[warn] remote fetch failed: {exc}", file=sys.stderr)
        return None


def load(name: str, source: str, base: str) -> Optional[dict]:
    """Load `name` (e.g. api_2024.json) from local cache or the remote site."""
    if source in ("auto", "local"):
        data = _local(os.path.join(DEFAULT_DATA_DIR, name))
        if data:
            return data
        if source == "local":
            return None
    if source in ("auto", "remote"):
        url = f"{base.rstrip('/')}/{name}"
        return _remote(url)
    return None


def resolve_version(source: str, base: str, preferred: str = "") -> Optional[dict]:
    for candidate in ([preferred] if preferred else []) + ["2024", "2023", "2025"]:
        data = load(f"api_{candidate}.json", source, base)
        if data:
            return data
    return None


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------


def cmd_member(args: argparse.Namespace) -> int:
    db = resolve_version(args.source, args.base, args.version)
    if not db:
        print("FATAL: no signature database available (try --source remote --base <url>)")
        return 1

    needle = args.pattern.lower()
    hits: List[dict] = []
    for member in db.get("members", []):
        if needle not in member.get("n", "").lower():
            continue
        if args.kind and member.get("k") != args.kind:
            continue
        if args.since and str(member.get("s", "")) < args.since:
            continue
        if args.type and args.type.lower() not in str(member.get("t", "")).lower():
            continue
        hits.append(member)
        if len(hits) >= args.limit:
            break

    if not hits:
        print(f"No member matching {args.pattern!r}")
        return 2

    print(f"Revit {db.get('version')} — {len(hits)} match(es)\n")
    for member in hits:
        header = f"{member['t']}.{member['n']}  [{member['k']}]"
        if member.get("s"):
            header += f"  since {member['s']}"
        if member.get("o"):
            header += "  [OBSOLETE]"
        print(header)
        if member.get("sig"):
            print(textwrap.fill(member["sig"], 96, initial_indent="    ", subsequent_indent="        "))
        if member.get("d") and args.desc:
            print(textwrap.fill(member["d"], 96, initial_indent="    ", subsequent_indent="    "))
        print()
    return 0


def cmd_type(args: argparse.Namespace) -> int:
    db = resolve_version(args.source, args.base, args.version)
    if not db:
        print("FATAL: no signature database available")
        return 1

    needle = args.pattern.lower()
    fq = [k for k in db.get("types", {}) if needle in k.lower()]
    if not fq:
        print(f"No type matching {args.pattern!r}")
        return 2

    for name in fq[: args.limit]:
        members = [
            m
            for m in db.get("members", [])
            if m.get("t", "") == name.rsplit(".", 1)[-1]
        ]
        print(f"{name}  [{db['types'][name].get('kind','')}]  {len(members)} members")
        for member in sorted(members, key=lambda m: (m.get("k", ""), m.get("n", "")))[
            : args.member_limit
        ]:
            since = f" since {member['s']}" if member.get("s") else ""
            print(f"  [{member['k']}]{since}  {member['n']}")
            if member.get("sig"):
                print(textwrap.fill(member["sig"], 96, initial_indent="      ", subsequent_indent="          "))
        print()
    return 0


def cmd_diff(args: argparse.Namespace) -> int:
    name = f"diff_{args.older}_{args.newer}.json"
    diff = load(name, args.source, args.base)
    if not diff:
        print(f"FATAL: {name} not found locally or remotely")
        return 1

    counts = diff.get("counts", {})
    print(f"Revit {diff.get('from')} -> {diff.get('to')}")
    for key, value in counts.items():
        print(f"  {key}: {value}")

    if args.only in ("", "added"):
        print("\n--- types added ---")
        for item in diff.get("types_added", [])[: args.limit]:
            print("  " + item)
        print("\n--- members added ---")
        for item in diff.get("members_added", [])[: args.limit]:
            print("  " + item)

    if args.only in ("", "removed"):
        print("\n--- types removed ---")
        for item in diff.get("types_removed", [])[: args.limit]:
            print("  " + item)
        print("\n--- members removed ---")
        for item in diff.get("members_removed", [])[: args.limit]:
            print("  " + item)

    if args.only in ("", "changed"):
        print("\n--- signature changes ---")
        for item in diff.get("members_changed", [])[: args.limit]:
            print(f"  {item['key']}")
            print(f"    - {item['old_sig']}")
            print(f"    + {item['new_sig']}")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    for version in args.versions:
        db = load(f"api_{version}.json", args.source, args.base)
        if not db:
            print(f"{version}: unavailable")
            continue
        counts = db.get("counts", {})
        print(
            f"{version}: types={counts.get('types',0)} "
            f"members={counts.get('members',0)} pages={counts.get('pages',0)}"
        )
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    # `common` uses SUPPRESS so the global flags work BOTH before and after the
    # subcommand (`query.py --source local member X` and `query.py member X --source local`).
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--source", choices=["auto", "local", "remote"], default=argparse.SUPPRESS)
    common.add_argument("--base", default=argparse.SUPPRESS,
                        help="remote base URL serving api_*.json / diff_*.json")
    common.add_argument("--version", default=argparse.SUPPRESS, help="preferred Revit version")
    common.add_argument("--limit", type=int, default=argparse.SUPPRESS)

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", choices=["auto", "local", "remote"],
                        default=os.environ.get("REVIT_API_KB_SOURCE", "auto"))
    parser.add_argument(
        "--base",
        default=os.environ.get("REVIT_API_KB_BASE", DEFAULT_BASE),
        help="remote base URL serving api_*.json / diff_*.json",
    )
    parser.add_argument("--version", default="", help="preferred Revit version")
    parser.add_argument("--limit", type=int, default=40)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_member = sub.add_parser("member", help="search members by name", parents=[common])
    p_member.add_argument("pattern")
    p_member.add_argument("--kind", default="", choices=["", "Method", "Property", "Constructor", "Event", "Field"])
    p_member.add_argument("--since", default="", help="only members introduced >= version, e.g. 2021")
    p_member.add_argument("--type", default="", help="restrict to a containing type")
    p_member.add_argument("--desc", action="store_true", help="print the summary text")
    p_member.set_defaults(func=cmd_member)

    p_type = sub.add_parser("type", help="describe a type and list its members", parents=[common])
    p_type.add_argument("pattern")
    p_type.add_argument("--member-limit", type=int, default=60)
    p_type.set_defaults(func=cmd_type)

    p_diff = sub.add_parser("diff", help="version differences", parents=[common])
    p_diff.add_argument("older", nargs="?", default="2023")
    p_diff.add_argument("newer", nargs="?", default="2024")
    p_diff.add_argument("--only", default="", choices=["", "added", "removed", "changed"])
    p_diff.set_defaults(func=cmd_diff)

    p_stats = sub.add_parser("stats", help="database sizes", parents=[common])
    p_stats.add_argument("versions", nargs="*", default=["2023", "2024"])
    p_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
