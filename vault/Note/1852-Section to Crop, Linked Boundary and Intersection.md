---
num: 1852
date: 2020-06-25
themes: [Geometry, LinkedModel]
tags: [revit-api, tbc]
---

# Section to Crop, Linked Boundary and Intersection

<https://jeremytammik.github.io/tbc/a/1852_sect_box_2_view_crop.html>

```csharp
Private Function TObj75(ByVal commandData As Autodesk.Revit.UI.ExternalCommandData, ByRef message As String, ByVal elements As Autodesk.Revit.DB.ElementSet) As Result If commandData.Application.ActiveUIDocument Is Nothing Then Return Result.Cancelled Else Dim UIDoc As UIDocument = commandData.Application.ActiveUIDocument Dim Doc As Document = UIDoc.Document Dim R As Reference = Nothing Try R = UIDoc.Selection.PickObject(Selection.ObjectType.Element, "Pick a room any room.") Catch ex As Exception End Try If R Is Nothing Then Return Result.Cancelled Else Dim Room As Room = TryCast(Doc.GetElement(R), Room) If Room Is Nothing Then Return Result.Cancelled Else Dim GeomEl As GeometryElement = Room.ClosedShell Dim S As Solid = GeomEl(0) 'Assume single solid for brevity Dim FEClnk As New FilteredElementCollector(Doc) Dim ECFlnk As New ElementClassFilter(GetType(RevitLinkInstance)) Dim Lnk As List(Of RevitLinkInstance) = FEClnk.WherePasses(ECFlnk).ToElements.Cast(Of RevitLinkInstance).ToList Dim LinkDoc As Document = Lnk(0).GetLinkDocument() 'Assume single link containing columns for brevity Dim SolTransformed As Solid = SolidUtils.CreateTransformed(S, Lnk(0).GetTransform.Inverse) 'The solid in the coord system of the link Dim ElintS As New ElementIntersectsSolidFilter(SolTransformed) Dim ECF As New ElementCategoryFilter(BuiltInCategory.OST_StructuralColumns) Dim LandF As New LogicalAndFilter(ElintS, ECF) Dim FEC As New FilteredElementCollector(LinkDoc) Dim Els As List(Of ElementId) = FEC.WherePasses(LandF).ToElementIds Using tx As New Transaction(Doc, "Copy") If tx.Start = TransactionStatus.Started Then Dim NewIDs As List(Of ElementId) = ElementTransformUtils.CopyElements(LinkDoc, Els, Doc, Lnk(0).GetTransform, Nothing) Dim Ops As New SpatialElementBoundaryOptions() With {.SpatialElementBoundaryLocation = SpatialElementBoundaryLocation.Finish} Dim BoundSegs As IList(Of IList(Of BoundarySegment)) = Room.GetBoundarySegments(Ops) For i = 0 To BoundSegs.Count - 1 Dim SegLst As IList(Of BoundarySegment) = BoundSegs(i) Debug.WriteLine("List: " & CStr(i + 1)) 'List 0' just doesn't sound right For ix = 0 To SegLst.Count - 1 Dim Seg As BoundarySegment = SegLst(ix) If NewIDs.Contains(Seg.ElementId) = False Then Continue For Else Debug.WriteLine(CStr(Seg.ElementId.IntegerValue) & ", " & (Seg.GetCurve.Length * 304.8).ToString("F1")) 'Tried below to see what .LinkedElementId rep
```

```csharp
List: 1 427532, 400.0 427532, 750.0 427532, 400.0 427536, 275.0 427536, 200.0 427534, 200.0 427534, 750.0 427534, 200.0
```
