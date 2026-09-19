---
type: MechanicalEquipmentSet
namespace: Autodesk.Revit.DB.Mechanical
version: 2024
members: 10
tags: [revit-api, class]
---

# MechanicalEquipmentSet

`Autodesk.Revit.DB.Mechanical.MechanicalEquipmentSet` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Add | 2019 | `public void Add ( ISet < ElementId > elemIds )` |
| Method | AreElementsNotConnectedInSeries | 2019 | `public static bool AreElementsNotConnectedInSeries ( Document document , ISet < ElementId > elemIds )` |
| Method | AreValidMembers | 2019 | `public static bool AreValidMembers ( Document document , ISet < ElementId > memberIds )` |
| Method | Create | 2019 | `public static MechanicalEquipmentSet Create ( Document document , ElementId typeId , ISet < ElementId > memberIds )` |
| Method | GetMembers | 2019 | `public ISet < ElementId > GetMembers ()` |
| Method | Remove | 2019 | `public void Remove ( ISet < ElementId > elemIds )` |
| Property | Classification | 2019 | `public EquipmentClassification Classification { get ; }` |
| Property | OnDuty | 2019 | `public int OnDuty { get ; set ; }` |
| Property | OnStandby | 2019 | `public int OnStandby { get ; set ; }` |
| Property | Parameter | — | `` |