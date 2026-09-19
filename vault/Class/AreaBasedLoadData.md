---
type: AreaBasedLoadData
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 19
tags: [revit-api, class]
---

# AreaBasedLoadData

`Autodesk.Revit.DB.Electrical.AreaBasedLoadData` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddElectricalLoadArea | 2023 | `public void AddElectricalLoadArea ( ElementId electricalLoadAreaId )` |
| Method | CanConnectToUpstreamNode | 2024 | `public bool CanConnectToUpstreamNode ( ElementId upstreamNodeId )` |
| Method | CanDisconnectFromUpstreamNode | 2024 | `public bool CanDisconnectFromUpstreamNode ()` |
| Method | ConnectToUpstreamNode | 2024 | `public void ConnectToUpstreamNode ( ElementId upstreamNodeId )` |
| Method | DisconnectFromUpstreamNode | 2024 | `public void DisconnectFromUpstreamNode ()` |
| Method | GetElectricalLoadAreas | 2023 | `public ISet < ElementId > GetElectricalLoadAreas ()` |
| Method | GetUpstreamNodeId | 2024 | `public ElementId GetUpstreamNodeId ()` |
| Method | RemoveElectricalLoadArea | 2023 | `public void RemoveElectricalLoadArea ( ElementId electricalLoadAreaId )` |
| Property | ApparentLoad | 2023 | `public double ApparentLoad { get ; }` |
| Property | ApparentPowerDensity | 2023 | `public double ApparentPowerDensity { get ; }` |
| Property | AreaBasedLoadType | 2023 | `public ElementId AreaBasedLoadType { get ; set ; }` |
| Property | Current | 2023 | `public double Current { get ; }` |
| Property | LoadClassification | 2023 | `public ElementId LoadClassification { get ; }` |
| Property | LoadDensity | 2023 | `public double LoadDensity { get ; }` |
| Property | LoadType | 2023 | `public ElectricalLoadType LoadType { get ; }` |
| Property | PhasesNumber | 2023 | `public int PhasesNumber { get ; }` |
| Property | PowerFactor | 2023 | `public double PowerFactor { get ; }` |
| Property | TrueLoad | 2023 | `public double TrueLoad { get ; }` |
| Property | Voltage | 2023 | `public double Voltage { get ; set ; }` |