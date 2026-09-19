---
type: ElectricalSystem
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 60
tags: [revit-api, class]
---

# ElectricalSystem

`Autodesk.Revit.DB.Electrical.ElectricalSystem` · Revit 2024 · 60 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddToCircuit | — | `public bool AddToCircuit ( ElementSet components )` |
| Method | Create | — | `` |
| Method | DisconnectPanel | 2011 | `public void DisconnectPanel ()` |
| Method | GetCircuitPath | 2018 | `public IList < XYZ > GetCircuitPath ()` |
| Method | IsCircuitPathValid | 2018 | `public bool IsCircuitPathValid ( IList < XYZ > nodes )` |
| Method | NewWires | — | `public WireSet NewWires ( View view , WiringType wiringType )` |
| Method | Remove | — | `` |
| Method | RemoveFromCircuit | — | `public void RemoveFromCircuit ( ElementSet components )` |
| Method | SelectPanel | 2011 | `public void SelectPanel ( FamilyInstance panel )` |
| Method | SetCircuitPath | 2018 | `public void SetCircuitPath ( IList < XYZ > nodes )` |
| Property | ApparentCurrent | 2011 | `public double ApparentCurrent { get ; }` |
| Property | ApparentCurrentPhaseA | 2011 | `public double ApparentCurrentPhaseA { get ; }` |
| Property | ApparentCurrentPhaseB | 2011 | `public double ApparentCurrentPhaseB { get ; }` |
| Property | ApparentCurrentPhaseC | 2011 | `public double ApparentCurrentPhaseC { get ; }` |
| Property | ApparentLoad | 2011 | `public double ApparentLoad { get ; }` |
| Property | ApparentLoadPhaseA | 2011 | `public double ApparentLoadPhaseA { get ; }` |
| Property | ApparentLoadPhaseB | 2011 | `public double ApparentLoadPhaseB { get ; }` |
| Property | ApparentLoadPhaseC | 2011 | `public double ApparentLoadPhaseC { get ; }` |
| Property | BalancedLoad | 2011 | `public bool BalancedLoad { get ; }` |
| Property | CircuitConnectionType | 2020 | `public CircuitConnectionType CircuitConnectionType { get ; set ; }` |
| Property | CircuitNamingIndex | 2021 | `public int CircuitNamingIndex { get ; }` |
| Property | CircuitNumber | 2011 | `public string CircuitNumber { get ; }` |
| Property | CircuitPathMode | 2018 | `public ElectricalCircuitPathMode CircuitPathMode { get ; set ; }` |
| Property | CircuitType | 2011 | `public CircuitType CircuitType { get ; }` |
| Property | Frame | 2021 | `public double Frame { get ; set ; }` |
| Property | GroundConductorsNumber | 2011 | `public int GroundConductorsNumber { get ; }` |
| Property | HasCustomCircuitPath | 2018 | `public bool HasCustomCircuitPath { get ; }` |
| Property | HasPathOffset | 2018 | `public bool HasPathOffset { get ; }` |
| Property | HotConductorsNumber | 2011 | `public int HotConductorsNumber { get ; }` |
| Property | IsBasePanelFeedThroughLugsOccupied | 2020 | `public bool IsBasePanelFeedThroughLugsOccupied { get ; }` |
| Property | Length | 2011 | `public double Length { get ; }` |
| Property | LoadClassificationAbbreviations | 2021 | `public string LoadClassificationAbbreviations { get ; }` |
| Property | LoadClassifications | 2011 | `public string LoadClassifications { get ; }` |
| Property | LoadName | 2011 | `public string LoadName { get ; set ; }` |
| Property | NeutralConductorsNumber | 2011 | `public int NeutralConductorsNumber { get ; set ; }` |
| Property | PanelName | 2011 | `public string PanelName { get ; }` |
| Property | Parameter | — | `` |
| Property | PathOffset | 2018 | `public double PathOffset { get ; set ; }` |
| Property | PhaseLabel | 2021 | `public string PhaseLabel { get ; }` |
| Property | PolesNumber | 2011 | `public int PolesNumber { get ; }` |
| Property | PowerFactor | 2011 | `public double PowerFactor { get ; }` |
| Property | PowerFactorState | 2011 | `public PowerFactorStateType PowerFactorState { get ; }` |
| Property | Rating | 2011 | `public double Rating { get ; set ; }` |
| Property | RunsNumber | 2011 | `public int RunsNumber { get ; }` |
| Property | SlotIndex | 2021 | `public string SlotIndex { get ; }` |
| Property | StartSlot | 2011 | `public int StartSlot { get ; }` |
| Property | SystemType | 2011 | `public ElectricalSystemType SystemType { get ; }` |
| Property | TrueCurrent | 2011 | `public double TrueCurrent { get ; }` |
| Property | TrueCurrentPhaseA | 2011 | `public double TrueCurrentPhaseA { get ; }` |
| Property | TrueCurrentPhaseB | 2011 | `public double TrueCurrentPhaseB { get ; }` |
| Property | TrueCurrentPhaseC | 2011 | `public double TrueCurrentPhaseC { get ; }` |
| Property | TrueLoad | 2011 | `public double TrueLoad { get ; set ; }` |
| Property | TrueLoadPhaseA | 2011 | `public double TrueLoadPhaseA { get ; }` |
| Property | TrueLoadPhaseB | 2011 | `public double TrueLoadPhaseB { get ; }` |
| Property | TrueLoadPhaseC | 2011 | `public double TrueLoadPhaseC { get ; }` |
| Property | Voltage | 2011 | `public double Voltage { get ; }` |
| Property | VoltageDrop | 2011 | `public double VoltageDrop { get ; }` |
| Property | Ways | 2021 | `public int Ways { get ; }` |
| Property | WireSizeString | 2011 | `public string WireSizeString { get ; }` |
| Property | WireType | 2011 | `public WireType WireType { get ; set ; }` |