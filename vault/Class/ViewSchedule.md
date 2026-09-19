---
type: ViewSchedule
namespace: Autodesk.Revit.DB
version: 2024
members: 64
tags: [revit-api, class]
---

# ViewSchedule

`Autodesk.Revit.DB.ViewSchedule` · Revit 2024 · 64 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanGroupHeaders | 2014 | `public bool CanGroupHeaders ( int top , int left , int bottom , int right )` |
| Method | CanUngroupHeaders | 2014 | `public bool CanUngroupHeaders ( int top , int left , int bottom , int right )` |
| Method | CreateKeySchedule | 2013 | `public static ViewSchedule CreateKeySchedule ( Document document , ElementId categoryId )` |
| Method | CreateKeynoteLegend | 2013 | `public static ViewSchedule CreateKeynoteLegend ( Document document )` |
| Method | CreateMaterialTakeoff | 2013 | `public static ViewSchedule CreateMaterialTakeoff ( Document document , ElementId categoryId )` |
| Method | CreateNoteBlock | 2013 | `public static ViewSchedule CreateNoteBlock ( Document document , ElementId familyId )` |
| Method | CreateRevisionSchedule | 2013 | `public static ViewSchedule CreateRevisionSchedule ( Document document )` |
| Method | CreateSchedule | — | `` |
| Method | CreateSheetList | 2013 | `public static ViewSchedule CreateSheetList ( Document document )` |
| Method | CreateViewList | 2013 | `public static ViewSchedule CreateViewList ( Document document )` |
| Method | DeleteSegment | 2022.1 | `public void DeleteSegment ( int segmentIndex )` |
| Method | Export | 2013 | `public void Export ( string folder , string name , ViewScheduleExportOptions options )` |
| Method | GetDefaultNameForKeySchedule | 2013 | `public static string GetDefaultNameForKeySchedule ( Document document , ElementId categoryId )` |
| Method | GetDefaultNameForKeynoteLegend | 2013 | `public static string GetDefaultNameForKeynoteLegend ( Document document )` |
| Method | GetDefaultNameForMaterialTakeoff | 2013 | `public static string GetDefaultNameForMaterialTakeoff ( Document document , ElementId categoryId )` |
| Method | GetDefaultNameForNoteBlock | 2013 | `public static string GetDefaultNameForNoteBlock ( Document document )` |
| Method | GetDefaultNameForRevisionSchedule | 2013 | `public static string GetDefaultNameForRevisionSchedule ( Document document )` |
| Method | GetDefaultNameForSchedule | — | `` |
| Method | GetDefaultNameForSheetList | 2013 | `public static string GetDefaultNameForSheetList ( Document document )` |
| Method | GetDefaultNameForViewList | 2013 | `public static string GetDefaultNameForViewList ( Document document )` |
| Method | GetDefaultParameterNameForKeySchedule | 2013 | `public static string GetDefaultParameterNameForKeySchedule ( Document document , ElementId categoryId )` |
| Method | GetScheduleHeightsOnSheet | 2022.1 | `public ScheduleHeightsOnSheet GetScheduleHeightsOnSheet ()` |
| Method | GetScheduleInstances | 2022.1 | `public IList < ElementId > GetScheduleInstances ( int segmentIndex )` |
| Method | GetSegmentCount | 2022.1 | `public int GetSegmentCount ()` |
| Method | GetSegmentHeight | 2022.1 | `public double GetSegmentHeight ( int segmentIndex )` |
| Method | GetStripedRowsColor | 2021 | `public Color GetStripedRowsColor ( StripedRowPattern index )` |
| Method | GetTableData | 2014 | `public TableData GetTableData ()` |
| Method | GetValidCategoriesForKeySchedule | 2013 | `public static ICollection < ElementId > GetValidCategoriesForKeySchedule ()` |
| Method | GetValidCategoriesForMaterialTakeoff | 2013 | `public static ICollection < ElementId > GetValidCategoriesForMaterialTakeoff ()` |
| Method | GetValidCategoriesForSchedule | 2013 | `public static ICollection < ElementId > GetValidCategoriesForSchedule ()` |
| Method | GetValidFamiliesForNoteBlock | 2013 | `public static ICollection < ElementId > GetValidFamiliesForNoteBlock ( Document document )` |
| Method | GroupHeaders | 2014 | `public void GroupHeaders ( int top , int left , int bottom , int right , string caption )` |
| Method | HasImageField | 2015 | `public bool HasImageField ()` |
| Method | IsDataOutOfDate | 2014 | `public bool IsDataOutOfDate ()` |
| Method | IsSplit | 2022.1 | `public bool IsSplit ()` |
| Method | IsValidCategoryForKeySchedule | 2013 | `public static bool IsValidCategoryForKeySchedule ( ElementId categoryId )` |
| Method | IsValidCategoryForMaterialTakeoff | 2013 | `public static bool IsValidCategoryForMaterialTakeoff ( ElementId categoryId )` |
| Method | IsValidCategoryForSchedule | 2013 | `public static bool IsValidCategoryForSchedule ( ElementId categoryId )` |
| Method | IsValidFamilyForNoteBlock | 2013 | `public static bool IsValidFamilyForNoteBlock ( Document document , ElementId familyId )` |
| Method | IsValidTextTypeId | 2014 | `public bool IsValidTextTypeId ( ElementId textTypeId )` |
| Method | MergeSegments | 2022.1 | `public void MergeSegments ( int movedSegmentIndex , int targetSegmentIndex )` |
| Method | Print | — | `` |
| Method | RefreshData | 2014 | `public bool RefreshData ()` |
| Method | RestoreImageSize | 2015 | `public void RestoreImageSize ()` |
| Method | SetSegmentHeight | 2022.1 | `public void SetSegmentHeight ( int segmentIndex , double height )` |
| Method | SetStripedRowsColor | 2021 | `public void SetStripedRowsColor ( StripedRowPattern index , Color color )` |
| Method | Split | — | `` |
| Method | SplitSegment | 2022.1 | `public void SplitSegment ( int segmentIndex , IList < double > segmentHeights )` |
| Method | UngroupHeaders | 2014 | `public void UngroupHeaders ( int top , int left , int bottom , int right )` |
| Property | BodyTextTypeId | 2014 | `public ElementId BodyTextTypeId { get ; set ; }` |
| Property | Definition | 2013 | `public ScheduleDefinition Definition { get ; }` |
| Property | EmbeddedDefinition | 2013 | `public ScheduleDefinition EmbeddedDefinition { get ; }` |
| Property | HasStripedRows | 2020.1 | `public bool HasStripedRows { get ; set ; }` |
| Property | HeaderTextTypeId | 2014 | `public ElementId HeaderTextTypeId { get ; set ; }` |
| Property | ImageRowHeight | 2015 | `[ ObsoleteAttribute ("This property is deprecated in Revit 2024 and my be removed in a later version of Revit. We suggest you use the 'RowHeight' property instead.")] public double ImageRowHeight { get ; set ; }` |
| Property | IsHeaderFrozen | 2020.1 | `public static bool IsHeaderFrozen { get ; set ; }` |
| Property | IsInternalKeynoteSchedule | 2013 | `public bool IsInternalKeynoteSchedule { get ; }` |
| Property | IsTitleblockRevisionSchedule | 2013 | `public bool IsTitleblockRevisionSchedule { get ; }` |
| Property | KeyScheduleParameterName | 2013 | `public string KeyScheduleParameterName { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | RowHeight | 2024 | `public double RowHeight { get ; set ; }` |
| Property | RowHeightOverride | 2024 | `public RowHeightOverrideOptions RowHeightOverride { get ; set ; }` |
| Property | TitleTextTypeId | 2014 | `public ElementId TitleTextTypeId { get ; set ; }` |
| Property | UseStripedRowsOnSheets | 2021 | `public bool UseStripedRowsOnSheets { get ; set ; }` |