---
type: ModelPathUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 6
tags: [revit-api, class]
---

# ModelPathUtils

`Autodesk.Revit.DB.ModelPathUtils` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ConvertCloudGUIDsToCloudPath | 2021 | `public static ModelPath ConvertCloudGUIDsToCloudPath ( string region , Guid projectGuid , Guid modelGuid )` |
| Method | ConvertModelPathToUserVisiblePath | 2012 | `public static string ConvertModelPathToUserVisiblePath ( ModelPath path )` |
| Method | ConvertUserVisiblePathToModelPath | 2012 | `public static ModelPath ConvertUserVisiblePathToModelPath ( string strPath )` |
| Method | IsValidUserVisibleFullServerPath | 2012 | `public static bool IsValidUserVisibleFullServerPath ( string strPath )` |
| Property | CloudRegionEMEA | 2021 | `public static string CloudRegionEMEA { get ; }` |
| Property | CloudRegionUS | 2021 | `public static string CloudRegionUS { get ; }` |