---
type: SiteLocation
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# SiteLocation

`Autodesk.Revit.DB.SiteLocation` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ConvertFromProjectTime | — | `public DateTime ConvertFromProjectTime ( DateTime projectTime )` |
| Method | ConvertToProjectTime | — | `public DateTime ConvertToProjectTime ( DateTime inputTime )` |
| Method | IsCompatibleWith | 2018 | `public bool IsCompatibleWith ( SiteLocation otherSiteLocation )` |
| Method | SetGeoCoordinateSystem | 2019.2 | `public void SetGeoCoordinateSystem ( string coordSystem )` |
| Property | Elevation | 2014 UR2 | `public double Elevation { get ; }` |
| Property | GeoCoordinateSystemDefinition | 2018 | `public string GeoCoordinateSystemDefinition { get ; }` |
| Property | GeoCoordinateSystemId | 2018 | `public string GeoCoordinateSystemId { get ; }` |
| Property | Latitude | — | `public double Latitude { get ; set ; }` |
| Property | Longitude | — | `public double Longitude { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | PlaceName | 2013 | `public string PlaceName { get ; set ; }` |
| Property | TimeZone | — | `public double TimeZone { get ; set ; }` |
| Property | WeatherStationName | 2014 UR2 | `public string WeatherStationName { get ; }` |