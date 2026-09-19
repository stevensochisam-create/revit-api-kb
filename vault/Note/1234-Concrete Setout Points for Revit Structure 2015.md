---
num: 1234
date: 2014-11-03
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Concrete Setout Points for Revit Structure 2015

<https://jeremytammik.github.io/tbc/a/1234_setout_points.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Retrieve the first non-empty solid found for &nbsp; /// the given element. In case the element is a &nbsp; /// family instance, it may have its own non-empty &nbsp; /// solid, in which case we use that. Otherwise we &nbsp; /// search the symbol geometry. If we use the &nbsp; /// symbol geometry, we have to keep track of the &nbsp; /// instance transform to map it to the actual &nbsp; /// instance project location. &nbsp; /// &lt;/summary&gt; &nbsp; Solid GetSolid( &nbsp; &nbsp; Element e, &nbsp; &nbsp; Options opt, &nbsp; &nbsp; out Transform t ) &nbsp; { &nbsp; &nbsp; GeometryElement geo = e.get_Geometry( opt ); &nbsp; &nbsp; &nbsp; Solid solid = null; &nbsp; &nbsp; GeometryInstance inst = null; &nbsp; &nbsp; t = Transform.Identity; &nbsp; &nbsp; &nbsp; // Some columns have no solids, and we have to &nbsp; &nbsp; // retrieve the geometry from the symbol; &nbsp; &nbsp; // others do have solids on the instance itself &nbsp; &nbsp; // and no contents in the instance geometry &nbsp; &nbsp; // (e.g. in rst_basic_sample_project.rvt). &nbsp; &nbsp; &nbsp; foreach( GeometryObject obj in geo ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; solid = obj as Solid; &nbsp; &nbsp; &nbsp; &nbsp; if( null != solid &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; 0 &lt; solid.Faces.Size ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; inst = obj as GeometryInstance; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; if( null == solid &amp;&amp; null != inst ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; geo = inst.GetSymbolGeometry(); &nbsp; &nbsp; &nbsp; t = inst.Transform; &nbsp; &nbsp; &nbsp; &nbsp; foreach( GeometryObject obj in geo ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; solid = obj as Solid; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( null != solid &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; 0 &lt; solid.Faces.Size ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return solid; &nbsp; }
```

```csharp
&nbsp; XYZ p1 = t.OfPoint( p ); &nbsp; &nbsp; FamilyInstance fi &nbsp; &nbsp; = doc.Create.NewFamilyInstance( p1, &nbsp; &nbsp; &nbsp; symbols[1], StructuralType.NonStructural );
```
