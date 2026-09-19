---
type: RoutingPreferenceRule
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# RoutingPreferenceRule

`Autodesk.Revit.DB.RoutingPreferenceRule` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | RoutingPreferenceRule | 2013 | `public RoutingPreferenceRule ( ElementId MEPPartId , string description )` |
| Method | AddCriterion | 2013 | `public void AddCriterion ( RoutingCriterionBase myCriterion )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCriterion | 2013 | `public RoutingCriterionBase GetCriterion ( int index )` |
| Method | RemoveCriteron | 2013 | `public void RemoveCriteron ( int index )` |
| Property | Description | 2013 | `public string Description { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | MEPPartId | 2013 | `public ElementId MEPPartId { get ; }` |
| Property | NumberOfCriteria | 2013 | `public int NumberOfCriteria { get ; }` |
| Property | RoutingPreferenceManager | 2013 | `public RoutingPreferenceManager RoutingPreferenceManager { get ; }` |