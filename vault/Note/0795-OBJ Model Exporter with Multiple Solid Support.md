---
num: 795
date: 2012-07-03
themes: [Geometry]
tags: [revit-api, tbc]
---

# OBJ Model Exporter with Multiple Solid Support

<https://jeremytammik.github.io/tbc/a/0795_obj_export_solids.htm>

```csharp
int GetRevitTextColorFromSystemColor( &nbsp; System.Drawing.Color color ) { &nbsp; return ( ( (int) color.R ) * (int) Math.Pow( 2, 0 ) &nbsp; &nbsp; + ( (int) color.G ) * (int) Math.Pow( 2, 8 ) &nbsp; &nbsp; + ( (int) color.B ) * (int) Math.Pow( 2, 16 ) ); }
```

```csharp
&nbsp; // Set Revit text colour from system colour &nbsp; &nbsp; int color = GetRevitTextColorFromSystemColor( &nbsp; &nbsp; System.Drawing.Color.Wheat ); &nbsp; &nbsp; tnt.get_Parameter( BuiltInParameter.LINE_COLOR ) &nbsp; &nbsp; .Set( color );
```

```csharp
bool ExportSolid( &nbsp; IJtFaceEmitter emitter, &nbsp; Document doc, &nbsp; Solid solid, &nbsp; Color color ) { &nbsp; foreach( Face face in solid.Faces ) &nbsp; { &nbsp; &nbsp; Material m = doc.GetElement( &nbsp; &nbsp; &nbsp; face.MaterialElementId ) as Material; &nbsp; &nbsp; &nbsp; Color c = ( null == m ) ? color : m.Color; &nbsp; &nbsp; &nbsp; emitter.EmitFace( face, &nbsp; &nbsp; &nbsp; (null == c) ? _default_color : c ); &nbsp; } &nbsp; return true; } &nbsp; /// &lt;summary&gt; /// Export all non-empty solids found for /// the given element. Family instances may have /// their own non-empty solids, in which case /// those are used, otherwise the symbol geometry. /// The symbol geometry could keep track of the /// instance transform to map it to the actual /// project location. Instead, we ask for /// transformed geometry to be returned, so the /// resulting solids are already in place. /// &lt;/summary&gt; int ExportSolids( &nbsp; IJtFaceEmitter emitter, &nbsp; Element e, &nbsp; Options opt, &nbsp; Color color ) { &nbsp; int nSolids = 0; &nbsp; &nbsp; GeometryElement geo = e.get_Geometry( opt ); &nbsp; &nbsp; Solid solid; &nbsp; &nbsp; if( null != geo ) &nbsp; { &nbsp; &nbsp; Document doc = e.Document; &nbsp; &nbsp; &nbsp; if( e is FamilyInstance ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; geo = geo.GetTransformed( &nbsp; &nbsp; &nbsp; &nbsp; Transform.Identity ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; GeometryInstance inst = null; &nbsp; &nbsp; &nbsp; foreach( GeometryObject obj in geo ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; solid = obj as Solid; &nbsp; &nbsp; &nbsp; &nbsp; if( null != solid &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; 0 &lt; solid.Faces.Size &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; ExportSolid( emitter, doc, solid, color ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; ++nSolids; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; inst = obj as GeometryInstance; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; if( 0 == nSolids &amp;&amp; null != inst ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; geo = inst.GetSymbolGeometry(); &nbsp; &nbsp; &nbsp; &nbsp; foreach( GeometryObject obj in geo ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; solid = obj as Solid; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( null != solid &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; 0 &lt; solid.Faces.Size &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; ExportSolid( emitter, doc, solid, color 
```
