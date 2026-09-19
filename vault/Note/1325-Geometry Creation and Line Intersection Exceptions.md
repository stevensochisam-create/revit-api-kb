---
num: 1325
date: 2015-05-28
themes: [Geometry]
tags: [revit-api, tbc]
---

# Geometry Creation and Line Intersection Exceptions

<https://jeremytammik.github.io/tbc/a/1325_solid_line_intersect.htm>

```csharp
&nbsp; List&lt;XYZ&gt; ctrPoints = new List&lt;XYZ&gt;(); &nbsp; &nbsp; ctrPoints.Add( new XYZ( Utils.mmToFeet( 72500.017337 ), &nbsp; &nbsp; Utils.mmToFeet( -5072.522765 ), Utils.mmToFeet( 0 ) ) ); &nbsp; ctrPoints.Add( new XYZ( Utils.mmToFeet( 105082.371745 ), &nbsp; &nbsp; Utils.mmToFeet( -748.798009 ), tils.mmToFeet( 0 ) ) ); &nbsp; ctrPoints.Add( new XYZ( Utils.mmToFeet( 117899.12727 ), &nbsp; &nbsp; Utils.mmToFeet( -15572.997171 ), Utils.mmToFeet( 0 ) ) ); &nbsp; &nbsp; List&lt;double&gt; weights = new List&lt;double&gt;(); &nbsp; weights.Add( 1 ); &nbsp; weights.Add( 1 ); &nbsp; weights.Add( 1 ); &nbsp; &nbsp; List&lt;double&gt; knots = new List&lt;double&gt;(); &nbsp; knots.Add( 0 ); &nbsp; knots.Add( 0 ); &nbsp; knots.Add( 0 ); &nbsp; knots.Add( 52464.568605 ); &nbsp; knots.Add( 52464.568605 ); &nbsp; knots.Add( 52464.568605 ); &nbsp; &nbsp; NurbSpline detailNurbSpline = NurbSpline.Create( &nbsp; &nbsp; ctrPoints, weights, knots, 3, false, true );
```

```csharp
// Use degree 1 for two CPs, degree 2 for three CPs, // and degree 3 for four or more CPs.
```

```csharp
&nbsp; Solid GetFirstSolidClone( Element e ) &nbsp; { &nbsp; &nbsp; Solid clone = null; &nbsp; &nbsp; Options opt = new Options(); &nbsp; &nbsp; GeometryElement geo = e.get_Geometry( opt ); &nbsp; &nbsp; foreach( GeometryObject obj in geo ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Solid solid = obj as Solid; &nbsp; &nbsp; &nbsp; &nbsp; if( solid != null &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; 0 &lt; solid.Faces.Size ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; return clone = SolidUtils.Clone( solid ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return clone; &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Return the 2D intersection point between two &nbsp; /// unbounded lines defined in the XY plane by the &nbsp; /// start and end points of the two given curves. &nbsp; /// By Magson Leone. &nbsp; /// Return null if the two lines are coincident, &nbsp; /// in which case the intersection is an infinite &nbsp; /// line, or non-coincident and parallel, in which &nbsp; /// case it is empty. &nbsp; /// https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection &nbsp; /// &lt;/summary&gt; &nbsp; public static XYZ Intersection( Curve c1, Curve c2 ) &nbsp; { &nbsp; &nbsp; XYZ p1 = c1.GetEndPoint( 0 ); &nbsp; &nbsp; XYZ q1 = c1.GetEndPoint( 1 ); &nbsp; &nbsp; XYZ p2 = c2.GetEndPoint( 0 ); &nbsp; &nbsp; XYZ q2 = c2.GetEndPoint( 1 ); &nbsp; &nbsp; XYZ v1 = q1 - p1; &nbsp; &nbsp; XYZ v2 = q2 - p2; &nbsp; &nbsp; XYZ w = p2 - p1; &nbsp; &nbsp; &nbsp; XYZ p5 = null; &nbsp; &nbsp; &nbsp; double c = ( v2.X * w.Y - v2.Y * w.X ) &nbsp; &nbsp; &nbsp; / ( v2.X * v1.Y - v2.Y * v1.X ); &nbsp; &nbsp; &nbsp; if( !double.IsInfinity( c ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; double x = p1.X + c * v1.X; &nbsp; &nbsp; &nbsp; double y = p1.Y + c * v1.Y; &nbsp; &nbsp; &nbsp; &nbsp; p5 = new XYZ( x, y, 0 ); &nbsp; &nbsp; } &nbsp; &nbsp; return p5; &nbsp; }
```
