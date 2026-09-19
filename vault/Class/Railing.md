---
type: Railing
namespace: Autodesk.Revit.DB.Architecture
version: 2024
members: 21
tags: [revit-api, class]
---

# Railing

`Autodesk.Revit.DB.Architecture.Railing` · Revit 2024 · 21 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | Flip | 2013 | `public void Flip ()` |
| Method | GetHandRails | 2013 | `public IList < ElementId > GetHandRails ()` |
| Method | GetMultistoryStairsPlacementLevels | 2018 | `public ISet < ElementId > GetMultistoryStairsPlacementLevels ()` |
| Method | GetPath | 2013 | `public IList < Curve > GetPath ()` |
| Method | GetSubelementOnLevel | 2018 | `public Subelement GetSubelementOnLevel ( ElementId levelId )` |
| Method | IsValidHostForNewRailing | 2013 | `public static bool IsValidHostForNewRailing ( Document document , ElementId elementId )` |
| Method | IsValidPathForRailing | 2018 | `public static bool IsValidPathForRailing ( CurveLoop curveLoop )` |
| Method | RailingCanBeHostedByElement | 2017 | `public bool RailingCanBeHostedByElement ( ElementId hostId )` |
| Method | RemoveHost | 2013 | `public void RemoveHost ()` |
| Method | Reset | 2013 | `public void Reset ()` |
| Method | ResetSupportPosition | 2013 | `public void ResetSupportPosition ()` |
| Method | SetMultistoryStairsPlacementLevels | 2018 | `public void SetMultistoryStairsPlacementLevels ( ISet < ElementId > levelIds )` |
| Method | SetPath | 2017 | `public void SetPath ( CurveLoop curveLoop )` |
| Property | CanReset | 2013 | `public bool CanReset { get ; }` |
| Property | Flipped | 2013 | `public bool Flipped { get ; }` |
| Property | HasHost | 2013 | `public bool HasHost { get ; }` |
| Property | HostId | 2013 | `public ElementId HostId { get ; set ; }` |
| Property | IsDefault | 2013 | `public bool IsDefault { get ; }` |
| Property | Parameter | — | `` |
| Property | TopRail | 2013 | `public ElementId TopRail { get ; }` |