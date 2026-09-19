---
num: 57
date: 2008-12-15
themes: [Geometry]
tags: [revit-api, tbc]
---

# Polygon Transformation

<https://jeremytammik.github.io/tbc/a/0057_polygon_transformation.htm>

```csharp
#if DEBUG &nbsp; Transform t = GetTransformToZ( normal ); &nbsp; &nbsp; List&lt;XYZ&gt; polygonHorizontal &nbsp; &nbsp; = ApplyTransform( polygon, t ); &nbsp; &nbsp; List&lt;UV&gt; polygon2d &nbsp; &nbsp; = CmdSlabBoundaryArea.Flatten( &nbsp; &nbsp; &nbsp; polygonHorizontal ); &nbsp; &nbsp; double a2 &nbsp; &nbsp; = CmdSlabBoundaryArea.GetSignedPolygonArea( &nbsp; &nbsp; &nbsp; polygon2d ); &nbsp; &nbsp; Debug.Assert( Util.IsEqual( a, a2 ), &nbsp; &nbsp; "expected same area from 2D and 3D calculations" ); #endif
```

```csharp
Transform GetTransformToZ( XYZ v ) { &nbsp; Transform t; &nbsp; &nbsp; double a = XYZ.BasisZ.Angle( v ); &nbsp; &nbsp; if( Util.IsZero( a ) ) &nbsp; { &nbsp; &nbsp; t = Transform.Identity; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; XYZ axis = Util.IsEqual( a, Math.PI ) &nbsp; &nbsp; &nbsp; ? XYZ.BasisX &nbsp; &nbsp; &nbsp; : v.Cross( XYZ.BasisZ ); &nbsp; &nbsp; &nbsp; t = Transform.get_Rotation( XYZ.Zero, axis, a ); &nbsp; } &nbsp; return t; }
```
