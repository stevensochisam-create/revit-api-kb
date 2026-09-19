---
type: FabricationRodInfo
namespace: Autodesk.Revit.DB
version: 2024
members: 18
tags: [revit-api, class]
---

# FabricationRodInfo

`Autodesk.Revit.DB.FabricationRodInfo` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AttachToHanger | 2017 | `public void AttachToHanger ( ElementId hangerId , int rodIndex , XYZ position )` |
| Method | AttachToStructure | 2016 | `public void AttachToStructure ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetBearerExtension | 2017 | `public double GetBearerExtension ( int rodIndex )` |
| Method | GetRodAttachedElementId | 2016 | `public LinkElementId GetRodAttachedElementId ( int rodIndex )` |
| Method | GetRodEndPosition | 2016 | `public XYZ GetRodEndPosition ( int rodIndex )` |
| Method | GetRodLength | 2018 | `public double GetRodLength ( int rodIndex )` |
| Method | GetRodStructureExtension | 2018 | `public double GetRodStructureExtension ( int rodIndex )` |
| Method | IsRodLockedWithHost | 2017 | `public bool IsRodLockedWithHost ( int rodIndex )` |
| Method | SetBearerExtension | 2017 | `public void SetBearerExtension ( int rodIndex , double length )` |
| Method | SetRodEndPosition | 2017 | `public void SetRodEndPosition ( int rodIndex , XYZ position )` |
| Method | SetRodLength | 2018 | `public bool SetRodLength ( int rodIndex , double newLength )` |
| Method | SetRodLockedWithHost | 2017 | `public void SetRodLockedWithHost ( int rodIndex , bool locked )` |
| Method | SetRodStructureExtension | 2018 | `public bool SetRodStructureExtension ( int rodIndex , double extension )` |
| Property | CanRodsBeHosted | 2018 | `public bool CanRodsBeHosted { get ; set ; }` |
| Property | IsAttachedToStructure | 2016 | `public bool IsAttachedToStructure { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | RodCount | 2016 | `public int RodCount { get ; }` |