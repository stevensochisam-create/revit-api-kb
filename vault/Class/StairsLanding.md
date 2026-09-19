---
type: StairsLanding
namespace: Autodesk.Revit.DB.Architecture
version: 2024
members: 14
tags: [revit-api, class]
---

# StairsLanding

`Autodesk.Revit.DB.Architecture.StairsLanding` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanCreateAutomaticLanding | 2013 | `public static bool CanCreateAutomaticLanding ( Document document , ElementId firstRunId , ElementId secondRunId )` |
| Method | CreateAutomaticLanding | 2013 | `public static IList < ElementId > CreateAutomaticLanding ( Document document , ElementId firstRunId , ElementId secondRunId )` |
| Method | CreateSketchedLanding | 2013 | `public static StairsLanding CreateSketchedLanding ( Document document , ElementId stairsId , CurveLoop curveLoop , double baseElevation )` |
| Method | CreateSketchedLandingWithSlopeData | 2013 | `public static StairsLanding CreateSketchedLandingWithSlopeData ( Document document , ElementId stairsId , IList < SketchedStairsCurveData > curveLoop , double baseElevation )` |
| Method | GetAllSupports | 2013 | `public IList < ElementId > GetAllSupports ()` |
| Method | GetConnections | 2014 | `public IList < StairsComponentConnection > GetConnections ()` |
| Method | GetFootprintBoundary | 2013 | `public CurveLoop GetFootprintBoundary ()` |
| Method | GetStairs | 2013 | `public Stairs GetStairs ()` |
| Method | GetStairsPath | 2013 | `public CurveLoop GetStairsPath ()` |
| Method | SetSketchedLandingBoundaryAndPath | 2017 | `public void SetSketchedLandingBoundaryAndPath ( Document document , CurveLoop boundaryCurveLoop , CurveLoop pathCurveLoop )` |
| Property | BaseElevation | 2013 | `public double BaseElevation { get ; set ; }` |
| Property | IsAutomaticLanding | 2013 | `public bool IsAutomaticLanding { get ; }` |
| Property | Parameter | — | `` |
| Property | Thickness | 2013 | `public double Thickness { get ; }` |