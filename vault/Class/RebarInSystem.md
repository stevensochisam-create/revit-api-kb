---
type: RebarInSystem
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 39
tags: [revit-api, class]
---

# RebarInSystem

`Autodesk.Revit.DB.Structure.RebarInSystem` · Revit 2024 · 39 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanApplyPresentationMode | 2015 | `public bool CanApplyPresentationMode ( View dBView )` |
| Method | CanEditIndividualBars | 2022 | `public bool CanEditIndividualBars ()` |
| Method | ClearPresentationMode | 2015 | `public void ClearPresentationMode ( View dBView )` |
| Method | DoesBarExistAtPosition | 2013 | `public bool DoesBarExistAtPosition ( int barPosition )` |
| Method | FindMatchingPredefinedPresentationMode | 2015 | `public RebarPresentationMode FindMatchingPredefinedPresentationMode ( View dBView )` |
| Method | GetBarIndexFromReference | 2022 | `public int GetBarIndexFromReference ( Reference barReference )` |
| Method | GetBarPositionTransform | 2013 | `public Transform GetBarPositionTransform ( int barPositionIndex )` |
| Method | GetBendData | 2013 | `public RebarBendData GetBendData ()` |
| Method | GetCenterlineCurves | 2013 | `public IList < Curve > GetCenterlineCurves ( bool adjustForSelfIntersection , bool suppressHooks , bool suppressBendRadius )` |
| Method | GetDistributionPath | 2013 | `public Line GetDistributionPath ()` |
| Method | GetHookTypeId | 2013 | `public ElementId GetHookTypeId ( int end )` |
| Method | GetHostId | 2013 | `public ElementId GetHostId ()` |
| Method | GetMovedBarTransform | 2022 | `public Transform GetMovedBarTransform ( int barPositionIndex )` |
| Method | GetPresentationMode | 2015 | `public RebarPresentationMode GetPresentationMode ( View dBView )` |
| Method | GetReinforcementRoundingManager | 2014 | `public RebarRoundingManager GetReinforcementRoundingManager ()` |
| Method | GetTransformedCenterlineCurves | 2022 | `public IList < Curve > GetTransformedCenterlineCurves ( bool adjustForSelfIntersection , bool suppressHooks , bool suppressBendRadius , int barPositionIndex )` |
| Method | HasPresentationOverrides | 2015 | `public bool HasPresentationOverrides ( View dBView )` |
| Method | IsBarHidden | 2015 | `public bool IsBarHidden ( View view , int barIndex )` |
| Method | IsRebarInSection | 2015 | `public bool IsRebarInSection ( View dBView )` |
| Method | IsUnobscuredInView | 2013 | `public bool IsUnobscuredInView ( View view )` |
| Method | MoveBarInSet | 2022 | `public void MoveBarInSet ( int barPositionIndex , Transform moveTransform )` |
| Method | ResetMovedBarTransform | 2022 | `public void ResetMovedBarTransform ( int barPositionIndex )` |
| Method | SetBarHiddenStatus | 2015 | `public void SetBarHiddenStatus ( View view , int barIndex , bool hide )` |
| Method | SetBarIncluded | 2022 | `public void SetBarIncluded ( bool include , int barPositionIndex )` |
| Method | SetPresentationMode | 2015 | `public void SetPresentationMode ( View dBView , RebarPresentationMode presentationMode )` |
| Method | SetUnobscuredInView | 2014 | `public void SetUnobscuredInView ( View view , bool unobscured )` |
| Property | ArrayLength | 2013 | `public double ArrayLength { get ; }` |
| Property | BarsOnNormalSide | 2013 | `public bool BarsOnNormalSide { get ; }` |
| Property | LayoutRule | 2013 | `public RebarLayoutRule LayoutRule { get ; }` |
| Property | MaxSpacing | 2013 | `public double MaxSpacing { get ; }` |
| Property | Normal | 2013 | `public XYZ Normal { get ; }` |
| Property | NumberOfBarPositions | 2013 | `public int NumberOfBarPositions { get ; }` |
| Property | Parameter | — | `` |
| Property | Quantity | 2013 | `public int Quantity { get ; }` |
| Property | RebarShapeId | 2013 | `public ElementId RebarShapeId { get ; }` |
| Property | ScheduleMark | 2013 | `public string ScheduleMark { get ; set ; }` |
| Property | SystemId | 2013 | `public ElementId SystemId { get ; }` |
| Property | TotalLength | 2013 | `public double TotalLength { get ; }` |
| Property | Volume | 2013 | `public double Volume { get ; }` |