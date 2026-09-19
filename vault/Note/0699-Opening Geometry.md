---
num: 699
date: 2012-01-04
themes: [Geometry]
tags: [revit-api, tbc]
---

# Opening Geometry

<https://jeremytammik.github.io/tbc/a/0699_opening_geometry.htm>

```csharp
&nbsp; FamilySymbol symbol = null; &nbsp; &nbsp; foreach( FamilySymbol s in f.Symbols ) &nbsp; { &nbsp; &nbsp; symbol = s; &nbsp; &nbsp; break; &nbsp; }
```

```csharp
&nbsp; FamilySymbol symbol = f.Symbols &nbsp; &nbsp; .Cast&lt;FamilySymbol&gt;() &nbsp; &nbsp; .FirstOrDefault&lt;FamilySymbol&gt;();
```

```csharp
&nbsp; FamilySymbol symbol = f.Symbols &nbsp; &nbsp; .FirstOrDefault();
```
