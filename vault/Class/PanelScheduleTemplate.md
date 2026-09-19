---
type: PanelScheduleTemplate
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 14
tags: [revit-api, class]
---

# PanelScheduleTemplate

`Autodesk.Revit.DB.Electrical.PanelScheduleTemplate` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CopyFrom | — | `public void CopyFrom ( Document OtherADoc , PanelScheduleTemplate otherElem )` |
| Method | Create | — | `public static PanelScheduleTemplate Create ( Document document , PanelScheduleType type , PanelConfiguration config , string strName )` |
| Method | GetPanelScheduleType | — | `public PanelScheduleType GetPanelScheduleType ()` |
| Method | GetSectionData | — | `public TableSectionData GetSectionData ( SectionType sectionType )` |
| Method | GetTableData | — | `public PanelScheduleData GetTableData ()` |
| Method | HasSameType | 2011 | `public bool HasSameType ( PanelScheduleTemplate otherTemplate )` |
| Method | IsValidPanelConfiguration | 2011 | `public static bool IsValidPanelConfiguration ( PanelScheduleType scheduleType , PanelConfiguration configuration )` |
| Method | IsValidType | — | `` |
| Method | SetTableData | — | `public void SetTableData ( PanelScheduleData Data )` |
| Property | IsBranchPanelSchedule | — | `public bool IsBranchPanelSchedule { get ; }` |
| Property | IsDataPanelSchedule | — | `public bool IsDataPanelSchedule { get ; }` |
| Property | IsDefault | — | `public bool IsDefault { get ; }` |
| Property | IsSwitchboardSchedule | — | `public bool IsSwitchboardSchedule { get ; }` |
| Property | Parameter | — | `` |