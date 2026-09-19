---
type: Element
namespace: Autodesk.Revit.DB
version: 2024
members: 81
tags: [revit-api, class]
---

# Element

`Autodesk.Revit.DB.Element` · Revit 2024 · 81 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ArePhasesModifiable | 2013 | `public bool ArePhasesModifiable ()` |
| Method | CanBeHidden | — | `public bool CanBeHidden ( View pView )` |
| Method | CanBeLocked | 2014 | `public bool CanBeLocked ()` |
| Method | CanDeleteSubelement | 2018 | `public bool CanDeleteSubelement ( Subelement subelem )` |
| Method | CanHaveTypeAssigned | — | `` |
| Method | CanHaveTypeAssigned | 2011 | `public bool CanHaveTypeAssigned ()` |
| Method | ChangeTypeId | — | `` |
| Method | DeleteEntity | — | `public bool DeleteEntity ( Schema schema )` |
| Method | DeleteSubelement | 2018 | `public bool DeleteSubelement ( Subelement subelem )` |
| Method | DeleteSubelements | 2018 | `public bool DeleteSubelements ( IList < Subelement > subelems )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | EvaluateAllParameterValues | 2024 | `public IList < EvaluatedParameter > EvaluateAllParameterValues ()` |
| Method | EvaluateParameterValues | 2024 | `public IList < EvaluatedParameter > EvaluateParameterValues ( ISet < ElementId > parameterIds )` |
| Method | GetChangeTypeAny | — | `public static ChangeType GetChangeTypeAny ()` |
| Method | GetChangeTypeElementAddition | — | `public static ChangeType GetChangeTypeElementAddition ()` |
| Method | GetChangeTypeElementDeletion | — | `public static ChangeType GetChangeTypeElementDeletion ()` |
| Method | GetChangeTypeGeometry | — | `public static ChangeType GetChangeTypeGeometry ()` |
| Method | GetChangeTypeParameter | — | `` |
| Method | GetDependentElements | 2018.1 | `public IList < ElementId > GetDependentElements ( ElementFilter filter )` |
| Method | GetEntity | — | `public Entity GetEntity ( Schema schema )` |
| Method | GetEntitySchemaGuids | 2014 | `public IList < Guid > GetEntitySchemaGuids ()` |
| Method | GetExternalFileReference | 2012 | `public ExternalFileReference GetExternalFileReference ()` |
| Method | GetExternalResourceReference | 2015 | `public ExternalResourceReference GetExternalResourceReference ( ExternalResourceType resourceType )` |
| Method | GetExternalResourceReferenceExpanded | 2023 | `public IList < ExternalResourceReference > GetExternalResourceReferenceExpanded ( ExternalResourceType resourceType )` |
| Method | GetExternalResourceReferences | 2015 | `public IDictionary < ExternalResourceType , ExternalResourceReference > GetExternalResourceReferences ()` |
| Method | GetExternalResourceReferencesExpanded | 2023 | `public IDictionary < ExternalResourceType , IList < ExternalResourceReference >> GetExternalResourceReferencesExpanded ()` |
| Method | GetGeneratingElementIds | 2012 | `public ICollection < ElementId > GetGeneratingElementIds ( GeometryObject geometryObject )` |
| Method | GetGeometryObjectFromReference | 2012 | `public GeometryObject GetGeometryObjectFromReference ( Reference reference )` |
| Method | GetMaterialArea | 2014 | `public double GetMaterialArea ( ElementId materialId , bool usePaintMaterial )` |
| Method | GetMaterialIds | 2014 | `public ICollection < ElementId > GetMaterialIds ( bool returnPaintMaterials )` |
| Method | GetMaterialVolume | 2014 | `public double GetMaterialVolume ( ElementId materialId )` |
| Method | GetMonitoredLinkElementIds | 2011 | `public IList < ElementId > GetMonitoredLinkElementIds ()` |
| Method | GetMonitoredLocalElementIds | 2011 | `public IList < ElementId > GetMonitoredLocalElementIds ()` |
| Method | GetOrderedParameters | 2015 | `public IList < Parameter > GetOrderedParameters ()` |
| Method | GetParameter | 2022 | `public Parameter GetParameter ( ForgeTypeId parameterTypeId )` |
| Method | GetParameterFormatOptions | 2014 | `public FormatOptions GetParameterFormatOptions ( ElementId parameterId )` |
| Method | GetParameters | 2015 | `public IList < Parameter > GetParameters ( string name )` |
| Method | GetPhaseStatus | — | `public ElementOnPhaseStatus GetPhaseStatus ( ElementId phaseId )` |
| Method | GetSubelements | 2018 | `public IList < Subelement > GetSubelements ()` |
| Method | GetTypeId | 2011 | `public ElementId GetTypeId ()` |
| Method | GetValidTypes | — | `` |
| Method | GetValidTypes | 2011 | `public ICollection < ElementId > GetValidTypes ()` |
| Method | HasPhases | 2013 | `public bool HasPhases ()` |
| Method | IsCreatedPhaseOrderValid | 2022 | `public bool IsCreatedPhaseOrderValid ( ElementId createdPhaseId )` |
| Method | IsDemolishedPhaseOrderValid | 2022 | `public bool IsDemolishedPhaseOrderValid ( ElementId demolishedPhaseId )` |
| Method | IsExternalFileReference | 2012 | `public bool IsExternalFileReference ()` |
| Method | IsHidden | — | `public bool IsHidden ( View pView )` |
| Method | IsMonitoringLinkElement | 2011 | `public bool IsMonitoringLinkElement ()` |
| Method | IsMonitoringLocalElement | 2011 | `public bool IsMonitoringLocalElement ()` |
| Method | IsPhaseCreatedValid | 2013 | `public bool IsPhaseCreatedValid ( ElementId createdPhaseId )` |
| Method | IsPhaseDemolishedValid | 2013 | `public bool IsPhaseDemolishedValid ( ElementId demolishedPhaseId )` |
| Method | IsValidType | — | `` |
| Method | LookupParameter | 2015 | `public Parameter LookupParameter ( string name )` |
| Method | RefersToExternalResourceReference | 2015 | `public bool RefersToExternalResourceReference ( ExternalResourceType resourceType )` |
| Method | RefersToExternalResourceReferences | 2015 | `public bool RefersToExternalResourceReferences ()` |
| Method | SetEntity | — | `public void SetEntity ( Entity entity )` |
| Property | AssemblyInstanceId | — | `public ElementId AssemblyInstanceId { get ; }` |
| Property | BoundingBox | — | `public BoundingBoxXYZ this [ View A_0 ] { get ; }` |
| Property | Category | — | `public Category Category { get ; }` |
| Property | CreatedPhaseId | 2013 | `public ElementId CreatedPhaseId { get ; set ; }` |
| Property | DemolishedPhaseId | 2013 | `public ElementId DemolishedPhaseId { get ; set ; }` |
| Property | DesignOption | — | `public DesignOption DesignOption { get ; }` |
| Property | Document | — | `public Document Document { get ; }` |
| Property | Geometry | — | `public GeometryElement this [ Options options ] { get ; }` |
| Property | GroupId | 2014 | `public ElementId GroupId { get ; }` |
| Property | Id | — | `public ElementId Id { get ; }` |
| Property | IsModifiable | 2023 | `public bool IsModifiable { get ; }` |
| Property | IsTransient | 2016 | `public bool IsTransient { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | LevelId | 2014 | `public ElementId LevelId { get ; }` |
| Property | Location | — | `public virtual Location Location { get ; }` |
| Property | Name | — | `public virtual string Name { get ; set ; }` |
| Property | OwnerViewId | — | `public ElementId OwnerViewId { get ; }` |
| Property | Parameter | — | `` |
| Property | Parameters | — | `public ParameterSet Parameters { get ; }` |
| Property | ParametersMap | — | `public ParameterMap ParametersMap { get ; }` |
| Property | Pinned | — | `public bool Pinned { get ; set ; }` |
| Property | UniqueId | — | `public string UniqueId { get ; }` |
| Property | VersionGuid | 2021 | `public Guid VersionGuid { get ; }` |
| Property | ViewSpecific | — | `public bool ViewSpecific { get ; }` |
| Property | WorksetId | — | `public WorksetId WorksetId { get ; }` |