---
type: ViewShapeBuilder
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# ViewShapeBuilder

`Autodesk.Revit.DB.ViewShapeBuilder` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ViewShapeBuilder | — | `` |
| Constructor | ViewShapeBuilder | 2015 | `public ViewShapeBuilder ()` |
| Method | AddCurve | 2015 | `public void AddCurve ( Curve GCurve )` |
| Method | Reset | 2015 | `public void Reset ()` |
| Method | ValidateCurve | — | `` |
| Method | ValidateShape | 2017 | `public static bool ValidateShape ( IList < GeometryObject > shape , DirectShapeTargetViewType targetViewType )` |
| Method | ValidateViewType | 2015 | `public static bool ValidateViewType ( DirectShapeTargetViewType targetViewType )` |
| Property | ViewNormal | 2015 | `public XYZ ViewNormal { get ; set ; }` |
| Property | ViewType | 2015 | `public DirectShapeTargetViewType ViewType { get ; set ; }` |