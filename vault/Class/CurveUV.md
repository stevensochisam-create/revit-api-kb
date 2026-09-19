---
type: CurveUV
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# CurveUV

`Autodesk.Revit.DB.CurveUV` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | As3DCurveInXYPlane | 2021 | `public Curve As3DCurveInXYPlane ()` |
| Method | ComputeDerivatives | 2021 | `public IList < UV > ComputeDerivatives ( double parameter , bool normalized )` |
| Method | Create | 2021 | `public static CurveUV Create ( Curve curve3D )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | Evaluate | 2021 | `public UV Evaluate ( double parameter , bool normalized )` |
| Method | GetEndParameter | 2021 | `public double GetEndParameter ( int index )` |
| Method | Transform | 2021 | `public CurveUV Transform ( Transform2D trfUV )` |
| Property | IsBound | 2021 | `public bool IsBound { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |