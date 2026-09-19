---
type: ExporterIFC
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 41
tags: [revit-api, class]
---

# ExporterIFC

`Autodesk.Revit.DB.IFC.ExporterIFC` · Revit 2024 · 41 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddBuildingStorey | 2013 | `public void AddBuildingStorey ( ElementId id , IFCLevelInfo levelInfo )` |
| Method | ClearFaceWithElementHandleMap | 2014 | `public void ClearFaceWithElementHandleMap ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | FindSpaceBoundingElementHandle | 2013 | `public IFCAnyHandle FindSpaceBoundingElementHandle ( ElementId id , ElementId levelId )` |
| Method | Get2DContextHandle | 2012 | `public IFCAnyHandle Get2DContextHandle ()` |
| Method | Get3DContextHandle | 2012 | `public IFCAnyHandle Get3DContextHandle ( string subContextName )` |
| Method | GetDoorWindowOpeningHandle | 2014 | `public IFCAnyHandle GetDoorWindowOpeningHandle ( ElementId familyInstanceId )` |
| Method | GetFamilyName | 2013 | `public string GetFamilyName ()` |
| Method | GetFile | 2012 | `public IFCFile GetFile ()` |
| Method | GetHostObjects | 2013 | `public IList < IDictionary < ElementId , IFCAnyHandle >> GetHostObjects ()` |
| Method | GetLayerNameForPresentationLayer | 2022 | `public string GetLayerNameForPresentationLayer ( Element pElement , ElementId categoryId )` |
| Method | GetLevelInfo | 2012 | `public IFCLevelInfo GetLevelInfo ( ElementId levelId )` |
| Method | GetLevelInfos | 2012 | `public IDictionary < ElementId , IFCLevelInfo > GetLevelInfos ()` |
| Method | GetMaterialIdForCurrentExportState | 2013 | `public ElementId GetMaterialIdForCurrentExportState ()` |
| Method | GetOptions | 2013 | `public IDictionary < string , string > GetOptions ()` |
| Method | GetOrCreateFillPattern | 2013 | `public IFCAnyHandle GetOrCreateFillPattern ( ElementId fillPatternId , Color color , double planScale )` |
| Method | GetPresentationLayerAssignments | 2022 | `public IDictionary < string , IList < IFCAnyHandle >> GetPresentationLayerAssignments ()` |
| Method | GetRelatedElements | 2013 | `public ICollection < IFCAnyHandle > GetRelatedElements ()` |
| Method | GetRelatedProducts | 2013 | `public ICollection < IFCAnyHandle > GetRelatedProducts ()` |
| Method | PopExportState | 2012 | `public void PopExportState ()` |
| Method | PopTransform | 2014 | `public void PopTransform ()` |
| Method | PushExportState | 2012 | `public void PushExportState ( Element Elem , GeometryElement GRep )` |
| Method | PushTransform | 2014 | `public void PushTransform ( Transform trf )` |
| Method | RegisterDoorWindowForUncreatedOpening | 2012 | `public void RegisterDoorWindowForUncreatedOpening ( ElementId familyInstanceId , IFCAnyHandle instanceHandle )` |
| Method | RegisterFaceWithElementHandle | 2014 | `public void RegisterFaceWithElementHandle ( Face face , IFCAnyHandle elemHandle )` |
| Method | RegisterSpaceBoundingElementHandle | 2012 | `public void RegisterSpaceBoundingElementHandle ( IFCAnyHandle instanceHandle , ElementId id , ElementId levelId )` |
| Method | RemoveBuildingStorey | 2013 | `public void RemoveBuildingStorey ( ElementId id )` |
| Method | Set2DContextHandle | 2013 | `public void Set2DContextHandle ( IFCAnyHandle contextHandle )` |
| Method | Set3DContextHandle | 2013 | `public void Set3DContextHandle ( IFCAnyHandle contextHandle , string subContextName )` |
| Method | SetCurrentExportedDocument | 2023.1 | `public void SetCurrentExportedDocument ( Document pDocument )` |
| Method | SetFile | 2012 | `public void SetFile ( IFCFile file )` |
| Method | SetMaterialIdForCurrentExportState | 2012 | `public void SetMaterialIdForCurrentExportState ( ElementId elementId )` |
| Method | SetOwnerHistoryHandle | 2013 | `public void SetOwnerHistoryHandle ( IFCAnyHandle ownerHistory )` |
| Property | ExportAs2x2 | 2012 | `public bool ExportAs2x2 { get ; }` |
| Property | ExportAs2x3 | 2012 | `public bool ExportAs2x3 { get ; }` |
| Property | ExportBaseQuantities | 2012 | `public bool ExportBaseQuantities { get ; }` |
| Property | FileName | 2012 | `public string FileName { get ; }` |
| Property | FileVersion | 2012 | `public IFCVersion FileVersion { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | SpaceBoundaryLevel | 2012 | `public int SpaceBoundaryLevel { get ; }` |
| Property | WallAndColumnSplitting | 2012 | `public bool WallAndColumnSplitting { get ; }` |