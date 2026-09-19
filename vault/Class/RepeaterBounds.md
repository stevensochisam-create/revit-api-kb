---
type: RepeaterBounds
namespace: Autodesk.Revit.DB
version: 2024
members: 8
tags: [revit-api, class]
---

# RepeaterBounds

`Autodesk.Revit.DB.RepeaterBounds` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AdjustForCyclicalBounds | 2014 | `public RepeaterCoordinates AdjustForCyclicalBounds ( RepeaterCoordinates coordinates )` |
| Method | AreCoordinatesInBounds | 2014 | `public bool AreCoordinatesInBounds ( RepeaterCoordinates coordinates , bool treatCyclicalBoundsAsInfinite )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetLowerBound | 2014 | `public int GetLowerBound ( int dimension )` |
| Method | GetUpperBound | 2014 | `public int GetUpperBound ( int dimension )` |
| Method | IsCyclical | 2014 | `public bool IsCyclical ( int dimension )` |
| Property | DimensionCount | 2014 | `public int DimensionCount { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |