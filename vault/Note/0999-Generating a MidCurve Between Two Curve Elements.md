---
num: 999
date: 2013-08-15
themes: [Geometry]
tags: [revit-api, tbc]
---

# Generating a MidCurve Between Two Curve Elements

<https://jeremytammik.github.io/tbc/a/0999_midcurve.htm>

```csharp
&nbsp; // Extract data from the two selected curves. &nbsp; Curve c0 = curves[0].GeometryCurve; &nbsp; Curve c1 = curves[1].GeometryCurve; &nbsp; double sp0 = c0.GetEndParameter( 0 ); &nbsp; double ep0 = c0.GetEndParameter( 1 ); &nbsp; double step0 = ( ep0 - sp0 ) / _nSegments; &nbsp; double sp1 = c1.GetEndParameter( 0 ); &nbsp; double ep1 = c1.GetEndParameter( 1 ); &nbsp; double step1 = ( ep1 - sp1 ) / _nSegments; &nbsp; Debug.Print( &quot;Two curves' step size [start, end]:&quot; &nbsp; &nbsp; + &quot; {0} [{1},{2}] -- {3} [{4},{5}]&quot;, &nbsp; &nbsp; Util.RealString( step0 ), &nbsp; &nbsp; Util.RealString( sp0 ), &nbsp; &nbsp; Util.RealString( ep0 ), &nbsp; &nbsp; Util.RealString( step1 ), &nbsp; &nbsp; Util.RealString( sp1 ), &nbsp; &nbsp; Util.RealString( ep1 ) );
```

```csharp
&nbsp; // Modify document within a transaction. &nbsp; using( Transaction tx = new Transaction( doc ) ) &nbsp; { &nbsp; &nbsp; Creator creator = new Creator( doc ); &nbsp; &nbsp; tx.Start( &quot;MidCurve&quot; ); &nbsp; &nbsp; // Current segment start points. &nbsp; &nbsp; double t0 = sp0; &nbsp; &nbsp; double t1 = sp1; &nbsp; &nbsp; XYZ p0 = c0.GetEndPoint( 0 ); &nbsp; &nbsp; XYZ p1 = c1.GetEndPoint( 0 ); &nbsp; &nbsp; XYZ p = Util.Midpoint( p0, p1 ); &nbsp; &nbsp; Debug.Assert( &nbsp; &nbsp; &nbsp; p0.IsAlmostEqualTo( c0.Evaluate( t0, false ) ), &nbsp; &nbsp; &nbsp; &quot;expected equal start points&quot; ); &nbsp; &nbsp; Debug.Assert( &nbsp; &nbsp; &nbsp; p1.IsAlmostEqualTo( c1.Evaluate( t1, false ) ), &nbsp; &nbsp; &nbsp; &quot;expected equal start points&quot; ); &nbsp; &nbsp; // Current segment end points. &nbsp; &nbsp; t0 += step0; &nbsp; &nbsp; t1 += step1; &nbsp; &nbsp; XYZ q0, q1, q; &nbsp; &nbsp; Line line; &nbsp; &nbsp; for( int i = 0; i &lt; _nSegments; ++i, t0 += step0, t1 += step1 ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; q0 = c0.Evaluate( t0, false ); &nbsp; &nbsp; &nbsp; q1 = c1.Evaluate( t1, false ); &nbsp; &nbsp; &nbsp; q = Util.Midpoint( q0, q1 ); &nbsp; &nbsp; &nbsp; Debug.Print( &nbsp; &nbsp; &nbsp; &nbsp; &quot;{0} {1} {2} {3}-{4} {5}-{6} {7}-{8}&quot;, &nbsp; &nbsp; &nbsp; &nbsp; i, &nbsp; &nbsp; &nbsp; &nbsp; Util.RealString( t0 ), &nbsp; &nbsp; &nbsp; &nbsp; Util.RealString( t1 ), &nbsp; &nbsp; &nbsp; &nbsp; Util.PointString( p0 ), &nbsp; &nbsp; &nbsp; &nbsp; Util.PointString( q0 ), &nbsp; &nbsp; &nbsp; &nbsp; Util.PointString( p1 ), &nbsp; &nbsp; &nbsp; &nbsp; Util.PointString( q1 ), &nbsp; &nbsp; &nbsp; &nbsp; Util.PointString( p ), &nbsp; &nbsp; &nbsp; &nbsp; Util.PointString( q ) ); &nbsp; &nbsp; &nbsp; // Create approximating curve segment. &nbsp; &nbsp; &nbsp; line = Line.CreateBound( p, q ); &nbsp; &nbsp; &nbsp; creator.CreateModelCurve( line ); &nbsp; &nbsp; &nbsp; p0 = q0; &nbsp; &nbsp; &nbsp; p1 = q1; &nbsp; &nbsp; &nbsp; p = q; &nbsp; &nbsp; } &nbsp; &nbsp; tx.Commit(); &nbsp; }
```
