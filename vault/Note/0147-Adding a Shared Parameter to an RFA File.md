---
num: 147
date: 2009-06-08
themes: [Parameter]
tags: [revit-api, tbc]
---

# Adding a Shared Parameter to an RFA File

<https://jeremytammik.github.io/tbc/a/0147_shared_param_rfa.htm>

```csharp
C:\tmp\ > diff RevitElementsBeforeLoadingFamily.txt RevitElementsAfterLoadingFamily.txt 2160a2161,2172 > Id=127149; Class=Family; Category=Doors; Name=M_Double-Flush > Id=127705; Class=Element; Category=?; Name=M_Double-Flush > Id=127706; Class=FamilySymbol; Category=Doors; Name=1830 x 1981mm > Id=127707; Class=Element; Category=?; Name=1830 x 1981mm > Id=127708; Class=FamilySymbol; Category=Doors; Name=1830 x 2083mm > Id=127709; Class=Element; Category=?; Name=1830 x 2083mm > Id=127710; Class=FamilySymbol; Category=Doors; Name=1730 x 2134mm > Id=127711; Class=Element; Category=?; Name=1730 x 2134mm > Id=127712; Class=FamilySymbol; Category=Doors; Name=1730 x 2032mm > Id=127713; Class=Element; Category=?; Name=1730 x 2032mm > Id=127714; Class=FamilySymbol; Category=Doors; Name=1830 x 2134mm > Id=127715; Class=Element; Category=?; Name=1830 x 2134mm
```
