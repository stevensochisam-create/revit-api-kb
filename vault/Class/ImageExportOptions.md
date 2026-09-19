---
type: ImageExportOptions
namespace: Autodesk.Revit.DB
version: 2024
members: 19
tags: [revit-api, class]
---

# ImageExportOptions

`Autodesk.Revit.DB.ImageExportOptions` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ImageExportOptions | 2011 | `public ImageExportOptions ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetFileName | 2015 | `public static string GetFileName ( Document aDoc , ElementId dbViewId )` |
| Method | GetViewsAndSheets | 2011 | `public IList < ElementId > GetViewsAndSheets ()` |
| Method | IsValidFileName | 2011 | `public static bool IsValidFileName ( string filePath )` |
| Method | IsValidForSaveToProjectAsImage | 2011 | `public static bool IsValidForSaveToProjectAsImage ( ImageExportOptions options , Document doc )` |
| Method | SetViewsAndSheets | 2011 | `public void SetViewsAndSheets ( IList < ElementId > viewsAndSheets )` |
| Property | ExportRange | 2011 | `public ExportRange ExportRange { get ; set ; }` |
| Property | FilePath | 2011 | `public string FilePath { get ; set ; }` |
| Property | FitDirection | 2011 | `public FitDirectionType FitDirection { get ; set ; }` |
| Property | HLRandWFViewsFileType | 2011 | `public ImageFileType HLRandWFViewsFileType { get ; set ; }` |
| Property | ImageResolution | 2011 | `public ImageResolution ImageResolution { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | PixelSize | 2011 | `public int PixelSize { get ; set ; }` |
| Property | ShadowViewsFileType | 2011 | `public ImageFileType ShadowViewsFileType { get ; set ; }` |
| Property | ShouldCreateWebSite | 2011 | `public bool ShouldCreateWebSite { get ; set ; }` |
| Property | ViewName | 2011 | `public string ViewName { get ; set ; }` |
| Property | Zoom | 2011 | `public int Zoom { get ; set ; }` |
| Property | ZoomType | 2011 | `public ZoomFitType ZoomType { get ; set ; }` |