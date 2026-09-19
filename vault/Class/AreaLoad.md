---
type: AreaLoad
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 14
tags: [revit-api, class]
---

# AreaLoad

`Autodesk.Revit.DB.Structure.AreaLoad` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreCurveLoopsValid | 2024 | `public static bool AreCurveLoopsValid ( IList < CurveLoop > loops )` |
| Method | Create | — | `` |
| Method | GetLoops | 2016 | `public IList < CurveLoop > GetLoops ()` |
| Method | GetRefPoint | 2016 | `public XYZ GetRefPoint ( int index )` |
| Method | IsCurveLoopsInsideHostBoundaries | 2024 | `public static bool IsCurveLoopsInsideHostBoundaries ( Document doc , ElementId hostId , IList < CurveLoop > loops )` |
| Method | IsValidHostId | 2023 | `public static bool IsValidHostId ( Document pDoc , ElementId hostId )` |
| Method | SetLoops | 2016 | `public bool SetLoops ( Document doc , IList < CurveLoop > newLoops )` |
| Property | Area | 2016 | `public double Area { get ; }` |
| Property | ForceVector1 | 2016 | `public XYZ ForceVector1 { get ; set ; }` |
| Property | ForceVector2 | 2016 | `public XYZ ForceVector2 { get ; set ; }` |
| Property | ForceVector3 | 2016 | `public XYZ ForceVector3 { get ; set ; }` |
| Property | IsProjected | 2016 | `public bool IsProjected { get ; set ; }` |
| Property | NumRefPoints | — | `public int NumRefPoints { get ; }` |
| Property | Parameter | — | `` |