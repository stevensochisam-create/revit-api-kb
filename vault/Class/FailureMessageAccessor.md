---
type: FailureMessageAccessor
namespace: Autodesk.Revit.DB
version: 2024
members: 15
tags: [revit-api, class]
---

# FailureMessageAccessor

`Autodesk.Revit.DB.FailureMessageAccessor` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CloneFailureMessage | 2011 | `public FailureMessage CloneFailureMessage ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAdditionalElementIds | 2011 | `public ICollection < ElementId > GetAdditionalElementIds ()` |
| Method | GetCurrentResolutionType | 2011 | `public FailureResolutionType GetCurrentResolutionType ()` |
| Method | GetDefaultResolutionCaption | 2011 | `public string GetDefaultResolutionCaption ()` |
| Method | GetDescriptionText | 2011 | `public string GetDescriptionText ()` |
| Method | GetFailingElementIds | 2011 | `public ICollection < ElementId > GetFailingElementIds ()` |
| Method | GetFailureDefinitionId | 2011 | `public FailureDefinitionId GetFailureDefinitionId ()` |
| Method | GetNumberOfResolutions | 2011 | `public int GetNumberOfResolutions ()` |
| Method | GetSeverity | 2011 | `public FailureSeverity GetSeverity ()` |
| Method | HasResolutionOfType | 2011 | `public bool HasResolutionOfType ( FailureResolutionType type )` |
| Method | HasResolutions | 2011 | `public bool HasResolutions ()` |
| Method | SetCurrentResolutionType | 2011 | `public void SetCurrentResolutionType ( FailureResolutionType resolutionType )` |
| Method | ShouldMergeWithMessage | 2011 | `public bool ShouldMergeWithMessage ( FailureMessageAccessor messageToMergeWith )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |