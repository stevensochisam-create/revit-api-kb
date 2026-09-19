---
type: Zone
namespace: Autodesk.Revit.DB.Mechanical
version: 2024
members: 25
tags: [revit-api, class]
---

# Zone

`Autodesk.Revit.DB.Mechanical.Zone` · Revit 2024 · 25 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddSpaces | — | `public bool AddSpaces ( SpaceSet spaces )` |
| Method | CreateAreaBasedLoad | 2023 | `public static Zone CreateAreaBasedLoad ( Document doc , string name , ElementId levelId , ElementId phaseId )` |
| Method | GetDomainData | 2023 | `public ZoneElementDomainData GetDomainData ()` |
| Method | RemoveSpaces | — | `public bool RemoveSpaces ( SpaceSet spaces )` |
| Property | Area | — | `public double Area { get ; }` |
| Property | Boundary | — | `public CurveArray Boundary { get ; }` |
| Property | CalculatedCoolingLoad | — | `public double CalculatedCoolingLoad { get ; }` |
| Property | CalculatedHeatingLoad | — | `public double CalculatedHeatingLoad { get ; }` |
| Property | CalculatedSupplyAirflow | — | `public double CalculatedSupplyAirflow { get ; }` |
| Property | CoolingAirTemperature | — | `public double CoolingAirTemperature { get ; set ; }` |
| Property | CoolingSetPoint | — | `public double CoolingSetPoint { get ; set ; }` |
| Property | DehumidificationSetPoint | — | `public double DehumidificationSetPoint { get ; set ; }` |
| Property | GrossArea | — | `public double GrossArea { get ; }` |
| Property | GrossVolume | — | `public double GrossVolume { get ; }` |
| Property | HeatingAirTemperature | — | `public double HeatingAirTemperature { get ; set ; }` |
| Property | HeatingSetPoint | — | `public double HeatingSetPoint { get ; set ; }` |
| Property | HumidificationSetPoint | — | `public double HumidificationSetPoint { get ; set ; }` |
| Property | IsDefaultZone | — | `public bool IsDefaultZone { get ; set ; }` |
| Property | Name | — | `public override string Name { set ; }` |
| Property | Parameter | — | `` |
| Property | Perimeter | — | `public double Perimeter { get ; }` |
| Property | Phase | — | `public Phase Phase { get ; }` |
| Property | ServiceType | — | `public ServiceType ServiceType { get ; set ; }` |
| Property | Spaces | — | `public SpaceSet Spaces { get ; }` |
| Property | Volume | — | `public double Volume { get ; }` |