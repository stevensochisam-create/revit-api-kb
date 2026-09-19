---
num: 671
date: 2011-11-07
themes: [Geometry]
tags: [revit-api, tbc]
---

# Planar Face Transform

<https://jeremytammik.github.io/tbc/a/0671_planar_face_transform.htm>

```csharp
&nbsp; Public Function Execute( _ &nbsp; &nbsp; ByVal commandData As ExternalCommandData, _ &nbsp; &nbsp; ByRef message As String, _ &nbsp; &nbsp; ByVal elements As ElementSet) As Result Implements IExternalCommand.Execute &nbsp; &nbsp; &nbsp; Dim uiapp As UIApplication = commandData.Application &nbsp; &nbsp; Dim app As Application = uiapp.Application &nbsp; &nbsp; Dim uidoc As UIDocument = uiapp.ActiveUIDocument &nbsp; &nbsp; Dim doc As Document = uidoc.Document &nbsp; &nbsp; Dim sel As Selection = uidoc.Selection &nbsp; &nbsp; &nbsp; Try &nbsp; &nbsp; &nbsp; Dim ref As Reference = sel.PickObject( _ &nbsp; &nbsp; &nbsp; &nbsp; ObjectType.Face, &quot;Select a face&quot;) &nbsp; &nbsp; &nbsp; &nbsp; Dim elem As Element = doc.GetElement(ref) &nbsp; &nbsp; &nbsp; &nbsp; Dim gObj As GeometryObject _ &nbsp; &nbsp; &nbsp; &nbsp; = elem.GetGeometryObjectFromReference(ref) &nbsp; &nbsp; &nbsp; &nbsp; Dim face As PlanarFace = TryCast(gObj, PlanarFace) &nbsp; &nbsp; &nbsp; &nbsp; If face Is Nothing Then &nbsp; &nbsp; &nbsp; &nbsp; MsgBox(&quot;Not a planar face&quot;) &nbsp; &nbsp; &nbsp; End If &nbsp; &nbsp; &nbsp; &nbsp; Dim v As ViewDrafting = Nothing &nbsp; &nbsp; &nbsp; &nbsp; Dim tr As New Transaction(doc, &quot;Draw Face&quot;) &nbsp; &nbsp; &nbsp; tr.Start() &nbsp; &nbsp; &nbsp; &nbsp; Try &nbsp; &nbsp; &nbsp; &nbsp; v = doc.Create.NewViewDrafting 'create a new view &nbsp; &nbsp; &nbsp; &nbsp; v.Scale = 48 '1/4&quot; = 1'-0&quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 'this transform re-orients the global &nbsp; &nbsp; &nbsp; &nbsp; 'coordinate system to the face's coordinate system &nbsp; &nbsp; &nbsp; &nbsp; Dim trans As Transform _ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = Util.PlanarFaceTransform(face) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; For Each eArr As EdgeArray In face.EdgeLoops &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; For Each e As Edge In eArr &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Dim c As Curve = e.AsCurveFollowingFace(face) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; c = c.Transformed(trans) 'orient the curve on the XY plane &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; doc.Create.NewDetailCurve(v, c) 'draw the curve &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Next &nbsp; &nbsp; &nbsp; &nbsp; Next &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; tr.Commit() &nbsp; &nbsp; &nbsp; Catch ex As Exception &nbsp; &nbsp; &nbsp; &nbsp; tr.RollBack() &nbsp; &nbsp; &nbsp; &nbsp; MsgBox(&quot;Error: &
```
