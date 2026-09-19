---
type: IExternalResourceServer
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# IExternalResourceServer

`Autodesk.Revit.DB.IExternalResourceServer` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreSameResources | 2015 | `bool AreSameResources ( IDictionary < string , string > reference1 , IDictionary < string , string > reference2 )` |
| Method | GetIconPath | 2015 | `string GetIconPath ()` |
| Method | GetInSessionPath | 2015 | `string GetInSessionPath ( ExternalResourceReference reference , string originalDisplayPath )` |
| Method | GetInformationLink | 2015 | `string GetInformationLink ()` |
| Method | GetResourceVersionStatus | 2015 | `ResourceVersionStatus GetResourceVersionStatus ( ExternalResourceReference reference )` |
| Method | GetShortName | 2015 | `string GetShortName ()` |
| Method | GetTypeSpecificServerOperations | 2015 | `void GetTypeSpecificServerOperations ( ExternalResourceServerExtensions extensions )` |
| Method | IsResourceWellFormed | 2015 | `bool IsResourceWellFormed ( ExternalResourceReference extRef )` |
| Method | LoadResource | 2015 | `void LoadResource ( Guid loadRequestId , ExternalResourceType resourceType , ExternalResourceReference desiredResource , ExternalResourceLoadContext loadContext , ExternalResourceLoadContent loadResults )` |
| Method | SetupBrowserData | 2015 | `void SetupBrowserData ( ExternalResourceBrowserData browseData )` |
| Method | SupportsExternalResourceType | 2015 | `bool SupportsExternalResourceType ( ExternalResourceType type )` |