---
type: PointOnPlane
namespace: Autodesk.Revit.DB
version: 2024
members: 7
tags: [revit-api, class]
---

# PointOnPlane

`Autodesk.Revit.DB.PointOnPlane` · Revit 2024 · 7 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetPlaneReference | — | `public Reference GetPlaneReference ()` |
| Method | IsValidPlaneReference | — | `public static bool IsValidPlaneReference ( Document doc , Reference planeReference )` |
| Method | NewPointOnPlane | — | `public static PointOnPlane NewPointOnPlane ( Document doc , Reference planeReference , XYZ position , XYZ xvec )` |
| Method | SetPlaneReference | — | `public void SetPlaneReference ( Reference planeReference )` |
| Property | Offset | — | `public double Offset { get ; set ; }` |
| Property | Position | — | `public UV Position { get ; set ; }` |
| Property | XVec | — | `public UV XVec { get ; set ; }` |