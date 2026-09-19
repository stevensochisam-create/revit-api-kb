---
type: RebarBarType
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 22
tags: [revit-api, class]
---

# RebarBarType

`Autodesk.Revit.DB.Structure.RebarBarType` · Revit 2024 · 22 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `public static RebarBarType Create ( Document ADoc )` |
| Method | CreateDefaultRebarBarType | 2015 | `public static ElementId CreateDefaultRebarBarType ( Document ADoc )` |
| Method | GetAutoCalcHookLengths | — | `public bool GetAutoCalcHookLengths ( ElementId hookId )` |
| Method | GetHookLength | — | `public double GetHookLength ( ElementId hookId )` |
| Method | GetHookOffsetLength | — | `public double GetHookOffsetLength ( ElementId hookId )` |
| Method | GetHookPermission | — | `public bool GetHookPermission ( ElementId hookId )` |
| Method | GetHookTangentLength | — | `public double GetHookTangentLength ( ElementId hookId )` |
| Method | GetReinforcementRoundingManager | 2014 | `public RebarRoundingManager GetReinforcementRoundingManager ()` |
| Method | SetAutoCalcHookLengths | — | `public void SetAutoCalcHookLengths ( ElementId hookId , bool autoCalculated )` |
| Method | SetBarTypeDiameters | 2018.1 | `public void SetBarTypeDiameters ( BarTypeDiameterOptions diametersOptions )` |
| Method | SetHookLength | — | `public void SetHookLength ( ElementId hookId , double hookLength )` |
| Method | SetHookOffsetLength | — | `public void SetHookOffsetLength ( ElementId hookId , double newLength )` |
| Method | SetHookPermission | — | `public void SetHookPermission ( ElementId hookId , bool permission )` |
| Method | SetHookTangentLength | 2014 | `public void SetHookTangentLength ( ElementId hookId , double newLength )` |
| Property | BarModelDiameter | 2022 | `public double BarModelDiameter { get ; set ; }` |
| Property | BarNominalDiameter | 2022 | `public double BarNominalDiameter { get ; set ; }` |
| Property | DeformationType | — | `public RebarDeformationType DeformationType { get ; set ; }` |
| Property | MaximumBendRadius | — | `public double MaximumBendRadius { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | StandardBendDiameter | — | `public double StandardBendDiameter { get ; set ; }` |
| Property | StandardHookBendDiameter | — | `public double StandardHookBendDiameter { get ; set ; }` |
| Property | StirrupTieBendDiameter | — | `public double StirrupTieBendDiameter { get ; set ; }` |