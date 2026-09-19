---
num: 1282
date: 2015-02-14
themes: [Geometry]
tags: [revit-api, tbc]
---

# Determining the Face Tangent at a Picked Point

<https://jeremytammik.github.io/tbc/a/1282_face_point_tangent.htm>

```csharp
&nbsp; Reference r = uidoc.Selection.PickObject( &nbsp; &nbsp; ObjectType.Face, &quot;Please pick a point on a &quot; &nbsp; &nbsp; + &quot;face for family instance insertion&quot; ); &nbsp; &nbsp; Element e = doc.GetElement( r.ElementId ); &nbsp; &nbsp; GeometryObject obj &nbsp; &nbsp; = e.GetGeometryObjectFromReference( r ); &nbsp; &nbsp; //PlanarFace face = obj as PlanarFace; &nbsp; CylindricalFace face = obj as CylindricalFace; &nbsp; &nbsp; XYZ p = r.GlobalPoint; &nbsp; XYZ v = face.Axis.CrossProduct( XYZ.BasisZ ); &nbsp; if( v.IsZeroLength() ) &nbsp; { &nbsp; &nbsp; v = face.Axis.CrossProduct( XYZ.BasisX ); &nbsp; } &nbsp; doc.Create.NewFamilyInstance( r, p, v, symbol );
```

```csharp
&nbsp; Reference r = uidoc.Selection.PickObject( &nbsp; &nbsp; ObjectType.Face, &quot;Please pick a point on a &quot; &nbsp; &nbsp; + &quot;face for family instance insertion&quot; ); &nbsp; &nbsp; Element e = doc.GetElement( r.ElementId ); &nbsp; &nbsp; GeometryObject obj &nbsp; &nbsp; = e.GetGeometryObjectFromReference( r ); &nbsp; &nbsp; PlanarFace face = obj as PlanarFace; &nbsp; //CylindricalFace face = obj as CylindricalFace; &nbsp; &nbsp; XYZ p = r.GlobalPoint; &nbsp; XYZ v = face.Normal.CrossProduct( XYZ.BasisZ ); &nbsp; if( v.IsZeroLength() ) &nbsp; { &nbsp; &nbsp; v = face.Normal.CrossProduct( XYZ.BasisX ); &nbsp; } &nbsp; doc.Create.NewFamilyInstance( r, p, v, symbol );
```

```csharp
&nbsp; if( obj is PlanarFace ) &nbsp; { &nbsp; &nbsp; PlanarFace planarFace = obj as PlanarFace; &nbsp; &nbsp; &nbsp; // Handle planar face case ... &nbsp; } &nbsp; else if( obj is CylindricalFace ) &nbsp; { &nbsp; &nbsp; CylindricalFace cylindricalFace = obj &nbsp; &nbsp; &nbsp; as CylindricalFace; &nbsp; &nbsp; &nbsp; // Handle cylindrical face case ... &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Place an instance of the given family symbol &nbsp; /// on a selected face of an existing 3D element. &nbsp; /// &lt;/summary&gt; &nbsp; FamilyInstance PlaceFamilyInstanceOnFace( &nbsp; &nbsp; UIDocument uidoc, &nbsp; &nbsp; FamilySymbol symbol ) &nbsp; { &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; Reference r = uidoc.Selection.PickObject( &nbsp; &nbsp; &nbsp; ObjectType.Face, &quot;Please pick a point on &quot; &nbsp; &nbsp; &nbsp; + &quot; a face for family instance insertion&quot;); &nbsp; &nbsp; &nbsp; Element e = doc.GetElement( r.ElementId ); &nbsp; &nbsp; &nbsp; GeometryObject obj &nbsp; &nbsp; &nbsp; = e.GetGeometryObjectFromReference( r ); &nbsp; &nbsp; &nbsp; XYZ p = r.GlobalPoint; &nbsp; &nbsp; &nbsp; // Better than specialised individual handlers &nbsp; &nbsp; // for each specific case, handle the general &nbsp; &nbsp; // case in a generic fashion. &nbsp; &nbsp; &nbsp; Face face = obj as Face; &nbsp; &nbsp; IntersectionResult ir = face.Project( p ); &nbsp; &nbsp; UV q = ir.UVPoint; &nbsp; &nbsp; Transform t = face.ComputeDerivatives( q ); &nbsp; &nbsp; XYZ v = t.BasisX; // or BasisY, or whatever... &nbsp; &nbsp; &nbsp; return doc.Create.NewFamilyInstance(r, p, v, symbol); &nbsp; }
```

```csharp
&nbsp; Reference r = uidoc.Selection.PickObject( &nbsp; &nbsp; ObjectType.Face, &quot;Please pick a point on &quot; &nbsp; &nbsp; + &quot; a face for family instance insertion&quot; ); &nbsp; &nbsp; Element e = doc.GetElement( r.ElementId ); &nbsp; &nbsp; GeometryObject obj &nbsp; &nbsp; = e.GetGeometryObjectFromReference( r ); &nbsp; &nbsp; Face face = obj as Face; &nbsp; UV q = r.UVPoint; &nbsp; &nbsp; Transform t = face.ComputeDerivatives( q ); &nbsp; XYZ v = t.BasisX; // or BasisY, or whatever... &nbsp; &nbsp; return doc.Create.NewFamilyInstance( r, p, v, symbol );
```
