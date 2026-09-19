---
num: 985
date: 2013-07-17
themes: [DynamoPython, Geometry, Pitfall, Units]
tags: [revit-api, tbc]
---

# Curve Length, Idling, Units and RevitPythonShell

<https://jeremytammik.github.io/tbc/a/0985_curve_idling_unit.htm>

```csharp
oFormatOption.DisplayUnits = eDisplayUnitType; using (Transaction t = new Transaction(doc)) { t.Start("Set options"); units.SetFormatOptions(unitType, oFormatOption); t.Commit(); }
```
