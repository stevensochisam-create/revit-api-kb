---
type: ExternalService
namespace: Autodesk.Revit.DB.ExternalService
version: 2024
members: 17
tags: [revit-api, class]
---

# ExternalService

`Autodesk.Revit.DB.ExternalService.ExternalService` · Revit 2024 · 17 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddServer | 2013 | `public void AddServer ( IExternalServer server )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetDefaultServerId | 2013 | `public Guid GetDefaultServerId ()` |
| Method | GetOptions | 2014 | `public ExternalServiceOptions GetOptions ()` |
| Method | GetPublicAccessKey | 2014 | `public Guid GetPublicAccessKey ()` |
| Method | GetRegisteredServerIds | 2013 | `public IList < Guid > GetRegisteredServerIds ()` |
| Method | GetServer | 2013 | `public IExternalServer GetServer ( Guid serverId )` |
| Method | IsRegisteredServerId | 2013 | `public bool IsRegisteredServerId ( Guid serverId )` |
| Method | RemoveServer | 2013 | `public void RemoveServer ( Guid serverId )` |
| Property | Description | 2013 | `public string Description { get ; }` |
| Property | IsSerializable | 2013 | `public bool IsSerializable { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Name | 2013 | `public string Name { get ; }` |
| Property | NumberOfServers | 2013 | `public int NumberOfServers { get ; }` |
| Property | ServiceId | 2013 | `public ExternalServiceId ServiceId { get ; }` |
| Property | SupportActivation | 2024 | `public bool SupportActivation { get ; }` |
| Property | VendorId | 2013 | `public string VendorId { get ; }` |