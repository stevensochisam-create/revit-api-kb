---
num: 289
date: 2010-01-22
themes: [Geometry, MEP]
tags: [revit-api, tbc]
---

# Insert Face-Hosted Sprinkler

<https://jeremytammik.github.io/tbc/a/0289_insert_sprinkler.htm>

```csharp
FamilyInstance NewFamilyInstance( Face face, XYZ location, XYZ referenceDirection, FamilySymbol symbol )
```

```csharp
XYZ PointOnFace( PlanarFace face ) { &nbsp; XYZ p = new XYZ( 0, 0, 0 ); &nbsp; Mesh mesh = face.Triangulate(); &nbsp; &nbsp; for( int i = 0; i &lt; mesh.NumTriangles; ++i ) &nbsp; { &nbsp; &nbsp; MeshTriangle triangle = mesh.get_Triangle( i ); &nbsp; &nbsp; p += triangle.get_Vertex( 0 ); &nbsp; &nbsp; p += triangle.get_Vertex( 1 ); &nbsp; &nbsp; p += triangle.get_Vertex( 2 ); &nbsp; &nbsp; p *= 0.3333333333333333; &nbsp; &nbsp; break; &nbsp; } &nbsp; return p; }
```

```csharp
Application app = commandData.Application; Document doc = app.ActiveDocument; &nbsp; // retrieve the sprinkler family symbol: &nbsp; Filter filter = app.Create.Filter.NewFamilyFilter( &nbsp; _name ); &nbsp; List&lt;RvtElement&gt; families = new List&lt;RvtElement&gt;(); doc.get_Elements( filter, families ); Family family = null; &nbsp; foreach( RvtElement e in families ) { &nbsp; family = e as Family; &nbsp; if( null != family ) &nbsp; &nbsp; break; } &nbsp; if( null == family ) { &nbsp; if( !doc.LoadFamily( _filename, out family ) ) &nbsp; { &nbsp; &nbsp; message = &quot;Unable to load '&quot; + _filename + &quot;'.&quot;; &nbsp; &nbsp; return CmdResult.Failed; &nbsp; } } &nbsp; FamilySymbol sprinklerSymbol = null; foreach( FamilySymbol fs in family.Symbols ) { &nbsp; sprinklerSymbol = fs; &nbsp; break; } &nbsp; Debug.Assert( null != sprinklerSymbol, &nbsp; &quot;expected at least one sprinkler symbol&quot; &nbsp; + &quot; to be defined in family&quot; ); &nbsp; // pick the host ceiling: &nbsp; RvtElement ceiling = Util.SelectSingleElement( &nbsp; doc, &quot;ceiling to host sprinkler&quot; ); &nbsp; if( null == ceiling &nbsp; || !ceiling.Category.Id.Value.Equals( &nbsp; &nbsp; (int) BuiltInCategory.OST_Ceilings ) ) { &nbsp; message = &quot;No ceiling selected.&quot;; &nbsp; return CmdResult.Failed; } &nbsp; // retrieve the bottom face of the ceiling: &nbsp; Options opt = app.Create.NewGeometryOptions(); opt.ComputeReferences = true; GeoElement geo = ceiling.get_Geometry( opt ); &nbsp; PlanarFace ceilingBottom = null; &nbsp; foreach( GeometryObject obj in geo.Objects ) { &nbsp; Solid solid = obj as Solid; &nbsp; &nbsp; if( null != solid ) &nbsp; { &nbsp; &nbsp; foreach( Face face in solid.Faces ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; PlanarFace pf = face as PlanarFace; &nbsp; &nbsp; &nbsp; &nbsp; if( null != pf ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; XYZ normal = pf.Normal.Normalized; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( Util.IsVertical( normal ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; 0.0 &gt; normal.Z ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ceilingBottom = pf; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } } if( null != ceilingBottom ) { &nbsp; XYZ p = PointOnFace( ceilingBottom ); &nbsp; &nbsp; // create the sprinkler family instance &nb
```
