---
type: FabricSheet
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 32
tags: [revit-api, class]
---

# FabricSheet

`Autodesk.Revit.DB.Structure.FabricSheet` · Revit 2024 · 32 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | GetBendProfile | 2016 | `public CurveLoop GetBendProfile ()` |
| Method | GetBendProfileWithFillets | 2016 | `public CurveLoop GetBendProfileWithFillets ()` |
| Method | GetReinforcementRoundingManager | 2014 | `public FabricRoundingManager GetReinforcementRoundingManager ()` |
| Method | GetSegmentParameterIdsAndLengths | 2017 | `public IDictionary < ElementId , double > GetSegmentParameterIdsAndLengths ( bool rounded )` |
| Method | GetSheetLocation | 2015 | `public Transform GetSheetLocation ()` |
| Method | GetWireCenterlines | — | `` |
| Method | GetWireCenterlines | 2013 | `public IList < Curve > GetWireCenterlines ()` |
| Method | IsCoverOffsetValid | 2015 | `public bool IsCoverOffsetValid ( double coverOffset )` |
| Method | IsSingleFabricSheetWithinHost | 2015 | `public bool IsSingleFabricSheetWithinHost ( Element hostElement , Transform transform )` |
| Method | IsUnobscuredInView | 2021 | `public bool IsUnobscuredInView ( View view )` |
| Method | IsValidHost | — | `` |
| Method | PlaceInHost | 2015 | `public void PlaceInHost ( Element hostElement , Transform transform )` |
| Method | SetBendProfile | 2016 | `public void SetBendProfile ( CurveLoop bendProfile )` |
| Method | SetSegmentLength | 2017 | `public void SetSegmentLength ( ElementId segmentParameterId , double value )` |
| Method | SetUnobscuredInView | 2021 | `public void SetUnobscuredInView ( View view , bool unobscured )` |
| Property | BendFinalLoopOrientationVector | 2016 | `public XYZ BendFinalLoopOrientationVector { get ; }` |
| Property | BentFabricBendDirection | 2016 | `public BentFabricBendDirection BentFabricBendDirection { get ; set ; }` |
| Property | BentFabricLongitudinalCutLength | 2016 | `public double BentFabricLongitudinalCutLength { get ; set ; }` |
| Property | BentFabricStraightWiresLocation | 2017 | `public BentFabricStraightWiresLocation BentFabricStraightWiresLocation { get ; set ; }` |
| Property | CoverOffset | 2015 | `public double CoverOffset { get ; set ; }` |
| Property | CutOverallLength | 2013 | `public double CutOverallLength { get ; }` |
| Property | CutOverallWidth | 2013 | `public double CutOverallWidth { get ; }` |
| Property | CutSheetMass | 2013 | `public double CutSheetMass { get ; }` |
| Property | FabricAreaOwnerId | 2013 | `public ElementId FabricAreaOwnerId { get ; }` |
| Property | FabricHostReference | 2015 | `public FabricHostReference FabricHostReference { get ; set ; }` |
| Property | FabricLocation | 2015 | `public FabricLocation FabricLocation { get ; set ; }` |
| Property | FabricNumber | 2017 | `public string FabricNumber { get ; }` |
| Property | HostId | 2015 | `public ElementId HostId { get ; }` |
| Property | IsBent | 2016 | `public bool IsBent { get ; }` |
| Property | Parameter | — | `` |
| Property | SketchId | 2013 | `public ElementId SketchId { get ; }` |