---
type: RevitLinkType
namespace: Autodesk.Revit.DB
version: 2024
members: 27
tags: [revit-api, class]
---

# RevitLinkType

`Autodesk.Revit.DB.RevitLinkType` · Revit 2024 · 27 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | CreateFromIFC | — | `` |
| Method | GetChildIds | 2012 | `public ICollection < ElementId > GetChildIds ()` |
| Method | GetConversionData | 2015 | `public LinkConversionData GetConversionData ()` |
| Method | GetLinkedFileStatus | 2018.2 | `public LinkedFileStatus GetLinkedFileStatus ()` |
| Method | GetParentId | 2012 | `public ElementId GetParentId ()` |
| Method | GetPhaseMap | 2018.3 | `public IDictionary < ElementId , ElementId > GetPhaseMap ()` |
| Method | GetRootId | 2012 | `public ElementId GetRootId ()` |
| Method | GetTopLevelLink | — | `` |
| Method | HasSaveablePositions | 2012 | `public bool HasSaveablePositions ()` |
| Method | IsFromLocalPath | 2015 | `public bool IsFromLocalPath ()` |
| Method | IsFromRevitServer | 2015 | `public bool IsFromRevitServer ()` |
| Method | IsLoaded | 2012 | `public static bool IsLoaded ( Document document , ElementId typeId )` |
| Method | IsNotLoadedIntoMultipleOpenDocuments | 2014 | `public bool IsNotLoadedIntoMultipleOpenDocuments ()` |
| Method | Load | 2014 | `public LinkLoadResult Load ()` |
| Method | LoadFrom | — | `` |
| Method | Reload | 2015 | `public LinkLoadResult Reload ()` |
| Method | RevertLocalUnloadStatus | 2016 Subscription Update | `public LinkedFileStatus RevertLocalUnloadStatus ()` |
| Method | SavePositions | 2014 | `public bool SavePositions ( ISaveSharedCoordinatesCallback callback )` |
| Method | Unload | 2014 | `public void Unload ( ISaveSharedCoordinatesCallback callback )` |
| Method | UnloadLocally | 2016 Subscripton Update | `public bool UnloadLocally ( ISaveSharedCoordinatesCallbackForUnloadLocally callback )` |
| Method | UpdateFromIFC | — | `` |
| Property | AttachmentType | 2012 | `public AttachmentType AttachmentType { get ; set ; }` |
| Property | IsNestedLink | 2012 | `public bool IsNestedLink { get ; }` |
| Property | LocallyUnloaded | 2012 | `public bool LocallyUnloaded { get ; }` |
| Property | Parameter | — | `` |
| Property | PathType | 2014 | `public PathType PathType { get ; set ; }` |