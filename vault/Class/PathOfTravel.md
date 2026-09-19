---
type: PathOfTravel
namespace: Autodesk.Revit.DB.Analysis
version: 2024
members: 20
tags: [revit-api, class]
---

# PathOfTravel

`Autodesk.Revit.DB.Analysis.PathOfTravel` · Revit 2024 · 20 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | CreateMapped | — | `` |
| Method | CreateMultiple | — | `` |
| Method | FindEndsOfShortestPaths | 2020.2 | `public static IList < XYZ > FindEndsOfShortestPaths ( View DBView , IList < XYZ > destinationPoints , IList < XYZ > startPoints )` |
| Method | FindShortestPaths | 2021 | `public static IList < IList < XYZ >> FindShortestPaths ( View DBView , IList < XYZ > destinationPoints , IList < XYZ > startPoints )` |
| Method | FindStartsOfLongestPathsFromRooms | 2020.2 | `public static IList < XYZ > FindStartsOfLongestPathsFromRooms ( View DBView , IList < XYZ > destinationPoints )` |
| Method | GetCurves | 2020 | `public IList < Curve > GetCurves ()` |
| Method | GetWaypoints | 2020.2 | `public IList < XYZ > GetWaypoints ()` |
| Method | InsertWaypoint | 2020.2 | `public void InsertWaypoint ( XYZ waypoint , int index )` |
| Method | IsInRevealObstaclesMode | 2020.1 | `public static bool IsInRevealObstaclesMode ( View DBView )` |
| Method | RemoveWaypoint | 2020.2 | `public void RemoveWaypoint ( int index )` |
| Method | SetRevealObstaclesMode | 2020.1 | `public static PathOfTravelCalculationStatus SetRevealObstaclesMode ( View DBView , bool newState )` |
| Method | SetWaypoint | 2020.2 | `public void SetWaypoint ( XYZ waypoint , int index )` |
| Method | Update | 2020 | `public PathOfTravelCalculationStatus Update ()` |
| Method | UpdateMultiple | — | `` |
| Property | LineStyle | 2020 | `public ElementId LineStyle { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | PathEnd | 2020 | `public XYZ PathEnd { get ; set ; }` |
| Property | PathMidpoint | 2020 | `public XYZ PathMidpoint { get ; }` |
| Property | PathStart | 2020 | `public XYZ PathStart { get ; set ; }` |