---
num: 1563
date: 2017-06-01
themes: [Transaction]
tags: [revit-api, tbc]
---

# AI News and Sub-Transaction Regen

<https://jeremytammik.github.io/tbc/a/1563_subtrans_regen.html>

```csharp
start main transaction { ... start sub transaction { ... if (!familySymbol.IsActive) familySymbol.Activate() ... subtransaction.Commit() } document.Regenerate() ... geometry = familySymbol.get_Geometry(options) ... }
```
