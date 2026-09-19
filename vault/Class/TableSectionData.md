---
type: TableSectionData
namespace: Autodesk.Revit.DB
version: 2024
members: 58
tags: [revit-api, class]
---

# TableSectionData

`Autodesk.Revit.DB.TableSectionData` · Revit 2024 · 58 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AllowOverrideCellStyle | 2014 | `public bool AllowOverrideCellStyle ( int nRow , int nCol )` |
| Method | CanInsertColumn | 2014 | `public bool CanInsertColumn ( int nIndex )` |
| Method | CanInsertRow | 2014 | `public bool CanInsertRow ( int nIndex )` |
| Method | CanRemoveColumn | 2014 | `public bool CanRemoveColumn ( int nIndex )` |
| Method | CanRemoveRow | 2014 | `public bool CanRemoveRow ( int nIndex )` |
| Method | ClearCell | — | `public void ClearCell ( int nRow , int nCol )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCellCalculatedValue | — | `` |
| Method | GetCellCategoryId | — | `` |
| Method | GetCellCombinedParameters | — | `` |
| Method | GetCellFormatOptions | — | `` |
| Method | GetCellParamId | — | `` |
| Method | GetCellSpec | — | `public ForgeTypeId GetCellSpec ( int nRow , int nCol )` |
| Method | GetCellText | — | `public string GetCellText ( int nRow , int nCol )` |
| Method | GetCellType | — | `` |
| Method | GetColumnWidth | — | `public double GetColumnWidth ( int nCol )` |
| Method | GetColumnWidthInPixels | — | `public int GetColumnWidthInPixels ( int nCol )` |
| Method | GetCustomFieldId | 2024 | `public Guid GetCustomFieldId ( int row , int col )` |
| Method | GetMergedCell | — | `public TableMergedCell GetMergedCell ( int nRow , int nCol )` |
| Method | GetRowHeight | — | `public double GetRowHeight ( int nRow )` |
| Method | GetRowHeightInPixels | — | `public int GetRowHeightInPixels ( int nRow )` |
| Method | GetTableCellStyle | — | `public TableCellStyle GetTableCellStyle ( int nRow , int nCol )` |
| Method | InsertColumn | 2015 | `public void InsertColumn ( int index )` |
| Method | InsertImage | 2014 | `public void InsertImage ( int nRow , int nColumn , ElementId imageSymbolId )` |
| Method | InsertRow | 2014 | `public void InsertRow ( int nIndex )` |
| Method | IsAcceptableParamIdAndCategoryId | — | `` |
| Method | IsCellFormattable | 2014 | `public bool IsCellFormattable ( int nRow , int nCol )` |
| Method | IsCellOverridden | — | `` |
| Method | IsDataOutOfDate | 2014 | `public bool IsDataOutOfDate ()` |
| Method | IsValidColumnNumber | 2014 | `public bool IsValidColumnNumber ( int nCol )` |
| Method | IsValidImageSymbolId | 2014 | `public bool IsValidImageSymbolId ( ElementId imageSymbolId )` |
| Method | IsValidRowNumber | 2014 | `public bool IsValidRowNumber ( int nRow )` |
| Method | MergeCells | — | `public void MergeCells ( TableMergedCell mergedCell )` |
| Method | RefreshData | 2014 | `public bool RefreshData ()` |
| Method | RemoveColumn | 2014 | `public void RemoveColumn ( int nIndex )` |
| Method | RemoveRow | 2014 | `public void RemoveRow ( int nIndex )` |
| Method | ResetCellOverride | — | `` |
| Method | SetCellCalculatedValue | — | `` |
| Method | SetCellCombinedParameters | — | `` |
| Method | SetCellFormatOptions | 2014 | `public void SetCellFormatOptions ( int nRow , int nCol , FormatOptions options )` |
| Method | SetCellParamIdAndCategoryId | — | `` |
| Method | SetCellStyle | — | `` |
| Method | SetCellText | — | `public void SetCellText ( int nRow , int nCol , string text )` |
| Method | SetCellType | — | `` |
| Method | SetColumnWidth | — | `public void SetColumnWidth ( int nCol , double width )` |
| Method | SetColumnWidthInPixels | — | `public void SetColumnWidthInPixels ( int nCol , int width )` |
| Method | SetMergedCell | — | `public void SetMergedCell ( int nRow , int nCol , TableMergedCell mergedCell )` |
| Method | SetRowHeight | — | `public void SetRowHeight ( int nRow , double height )` |
| Method | SetRowHeightInPixels | — | `public void SetRowHeightInPixels ( int nRow , int height )` |
| Property | FirstColumnNumber | 2014 | `public int FirstColumnNumber { get ; }` |
| Property | FirstRowNumber | 2014 | `public int FirstRowNumber { get ; }` |
| Property | HideSection | — | `public bool HideSection { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | LastColumnNumber | 2014 | `public int LastColumnNumber { get ; }` |
| Property | LastRowNumber | 2014 | `public int LastRowNumber { get ; }` |
| Property | NeedsRefresh | — | `public bool NeedsRefresh { get ; set ; }` |
| Property | NumberOfColumns | — | `public int NumberOfColumns { get ; set ; }` |
| Property | NumberOfRows | — | `public int NumberOfRows { get ; set ; }` |