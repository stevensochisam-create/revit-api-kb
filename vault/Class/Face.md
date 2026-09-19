---
type: Face
namespace: Autodesk.Revit.DB
version: 2024
members: 22
tags: [revit-api, class]
---

# Face

`Autodesk.Revit.DB.Face` · Revit 2024 · 22 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ComputeDerivatives | — | `public Transform ComputeDerivatives ( UV point )` |
| Method | ComputeNormal | — | `public XYZ ComputeNormal ( UV point )` |
| Method | ComputeSecondDerivatives | 2016 | `public FaceSecondDerivatives ComputeSecondDerivatives ( UV point )` |
| Method | Evaluate | — | `public XYZ Evaluate ( UV params )` |
| Method | GetBoundingBox | 2011 | `public BoundingBoxUV GetBoundingBox ()` |
| Method | GetEdgesAsCurveLoops | 2015 | `public IList < CurveLoop > GetEdgesAsCurveLoops ()` |
| Method | GetRegions | — | `public IList < Face > GetRegions ()` |
| Method | GetSurface | 2018 | `public Surface GetSurface ()` |
| Method | Intersect | — | `` |
| Method | IsInside | — | `` |
| Method | Project | — | `public IntersectionResult Project ( XYZ point )` |
| Method | Triangulate | — | `` |
| Method | Triangulate | — | `public Mesh Triangulate ()` |
| Property | Area | — | `public double Area { get ; }` |
| Property | EdgeLoops | — | `public EdgeArrayArray EdgeLoops { get ; }` |
| Property | HasRegions | — | `public bool HasRegions { get ; }` |
| Property | IsCyclic | — | `public bool this [ int paramIdx ] { get ; }` |
| Property | IsTwoSided | — | `public virtual bool IsTwoSided { get ; }` |
| Property | MaterialElementId | — | `public ElementId MaterialElementId { get ; }` |
| Property | OrientationMatchesSurfaceOrientation | — | `public bool OrientationMatchesSurfaceOrientation { get ; }` |
| Property | Period | — | `public double this [ int paramIdx ] { get ; }` |
| Property | Reference | — | `public Reference Reference { get ; }` |