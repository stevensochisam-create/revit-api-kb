---
num: 666
date: 2011-10-17
themes: [Geometry]
tags: [revit-api, tbc]
---

# Retrieving Detailed Wall Layer Geometry

<https://jeremytammik.github.io/tbc/a/0666_wall_layer_geom.htm>

```csharp
public List&lt;XYZ&gt; GetBottomFacePoints( Element e ) { &nbsp; List&lt;XYZ&gt; resultingPts = new List&lt;XYZ&gt;(); &nbsp; &nbsp; FaceExtractor faceExtractor &nbsp; &nbsp; = new FaceExtractor( e ); &nbsp; &nbsp; FaceArray faces = faceExtractor.Faces; &nbsp; &nbsp; if( faces.Size == 0 ) { return resultingPts; } &nbsp; &nbsp; foreach( Face face in faces ) &nbsp; { &nbsp; &nbsp; PlanarFace pf = face as PlanarFace; &nbsp; &nbsp; &nbsp; if( pf == null ) { continue; } &nbsp; &nbsp; &nbsp; if( pf.Normal.IsAlmostEqualTo( -XYZ.BasisZ ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; EdgeArrayArray edgeLoops = face.EdgeLoops; &nbsp; &nbsp; &nbsp; &nbsp; foreach( EdgeArray edgeArray in edgeLoops ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; foreach( Edge edge in edgeArray ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; List&lt;XYZ&gt; points &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = edge.Tessellate() as List&lt;XYZ&gt;; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; resultingPts.AddRange( points ); &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; return resultingPts; }
```
