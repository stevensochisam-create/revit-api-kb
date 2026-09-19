---
type: StairsPath
namespace: Autodesk.Revit.DB.Architecture
version: 2024
members: 13
tags: [revit-api, class]
---

# StairsPath

`Autodesk.Revit.DB.Architecture.StairsPath` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanCreateOnMultistoryStairs | 2013 | `public static bool CanCreateOnMultistoryStairs ( Document document , LinkElementId multistoryStairsId )` |
| Method | Create | 2013 | `public static StairsPath Create ( Document document , LinkElementId stairsId , ElementId typeId , ElementId planViewId )` |
| Method | CreateOnMultistoryStairs | 2018 | `public static IList < StairsPath > CreateOnMultistoryStairs ( Document document , LinkElementId multistoryStairsId , ElementId typeId )` |
| Property | DownText | 2013 | `public string DownText { get ; set ; }` |
| Property | DownTextOffset | 2013 | `public XYZ DownTextOffset { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | ShowDownText | 2013 | `public bool ShowDownText { get ; set ; }` |
| Property | ShowUpText | 2013 | `public bool ShowUpText { get ; set ; }` |
| Property | StairsId | 2013 | `public LinkElementId StairsId { get ; }` |
| Property | StairsPathOffset | 2013 | `public double StairsPathOffset { get ; set ; }` |
| Property | TextOrientation | 2013 | `public StairsTextOrientation TextOrientation { get ; set ; }` |
| Property | UpText | 2013 | `public string UpText { get ; set ; }` |
| Property | UpTextOffset | 2013 | `public XYZ UpTextOffset { get ; set ; }` |