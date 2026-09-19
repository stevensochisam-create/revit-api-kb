---
type: SiteSubRegion
namespace: Autodesk.Revit.DB.Architecture
version: 2024
members: 8
tags: [revit-api, class]
---

# SiteSubRegion

`Autodesk.Revit.DB.Architecture.SiteSubRegion` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetBoundary | 2014 | `public IList < CurveLoop > GetBoundary ()` |
| Method | IsValidBoundary | 2014 | `public static bool IsValidBoundary ( IList < CurveLoop > curveLoops )` |
| Method | SetBoundary | 2014 | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements. It is recommended that TopographySurface elements should be converted to Toposolid elements to enable bet` |
| Property | HostId | 2014 | `public ElementId HostId { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | TopographySurface | 2014 | `public TopographySurface TopographySurface { get ; }` |