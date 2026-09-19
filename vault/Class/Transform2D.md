---
type: Transform2D
namespace: Autodesk.Revit.DB
version: 2024
members: 23
tags: [revit-api, class]
---

# Transform2D

`Autodesk.Revit.DB.Transform2D` · Revit 2024 · 23 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | Transform2D | — | `` |
| Method | AlmostEqual | 2021 | `public bool AlmostEqual ( Transform2D right )` |
| Method | Assign | 2021 | `public void Assign ( Transform2D from )` |
| Method | CreateIdentity | 2021 | `public static Transform2D CreateIdentity ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetInverse | 2021 | `public Transform2D GetInverse ()` |
| Method | Multiply | 2021 | `public Transform2D Multiply ( Transform2D right )` |
| Method | OfPoint | 2021 | `public UV OfPoint ( UV point )` |
| Method | OfVector | 2021 | `public UV OfVector ( UV vector )` |
| Method | PostScale | 2021 | `public Transform2D PostScale ( double scale )` |
| Method | PreScale | 2021 | `public Transform2D PreScale ( double scale )` |
| Method | SetToIdentity | 2021 | `public Transform2D SetToIdentity ()` |
| Method | TransformUVDomainIfPossible | 2021 | `public BoundingBoxUV TransformUVDomainIfPossible ( BoundingBoxUV uvDomain )` |
| Property | BasisU | 2021 | `public UV BasisU { get ; set ; }` |
| Property | BasisV | 2021 | `public UV BasisV { get ; set ; }` |
| Property | Determinant | 2021 | `public double Determinant { get ; }` |
| Property | HasReflection | 2021 | `public bool HasReflection { get ; }` |
| Property | IsConformal | 2021 | `public bool IsConformal { get ; }` |
| Property | IsIdentity | 2021 | `public bool IsIdentity { get ; }` |
| Property | IsTranslation | 2021 | `public bool IsTranslation { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Origin | 2021 | `public UV Origin { get ; set ; }` |
| Property | Scale | 2021 | `public double Scale { get ; }` |