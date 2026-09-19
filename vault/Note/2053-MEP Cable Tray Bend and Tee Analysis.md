---
num: 2053
date: 2024-09-12
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# MEP Cable Tray Bend and Tee Analysis

<https://jeremytammik.github.io/tbc/a/2053_cable_tray_bend.html>

```csharp
pair_sys_origin = [[con.CoordinateSystem, con.Origin] for con in conSet] pta = pair_sys_origin[0][1].ToPoint() ptb = pair_sys_origin[1][1].ToPoint() vector = pair_sys_origin[0][0].BasisZ.Negate().ToVector() arc = DS.Arc.ByStartPointEndPointStartTangent(pta, ptb, vector) return arc, arc.Length
```

```csharp
// méthode à partir de deux connecteurs if (connectors.Size == 2) { // Transforme le Set en liste var castConnectors = connectors.Cast&lt;Connector&gt;(); List&lt;Connector&gt; connectorList = castConnectors.ToList(); // get first point Transform transformPtA = connectorList[0].CoordinateSystem; XYZ originPtA = transformPtA.Origin; // get Vector from this point XYZ vector = transformPtA.BasisZ.Negate(); // get second point Transform transformPtB = connectorList[1].CoordinateSystem; XYZ originPtB = transformPtB.Origin; // Get arc from those points Arc arc = Arc.Create(originPtA, originPtB, vector); length = arc.Length; }
```

```csharp
// assuming you already have the two connectors. // we get the curves lines from its owner. var horizontalLine = ((LocationCurve)connectorA.Owner.Location).Curve as Line; var verticalLine = ((LocationCurve)connectorB.Owner.Location).Curve as Line; // catch the distance and location of the 2 connectors and the distance between var originA = connectorA.Origin; var originB = connectorB.Origin; var diagonalDistance = originA.DistanceTo(originB); // get the sketchplan used to draw such cable trays var sketchPlan = SketchPlane.Create(Doc, ((MEPCurve)connectorA.Owner).ReferenceLevel.Id).GetPlane(); // now we need draw a perpendicular line to any of the mep curves. var perDirection = horizontalLine.Direction.CrossProduct(sketchPlan.Normal); var perpL1 = Line.CreateBound(originA - perDirection * diagonalDistance, originA + perDirection * diagonalDistance); // then project the second point over this perpendicular curve to get the center point var centerPoint = perpL1.Project(originB).XYZPoint; // arc requires 2 angles start and end double angleX = sketchPlan.XVec.AngleTo((originA - centerPoint).Normalize()); double angleY = sketchPlan.XVec.AngleTo((originB - centerPoint).Normalize()); // draw the arc
```

```csharp
//Transforme le Set en liste var castConnectors = connectors.Cast&lt;Connector&gt;(); List&lt;Connector&gt; connectorList = castConnectors.ToList(); Connector connectorA = connectorList[0]; Connector connectorB = connectorList[1]; #region connectorA_Perpendicular //get Transform Transform transformPtA = connectorA.CoordinateSystem; //get origin XYZ originPtA = transformPtA.Origin; //get direction XYZ directionA = (connectorA.Owner.Location as LocationPoint).Point; //set line between origin and direction of owner Line lineA = Line.CreateBound(originPtA, directionA); //get perpendicular XYZ normalA = lineA.Direction.Normalize(); XYZ dirA = new XYZ(0, 0, 1); XYZ crossA = normalA.CrossProduct(dirA); XYZ endA = originPtA + crossA.Multiply(4); XYZ endAMirror = originPtA + crossA.Multiply(-4); Line linePerpendicularA = Line.CreateBound(endA, endAMirror); #endregion #region connectorB_Perpendicular //get Transform Transform transformPtB = connectorB.CoordinateSystem; //get origin XYZ originPtB = transformPtB.Origin; //get direction XYZ directionB = (connectorB.Owner.Location as LocationPoint).Point; //set line between origin and direction of owner Line lineB = Line.CreateBound(originPtB, directionB); //get perpendicular XYZ normalB = lineB.Direction.Normalize(); XYZ dirB = new XYZ(0, 0, 1); XYZ crossB = normalB.CrossProduct(dirB); XYZ endB = originPtB + crossB.Multiply(4); XYZ endBMirror = originPtB + crossB.Multiply(-4); Line linePerpendicularB = Line.CreateBound(endB, endBMirror); #endregion //get intersection between perpendiculars XYZ centerOfArc = null; IntersectionResultArray intersectionResults = new IntersectionResultArray(); SetComparisonResult setCR = linePerpendicularA.Intersect(linePerpendicularB, out intersectionResults); if (setCR == SetComparisonResult.Overlap) { if (intersectionResults != null && intersectionResults.Size == 1) { //there is one point interesction IntersectionResult iResult = intersectionResults.get_Item(0); centerOfArc = iResult.XYZPoint; _geometries.Add(Point.Create(centerOfArc)); } } if (centerOfArc != null) { //Set arc from point A and B double radius = centerOfArc.DistanceTo(originPtA); XYZ xAxis = new XYZ(1, 0, 0); // The x axis to define the arc plane. Must be normalized XYZ yAxis = new XYZ(0, 1, 0); // The y axis to define the arc plane. Must be normalized Arc arc = Arc.Create(centerOfArc, radius, 0, Math.PI / 2.0, xAxis, yAxis
```

```csharp
ElementId id = uidoc.Selection.PickObject( Autodesk.Revit.UI.Selection.ObjectType.Element).ElementId; FamilyInstance inst = doc.GetElement(id) as FamilyInstance; Options opt = new Options(); opt.ComputeReferences = true; opt.DetailLevel = ViewDetailLevel.Coarse; GeometryElement geoElement = inst.get_Geometry(opt); using (Transaction createArc = new Transaction(doc, "Create Arc")) { createArc.Start(); foreach (GeometryInstance geoInst in geoElement) { if(geoInst != null) { foreach (GeometryObject obj in geoInst.GetInstanceGeometry()) { if (obj is Arc) { doc.Create.NewModelCurve(obj as Curve, SketchPlane.Create( doc, Plane.CreateByNormalAndOrigin((obj as Arc).Normal, (obj as Arc).GetEndPoint(0)))); } } } } createArc.Commit(); }
```
