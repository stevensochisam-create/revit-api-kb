---
type: Outline
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# Outline

`Autodesk.Revit.DB.Outline` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | Outline | — | `` |
| Method | AddPoint | 2011 | `public void AddPoint ( XYZ point )` |
| Method | Contains | 2011 | `public bool Contains ( XYZ point , double tolerance )` |
| Method | ContainsOtherOutline | 2011 | `public bool ContainsOtherOutline ( Outline otherOutline , double tolerance )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetDiagonalLength | 2011 | `public double GetDiagonalLength ()` |
| Method | Intersects | 2011 | `public bool Intersects ( Outline outline , double tolerance )` |
| Method | IsScaleValid | 2011 | `public bool IsScaleValid ( double scale )` |
| Method | Scale | 2011 | `public void Scale ( double scale )` |
| Property | IsEmpty | 2011 | `public bool IsEmpty { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | MaximumPoint | 2011 | `public XYZ MaximumPoint { get ; set ; }` |
| Property | MinimumPoint | 2011 | `public XYZ MinimumPoint { get ; set ; }` |