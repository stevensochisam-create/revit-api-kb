---
type: BRepBuilder
namespace: Autodesk.Revit.DB
version: 2024
members: 21
tags: [revit-api, class]
---

# BRepBuilder

`Autodesk.Revit.DB.BRepBuilder` · Revit 2024 · 21 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | BRepBuilder | 2016 | `public BRepBuilder ( BRepType geomType )` |
| Method | AddCoEdge | 2016 | `public BRepBuilderGeometryId AddCoEdge ( BRepBuilderGeometryId loopId , BRepBuilderGeometryId edgeId , bool bCoEdgeIsReversed )` |
| Method | AddEdge | 2016 | `public BRepBuilderGeometryId AddEdge ( BRepBuilderEdgeGeometry edgeGeom )` |
| Method | AddFace | 2016 | `public BRepBuilderGeometryId AddFace ( BRepBuilderSurfaceGeometry surfaceGeom , bool bFaceIsReversed )` |
| Method | AddLoop | 2016 | `public BRepBuilderGeometryId AddLoop ( BRepBuilderGeometryId faceId )` |
| Method | AllowRemovalOfProblematicFaces | 2017_subscription_update | `public void AllowRemovalOfProblematicFaces ()` |
| Method | CanAddGeometry | 2016 | `public bool CanAddGeometry ()` |
| Method | Finish | 2016 | `public BRepBuilderOutcome Finish ()` |
| Method | FinishFace | 2016 | `public void FinishFace ( BRepBuilderGeometryId faceId )` |
| Method | FinishLoop | 2016 | `public void FinishLoop ( BRepBuilderGeometryId loopId )` |
| Method | GetResult | — | `` |
| Method | GetResult | 2016 | `public Solid GetResult ()` |
| Method | IsPermittedSurfaceType | 2016 | `public static bool IsPermittedSurfaceType ( Surface surface )` |
| Method | IsResultAvailable | 2016 | `public bool IsResultAvailable ()` |
| Method | IsValidEdgeId | 2016 | `public bool IsValidEdgeId ( BRepBuilderGeometryId edgeId )` |
| Method | IsValidFaceId | 2016 | `public bool IsValidFaceId ( BRepBuilderGeometryId faceId )` |
| Method | IsValidLoopId | 2016 | `public bool IsValidLoopId ( BRepBuilderGeometryId loopId )` |
| Method | IsValidPersistentIdsMap | 2016 | `public bool IsValidPersistentIdsMap ( BRepBuilderPersistentIds brepPersistentIds )` |
| Method | RemovedSomeFaces | 2017_subscription_update | `public bool RemovedSomeFaces ()` |
| Method | SetAllowShortEdges | 2017_subscription_update | `public void SetAllowShortEdges ()` |
| Method | SetFaceMaterialId | 2016 | `public void SetFaceMaterialId ( BRepBuilderGeometryId faceId , ElementId materialId )` |