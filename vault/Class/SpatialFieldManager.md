---
type: SpatialFieldManager
namespace: Autodesk.Revit.DB.Analysis
version: 2024
members: 28
tags: [revit-api, class]
---

# SpatialFieldManager

`Autodesk.Revit.DB.Analysis.SpatialFieldManager` · Revit 2024 · 28 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddSpatialFieldPrimitive | — | `` |
| Method | AddSpatialFieldPrimitive | 2011 | `public int AddSpatialFieldPrimitive ()` |
| Method | Clear | 2011 | `public void Clear ()` |
| Method | CreateSpatialFieldManager | 2011 | `public static SpatialFieldManager CreateSpatialFieldManager ( View view , int numberOfMeasurements )` |
| Method | GetLegend | 2011 | `public AnalysisDisplayLegend GetLegend ()` |
| Method | GetMaximum | 2012 | `public double GetMaximum ( int resultIndex , bool rawValue )` |
| Method | GetMinimum | 2012 | `public double GetMinimum ( int resultIndex , bool rawValue )` |
| Method | GetRegisteredResults | 2012 | `public IList < int > GetRegisteredResults ()` |
| Method | GetResultSchema | 2012 | `public AnalysisResultSchema GetResultSchema ( int idx )` |
| Method | GetSpatialFieldManager | 2011 | `public static SpatialFieldManager GetSpatialFieldManager ( View view )` |
| Method | IsResultSchemaNameUnique | 2011 | `public bool IsResultSchemaNameUnique ( string name , int resultIndexToSkip )` |
| Method | IsTextTypeIdValid | 2012 | `public static bool IsTextTypeIdValid ( ElementId textTypeId , Document doc )` |
| Method | RegisterResult | 2012 | `public int RegisterResult ( AnalysisResultSchema resultSchema )` |
| Method | RemoveSpatialFieldPrimitive | 2011 | `public void RemoveSpatialFieldPrimitive ( int idx )` |
| Method | SetMeasurementDescriptions | 2012 | `public void SetMeasurementDescriptions ( IList < string > measurementDescriptions )` |
| Method | SetMeasurementNames | 2011 | `public void SetMeasurementNames ( IList < string > measurementNames )` |
| Method | SetResultSchema | 2012 | `public void SetResultSchema ( int idx , AnalysisResultSchema resultSchema )` |
| Method | UpdateSpatialFieldPrimitive | 2012 | `public void UpdateSpatialFieldPrimitive ( int idx , FieldDomainPoints fieldDomainPoints , FieldValues fieldValues , int resultIndex )` |
| Property | AllowInteractiveSettings | 2021 | `public bool AllowInteractiveSettings { get ; set ; }` |
| Property | CurrentMeasurement | 2011 | `public int CurrentMeasurement { get ; set ; }` |
| Property | LegendPosition | 2012 | `public XYZ LegendPosition { get ; set ; }` |
| Property | LegendShowConfigurationName | 2012 | `public bool LegendShowConfigurationName { get ; set ; }` |
| Property | LegendShowDescription | 2012 | `public bool LegendShowDescription { get ; set ; }` |
| Property | LegendTextTypeId | 2012 | `public ElementId LegendTextTypeId { get ; set ; }` |
| Property | NumberOfMeasurements | 2011 | `public int NumberOfMeasurements { get ; }` |
| Property | Parameter | — | `` |
| Property | ResultsVisibleInView | 2012 | `public bool ResultsVisibleInView { get ; set ; }` |
| Property | UseRangeForAllMeasurements | 2011 | `public bool UseRangeForAllMeasurements { get ; set ; }` |