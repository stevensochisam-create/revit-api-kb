---
type: PipingSystem
namespace: Autodesk.Revit.DB.Plumbing
version: 2024
members: 18
tags: [revit-api, class]
---

# PipingSystem

`Autodesk.Revit.DB.Plumbing.PipingSystem` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanBeHydraulicLoopBoundary | 2019 | `public static bool CanBeHydraulicLoopBoundary ( Element element )` |
| Method | Create | — | `` |
| Method | CreateHydraulicSeparation | 2019 | `public static ISet < ElementId > CreateHydraulicSeparation ( Document document , ISet < ElementId > pipeElementIds )` |
| Method | DeleteHydraulicSeparation | 2019 | `public static void DeleteHydraulicSeparation ( Document document , ISet < ElementId > pipeElementIds )` |
| Method | GetFixtureUnits | 2017 | `public double GetFixtureUnits ()` |
| Method | GetFlow | 2017 | `public double GetFlow ()` |
| Method | GetPumpSets | 2019 | `public ISet < ElementId > GetPumpSets ()` |
| Method | GetStaticPressure | 2017 | `public double GetStaticPressure ()` |
| Method | GetVolume | 2017 | `public double GetVolume ()` |
| Method | IsFlowServerMissing | 2014 | `public bool IsFlowServerMissing ()` |
| Method | IsHydraulicLoopBoundary | 2019 | `public static bool IsHydraulicLoopBoundary ( Element element )` |
| Method | IsPressureDropServerMissing | 2014 | `public bool IsPressureDropServerMissing ()` |
| Method | Remove | — | `` |
| Property | BaseEquipmentConnector | — | `public Connector BaseEquipmentConnector { get ; set ; }` |
| Property | IsWellConnected | 2011 | `public bool IsWellConnected { get ; }` |
| Property | Parameter | — | `` |
| Property | PipingNetwork | — | `public ElementSet PipingNetwork { get ; }` |
| Property | SystemType | — | `public PipeSystemType SystemType { get ; }` |