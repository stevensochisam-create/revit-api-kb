---
type: WorksetTable
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# WorksetTable

`Autodesk.Revit.DB.WorksetTable` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanDeleteWorkset | 2022.1 | `public static bool CanDeleteWorkset ( Document document , WorksetId worksetId , DeleteWorksetSettings deleteWorksetSettings )` |
| Method | DeleteWorkset | 2022.1 | `public static void DeleteWorkset ( Document document , WorksetId worksetId , DeleteWorksetSettings deleteWorksetSettings )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetActiveWorksetId | 2012 | `public WorksetId GetActiveWorksetId ()` |
| Method | GetWorkset | — | `` |
| Method | IsWorksetNameUnique | 2015 Subscription Update | `public static bool IsWorksetNameUnique ( Document aDoc , string name )` |
| Method | RenameWorkset | 2015 Subscription Update | `public static void RenameWorkset ( Document aDoc , WorksetId worksetId , string name )` |
| Method | SetActiveWorksetId | 2015 Subscription Update | `public void SetActiveWorksetId ( WorksetId worksetId )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |