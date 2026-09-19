---
type: Plane
namespace: Autodesk.Revit.DB
version: 2024
members: 8
tags: [revit-api, class]
---

# Plane

`Autodesk.Revit.DB.Plane` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2017 | `public static Plane Create ( Frame frameOfReference )` |
| Method | CreateByNormalAndOrigin | 2017 | `public static Plane CreateByNormalAndOrigin ( XYZ normal , XYZ origin )` |
| Method | CreateByOriginAndBasis | 2017 | `public static Plane CreateByOriginAndBasis ( XYZ origin , XYZ basisX , XYZ basisY )` |
| Method | CreateByThreePoints | 2017 | `public static Plane CreateByThreePoints ( XYZ point1 , XYZ point2 , XYZ point3 )` |
| Property | Normal | 2016 | `public XYZ Normal { get ; }` |
| Property | Origin | 2016 | `public XYZ Origin { get ; }` |
| Property | XVec | 2016 | `public XYZ XVec { get ; }` |
| Property | YVec | 2016 | `public XYZ YVec { get ; }` |