---
type: IExternalService
namespace: Autodesk.Revit.DB.ExternalService
version: 2024
members: 8
tags: [revit-api, class]
---

# IExternalService

`Autodesk.Revit.DB.ExternalService.IExternalService` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Execute | 2013 | `bool Execute ( IExternalServer server , Document document , IExternalData data )` |
| Method | GetDescription | 2013 | `string GetDescription ()` |
| Method | GetName | 2013 | `string GetName ()` |
| Method | GetServiceId | 2013 | `ExternalServiceId GetServiceId ()` |
| Method | GetVendorId | 2013 | `string GetVendorId ()` |
| Method | IsValidServer | 2013 | `bool IsValidServer ( IExternalServer server )` |
| Method | OnServersChanged | 2013 | `void OnServersChanged ( Document document , ServerChangeCause cause , IList < Guid > oldServers )` |
| Method | OnServersDisparity | 2013 | `DisparityResponse OnServersDisparity ( Document document , IList < Guid > oldServers )` |