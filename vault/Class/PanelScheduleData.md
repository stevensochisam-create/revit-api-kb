---
type: PanelScheduleData
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 34
tags: [revit-api, class]
---

# PanelScheduleData

`Autodesk.Revit.DB.Electrical.PanelScheduleData` · Revit 2024 · 34 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddLoadClassification | — | `public bool AddLoadClassification ( ElementId loadClassficationId )` |
| Method | GetLoadClassifications | — | `public IList < ElementId > GetLoadClassifications ()` |
| Method | GetNumberOfCircuitRows | — | `public int GetNumberOfCircuitRows ()` |
| Method | GetSectionData | — | `` |
| Method | IsSymmetric | — | `public bool IsSymmetric ()` |
| Method | RemoveLoadClassification | — | `public void RemoveLoadClassification ( int nIndex )` |
| Method | SetBorderAroundSchedule | — | `public void SetBorderAroundSchedule ( ElementId borderId )` |
| Method | SetBorderAroundSections | — | `public void SetBorderAroundSections ( ElementId borderId )` |
| Method | SetLoadClassifications | — | `public void SetLoadClassifications ( IList < ElementId > loadClassificaions )` |
| Method | UpdateCircuitTableForInstance | — | `public void UpdateCircuitTableForInstance ( FamilyInstance pPanel )` |
| Method | UpdateCircuitTableForTemplate | — | `public void UpdateCircuitTableForTemplate ( PanelSchedulePhaseLoadType newType , int nNumSlots , bool bPhasesAsCurrents )` |
| Method | UpdateIsSectionHidden | — | `public void UpdateIsSectionHidden ( SectionType sectionType , bool bHide )` |
| Method | UpdateLoadSummary | — | `public void UpdateLoadSummary ()` |
| Method | UpdateVerticalHeadersInSection | — | `public void UpdateVerticalHeadersInSection ( SectionType sectionType , bool bVertical )` |
| Property | BodyShowsVerticalHeaders | — | `public bool BodyShowsVerticalHeaders { get ; }` |
| Property | BorderAroundSchedule | — | `public ElementId BorderAroundSchedule { get ; }` |
| Property | BorderAroundSections | — | `public ElementId BorderAroundSections { get ; }` |
| Property | IsAutoShadingForLoadDisplay | 2022 | `public bool IsAutoShadingForLoadDisplay { get ; set ; }` |
| Property | IsFooterSectionHidden | — | `public bool IsFooterSectionHidden { get ; }` |
| Property | IsHeaderSectionHidden | — | `public bool IsHeaderSectionHidden { get ; }` |
| Property | IsPanelSinglePhase | — | `public bool IsPanelSinglePhase { get ; set ; }` |
| Property | IsSummarySectionHidden | — | `public bool IsSummarySectionHidden { get ; }` |
| Property | IsUnusedPhaseHidden | 2021 | `public bool IsUnusedPhaseHidden { get ; set ; }` |
| Property | NumberOfSlots | — | `public int NumberOfSlots { get ; }` |
| Property | PanelConfiguration | — | `public PanelConfiguration PanelConfiguration { get ; }` |
| Property | PhaseLoadType | — | `public PanelSchedulePhaseLoadType PhaseLoadType { get ; }` |
| Property | PhasesAsCurrents | — | `public bool PhasesAsCurrents { get ; }` |
| Property | ScheduleType | — | `public PanelScheduleType ScheduleType { get ; }` |
| Property | ShowCircuitNumberOnOneRowForMultiphaseCircuits | — | `public bool ShowCircuitNumberOnOneRowForMultiphaseCircuits { get ; set ; }` |
| Property | ShowMultipleRowsForMultiphaseCircuits | — | `public bool ShowMultipleRowsForMultiphaseCircuits { get ; set ; }` |
| Property | ShowSlotFromDeviceInsteadOfTemplate | — | `public bool ShowSlotFromDeviceInsteadOfTemplate { get ; set ; }` |
| Property | SummaryShowsGroups | — | `public bool SummaryShowsGroups { get ; set ; }` |
| Property | SummaryShowsOnlyConnectedLoads | — | `public bool SummaryShowsOnlyConnectedLoads { get ; set ; }` |
| Property | SummaryShowsVerticalHeaders | — | `public bool SummaryShowsVerticalHeaders { get ; }` |