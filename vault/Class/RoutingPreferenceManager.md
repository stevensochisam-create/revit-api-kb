---
type: RoutingPreferenceManager
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# RoutingPreferenceManager

`Autodesk.Revit.DB.RoutingPreferenceManager` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddRule | — | `` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetMEPPartId | 2013 | `public ElementId GetMEPPartId ( RoutingPreferenceRuleGroupType groupType , RoutingConditions conditions )` |
| Method | GetNumberOfRules | 2013 | `public int GetNumberOfRules ( RoutingPreferenceRuleGroupType eGroupType )` |
| Method | GetRule | 2013 | `public RoutingPreferenceRule GetRule ( RoutingPreferenceRuleGroupType groupType , int index )` |
| Method | GetSharedSizes | 2013 | `public IList < ElementId > GetSharedSizes ( double size , ConnectorProfileType shape )` |
| Method | RemoveRule | 2013 | `public void RemoveRule ( RoutingPreferenceRuleGroupType groupType , int index )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | OwnerId | 2013 | `public ElementId OwnerId { get ; }` |
| Property | PreferredJunctionType | 2013 | `public PreferredJunctionType PreferredJunctionType { get ; set ; }` |