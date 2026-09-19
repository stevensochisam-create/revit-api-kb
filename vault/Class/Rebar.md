---
type: Rebar
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 68
tags: [revit-api, class]
---

# Rebar

`Autodesk.Revit.DB.Structure.Rebar` · Revit 2024 · 68 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanApplyPresentationMode | 2015 | `public bool CanApplyPresentationMode ( View dBView )` |
| Method | CanBeMatchedWithMultipleShapes | 2019 | `public bool CanBeMatchedWithMultipleShapes ()` |
| Method | CanSuppressFirstOrLastBar | 2017 | `public bool CanSuppressFirstOrLastBar ( View dBView , int end )` |
| Method | CanUseHookType | 2014 | `public bool CanUseHookType ( ElementId proposedHookId )` |
| Method | ClearPresentationMode | 2015 | `public void ClearPresentationMode ( View dBView )` |
| Method | ConstraintsCanBeEdited | 2014 | `public bool ConstraintsCanBeEdited ()` |
| Method | ContainsValidArcRadiiForStyleAndBarType | 2009 | `public static bool ContainsValidArcRadiiForStyleAndBarType ( IList < Curve > curves , RebarStyle style , RebarBarType barType )` |
| Method | CreateFreeForm | — | `` |
| Method | CreateFromCurves | — | `` |
| Method | CreateFromCurvesAndShape | — | `` |
| Method | CreateFromRebarShape | 2009 | `public static Rebar CreateFromRebarShape ( Document doc , RebarShape rebarShape , RebarBarType barType , Element host , XYZ origin , XYZ xVec , XYZ yVec )` |
| Method | DoesBarExistAtPosition | 2013 | `public bool DoesBarExistAtPosition ( int barPosition )` |
| Method | EnableHookLengthOverride | 2021 | `public void EnableHookLengthOverride ( bool enable )` |
| Method | FindMatchingPredefinedPresentationMode | 2015 | `public RebarPresentationMode FindMatchingPredefinedPresentationMode ( View dBView )` |
| Method | GetAllRebarShapeIds | 2019 | `public IList < ElementId > GetAllRebarShapeIds ()` |
| Method | GetBarIndexFromReference | 2022 | `public int GetBarIndexFromReference ( Reference barReference )` |
| Method | GetBendData | 2009 | `public RebarBendData GetBendData ()` |
| Method | GetCenterlineCurves | 2017 | `public IList < Curve > GetCenterlineCurves ( bool adjustForSelfIntersection , bool suppressHooks , bool suppressBendRadius , MultiplanarOption multiplanarOption , int barPositionIndex )` |
| Method | GetCouplerId | 2009 | `public ElementId GetCouplerId ( int end )` |
| Method | GetEndTreatmentTypeId | 2009 | `public ElementId GetEndTreatmentTypeId ( int end )` |
| Method | GetFreeFormAccessor | 2018 | `public RebarFreeFormAccessor GetFreeFormAccessor ()` |
| Method | GetFullGeometryForView | 2017 | `public GeometryElement GetFullGeometryForView ( View view )` |
| Method | GetHookOrientation | 2014 | `public RebarHookOrientation GetHookOrientation ( int iEnd )` |
| Method | GetHookRotationAngle | 2021 | `public double GetHookRotationAngle ( int iEnd )` |
| Method | GetHookTypeId | 2009 | `public ElementId GetHookTypeId ( int end )` |
| Method | GetHostId | 2009 | `public ElementId GetHostId ()` |
| Method | GetMovedBarTransform | 2022 | `public Transform GetMovedBarTransform ( int barPositionIndex )` |
| Method | GetOverridableHookParameters | 2021 | `public void GetOverridableHookParameters ( out ISet < ElementId > startHookLengthPrameters , out ISet < ElementId > startHookTangentLengthParameters , out ISet < ElementId > endHookLengthParameters , out ISet < ElementId` |
| Method | GetParameterValueAtIndex | 2017 | `public ParameterValue GetParameterValueAtIndex ( ElementId paramId , int barPositionIndex )` |
| Method | GetPresentationMode | 2015 | `public RebarPresentationMode GetPresentationMode ( View dBView )` |
| Method | GetRebarConstraintsManager | 2014 | `public RebarConstraintsManager GetRebarConstraintsManager ()` |
| Method | GetReinforcementRoundingManager | 2014 | `public RebarRoundingManager GetReinforcementRoundingManager ()` |
| Method | GetShapeDrivenAccessor | 2018 | `public RebarShapeDrivenAccessor GetShapeDrivenAccessor ()` |
| Method | GetShapeId | 2009 | `public ElementId GetShapeId ()` |
| Method | GetTransformedCenterlineCurves | 2022 | `public IList < Curve > GetTransformedCenterlineCurves ( bool adjustForSelfIntersection , bool suppressHooks , bool suppressBendRadius , MultiplanarOption multiplanarOption , int barPositionIndex )` |
| Method | HasPresentationOverrides | 2015 | `public bool HasPresentationOverrides ( View dBView )` |
| Method | HookAngleMatchesRebarShapeDefinition | 2014 | `public bool HookAngleMatchesRebarShapeDefinition ( int iEnd , ElementId proposedHookId )` |
| Method | IsBarHidden | 2015 | `public bool IsBarHidden ( View view , int barIndex )` |
| Method | IsHookLengthOverrideEnabled | 2021 | `public bool IsHookLengthOverrideEnabled ()` |
| Method | IsRebarFreeForm | 2018 | `public bool IsRebarFreeForm ()` |
| Method | IsRebarInSection | 2015 | `public bool IsRebarInSection ( View dBView )` |
| Method | IsRebarShapeDriven | 2018 | `public bool IsRebarShapeDriven ()` |
| Method | IsUnobscuredInView | 2011 | `public bool IsUnobscuredInView ( View view )` |
| Method | MoveBarInSet | 2022 | `public void MoveBarInSet ( int barPositionIndex , Transform moveTransform )` |
| Method | RebarShapeMatchesCurvesAndHooks | 2013 | `public static bool RebarShapeMatchesCurvesAndHooks ( RebarShape rebarShape , RebarBarType barType , XYZ norm , IList < Curve > curves , RebarHookType startHook , RebarHookType endHook , RebarHookOrientation startHookOrie` |
| Method | RebarShapeMatchesCurvesHooksAndEndTreatment | 2021 | `public static bool RebarShapeMatchesCurvesHooksAndEndTreatment ( RebarShape rebarShape , RebarBarType barType , XYZ norm , IList < Curve > curves , RebarHookType startHook , RebarHookType endHook , RebarHookOrientation s` |
| Method | ResetMovedBarTransform | 2022 | `public void ResetMovedBarTransform ( int barPositionIndex )` |
| Method | SetBarHiddenStatus | 2015 | `public void SetBarHiddenStatus ( View view , int barIndex , bool hide )` |
| Method | SetBarIncluded | 2022 | `public void SetBarIncluded ( bool include , int barPositionIndex )` |
| Method | SetEndTreatmentTypeId | 2021 | `public void SetEndTreatmentTypeId ( int end , ElementId endTreatmentTypeId )` |
| Method | SetHookOrientation | 2014 | `public void SetHookOrientation ( int iEnd , RebarHookOrientation hookOrientation )` |
| Method | SetHookRotationAngle | 2021 | `public void SetHookRotationAngle ( double hookRotationAngle , int iEnd )` |
| Method | SetHookTypeId | 2009 | `public void SetHookTypeId ( int end , ElementId hookTypeId )` |
| Method | SetHostId | 2009 | `public void SetHostId ( Document doc , ElementId hostId )` |
| Method | SetPresentationMode | 2015 | `public void SetPresentationMode ( View dBView , RebarPresentationMode presentationMode )` |
| Method | SetUnobscuredInView | 2011 | `public void SetUnobscuredInView ( View view , bool unobscured )` |
| Property | DistributionType | 2017 | `public DistributionType DistributionType { get ; set ; }` |
| Property | IncludeFirstBar | 2009 | `public bool IncludeFirstBar { get ; set ; }` |
| Property | IncludeLastBar | 2009 | `public bool IncludeLastBar { get ; set ; }` |
| Property | LayoutRule | 2009 | `public RebarLayoutRule LayoutRule { get ; }` |
| Property | MaxSpacing | 2009 | `public double MaxSpacing { get ; set ; }` |
| Property | NumberOfBarPositions | 2009 | `public int NumberOfBarPositions { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | Quantity | 2009 | `public int Quantity { get ; }` |
| Property | ReadOnlyParameters | 2018 | `public bool ReadOnlyParameters { get ; set ; }` |
| Property | ScheduleMark | 2013 | `public string ScheduleMark { get ; set ; }` |
| Property | TotalLength | 2009 | `public double TotalLength { get ; }` |
| Property | Volume | 2009 | `public double Volume { get ; }` |