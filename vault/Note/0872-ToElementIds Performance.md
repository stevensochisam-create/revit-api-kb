---
num: 872
date: 2012-12-13
themes: [ElementId]
tags: [revit-api, tbc]
---

# ToElementIds Performance

<https://jeremytammik.github.io/tbc/a/0872_toelementids_perf.htm>

```csharp
"> &nbsp; var fc = new FilteredElementCollector( doc ) &nbsp; &nbsp; .OfSomething() &nbsp; &nbsp; .ToElementIds(); &nbsp; &nbsp; foreach( var elemId in fc ) &nbsp; { &nbsp; &nbsp; var element = doc.GetElement( elemId ); &nbsp; }
```

```csharp
"> &nbsp; var fc = new FilteredElementCollector( doc ) &nbsp; &nbsp; .OfSomething(); &nbsp; &nbsp; foreach (var elem in fc) &nbsp; { &nbsp; &nbsp; &nbsp; var element = elem; &nbsp; }
```
