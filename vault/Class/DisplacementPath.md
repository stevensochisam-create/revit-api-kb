---
type: DisplacementPath
namespace: Autodesk.Revit.DB
version: 2024
members: 7
tags: [revit-api, class]
---

# DisplacementPath

`Autodesk.Revit.DB.DisplacementPath` · Revit 2024 · 7 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2014 | `public static ElementId Create ( Document aDoc , DisplacementElement displacementElement , Reference reference , double param )` |
| Method | IsValidParam | 2014 | `public static bool IsValidParam ( double param )` |
| Method | IsValidReference | 2014 | `public static bool IsValidReference ( DisplacementElement displacementElement , Reference reference )` |
| Method | SetAnchorPoint | 2014 | `public void SetAnchorPoint ( DisplacementElement displacementElement , Reference reference , double param )` |
| Property | AncestorIdx | 2014 | `public int AncestorIdx { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | PathStyle | 2014 | `public DisplacementPathStyle PathStyle { get ; set ; }` |