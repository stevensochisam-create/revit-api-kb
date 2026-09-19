---
type: ScheduleField
namespace: Autodesk.Revit.DB
version: 2024
members: 42
tags: [revit-api, class]
---

# ScheduleField

`Autodesk.Revit.DB.ScheduleField` · Revit 2024 · 42 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanDisplayMinMax | 2017 | `public bool CanDisplayMinMax ()` |
| Method | CanTotal | 2013 | `public bool CanTotal ()` |
| Method | CanTotalByAssemblyType | 2013 | `public bool CanTotalByAssemblyType ()` |
| Method | CreatesCircularReferences | 2013 | `public bool CreatesCircularReferences ( ScheduleFieldId fieldId )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCombinedParameters | 2017 | `public IList < TableCellCombinedParameterData > GetCombinedParameters ()` |
| Method | GetCustomFieldData | 2024 | `public CustomFieldData GetCustomFieldData ()` |
| Method | GetFormatOptions | 2014 | `public FormatOptions GetFormatOptions ()` |
| Method | GetName | 2013 | `public string GetName ()` |
| Method | GetSchedulableField | 2013 | `public SchedulableField GetSchedulableField ()` |
| Method | GetSpecTypeId | 2013 | `public ForgeTypeId GetSpecTypeId ()` |
| Method | GetStyle | 2014 | `public TableCellStyle GetStyle ()` |
| Method | IsValidCombinedParameters | 2017 | `public bool IsValidCombinedParameters ( IList < TableCellCombinedParameterData > data )` |
| Method | ResetOverride | 2014 | `public void ResetOverride ()` |
| Method | SetCombinedParameters | 2017 | `public void SetCombinedParameters ( IList < TableCellCombinedParameterData > data )` |
| Method | SetFormatOptions | 2014 | `public void SetFormatOptions ( FormatOptions formatOptions )` |
| Method | SetStyle | 2014 | `public void SetStyle ( TableCellStyle style )` |
| Property | ColumnHeading | 2013 | `public string ColumnHeading { get ; set ; }` |
| Property | Definition | 2013 | `public ScheduleDefinition Definition { get ; }` |
| Property | DisplayType | 2017 | `public ScheduleFieldDisplayType DisplayType { get ; set ; }` |
| Property | FieldId | 2013 | `public ScheduleFieldId FieldId { get ; }` |
| Property | FieldIndex | 2013 | `public int FieldIndex { get ; }` |
| Property | FieldType | 2013 | `public ScheduleFieldType FieldType { get ; }` |
| Property | GridColumnWidth | 2013 | `public double GridColumnWidth { get ; set ; }` |
| Property | HasSchedulableField | 2014 | `public bool HasSchedulableField { get ; }` |
| Property | HeadingOrientation | 2013 | `public ScheduleHeadingOrientation HeadingOrientation { get ; set ; }` |
| Property | HorizontalAlignment | 2013 | `public ScheduleHorizontalAlignment HorizontalAlignment { get ; set ; }` |
| Property | IsCalculatedField | 2014 | `public bool IsCalculatedField { get ; }` |
| Property | IsCombinedParameterField | 2017 | `public bool IsCombinedParameterField { get ; }` |
| Property | IsHidden | 2013 | `public bool IsHidden { get ; set ; }` |
| Property | IsOverridden | 2014 | `public bool IsOverridden { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | MultipleValuesCustomText | 2022 | `public string MultipleValuesCustomText { get ; set ; }` |
| Property | MultipleValuesDisplayType | 2022 | `public ScheduleFieldMultipleValuesDisplayType MultipleValuesDisplayType { get ; set ; }` |
| Property | MultipleValuesText | 2022 | `public string MultipleValuesText { get ; }` |
| Property | ParameterId | 2013 | `public ElementId ParameterId { get ; }` |
| Property | PercentageBy | 2013 | `public ScheduleFieldId PercentageBy { get ; set ; }` |
| Property | PercentageOf | 2013 | `public ScheduleFieldId PercentageOf { get ; set ; }` |
| Property | Schedule | 2013 | `public ViewSchedule Schedule { get ; }` |
| Property | SheetColumnWidth | 2013 | `public double SheetColumnWidth { get ; set ; }` |
| Property | TotalByAssemblyType | 2013 | `public bool TotalByAssemblyType { get ; set ; }` |
| Property | VerticalAlignment | 2024 | `public ScheduleVerticalAlignment VerticalAlignment { get ; set ; }` |