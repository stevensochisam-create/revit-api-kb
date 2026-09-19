---
type: Pipe
namespace: Autodesk.Revit.DB.Plumbing
version: 2024
members: 11
tags: [revit-api, class]
---

# Pipe

`Autodesk.Revit.DB.Plumbing.Pipe` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | CreatePlaceholder | 2014 | `public static Pipe CreatePlaceholder ( Document document , ElementId systemTypeId , ElementId pipeTypeId , ElementId levelId , XYZ startPoint , XYZ endPoint )` |
| Method | IsPipeTypeId | 2011 | `public static bool IsPipeTypeId ( Document document , ElementId pipeTypeId )` |
| Method | IsPipingConnector | 2016 | `public static bool IsPipingConnector ( Connector connector )` |
| Method | IsPipingSystemTypeId | 2014 | `public static bool IsPipingSystemTypeId ( Document document , ElementId systemTypeId )` |
| Method | SetSystemType | 2015 | `public void SetSystemType ( ElementId systemTypeId )` |
| Property | FlowState | — | `public PipeFlowState FlowState { get ; }` |
| Property | IsPlaceholder | — | `public bool IsPlaceholder { get ; }` |
| Property | Parameter | — | `` |
| Property | PipeSegment | 2017 | `public PipeSegment PipeSegment { get ; }` |
| Property | PipeType | — | `public PipeType PipeType { get ; set ; }` |