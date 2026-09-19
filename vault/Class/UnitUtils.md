---
type: UnitUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# UnitUtils

`Autodesk.Revit.DB.UnitUtils` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Convert | 2014 | `public static double Convert ( double value , ForgeTypeId currentUnitTypeId , ForgeTypeId desiredUnitTypeId )` |
| Method | ConvertFromInternalUnits | 2014 | `public static double ConvertFromInternalUnits ( double value , ForgeTypeId unitTypeId )` |
| Method | ConvertToInternalUnits | 2014 | `public static double ConvertToInternalUnits ( double value , ForgeTypeId unitTypeId )` |
| Method | GetAllDisciplines | 2014 | `public static IList < ForgeTypeId > GetAllDisciplines ()` |
| Method | GetAllMeasurableSpecs | 2014 | `public static IList < ForgeTypeId > GetAllMeasurableSpecs ()` |
| Method | GetAllUnits | 2014 | `public static IList < ForgeTypeId > GetAllUnits ()` |
| Method | GetDiscipline | 2014 | `public static ForgeTypeId GetDiscipline ( ForgeTypeId specTypeId )` |
| Method | GetTypeCatalogStringForSpec | 2014 | `public static string GetTypeCatalogStringForSpec ( ForgeTypeId specTypeId )` |
| Method | GetTypeCatalogStringForUnit | 2014 | `public static string GetTypeCatalogStringForUnit ( ForgeTypeId unitTypeId )` |
| Method | GetValidUnits | 2014 | `public static IList < ForgeTypeId > GetValidUnits ( ForgeTypeId specTypeId )` |
| Method | IsMeasurableSpec | 2014 | `public static bool IsMeasurableSpec ( ForgeTypeId specTypeId )` |
| Method | IsSymbol | 2014 | `public static bool IsSymbol ( ForgeTypeId symbolTypeId )` |
| Method | IsUnit | 2014 | `public static bool IsUnit ( ForgeTypeId unitTypeId )` |
| Method | IsValidUnit | 2014 | `public static bool IsValidUnit ( ForgeTypeId specTypeId , ForgeTypeId unitTypeId )` |