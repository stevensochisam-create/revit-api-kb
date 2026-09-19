---
type: NurbSpline
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# NurbSpline

`Autodesk.Revit.DB.NurbSpline` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2017 | `public static NurbSpline Create ( HermiteSpline hermiteSpline )` |
| Method | CreateCurve | — | `` |
| Method | Intersect | — | `` |
| Method | IsInside | — | `` |
| Method | SetControlPointsAndWeights | — | `public void SetControlPointsAndWeights ( IList < XYZ > ctrlPoints , DoubleArray weights )` |
| Property | CtrlPoints | — | `public IList < XYZ > CtrlPoints { get ; }` |
| Property | Degree | — | `public int Degree { get ; }` |
| Property | Knots | — | `public DoubleArray Knots { get ; set ; }` |
| Property | Weights | — | `public DoubleArray Weights { get ; }` |
| Property | isRational | — | `public bool isRational { get ; }` |