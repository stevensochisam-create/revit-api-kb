---
type: FabricationService
namespace: Autodesk.Revit.DB
version: 2024
members: 17
tags: [revit-api, class]
---

# FabricationService

`Autodesk.Revit.DB.FabricationService` · Revit 2024 · 17 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetButton | 2016 | `public FabricationServiceButton GetButton ( int paletteIndex , int buttonIndex )` |
| Method | GetButtonCount | 2016 | `public int GetButtonCount ( int palette )` |
| Method | GetPaletteName | 2022 | `public string GetPaletteName ( int palette )` |
| Method | IsCompatibleWith | 2016 | `public bool IsCompatibleWith ( FabricationService otherService )` |
| Method | IsPaletteExcluded | 2022 | `public bool IsPaletteExcluded ( int paletteIndex )` |
| Method | IsValidButtonIndex | 2016 | `public bool IsValidButtonIndex ( int paletteIndex , int buttonIndex )` |
| Method | IsValidPaletteIndex | 2022 | `public bool IsValidPaletteIndex ( int paletteIndex )` |
| Method | OverrideServiceButtonExclusion | 2017 Subscription Update | `public void OverrideServiceButtonExclusion ( int paletteIndex , int buttonIndex , bool exclude )` |
| Method | ResetServiceExclusionOverrides | 2017 Subscription Update | `public void ResetServiceExclusionOverrides ()` |
| Method | SetServicePaletteExclusions | 2022 | `public bool SetServicePaletteExclusions ( IList < int > excludedPalettes )` |
| Property | Abbreviation | 2016 | `public string Abbreviation { get ; }` |
| Property | FabricationSystemName | 2016 | `public string FabricationSystemName { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Name | 2016 | `public string Name { get ; }` |
| Property | PaletteCount | 2022 | `public int PaletteCount { get ; }` |
| Property | ServiceId | 2016 | `public int ServiceId { get ; }` |