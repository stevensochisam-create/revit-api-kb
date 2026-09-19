---
type: Toposolid
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# Toposolid

`Autodesk.Revit.DB.Toposolid` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | CreateFromTopographySurface | 2024 | `public static Toposolid CreateFromTopographySurface ( Document document , ElementId hostSurfaceId , ElementId topoTypeId , ElementId levelId )` |
| Method | CreateSubDivision | 2024 | `public Toposolid CreateSubDivision ( Document document , IList < CurveLoop > profiles )` |
| Method | GetSlabShapeEditor | 2024 | `public SlabShapeEditor GetSlabShapeEditor ()` |
| Method | GetSubDivisionIds | 2024 | `public IList < ElementId > GetSubDivisionIds ()` |
| Method | Simplify | 2024 | `public void Simplify ( double percentage )` |
| Method | Split | 2024 | `public IList < ElementId > Split ( IList < CurveLoop > splitCurveLoops )` |
| Property | HostTopoId | 2024 | `public ElementId HostTopoId { get ; }` |
| Property | Parameter | — | `` |
| Property | SketchId | 2024 | `public ElementId SketchId { get ; }` |