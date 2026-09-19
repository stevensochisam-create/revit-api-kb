---
type: FabricationNetworkChangeService
namespace: Autodesk.Revit.DB.Fabrication
version: 2024
members: 16
tags: [revit-api, class]
---

# FabricationNetworkChangeService

`Autodesk.Revit.DB.Fabrication.FabricationNetworkChangeService` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | FabricationNetworkChangeService | 2018.2 | `public FabricationNetworkChangeService ( Document document )` |
| Method | ApplyChange | 2018.2 | `public FabricationNetworkChangeServiceResult ApplyChange ()` |
| Method | ChangeService | — | `` |
| Method | ChangeSize | 2018.2 | `public FabricationNetworkChangeServiceResult ChangeSize ( ISet < ElementId > selection , ISet < FabricationPartSizeMap > fabricationPartSizeMaps )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetElementsThatFailed | 2018.2 | `public ISet < ElementId > GetElementsThatFailed ()` |
| Method | GetInLinePartTypes | 2018.2 | `public ISet < ElementId > GetInLinePartTypes ()` |
| Method | GetMapOfAllSizesForStraights | 2018.2 | `public ISet < FabricationPartSizeMap > GetMapOfAllSizesForStraights ()` |
| Method | GetStraightsThatWereNotChanged | 2018.2 | `public ISet < ElementId > GetStraightsThatWereNotChanged ()` |
| Method | SetMapOfInLinePartTypes | 2018.2 | `public void SetMapOfInLinePartTypes ( IDictionary < ElementId , ElementId > fabricationPartTypes )` |
| Method | SetMapOfSizesForStraights | 2018.2 | `public void SetMapOfSizesForStraights ( ISet < FabricationPartSizeMap > fabricationPartSizeMaps )` |
| Method | SetPaletteId | 2022 | `public void SetPaletteId ( int paletteId )` |
| Method | SetRestrictPalette | 2022 | `public void SetRestrictPalette ( bool restrictPalette )` |
| Method | SetSelection | 2018.2 | `public FabricationNetworkChangeServiceResult SetSelection ( ISet < ElementId > selection )` |
| Method | SetServiceId | 2018.2 | `public void SetServiceId ( int serviceId )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |