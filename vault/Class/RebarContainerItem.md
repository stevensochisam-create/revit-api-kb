---
type: RebarContainerItem
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 50
tags: [revit-api, class]
---

# RebarContainerItem

`Autodesk.Revit.DB.Structure.RebarContainerItem` · Revit 2024 · 50 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanApplyPresentationMode | 2016 | `public bool CanApplyPresentationMode ( View dBView )` |
| Method | CanUseHookType | 2016 | `public bool CanUseHookType ( ElementId proposedHookId )` |
| Method | ClearPresentationMode | 2016 | `public void ClearPresentationMode ( View dBView )` |
| Method | ComputeDrivingCurves | 2016 | `public IList < Curve > ComputeDrivingCurves ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | DoesBarExistAtPosition | 2016 | `public bool DoesBarExistAtPosition ( int barPosition )` |
| Method | FindMatchingPredefinedPresentationMode | 2016 | `public RebarPresentationMode FindMatchingPredefinedPresentationMode ( View dBView )` |
| Method | GetBarPositionTransform | 2016 | `public Transform GetBarPositionTransform ( int barPositionIndex )` |
| Method | GetBendData | 2016 | `public RebarBendData GetBendData ()` |
| Method | GetCenterlineCurves | — | `` |
| Method | GetDistributionPath | 2016 | `public Line GetDistributionPath ()` |
| Method | GetHookOrientation | 2016 | `public RebarHookOrientation GetHookOrientation ( int iEnd )` |
| Method | GetHookTypeId | 2016 | `public ElementId GetHookTypeId ( int end )` |
| Method | GetPresentationMode | 2016 | `public RebarPresentationMode GetPresentationMode ( View dBView )` |
| Method | HasPresentationOverrides | 2016 | `public bool HasPresentationOverrides ( View dBView )` |
| Method | IsBarHidden | 2016 | `public bool IsBarHidden ( View view , int barIndex )` |
| Method | IsRebarInSection | 2016 | `public bool IsRebarInSection ( View dBView )` |
| Method | SetBarHiddenStatus | 2016 | `public void SetBarHiddenStatus ( View view , int barIndex , bool hide )` |
| Method | SetFromCurves | 2016 | `public void SetFromCurves ( RebarStyle style , RebarBarType barType , RebarHookType startHook , RebarHookType endHook , XYZ norm , IList < Curve > curves , RebarHookOrientation startHookOrient , RebarHookOrientation endH` |
| Method | SetFromCurvesAndShape | 2016 | `public void SetFromCurvesAndShape ( RebarShape rebarShape , RebarBarType barType , RebarHookType startHook , RebarHookType endHook , XYZ norm , IList < Curve > curves , RebarHookOrientation startHookOrient , RebarHookOri` |
| Method | SetFromRebar | 2016 | `public void SetFromRebar ( Rebar rebar )` |
| Method | SetFromRebarShape | 2016 | `public void SetFromRebarShape ( RebarShape rebarShape , RebarBarType barType , XYZ origin , XYZ xVec , XYZ yVec )` |
| Method | SetHookOrientation | 2016 | `public void SetHookOrientation ( int iEnd , RebarHookOrientation hookOrientation )` |
| Method | SetHookTypeId | 2016 | `public void SetHookTypeId ( int end , ElementId hookTypeId )` |
| Method | SetLayoutAsFixedNumber | 2016 | `public void SetLayoutAsFixedNumber ( int numberOfBarPositions , double arrayLength , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsMaximumSpacing | 2016 | `public void SetLayoutAsMaximumSpacing ( double spacing , double arrayLength , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsMinimumClearSpacing | 2016 | `public void SetLayoutAsMinimumClearSpacing ( double spacing , double arrayLength , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsNumberWithSpacing | 2016 | `public void SetLayoutAsNumberWithSpacing ( int numberOfBarPositions , double spacing , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsSingle | 2016 | `public void SetLayoutAsSingle ()` |
| Method | SetPresentationMode | 2016 | `public void SetPresentationMode ( View dBView , RebarPresentationMode presentationMode )` |
| Property | ArrayLength | 2016 | `public double ArrayLength { get ; set ; }` |
| Property | BarTypeId | 2016 | `public ElementId BarTypeId { get ; }` |
| Property | BarsOnNormalSide | 2016 | `public bool BarsOnNormalSide { get ; set ; }` |
| Property | BaseFinishingTurns | 2016 | `public int BaseFinishingTurns { get ; set ; }` |
| Property | Height | 2016 | `public double Height { get ; set ; }` |
| Property | IncludeFirstBar | 2016 | `public bool IncludeFirstBar { get ; set ; }` |
| Property | IncludeLastBar | 2016 | `public bool IncludeLastBar { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | ItemIndex | 2016 | `public int ItemIndex { get ; }` |
| Property | LayoutRule | 2016 | `public RebarLayoutRule LayoutRule { get ; }` |
| Property | MaxSpacing | 2016 | `public double MaxSpacing { get ; set ; }` |
| Property | MultiplanarDepth | 2016 | `public double MultiplanarDepth { get ; set ; }` |
| Property | Normal | 2016 | `public XYZ Normal { get ; }` |
| Property | NumberOfBarPositions | 2016 | `public int NumberOfBarPositions { get ; set ; }` |
| Property | Pitch | 2016 | `public double Pitch { get ; set ; }` |
| Property | Quantity | 2016 | `public int Quantity { get ; }` |
| Property | RebarShapeId | 2016 | `public ElementId RebarShapeId { get ; set ; }` |
| Property | TopFinishingTurns | 2016 | `public int TopFinishingTurns { get ; set ; }` |
| Property | TotalLength | 2016 | `public double TotalLength { get ; }` |
| Property | Volume | 2016 | `public double Volume { get ; }` |