---
type: Solid
namespace: Autodesk.Revit.DB
version: 2024
members: 7
tags: [revit-api, class]
---

# Solid

`Autodesk.Revit.DB.Solid` · Revit 2024 · 7 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ComputeCentroid | — | `public XYZ ComputeCentroid ()` |
| Method | GetBoundingBox | 2014 | `public BoundingBoxXYZ GetBoundingBox ()` |
| Method | IntersectWithCurve | 2013 | `public SolidCurveIntersection IntersectWithCurve ( Curve curve , SolidCurveIntersectionOptions options )` |
| Property | Edges | — | `public EdgeArray Edges { get ; }` |
| Property | Faces | — | `public FaceArray Faces { get ; }` |
| Property | SurfaceArea | — | `public double SurfaceArea { get ; }` |
| Property | Volume | — | `public double Volume { get ; }` |