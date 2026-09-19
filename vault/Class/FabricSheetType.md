---
type: FabricSheetType
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 37
tags: [revit-api, class]
---

# FabricSheetType

`Autodesk.Revit.DB.Structure.FabricSheetType` · Revit 2024 · 37 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateDefaultFabricSheetType | 2015 | `public static ElementId CreateDefaultFabricSheetType ( Document ADoc )` |
| Method | GetReinforcementRoundingManager | 2014 | `public FabricRoundingManager GetReinforcementRoundingManager ()` |
| Method | GetWireItem | 2017 | `public FabricWireItem GetWireItem ( int wireIndex , WireDistributionDirection direction )` |
| Method | IsCustom | 2017 | `public bool IsCustom ()` |
| Method | IsValidMajorLapSplice | 2013 | `public bool IsValidMajorLapSplice ( double majorLapSplice )` |
| Method | IsValidMinorLapSplice | 2013 | `public bool IsValidMinorLapSplice ( double minorLapSplice )` |
| Method | SetLayoutAsCustomPattern | 2018 | `public void SetLayoutAsCustomPattern ( double minorStartOverhang , double majorStartOverhang , IList < FabricWireItem > minorFabricWireItems , IList < FabricWireItem > majorFabricWireItems )` |
| Method | SetMajorLayoutAsActualSpacing | 2013 | `public void SetMajorLayoutAsActualSpacing ( double overallWidth , double minorStartOverhang , double spacing )` |
| Method | SetMajorLayoutAsFixedNumber | 2013 | `public void SetMajorLayoutAsFixedNumber ( double overallWidth , double minorStartOverhang , double minorEndOverhang , int numberOfWires )` |
| Method | SetMajorLayoutAsMaximumSpacing | 2013 | `public void SetMajorLayoutAsMaximumSpacing ( double overallWidth , double minorStartOverhang , double minorEndOverhang , double spacing )` |
| Method | SetMajorLayoutAsNumberWithSpacing | 2013 | `public void SetMajorLayoutAsNumberWithSpacing ( double overallWidth , double minorStartOverhang , int numberOfWires , double spacing )` |
| Method | SetMinorLayoutAsActualSpacing | 2013 | `public void SetMinorLayoutAsActualSpacing ( double overallLength , double majorStartOverhang , double spacing )` |
| Method | SetMinorLayoutAsFixedNumber | 2013 | `public void SetMinorLayoutAsFixedNumber ( double overallLength , double majorStartOverhang , double majorEndOverhang , int numberOfWires )` |
| Method | SetMinorLayoutAsMaximumSpacing | 2013 | `public void SetMinorLayoutAsMaximumSpacing ( double overallLength , double majorStartOverhang , double majorEndOverhang , double spacing )` |
| Method | SetMinorLayoutAsNumberWithSpacing | 2013 | `public void SetMinorLayoutAsNumberWithSpacing ( double overallLength , double majorStartOverhang , int numberOfWires , double spacing )` |
| Property | MajorDirectionWireType | 2013 | `public ElementId MajorDirectionWireType { get ; set ; }` |
| Property | MajorEndOverhang | 2013 | `public double MajorEndOverhang { get ; }` |
| Property | MajorLapSpliceLength | 2013 | `public double MajorLapSpliceLength { get ; set ; }` |
| Property | MajorLayoutPattern | 2013 | `public FabricSheetLayoutPattern MajorLayoutPattern { get ; }` |
| Property | MajorNumberOfWires | 2013 | `public int MajorNumberOfWires { get ; }` |
| Property | MajorReinforcementArea | 2013 | `public double MajorReinforcementArea { get ; }` |
| Property | MajorSpacing | 2013 | `public double MajorSpacing { get ; }` |
| Property | MajorStartOverhang | 2013 | `public double MajorStartOverhang { get ; }` |
| Property | Material | 2013 | `public ElementId Material { get ; set ; }` |
| Property | MinorDirectionWireType | 2013 | `public ElementId MinorDirectionWireType { get ; set ; }` |
| Property | MinorEndOverhang | 2013 | `public double MinorEndOverhang { get ; }` |
| Property | MinorLapSpliceLength | 2013 | `public double MinorLapSpliceLength { get ; set ; }` |
| Property | MinorLayoutPattern | 2013 | `public FabricSheetLayoutPattern MinorLayoutPattern { get ; }` |
| Property | MinorNumberOfWires | 2013 | `public int MinorNumberOfWires { get ; }` |
| Property | MinorReinforcementArea | 2013 | `public double MinorReinforcementArea { get ; }` |
| Property | MinorSpacing | 2013 | `public double MinorSpacing { get ; }` |
| Property | MinorStartOverhang | 2013 | `public double MinorStartOverhang { get ; }` |
| Property | OverallLength | 2013 | `public double OverallLength { get ; }` |
| Property | OverallWidth | 2013 | `public double OverallWidth { get ; }` |
| Property | Parameter | — | `` |
| Property | SheetMass | 2013 | `public double SheetMass { get ; set ; }` |
| Property | SheetMassUnit | 2013 | `public double SheetMassUnit { get ; }` |