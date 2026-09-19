---
num: 1985
date: 2023-03-14
themes: [Geometry]
tags: [revit-api, tbc]
---

# IFC, Dimension and Reference Intersector with Links

<https://jeremytammik.github.io/tbc/a/1985_refinters_link.html>

```csharp
Private Function Obj_230305a(ByVal commandData As Autodesk.Revit.UI.ExternalCommandData, ByRef message As String, ByVal elements As Autodesk.Revit.DB.ElementSet) As Result Dim UIApp As UIApplication = commandData.Application Dim UIDoc As UIDocument = commandData.Application.ActiveUIDocument If UIDoc Is Nothing Then Return Result.Cancelled Else Dim IntDoc As Document = UIDoc.Document Dim FEC As New FilteredElementCollector(IntDoc) Dim RvtLnks As List(Of RevitLinkInstance) = FEC.OfClass(GetType(RevitLinkInstance)).OfType(Of RevitLinkInstance).ToList Dim BBOrds As XYZ() = New XYZ(1) {New XYZ(-11.3, 10, -1), New XYZ(2.3, 31.9, 0.1)} Dim EFs As ElementFilter() = New ElementFilter(RvtLnks.Count - 1) {} For i = 0 To RvtLnks.Count - 1 Dim RInst As RevitLinkInstance = RvtLnks(i) Dim Tinv As Transform = RInst.GetTransform.Inverse Dim Min As XYZ = Tinv.OfPoint(BBOrds(0)) Dim Max As XYZ = Tinv.OfPoint(BBOrds(1)) Dim OL As New Outline(Min, Max) EFs(i) = New BoundingBoxIsInsideFilter(OL) Next Dim LorF As New LogicalOrFilter(EFs.ToList) Dim V3D As View3D = TryCast(UIDoc.ActiveGraphicalView, View3D) If V3D Is Nothing Then Return Result.Cancelled Else Dim REFInt As New ReferenceIntersector(LorF, FindReferenceTarget.Element, V3D) With {.FindReferencesInRevitLinks = True} Dim R As Reference = Nothing Try R = UIDoc.Selection.PickObject(Selection.ObjectType.Element, "Pick ray line") Catch ex As Exception Return Result.Cancelled End Try Dim CE As CurveElement = TryCast(IntDoc.GetElement(R), CurveElement) If CE Is Nothing Then Return Result.Cancelled Else Dim LN As Line = TryCast(CE.GeometryCurve, Line) If LN Is Nothing Then Return Result.Cancelled Else Dim Res As List(Of ReferenceWithContext) = REFInt.Find(LN.GetEndPoint(0), LN.Direction) For i = 0 To Res.Count - 1 Dim RwC As ReferenceWithContext = Res(i) Dim Rf As Reference = RwC.GetReference Debug.WriteLine($"{Rf.ElementId.IntegerValue}, {Rf.LinkedElementId?.IntegerValue}, {RwC.Proximity}") Next Return Result.Succeeded End Function
```

```csharp
432129, 432128, 6.68864267244516 432129, 432128, 3.38973099408717 432129, 432168, 13.2864660291611 432129, 432168, 9.98755435080315 432142, 432128, 17.9884761277055 432142, 432128, 14.6895644493475 432142, 432168, 24.5862994844214 432142, 432168, 21.2873878060635
```

```csharp
BB1.Min/Max = (-12.4839, -8.3542, 0) , (-5.0602, -0.9306, 9.8425) BB2.Min/Max = (-11.4847, -12.3077, 0) , (-6.0974, -10.8641, 9.8425) Ray = XYZ.BasisX Origin = BB1.Min with Z+3
```

```csharp
FindReferencesInRevitLinks = True, FindReferenceTarget.Element 309836, 309843, REFERENCE_TYPE_SURFACE, 3.76375750430962 (Linked wall near face) 309836, 309843, REFERENCE_TYPE_SURFACE, 4.71520107386343 (Linked wall far face) 310123, -1, REFERENCE_TYPE_SURFACE, 2.84087372715355 (Wall far face) 310123, -1, REFERENCE_TYPE_SURFACE, 1.39730417334777 (Wall near face) 310123, -1, REFERENCE_TYPE_NONE, 1.39730417334777 (Wall element) 'FindReferencesInRevitLinks = False, FindReferenceTarget.Element 310123, -1, REFERENCE_TYPE_NONE, 1.39730417334777 (Wall element) 'FindReferencesInRevitLinks = False, FindReferenceTarget.All 310123, -1, REFERENCE_TYPE_SURFACE, 2.84087372715355 (Wall far face) 310123, -1, REFERENCE_TYPE_SURFACE, 1.39730417334777 (Wall near face) 310123, -1, REFERENCE_TYPE_NONE, 1.39730417334777 (Wall element)
```
