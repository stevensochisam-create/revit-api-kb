---
num: 2056
date: 2024-10-02
themes: [Geometry]
tags: [revit-api, tbc]
---

# Join Beams and Solid from Face

<https://jeremytammik.github.io/tbc/a/2056_solid_from_face.html>

```csharp
using Autodesk.Revit.Attributes; using Autodesk.Revit.DB; using Autodesk.Revit.UI; using System; namespace RevitAddin.Forum.Revit.Commands { [Transaction(TransactionMode.Manual)] public class CommandFaceToSolid : IExternalCommand { public Result Execute( ExternalCommandData commandData, ref string message, ElementSet elementSet) { UIApplication uiapp = commandData.Application; Document document = uiapp.ActiveUIDocument.Document; try { var faceReference = uiapp.ActiveUIDocument.Selection.PickObject( Autodesk.Revit.UI.Selection.ObjectType.Face); var element = document.GetElement(faceReference); var face = element.GetGeometryObjectFromReference(faceReference) as Face; var solid = CreateSolidFromFace(face); var normal = face.ComputeNormal(new UV(0.5, 0.5)); using (Transaction transaction = new Transaction(document)) { transaction.Start("Create Solid"); var ds = DirectShape.CreateElement(document, new ElementId(BuiltInCategory.OST_GenericModel)); ds.SetName(ds.Category.Name); ds.SetShape(new[] { solid }); ds.Location.Move(normal); transaction.Commit(); } } catch (Exception ex) { Console.WriteLine(ex); } return Result.Succeeded; } private Solid CreateSolidFromFace(Face face) { var surface = face.GetSurface(); var brepBuilder = new BRepBuilder(BRepType.OpenShell); var faceIsReversed = !face.OrientationMatchesSurfaceOrientation; BRepBuilderGeometryId faceId = brepBuilder.AddFace( BRepBuilderSurfaceGeometry.Create(surface, null), faceIsReversed); foreach (CurveLoop curveLoop in face.GetEdgesAsCurveLoops()) { BRepBuilderGeometryId loopId = brepBuilder.AddLoop(faceId); foreach (Curve curve in curveLoop) { var edge = BRepBuilderEdgeGeometry.Create(curve); BRepBuilderGeometryId edgeId = brepBuilder.AddEdge(edge); brepBuilder.AddCoEdge(loopId, edgeId, false); } brepBuilder.FinishLoop(loopId); } brepBuilder.SetFaceMaterialId(faceId, face.MaterialElementId); brepBuilder.FinishFace(faceId); brepBuilder.Finish(); return brepBuilder.GetResult(); } } }
```

```csharp
private void JoinGeometryBeam1ToBeam2Beam3( Document activeDoc, FamilyInstance Beam1) { XYZ minPt = primaryBeam.get_BoundingBox(activeDoc.ActiveView).Min; XYZ maxPt = primaryBeam.get_BoundingBox(activeDoc.ActiveView).Max; Outline outLine = new Outline(minPt, maxPt); outLine.Scale(1.5); BoundingBoxIntersectsFilter filter = new BoundingBoxIntersectsFilter(outLine); List&lt;FamilyInstance&gt; connectedBeams = new FilteredElementCollector(activeDoc) .WherePasses(filter) .OfCategory(BuiltInCategory.OST_StructuralFraming) .OfClass(typeof(FamilyInstance)) .Cast&lt;FamilyInstance&gt;() .ToList(); foreach (FamilyInstance beam in connectedBeams) { JoinGeometryUtils.JoinGeometry(this.ActiveDoc, beam, Beam1); } }
```

```csharp
StructuralFramingUtils.DisallowJoinAtEnd(girderInstance, 0);
```
