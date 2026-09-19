---
type: ParameterUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# ParameterUtils

`Autodesk.Revit.DB.ParameterUtils` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | DownloadCompanyName | 2024 | `public static string DownloadCompanyName ( Document document , ForgeTypeId parameterTypeId )` |
| Method | DownloadParameter | 2024 | `public static SharedParameterElement DownloadParameter ( Document document , ParameterDownloadOptions options , ForgeTypeId parameterTypeId )` |
| Method | DownloadParameterOptions | 2024 | `public static ParameterDownloadOptions DownloadParameterOptions ( ForgeTypeId parameterTypeId )` |
| Method | GetAllBuiltInGroups | 2022 | `public static IList < ForgeTypeId > GetAllBuiltInGroups ()` |
| Method | GetAllBuiltInParameters | 2022 | `public static IList < ForgeTypeId > GetAllBuiltInParameters ()` |
| Method | GetBuiltInParameter | — | `public static BuiltInParameter GetBuiltInParameter ( ForgeTypeId parameterTypeId )` |
| Method | GetBuiltInParameterGroup | — | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 and may be removed in a future version of Revit. Please use members of the `GroupTypeId` class instead.")] public static BuiltInParameterGroup GetBuiltInParam` |
| Method | GetParameterGroupTypeId | — | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 and may be removed in a future version of Revit. Please use members of the `GroupTypeId` class instead.")] public static ForgeTypeId GetParameterGroupTypeId (` |
| Method | GetParameterTypeId | — | `public static ForgeTypeId GetParameterTypeId ( BuiltInParameter builtInParam )` |
| Method | IsBuiltInGroup | 2022 | `public static bool IsBuiltInGroup ( ForgeTypeId groupTypeId )` |
| Method | IsBuiltInParameter | — | `` |