---
num: 692
date: 2011-12-12
themes: [Geometry]
tags: [revit-api, tbc]
---

# Top Faces of Sloped Wall Update

<https://jeremytammik.github.io/tbc/a/0692_top_faces_of_wall.htm>

```csharp
if( f is PlanarFace && PointsUpwards( ((PlanarFace)f).Normal ) )
```

```csharp
0 top faces found on Walls 0 top faces found on Walls
```

```csharp
&nbsp; For Each f As DB.Face In Solid.Faces &nbsp; &nbsp; ' &nbsp; &nbsp; If TypeOf f Is DB.PlanarFace Then &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; Dim pf As DB.PlanarFace = f &nbsp; &nbsp; &nbsp; Dim p As XYZ = pf.Origin &nbsp; &nbsp; &nbsp; If pf.ComputeNormal(New DB.UV(p.X, p.Y)).Z &gt; 0 Then &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; &nbsp; Dim faceVertices As IList(Of DB.XYZ) _ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = pf.Triangulate().Vertices &nbsp; &nbsp; &nbsp; &nbsp; For Each v As DB.XYZ In faceVertices &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; If sideVertices.Contains(v, comparer) Then &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; If Not ret.Contains(f) Then &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ret.Add(f) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; End If &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Exit For &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; End If &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; &nbsp; Next &nbsp; &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; &nbsp; End If &nbsp; &nbsp; &nbsp; ' &nbsp; &nbsp; End If &nbsp; &nbsp; ' &nbsp; Next
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Super-simple test whether a face is planar &nbsp; /// and its normal vector points upwards. &nbsp; /// &lt;/summary&gt; &nbsp; static bool IsTopPlanarFace( Face f ) &nbsp; { &nbsp; &nbsp; return f is PlanarFace &nbsp; &nbsp; &nbsp; &amp;&amp; PointsUpwards( ( (PlanarFace) f ).Normal ); &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Simple test whether a given face normal vector &nbsp; /// points upwards in the middle of the face. &nbsp; /// &lt;/summary&gt; &nbsp; static bool IsTopFace( Face f ) &nbsp; { &nbsp; &nbsp; BoundingBoxUV b = f.GetBoundingBox(); &nbsp; &nbsp; UV p = b.Min; &nbsp; &nbsp; UV q = b.Max; &nbsp; &nbsp; UV midpoint = p + 0.5 * ( q - p ); &nbsp; &nbsp; XYZ normal = f.ComputeNormal( midpoint ); &nbsp; &nbsp; return PointsUpwards( normal ); &nbsp; }
```
