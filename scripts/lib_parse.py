# -*- coding: utf-8 -*-
"""lib_parse.py — Revit API CHM decompiled HTML parser.

Parses the ADN-DevTech/revit-api-chms `html/<version>/` tree:
  - RevitAPI.hhc  : table of contents (Namespace -> Type -> Member)
  - html/<guid>.htm : individual member / type pages

Verified against Revit 2024 structure (2026-09-18):
  TOC  : <UL> nesting -> depth 1 Namespaces | 2 Namespace | 3 Type
         | 4 "<Type> Methods/Properties/..." | 5 Member | 6 Overload
  Page : <div class="summary">  <b>Namespace:</b>  <b>Assembly:</b>
         <b>Since:</b>          <span codeLanguage="CSharp"><pre ...>

Public API:
    parse_hhc(path)          -> list[TocEntry]
    parse_page(html_text)    -> dict
    iter_toc_types(entries)  -> iterator of (namespace, type_name, kind)
"""

from __future__ import annotations

import html as html_mod
import re
import unicodedata
from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Tuple

__all__ = [
    "TocEntry",
    "parse_hhc",
    "parse_page",
    "iter_toc_types",
    "iter_toc_members",
    "normalise_since",
    "safe_filename",
    "strip_tags",
    "collapse_ws",
]

# --------------------------------------------------------------------------
# Text helpers
# --------------------------------------------------------------------------

_WS_RE = re.compile(r"\s+")
_SCRIPT_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)
_TAG_RE = re.compile(r"<[^>]+>")

# TOC type-name suffixes used by Sandcastle CHM output
_KIND_SUFFIXES = (
    "Class",
    "Enumeration",
    "Interface",
    "Structure",
    "Delegate",
    "Constructor",
    "Method",
    "Property",
    "Event",
    "Field",
    "Methods",
    "Properties",
    "Events",
    "Fields",
    "Constructors",
    "Members",
)


def strip_tags(fragment: str) -> str:
    """Remove tags, unescape entities, collapse whitespace."""
    if not fragment:
        return ""
    no_script = _SCRIPT_RE.sub(" ", fragment)
    text = _TAG_RE.sub(" ", no_script)
    text = html_mod.unescape(text)
    # Sandcastle inserts " . . :: . ." separators inside dotted names
    text = text.replace(". . :: . .", ".")
    return collapse_ws(text)


def collapse_ws(text: str) -> str:
    return _WS_RE.sub(" ", text).strip()


def _clean_dotted(text: str) -> str:
    """Sandcastle renders 'Autodesk.Revit.DB..::..ModelPath' -> clean dotted."""
    t = text.replace(". . :: . .", ".")
    t = re.sub(r"\s+", "", t)
    return t


# --------------------------------------------------------------------------
# TOC
# --------------------------------------------------------------------------


@dataclass
class TocEntry:
    depth: int
    name: str
    local: str  # e.g. "html/72fdfc1b-....htm"
    index: int = 0

    @property
    def kind(self) -> str:
        """Return the Sandcastle kind suffix (Class / Method / ...), else ''."""
        for suf in _KIND_SUFFIXES:
            if self.name.endswith(" " + suf):
                return suf
        if self.name.endswith(" Namespace"):
            return "Namespace"
        return ""

    @property
    def bare_name(self) -> str:
        name = self.name
        if name.endswith(" Namespace"):
            return name[: -len(" Namespace")]
        for suf in _KIND_SUFFIXES:
            if name.endswith(" " + suf):
                return name[: -(len(suf) + 1)]
        return name


_TOK_RE = re.compile(r"<UL>|</UL>|<OBJECT[^>]*>.*?</OBJECT>", re.S | re.I)
_PARAM_RE = re.compile(
    r'<param\s+name="Name"\s+value="([^"]*)"\s*>\s*'
    r'<param\s+name="Local"\s+value="([^"]*)"',
    re.S | re.I,
)


def parse_hhc(path: str) -> List[TocEntry]:
    """Parse a RevitAPI.hhc file into a flat depth-annotated list."""
    with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
        raw = fh.read()

    entries: List[TocEntry] = []
    depth = 0
    for match in _TOK_RE.finditer(raw):
        token = match.group(0)
        head = token[:5].upper()
        if head.startswith("<UL>"):
            depth += 1
            continue
        if head.startswith("</UL>"):
            depth = max(0, depth - 1)
            continue
        param = _PARAM_RE.search(token)
        if not param:
            continue
        name = collapse_ws(html_mod.unescape(param.group(1)))
        local = param.group(2).strip()
        if not name:
            continue
        entries.append(TocEntry(depth=depth, name=name, local=local, index=len(entries)))
    return entries


def iter_toc_types(entries: List[TocEntry]) -> Iterator[Tuple[str, str, str, str]]:
    """Yield (namespace, type_name, kind, type_local) for every type in the TOC.

    Handles TOC layouts where the namespace sits at depth 2, types at depth 3,
    and also the flatter depth-1/2 layouts seen in some SDK versions.
    """
    ns_by_depth: dict = {}
    for entry in entries:
        if entry.name.endswith(" Namespace"):
            ns_by_depth[entry.depth] = entry.bare_name
            continue
        kind = entry.kind
        if kind in ("Class", "Enumeration", "Interface", "Structure", "Delegate"):
            # namespace is the nearest recorded namespace with smaller depth
            ns = ""
            for depth in sorted(ns_by_depth, reverse=True):
                if depth < entry.depth:
                    ns = ns_by_depth[depth]
                    break
            yield ns, entry.bare_name, kind, entry.local


