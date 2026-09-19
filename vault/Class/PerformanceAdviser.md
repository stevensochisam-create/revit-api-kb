---
type: PerformanceAdviser
namespace: Autodesk.Revit.DB
version: 2024
members: 17
tags: [revit-api, class]
---

# PerformanceAdviser

`Autodesk.Revit.DB.PerformanceAdviser` · Revit 2024 · 17 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddRule | 2012 | `public void AddRule ( PerformanceAdviserRuleId id , IPerformanceAdviserRule rule )` |
| Method | DeleteRule | 2012 | `public void DeleteRule ( PerformanceAdviserRuleId id )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | ExecuteAllRules | 2012 | `public IList < FailureMessage > ExecuteAllRules ( Document document )` |
| Method | ExecuteRules | — | `` |
| Method | GetAllRuleIds | 2012 | `public IList < PerformanceAdviserRuleId > GetAllRuleIds ()` |
| Method | GetElementFilterFromRule | — | `` |
| Method | GetNumberOfRules | 2012 | `public int GetNumberOfRules ()` |
| Method | GetPerformanceAdviser | 2012 | `public static PerformanceAdviser GetPerformanceAdviser ()` |
| Method | GetRuleDescription | — | `` |
| Method | GetRuleId | 2012 | `public PerformanceAdviserRuleId GetRuleId ( int index )` |
| Method | GetRuleName | — | `` |
| Method | IsRuleEnabled | — | `` |
| Method | PostWarning | 2012 | `public void PostWarning ( FailureMessage message )` |
| Method | SetRuleEnabled | — | `` |
| Method | WillRuleCheckElements | — | `` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |