---
type: FillPattern
namespace: Autodesk.Revit.DB
version: 2024
members: 18
tags: [revit-api, class]
---

# FillPattern

`Autodesk.Revit.DB.FillPattern` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | FillPattern | — | `` |
| Constructor | FillPattern | — | `public FillPattern ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | ExpandDots | — | `public bool ExpandDots ()` |
| Method | GetFillGrid | — | `public FillGrid GetFillGrid ( int gridIdx )` |
| Method | GetFillGrids | — | `public IList < FillGrid > GetFillGrids ()` |
| Method | IsEqual | — | `public bool IsEqual ( FillPattern other )` |
| Method | SetFillGrid | — | `public void SetFillGrid ( int gridIdx , FillGrid fillGrid )` |
| Method | SetFillGrids | — | `public void SetFillGrids ( IList < FillGrid > fillGrids )` |
| Property | GridCount | — | `public int GridCount { get ; }` |
| Property | HostOrientation | — | `public FillPatternHostOrientation HostOrientation { get ; set ; }` |
| Property | IsSolidFill | — | `public bool IsSolidFill { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | LengthPerArea | — | `public double LengthPerArea { get ; }` |
| Property | LinesPerLength | — | `public double LinesPerLength { get ; }` |
| Property | Name | — | `public string Name { get ; set ; }` |
| Property | StrokesPerArea | — | `public double StrokesPerArea { get ; }` |
| Property | Target | — | `public FillPatternTarget Target { get ; set ; }` |