---
num: 98
date: 2009-02-13
themes: [Geometry]
tags: [revit-api, tbc]
---

# Boolean Operations for 2D Polygons

<https://jeremytammik.github.io/tbc/a/0098_booleans_on_polygons.htm>

```csharp
Polygon getPolygon( Floor floor ) { &nbsp; Options geomOptions &nbsp; &nbsp; = app.Create.NewGeometryOptions(); &nbsp; &nbsp; GeoElement elem &nbsp; &nbsp; = floor.get_Geometry( geomOptions ); &nbsp; &nbsp; List&lt;Vertex&gt; vertices = new List&lt;Vertex&gt;(); &nbsp; &nbsp; foreach( object obj in elem.Objects ) &nbsp; { &nbsp; &nbsp; Solid solid = obj as Solid; &nbsp; &nbsp; if( null != solid ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Face face = solid.Faces.get_Item( 0 ); &nbsp; &nbsp; &nbsp; EdgeArray loop = face.EdgeLoops.get_Item( 0 ); &nbsp; &nbsp; &nbsp; foreach( Edge edge in loop ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; XYZArray edgePts = edge.Tessellate(); &nbsp; &nbsp; &nbsp; &nbsp; int n = edgePts.Size; &nbsp; &nbsp; &nbsp; &nbsp; for( int i = 0; i &lt; n - 1; ++i ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; XYZ p = edgePts.get_Item( i ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; vertices.Add( new Vertex( p.X, p.Y ) ); &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; } &nbsp; } &nbsp; VertexList vertexList = new VertexList(); &nbsp; vertexList.NofVertices = vertices.Count; &nbsp; vertexList.Vertex = vertices.ToArray(); &nbsp; Polygon poly = new Polygon(); &nbsp; poly.AddContour( vertexList, false ); &nbsp; return poly; }
```

```csharp
CmdResult rc = CmdResult.Failed; app = commandData.Application; doc = app.ActiveDocument; &nbsp; Floor[] floors = new Floor[2] { null, null }; &nbsp; // get the first 2 floors of the selection foreach( RvtElement e in doc.Selection.Elements ) { &nbsp; if( null == floors[0] ) &nbsp; { &nbsp; &nbsp; floors[0] = e as Floor; &nbsp; } &nbsp; else if( null == floors[1] ) &nbsp; { &nbsp; &nbsp; floors[1] = e as Floor; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; break; &nbsp; } } &nbsp; // if the selction did not contain two floors, return if( null == floors[0] || null == floors[1] ) { &nbsp; MessageBox.Show( &nbsp; &nbsp; "Please select two floors before" &nbsp; &nbsp; + " running this command.", &nbsp; &nbsp; "GpcNET" ); } else { &nbsp; // get the intersection &nbsp; Polygon poly1 = getPolygon( floors[0] ); &nbsp; &nbsp; Polygon poly2 = getPolygon( floors[1] ); &nbsp; &nbsp; Polygon poly3 = poly1.Clip( &nbsp; &nbsp; GpcOperation.Intersection, &nbsp; &nbsp; poly2 ); &nbsp; &nbsp; // if it looks like a valid polygon, create a new floor &nbsp; if( 0 &lt; poly3.NofContours ) &nbsp; { &nbsp; &nbsp; CurveArray curves = app.Create.NewCurveArray(); &nbsp; &nbsp; VertexList v = poly3.Contour[0]; &nbsp; &nbsp; int i, j, n = v.NofVertices; &nbsp; &nbsp; for( i = 0; i &lt; n; ++i ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; j = ( i + 1 ) % n; &nbsp; &nbsp; &nbsp; Vertex p = v.Vertex[i]; &nbsp; &nbsp; &nbsp; Vertex q = v.Vertex[j]; &nbsp; &nbsp; &nbsp; &nbsp; curves.Append( app.Create.NewLineBound( &nbsp; &nbsp; &nbsp; &nbsp; app.Create.NewXYZ( p.X, p.Y, 0 ), &nbsp; &nbsp; &nbsp; &nbsp; app.Create.NewXYZ( q.X, q.Y, 0 ) ) ); &nbsp; &nbsp; } &nbsp; &nbsp; doc.Create.NewFloor( curves, &nbsp; &nbsp; &nbsp; floors[0].FloorType, &nbsp; &nbsp; &nbsp; floors[0].Level, false ); &nbsp; &nbsp; &nbsp; rc = CmdResult.Succeeded; &nbsp; } } return rc;
```
