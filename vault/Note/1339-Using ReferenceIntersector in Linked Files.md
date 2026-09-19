---
num: 1339
date: 2015-07-07
themes: [Geometry, LinkedModel]
tags: [revit-api, tbc]
---

# Using ReferenceIntersector in Linked Files

<https://jeremytammik.github.io/tbc/a/1339_reference_intersector.htm>

```csharp
&nbsp; ReferenceIntersector refIntersector &nbsp; &nbsp; = new ReferenceIntersector( intersectFilter, &nbsp; &nbsp; &nbsp; FindReferenceTarget.Face, view3D ); &nbsp; &nbsp; refIntersector.FindReferencesInRevitLinks = true; &nbsp; &nbsp; IList&lt;ReferenceWithContext&gt; referencesWithContext &nbsp; &nbsp; = refIntersector.Find( startPoint, rayDirection );
```

```csharp
public Dictionary&lt;Reference, XYZ&gt; GetIntersectPoints( &nbsp; Document doc, &nbsp; Element intersect ) { &nbsp; // Find a 3D view to use for the &nbsp; // ReferenceIntersector constructor. &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; Func&lt;View3D, bool&gt; isNotTemplate = v3 &nbsp; &nbsp; =&gt; !( v3.IsTemplate ); &nbsp; &nbsp; View3D view3D = collector &nbsp; &nbsp; .OfClass( typeof( View3D ) ) &nbsp; &nbsp; .Cast&lt;View3D&gt;() &nbsp; &nbsp; .First&lt;View3D&gt;( isNotTemplate ); &nbsp; &nbsp; // Use location point as start point for intersector. &nbsp; &nbsp; LocationCurve lp = intersect.Location as LocationCurve; &nbsp; XYZ startPoint = lp.Curve.GetEndPoint( 0 ) as XYZ; &nbsp; XYZ endPoint = lp.Curve.GetEndPoint( 1 ) as XYZ; &nbsp; &nbsp; // Shoot intersector along element. &nbsp; &nbsp; XYZ rayDirection = endPoint.Subtract( &nbsp; &nbsp; startPoint ).Normalize(); &nbsp; &nbsp; List&lt;BuiltInCategory&gt; builtInCats &nbsp; &nbsp; = new List&lt;BuiltInCategory&gt;(); &nbsp; &nbsp; builtInCats.Add( BuiltInCategory.OST_Roofs ); &nbsp; builtInCats.Add( BuiltInCategory.OST_Ceilings ); &nbsp; builtInCats.Add( BuiltInCategory.OST_Floors ); &nbsp; builtInCats.Add( BuiltInCategory.OST_Walls ); &nbsp; &nbsp; ElementMulticategoryFilter intersectFilter &nbsp; &nbsp; = new ElementMulticategoryFilter( builtInCats ); &nbsp; &nbsp; ReferenceIntersector refIntersector &nbsp; &nbsp; = new ReferenceIntersector( intersectFilter, &nbsp; &nbsp; &nbsp; FindReferenceTarget.Element, view3D ); &nbsp; &nbsp; refIntersector.FindReferencesInRevitLinks = true; &nbsp; &nbsp; IList&lt;ReferenceWithContext&gt; referencesWithContext &nbsp; &nbsp; = refIntersector.Find( startPoint, &nbsp; &nbsp; &nbsp; rayDirection ); &nbsp; &nbsp; IList&lt;XYZ&gt; intersectPoints = new List&lt;XYZ&gt;(); &nbsp; &nbsp; IList&lt;Reference&gt; intersectRefs &nbsp; &nbsp; = new List&lt;Reference&gt;(); &nbsp; &nbsp; Dictionary&lt;Reference, XYZ&gt; dictProvisionForVoidRefs &nbsp; &nbsp; = new Dictionary&lt;Reference, XYZ&gt;(); &nbsp; &nbsp; foreach( ReferenceWithContext r in &nbsp; &nbsp; referencesWithContext ) &nbsp; { &nbsp; &nbsp; dictProvisionForVoidRefs.Add( r.GetReference(), &nbsp; &nbsp; &nbsp; r.GetReference().GlobalPoint ); &nbsp; } &nbsp; return dictProvisionForVoidRefs; }
```
