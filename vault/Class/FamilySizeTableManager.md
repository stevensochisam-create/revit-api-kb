---
type: FamilySizeTableManager
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# FamilySizeTableManager

`Autodesk.Revit.DB.FamilySizeTableManager` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateFamilySizeTableManager | 2014 | `public static bool CreateFamilySizeTableManager ( Document document , ElementId familyId )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | ExportSizeTable | 2014 | `public bool ExportSizeTable ( string tableName , string filePath )` |
| Method | GetAllSizeTableNames | 2014 | `public IList < string > GetAllSizeTableNames ()` |
| Method | GetFamilySizeTableManager | 2014 | `public static FamilySizeTableManager GetFamilySizeTableManager ( Document document , ElementId familyId )` |
| Method | GetSizeTable | 2014 | `public FamilySizeTable GetSizeTable ( string tableName )` |
| Method | HasSizeTable | 2014 | `public bool HasSizeTable ( string tableName )` |
| Method | ImportSizeTable | 2014 | `public bool ImportSizeTable ( Document document , string filePath , FamilySizeTableErrorInfo errorInfo )` |
| Method | RemoveSizeTable | 2014 | `public bool RemoveSizeTable ( string tableName )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | NumberOfSizeTables | 2014 | `public int NumberOfSizeTables { get ; }` |