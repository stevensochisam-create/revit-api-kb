---
type: PipeSettings
namespace: Autodesk.Revit.DB.Plumbing
version: 2024
members: 27
tags: [revit-api, class]
---

# PipeSettings

`Autodesk.Revit.DB.Plumbing.PipeSettings` · Revit 2024 · 27 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddPipeSlope | 2012 | `public void AddPipeSlope ( double slope )` |
| Method | GetFlowConvertionServerInfo | 2012 | `public MEPCalculationServerInfo GetFlowConvertionServerInfo ()` |
| Method | GetPipeSettings | 2012 | `public static PipeSettings GetPipeSettings ( Document document )` |
| Method | GetPipeSlopes | 2012 | `public IList < double > GetPipeSlopes ()` |
| Method | GetSpecificFittingAngleStatus | 2014 | `public bool GetSpecificFittingAngleStatus ( double angle )` |
| Method | GetSpecificFittingAngles | 2014 | `public IList < double > GetSpecificFittingAngles ()` |
| Method | IsAnalysisForClosedLoopHydronicPipingNetworksEnabled | 2012 | `public static bool IsAnalysisForClosedLoopHydronicPipingNetworksEnabled ( Document ccda )` |
| Method | IsValidSpecificFittingAngle | 2012 | `public bool IsValidSpecificFittingAngle ( double angle )` |
| Method | SetFlowConvertionServerInfo | 2012 | `public void SetFlowConvertionServerInfo ( MEPCalculationServerInfo serverInfo )` |
| Method | SetPipeSlopes | 2012 | `public void SetPipeSlopes ( IList < double > slopes )` |
| Method | SetSpecificFittingAngleStatus | 2014 | `public void SetSpecificFittingAngleStatus ( double angle , bool bStatus )` |
| Property | AnalysisForClosedLoopHydronicPipingNetworks | 2018 | `public bool AnalysisForClosedLoopHydronicPipingNetworks { get ; set ; }` |
| Property | Centerline | 2017 | `public string Centerline { get ; set ; }` |
| Property | ConnectorSeparator | 2012 | `public string ConnectorSeparator { get ; set ; }` |
| Property | ConnectorTolerance | 2012 | `public double ConnectorTolerance { get ; set ; }` |
| Property | FittingAngleUsage | 2014 | `public FittingAngleUsage FittingAngleUsage { get ; set ; }` |
| Property | FittingAnnotationSize | 2012 | `public double FittingAnnotationSize { get ; set ; }` |
| Property | FlatOnBottom | 2017 | `public string FlatOnBottom { get ; set ; }` |
| Property | FlatOnTop | 2017 | `public string FlatOnTop { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | SetDown | 2017 | `public string SetDown { get ; set ; }` |
| Property | SetDownFromBottom | 2019 | `public string SetDownFromBottom { get ; set ; }` |
| Property | SetUp | 2017 | `public string SetUp { get ; set ; }` |
| Property | SetUpFromBottom | 2019 | `public string SetUpFromBottom { get ; set ; }` |
| Property | SizePrefix | 2012 | `public string SizePrefix { get ; set ; }` |
| Property | SizeSuffix | 2012 | `public string SizeSuffix { get ; set ; }` |
| Property | UseAnnotationScaleForSingleLineFittings | 2012 | `public bool UseAnnotationScaleForSingleLineFittings { get ; set ; }` |