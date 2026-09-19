---
type: ElectricalEquipment
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 8
tags: [revit-api, class]
---

# ElectricalEquipment

`Autodesk.Revit.DB.Electrical.ElectricalEquipment` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetCircuitNamingSchemeType | 2021 | `public CircuitNaming GetCircuitNamingSchemeType ()` |
| Method | IsValidCircuitNamingSchemeId | 2021 | `public static bool IsValidCircuitNamingSchemeId ( Document aDocument , ElementId circuitNamingSchemeId )` |
| Method | IsValidDistributionSystem | 2021 | `public bool IsValidDistributionSystem ( DistributionSysType distributionSystem )` |
| Method | SetCircuitNamingSchemeType | 2021 | `public void SetCircuitNamingSchemeType ( CircuitNaming circuitNamingType )` |
| Property | CircuitNamingSchemeId | 2021 | `public ElementId CircuitNamingSchemeId { get ; set ; }` |
| Property | DistributionSystem | — | `public DistributionSysType DistributionSystem { get ; set ; }` |
| Property | IsSwitchboard | 2021 | `public bool IsSwitchboard { get ; }` |
| Property | MaxNumberOfCircuits | 2021 | `public int MaxNumberOfCircuits { get ; set ; }` |