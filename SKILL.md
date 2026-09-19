---
name: revit-api-kb
description: >
  Revit API signature and version-compatibility knowledge base for writing
  Dynamo CPython3 / pyRevit code. Use when you need an exact Revit API member
  signature, whether a member exists in a given Revit version, what changed
  between Revit 2023/2024/2025, or real-world migration pitfalls (ElementId
  64-bit, ForgeTypeId, UnitTypeId, Toposolid, .NET 8). Triggers on "Revit API",
  "Dynamo Python", "which Revit version has", "API signature", "ElementId
  64-bit", "ForgeTypeId", "Toposolid", "UnitTypeId", "obsolete API".
agent_created: true
---

# Revit API Knowledge Base

Ground truth for Revit API code. **Verify before writing** — never emit a
member signature from memory if this KB can confirm it.

## Where the data lives

The corpus (1 GB CHM + 2 GB TBC archive) is **never downloaded locally**.
Extraction runs in GitHub Actions and publishes:

| Artefact | Location |
| --- | --- |
| Site (search UI) | `https://<owner>.github.io/revit-api-kb/` |
| `api_<version>.json` | repo `data/` + Pages root |
| `diff_<a>_<b>.json` | repo `data/` + Pages root |
| `tbc_notes.json` | repo `data/` |
| Obsidian vault | repo `vault/` (`Class/`, `Version/`, `Pitfall/`, `Note/`, `graph.canvas`) |

Set `REVIT_API_KB_BASE` (or pass `--base`) to the Pages URL once it exists.

## Query (do this first)

```bash
cd <skill>/scripts

python query.py member CopyModel                # exact signature + since
python query.py member "GetAnalytical" --kind Method
python query.py member "Wall" --since 2021      # only members added >= 2021
python query.py type Wall                       # all members of a type
python query.py diff 2023 2024 --only added     # version delta
python query.py stats 2023 2024                 # coverage sanity check
```

`--source auto` (default) uses the local `data/` cache when present, else the
remote site. Force with `--source remote --base https://<owner>.github.io/revit-api-kb`.

## Schema

```
Class  --has_member-->  Method/Property  --added_in/changed_in-->  Revit version
Note    (TBC real-world snippet)      Pitfall (migration trap)
```

Each member record: `t` type, `n` name, `k` kind, `sig` C# signature,
`s` since-version, `p` parameters, `d` summary, `o` obsolete flag.

## Rules when generating code

1. **Confirm the member exists in the target Revit version** — `query.py member <name>`,
   then check `since`. If `since` > target version, say so and offer an alternative.
2. **Prefer stable identifiers**: `BuiltInParameter`, `BuiltInCategory`, `ElementId`.
   Never match on element names.
3. **CPython3 (Dynamo 3.x) is the default.** f-strings OK, `UnitTypeId` /
   `SpecTypeId` instead of the removed `DisplayUnitType`. IronPython 2.7 notes
   only when the user explicitly asks for Dynamo 2.x.
4. **Always** wrap model changes in a transaction, convert internal units
   (feet ↔ mm), and guard `None` — see `references/generate-dynamo/`.
5. **Flag obsolete APIs** (`"o": true` in the DB) instead of emitting them silently.

## Sub-skills

- `references/generate-dynamo/` — Dynamo Python script generation, output format, quality checklist
- `references/revit-api-code/` — C# add-ins, macros, pyRevit scripts

## Rebuilding

`scripts/build_signature_db.py`, `build_tbc_notes.py`, `build_vault.py` are
driven by `.github/workflows/build.yml` (monthly + manual dispatch). Running
them locally with `--fetch` will download ~700 MB transiently; use the workflow
unless you really need a local run.

## Sources

- `ADN-DevTech/revit-api-chms` (MIT) — Revit SDK API docs, decompiled HTML
- `jeremytammik/tbc` (MIT) — The Building Coder archive, 2081 posts
