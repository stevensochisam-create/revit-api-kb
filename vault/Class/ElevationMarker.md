---
type: ElevationMarker
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# ElevationMarker

`Autodesk.Revit.DB.ElevationMarker` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateElevation | 2013 | `public ViewSection CreateElevation ( Document document , ElementId viewPlanId , int index )` |
| Method | CreateElevationMarker | 2013 | `public static ElevationMarker CreateElevationMarker ( Document document , ElementId viewFamilyTypeId , XYZ origin , int initialViewScale )` |
| Method | CreateReferenceElevation | 2013 | `public void CreateReferenceElevation ( Document document , int index , ElementId viewIdToReference )` |
| Method | CreateReferenceElevationMarker | 2013 | `public static ElevationMarker CreateReferenceElevationMarker ( Document document , ElementId viewFamilyTypeId , XYZ origin , ElementId viewPlanId )` |
| Method | GetViewId | 2013 | `public ElementId GetViewId ( int index )` |
| Method | HasElevations | 2013 | `public bool HasElevations ()` |
| Method | IsAvailableIndex | 2013 | `public bool IsAvailableIndex ( int index )` |
| Property | CurrentViewCount | 2013 | `public int CurrentViewCount { get ; }` |
| Property | IsReference | 2013 | `public bool IsReference { get ; }` |
| Property | MaximumViewCount | 2013 | `public int MaximumViewCount { get ; }` |
| Property | Parameter | — | `` |