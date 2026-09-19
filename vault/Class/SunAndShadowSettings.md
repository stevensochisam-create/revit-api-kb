---
type: SunAndShadowSettings
namespace: Autodesk.Revit.DB
version: 2024
members: 37
tags: [revit-api, class]
---

# SunAndShadowSettings

`Autodesk.Revit.DB.SunAndShadowSettings` · Revit 2024 · 37 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CalculateTimeZone | 2012 | `public static double CalculateTimeZone ( double latitude , double longitude )` |
| Method | FitToModel | 2011 | `public void FitToModel ()` |
| Method | GetActiveSunAndShadowSettings | 2011 | `public static Element GetActiveSunAndShadowSettings ( Document aDocument )` |
| Method | GetFrameAltitude | 2011 | `public double GetFrameAltitude ( double frame )` |
| Method | GetFrameAzimuth | 2011 | `public double GetFrameAzimuth ( double frame )` |
| Method | GetFrameTime | 2011 | `public DateTime GetFrameTime ( double frame )` |
| Method | GetMatchingPreset | 2011 | `public string GetMatchingPreset ()` |
| Method | GetSunrise | 2011 | `public DateTime GetSunrise ( DateTime date )` |
| Method | GetSunset | 2011 | `public DateTime GetSunset ( DateTime date )` |
| Method | IsAfterStartDateAndTime | 2011 | `public bool IsAfterStartDateAndTime ( DateTime time )` |
| Method | IsBeforeEndDateAndTime | 2011 | `public bool IsBeforeEndDateAndTime ( DateTime time )` |
| Method | IsFrameValid | 2011 | `public bool IsFrameValid ( double frame )` |
| Method | IsGroundPlaneLevelValid | 2011 | `public bool IsGroundPlaneLevelValid ( ElementId levelId )` |
| Method | IsTimeIntervalValid | 2011 | `public bool IsTimeIntervalValid ( SunStudyTimeInterval interval )` |
| Property | ActiveFrame | 2011 | `public double ActiveFrame { get ; set ; }` |
| Property | ActiveFrameTime | 2011 | `public DateTime ActiveFrameTime { get ; }` |
| Property | Altitude | 2011 | `public double Altitude { get ; set ; }` |
| Property | Azimuth | 2011 | `public double Azimuth { get ; set ; }` |
| Property | EndDateAndTime | 2011 | `public DateTime EndDateAndTime { get ; set ; }` |
| Property | GroundPlaneHeight | 2011 | `public double GroundPlaneHeight { get ; }` |
| Property | GroundPlaneLevelId | 2011 | `public ElementId GroundPlaneLevelId { get ; set ; }` |
| Property | Latitude | 2011 | `public double Latitude { get ; }` |
| Property | Longitude | 2011 | `public double Longitude { get ; }` |
| Property | NumberOfFrames | 2011 | `public double NumberOfFrames { get ; }` |
| Property | Parameter | — | `` |
| Property | ProjectLocationId | 2011 | `public ElementId ProjectLocationId { get ; }` |
| Property | ProjectLocationName | 2011 | `public string ProjectLocationName { get ; }` |
| Property | RelativeToView | 2011 | `public bool RelativeToView { get ; set ; }` |
| Property | SharesSettings | 2011 | `public bool SharesSettings { get ; set ; }` |
| Property | StartDateAndTime | 2011 | `public DateTime StartDateAndTime { get ; set ; }` |
| Property | SunAndShadowType | 2011 | `public SunAndShadowType SunAndShadowType { get ; set ; }` |
| Property | SunriseToSunset | 2011 | `public bool SunriseToSunset { get ; set ; }` |
| Property | TimeInterval | 2011 | `public SunStudyTimeInterval TimeInterval { get ; set ; }` |
| Property | TimeZone | 2011 | `public double TimeZone { get ; }` |
| Property | UsesDST | 2011 | `public bool UsesDST { get ; }` |
| Property | UsesGroundPlane | 2011 | `public bool UsesGroundPlane { get ; set ; }` |
| Property | Visible | 2011 | `public bool Visible { get ; set ; }` |