#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_vault.py — Turn the signature DB + TBC notes into an Obsidian vault
and a static searchable site.

Layout (mirrors graphify's Obsidian output style):
    vault/Class/<Namespace>.<Type>.md
    vault/Version/<version>.md
    vault/Pitfall/<term>.md
    vault/Note/<num>-<title>.md
    vault/index.md
    vault/graph.canvas
    site/index.html          single-page search UI
    site/search-index.json   trimmed index loaded by the UI

Usage:
    python scripts/build_vault.py --data-dir data --vault vault --site site
"""

from __future__ import annotations

import argparse
import datetime as _dt
import html as html_mod
import json
import logging
import os
import re
from collections import Counter, defaultdict
from typing import Dict, List, Optional

LOG = logging.getLogger("build_vault")

SITE_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Revit API Knowledge Base</title>
<style>
:root{--bg:#fbfbfa;--fg:#1f2328;--mut:#6b7280;--acc:#2563eb;--bd:#e5e7eb;--cd:#ffffff}
@media(prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--mut:#8b949e;--acc:#58a6ff;--bd:#30363d;--cd:#161b22}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);
font:14px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",sans-serif}
header{padding:20px 24px 8px;border-bottom:1px solid var(--bd)}
h1{margin:0 0 4px;font-size:19px}.meta{color:var(--mut);font-size:12px}
main{max-width:980px;margin:0 auto;padding:20px 24px 80px}
#q{width:100%;padding:12px 14px;font-size:15px;border:1px solid var(--bd);
border-radius:8px;background:var(--cd);color:var(--fg)}
#q:focus{outline:2px solid var(--acc);outline-offset:1px}
.bar{display:flex;gap:8px;margin:14px 0;flex-wrap:wrap;align-items:center}
.chip{padding:4px 10px;border:1px solid var(--bd);border-radius:999px;
background:var(--cd);cursor:pointer;font-size:12px;color:var(--fg)}
.chip.on{background:var(--acc);border-color:var(--acc);color:#fff}
#stat{color:var(--mut);font-size:12px;margin:6px 0 18px}
.card{border:1px solid var(--bd);border-radius:10px;padding:14px 16px;margin:0 0 12px;background:var(--cd)}
.card h3{margin:0 0 4px;font-size:15px}
.card .ns{color:var(--mut);font-size:12px}
.card pre{margin:8px 0 0;padding:10px 12px;background:rgba(125,125,125,.1);
border-radius:6px;overflow-x:auto;font-size:12.5px}
.card table{width:100%;border-collapse:collapse;margin-top:8px;font-size:12.5px}
.card td{padding:3px 6px;border-top:1px solid var(--bd);vertical-align:top}
.card td.k{color:var(--mut);white-space:nowrap;width:1%}
.badge{display:inline-block;padding:1px 7px;border-radius:999px;font-size:11px;
background:rgba(37,99,235,.12);color:var(--acc);margin-left:6px}
.empty{color:var(--mut);padding:30px 0;text-align:center}
</style></head><body>
<header><h1>Revit API Knowledge Base</h1>
<div class="meta">__META__</div></header>
<main>
<input id="q" placeholder="Search: Wall.GetAnalyticalModel / ForgeTypeId / Toposolid ..." autofocus>
<div class="bar" id="filters"></div>
<div id="stat"></div>
<div id="out"><div class="empty">Loading index…</div></div>
</main>
<script>
const KINDS=["Method","Property","Constructor","Event","Field"];
let IDX=[],active=null;
function esc(s){return (s||"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));}
fetch("search-index.json").then(r=>r.json()).then(d=>{
  IDX=d.items||[];
  document.querySelector(".meta").textContent =
    d.meta||"";
  const f=document.getElementById("filters");
  KINDS.forEach(k=>{const b=document.createElement("button");
    b.className="chip";b.textContent=k;b.onclick=()=>{
      active=(active===k)?null:k;
      [...f.children].forEach(c=>c.classList.toggle("on",c.textContent===active));
      run();};f.appendChild(b);});
  document.getElementById("q").addEventListener("input",run);
  run();
}).catch(e=>{document.getElementById("out").innerHTML=
  '<div class="empty">Failed to load search-index.json</div>';});
function run(){
  const q=document.getElementById("q").value.trim().toLowerCase();
  const terms=q?q.split(/\\s+/):[];
  let hits=IDX;
  if(active) hits=hits.filter(x=>x.kind===active);
  if(terms.length) hits=hits.filter(x=>x.hay.includes(terms[0]))
    .filter(x=>terms.every(t=>x.hay.includes(t)));
  hits=hits.slice(0,120);
  document.getElementById("stat").textContent =
    hits.length+" result(s)"+(hits.length>=120?" — refine your search":"");
  document.getElementById("out").innerHTML = hits.length? hits.map(card).join("")
    : '<div class="empty">No match</div>';
  if(hits.length) window.scrollTo(0,0);
}
function card(x){
  const mem=(x.members||[]).map(m=>
    '<tr><td class="k">'+esc(m.k)+'</td><td>'+esc(m.n)+
    (m.s?'<span class="badge">since '+esc(m.s)+'</span>':'')+
    (m.sig?'<pre>'+esc(m.sig)+'</pre>':'')+'</td></tr>').join("");
  return '<div class="card"><h3>'+esc(x.name)+
    (x.since?'<span class="badge">since '+esc(x.since)+'</span>':'')+
    '</h3><div class="ns">'+esc(x.ns)+' · '+esc(x.kind)+
    ' · '+((x.members||[]).length)+' members</div>'+
    (mem?'<table>'+mem+'</table>':'')+'</div>';
}
</script></body></html>
"""


def _md_escape(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def load_json(path: str) -> Optional[dict]:
    if not os.path.isfile(path):
        LOG.warning("missing %s", path)
        return None
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------
# Vault writers
# --------------------------------------------------------------------------


def write_text(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)


def build_class_notes(db: dict, vault: str, max_types: int = 0) -> List[dict]:
    """One markdown per API type, listing members with `since` versions."""
    version = db.get("version", "?")
    by_type: Dict[str, List[dict]] = defaultdict(list)
    ns_of: Dict[str, str] = {}
    for member in db.get("members", []):
        by_type[member.get("t", "")].append(member)
    for fqname, meta in db.get("types", {}).items():
        short = fqname.rsplit(".", 1)[-1]
        ns_of[short] = meta.get("ns", "")

    index: List[dict] = []
    names = sorted(by_type)
    if max_types:
        names = names[:max_types]

    for short in names:
        members = sorted(by_type[short], key=lambda m: (m.get("k", ""), m.get("n", "")))
        ns = ns_of.get(short, "")
        lines = [
            "---",
            f"type: {short}",
            f"namespace: {ns}",
            f"version: {version}",
            f"members: {len(members)}",
            "tags: [revit-api, class]",
            "---",
            "",
            f"# {short}",
            "",
            f"`{ns}.{short}` · Revit {version} · {len(members)} members",
            "",
            "| Kind | Member | Since | Signature |",
            "| --- | --- | --- | --- |",
        ]
        trimmed: List[dict] = []
        for member in members:
            lines.append(
                "| {k} | {n} | {s} | `{sig}` |".format(
                    k=_md_escape(member.get("k", "")),
                    n=_md_escape(member.get("n", "")),
                    s=member.get("s", "") or "—",
                    sig=_md_escape(member.get("sig", ""))[:220],
                )
            )
            trimmed.append(
                {
                    "k": member.get("k", ""),
                    "n": member.get("n", ""),
                    "s": member.get("s", ""),
                    "sig": member.get("sig", "")[:220],
                }
            )
        write_text(os.path.join(vault, "Class", f"{short}.md"), "\n".join(lines))

        hay = " ".join(
            [short.lower(), ns.lower()]
            + [m.get("n", "").lower() for m in members]
            + [m.get("sig", "").lower() for m in members]
        )
        index.append(
            {
                "name": short,
                "ns": ns,
                "kind": next(
                    (db["types"][f"{ns}.{short}"]["kind"] for ns2 in [ns]
                     if f"{ns2}.{short}" in db.get("types", {})),
                    "Class",
                ),
                "since": "",
                "members": trimmed,
                "hay": hay[:6000],
            }
        )
    LOG.info("wrote %d Class notes", len(index))
    return index


def build_version_notes(databases: Dict[str, dict], vault: str) -> None:
    for version, db in databases.items():
        counts = db.get("counts", {})
        since_hist = Counter(m.get("s", "") or "unknown" for m in db.get("members", []))
        top = ", ".join(
            f"{k}: {v}" for k, v in sorted(since_hist.items(), key=lambda kv: -kv[1])[:15]
        )
        write_text(
            os.path.join(vault, "Version", f"Revit {version}.md"),
            "\n".join(
                [
                    "---",
                    f"version: {version}",
                    "tags: [revit-api, version]",
                    "---",
                    "",
                    f"# Revit {version} API",
                    "",
                    f"- Types: **{counts.get('types', 0)}**",
                    f"- Members: **{counts.get('members', 0)}**",
                    f"- Pages parsed: {counts.get('pages', 0)}",
                    f"- Generated: {db.get('generated', '')}",
                    "",
                    "## Members by 'Since' version",
                    top,
                    "",
                    "## Links",
                    "- [[index]]",
                ]
            ),
        )


def build_pitfalls(notes_payload: dict, vault: str) -> None:
    by_term: Dict[str, List[dict]] = defaultdict(list)
    for note in notes_payload.get("notes", []):
        for term in note.get("pitfall_terms", []):
            by_term[term].append(note)
    for term, group in sorted(by_term.items(), key=lambda kv: -len(kv[1])):
        safe = re.sub(r'[<>:"/\\|?*]', "_", term)
        lines = [
            "---",
            f"term: {term}",
            f"posts: {len(group)}",
            "tags: [revit-api, pitfall, migration]",
            "---",
            "",
            f"# Pitfall — {term}",
            "",
        ]
        for note in group[:40]:
            lines.append(
                f"- [{_md_escape(note['title'])}]({note['url']}) — {note.get('date','')}"
            )
        write_text(os.path.join(vault, "Pitfall", f"{safe}.md"), "\n".join(lines))
    LOG.info("wrote %d Pitfall notes", len(by_term))


def build_notes(notes_payload: dict, vault: str) -> None:
    count = 0
    for note in notes_payload.get("notes", []):
        safe = re.sub(r'[<>:"/\\|?*]', "_", note.get("title", "note"))[:90]
        lines = [
            "---",
            f"num: {note.get('num')}",
            f"date: {note.get('date','')}",
            f"themes: [{', '.join(note.get('themes', []))}]",
            "tags: [revit-api, tbc]",
            "---",
            "",
            f"# {note.get('title','')}",
            "",
            f"<{note.get('url','')}>",
            "",
        ]
        for snippet in note.get("snippets", [])[:5]:
            lines += ["```csharp", snippet[:2400], "```", ""]
        write_text(
            os.path.join(vault, "Note", f"{note.get('num',0):04d}-{safe}.md"),
            "\n".join(lines),
        )
        count += 1
    LOG.info("wrote %d TBC notes", count)


def build_canvas(databases: Dict[str, dict], vault: str) -> None:
    nodes = []
    edges = []
    x = 0
    for version in sorted(databases):
        nodes.append(
            {
                "id": f"v{version}",
                "type": "text",
                "text": f"# Revit {version}",
                "x": x,
                "y": 0,
                "width": 260,
                "height": 90,
            }
        )
        x += 320
    for i, term in enumerate(["ElementId", "ForgeTypeId", "Toposolid", "Transaction"]):
        nodes.append(
            {
                "id": f"p{i}",
                "type": "text",
                "text": f"# Pitfall\\n{term}",
                "x": i * 220,
                "y": 240,
                "width": 200,
                "height": 90,
            }
        )
        for j, version in enumerate(sorted(databases)):
            edges.append(
                {"id": f"e{j}_{i}", "fromNode": f"v{version}", "toNode": f"p{i}"}
            )
    write_text(
        os.path.join(vault, "graph.canvas"),
        json.dumps({"nodes": nodes, "edges": edges}, indent=1),
    )


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--vault", default="vault")
    parser.add_argument("--site", default="site")
    parser.add_argument("--max-types", type=int, default=0)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    databases: Dict[str, dict] = {}
    for name in sorted(os.listdir(args.data_dir)) if os.path.isdir(args.data_dir) else []:
        if name.startswith("api_") and name.endswith(".json"):
            db = load_json(os.path.join(args.data_dir, name))
            if db:
                databases[str(db.get("version"))] = db
    if not databases:
        LOG.error("no api_*.json found in %s", args.data_dir)
        return 1

    notes_payload = load_json(os.path.join(args.data_dir, "tbc_notes.json")) or {
        "notes": []
    }

    os.makedirs(args.vault, exist_ok=True)
    newest = databases[max(databases, key=lambda v: str(v))]
    index = build_class_notes(newest, args.vault, max_types=args.max_types)
    build_version_notes(databases, args.vault)
    build_pitfalls(notes_payload, args.vault)
    build_notes(notes_payload, args.vault)
    build_canvas(databases, args.vault)

    write_text(
        os.path.join(args.vault, "index.md"),
        "\n".join(
            [
                "---",
                "tags: [revit-api, index]",
                "---",
                "",
                "# Revit API Knowledge Base",
                "",
                f"- Versions: {', '.join(sorted(databases))}",
                f"- Types indexed: {len(index)}",
                f"- TBC notes: {len(notes_payload.get('notes', []))}",
                "- Schema: `Class → has_member → Method/Property → added_in/changed_in → Version`",
                "",
                "## Versions",
            ]
            + [f"- [[Revit {v}]]" for v in sorted(databases)]
        ),
    )

    os.makedirs(args.site, exist_ok=True)
    meta = "Revit {versions} · {types} types · {members} members · {notes} TBC notes · built {date}".format(
        versions="/".join(sorted(databases)),
        types=newest.get("counts", {}).get("types", 0),
        members=newest.get("counts", {}).get("members", 0),
        notes=len(notes_payload.get("notes", [])),
        date=_dt.date.today().isoformat(),
    )
    with open(os.path.join(args.site, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(SITE_TEMPLATE.replace("__META__", html_mod.escape(meta)))
    with open(os.path.join(args.site, "search-index.json"), "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "items": index}, fh, ensure_ascii=False, separators=(",", ":"))
    LOG.info("site: %s (%.1f MB index)", args.site,
             os.path.getsize(os.path.join(args.site, "search-index.json")) / 1_048_576)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
