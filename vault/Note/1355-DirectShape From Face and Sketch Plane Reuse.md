---
num: 1355
date: 2015-09-08
themes: [Geometry]
tags: [revit-api, tbc]
---

# DirectShape From Face and Sketch Plane Reuse

<https://jeremytammik.github.io/tbc/a/1355_directshape_face.html>

```csharp
&nbsp; Selection choices = uidoc.Selection; &nbsp; &nbsp; Reference reference = choices.PickObject( &nbsp; &nbsp; ObjectType.Face ); &nbsp; &nbsp; Element el = doc.GetElement( &nbsp; &nbsp; reference.ElementId ); &nbsp; &nbsp; Face face = el.GetGeometryObjectFromReference( &nbsp; &nbsp; reference ) as Face;
```

```csharp
/// &lt;summary&gt; /// Determine the stack of transforms to apply to /// the given target geometry object to bring it /// to the proper location in the project coordinates. /// Unfortunetely, we have not found any way at all /// yet to identify the target object we are after. /// &lt;/summary&gt; static bool GetTransformStackForObject( &nbsp; Stack&lt;Transform&gt; tstack, &nbsp; GeometryElement geo, &nbsp; GeometryObject targetObj, &nbsp; Reference targetRef ) { &nbsp; foreach( GeometryObject obj in geo ) &nbsp; { &nbsp; &nbsp; if( obj == targetObj ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; GeometryInstance gi = obj as GeometryInstance; &nbsp; &nbsp; &nbsp; if( null != gi ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; tstack.Push( gi.Transform ); &nbsp; &nbsp; &nbsp; return GetTransformStackForObject( tstack, &nbsp; &nbsp; &nbsp; &nbsp; gi.GetInstanceGeometry(), targetObj, targetRef ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; Solid solid = obj as Solid; &nbsp; &nbsp; if( null != solid ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( 0 &lt; solid.Faces.Size ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; foreach( Face face in solid.Faces ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( face == targetObj ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( face.Reference == targetRef ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; if( 0 &lt; solid.Edges.Size ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; foreach( Edge edge in solid.Edges ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( edge == targetObj ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( edge.Reference == targetRef ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; return false; }
```
