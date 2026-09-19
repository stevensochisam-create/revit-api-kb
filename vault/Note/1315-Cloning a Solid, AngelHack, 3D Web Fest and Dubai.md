---
num: 1315
date: 2015-05-07
themes: [Geometry]
tags: [revit-api, tbc]
---

# Cloning a Solid, AngelHack, 3D Web Fest and Dubai

<https://jeremytammik.github.io/tbc/a/1315_2016_au_dubai_ah8.htm>

```csharp
&nbsp; static public Solid Clone( this Solid solid ) &nbsp; { &nbsp; &nbsp; if( solid == null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return null; &nbsp; &nbsp; } &nbsp; &nbsp; return BooleanOperationsUtils &nbsp; &nbsp; &nbsp; .ExecuteBooleanOperation( solid, solid, &nbsp; &nbsp; &nbsp; &nbsp; BooleanOperationsType.Union ); &nbsp; }
```
