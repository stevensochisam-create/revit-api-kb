---
num: 33
date: 2008-11-05
themes: [Geometry]
tags: [revit-api, tbc]
---

# Slab Side Faces

<https://jeremytammik.github.io/tbc/a/0033_slab_side_faces.htm>

```csharp
public CmdResult Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; Application app = commandData.Application; &nbsp; Document doc = app.ActiveDocument; &nbsp; &nbsp; List&lt;RvtElement&gt; floors = new List&lt;RvtElement&gt;(); &nbsp; if( !Util.GetSelectedElementsOrAll( &nbsp; &nbsp; floors, doc, typeof( Floor ) ) ) &nbsp; { &nbsp; &nbsp; Selection sel = doc.Selection; &nbsp; &nbsp; message = ( 0 &lt; sel.Elements.Size ) &nbsp; &nbsp; &nbsp; ? "Please select some floor elements." &nbsp; &nbsp; &nbsp; : "No floor elements found."; &nbsp; &nbsp; return CmdResult.Failed; &nbsp; } &nbsp; &nbsp; List&lt;Face&gt; faces = new List&lt;Face&gt;(); &nbsp; Options opt = app.Create.NewGeometryOptions(); &nbsp; &nbsp; foreach( Floor floor in floors ) &nbsp; { &nbsp; &nbsp; GeoElement geo = floor.get_Geometry( opt ); &nbsp; &nbsp; GeometryObjectArray objects = geo.Objects; &nbsp; &nbsp; foreach( GeometryObject obj in objects ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Solid solid = obj as Solid; &nbsp; &nbsp; &nbsp; if( solid != null ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; GetSideFaces( faces, solid ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; int n = faces.Count; &nbsp; &nbsp; Debug.WriteLine( string.Format( &nbsp; &nbsp; "{0} side face{1} found.", &nbsp; &nbsp; n, Util.PluralSuffix( n ) ) ); &nbsp; &nbsp; Creator creator = new Creator( app ); &nbsp; foreach( Face f in faces ) &nbsp; { &nbsp; &nbsp; creator.DrawFaceTriangleNormals( f ); &nbsp; } &nbsp; return CmdResult.Succeeded; }
```

```csharp
void GetSideFaces( &nbsp; List&lt;Face&gt; verticalFaces, &nbsp; Solid solid ) { &nbsp; FaceArray faces = solid.Faces; &nbsp; foreach( Face f in faces ) &nbsp; { &nbsp; &nbsp; if( f is PlanarFace ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( Util.IsVertical( f as PlanarFace ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; verticalFaces.Add( f ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; if( f is CylindricalFace ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( Util.IsVertical( f as CylindricalFace ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; verticalFaces.Add( f ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } }
```

```csharp
public void DrawFaceTriangleNormals( Face f ) { &nbsp; Mesh mesh = f.Triangulate(); &nbsp; int n = mesh.NumTriangles; &nbsp; &nbsp; string s = "{0} face triangulation returns " &nbsp; &nbsp; + "mesh triangle{1} and normal vector{1}:"; &nbsp; &nbsp; Debug.WriteLine( string.Format( &nbsp; &nbsp; s, n, Util.PluralSuffix( n ) ) ); &nbsp; &nbsp; for( int i = 0; i &lt; n; ++i ) &nbsp; { &nbsp; &nbsp; MeshTriangle t = mesh.get_Triangle( i ); &nbsp; &nbsp; &nbsp; XYZ p = ( t.get_Vertex( 0 ) &nbsp; &nbsp; &nbsp; + t.get_Vertex( 1 ) &nbsp; &nbsp; &nbsp; + t.get_Vertex( 2 ) ) / 3; &nbsp; &nbsp; &nbsp; XYZ v = t.get_Vertex( 1 ) &nbsp; &nbsp; &nbsp; - t.get_Vertex( 0 ); &nbsp; &nbsp; &nbsp; XYZ w = t.get_Vertex( 2 ) &nbsp; &nbsp; &nbsp; - t.get_Vertex( 0 ); &nbsp; &nbsp; &nbsp; XYZ normal = v.Cross( w ).Normalized; &nbsp; &nbsp; &nbsp; Debug.WriteLine( string.Format( &nbsp; &nbsp; &nbsp; "{0} {1} --&gt; {2}", i, &nbsp; &nbsp; &nbsp; Util.PointString( p ), &nbsp; &nbsp; &nbsp; Util.PointString( normal ) ) ); &nbsp; &nbsp; &nbsp; CreateModelLine( p, p + normal ); &nbsp; } }
```
