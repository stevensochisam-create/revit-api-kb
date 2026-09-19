---
type: TableView
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# TableView

`Autodesk.Revit.DB.TableView` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetAvailableParameterCategories | — | `public IList < ElementId > GetAvailableParameterCategories ( SectionType sectionType , int row )` |
| Method | GetAvailableParameters | — | `public static IList < ElementId > GetAvailableParameters ( Document cda , ElementId categoryId )` |
| Method | GetCalculatedValueName | — | `public string GetCalculatedValueName ( SectionType sectionType , int row , int column )` |
| Method | GetCalculatedValueText | — | `public string GetCalculatedValueText ( SectionType sectionType , int row , int column )` |
| Method | GetCellText | 2014 | `public string GetCellText ( SectionType sectionType , int row , int column )` |
| Method | IsValidSectionType | 2014 | `public bool IsValidSectionType ( SectionType sectionType )` |
| Method | Print | — | `` |
| Property | MaximumColumnWidth | — | `public int MaximumColumnWidth { get ; }` |
| Property | MaximumGridWidth | 2014 | `public int MaximumGridWidth { get ; }` |
| Property | MaximumRowHeight | — | `public int MaximumRowHeight { get ; }` |
| Property | MinimumColumnWidth | 2014 | `public int MinimumColumnWidth { get ; }` |
| Property | MinimumRowHeight | 2014 | `public int MinimumRowHeight { get ; }` |
| Property | Parameter | — | `` |
| Property | TargetId | — | `public ElementId TargetId { get ; set ; }` |