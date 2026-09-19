---
type: LightGroupManager
namespace: Autodesk.Revit.DB.Lighting
version: 2024
members: 12
tags: [revit-api, class]
---

# LightGroupManager

`Autodesk.Revit.DB.Lighting.LightGroupManager` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateGroup | 2013 | `public LightGroup CreateGroup ( string name )` |
| Method | DeleteGroup | 2013 | `public void DeleteGroup ( ElementId groupId )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetGroups | 2013 | `public IList < LightGroup > GetGroups ()` |
| Method | GetLightDimmer | 2013 | `public double GetLightDimmer ( ElementId viewId , ElementId lightId )` |
| Method | GetLightGroupManager | 2013 | `public static LightGroupManager GetLightGroupManager ( Document document )` |
| Method | IsLightGroupOn | 2013 | `public bool IsLightGroupOn ( ElementId viewId , ElementId groupId )` |
| Method | IsLightOn | 2013 | `public bool IsLightOn ( ElementId viewId , ElementId lightId )` |
| Method | SetLightDimmer | 2013 | `public void SetLightDimmer ( ElementId viewId , ElementId lightId , double dimmingValue )` |
| Method | SetLightGroupOn | 2013 | `public void SetLightGroupOn ( ElementId viewId , ElementId groupId , bool turnOn )` |
| Method | SetLightOn | 2013 | `public void SetLightOn ( ElementId viewId , ElementId lightId , bool turnOn )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |