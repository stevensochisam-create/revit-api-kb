---
type: NurbsSurfaceData
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# NurbsSurfaceData

`Autodesk.Revit.DB.NurbsSurfaceData` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | NurbsSurfaceData | 2016 | `public NurbsSurfaceData ( NurbsSurfaceData other )` |
| Method | Create | 2016 | `public static NurbsSurfaceData Create ( int degreeU , int degreeV , IList < double > knotsU , IList < double > knotsV , IList < XYZ > controlPoints , IList < double > weights , bool bReverseOrientation )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetControlPoints | 2016 | `public IList < XYZ > GetControlPoints ()` |
| Method | GetKnotsU | 2016 | `public IList < double > GetKnotsU ()` |
| Method | GetKnotsV | 2016 | `public IList < double > GetKnotsV ()` |
| Method | GetWeights | 2016 | `public IList < double > GetWeights ()` |
| Method | IsValid | 2016 | `public bool IsValid ()` |
| Property | DegreeU | 2016 | `public int DegreeU { get ; }` |
| Property | DegreeV | 2016 | `public int DegreeV { get ; }` |
| Property | IsRational | 2016 | `public bool IsRational { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | ReverseOrientation | 2016 | `public bool ReverseOrientation { get ; }` |