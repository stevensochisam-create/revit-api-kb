---
type: RebarUpdateCurvesData
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 42
tags: [revit-api, class]
---

# RebarUpdateCurvesData

`Autodesk.Revit.DB.Structure.RebarUpdateCurvesData` · Revit 2024 · 42 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAttachmentType | 2018 | `public StirrupTieAttachmentType GetAttachmentType ()` |
| Method | GetBarGeometry | 2018 | `public IList < Curve > GetBarGeometry ( int barIndex )` |
| Method | GetBarModelDiameter | 2022 | `public double GetBarModelDiameter ()` |
| Method | GetBarNominalDiameter | 2022 | `public double GetBarNominalDiameter ()` |
| Method | GetBarsNumber | 2018 | `public int GetBarsNumber ()` |
| Method | GetBendingRadius | 2018 | `public double GetBendingRadius ()` |
| Method | GetChangedCustomHandles | 2018 | `public IList < int > GetChangedCustomHandles ()` |
| Method | GetChangedSharedParameterGUIDs | 2020 | `public IList < Guid > GetChangedSharedParameterGUIDs ()` |
| Method | GetCustomConstraints | 2018 | `public IList < RebarConstraint > GetCustomConstraints ()` |
| Method | GetCycleCounter | 2024 | `public int GetCycleCounter ()` |
| Method | GetDocument | 2018 | `public Document GetDocument ()` |
| Method | GetEndConstraint | 2018 | `public RebarConstraint GetEndConstraint ()` |
| Method | GetHookOrientationAngle | 2018 | `public double GetHookOrientationAngle ( int end )` |
| Method | GetHookPlaneNormalForBarIdx | 2018 | `public XYZ GetHookPlaneNormalForBarIdx ( int end , int barPositionIndex )` |
| Method | GetHostId | 2018 | `public ElementId GetHostId ()` |
| Method | GetLayoutRule | 2018 | `public RebarLayoutRule GetLayoutRule ()` |
| Method | GetNumberOfBars | 2018 | `public int GetNumberOfBars ()` |
| Method | GetRebarId | 2020 | `public ElementId GetRebarId ()` |
| Method | GetRebarStyle | 2018 | `public RebarStyle GetRebarStyle ()` |
| Method | GetStartConstraint | 2018 | `public RebarConstraint GetStartConstraint ()` |
| Method | SetCycleCounter | 2024 | `public void SetCycleCounter ( int cycleCounter )` |
| Method | SetHookOrientationAngle | 2018 | `public void SetHookOrientationAngle ( int end , double angle )` |
| Method | SetHookPlaneNormalForBarIdx | 2018 | `public void SetHookPlaneNormalForBarIdx ( int end , int barPositionIndex , XYZ hookNormal )` |
| Property | AlignedFreeFormSetOrientationOptions | 2024 | `public AlignedFreeFormSetOrientationOptions AlignedFreeFormSetOrientationOptions { get ; }` |
| Property | AreOrientationOptionsChanged | 2024 | `public bool AreOrientationOptionsChanged { get ; }` |
| Property | AreWorkshopInstructionsChanged | 2019 | `public bool AreWorkshopInstructionsChanged { get ; }` |
| Property | CycleCounterChanged | 2024 | `public bool CycleCounterChanged { get ; }` |
| Property | ErrorMessage | 2018.1 | `public string ErrorMessage { get ; set ; }` |
| Property | HostMirrored | 2018.1 | `public bool HostMirrored { get ; set ; }` |
| Property | IsAttachmentTypeChanged | 2018 | `public bool IsAttachmentTypeChanged { get ; }` |
| Property | IsBarsNumberChanged | 2018 | `public bool IsBarsNumberChanged { get ; }` |
| Property | IsBendingRadiusChanged | 2018 | `public bool IsBendingRadiusChanged { get ; }` |
| Property | IsEndConstraintChanged | 2018 | `public bool IsEndConstraintChanged { get ; }` |
| Property | IsLayoutChanged | 2018 | `public bool IsLayoutChanged { get ; }` |
| Property | IsReversed | 2018.1 | `public bool IsReversed { get ; set ; }` |
| Property | IsSpacingChanged | 2018 | `public bool IsSpacingChanged { get ; }` |
| Property | IsStartConstraintChanged | 2018 | `public bool IsStartConstraintChanged { get ; }` |
| Property | IsStyleChanged | 2018 | `public bool IsStyleChanged { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Spacing | 2018 | `public double Spacing { get ; }` |
| Property | WorkshopInstructions | 2019 | `public RebarWorkInstructions WorkshopInstructions { get ; }` |