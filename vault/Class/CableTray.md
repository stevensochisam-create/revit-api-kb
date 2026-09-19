---
type: CableTray
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 7
tags: [revit-api, class]
---

# CableTray

`Autodesk.Revit.DB.Electrical.CableTray` · Revit 2024 · 7 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `public static CableTray Create ( Document document , ElementId cabletrayType , XYZ startPoint , XYZ endPoint , ElementId levelId )` |
| Method | GetShapeType | — | `public CableTrayShape GetShapeType ()` |
| Method | IsValidCableTrayType | — | `public static bool IsValidCableTrayType ( Document document , ElementId cabletrayType )` |
| Method | IsValidRungSpace | — | `public bool IsValidRungSpace ( double rungSpace )` |
| Property | CurveNormal | 2014 | `public XYZ CurveNormal { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | RungSpace | — | `public double RungSpace { get ; set ; }` |