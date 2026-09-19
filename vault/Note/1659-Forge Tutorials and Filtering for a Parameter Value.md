---
num: 1659
date: 2018-06-01
themes: [Parameter]
tags: [revit-api, tbc]
---

# Forge Tutorials and Filtering for a Parameter Value

<https://jeremytammik.github.io/tbc/a/1659_param_filter.html>

```csharp
var collector = new FilteredElementCollector(doc) .Where(a => a.LookupParameter("house number") .AsString() == "12")
```

```csharp
List list = new FilteredElementCollector(doc) .OfClass(typeof(FamilyInstance)) .Where(a => a.LookupParameter("house number") .AsString() == "12") .Cast() .ToList();
```
