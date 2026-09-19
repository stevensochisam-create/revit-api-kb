---
type: ExternalResourceReference
namespace: Autodesk.Revit.DB
version: 2024
members: 12
tags: [revit-api, class]
---

# ExternalResourceReference

`Autodesk.Revit.DB.ExternalResourceReference` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ExternalResourceReference | — | `` |
| Method | CreateLocalResource | 2015 | `public static ExternalResourceReference CreateLocalResource ( Document doc , ExternalResourceType resourceType , ModelPath path , PathType pathType )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetReferenceInformation | 2015 | `public IDictionary < string , string > GetReferenceInformation ()` |
| Method | GetResourceShortDisplayName | 2015 | `public string GetResourceShortDisplayName ()` |
| Method | GetResourceVersionStatus | 2015 | `public ResourceVersionStatus GetResourceVersionStatus ()` |
| Method | HasValidDisplayPath | 2015 | `public bool HasValidDisplayPath ()` |
| Method | IsValidReference | 2015 | `public bool IsValidReference ( ExternalResourceType resourceType )` |
| Property | InSessionPath | 2015 | `public string InSessionPath { get ; internal set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | ServerId | 2015 | `public Guid ServerId { get ; }` |
| Property | Version | 2015 | `public string Version { get ; internal set ; }` |