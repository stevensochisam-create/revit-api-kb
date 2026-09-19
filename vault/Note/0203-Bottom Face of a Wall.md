---
num: 203
date: 2009-08-17
themes: [Geometry]
tags: [revit-api, tbc]
---

# Bottom Face of a Wall

<https://jeremytammik.github.io/tbc/a/0203_wall_bottom_face.htm>

```csharp
Application app = commandData.Application; Document doc = app.ActiveDocument; &nbsp; string s = &quot;a wall, to retrieve its bottom face&quot;; &nbsp; Wall wall = Util.SelectSingleElementOfType( &nbsp; doc, typeof( Wall ), s ) as Wall; &nbsp; if( null == wall ) { &nbsp; message = &quot;Please select a wall.&quot;; } else { &nbsp; Options opt = app.Create.NewGeometryOptions(); &nbsp; GeoElement e = wall.get_Geometry( opt ); &nbsp; &nbsp; foreach( GeometryObject obj in e.Objects ) &nbsp; { &nbsp; &nbsp; Solid solid = obj as Solid; &nbsp; &nbsp; if( null != solid ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( Face face in solid.Faces ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; PlanarFace pf = face as PlanarFace; &nbsp; &nbsp; &nbsp; &nbsp; if( null != pf ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( Util.IsVertical( pf.Normal, _tolerance ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; pf.Normal.Z &lt; 0 ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Util.InfoMsg( string.Format( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;The bottom face area is {0},&quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + &quot; and its origin is at {1}.&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Util.RealString( pf.Area ), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Util.PointString( pf.Origin ) ) ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } } return CmdResult.Failed;
```

```csharp
The bottom face area is 265.82, and its origin is at (30.76,20.57,-9.84).
```
