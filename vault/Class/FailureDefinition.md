---
type: FailureDefinition
namespace: Autodesk.Revit.DB
version: 2024
members: 12
tags: [revit-api, class]
---

# FailureDefinition

`Autodesk.Revit.DB.FailureDefinition` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddResolutionType | 2011 | `public FailureDefinition AddResolutionType ( FailureResolutionType type , string caption , Type classOfResolution )` |
| Method | CreateFailureDefinition | 2011 | `public static FailureDefinition CreateFailureDefinition ( FailureDefinitionId id , FailureSeverity severity , string messageString )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetApplicableResolutionTypes | 2011 | `public IList < FailureResolutionType > GetApplicableResolutionTypes ()` |
| Method | GetDefaultResolutionType | 2011 | `public FailureResolutionType GetDefaultResolutionType ()` |
| Method | GetDescriptionText | 2011 | `public string GetDescriptionText ()` |
| Method | GetResolutionCaption | 2011 | `public string GetResolutionCaption ( FailureResolutionType type )` |
| Method | HasResolutions | 2011 | `public bool HasResolutions ()` |
| Method | IsResolutionApplicable | 2011 | `public bool IsResolutionApplicable ( FailureResolutionType type )` |
| Method | SetDefaultResolutionType | 2011 | `public FailureDefinition SetDefaultResolutionType ( FailureResolutionType type )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Severity | 2011 | `public FailureSeverity Severity { get ; }` |