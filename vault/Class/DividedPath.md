---
type: DividedPath
namespace: Autodesk.Revit.DB
version: 2024
members: 33
tags: [revit-api, class]
---

# DividedPath

`Autodesk.Revit.DB.DividedPath` · Revit 2024 · 33 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreCurveReferencesConnected | 2013 | `public static bool AreCurveReferencesConnected ( Document document , IList < Reference > curveReferences )` |
| Method | Create | — | `` |
| Method | Flip | 2013 | `public void Flip ()` |
| Method | GetIntersectingElements | 2013 | `public ICollection < ElementId > GetIntersectingElements ()` |
| Method | IsCurveReferenceValid | 2013 | `public static bool IsCurveReferenceValid ( Document document , Reference curveReference )` |
| Method | IsIntersectorValidForCreation | 2013 | `public static bool IsIntersectorValidForCreation ( Document document , ElementId intersector )` |
| Method | IsIntersectorValidForDividedPath | 2013 | `public bool IsIntersectorValidForDividedPath ( ElementId intersector )` |
| Method | IsValidBeginningIndent | 2013 | `public bool IsValidBeginningIndent ( double beginningIndent )` |
| Method | IsValidEndIndent | 2013 | `public bool IsValidEndIndent ( double endIndent )` |
| Method | IsValidFixedNumberOfPoints | 2013 | `public static bool IsValidFixedNumberOfPoints ( int fixedNumberOfPoints )` |
| Method | IsValidMeasurementType | 2013 | `public bool IsValidMeasurementType ( DividedPathMeasurementType measurementType )` |
| Method | IsValidSpacingRuleJustification | 2013 | `public bool IsValidSpacingRuleJustification ( SpacingRuleJustification justification )` |
| Method | IsValidSpacingRuleLayout | 2013 | `public bool IsValidSpacingRuleLayout ( SpacingRuleLayout layout )` |
| Method | SeparateReferencesIntoConnectedReferences | 2013 | `public static IList < IList < Reference >> SeparateReferencesIntoConnectedReferences ( Document document , IList < Reference > curveReferences )` |
| Method | SetIntersectingElements | 2013 | `public void SetIntersectingElements ( ICollection < ElementId > intersectors )` |
| Property | BeginningIndent | 2013 | `public double BeginningIndent { get ; set ; }` |
| Property | DisplayNodeNumbers | 2013 | `public bool DisplayNodeNumbers { get ; set ; }` |
| Property | DisplayNodes | 2013 | `public bool DisplayNodes { get ; set ; }` |
| Property | DisplayReferenceCurves | 2013 | `public bool DisplayReferenceCurves { get ; set ; }` |
| Property | Distance | 2013 | `public double Distance { get ; set ; }` |
| Property | EndIndent | 2013 | `public double EndIndent { get ; set ; }` |
| Property | FixedNumberOfPoints | 2013 | `public int FixedNumberOfPoints { get ; set ; }` |
| Property | Flipped | 2013 | `public bool Flipped { get ; }` |
| Property | IsClosedLoop | 2013 | `public bool IsClosedLoop { get ; }` |
| Property | IsCyclical | 2013 | `public bool IsCyclical { get ; }` |
| Property | MaximumDistance | 2013 | `public double MaximumDistance { get ; set ; }` |
| Property | MeasurementType | 2013 | `public DividedPathMeasurementType MeasurementType { get ; set ; }` |
| Property | MinimumDistance | 2013 | `public double MinimumDistance { get ; set ; }` |
| Property | NumberOfPoints | 2013 | `public int NumberOfPoints { get ; }` |
| Property | Parameter | — | `` |
| Property | SpacingRuleJustification | 2013 | `public SpacingRuleJustification SpacingRuleJustification { get ; set ; }` |
| Property | SpacingRuleLayout | 2013 | `public SpacingRuleLayout SpacingRuleLayout { get ; set ; }` |
| Property | TotalPathLength | 2013 | `public double TotalPathLength { get ; }` |