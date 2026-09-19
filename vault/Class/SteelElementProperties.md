---
type: SteelElementProperties
namespace: Autodesk.Revit.DB.Steel
version: 2024
members: 6
tags: [revit-api, class]
---

# SteelElementProperties

`Autodesk.Revit.DB.Steel.SteelElementProperties` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddFabricationInformationForRevitElements | 2019 | `public static IList < ElementId > AddFabricationInformationForRevitElements ( Document aDoc , IList < ElementId > elementIds )` |
| Method | GetFabricationUniqueID | 2019 | `public static Guid GetFabricationUniqueID ( Document aDoc , Reference reference )` |
| Method | GetReference | 2019 | `public static Reference GetReference ( Document aDoc , Guid guid )` |
| Method | GetSteelElementProperties | 2019 | `public static SteelElementProperties GetSteelElementProperties ( Element pElement )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | UniqueID | 2019 | `public Guid UniqueID { get ; internal set ; }` |