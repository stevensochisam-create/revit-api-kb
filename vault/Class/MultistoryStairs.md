---
type: MultistoryStairs
namespace: Autodesk.Revit.DB.Architecture
version: 2024
members: 16
tags: [revit-api, class]
---

# MultistoryStairs

`Autodesk.Revit.DB.Architecture.MultistoryStairs` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanConnectLevel | 2018 | `public bool CanConnectLevel ( ElementId levelId )` |
| Method | CanDisconnectLevel | 2018 | `public bool CanDisconnectLevel ( ElementId levelId )` |
| Method | ConnectLevels | 2018 | `public void ConnectLevels ( ISet < ElementId > levelIds )` |
| Method | Create | 2018 | `public static MultistoryStairs Create ( Stairs stairs )` |
| Method | DisconnectLevels | 2018 | `public void DisconnectLevels ( ISet < ElementId > levelIds )` |
| Method | GetAllConnectedLevels | 2018 | `public ISet < ElementId > GetAllConnectedLevels ()` |
| Method | GetAllStairsIds | 2018 | `public ISet < ElementId > GetAllStairsIds ()` |
| Method | GetStairsOnLevel | 2018 | `public Stairs GetStairsOnLevel ( ElementId levelId )` |
| Method | GetStairsPlacementLevels | 2018 | `public ISet < ElementId > GetStairsPlacementLevels ( Stairs stairs )` |
| Method | IsAcceptableForMultistoryStairs | 2018 | `public static bool IsAcceptableForMultistoryStairs ( Stairs stairs )` |
| Method | IsPinned | 2018 | `public bool IsPinned ( Stairs stairs )` |
| Method | Pin | 2018 | `public Stairs Pin ( ElementId levelId )` |
| Method | Unpin | 2018 | `public Stairs Unpin ( ElementId levelId )` |
| Property | ActualTreadDepth | 2018 | `public double ActualTreadDepth { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | StandardStairsId | 2018 | `public ElementId StandardStairsId { get ; }` |