def iter_toc_members(entries: List[TocEntry]) -> Iterator[Tuple[str, str, str, str]]:
    """Yield (owner_type, member_name, member_kind, member_local).

    Members are the TOC leaves (depth >= 5 in Revit 2024). Overload entries
    (depth 6) are folded into their parent member name.
    """
    current_type = ""
    for entry in entries:
        kind = entry.kind
        if kind in ("Class", "Enumeration", "Interface", "Structure", "Delegate"):
            current_type = entry.bare_name
            continue
        if kind in (
            "Constructor",
            "Method",
            "Property",
            "Event",
            "Field",
        ):
            yield current_type, entry.bare_name, kind, entry.local


# --------------------------------------------------------------------------
# Member / type pages
# --------------------------------------------------------------------------

_SUMMARY_RE = re.compile(r'<div\s+class="summary"\s*>(.*?)</div>', re.S | re.I)
_NS_RE = re.compile(r"<b>\s*Namespace:\s*</b>\s*<a[^>]*>(.*?)</a>", re.S | re.I)
_ASM_RE = re.compile(
    r"<b>\s*Assembly:\s*</b>.*?Version:\s*([0-9][0-9.]*)", re.S | re.I
)
_SINCE_RE = re.compile(r"<b>\s*Since:\s*</b>\s*([^<]*)", re.S | re.I)
_CS_RE = re.compile(
    r'<span\s+codeLanguage="CSharp".*?<pre[^>]*>(.*?)</pre>', re.S | re.I
)
_PARAM_SEC_RE = re.compile(
    r'<div[^>]*id="[^"]*parameterSection[^"]*"[^>]*>(.*?)<h1', re.S | re.I
)
_PARAM_ROW_RE = re.compile(
    r'<span\s+class="parameter"\s*>(.*?)</span>', re.S | re.I
)
_H1_RE = re.compile(r'<h1\s+class="heading"\s*>(.*?)</h1>', re.S | re.I)
_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
_RETURNS_RE = re.compile(
    r"<b>\s*(?:Return Value|Property Value)\s*</b>\s*(.*?)(?:</div>|<h1)",
    re.S | re.I,
)
_OBSOLETE_RE = re.compile(r"[Oo]bsolete", re.I)


def parse_page(html_text: str) -> dict:
    """Extract structured data from one decompiled CHM page.

    Returns a dict with keys: title, summary, namespace, api_version,
    since, signature_cs, parameters, returns, obsolete. Missing fields
    fall back to "" / [] — callers must treat all values as optional.
    """
    result = {
        "title": "",
        "summary": "",
        "namespace": "",
        "api_version": "",
        "since": "",
        "signature_cs": "",
        "parameters": [],
        "returns": "",
        "obsolete": False,
    }
    if not html_text:
        return result

    # Sandcastle puts the real name in <title>; the first <h1 class="heading">
    # is usually the "Syntax" section header, so <title> takes priority.
    match = _TITLE_RE.search(html_text)
    if match:
        candidate = collapse_ws(strip_tags(match.group(1)))
        if candidate and candidate.lower() != "syntax":
            result["title"] = candidate
    if not result["title"]:
        match = _H1_RE.search(html_text)
        if match:
            candidate = collapse_ws(strip_tags(match.group(1)))
            if candidate and candidate.lower() != "syntax":
                result["title"] = candidate

    match = _SUMMARY_RE.search(html_text)
    if match:
        result["summary"] = collapse_ws(strip_tags(match.group(1)))

    match = _NS_RE.search(html_text)
    if match:
        result["namespace"] = _clean_dotted(strip_tags(match.group(1)))

    match = _ASM_RE.search(html_text)
    if match:
        result["api_version"] = collapse_ws(strip_tags(match.group(1)))

    match = _SINCE_RE.search(html_text)
    if match:
        result["since"] = collapse_ws(strip_tags(match.group(1)))

    match = _CS_RE.search(html_text)
    if match:
        signature = strip_tags(match.group(1))
        # Sandcastle hard-wraps signatures; normalise newlines but keep the
        # parameter list readable as a single line.
        signature = collapse_ws(signature).replace("\t", " ")
        result["signature_cs"] = signature
        result["parameters"] = [
            collapse_ws(strip_tags(p)) for p in _PARAM_ROW_RE.findall(match.group(1))
        ]

    match = _RETURNS_RE.search(html_text)
    if match:
        result["returns"] = collapse_ws(strip_tags(match.group(1)))[:400]

    if _OBSOLETE_RE.search(html_text[:20000]):
        result["obsolete"] = True

    return result


def normalise_since(since: str) -> str:
    """'Since' values look like '2012', '2012.1', '2024' — return canonical str."""
    if not since:
        return ""
    since = collapse_ws(since)
    match = re.match(r"^(\d{4})(?:\.(\d+))?$", since)
    if not match:
        return since
    year = match.group(1)
    point = match.group(2)
    return f"{year}.{point}" if point else year


def safe_filename(name: str) -> str:
    """Filesystem-safe name for vault markdown files."""
    name = unicodedata.normalize("NFKC", name)
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    return collapse_ws(name) or "unnamed"
