---
type: TopographySurface
namespace: Autodesk.Revit.DB.Architecture
version: 2024
members: 24
tags: [revit-api, class]
---

# TopographySurface

`Autodesk.Revit.DB.Architecture.TopographySurface` · Revit 2024 · 24 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddPoints | — | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements. It is recommended that TopographySurface elements should be converted to Toposolid elements to enable bet` |
| Method | ArePointsDistinct | 2014 | `public static bool ArePointsDistinct ( IList < XYZ > points )` |
| Method | AsSiteSubRegion | 2014 | `public SiteSubRegion AsSiteSubRegion ()` |
| Method | ChangePointElevation | 2014 | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements. It is recommended that TopographySurface elements should be converted to Toposolid elements to enable bet` |
| Method | ChangePointsElevation | 2014 | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements. It is recommended that TopographySurface elements should be converted to Toposolid elements to enable bet` |
| Method | ContainsPoint | 2014 | `public bool ContainsPoint ( XYZ point )` |
| Method | Create | — | `` |
| Method | DeletePoints | 2014 | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements. It is recommended that TopographySurface elements should be converted to Toposolid elements to enable bet` |
| Method | FindPoints | 2014 | `public IList < XYZ > FindPoints ( Outline boundingBox )` |
| Method | GetBoundaryPoints | 2014 | `public IList < XYZ > GetBoundaryPoints ()` |
| Method | GetHostedSubRegionIds | 2014 | `public IList < ElementId > GetHostedSubRegionIds ()` |
| Method | GetInteriorPoints | 2014 | `public IList < XYZ > GetInteriorPoints ()` |
| Method | GetPoints | 2014 | `public IList < XYZ > GetPoints ()` |
| Method | IsBoundaryPoint | 2014 | `public bool IsBoundaryPoint ( XYZ point )` |
| Method | IsValidFaceSet | 2019.2 | `public static bool IsValidFaceSet ( IList < PolymeshFacet > facets , IList < XYZ > points )` |
| Method | IsValidRegion | 2014 | `public static bool IsValidRegion ( IList < XYZ > points )` |
| Method | MovePoint | 2014 | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements. It is recommended that TopographySurface elements should be converted to Toposolid elements to enable bet` |
| Method | MovePoints | 2014 | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 with the introduction of the new Toposolid elements. It is recommended that TopographySurface elements should be converted to Toposolid elements to enable bet` |
| Property | ArePointsEditable | 2019 | `public bool ArePointsEditable { get ; }` |
| Property | AssociatedBuildingPadId | 2015 | `public ElementId AssociatedBuildingPadId { get ; }` |
| Property | IsAssociatedWithBuildingPad | 2015 | `public bool IsAssociatedWithBuildingPad { get ; }` |
| Property | IsSiteSubRegion | 2014 | `public bool IsSiteSubRegion { get ; }` |
| Property | MaterialId | 2014 | `public ElementId MaterialId { get ; set ; }` |
| Property | Parameter | — | `` |