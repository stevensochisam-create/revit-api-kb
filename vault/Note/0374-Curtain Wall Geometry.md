---
num: 374
date: 2010-05-26
themes: [Geometry]
tags: [revit-api, tbc]
---

# Curtain Wall Geometry

<https://jeremytammik.github.io/tbc/a/0374_curtain_wall_geometry.htm>

```csharp
C:\tmp\ &gt;diff RevitElementsBeforeCurtainWall.txt RevitElementsAfterCurtainWall.txt 2842a2843,2844 &gt; Id=149169; Class=Wall; Category=Walls; Name=Curtain Wall &gt; Id=149170; Class=Panel; Category=Curtain Panels; Name=Glazed
```

```csharp
C:\tmp\ &gt;diff RevitElementsBeforeCurtainWall2010.txt RevitElementsAfterCurtainWall2010.txt 2255a2256,2257 &gt; Id=130424; Class=Wall; Category=Walls; Name=Curtain Wall &gt; Id=130425; Class=Panel; Category=Curtain Panels; Name=Glazed
```

```csharp
void list_wall_geom( Wall w, Application app ) { &nbsp; string s = &quot;&quot;; &nbsp; &nbsp; CurtainGrid cgrid = w.CurtainGrid; &nbsp; &nbsp; Options options &nbsp; &nbsp; = app.Create.NewGeometryOptions(); &nbsp; &nbsp; options.ComputeReferences = true; &nbsp; options.IncludeNonVisibleObjects = true; &nbsp; &nbsp; GeometryElement geomElem &nbsp; &nbsp; = w.get_Geometry( options ); &nbsp; &nbsp; foreach( GeometryObject obj &nbsp; &nbsp; in geomElem.Objects ) &nbsp; { &nbsp; &nbsp; Visibility vis = obj.Visibility; &nbsp; &nbsp; &nbsp; string visString = vis.ToString(); &nbsp; &nbsp; &nbsp; Arc arc = obj as Arc; &nbsp; &nbsp; Line line = obj as Line; &nbsp; &nbsp; Solid solid = obj as Solid; &nbsp; &nbsp; &nbsp; if( arc != null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; double length = arc.ApproximateLength; &nbsp; &nbsp; &nbsp; &nbsp; s += &quot;Length (arc) (&quot; + visString + &quot;): &quot; &nbsp; &nbsp; &nbsp; &nbsp; + length + &quot;\n&quot;; &nbsp; &nbsp; } &nbsp; &nbsp; if( line != null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; double length = line.ApproximateLength; &nbsp; &nbsp; &nbsp; &nbsp; s += &quot;Length (line) (&quot; + visString + &quot;): &quot; &nbsp; &nbsp; &nbsp; &nbsp; + length + &quot;\n&quot;; &nbsp; &nbsp; } &nbsp; &nbsp; if( solid != null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; int faceCount = solid.Faces.Size; &nbsp; &nbsp; &nbsp; &nbsp; s += &quot;Faces: &quot; + faceCount + &quot;\n&quot;; &nbsp; &nbsp; &nbsp; &nbsp; foreach( Face face in solid.Faces ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; s += &quot;Face area (&quot; + visString + &quot;): &quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + face.Area + &quot;\n&quot;; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; if( line == null &amp;&amp; solid == null &amp;&amp; arc == null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; s += &quot;&lt;Other&gt;\n&quot;; &nbsp; &nbsp; } &nbsp; } &nbsp; TaskDialog.Show( &quot;revit&quot;, s ); }
```
