---
type: ExternalResourceBrowserData
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# ExternalResourceBrowserData

`Autodesk.Revit.DB.ExternalResourceBrowserData` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ExternalResourceBrowserData | 2015 | `public ExternalResourceBrowserData ( Document document , Guid serverId , string folderPath , ExternalResourceMatchOptions matchOptions )` |
| Method | AddResource | — | `` |
| Method | AddSubFolder | — | `` |
| Method | CallingDocumentHasModelPath | 2015 | `public bool CallingDocumentHasModelPath ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCallingDocumentModelPath | 2015 | `public ModelPath GetCallingDocumentModelPath ()` |
| Method | GetMatchOptions | 2015 | `public ExternalResourceMatchOptions GetMatchOptions ()` |
| Method | GetResources | 2015 | `public IList < ExternalResourceReference > GetResources ()` |
| Method | GetSubFoldersData | 2019.1 | `public IList < ExternalResourceSubFolder > GetSubFoldersData ()` |
| Method | IsValidFolderName | 2015 | `public bool IsValidFolderName ( string folderName )` |
| Method | IsValidResourceName | 2018 | `public bool IsValidResourceName ( string resourceName )` |
| Property | FolderPath | 2015 | `public string FolderPath { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | ServerId | 2015 | `public Guid ServerId { get ; }` |