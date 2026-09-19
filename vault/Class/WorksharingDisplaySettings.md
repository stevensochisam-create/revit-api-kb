---
type: WorksharingDisplaySettings
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# WorksharingDisplaySettings

`Autodesk.Revit.DB.WorksharingDisplaySettings` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanUserHaveOverrides | 2012 | `public bool CanUserHaveOverrides ( string username )` |
| Method | GetAllUsersWithGraphicOverrides | 2012 | `public ICollection < string > GetAllUsersWithGraphicOverrides ()` |
| Method | GetGraphicOverrides | — | `` |
| Method | GetOrCreateWorksharingDisplaySettings | 2012 | `public static WorksharingDisplaySettings GetOrCreateWorksharingDisplaySettings ( Document doc )` |
| Method | GetRemovedUsers | 2012 | `public ICollection < string > GetRemovedUsers ()` |
| Method | RemoveUsers | 2012 | `public void RemoveUsers ( Document document , ICollection < string > usersToRemove , out ICollection < string > usersActuallyRemoved )` |
| Method | RestoreUsers | 2012 | `public int RestoreUsers ( ICollection < string > usersToRestore )` |
| Method | SetGraphicOverrides | — | `` |
| Method | UserHasGraphicOverrides | 2012 | `public bool UserHasGraphicOverrides ( string username )` |
| Property | Parameter | — | `` |