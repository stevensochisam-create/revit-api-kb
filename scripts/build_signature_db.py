#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_signature_db.py — Build the Revit API signature knowledge base.

Reads the decompiled CHM tree of ADN-DevTech/revit-api-chms and emits one
compact JSON per Revit version plus a cross-version diff.

Typical cloud usage (GitHub Actions):
    python scripts/build_signature_db.py --fetch --versions 2023 2024 \
        --out-dir data

Local usage against an already-downloaded tree:
    python scripts/build_signature_db.py --source-root /tmp/chms \
        --versions 2024 --out-dir data

Outputs:
    data/api_<version>.json      signature database for one version
    data/version_diff.json       added / removed / changed between versions

Exit codes: 0 success, 1 fatal error, 2 validation failed.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Dict, List, Optional, Tuple

try:
    from lib_parse import (
        iter_toc_members,
        iter_toc_types,
        normalise_since,
        parse_hhc,
        parse_page,
    )
except ImportError:  # pragma: no cover - allows `python scripts/x.py` from repo root
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from lib_parse import (
        iter_toc_members,
        iter_toc_types,
        normalise_since,
        parse_hhc,
        parse_page,
    )

LOG = logging.getLogger("build_signature_db")

CHMS_REPO = "https://github.com/ADN-DevTech/revit-api-chms.git"

# Validation thresholds — a real Revit API has well over 10k members.
MIN_TYPES = 800
MIN_MEMBERS = 8000


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------


def _run(cmd: List[str], cwd: Optional[str] = None, timeout: int = 1800) -> Tuple[int, str]:
    LOG.debug("$ %s", " ".join(cmd))
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, proc.stdout or ""


def fetch_chms(dest: str, versions: List[str], shallow_filter: bool = True) -> str:
    """Sparse-clone only `html/<version>/` subtrees into `dest`.

    Uses a blobless partial clone so the 1 GB CHM binaries are never fetched.
    Returns the path containing `html/`.
    """
    os.makedirs(dest, exist_ok=True)
    cmd = ["git", "clone", "--depth", "1"]
    if shallow_filter:
        cmd += ["--filter=blob:none", "--sparse"]
    cmd += [CHMS_REPO, "chms"]
    code, out = _run(cmd, cwd=dest)
    if code != 0:
        raise RuntimeError(f"git clone failed ({code}): {out[-2000:]}")

    repo = os.path.join(dest, "chms")
    if shallow_filter:
        patterns = []
        for version in versions:
            patterns += [f"html/{version}"]
        code, out = _run(["git", "sparse-checkout", "set"] + patterns, cwd=repo)
        if code != 0:
            raise RuntimeError(f"sparse-checkout failed ({code}): {out[-2000:]}")
    return repo


# --------------------------------------------------------------------------
# Extraction
# --------------------------------------------------------------------------


def build_for_version(source_root: str, version: str, limit: Optional[int] = None) -> dict:
    """Parse one version's html tree into a compact signature database."""
    version_dir = os.path.join(source_root, "html", version)
    hhc_path = os.path.join(version_dir, "RevitAPI.hhc")
    if not os.path.isfile(hhc_path):
        raise FileNotFoundError(f"missing TOC: {hhc_path}")

    LOG.info("[%s] parsing TOC %s", version, hhc_path)
    toc = parse_hhc(hhc_path)
    if not toc:
        raise ValueError(f"empty TOC for {version}")

    types: Dict[str, dict] = {}
    for ns, name, kind, local in iter_toc_types(toc):
        fqname = f"{ns}.{name}" if ns else name
        types[fqname] = {"ns": ns, "kind": kind, "file": local, "since": ""}

    members: List[dict] = []
    parsed_pages = 0
    for owner, name, kind, local in iter_toc_members(toc):
        if limit is not None and len(members) >= limit:
            break
        page_path = os.path.join(version_dir, local.replace("/", os.sep))
        record = {
            "t": owner,
            "n": name,
            "k": kind,
            "s": "",
            "sig": "",
            "p": [],
            "d": "",
            "o": False,
        }
        try:
            with open(page_path, "r", encoding="utf-8-sig", errors="replace") as fh:
                page = parse_page(fh.read())
            parsed_pages += 1
        except (OSError, ValueError) as exc:
            LOG.debug("[%s] skip %s: %s", version, page_path, exc)
            members.append(record)
            continue

        record["sig"] = page.get("signature_cs", "")
        record["s"] = normalise_since(page.get("since", ""))
        record["p"] = page.get("parameters", [])[:12]
        record["d"] = (page.get("summary", "") or "")[:280]
        record["o"] = bool(page.get("obsolete"))
        members.append(record)

    LOG.info(
        "[%s] types=%d members=%d pages_ok=%d",
        version,
        len(types),
        len(members),
        parsed_pages,
    )
    return {
        "version": version,
        "generated": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "source": "ADN-DevTech/revit-api-chms (MIT)",
        "counts": {"types": len(types), "members": len(members), "pages": parsed_pages},
        "types": types,
        "members": members,
    }


def validate(db: dict) -> List[str]:
    """Return a list of validation problems; empty list means OK."""
    problems: List[str] = []
    counts = db.get("counts", {})
    if counts.get("types", 0) < MIN_TYPES:
        problems.append(f"types={counts.get('types')} < {MIN_TYPES}")
    if counts.get("members", 0) < MIN_MEMBERS:
        problems.append(f"members={counts.get('members')} < {MIN_MEMBERS}")
    with_sig = sum(1 for m in db.get("members", []) if m.get("sig"))
    ratio = with_sig / max(1, counts.get("members", 1))
    if ratio < 0.5:
        problems.append(f"signature coverage {ratio:.0%} < 50%")
    return problems


# --------------------------------------------------------------------------
# Diff
# --------------------------------------------------------------------------


def _member_key(record: dict, types_ns: Dict[str, str]) -> str:
    owner = record.get("t", "")
    return f"{owner}|{record.get('n','')}|{record.get('k','')}"


def diff_versions(older: dict, newer: dict) -> dict:
    """Compare two signature databases by member key."""
    def index(db: dict) -> Dict[str, dict]:
        out: Dict[str, dict] = {}
        for record in db.get("members", []):
            out[_member_key(record, {})] = record
        return out

    old_idx = index(older)
    new_idx = index(newer)
    added = sorted(set(new_idx) - set(old_idx))
    removed = sorted(set(old_idx) - set(new_idx))

    changed: List[dict] = []
    for key in sorted(set(old_idx) & set(new_idx)):
        old_sig = old_idx[key].get("sig", "")
        new_sig = new_idx[key].get("sig", "")
        if old_sig != new_sig:
            changed.append(
                {
                    "key": key,
                    "old_sig": old_sig[:300],
                    "new_sig": new_sig[:300],
                    "obsolete": new_idx[key].get("o", False),
                }
            )

    old_types = set(older.get("types", {}))
    new_types = set(newer.get("types", {}))
    return {
        "from": older.get("version"),
        "to": newer.get("version"),
        "generated": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "counts": {
            "members_added": len(added),
            "members_removed": len(removed),
            "members_changed": len(changed),
            "types_added": len(new_types - old_types),
            "types_removed": len(old_types - new_types),
        },
        "types_added": sorted(new_types - old_types),
        "types_removed": sorted(old_types - new_types),
        "members_added": [new_idx[k]["t"] + "." + new_idx[k]["n"] for k in added][:4000],
        "members_removed": [old_idx[k]["t"] + "." + old_idx[k]["n"] for k in removed][:2000],
        "members_changed": changed[:2000],
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="sparse-clone the CHMS repo first")
    parser.add_argument("--source-root", default="", help="existing checkout containing html/")
    parser.add_argument("--versions", nargs="+", default=["2023", "2024"])
    parser.add_argument("--out-dir", default="data")
    parser.add_argument("--limit", type=int, default=0, help="debug: cap members per version")
    parser.add_argument("--keep-source", action="store_true", help="do not delete fetched source")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    os.makedirs(args.out_dir, exist_ok=True)
    tmp_root = ""
    source_root = args.source_root

    try:
        if args.fetch:
            tmp_root = tempfile.mkdtemp(prefix="revit-api-kb-")
            LOG.info("fetching %s -> %s", CHMS_REPO, tmp_root)
            source_root = fetch_chms(tmp_root, args.versions)
        if not source_root:
            parser.error("need --source-root or --fetch")

        databases: Dict[str, dict] = {}
        for version in args.versions:
            db = build_for_version(
                source_root, version, limit=args.limit or None
            )
            problems = validate(db)
            if problems:
                LOG.warning("[%s] validation: %s", version, "; ".join(problems))
            out_path = os.path.join(args.out_dir, f"api_{version}.json")
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(db, fh, ensure_ascii=False, separators=(",", ":"))
            size_mb = os.path.getsize(out_path) / 1_048_576
            LOG.info("[%s] wrote %s (%.1f MB)", version, out_path, size_mb)
            databases[version] = db

        ordered = [v for v in args.versions if v in databases]
        for older_v, newer_v in zip(ordered, ordered[1:]):
            diff = diff_versions(databases[older_v], databases[newer_v])
            out_path = os.path.join(args.out_dir, f"diff_{older_v}_{newer_v}.json")
            with open(out_path, "w", encoding="utf-8") as fh:
                json.dump(diff, fh, ensure_ascii=False, indent=1)
            LOG.info(
                "diff %s->%s: %s", older_v, newer_v, json.dumps(diff["counts"])
            )
    except Exception as exc:  # noqa: BLE001 - top-level guard for CI logging
        LOG.error("FATAL: %s", exc, exc_info=args.verbose)
        return 1
    finally:
        if tmp_root and not args.keep_source:
            shutil.rmtree(tmp_root, ignore_errors=True)
            LOG.info("cleaned source %s", tmp_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
