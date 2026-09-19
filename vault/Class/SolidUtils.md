---
type: SolidUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 6
tags: [revit-api, class]
---

# SolidUtils

`Autodesk.Revit.DB.SolidUtils` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Clone | 2016 | `public static Solid Clone ( Solid solid )` |
| Method | CreateTransformed | 2016 | `public static Solid CreateTransformed ( Solid solid , Transform transform )` |
| Method | FindAllEdgeEndPointsAtVertex | 2021 | `public static IList < EdgeEndPoint > FindAllEdgeEndPointsAtVertex ( EdgeEndPoint edgeEndPoint )` |
| Method | IsValidForTessellation | 2013 | `public static bool IsValidForTessellation ( Solid solidOrShell )` |
| Method | SplitVolumes | 2013 | `public static IList < Solid > SplitVolumes ( Solid solid )` |
| Method | TessellateSolidOrShell | 2013 | `public static TriangulatedSolidOrShell TessellateSolidOrShell ( Solid solidOrShell , SolidOrShellTessellationControls tessellationControls )` |