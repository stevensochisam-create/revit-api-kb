---
num: 1328
date: 2015-06-03
themes: [Geometry, MEP]
tags: [revit-api, tbc]
---

# Create Duct, Pipe and Point Transform

<https://jeremytammik.github.io/tbc/a/1328_transform_point.htm>

```csharp
&nbsp; Transform t = Transform.CreateRotationAtPoint( &nbsp; &nbsp; new XYZ( Origin.X, Origin.Y, Origin.Z + 1 ), &nbsp; &nbsp; Math.Pi, Origin ); &nbsp; &nbsp; t.whatMethodHereToGetNewXYZLocationOfPoint?
```

```csharp
&nbsp; XYZ axis = XYZ.BasisZ; &nbsp; double angle = Math.PI; &nbsp; Transform t = Transform.CreateRotationAtPoint( &nbsp; &nbsp; axis, angle, base_point ); &nbsp; XYZ pNew = t.OfPoint( pOld );
```
