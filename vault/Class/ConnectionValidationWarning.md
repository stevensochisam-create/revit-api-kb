---
type: ConnectionValidationWarning
namespace: Autodesk.Revit.DB
version: 2024
members: 6
tags: [revit-api, class]
---

# ConnectionValidationWarning

`Autodesk.Revit.DB.ConnectionValidationWarning` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ConnectionValidationWarning | 2016 | `public ConnectionValidationWarning ( ConnectionResolution resolution , ConnectionWarning reason , ElementId part1 , ElementId part2 )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetParts | 2016 | `public ISet < ElementId > GetParts ()` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Reason | 2016 | `public ConnectionWarning Reason { get ; }` |
| Property | Resolution | 2016 | `public ConnectionResolution Resolution { get ; }` |