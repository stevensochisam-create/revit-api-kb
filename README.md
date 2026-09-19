# revit-api-kb

Revit API signature + version-compatibility knowledge base, built for writing
Dynamo **CPython 3** / pyRevit code. Zero local corpus: everything is extracted
in GitHub Actions and published to GitHub Pages.

## Layout

```
SKILL.md                  query routing + code-generation rules
scripts/
  lib_parse.py            CHM hhc + member-page parser
  build_signature_db.py   sparse-clone → extract → api_<ver>.json + diff
  build_tbc_notes.py      The Building Coder → tbc_notes.json
  build_vault.py          → vault/ (Obsidian) + site/ (static search UI)
  query.py                local/remote CLI lookup
.github/workflows/build.yml   monthly + manual cloud build
data/                     committed build output (gitignored except JSON)
vault/                    Obsidian vault: Class/ Version/ Pitfall/ Note/ graph.canvas
site/                     static site (published to Pages)
references/               generate-dynamo + revit-api-code (upstream: Utopia5327, MIT)
```

## Data model

```
Class --has_member--> Method/Property --added_in/changed_in--> Revit version
Note (TBC snippet)      Pitfall (migration trap)
```

Member record keys: `t` type · `n` name · `k` kind · `sig` C# signature ·
`s` since-version · `p` parameters · `d` summary · `o` obsolete.

## Sources

- `ADN-DevTech/revit-api-chms` (MIT) — Revit SDK API docs, decompiled HTML
- `jeremytammik/tbc` (MIT) — The Building Coder, 2081 posts (2008–2026)
- `Utopia5327/claude-plugin-for-revit-bim` (MIT) — 2 reference skills,
  re-pointed from IronPython 2.7 to CPython 3

## Setup

1. Push this directory as a **public** GitHub repo (Pages free tier requires it).
2. Settings → Pages → Source: **GitHub Actions**.
3. Actions → `build` → **Run workflow**.
4. Set `REVIT_API_KB_BASE=https://<owner>.github.io/revit-api-kb` in your shell
   so `query.py` resolves the remote data.

## Known limitations

- CHM tree has no `html/2026` — 2026 API coverage must come from the
  `Revit_Platform_API_Changes_and_Additions_2026.pdf` in `tbc/a/doc/`.
- TBC's own topic taxonomy (`toc-data.json`, 58 topics) is legacy 2013-era and
  contains no modern themes; filtering is title-keyword + body-grep instead.
- Title-keyword filtering misses posts that only mention a term in the body —
  Pagefind full-text search on the live site is the long-term fix.
