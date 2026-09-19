---
type: Mesh
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# Mesh

`Autodesk.Revit.DB.Mesh` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ComputeSurfaceArea | 2024 | `public double ComputeSurfaceArea ()` |
| Method | GetNormal | 2021 | `public XYZ GetNormal ( int idx )` |
| Method | GetNormals | 2021 | `public IList < XYZ > GetNormals ()` |
| Property | DistributionOfNormals | 2021 | `public DistributionOfNormals DistributionOfNormals { get ; }` |
| Property | IsClosed | 2022 | `public bool IsClosed { get ; }` |
| Property | MaterialElementId | — | `public ElementId MaterialElementId { get ; }` |
| Property | NumTriangles | — | `public int NumTriangles { get ; }` |
| Property | NumberOfNormals | 2021 | `public int NumberOfNormals { get ; }` |
| Property | Transformed | — | `public Mesh this [ Transform transform ] { get ; }` |
| Property | Triangle | — | `public MeshTriangle this [ int idx ] { get ; }` |
| Property | Vertices | — | `public IList < XYZ > Vertices { get ; }` |