---
type: PartMakerMethodToDivideVolumes
namespace: Autodesk.Revit.DB
version: 2024
members: 25
tags: [revit-api, class]
---

# PartMakerMethodToDivideVolumes

`Autodesk.Revit.DB.PartMakerMethodToDivideVolumes` · Revit 2024 · 25 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddIntersectingReference | 2013 | `public bool AddIntersectingReference ( ElementId intersectingReference , double offset )` |
| Method | AreElementsValidIntersectingReferences | — | `` |
| Method | CanBeDivisionProfile | — | `` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetOffsetForIntersectingReference | 2013 | `public double GetOffsetForIntersectingReference ( ElementId intersectingReference )` |
| Method | GetPlaneOfSketch | 2013 | `public Plane GetPlaneOfSketch ()` |
| Method | GetSketchCurves | 2013 | `public void GetSketchCurves ( out IList < Curve > curveArray )` |
| Method | GetSplitRefsOffsets | 2013 | `public IDictionary < ElementId , double > GetSplitRefsOffsets ()` |
| Method | IsElementValidIntersectingReference | — | `` |
| Method | IsValidSketchPlane | 2013 | `public static bool IsValidSketchPlane ( Document document , ElementId sketchPlaneId )` |
| Method | RemoveIntersectingReference | 2013 | `public bool RemoveIntersectingReference ( ElementId intersectingReference )` |
| Method | SetOffsetForIntersectingReference | 2013 | `public void SetOffsetForIntersectingReference ( ElementId intersectingReference , double offset )` |
| Method | UsesReference | 2013 | `public bool UsesReference ( ElementId intersectingReference )` |
| Property | DivisionGap | 2013 | `public double DivisionGap { get ; set ; }` |
| Property | DivisionPatternMirror | 2013 | `public bool DivisionPatternMirror { get ; set ; }` |
| Property | DivisionRotationAngle | 2013 | `public double DivisionRotationAngle { get ; set ; }` |
| Property | DivisionRuleId | 2013 | `public ElementId DivisionRuleId { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | ProfileFlipAcross | 2013 | `public bool ProfileFlipAcross { get ; set ; }` |
| Property | ProfileFlipAlong | 2013 | `public bool ProfileFlipAlong { get ; set ; }` |
| Property | ProfileMatch | 2013 | `public PartEdgeConditionOrientation ProfileMatch { get ; set ; }` |
| Property | ProfileOffset | 2013 | `public double ProfileOffset { get ; set ; }` |
| Property | ProfileType | 2013 | `public ElementId ProfileType { get ; set ; }` |
| Property | UConstDivisionIndent | 2013 | `public int UConstDivisionIndent { get ; set ; }` |
| Property | VConstDivisionIndent | 2013 | `public int VConstDivisionIndent { get ; set ; }` |