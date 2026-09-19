---
type: WireMaterialType
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 9
tags: [revit-api, class]
---

# WireMaterialType

`Autodesk.Revit.DB.Electrical.WireMaterialType` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddGroundConductorSize | — | `public GroundConductorSize AddGroundConductorSize ( long ampacity , string size )` |
| Method | AddTemperatureRatingType | — | `public TemperatureRatingType AddTemperatureRatingType ( string name , TemperatureRatingType baseOn )` |
| Method | RemoveGroundConductorSize | — | `public void RemoveGroundConductorSize ( GroundConductorSize grdConductorSize )` |
| Method | RemoveTemperatureRatingType | — | `public void RemoveTemperatureRatingType ( TemperatureRatingType temperatureRating )` |
| Property | GroundConductorSizes | — | `public GroundConductorSizeSet GroundConductorSizes { get ; }` |
| Property | IsInUse | — | `public bool IsInUse { get ; }` |
| Property | Name | — | `public override string Name { set ; }` |
| Property | Parameter | — | `` |
| Property | TemperatureRatings | — | `public TemperatureRatingTypeSet TemperatureRatings { get ; }` |