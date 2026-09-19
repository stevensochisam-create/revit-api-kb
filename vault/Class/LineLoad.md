---
type: LineLoad
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 15
tags: [revit-api, class]
---

# LineLoad

`Autodesk.Revit.DB.Structure.LineLoad` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | GetCurve | 2016 | `public Curve GetCurve ()` |
| Method | IsCurveInsideHostBoundaries | 2024 | `public static bool IsCurveInsideHostBoundaries ( Document doc , ElementId hostId , Curve curve )` |
| Method | IsValidHostId | 2023 | `public static bool IsValidHostId ( Document pDoc , ElementId hostId )` |
| Method | SetCurve | 2024 | `public void SetCurve ( Curve curve )` |
| Method | SetPoints | 2016 | `public bool SetPoints ( XYZ startPoint , XYZ endPoint )` |
| Property | EndPoint | — | `public XYZ EndPoint { get ; }` |
| Property | ForceVector1 | 2016 | `public XYZ ForceVector1 { get ; set ; }` |
| Property | ForceVector2 | 2016 | `public XYZ ForceVector2 { get ; set ; }` |
| Property | IsProjected | 2016 | `public bool IsProjected { get ; set ; }` |
| Property | IsUniform | 2016 | `public bool IsUniform { get ; }` |
| Property | MomentVector1 | 2016 | `public XYZ MomentVector1 { get ; set ; }` |
| Property | MomentVector2 | 2016 | `public XYZ MomentVector2 { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | StartPoint | — | `public XYZ StartPoint { get ; }` |