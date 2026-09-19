---
num: 42
date: 2008-11-19
themes: [Parameter]
tags: [revit-api, tbc]
---

# Exploring Element Parameters

<https://jeremytammik.github.io/tbc/a/0042_exploring_param.htm>

```csharp
C:\tmp\ > diff RevitElementsBeforeFilter.txt RevitElementsAfterFilter.txt 2159a2160 > Id=127147; Class=Symbol; Category=?; Name=Filter 1
```

```csharp
Symbol 'Filter 1' 127147 Instance Built-in Parameters ELEM_CATEGORY_PARAM_MT Category ElementId read-only -1 ELEM_CATEGORY_PARAM Category ElementId read-only -1 DESIGN_OPTION_ID Design Option ElementId read-only -1 PHASE_DEMOLISHED Phase Demolished ElementId read-write -1 PHASE_CREATED Phase Created ElementId read-write -1 ELEMENT_LOCKED_PARAM Locked Integer read-write 0 ELEM_DELETABLE_IN_FAMILY Deletable Integer read-write 1 UNIFORMAT_DESCRIPTION Assembly Description String read-only UNIFORMAT_CODE Assembly Code String read-write ID_PARAM Id ElementId read-only Symbol 'Filter 1' 127147 EDITED_BY Edited by String read-only ELEM_PARTITION_PARAM Workset Integer read-write 0 ELEM_FAMILY_AND_TYPE_PARAM Family and Type ElementId read-only -1 ELEM_FAMILY_PARAM Family ElementId read-only -1 ELEM_TYPE_PARAM Type ElementId read-only -1 SYMBOL_FAMILY_AND_TYPE_NAMES_PARAM Family and Type String read-only Filters: Filter 1 SYMBOL_FAMILY_NAME_PARAM Family Name String read-only Filters SYMBOL_FAMILY_NAME_PARAM Family Name String read-only Filters SYMBOL_NAME_PARAM Type Name String read-only Filter 1 SYMBOL_NAME_PARAM Type Name String read-only Filter 1 SYMBOL_ID_PARAM Type Id ElementId read-only -1
```
