---
num: 1035
date: 2013-10-14
themes: [Geometry]
tags: [revit-api, tbc]
---

# LINQ DIY Transformed Geometry Bounding Box

<https://jeremytammik.github.io/tbc/a/1035_geo_bound_box.htm>

```csharp
public void test( Element elem ) { &nbsp; Options geomOpts = new Options(); &nbsp; &nbsp; GeometryElement geometryElement &nbsp; &nbsp; = elem.get_Geometry( geomOpts ); &nbsp; &nbsp; if( geometryElement == null ) &nbsp; &nbsp; return; &nbsp; &nbsp; BoundingBoxXYZ preTransformBox &nbsp; &nbsp; = geometryElement.GetBoundingBox(); &nbsp; &nbsp; GeometryElement geometryElementTransformed &nbsp; &nbsp; = geometryElement.GetTransformed( &nbsp; &nbsp; &nbsp; Transform.Identity ); &nbsp; &nbsp; BoundingBoxXYZ blah = new BoundingBoxXYZ(); &nbsp; &nbsp; BoundingBoxXYZ postTransformBox &nbsp; &nbsp; = geometryElementTransformed.GetBoundingBox(); &nbsp; &nbsp; System.Windows.Forms.MessageBox.Show( &nbsp; &nbsp; &quot;Pre Min: &quot; + preTransformBox.Min.ToString() &nbsp; &nbsp; + &quot;\nPre Max: &quot; + preTransformBox.Min.ToString() &nbsp; &nbsp; + &quot;\nPost Min: &quot; + postTransformBox.Min.ToString() &nbsp; &nbsp; + &quot;\nPost Max: &quot; + postTransformBox.Min.ToString() ); }
```

```csharp
&nbsp; &nbsp; // get points from all edges in all solids &nbsp; &nbsp; // - allows for curves by using tessellated &nbsp; &nbsp; // edges &nbsp; &nbsp; List&lt;XYZ&gt; pts = new List&lt;XYZ&gt;(); &nbsp; &nbsp; foreach( Solid solid in geometryElement &nbsp; &nbsp; &nbsp; .OfType&lt;Solid&gt;() ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( Edge edge in solid.Edges ) &nbsp; &nbsp; &nbsp; &nbsp; pts.AddRange( edge.Tessellate() ); &nbsp; &nbsp; }
```

```csharp
&nbsp; #if _REVIT2014_ &nbsp; &nbsp; XYZ StartPoint = lc.Curve.GetEndPoint(0); &nbsp; &nbsp; XYZ EndPoint = lc.Curve.GetEndPoint(1); &nbsp; #else &nbsp; &nbsp; XYZ StartPoint = lc.Curve.get_EndPoint( 0 ); &nbsp; &nbsp; XYZ EndPoint = lc.Curve.get_EndPoint( 1 ); &nbsp; #endif
```
