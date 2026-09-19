---
num: 707
date: 2012-01-20
themes: [Geometry]
tags: [revit-api, tbc]
---

# Curved Analytical Model Approximation and Etabs Link

<https://jeremytammik.github.io/tbc/a/0707_etabs_rst_link.htm>

```csharp
&nbsp; public IList&lt;Curve&gt; &nbsp; &nbsp; GetStraightLineCurvesFromFloorAnalyticalModel( &nbsp; &nbsp; &nbsp; Document doc, &nbsp; &nbsp; &nbsp; AnalyticalModel analyticalmodel, &nbsp; &nbsp; &nbsp; double lineSegmentLength ) &nbsp; { &nbsp; &nbsp; IList&lt;Curve&gt; Curves; &nbsp; &nbsp; IList&lt;Curve&gt; SegmentedCurves = new List&lt;Curve&gt;(); &nbsp; &nbsp; &nbsp; // If no analytical model then skip &nbsp; &nbsp; &nbsp; if( analyticalmodel == null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return null; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; Curves = analyticalmodel.GetCurves( &nbsp; &nbsp; &nbsp; AnalyticalCurveType.ActiveCurves ); &nbsp; &nbsp; &nbsp; // This does not work: &nbsp; &nbsp; //Curves = analyticalmodel.GetCurves( &nbsp; &nbsp; //&nbsp; AnalyticalCurveType.ApproximatedCurves); &nbsp; &nbsp; &nbsp; foreach( Curve curve in Curves ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; IList&lt;XYZ&gt; pts = curve.Tessellate(); &nbsp; &nbsp; &nbsp; &nbsp; int ibefore = 0; &nbsp; &nbsp; &nbsp; &nbsp; for( int i = 1; i &lt; pts.Count; i++ ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; double distance &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = GeometryUtility.Get3DDistance( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pts[ibefore], pts[i] ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( pts.Count - 1 == i ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SegmentedCurves.Add( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; doc.Application.Create.NewLineBound( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pts[ibefore], pts[i] ) ); &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; else &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( distance &lt; lineSegmentLength ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; else &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SegmentedCurves.Add( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; doc.Application.Create.NewLineBound( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pts[ibefore], pts[i] ) ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ibefore = i; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return SegmentedCurves; &nbsp; }
```
