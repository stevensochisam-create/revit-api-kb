---
type: FabricArea
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 26
tags: [revit-api, class]
---

# FabricArea

`Autodesk.Revit.DB.Structure.FabricArea` · Revit 2024 · 26 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CopyCurveLoopsInSketch | 2013 | `public IList < CurveLoop > CopyCurveLoopsInSketch ()` |
| Method | Create | — | `` |
| Method | GetBoundaryCurveIds | 2015 | `public IList < ElementId > GetBoundaryCurveIds ()` |
| Method | GetFabricSheetElementIds | 2013 | `public IList < ElementId > GetFabricSheetElementIds ()` |
| Method | GetReinforcementRoundingManager | 2014 | `public FabricRoundingManager GetReinforcementRoundingManager ()` |
| Method | GetTotalSheetMass | 2013 | `public double GetTotalSheetMass ()` |
| Method | GetValidViewsForTags | 2013 | `public IList < ElementId > GetValidViewsForTags ()` |
| Method | IsCoverOffsetValid | 2013 | `public bool IsCoverOffsetValid ( double coverOffset )` |
| Method | IsValidMajorLapSplice | 2013 | `public bool IsValidMajorLapSplice ( double majorLapSplice )` |
| Method | IsValidMinorLapSplice | 2013 | `public bool IsValidMinorLapSplice ( double minorLapSplice )` |
| Method | RemoveFabricReinforcementSystem | 2015 | `public static IList < ElementId > RemoveFabricReinforcementSystem ( Document doc , FabricArea system )` |
| Property | CoverOffset | 2013 | `public double CoverOffset { get ; set ; }` |
| Property | Direction | 2013 | `public XYZ Direction { get ; }` |
| Property | DirectionOrigin | 2014 | `public XYZ DirectionOrigin { get ; }` |
| Property | FabricAreaType | 2013 | `public FabricAreaType FabricAreaType { get ; }` |
| Property | FabricLocation | 2013 | `public FabricLocation FabricLocation { get ; set ; }` |
| Property | FabricSheetTypeId | 2013 | `public ElementId FabricSheetTypeId { get ; set ; }` |
| Property | HostId | 2013 | `public ElementId HostId { get ; }` |
| Property | LapSplicePosition | 2013 | `public FabricLapSplicePosition LapSplicePosition { get ; set ; }` |
| Property | MajorLapSpliceLength | 2013 | `public double MajorLapSpliceLength { get ; set ; }` |
| Property | MajorSheetAlignment | 2013 | `public FabricSheetAlignment MajorSheetAlignment { get ; set ; }` |
| Property | MinorLapSpliceLength | 2013 | `public double MinorLapSpliceLength { get ; set ; }` |
| Property | MinorSheetAlignment | 2013 | `public FabricSheetAlignment MinorSheetAlignment { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | SketchId | 2013 | `public ElementId SketchId { get ; }` |
| Property | TagViewId | 2013 | `public ElementId TagViewId { get ; set ; }` |