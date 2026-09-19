---
type: RebarContainer
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 26
tags: [revit-api, class]
---

# RebarContainer

`Autodesk.Revit.DB.Structure.RebarContainer` · Revit 2024 · 26 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AppendItemFromCurves | 2016 | `public RebarContainerItem AppendItemFromCurves ( RebarStyle style , RebarBarType barType , RebarHookType startHook , RebarHookType endHook , XYZ normal , IList < Curve > curves , RebarHookOrientation startHookOrient , Re` |
| Method | AppendItemFromCurvesAndShape | 2016 | `public RebarContainerItem AppendItemFromCurvesAndShape ( RebarShape rebarShape , RebarBarType barType , RebarHookType startHook , RebarHookType endHook , XYZ normal , IList < Curve > curves , RebarHookOrientation startHo` |
| Method | AppendItemFromRebar | 2016 | `public RebarContainerItem AppendItemFromRebar ( Rebar rebar )` |
| Method | AppendItemFromRebarShape | 2016 | `public RebarContainerItem AppendItemFromRebarShape ( RebarShape rebarShape , RebarBarType barType , XYZ origin , XYZ xVector , XYZ yVector )` |
| Method | CanApplyPresentationMode | 2016 | `public bool CanApplyPresentationMode ( View dBView )` |
| Method | ClearItems | 2016 | `public void ClearItems ()` |
| Method | Contains | 2016 | `public bool Contains ( RebarContainerItem pItem )` |
| Method | Create | 2016 | `public static RebarContainer Create ( Document aDoc , Element hostElement , ElementId rebarContainerTypeId )` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetEnumerator | — | `public virtual IEnumerator < RebarContainerItem > GetEnumerator ()` |
| Method | GetHostId | 2016 | `public ElementId GetHostId ()` |
| Method | GetItem | 2016 | `public RebarContainerItem GetItem ( int itemIndex )` |
| Method | GetParametersManager | 2016 | `public RebarContainerParameterManager GetParametersManager ()` |
| Method | GetRebarContainerIterator | 2016 | `public RebarContainerIterator GetRebarContainerIterator ()` |
| Method | GetReinforcementRoundingManager | 2016 | `public RebarRoundingManager GetReinforcementRoundingManager ()` |
| Method | HasPresentationOverrides | 2016 | `public bool HasPresentationOverrides ( View dBView )` |
| Method | IsItemHidden | 2017 | `public bool IsItemHidden ( View view , int itemIndex )` |
| Method | IsUnobscuredInView | 2016 | `public bool IsUnobscuredInView ( View view )` |
| Method | RemoveItem | 2016 | `public void RemoveItem ( RebarContainerItem pItem )` |
| Method | SetHostId | 2016 | `public void SetHostId ( Document doc , ElementId hostId )` |
| Method | SetItemHiddenStatus | 2017 | `public void SetItemHiddenStatus ( View view , int itemIndex , bool hide )` |
| Method | SetUnobscuredInView | 2016 | `public void SetUnobscuredInView ( View view , bool unobscured )` |
| Property | ItemsCount | 2016 | `public int ItemsCount { get ; }` |
| Property | Parameter | — | `` |
| Property | PresentItemsAsSubelements | 2017 | `public bool PresentItemsAsSubelements { get ; set ; }` |
| Property | ScheduleMark | 2016 | `public string ScheduleMark { get ; set ; }` |