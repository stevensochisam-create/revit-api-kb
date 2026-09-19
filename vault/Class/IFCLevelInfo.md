---
type: IFCLevelInfo
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 9
tags: [revit-api, class]
---

# IFCLevelInfo

`Autodesk.Revit.DB.IFC.IFCLevelInfo` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2013 | `public static IFCLevelInfo Create ( IFCAnyHandle buildingStorey , IFCAnyHandle localPlacement , double height , double elevation , double scaleFactor , bool isPrimaryLevel )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetBuildingStorey | 2012 | `public IFCAnyHandle GetBuildingStorey ()` |
| Method | GetLocalPlacement | 2014 | `public IFCAnyHandle GetLocalPlacement ()` |
| Method | GetRelatedElements | 2013 | `public ICollection < IFCAnyHandle > GetRelatedElements ()` |
| Method | GetRelatedProducts | 2013 | `public ICollection < IFCAnyHandle > GetRelatedProducts ()` |
| Property | DistanceToNextLevel | 2012 | `public double DistanceToNextLevel { get ; }` |
| Property | Elevation | 2012 | `public double Elevation { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |