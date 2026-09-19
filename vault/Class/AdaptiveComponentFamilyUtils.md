---
type: AdaptiveComponentFamilyUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# AdaptiveComponentFamilyUtils

`Autodesk.Revit.DB.AdaptiveComponentFamilyUtils` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetNumberOfAdaptivePoints | 2012 | `public static int GetNumberOfAdaptivePoints ( Family family )` |
| Method | GetNumberOfPlacementPoints | 2012 | `public static int GetNumberOfPlacementPoints ( Family family )` |
| Method | GetNumberOfShapeHandlePoints | 2012 | `public static int GetNumberOfShapeHandlePoints ( Family family )` |
| Method | GetPlacementNumber | 2012 | `public static int GetPlacementNumber ( Document doc , ElementId refPointId )` |
| Method | GetPointConstraintType | 2012 | `public static AdaptivePointConstraintType GetPointConstraintType ( Document doc , ElementId refPointId )` |
| Method | GetPointOrientationType | 2012 | `public static AdaptivePointOrientationType GetPointOrientationType ( Document doc , ElementId refPointId )` |
| Method | IsAdaptiveComponentFamily | 2012 | `public static bool IsAdaptiveComponentFamily ( Family family )` |
| Method | IsAdaptivePlacementPoint | 2012 | `public static bool IsAdaptivePlacementPoint ( Document doc , ElementId refPointId )` |
| Method | IsAdaptivePoint | 2012 | `public static bool IsAdaptivePoint ( Document doc , ElementId refPointId )` |
| Method | IsAdaptiveShapeHandlePoint | 2012 | `public static bool IsAdaptiveShapeHandlePoint ( Document doc , ElementId refPointId )` |
| Method | MakeAdaptivePoint | 2012 | `public static void MakeAdaptivePoint ( Document doc , ElementId refPointId , AdaptivePointType type )` |
| Method | SetPlacementNumber | 2012 | `public static void SetPlacementNumber ( Document doc , ElementId refPointId , int placementNumber )` |
| Method | SetPointConstraintType | 2012 | `public static void SetPointConstraintType ( Document doc , ElementId refPointId , AdaptivePointConstraintType constraintType )` |
| Method | SetPointOrientationType | 2012 | `public static void SetPointOrientationType ( Document doc , ElementId refPointId , AdaptivePointOrientationType orientationType )` |