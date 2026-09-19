---
type: RebarShape
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 21
tags: [revit-api, class]
---

# RebarShape

`Autodesk.Revit.DB.Structure.RebarShape` · Revit 2024 · 21 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | GetAllowed | 2009 | `public bool GetAllowed ( RebarBarType barType )` |
| Method | GetCurvesForBrowser | 2009 | `public IList < Curve > GetCurvesForBrowser ()` |
| Method | GetDefaultHookAngle | 2014 | `public int GetDefaultHookAngle ( int index )` |
| Method | GetDefaultHookOrientation | 2014 | `public RebarHookOrientation GetDefaultHookOrientation ( int index )` |
| Method | GetEndTreatmentTypeId | 2017 | `public ElementId GetEndTreatmentTypeId ( int iEnd )` |
| Method | GetHookRotationAngle | 2021 | `public double GetHookRotationAngle ( int iEnd )` |
| Method | GetMultiplanarDefinition | 2012 | `public RebarShapeMultiplanarDefinition GetMultiplanarDefinition ()` |
| Method | GetRebarShapeDefinition | 2012 | `public RebarShapeDefinition GetRebarShapeDefinition ()` |
| Method | HasEndTreatment | 2017 | `public bool HasEndTreatment ()` |
| Method | IsSameShapeIgnoringHooks | 2012 | `public bool IsSameShapeIgnoringHooks ( RebarShape otherShape )` |
| Method | SetAllowed | 2009 | `public void SetAllowed ( RebarBarType barType , bool allowed )` |
| Method | SetEndTreatmentTypeId | 2017 | `public void SetEndTreatmentTypeId ( ElementId endTreatmentId , int iEnd )` |
| Method | SetHookRotationAngle | 2021 | `public void SetHookRotationAngle ( double hookRotationAngle , int iEnd )` |
| Property | HigherEnd | 2009 | `public int HigherEnd { get ; }` |
| Property | Parameter | — | `` |
| Property | RebarStyle | 2009 | `public RebarStyle RebarStyle { get ; }` |
| Property | ShapeFamilyId | 2015 | `public ElementId ShapeFamilyId { get ; }` |
| Property | SimpleArc | 2009 | `public bool SimpleArc { get ; }` |
| Property | SimpleLine | 2009 | `public bool SimpleLine { get ; }` |
| Property | StirrupTieAttachment | 2009 | `public StirrupTieAttachmentType StirrupTieAttachment { get ; }` |