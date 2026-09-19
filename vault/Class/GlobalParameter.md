---
type: GlobalParameter
namespace: Autodesk.Revit.DB
version: 2024
members: 20
tags: [revit-api, class]
---

# GlobalParameter

`Autodesk.Revit.DB.GlobalParameter` · Revit 2024 · 20 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanChangeReporting | 2017 | `public bool CanChangeReporting ()` |
| Method | CanLabelDimension | 2016 Subscription Update | `public bool CanLabelDimension ( ElementId dimensionId )` |
| Method | Create | 2016 Subscription Update | `public static GlobalParameter Create ( Document document , string name , ForgeTypeId specTypeId )` |
| Method | GetAffectedElements | 2016 Subscription Update | `public ISet < ElementId > GetAffectedElements ()` |
| Method | GetAffectedGlobalParameters | 2016 Subscription Update | `public ISet < ElementId > GetAffectedGlobalParameters ()` |
| Method | GetFormula | 2016 Subscription Update | `public string GetFormula ()` |
| Method | GetLabelName | 2016 Subscription Update | `public string GetLabelName ()` |
| Method | GetLabeledDimensions | 2016 Subscription Update | `public ISet < ElementId > GetLabeledDimensions ()` |
| Method | GetValue | 2016 Subscription Update | `public ParameterValue GetValue ()` |
| Method | HasValidTypeForReporting | 2016 Subscription Update | `public bool HasValidTypeForReporting ()` |
| Method | IsValidFormula | 2016 Subscription Update | `public bool IsValidFormula ( string expression )` |
| Method | LabelDimension | 2016 Subscription Update | `public void LabelDimension ( ElementId dimensionId )` |
| Method | SetDrivingDimension | 2016 Subscription Update | `public void SetDrivingDimension ( ElementId dimensionId )` |
| Method | SetFormula | 2016 Subscription Update | `public void SetFormula ( string expression )` |
| Method | SetValue | 2016 Subscription Update | `public void SetValue ( ParameterValue value )` |
| Method | UnlabelDimension | 2016 Subscription Update | `public void UnlabelDimension ( ElementId dimensionId )` |
| Property | IsDrivenByDimension | 2016 Subscription Update | `public bool IsDrivenByDimension { get ; }` |
| Property | IsDrivenByFormula | 2016 Subscription Update | `public bool IsDrivenByFormula { get ; }` |
| Property | IsReporting | 2016 Subscription Update | `public bool IsReporting { get ; set ; }` |
| Property | Parameter | — | `` |