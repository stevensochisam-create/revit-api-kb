---
type: IFCProductWrapper
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 14
tags: [revit-api, class]
---

# IFCProductWrapper

`Autodesk.Revit.DB.IFC.IFCProductWrapper` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddAnnotation | 2012 | `public void AddAnnotation ( IFCAnyHandle annoHnd , IFCLevelInfo levelInfo , bool relateToLevel )` |
| Method | AddBuilding | 2012 | `public void AddBuilding ( IFCAnyHandle buildingHandle )` |
| Method | AddElement | 2013 | `public void AddElement ( IFCAnyHandle elementHandle , IFCLevelInfo pLevelInfo , IFCExtrusionCreationData params , bool relateToLevel )` |
| Method | AddFinishMaterial | 2013 | `public void AddFinishMaterial ( IFCAnyHandle material )` |
| Method | AddSite | 2013 | `public void AddSite ( IFCAnyHandle siteHandle )` |
| Method | AddSpace | 2012 | `public void AddSpace ( IFCAnyHandle spaceHandle , IFCLevelInfo pLevelInfo , IFCExtrusionCreationData pParams , bool relateToLevel )` |
| Method | ClearFinishMaterials | 2013 | `public void ClearFinishMaterials ()` |
| Method | Create | — | `` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | FindExtrusionCreationParameters | 2012 | `public IFCExtrusionCreationData FindExtrusionCreationParameters ( IFCAnyHandle elementHandle )` |
| Method | GetAllObjects | 2012 | `public ICollection < IFCAnyHandle > GetAllObjects ()` |
| Method | GetAnElement | 2013 | `public IFCAnyHandle GetAnElement ()` |
| Property | Count | 2012 | `public int Count { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |