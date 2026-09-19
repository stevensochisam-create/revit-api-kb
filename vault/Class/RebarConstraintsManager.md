---
type: RebarConstraintsManager
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 15
tags: [revit-api, class]
---

# RebarConstraintsManager

`Autodesk.Revit.DB.Structure.RebarConstraintsManager` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AllowConstraintTargets | 2018 | `public bool AllowConstraintTargets ( RebarConstrainedHandle handle , IList < Reference > targetsToConstrain )` |
| Method | ApplyRebarConstraints | 2019 | `public bool ApplyRebarConstraints ( IList < RebarConstraint > constraintsToApply , IList < Reference > oldTargets , IList < Reference > newTargets )` |
| Method | ClearHandleConstraintPairHighlighting | 2014 | `public void ClearHandleConstraintPairHighlighting ( Document aDoc )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAllConstrainedHandles | 2014 | `public IList < RebarConstrainedHandle > GetAllConstrainedHandles ()` |
| Method | GetAllHandles | 2018 | `public IList < RebarConstrainedHandle > GetAllHandles ()` |
| Method | GetConstraintCandidatesForHandle | — | `` |
| Method | GetCurrentConstraintOnHandle | 2014 | `public RebarConstraint GetCurrentConstraintOnHandle ( RebarConstrainedHandle handle )` |
| Method | GetPreferredConstraintOnHandle | 2014 | `public RebarConstraint GetPreferredConstraintOnHandle ( RebarConstrainedHandle handle )` |
| Method | HasValidRebar | 2014 | `public bool HasValidRebar ()` |
| Method | HighlightHandleConstraintPairInAllViews | 2014 | `public void HighlightHandleConstraintPairInAllViews ( Document aDoc , RebarConstrainedHandle handle , RebarConstraint constraint )` |
| Method | RemovePreferredConstraintFromHandle | 2014 | `public void RemovePreferredConstraintFromHandle ( RebarConstrainedHandle handle )` |
| Method | SetPreferredConstraintForHandle | 2014 | `public void SetPreferredConstraintForHandle ( RebarConstrainedHandle handle , RebarConstraint constraint )` |
| Property | IsRebarConstrainedPlacementEnabled | 2014 | `public static bool IsRebarConstrainedPlacementEnabled { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |