---
type: DuctSettings
namespace: Autodesk.Revit.DB.Mechanical
version: 2024
members: 30
tags: [revit-api, class]
---

# DuctSettings

`Autodesk.Revit.DB.Mechanical.DuctSettings` · Revit 2024 · 30 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetDuctSettings | 2014 | `public static DuctSettings GetDuctSettings ( Document document )` |
| Method | GetPressLossCalculationServerInfo | 2014 | `public MEPCalculationServerInfo GetPressLossCalculationServerInfo ()` |
| Method | GetSpecificFittingAngleStatus | 2014 | `public bool GetSpecificFittingAngleStatus ( double angle )` |
| Method | GetSpecificFittingAngles | 2014 | `public IList < double > GetSpecificFittingAngles ()` |
| Method | IsNetworkBasedCalculationsEnabled | 2014 | `public static bool IsNetworkBasedCalculationsEnabled ( Document document )` |
| Method | IsValidSpecificFittingAngle | 2014 | `public bool IsValidSpecificFittingAngle ( double angle )` |
| Method | SetPressLossCalculationServerInfo | 2014 | `public void SetPressLossCalculationServerInfo ( MEPCalculationServerInfo serverInfo )` |
| Method | SetSpecificFittingAngleStatus | 2014 | `public void SetSpecificFittingAngleStatus ( double angle , bool useInLayout )` |
| Property | AirDensity | 2014 | `public double AirDensity { get ; set ; }` |
| Property | AirViscosity | 2014 | `public double AirViscosity { get ; set ; }` |
| Property | Centerline | 2017 | `public string Centerline { get ; set ; }` |
| Property | ConnectorSeparator | 2014 | `public string ConnectorSeparator { get ; set ; }` |
| Property | FittingAngleUsage | 2014 | `public FittingAngleUsage FittingAngleUsage { get ; set ; }` |
| Property | FittingAnnotationSize | 2014 | `public double FittingAnnotationSize { get ; set ; }` |
| Property | FlatOnBottom | 2017 | `public string FlatOnBottom { get ; set ; }` |
| Property | FlatOnTop | 2017 | `public string FlatOnTop { get ; set ; }` |
| Property | NetworkBasedCalculations | 2024 | `public bool NetworkBasedCalculations { get ; set ; }` |
| Property | OvalDuctSizeSeparator | 2014 | `public string OvalDuctSizeSeparator { get ; set ; }` |
| Property | OvalDuctSizeSuffix | 2014 | `public string OvalDuctSizeSuffix { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | RectangularDuctSizeSeparator | 2014 | `public string RectangularDuctSizeSeparator { get ; set ; }` |
| Property | RectangularDuctSizeSuffix | 2014 | `public string RectangularDuctSizeSuffix { get ; set ; }` |
| Property | RiseDropAnnotationSize | 2014 | `public double RiseDropAnnotationSize { get ; set ; }` |
| Property | RoundDuctSizePrefix | 2014 | `public string RoundDuctSizePrefix { get ; set ; }` |
| Property | RoundDuctSizeSuffix | 2014 | `public string RoundDuctSizeSuffix { get ; set ; }` |
| Property | SetDown | 2017 | `public string SetDown { get ; set ; }` |
| Property | SetDownFromBottom | 2019 | `public string SetDownFromBottom { get ; set ; }` |
| Property | SetUp | 2017 | `public string SetUp { get ; set ; }` |
| Property | SetUpFromBottom | 2019 | `public string SetUpFromBottom { get ; set ; }` |
| Property | UseAnnotationScaleForSingleLineFittings | 2014 | `public bool UseAnnotationScaleForSingleLineFittings { get ; set ; }` |