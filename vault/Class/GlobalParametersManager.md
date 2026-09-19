---
type: GlobalParametersManager
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# GlobalParametersManager

`Autodesk.Revit.DB.GlobalParametersManager` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreGlobalParametersAllowed | 2016 Subscription Update | `public static bool AreGlobalParametersAllowed ( Document document )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | FindByName | 2016 Subscription Update | `public static ElementId FindByName ( Document document , string name )` |
| Method | GetAllGlobalParameters | 2016 Subscription Update | `public static ISet < ElementId > GetAllGlobalParameters ( Document document )` |
| Method | GetGlobalParametersOrdered | 2017 | `public static IList < ElementId > GetGlobalParametersOrdered ( Document document )` |
| Method | IsUniqueName | 2016 Subscription Update | `public static bool IsUniqueName ( Document document , string name )` |
| Method | IsValidGlobalParameter | 2016 Subscription Update | `public static bool IsValidGlobalParameter ( Document document , ElementId parameterId )` |
| Method | MoveParameterDownOrder | 2017 | `public static bool MoveParameterDownOrder ( Document document , ElementId parameterId )` |
| Method | MoveParameterUpOrder | 2017 | `public static bool MoveParameterUpOrder ( Document document , ElementId parameterId )` |
| Method | SortParameters | 2017 | `public static void SortParameters ( Document document , ParametersOrder order )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |