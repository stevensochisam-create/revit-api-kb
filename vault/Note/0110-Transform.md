---
num: 110
date: 2009-03-17
themes: [Geometry]
tags: [revit-api, tbc]
---

# Transform

<https://jeremytammik.github.io/tbc/a/0110_transform.htm>

```csharp
XYZ ptOrigin = XYZ.Zero; XYZ ptXAxis = XYZ.BasisX; XYZ ptYAxis = XYZ.BasisY; &nbsp; trans1 = Transform.get_Rotation( // rotation &nbsp; ptOrigin, ptXAxis, 90 ); &nbsp; trans2 = Transform.get_Translation( // translation &nbsp; ptXAxis ); &nbsp; trans1 = trans2.ScaleBasis( 2.0 ); // scaling &nbsp; Plane plane1 = creApp.NewPlane( &nbsp; ptXAxis, ptYAxis ); &nbsp; trans3 = Transform.get_Reflection( // mirror &nbsp; plane1 );
```

```csharp
Transform GetTransformToZ( XYZ v ) { &nbsp; Transform t; &nbsp; &nbsp; double a = XYZ.BasisZ.Angle( v ); &nbsp; &nbsp; if( Util.IsZero( a ) ) &nbsp; { &nbsp; &nbsp; t = Transform.Identity; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; XYZ axis = Util.IsEqual( a, Math.PI ) &nbsp; &nbsp; &nbsp; ? XYZ.BasisX &nbsp; &nbsp; &nbsp; : v.Cross( XYZ.BasisZ ); &nbsp; &nbsp; &nbsp; t = Transform.get_Rotation( XYZ.Zero, &nbsp; &nbsp; &nbsp; axis, a ); &nbsp; } &nbsp; return t; } &nbsp; List&lt;XYZ&gt; ApplyTransform( &nbsp; List&lt;XYZ&gt; polygon, &nbsp; Transform t ) { &nbsp; int n = polygon.Count; &nbsp; &nbsp; List&lt;XYZ&gt; polygonTransformed &nbsp; &nbsp; = new List&lt;XYZ&gt;( n ); &nbsp; &nbsp; foreach( XYZ p in polygon ) &nbsp; { &nbsp; &nbsp; polygonTransformed.Add( t.OfPoint( p ) ); &nbsp; } &nbsp; return polygonTransformed; }
```
