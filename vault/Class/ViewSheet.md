---
type: ViewSheet
namespace: Autodesk.Revit.DB
version: 2024
members: 19
tags: [revit-api, class]
---

# ViewSheet

`Autodesk.Revit.DB.ViewSheet` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanBeDuplicated | 2023 | `public bool CanBeDuplicated ( SheetDuplicateOption duplicateOption )` |
| Method | ConvertToRealSheet | 2011 | `public void ConvertToRealSheet ( ElementId titleBlockTypeId )` |
| Method | Create | 2013 | `public static ViewSheet Create ( Document document , ElementId titleBlockTypeId )` |
| Method | CreatePlaceholder | 2011 | `public static ViewSheet CreatePlaceholder ( Document aDoc )` |
| Method | DeleteViewport | 2013 | `public void DeleteViewport ( Viewport viewport )` |
| Method | Duplicate | — | `` |
| Method | GetAdditionalRevisionIds | 2015 | `public ICollection < ElementId > GetAdditionalRevisionIds ()` |
| Method | GetAllPlacedViews | 2015 | `public ISet < ElementId > GetAllPlacedViews ()` |
| Method | GetAllRevisionCloudIds | 2023.1 | `public ISet < ElementId > GetAllRevisionCloudIds ()` |
| Method | GetAllRevisionIds | 2015 | `public IList < ElementId > GetAllRevisionIds ()` |
| Method | GetAllViewports | 2013 | `public ICollection < ElementId > GetAllViewports ()` |
| Method | GetCurrentRevision | 2015 | `public ElementId GetCurrentRevision ()` |
| Method | GetRevisionCloudNumberOnSheet | 2015 | `public string GetRevisionCloudNumberOnSheet ( ElementId revisionCloudId )` |
| Method | GetRevisionNumberOnSheet | 2015 | `public string GetRevisionNumberOnSheet ( ElementId revisionId )` |
| Method | Print | — | `` |
| Method | SetAdditionalRevisionIds | 2015 | `public void SetAdditionalRevisionIds ( ICollection < ElementId > projectRevisionIds )` |
| Property | IsPlaceholder | 2011 | `public bool IsPlaceholder { get ; }` |
| Property | Parameter | — | `` |
| Property | SheetNumber | — | `public string SheetNumber { get ; set ; }` |