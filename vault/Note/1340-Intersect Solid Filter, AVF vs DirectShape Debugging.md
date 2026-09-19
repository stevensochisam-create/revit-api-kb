---
num: 1340
date: 2015-07-08
themes: [Geometry]
tags: [revit-api, tbc]
---

# Intersect Solid Filter, AVF vs DirectShape Debugging

<https://jeremytammik.github.io/tbc/a/1340_inters_solid_filt.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Create and return a cube of &nbsp; /// side length d at the origin. &nbsp; /// &lt;/summary&gt; &nbsp; static Solid CreateCube( double d ) &nbsp; { &nbsp; &nbsp; return CreateRectangularPrism( &nbsp; &nbsp; &nbsp; XYZ.Zero, d, d, d ); &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Create and return a rectangular prism of the &nbsp; /// given side lengths centered at the given point. &nbsp; /// &lt;/summary&gt; &nbsp; static Solid CreateRectangularPrism( &nbsp; &nbsp; XYZ center, &nbsp; &nbsp; double d1, &nbsp; &nbsp; double d2, &nbsp; &nbsp; double d3 ) &nbsp; { &nbsp; &nbsp; List&lt;Curve&gt; profile = new List&lt;Curve&gt;(); &nbsp; &nbsp; XYZ profile00 = new XYZ( -d1 / 2, -d2 / 2, -d3 / 2 ); &nbsp; &nbsp; XYZ profile01 = new XYZ( -d1 / 2, d2 / 2, -d3 / 2 ); &nbsp; &nbsp; XYZ profile11 = new XYZ( d1 / 2, d2 / 2, -d3 / 2 ); &nbsp; &nbsp; XYZ profile10 = new XYZ( d1 / 2, -d2 / 2, -d3 / 2 ); &nbsp; &nbsp; &nbsp; profile.Add( Line.CreateBound( profile00, profile01 ) ); &nbsp; &nbsp; profile.Add( Line.CreateBound( profile01, profile11 ) ); &nbsp; &nbsp; profile.Add( Line.CreateBound( profile11, profile10 ) ); &nbsp; &nbsp; profile.Add( Line.CreateBound( profile10, profile00 ) ); &nbsp; &nbsp; &nbsp; CurveLoop curveLoop = CurveLoop.Create( profile ); &nbsp; &nbsp; &nbsp; SolidOptions options = new SolidOptions( &nbsp; &nbsp; &nbsp; ElementId.InvalidElementId, &nbsp; &nbsp; &nbsp; ElementId.InvalidElementId ); &nbsp; &nbsp; &nbsp; return GeometryCreationUtilities &nbsp; &nbsp; &nbsp; .CreateExtrusionGeometry( &nbsp; &nbsp; &nbsp; &nbsp; new CurveLoop[] { curveLoop }, &nbsp; &nbsp; &nbsp; &nbsp; XYZ.BasisZ, d3, options ); &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Create and return a solid sphere &nbsp; /// with a given radius and centre point. &nbsp; /// &lt;/summary&gt; &nbsp; static public Solid CreateSphereAt( &nbsp; &nbsp; XYZ centre, &nbsp; &nbsp; double radius ) &nbsp; { &nbsp; &nbsp; // Use the standard global coordinate system &nbsp; &nbsp; // as a frame, translated to the sphere centre. &nbsp; &nbsp; &nbsp; Frame frame = new Frame( centre, XYZ.BasisX, &nbsp; &nbsp; &nbsp; XYZ.BasisY, XYZ.BasisZ ); &nbsp; &nbsp; &nbsp; // Create a vertical half-circle loop &nbsp; &nbsp; // that must be in the frame location. &nbsp; &nbsp; &nbsp; Arc arc = Arc.Create( &nbsp; &nbsp; &nbsp; centre - radius * XYZ.BasisZ, &nbsp; &nbsp; &nbsp; centre + radius * XYZ.BasisZ, &nbsp; &nbsp; &nbsp; centre + radius * XYZ.BasisX ); &nbsp; &nbsp; &nbsp; Line line = Line.CreateBound( &nbsp; &nbsp; &nbsp; arc.GetEndPoint( 1 ), &nbsp; &nbsp; &nbsp; arc.GetEndPoint( 0 ) ); &nbsp; &nbsp; &nbsp; CurveLoop halfCircle = new CurveLoop(); &nbsp; &nbsp; halfCircle.Append( arc ); &nbsp; &nbsp; halfCircle.Append( line ); &nbsp; &nbsp; &nbsp; List&lt;CurveLoop&gt; loops = new List&lt;CurveLoop&gt;( 1 ); &nbsp; &nbsp; loops.Add( halfCircle ); &nbsp; &nbsp; &nbsp; return GeometryCreationUtilities &nbsp; &nbsp; &nbsp; .CreateRevolvedGeometry( frame, loops, &nbsp; &nbsp; &nbsp; &nbsp; 0, 2 * Math.PI ); &nbsp; }
```
