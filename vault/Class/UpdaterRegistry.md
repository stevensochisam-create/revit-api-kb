---
type: UpdaterRegistry
namespace: Autodesk.Revit.DB
version: 2024
members: 16
tags: [revit-api, class]
---

# UpdaterRegistry

`Autodesk.Revit.DB.UpdaterRegistry` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddTrigger | — | `` |
| Method | DisableUpdater | 2015 | `public static void DisableUpdater ( UpdaterId id )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | EnableUpdater | 2015 | `public static void EnableUpdater ( UpdaterId id )` |
| Method | GetIsUpdaterOptional | 2011 | `public static bool GetIsUpdaterOptional ( UpdaterId id )` |
| Method | GetRegisteredUpdaterInfos | — | `` |
| Method | GetRegisteredUpdaterInfos | 2011 | `public static IList < UpdaterInfo > GetRegisteredUpdaterInfos ()` |
| Method | IsUpdaterEnabled | 2015 | `public static bool IsUpdaterEnabled ( UpdaterId id )` |
| Method | IsUpdaterRegistered | — | `` |
| Method | RegisterUpdater | — | `` |
| Method | RemoveAllTriggers | 2011 | `public static void RemoveAllTriggers ( UpdaterId id )` |
| Method | RemoveDocumentTriggers | 2011 | `public static void RemoveDocumentTriggers ( UpdaterId id , Document document )` |
| Method | SetExecutionOrder | 2011 | `public static void SetExecutionOrder ( UpdaterId first , UpdaterId second )` |
| Method | SetIsUpdaterOptional | 2011 | `public static void SetIsUpdaterOptional ( UpdaterId id , bool isOptional )` |
| Method | UnregisterUpdater | — | `` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |