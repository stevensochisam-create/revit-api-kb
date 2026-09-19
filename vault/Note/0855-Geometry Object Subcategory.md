---
num: 855
date: 2012-11-06
themes: [Geometry]
tags: [revit-api, tbc]
---

# Geometry Object Subcategory

<https://jeremytammik.github.io/tbc/a/0855_geom_obj_category.htm>

```csharp
[Transaction( TransactionMode.ReadOnly )] public class Command : IExternalCommand { &nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication uiapp = commandData.Application; &nbsp; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; &nbsp; Application app = uiapp.Application; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; Selection sel = uidoc.Selection; &nbsp; &nbsp; &nbsp; Reference r = sel.PickObject( ObjectType.Element, &nbsp; &nbsp; &nbsp; &quot;Please pick a family instance&quot; ); &nbsp; &nbsp; &nbsp; Element e = doc.GetElement( r ); &nbsp; &nbsp; &nbsp; GeometryElement geoElem = e.get_Geometry( &nbsp; &nbsp; &nbsp; new Options() ); &nbsp; &nbsp; &nbsp; int n = 0; &nbsp; &nbsp; string s = string.Empty; &nbsp; &nbsp; &nbsp; foreach( GeometryObject obj in geoElem ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( obj is GeometryInstance ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; GeometryInstance geoInst &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = obj as GeometryInstance; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; GeometryElement geoElem2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = geoInst.GetSymbolGeometry(); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; foreach( GeometryObject geoObj2 in geoElem2 ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( geoObj2 is Solid ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Solid solid = geoObj2 as Solid; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ElementId id = solid.GraphicsStyleId; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; GraphicsStyle gStyle = doc.GetElement( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; id ) as GraphicsStyle; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( gStyle != null ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ++n; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; s += gStyle.GraphicsStyleCategory.Name &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + &quot;\r\n&quot;; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; TaskDialog.Show( n.ToString() + &quot; Graphics Styles&quot;, &nbsp; &nbsp; &nbsp; s ); &nbsp; &nbsp; &nbs
```
