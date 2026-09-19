---
type: PlumbingUtils
namespace: Autodesk.Revit.DB.Plumbing
version: 2024
members: 7
tags: [revit-api, class]
---

# PlumbingUtils

`Autodesk.Revit.DB.Plumbing.PlumbingUtils` · Revit 2024 · 7 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | BreakCurve | 2017 | `public static ElementId BreakCurve ( Document document , ElementId pipeId , XYZ ptBreak )` |
| Method | ConnectPipePlaceholdersAtCross | — | `` |
| Method | ConnectPipePlaceholdersAtElbow | — | `` |
| Method | ConnectPipePlaceholdersAtTee | — | `` |
| Method | ConvertPipePlaceholders | 2012 | `public static ICollection < ElementId > ConvertPipePlaceholders ( Document document , ICollection < ElementId > placeholderIds )` |
| Method | HasOpenConnector | 2014 | `public static bool HasOpenConnector ( Document document , ElementId elemId )` |
| Method | PlaceCapOnOpenEnds | 2014 | `public static void PlaceCapOnOpenEnds ( Document document , ElementId elemId , ElementId typeId )` |