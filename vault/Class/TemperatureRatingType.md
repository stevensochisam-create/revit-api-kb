---
type: TemperatureRatingType
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 13
tags: [revit-api, class]
---

# TemperatureRatingType

`Autodesk.Revit.DB.Electrical.TemperatureRatingType` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddCorrectionFactor | — | `public CorrectionFactor AddCorrectionFactor ( double temperature , double factor )` |
| Method | AddInsulationType | — | `public InsulationType AddInsulationType ( string name )` |
| Method | AddWireSize | — | `public WireSize AddWireSize ( string size , long ampacity , double diameter )` |
| Method | RemoveCorrectionFactor | — | `public void RemoveCorrectionFactor ( CorrectionFactor correctionFactor )` |
| Method | RemoveInsulationType | — | `public void RemoveInsulationType ( InsulationType insulationType )` |
| Method | RemoveWireSize | — | `public void RemoveWireSize ( WireSize wireSize )` |
| Property | CorrectionFactors | — | `public CorrectionFactorSet CorrectionFactors { get ; }` |
| Property | InsulationTypes | — | `public InsulationTypeSet InsulationTypes { get ; }` |
| Property | IsInUse | — | `public bool IsInUse { get ; }` |
| Property | MaterialType | — | `public WireMaterialType MaterialType { get ; }` |
| Property | Name | — | `public override string Name { set ; }` |
| Property | Parameter | — | `` |
| Property | WireSizes | — | `public WireSizeSet WireSizes { get ; }` |