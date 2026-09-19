---
type: Edge
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# Edge

`Autodesk.Revit.DB.Edge` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AsCurve | — | `public Curve AsCurve ()` |
| Method | AsCurveFollowingFace | — | `public Curve AsCurveFollowingFace ( Face faceForDir )` |
| Method | ComputeDerivatives | — | `public Transform ComputeDerivatives ( double parameter )` |
| Method | Evaluate | — | `public XYZ Evaluate ( double param )` |
| Method | EvaluateOnFace | — | `public UV EvaluateOnFace ( double param , Face face )` |
| Method | GetCurveUV | — | `` |
| Method | GetEndPointReference | — | `public Reference GetEndPointReference ( int index )` |
| Method | GetFace | 2014 | `public Face GetFace ( int index )` |
| Method | IsFlippedOnFace | — | `` |
| Method | Tessellate | — | `public IList < XYZ > Tessellate ()` |
| Method | TessellateOnFace | — | `public IList < UV > TessellateOnFace ( Face face )` |
| Property | ApproximateLength | — | `public double ApproximateLength { get ; }` |
| Property | Reference | — | `public Reference Reference { get ; }` |