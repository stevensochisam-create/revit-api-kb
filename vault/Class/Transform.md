---
type: Transform
namespace: Autodesk.Revit.DB
version: 2024
members: 24
tags: [revit-api, class]
---

# Transform

`Autodesk.Revit.DB.Transform` · Revit 2024 · 24 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | Transform | — | `public Transform ( Transform source )` |
| Method | AlmostEqual | — | `public bool AlmostEqual ( Transform right )` |
| Method | CreateReflection | 2014 | `public static Transform CreateReflection ( Plane plane )` |
| Method | CreateRotation | 2014 | `public static Transform CreateRotation ( XYZ axis , double angle )` |
| Method | CreateRotationAtPoint | 2014 | `public static Transform CreateRotationAtPoint ( XYZ axis , double angle , XYZ origin )` |
| Method | CreateTranslation | 2014 | `public static Transform CreateTranslation ( XYZ vector )` |
| Method | Multiply | — | `public Transform Multiply ( Transform right )` |
| Method | OfPoint | — | `public XYZ OfPoint ( XYZ point )` |
| Method | OfVector | — | `public XYZ OfVector ( XYZ vec )` |
| Method | ScaleBasis | — | `public Transform ScaleBasis ( double scale )` |
| Method | ScaleBasisAndOrigin | — | `public Transform ScaleBasisAndOrigin ( double scale )` |
| Property | Basis | — | `public XYZ this [ int idx ] { get ; set ; }` |
| Property | BasisX | — | `public XYZ BasisX { get ; set ; }` |
| Property | BasisY | — | `public XYZ BasisY { get ; set ; }` |
| Property | BasisZ | — | `public XYZ BasisZ { get ; set ; }` |
| Property | Determinant | — | `public double Determinant { get ; }` |
| Property | HasReflection | — | `public bool HasReflection { get ; }` |
| Property | Identity | — | `public static Transform Identity { get ; }` |
| Property | Inverse | — | `public Transform Inverse { get ; }` |
| Property | IsConformal | — | `public bool IsConformal { get ; }` |
| Property | IsIdentity | — | `public bool IsIdentity { get ; }` |
| Property | IsTranslation | — | `public bool IsTranslation { get ; }` |
| Property | Origin | — | `public XYZ Origin { get ; set ; }` |
| Property | Scale | — | `public double Scale { get ; }` |