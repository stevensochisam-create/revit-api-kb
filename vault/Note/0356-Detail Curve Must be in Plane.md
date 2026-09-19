---
num: 356
date: 2010-05-03
themes: [Geometry]
tags: [revit-api, tbc]
---

# Detail Curve Must be in Plane

<https://jeremytammik.github.io/tbc/a/0356_detail_curve_plane.htm>

```csharp
&nbsp; DetailCurve detailCurve &nbsp; &nbsp; = doc.Create.NewDetailCurve( &nbsp; &nbsp; &nbsp; doc.ActiveView, curve );
```

```csharp
XYZ GetCurveNormal( Curve curve ) { &nbsp; IList&lt;XYZ&gt; pts = curve.Tessellate(); &nbsp; int n = pts.Count; &nbsp; &nbsp; Debug.Assert( 1 &lt; n, &nbsp; &nbsp; &quot;expected at least two points &quot; &nbsp; &nbsp; + &quot;from curve tessellation&quot; ); &nbsp; &nbsp; XYZ p = pts[0]; &nbsp; XYZ q = pts[n - 1]; &nbsp; XYZ v = q - p; &nbsp; XYZ w, normal = null; &nbsp; &nbsp; if( 2 == n ) &nbsp; { &nbsp; &nbsp; Debug.Assert( curve is Line, &nbsp; &nbsp; &nbsp; &quot;expected non-line element to have &quot; &nbsp; &nbsp; &nbsp; + &quot;more than two tessellation points&quot; ); &nbsp; &nbsp; &nbsp; // for non-vertical lines, use Z axis to &nbsp; &nbsp; // span the plane, otherwise Y axis: &nbsp; &nbsp; &nbsp; double dxy = Math.Abs( v.X ) + Math.Abs( v.Y ); &nbsp; &nbsp; &nbsp; w = ( dxy &gt; Util.TolPointOnPlane ) &nbsp; &nbsp; &nbsp; ? XYZ.BasisZ &nbsp; &nbsp; &nbsp; : XYZ.BasisY; &nbsp; &nbsp; &nbsp; normal = v.CrossProduct( w ).Normalize(); &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; int i = 0; &nbsp; &nbsp; while( ++i &lt; n - 1 ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; w = pts[i] - p; &nbsp; &nbsp; &nbsp; normal = v.CrossProduct( w ); &nbsp; &nbsp; &nbsp; if( !normal.IsZeroLength() ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; normal = normal.Normalize(); &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; #if DEBUG &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; XYZ normal2; &nbsp; &nbsp; &nbsp; while( ++i &lt; n - 1 ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; w = pts[i] - p; &nbsp; &nbsp; &nbsp; &nbsp; normal2 = v.CrossProduct( w ); &nbsp; &nbsp; &nbsp; &nbsp; Debug.Assert( normal2.IsZeroLength() &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; || Util.IsZero( normal2.AngleTo( normal ) ), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;expected all points of curve to &quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + &quot;lie in same plane&quot; ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } #endif // DEBUG &nbsp; &nbsp; } &nbsp; return normal; }
```
