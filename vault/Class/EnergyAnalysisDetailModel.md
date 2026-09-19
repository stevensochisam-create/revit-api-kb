---
type: EnergyAnalysisDetailModel
namespace: Autodesk.Revit.DB.Analysis
version: 2024
members: 14
tags: [revit-api, class]
---

# EnergyAnalysisDetailModel

`Autodesk.Revit.DB.Analysis.EnergyAnalysisDetailModel` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2012 | `public static EnergyAnalysisDetailModel Create ( Document document , EnergyAnalysisDetailModelOptions options )` |
| Method | GetAnalyticalOpenings | 2012 | `public IList < EnergyAnalysisOpening > GetAnalyticalOpenings ()` |
| Method | GetAnalyticalShadingSurfaces | 2012 | `public IList < EnergyAnalysisSurface > GetAnalyticalShadingSurfaces ()` |
| Method | GetAnalyticalSpaces | 2012 | `public IList < EnergyAnalysisSpace > GetAnalyticalSpaces ()` |
| Method | GetAnalyticalSurfaces | 2012 | `public IList < EnergyAnalysisSurface > GetAnalyticalSurfaces ()` |
| Method | GetMainEnergyAnalysisDetailModel | 2012 | `public static EnergyAnalysisDetailModel GetMainEnergyAnalysisDetailModel ( Document document )` |
| Method | TransformModel | 2012 | `public void TransformModel ()` |
| Property | BuildingTypeId | 2012 | `public ElementId BuildingTypeId { get ; set ; }` |
| Property | ExportCategory | 2012 | `public ElementId ExportCategory { get ; set ; }` |
| Property | ExportMullions | 2012 | `public bool ExportMullions { get ; }` |
| Property | IncludeShadingSurfaces | 2012 | `public bool IncludeShadingSurfaces { get ; }` |
| Property | Parameter | — | `` |
| Property | SimplifyCurtainSystems | 2012 | `public bool SimplifyCurtainSystems { get ; }` |
| Property | Tier | 2012 | `public EnergyAnalysisDetailModelTier Tier { get ; }` |