---
type: PointCloudEngineRegistry
namespace: Autodesk.Revit.DB.PointClouds
version: 2024
members: 4
tags: [revit-api, class]
---

# PointCloudEngineRegistry

`Autodesk.Revit.DB.PointClouds.PointCloudEngineRegistry` · Revit 2024 · 4 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetSupportedEngines | 2012 | `public static IList < string > GetSupportedEngines ()` |
| Method | IsEngineFileBased | 2012 | `public static bool IsEngineFileBased ( string identifier )` |
| Method | RegisterPointCloudEngine | 2012 | `public static void RegisterPointCloudEngine ( string identifier , IPointCloudEngine engine , bool isFileBased )` |
| Method | UnregisterPointCloudEngine | 2012 | `public static void UnregisterPointCloudEngine ( string identifier )` |