---
type: ViewPlan
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# ViewPlan

`Autodesk.Revit.DB.ViewPlan` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CheckPlanViewRangeValidity | 2013 | `public IList < PlanViewRangeError > CheckPlanViewRangeValidity ( PlanViewRange planViewRange )` |
| Method | Create | 2013 | `public static ViewPlan Create ( Document document , ElementId viewFamilyTypeId , ElementId levelId )` |
| Method | CreateAreaPlan | 2013 | `public static ViewPlan CreateAreaPlan ( Document document , ElementId areaSchemeId , ElementId levelId )` |
| Method | GetUnderlayBaseLevel | 2017 | `public ElementId GetUnderlayBaseLevel ()` |
| Method | GetUnderlayOrientation | 2017 | `public UnderlayOrientation GetUnderlayOrientation ()` |
| Method | GetUnderlayTopLevel | 2017 | `public ElementId GetUnderlayTopLevel ()` |
| Method | GetViewRange | 2013 | `public PlanViewRange GetViewRange ()` |
| Method | Print | — | `` |
| Method | SetUnderlayBaseLevel | 2017 | `public void SetUnderlayBaseLevel ( ElementId levelId )` |
| Method | SetUnderlayOrientation | 2017 | `public void SetUnderlayOrientation ( UnderlayOrientation uo )` |
| Method | SetUnderlayRange | 2017 | `public void SetUnderlayRange ( ElementId baseLevelId , ElementId topLevelId )` |
| Method | SetViewRange | 2013 | `public void SetViewRange ( PlanViewRange planViewRange )` |
| Property | AreaScheme | — | `public AreaScheme AreaScheme { get ; }` |
| Property | Parameter | — | `` |