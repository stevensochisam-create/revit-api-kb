---
type: FailureMessage
namespace: Autodesk.Revit.DB
version: 2024
members: 16
tags: [revit-api, class]
---

# FailureMessage

`Autodesk.Revit.DB.FailureMessage` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | FailureMessage | 2011 | `public FailureMessage ( FailureDefinitionId id )` |
| Method | AddResolution | 2011 | `public FailureMessage AddResolution ( FailureResolutionType type , FailureResolution resolution )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAdditionalElements | 2011 | `public ICollection < ElementId > GetAdditionalElements ()` |
| Method | GetDefaultResolutionCaption | 2011 | `public string GetDefaultResolutionCaption ()` |
| Method | GetDescriptionText | 2011 | `public string GetDescriptionText ()` |
| Method | GetFailingElements | 2011 | `public ICollection < ElementId > GetFailingElements ()` |
| Method | GetFailureDefinitionId | 2011 | `public FailureDefinitionId GetFailureDefinitionId ()` |
| Method | GetSeverity | 2011 | `public FailureSeverity GetSeverity ()` |
| Method | HasResolutionOfType | 2011 | `public bool HasResolutionOfType ( FailureResolutionType type )` |
| Method | HasResolutions | 2011 | `public bool HasResolutions ()` |
| Method | SetAdditionalElement | 2011 | `public FailureMessage SetAdditionalElement ( ElementId additionalElement )` |
| Method | SetAdditionalElements | 2011 | `public FailureMessage SetAdditionalElements ( ICollection < ElementId > additionalElements )` |
| Method | SetFailingElement | 2011 | `public FailureMessage SetFailingElement ( ElementId id )` |
| Method | SetFailingElements | 2011 | `public FailureMessage SetFailingElements ( ICollection < ElementId > idsToShow )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |