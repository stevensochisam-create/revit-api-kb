---
type: Form
namespace: Autodesk.Revit.DB
version: 2024
members: 41
tags: [revit-api, class]
---

# Form

`Autodesk.Revit.DB.Form` · Revit 2024 · 41 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddEdge | — | `` |
| Method | AddProfile | — | `public int AddProfile ( Reference edgeReference , double param )` |
| Method | CanManipulateProfile | — | `public bool CanManipulateProfile ( int profileIndex )` |
| Method | CanManipulateSubElement | — | `public bool CanManipulateSubElement ( Reference subElementReference )` |
| Method | ConstrainProfiles | — | `public void ConstrainProfiles ( int primaryProfileIndex )` |
| Method | DeleteProfile | — | `public void DeleteProfile ( int profileIndex )` |
| Method | DeleteSubElement | — | `public void DeleteSubElement ( Reference subElementReference )` |
| Method | GetControlPoints | — | `public ReferenceArray GetControlPoints ( Reference curveOrEdgeOrFaceReference )` |
| Method | GetCurvesAndEdgesReference | — | `public ReferenceArray GetCurvesAndEdgesReference ( Reference pointReference )` |
| Method | GetPathCurveIndexByCurveReference | — | `public int GetPathCurveIndexByCurveReference ( Reference curveReference )` |
| Method | GetProfileAndCurveLoopIndexFromReference | — | `public void GetProfileAndCurveLoopIndexFromReference ( Reference curveOrEdgeReference , ref int profileIndex , ref int curveLoopIndex )` |
| Method | IsAutoCreaseEdge | — | `public bool IsAutoCreaseEdge ( Reference edgeReference )` |
| Method | IsBeginningFace | — | `public bool IsBeginningFace ( Reference faceReference )` |
| Method | IsConnectingEdge | — | `public bool IsConnectingEdge ( Reference edgeReference )` |
| Method | IsCurveReference | — | `public bool IsCurveReference ( Reference curveReference )` |
| Method | IsEdgeReference | — | `public bool IsEdgeReference ( Reference edgeReference )` |
| Method | IsEndFace | — | `public bool IsEndFace ( Reference faceReference )` |
| Method | IsFaceReference | — | `public bool IsFaceReference ( Reference faceReference )` |
| Method | IsProfileEdge | — | `public bool IsProfileEdge ( Reference curveOrEdgeReference )` |
| Method | IsReferenceOnlyProfile | — | `public bool IsReferenceOnlyProfile ( int profileIndex )` |
| Method | IsSideFace | — | `public bool IsSideFace ( Reference faceReference )` |
| Method | IsVertexReference | — | `public bool IsVertexReference ( Reference vertexReference )` |
| Method | MoveProfile | — | `public void MoveProfile ( int profileIndex , XYZ offset )` |
| Method | MoveSubElement | — | `public void MoveSubElement ( Reference subElementReference , XYZ offset )` |
| Method | Rehost | — | `` |
| Method | RotateProfile | — | `public void RotateProfile ( int profileIndex , Line axis , double angle )` |
| Method | RotateSubElement | — | `public void RotateSubElement ( Reference subElementReference , Line axis , double angle )` |
| Method | ScaleProfile | — | `public void ScaleProfile ( int profileIndex , double factor , XYZ origin )` |
| Method | ScaleSubElement | — | `public void ScaleSubElement ( Reference subElementReference , double factor , XYZ origin )` |
| Property | AreProfilesConstrained | — | `public bool AreProfilesConstrained { get ; set ; }` |
| Property | BaseOffset | — | `public double BaseOffset { get ; set ; }` |
| Property | CurveLoopReferencesOnProfile | — | `public ReferenceArray this [ int profileIndex , int curveLoopIndex ] { get ; }` |
| Property | HasOneOrMoreReferenceProfiles | — | `public bool HasOneOrMoreReferenceProfiles { get ; }` |
| Property | HasOpenGeometry | — | `public bool HasOpenGeometry { get ; }` |
| Property | IsInXRayMode | — | `public bool IsInXRayMode { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | PathCurveCount | — | `public int PathCurveCount { get ; }` |
| Property | PathCurveReference | — | `public Reference this [ int curveIndex ] { get ; }` |
| Property | ProfileCount | — | `public int ProfileCount { get ; }` |
| Property | ProfileCurveLoopCount | — | `public int this [ int index ] { get ; }` |
| Property | TopOffset | — | `public double TopOffset { get ; set ; }` |