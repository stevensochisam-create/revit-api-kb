---
type: Transform1D
namespace: Autodesk.Revit.DB
version: 2024
members: 15
tags: [revit-api, class]
---

# Transform1D

`Autodesk.Revit.DB.Transform1D` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | Transform1D | — | `` |
| Method | AlmostEqual | 2021 | `public bool AlmostEqual ( Transform1D right )` |
| Method | Assign | 2021 | `public void Assign ( Transform1D from )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetInverse | 2021 | `public Transform1D GetInverse ()` |
| Method | Multiply | 2021 | `public Transform1D Multiply ( Transform1D right )` |
| Method | OfPoint | 2021 | `public double OfPoint ( double point )` |
| Method | OfVector | 2021 | `public double OfVector ( double vector )` |
| Method | SetToIdentity | 2021 | `public Transform1D SetToIdentity ()` |
| Method | TransformParameterDomain | 2021 | `public IList < double > TransformParameterDomain ( double domainStart , double domainEnd )` |
| Property | Determinant | 2021 | `public double Determinant { get ; }` |
| Property | IsIdentity | 2021 | `public bool IsIdentity { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Scale | 2021 | `public double Scale { get ; set ; }` |
| Property | Translation | 2021 | `public double Translation { get ; set ; }` |