---
num: 1573
date: 2017-06-30
themes: [Geometry]
tags: [revit-api, tbc]
---

# Picked Instance Face Geometry in LCS Versus WCS

<https://jeremytammik.github.io/tbc/a/1573_family_inst_lcs_wcs.html>

```csharp
Instance = Doc.Create.NewFamilyInstance( line, FamilySymbol, Level, StructuralType.Beam)
```

```csharp
Reference&nbsp;refFace&nbsp;=&nbsp;null; while(&nbsp;true&nbsp;) { &nbsp;&nbsp;try &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;refFace&nbsp;=&nbsp;sel.PickObject(&nbsp;ObjectType.Face, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;select&nbsp;a&nbsp;face&quot;&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;Element&nbsp;selectedElement&nbsp;=&nbsp;doc.GetElement( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;refFace&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;GeometryObject&nbsp;selectedGeoObject&nbsp;=&nbsp;selectedElement &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.GetGeometryObjectFromReference(&nbsp;refFace&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;Face&nbsp;selectedFace&nbsp;=&nbsp;selectedGeoObject&nbsp;as&nbsp;Face; &nbsp;&nbsp;&nbsp;&nbsp;PlanarFace&nbsp;selectedPlanarFace&nbsp;=&nbsp;selectedFace&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as&nbsp;PlanarFace; &nbsp;&nbsp;&nbsp;&nbsp;BoundingBoxUV&nbsp;box&nbsp;=&nbsp;selectedFace.GetBoundingBox(); &nbsp;&nbsp;&nbsp;&nbsp;UV&nbsp;faceCenter&nbsp;=&nbsp;(&nbsp;box.Max&nbsp;+&nbsp;box.Min&nbsp;)&nbsp;/&nbsp;2; &nbsp;&nbsp;&nbsp;&nbsp;XYZ&nbsp;computedFaceNormal&nbsp;=&nbsp;selectedFace &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.ComputeNormal(&nbsp;faceCenter&nbsp;).Normalize(); &nbsp;&nbsp;&nbsp;&nbsp;XYZ&nbsp;faceNormal&nbsp;=&nbsp;selectedPlanarFace.FaceNormal; &nbsp;&nbsp;&nbsp;&nbsp;MessageBox.Show(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$&quot;computedFaceNormal:&nbsp;{computedFaceNormal.ToString()},&nbsp;&quot; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+&nbsp;&quot;faceNormal:&nbsp;{faceNormal.ToString()}&quot;&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;catch(&nbsp;Autodesk.Revit.Exceptions.OperationCanceledException&nbsp;e&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;Result.Cancelled; &nbsp;&nbsp;} }
```

```csharp
MessageBox.Show( &nbsp;&nbsp;$&quot;computedFaceNormal:&nbsp;{computedFaceNormal.ToString()},&nbsp;&quot; &nbsp;&nbsp;+&nbsp;&quot;faceNormal:&nbsp;{faceNormal.ToString()},&nbsp;&quot; &nbsp;&nbsp;+&nbsp;&quot;&nbsp;Area:&nbsp;{selectedFace.Area.ToString()}&quot;&nbsp;);
```

```csharp
refFace.ConvertToStableRepresentation(&nbsp;doc&nbsp;) &nbsp;&nbsp;.Contains(&nbsp;&quot;INSTANCE&quot;&nbsp;)
```

```csharp
if(&nbsp;refFace.ConvertToStableRepresentation(&nbsp;doc&nbsp;) &nbsp;&nbsp;.Contains(&nbsp;&quot;INSTANCE&quot;&nbsp;)&nbsp;) { &nbsp;&nbsp;Transform&nbsp;trans&nbsp;=&nbsp;(&nbsp;selectedElement&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;as&nbsp;FamilyInstance&nbsp;).GetTransform(); &nbsp;&nbsp;computedFaceNormal&nbsp;=&nbsp;trans.OfVector(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;computedFaceNormal&nbsp;); &nbsp;&nbsp;faceNormal&nbsp;=&nbsp;trans.OfVector(&nbsp;faceNormal&nbsp;); }
```
