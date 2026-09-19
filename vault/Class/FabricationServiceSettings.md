---
type: FabricationServiceSettings
namespace: Autodesk.Revit.DB
version: 2024
members: 8
tags: [revit-api, class]
---

# FabricationServiceSettings

`Autodesk.Revit.DB.FabricationServiceSettings` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetFabricationServiceSettings | 2024 | `public static FabricationServiceSettings GetFabricationServiceSettings ( Document doc )` |
| Method | GetFluidTemperature | 2024 | `public double GetFluidTemperature ( FabricationService service )` |
| Method | GetFluidType | 2024 | `public ElementId GetFluidType ( FabricationService service )` |
| Method | HasValidFluidSetting | 2024 | `public bool HasValidFluidSetting ( FabricationService service )` |
| Method | RemoveFluidSetting | 2024 | `public void RemoveFluidSetting ( FabricationService service )` |
| Method | SetFluidTypeAndTemperature | 2024 | `public void SetFluidTypeAndTemperature ( FabricationService service , ElementId fluidId , double temperature )` |
| Property | AirFluidType | 2024 | `public static ElementId AirFluidType { get ; }` |
| Property | Parameter | — | `` |