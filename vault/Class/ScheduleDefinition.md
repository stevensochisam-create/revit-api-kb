---
type: ScheduleDefinition
namespace: Autodesk.Revit.DB
version: 2024
members: 68
tags: [revit-api, class]
---

# ScheduleDefinition

`Autodesk.Revit.DB.ScheduleDefinition` · Revit 2024 · 68 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddEmbeddedSchedule | 2013 | `public void AddEmbeddedSchedule ( ElementId categoryId )` |
| Method | AddField | — | `` |
| Method | AddFilter | 2013 | `public void AddFilter ( ScheduleFilter filter )` |
| Method | AddSortGroupField | 2013 | `public void AddSortGroupField ( ScheduleSortGroupField sortGroupField )` |
| Method | CanFilter | 2013 | `public bool CanFilter ()` |
| Method | CanFilterByGlobalParameters | 2017 | `public bool CanFilterByGlobalParameters ( ScheduleFieldId fieldId )` |
| Method | CanFilterByParameterExistence | 2013 | `public bool CanFilterByParameterExistence ( ScheduleFieldId fieldId )` |
| Method | CanFilterBySubstring | 2013 | `public bool CanFilterBySubstring ( ScheduleFieldId fieldId )` |
| Method | CanFilterByValue | 2013 | `public bool CanFilterByValue ( ScheduleFieldId fieldId )` |
| Method | CanFilterByValuePresence | 2020 | `public bool CanFilterByValuePresence ( ScheduleFieldId fieldId )` |
| Method | CanHaveEmbeddedSchedule | 2013 | `public bool CanHaveEmbeddedSchedule ()` |
| Method | CanIncludeLinkedFiles | 2013 | `public bool CanIncludeLinkedFiles ()` |
| Method | CanSortByField | 2013 | `public bool CanSortByField ( ScheduleFieldId fieldId )` |
| Method | ClearFields | 2013 | `public void ClearFields ()` |
| Method | ClearFilters | 2013 | `public void ClearFilters ()` |
| Method | ClearSortGroupFields | 2013 | `public void ClearSortGroupFields ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetField | — | `` |
| Method | GetFieldCount | 2013 | `public int GetFieldCount ()` |
| Method | GetFieldId | 2013 | `public ScheduleFieldId GetFieldId ( int index )` |
| Method | GetFieldIndex | 2013 | `public int GetFieldIndex ( ScheduleFieldId fieldId )` |
| Method | GetFieldOrder | 2013 | `public IList < ScheduleFieldId > GetFieldOrder ()` |
| Method | GetFilter | 2013 | `public ScheduleFilter GetFilter ( int index )` |
| Method | GetFilterCount | 2013 | `public int GetFilterCount ()` |
| Method | GetFilters | 2013 | `public IList < ScheduleFilter > GetFilters ()` |
| Method | GetSchedulableFields | 2013 | `public IList < SchedulableField > GetSchedulableFields ()` |
| Method | GetSortGroupField | 2013 | `public ScheduleSortGroupField GetSortGroupField ( int index )` |
| Method | GetSortGroupFieldCount | 2013 | `public int GetSortGroupFieldCount ()` |
| Method | GetSortGroupFields | 2013 | `public IList < ScheduleSortGroupField > GetSortGroupFields ()` |
| Method | GetValidCategoriesForEmbeddedSchedule | 2013 | `public ICollection < ElementId > GetValidCategoriesForEmbeddedSchedule ()` |
| Method | InsertCombinedParameterField | 2017 | `public ScheduleField InsertCombinedParameterField ( IList < TableCellCombinedParameterData > data , string fieldName , int index )` |
| Method | InsertField | — | `` |
| Method | InsertFilter | 2013 | `public void InsertFilter ( ScheduleFilter filter , int index )` |
| Method | InsertSortGroupField | 2013 | `public void InsertSortGroupField ( ScheduleSortGroupField sortGroupField , int index )` |
| Method | IsSchedulableField | 2013 | `public bool IsSchedulableField ( SchedulableField schedulableField )` |
| Method | IsValidCategoryForEmbeddedSchedule | 2013 | `public bool IsValidCategoryForEmbeddedSchedule ( ElementId categoryId )` |
| Method | IsValidCategoryForFilterBySheet | 2023 | `public bool IsValidCategoryForFilterBySheet ()` |
| Method | IsValidCombinedParameters | 2017 | `public bool IsValidCombinedParameters ( IList < TableCellCombinedParameterData > data )` |
| Method | IsValidFieldId | 2013 | `public bool IsValidFieldId ( ScheduleFieldId fieldId )` |
| Method | IsValidFieldIndex | 2013 | `public bool IsValidFieldIndex ( int index )` |
| Method | RemoveEmbeddedSchedule | 2013 | `public void RemoveEmbeddedSchedule ()` |
| Method | RemoveField | — | `` |
| Method | RemoveFilter | 2013 | `public void RemoveFilter ( int index )` |
| Method | RemoveSortGroupField | 2013 | `public void RemoveSortGroupField ( int index )` |
| Method | SetFieldOrder | 2013 | `public void SetFieldOrder ( IList < ScheduleFieldId > fieldIds )` |
| Method | SetFilter | 2013 | `public void SetFilter ( int index , ScheduleFilter filter )` |
| Method | SetFilters | 2013 | `public void SetFilters ( IList < ScheduleFilter > filters )` |
| Method | SetSortGroupField | 2013 | `public void SetSortGroupField ( int index , ScheduleSortGroupField sortGroupField )` |
| Method | SetSortGroupFields | 2013 | `public void SetSortGroupFields ( IList < ScheduleSortGroupField > sortGroupFields )` |
| Property | AreaSchemeId | 2013 | `public ElementId AreaSchemeId { get ; }` |
| Property | CategoryId | 2013 | `public ElementId CategoryId { get ; }` |
| Property | EmbeddedDefinition | 2013 | `public ScheduleDefinition EmbeddedDefinition { get ; }` |
| Property | FamilyId | 2013 | `public ElementId FamilyId { get ; }` |
| Property | GrandTotalTitle | 2015 | `public string GrandTotalTitle { get ; set ; }` |
| Property | HasEmbeddedSchedule | 2013 | `public bool HasEmbeddedSchedule { get ; }` |
| Property | IncludeLinkedFiles | 2013 | `public bool IncludeLinkedFiles { get ; set ; }` |
| Property | IsEmbedded | 2013 | `public bool IsEmbedded { get ; }` |
| Property | IsFilteredBySheet | 2023 | `public bool IsFilteredBySheet { get ; set ; }` |
| Property | IsItemized | 2013 | `public bool IsItemized { get ; set ; }` |
| Property | IsKeySchedule | 2013 | `public bool IsKeySchedule { get ; }` |
| Property | IsMaterialTakeoff | 2013 | `public bool IsMaterialTakeoff { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | ShowGrandTotal | 2013 | `public bool ShowGrandTotal { get ; set ; }` |
| Property | ShowGrandTotalCount | 2013 | `public bool ShowGrandTotalCount { get ; set ; }` |
| Property | ShowGrandTotalTitle | 2013 | `public bool ShowGrandTotalTitle { get ; set ; }` |
| Property | ShowGridLines | 2019.2 | `public bool ShowGridLines { get ; set ; }` |
| Property | ShowHeaders | 2015 Subscription Update | `public bool ShowHeaders { get ; set ; }` |
| Property | ShowTitle | 2015 Subscription Update | `public bool ShowTitle { get ; set ; }` |