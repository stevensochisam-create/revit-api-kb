---
type: StairsRun
namespace: Autodesk.Revit.DB.Architecture
version: 2024
members: 27
tags: [revit-api, class]
---

# StairsRun

`Autodesk.Revit.DB.Architecture.StairsRun` · Revit 2024 · 27 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateSketchedRun | 2013 | `public static StairsRun CreateSketchedRun ( Document document , ElementId stairsId , double baseElevation , IList < Curve > boundaryCurves , IList < Curve > riserCurves , IList < Curve > stairsPath )` |
| Method | CreateSketchedRunWithSlopeData | 2013 | `public static StairsRun CreateSketchedRunWithSlopeData ( Document document , ElementId stairsId , double baseElevation , IList < SketchedStairsCurveData > boundaryCurves , IList < Curve > riserCurves , IList < Curve > st` |
| Method | CreateSpiralRun | 2013 | `public static StairsRun CreateSpiralRun ( Document document , ElementId stairsId , XYZ center , double radius , double startAngle , double includedAngle , bool clockwise , StairsRunJustification justification )` |
| Method | CreateStraightRun | 2013 | `public static StairsRun CreateStraightRun ( Document document , ElementId stairsId , Line locationPath , StairsRunJustification justification )` |
| Method | GetAllSupports | 2013 | `public IList < ElementId > GetAllSupports ()` |
| Method | GetConnections | 2014 | `public IList < StairsComponentConnection > GetConnections ()` |
| Method | GetFootprintBoundary | 2013 | `public CurveLoop GetFootprintBoundary ()` |
| Method | GetLeftSupports | 2013 | `public IList < ElementId > GetLeftSupports ()` |
| Method | GetNumberSystemReference | 2013 | `public Reference GetNumberSystemReference ( StairsNumberSystemReferenceOption referenceOption )` |
| Method | GetRightSupports | 2013 | `public IList < ElementId > GetRightSupports ()` |
| Method | GetStairs | 2013 | `public Stairs GetStairs ()` |
| Method | GetStairsPath | 2013 | `public CurveLoop GetStairsPath ()` |
| Method | SetLocationPathForSpiralRun | 2013 | `public static bool SetLocationPathForSpiralRun ( StairsRun stairsRun , XYZ center , double radius , double startAngle , double includedAngle , bool clockwise , StairsRunJustification justification )` |
| Method | SetLocationPathForStraightRun | 2013 | `public static bool SetLocationPathForStraightRun ( StairsRun stairsRun , Line locationPath )` |
| Property | ActualRisersNumber | 2013 | `public int ActualRisersNumber { get ; }` |
| Property | ActualRunWidth | 2013 | `public double ActualRunWidth { get ; set ; }` |
| Property | ActualTreadsNumber | 2013 | `public int ActualTreadsNumber { get ; }` |
| Property | BaseElevation | 2013 | `public double BaseElevation { get ; set ; }` |
| Property | BeginsWithRiser | 2013 | `public bool BeginsWithRiser { get ; set ; }` |
| Property | EndsWithRiser | 2013 | `public bool EndsWithRiser { get ; set ; }` |
| Property | ExtensionBelowRiserBase | 2014 | `public double ExtensionBelowRiserBase { get ; set ; }` |
| Property | ExtensionBelowTreadBase | 2014 | `public double ExtensionBelowTreadBase { get ; set ; }` |
| Property | Height | 2013 | `public double Height { get ; }` |
| Property | LocationLineJustification | 2013 | `public StairsRunJustification LocationLineJustification { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | StairsRunStyle | 2013 | `public StairsRunStyle StairsRunStyle { get ; }` |
| Property | TopElevation | 2013 | `public double TopElevation { get ; set ; }` |