---
type: EnergyDataSettings
namespace: Autodesk.Revit.DB.Analysis
version: 2024
members: 64
tags: [revit-api, class]
---

# EnergyDataSettings

`Autodesk.Revit.DB.Analysis.EnergyDataSettings` · Revit 2024 · 64 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CheckAnalysisType | 2011 | `public static bool CheckAnalysisType ( AnalysisMode analysisType )` |
| Method | CheckBuildingConstructionClass | 2011 | `public static bool CheckBuildingConstructionClass ( HVACLoadConstructionClass buildingConstructionClass )` |
| Method | CheckBuildingEnvelope | 2015 | `public static bool CheckBuildingEnvelope ( gbXMLExportBuildingEnvelope determinationMethod )` |
| Method | CheckBuildingHVACSystem | 2011 | `public static bool CheckBuildingHVACSystem ( gbXMLBuildingHVACSystem buildingHVACSystem )` |
| Method | CheckBuildingOperatingSchedule | 2011 | `public static bool CheckBuildingOperatingSchedule ( gbXMLBuildingOperatingSchedule buildingOperatingSchedule )` |
| Method | CheckBuildingType | 2011 | `public static bool CheckBuildingType ( gbXMLBuildingType buildingType )` |
| Method | CheckConstructionSetElement | 2011 | `public bool CheckConstructionSetElement ( ElementId constructionSetElementId )` |
| Method | CheckExportCategory | 2011 | `public static bool CheckExportCategory ( ElementId exportCategoryId )` |
| Method | CheckExportComplexity | 2011 | `public static bool CheckExportComplexity ( gbXMLExportComplexity exportComplexity )` |
| Method | CheckGroundPlane | — | `` |
| Method | CheckProjectPhase | 2011 | `public bool CheckProjectPhase ( ElementId projectPhaseId )` |
| Method | CheckProjectReportType | 2011 | `public static bool CheckProjectReportType ( HVACLoadLoadsReportType projectReportType )` |
| Method | CheckRangeOfPercentageGlazing | 2011 | `public static bool CheckRangeOfPercentageGlazing ( double percentageGlazing )` |
| Method | CheckRangeOfPercentageSkylights | 2011 | `public static bool CheckRangeOfPercentageSkylights ( double percentageSkylights )` |
| Method | CheckRangeOfShadeDepth | 2011 | `public static bool CheckRangeOfShadeDepth ( double shadeDepth )` |
| Method | CheckRangeOfSillHeight | 2011 | `public static bool CheckRangeOfSillHeight ( double sillHeight )` |
| Method | CheckRangeOfSkylightWidth | 2011 | `public static bool CheckRangeOfSkylightWidth ( double skylightWidth )` |
| Method | CheckRangeOfSliverSpaceTolerance | 2011 | `public static bool CheckRangeOfSliverSpaceTolerance ( double silverSpaceTolerance )` |
| Method | CheckServiceType | 2011 | `public static bool CheckServiceType ( gbXMLServiceType serviceType )` |
| Method | GetBuildingConstructionSetElementId | 2011 | `public static ElementId GetBuildingConstructionSetElementId ( Document ccda )` |
| Method | GetFromDocument | 2011 | `public static EnergyDataSettings GetFromDocument ( Document cda )` |
| Method | GetReportsFolderParsed | 2022 | `public string GetReportsFolderParsed ()` |
| Method | IsDocumentUsingEnergyDataAnalyticalModel | 2011 | `public static bool IsDocumentUsingEnergyDataAnalyticalModel ( Document ccda )` |
| Method | SetReportsFolder | 2022 | `public void SetReportsFolder ( string folderPath )` |
| Property | AnalysisType | 2011 | `public AnalysisMode AnalysisType { get ; set ; }` |
| Property | AnalyticalGridCellSize | 2015 | `public double AnalyticalGridCellSize { get ; set ; }` |
| Property | BuildingConstructionClass | 2011 | `public HVACLoadConstructionClass BuildingConstructionClass { get ; set ; }` |
| Property | BuildingEnvelopeDeterminationMethod | 2015 | `public gbXMLExportBuildingEnvelope BuildingEnvelopeDeterminationMethod { get ; set ; }` |
| Property | BuildingHVACSystem | 2011 | `public gbXMLBuildingHVACSystem BuildingHVACSystem { get ; set ; }` |
| Property | BuildingOperatingSchedule | 2011 | `public gbXMLBuildingOperatingSchedule BuildingOperatingSchedule { get ; set ; }` |
| Property | BuildingType | 2011 | `public gbXMLBuildingType BuildingType { get ; set ; }` |
| Property | BuildingTypeId | 2011 | `public ElementId BuildingTypeId { get ; set ; }` |
| Property | CoreOffset | 2011 | `public double CoreOffset { get ; set ; }` |
| Property | CreateAnalyticalModel | 2011 | `public bool CreateAnalyticalModel { get ; }` |
| Property | DividePerimeter | 2011 | `public bool DividePerimeter { get ; set ; }` |
| Property | EnergyModel | 2011 | `public bool EnergyModel { get ; set ; }` |
| Property | ExportCategory | 2011 | `public ElementId ExportCategory { get ; set ; }` |
| Property | ExportComplexity | 2011 | `public gbXMLExportComplexity ExportComplexity { get ; set ; }` |
| Property | ExportDefaults | 2011 | `public bool ExportDefaults { get ; set ; }` |
| Property | GroundPlane | 2011 | `public ElementId GroundPlane { get ; set ; }` |
| Property | IncludeThermalProperties | 2011 | `public bool IncludeThermalProperties { get ; set ; }` |
| Property | IsExportMullionsEnabled | 2011 | `public bool IsExportMullionsEnabled { get ; }` |
| Property | IsExportShadingSurfacesEnabled | 2011 | `public bool IsExportShadingSurfacesEnabled { get ; }` |
| Property | IsExportSimplifiedCurtainSystemsEnabled | 2011 | `public bool IsExportSimplifiedCurtainSystemsEnabled { get ; }` |
| Property | IsGlazingShaded | 2011 | `public bool IsGlazingShaded { get ; set ; }` |
| Property | OutsideAirChangesRatePerHour | 2011 | `public double OutsideAirChangesRatePerHour { get ; set ; }` |
| Property | OutsideAirPerArea | 2011 | `public double OutsideAirPerArea { get ; set ; }` |
| Property | OutsideAirPerPerson | 2011 | `public double OutsideAirPerPerson { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | PercentageGlazing | 2011 | `public double PercentageGlazing { get ; set ; }` |
| Property | PercentageSkylights | 2011 | `public double PercentageSkylights { get ; set ; }` |
| Property | ProjectPhase | 2011 | `public ElementId ProjectPhase { get ; set ; }` |
| Property | ProjectReportType | 2011 | `public HVACLoadLoadsReportType ProjectReportType { get ; set ; }` |
| Property | ReportsFolder | 2011 | `public string ReportsFolder { get ; }` |
| Property | ServiceType | 2011 | `public gbXMLServiceType ServiceType { get ; set ; }` |
| Property | ShadeDepth | 2011 | `public double ShadeDepth { get ; set ; }` |
| Property | SillHeight | 2011 | `public double SillHeight { get ; set ; }` |
| Property | SkylightWidth | 2011 | `public double SkylightWidth { get ; set ; }` |
| Property | SliverSpaceTolerance | 2011 | `public double SliverSpaceTolerance { get ; set ; }` |
| Property | UseAirChangesPerHour | 2011 | `public bool UseAirChangesPerHour { get ; set ; }` |
| Property | UseCurrentViewOnly | 2024 | `public bool UseCurrentViewOnly { get ; set ; }` |
| Property | UseHeatingCredits | 2011 | `public bool UseHeatingCredits { get ; set ; }` |
| Property | UseOutsideAirPerArea | 2011 | `public bool UseOutsideAirPerArea { get ; set ; }` |
| Property | UseOutsideAirPerPerson | 2011 | `public bool UseOutsideAirPerPerson { get ; set ; }` |