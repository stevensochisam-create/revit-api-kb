---
type: RebarFreeFormAccessor
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 35
tags: [revit-api, class]
---

# RebarFreeFormAccessor

`Autodesk.Revit.DB.Structure.RebarFreeFormAccessor` · Revit 2024 · 35 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddUpdatingSharedParameter | 2020 | `public void AddUpdatingSharedParameter ( ElementId parameterId )` |
| Method | CanBeHookNormal | 2018 | `public bool CanBeHookNormal ( int barIndex , int end , XYZ normal )` |
| Method | DisconnectFromServer | 2018 | `public void DisconnectFromServer ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCouplerIdAtIndex | 2019 | `public ElementId GetCouplerIdAtIndex ( int barPositionIndex , int end )` |
| Method | GetCustomDistributionPath | 2018 | `public IList < Curve > GetCustomDistributionPath ()` |
| Method | GetEndTreatmentTypeIdAtIndex | 2019 | `public ElementId GetEndTreatmentTypeIdAtIndex ( int barPositionIndex , int end )` |
| Method | GetHookOrientationAngle | 2018 | `public double GetHookOrientationAngle ( int end )` |
| Method | GetHookOrientationAngleAtIndex | 2019 | `public double GetHookOrientationAngleAtIndex ( int barPositionIndex , int end )` |
| Method | GetHookOrientationAtIndex | 2019 | `public RebarHookOrientation GetHookOrientationAtIndex ( int barPositionIndex , int end )` |
| Method | GetHookPlaneNormalForBarIdx | 2018 | `public XYZ GetHookPlaneNormalForBarIdx ( int end , int barPositionIndex )` |
| Method | GetHookTypeIdAtIndex | 2019 | `public ElementId GetHookTypeIdAtIndex ( int barPositionIndex , int end )` |
| Method | GetServerGUID | 2018 | `public Guid GetServerGUID ()` |
| Method | GetShapeIdAtIndex | 2019 | `public ElementId GetShapeIdAtIndex ( int barPositionIndex )` |
| Method | GetUpdatingSharedParameters | 2020 | `public IList < ElementId > GetUpdatingSharedParameters ()` |
| Method | HasValidAlignedServer | 2024 | `public bool HasValidAlignedServer ()` |
| Method | HasValidServer | 2018 | `public bool HasValidServer ()` |
| Method | IsBarMatchedWithShapeInReverseOrder | 2019 | `public bool IsBarMatchedWithShapeInReverseOrder ( int barPositionIndex )` |
| Method | IsUnconstrained | 2018 | `public bool IsUnconstrained ()` |
| Method | RemoveUpdatingSharedParameter | 2020 | `public void RemoveUpdatingSharedParameter ( ElementId parameterId )` |
| Method | SetCurves | — | `` |
| Method | SetHookOrientationAngle | 2018 | `public void SetHookOrientationAngle ( int end , double angle )` |
| Method | SetHookPlaneNormalForBarIdx | 2018 | `public void SetHookPlaneNormalForBarIdx ( int end , int barPositionIndex , XYZ hookNormal )` |
| Method | SetLayoutAsFixedNumber | 2018 | `public void SetLayoutAsFixedNumber ( int numberOfBars )` |
| Method | SetLayoutAsMaximumSpacing | 2018 | `public void SetLayoutAsMaximumSpacing ( double spacing )` |
| Method | SetLayoutAsMinimumClearSpacing | 2018 | `public void SetLayoutAsMinimumClearSpacing ( double spacing )` |
| Method | SetLayoutAsNumberWithSpacing | 2018 | `public void SetLayoutAsNumberWithSpacing ( int numberOfBars , double spacing )` |
| Method | SetLayoutAsSingle | 2018 | `public void SetLayoutAsSingle ()` |
| Method | SetReportedShape | 2022 | `public void SetReportedShape ( ElementId rebarShapeId )` |
| Property | AlignedFreeFormSetOrientationOptions | 2024 | `public AlignedFreeFormSetOrientationOptions AlignedFreeFormSetOrientationOptions { get ; set ; }` |
| Property | CycleCounter | 2024 | `public int CycleCounter { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | RebarStyle | 2022 | `public RebarStyle RebarStyle { get ; set ; }` |
| Property | StirrupTieAttachmentType | 2022 | `public StirrupTieAttachmentType StirrupTieAttachmentType { get ; set ; }` |
| Property | WorkshopInstructions | 2019 | `public RebarWorkInstructions WorkshopInstructions { get ; set ; }` |