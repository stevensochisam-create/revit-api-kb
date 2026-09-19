---
num: 879
date: 2013-01-09
themes: [Geometry]
tags: [revit-api, tbc]
---

# Set Detail Curve Visibility

<https://jeremytammik.github.io/tbc/a/0879_set_detail_curve_visib.htm>

```csharp
class DetailCurveSelectionFilter : ISelectionFilter { &nbsp; public bool AllowElement( Element e ) &nbsp; { &nbsp; &nbsp; CurveElementFilter filter &nbsp; &nbsp; &nbsp; = new CurveElementFilter( &nbsp; &nbsp; &nbsp; &nbsp; CurveElementType.DetailCurve ); &nbsp; &nbsp; &nbsp; return filter.PassesFilter( e ); &nbsp; } &nbsp; &nbsp; public bool AllowReference( Reference r, XYZ p ) &nbsp; { &nbsp; &nbsp; return false; &nbsp; } }
```

```csharp
public void SetFamilyVisibility( UIDocument uidoc ) { &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; Reference r = uidoc.Selection.PickObject( &nbsp; &nbsp; ObjectType.Element, &nbsp; &nbsp; new DetailCurveSelectionFilter(), &nbsp; &nbsp; &quot;Select detail curve&quot; ); &nbsp; &nbsp; Element elem = doc.GetElement( r ); &nbsp; &nbsp; Parameter visParam = elem.get_Parameter( &nbsp; &nbsp; BuiltInParameter.GEOM_VISIBILITY_PARAM ); &nbsp; &nbsp; int vis = visParam.AsInteger(); &nbsp; &nbsp; using( Transaction t = new Transaction( doc ) ) &nbsp; { &nbsp; &nbsp; t.Start( &quot;Set curve visibility&quot; ); &nbsp; &nbsp; &nbsp; // Turn off the bit corresponding &nbsp; &nbsp; // to the unwanted modes &nbsp; &nbsp; &nbsp; vis = vis &amp; ~( 1 &lt;&lt; 13 ); // Coarse &nbsp; &nbsp; //vis = vis &amp; ~(1 &lt;&lt; 14); // Medium &nbsp; &nbsp; //vis = vis &amp; ~(1 &lt;&lt; 15); // Fine &nbsp; &nbsp; &nbsp; visParam.Set( vis ); &nbsp; &nbsp; &nbsp; t.Commit(); &nbsp; } }
```
