---
type: ReinforcementSettings
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 15
tags: [revit-api, class]
---

# ReinforcementSettings

`Autodesk.Revit.DB.Structure.ReinforcementSettings` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetFabricRoundingManager | 2014 | `public FabricRoundingManager GetFabricRoundingManager ()` |
| Method | GetRebarRoundingManager | 2014 | `public RebarRoundingManager GetRebarRoundingManager ()` |
| Method | GetReinforcementAbbreviationTag | 2016 | `public string GetReinforcementAbbreviationTag ( ReinforcementAbbreviationTagType tagType )` |
| Method | GetReinforcementAbbreviationTags | 2016 | `public IList < ReinforcementAbbreviationTag > GetReinforcementAbbreviationTags ( ReinforcementAbbreviationObjectType objectType )` |
| Method | GetReinforcementSettings | 2013 | `public static ReinforcementSettings GetReinforcementSettings ( Document document )` |
| Method | IsEqual | 2013 | `public bool IsEqual ( ReinforcementSettings other )` |
| Method | SetReinforcementAbbreviationTag | 2016 | `public void SetReinforcementAbbreviationTag ( ReinforcementAbbreviationTagType tagType , string abbreviationTag )` |
| Property | HostStructuralRebar | 2013 | `public bool HostStructuralRebar { get ; set ; }` |
| Property | NumberVaryingLengthRebarsIndividually | 2017 | `public bool NumberVaryingLengthRebarsIndividually { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | RebarPresentationInSection | 2015 | `public RebarPresentationMode RebarPresentationInSection { get ; set ; }` |
| Property | RebarPresentationInView | 2015 | `public RebarPresentationMode RebarPresentationInView { get ; set ; }` |
| Property | RebarShapeDefinesEndTreatments | 2017 | `public bool RebarShapeDefinesEndTreatments { get ; set ; }` |
| Property | RebarShapeDefinesHooks | 2014 | `public bool RebarShapeDefinesHooks { get ; set ; }` |
| Property | RebarVaryingLengthNumberSuffix | 2017 | `public string RebarVaryingLengthNumberSuffix { get ; set ; }` |