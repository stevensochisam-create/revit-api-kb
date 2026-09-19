---
type: Curve
namespace: Autodesk.Revit.DB
version: 2024
members: 27
tags: [revit-api, class]
---

# Curve

`Autodesk.Revit.DB.Curve` · Revit 2024 · 27 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Clone | — | `public Curve Clone ()` |
| Method | ComputeClosestPoints | 2018.1 | `public void ComputeClosestPoints ( Curve otherCurve , bool withinThisCurveBounds , bool withinOtherCurveBounds , bool returnAllCriticalPnts , out IList < ClosestPointsPairBetweenTwoCurves > resultList )` |
| Method | ComputeDerivatives | — | `public Transform ComputeDerivatives ( double parameter , bool normalized )` |
| Method | ComputeNormalizedParameter | — | `public double ComputeNormalizedParameter ( double rawParameter )` |
| Method | ComputeRawParameter | — | `public double ComputeRawParameter ( double normalizedParameter )` |
| Method | CreateOffset | 2015 | `public Curve CreateOffset ( double offsetDist , XYZ referenceVector )` |
| Method | CreateReversed | 2015 | `public Curve CreateReversed ()` |
| Method | CreateTransformed | 2014 | `public Curve CreateTransformed ( Transform transform )` |
| Method | Distance | — | `public double Distance ( XYZ point )` |
| Method | Evaluate | — | `public XYZ Evaluate ( double parameter , bool normalized )` |
| Method | GetEndParameter | 2014 | `public double GetEndParameter ( int index )` |
| Method | GetEndPoint | 2014 | `public XYZ GetEndPoint ( int index )` |
| Method | GetEndPointReference | 2014 | `public Reference GetEndPointReference ( int index )` |
| Method | Intersect | — | `` |
| Method | IsInside | — | `` |
| Method | MakeBound | — | `public void MakeBound ( double startParameter , double endParameter )` |
| Method | MakeUnbound | — | `public void MakeUnbound ()` |
| Method | Project | — | `public IntersectionResult Project ( XYZ point )` |
| Method | SetGraphicsStyleId | — | `public void SetGraphicsStyleId ( ElementId id )` |
| Method | Tessellate | — | `public IList < XYZ > Tessellate ()` |
| Property | ApproximateLength | — | `public double ApproximateLength { get ; }` |
| Property | IsBound | — | `public bool IsBound { get ; }` |
| Property | IsClosed | 2021 | `public bool IsClosed { get ; }` |
| Property | IsCyclic | — | `public bool IsCyclic { get ; }` |
| Property | Length | — | `public double Length { get ; }` |
| Property | Period | — | `public double Period { get ; }` |
| Property | Reference | — | `public Reference Reference { get ; }` |