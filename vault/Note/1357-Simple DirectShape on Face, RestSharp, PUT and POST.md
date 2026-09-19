---
num: 1357
date: 2015-09-11
themes: [Geometry]
tags: [revit-api, tbc]
---

# Simple DirectShape on Face, RestSharp, PUT and POST

<https://jeremytammik.github.io/tbc/a/1357_directshape_simple.html>

```csharp
&nbsp; var familyInstance = el as FamilyInstance; &nbsp; &nbsp; var transform = familyInstance != null &nbsp; &nbsp; ? familyInstance.GetTotalTransform() &nbsp; &nbsp; : Transform.Identity;
```

```csharp
&nbsp; p1 = transform.OfPoint( p1 ); &nbsp; p2 = transform.OfPoint( p2 ); &nbsp; p3 = transform.OfPoint( p3 );
```
