---
type: DirectShape
namespace: Autodesk.Revit.DB
version: 2024
members: 38
tags: [revit-api, class]
---

# DirectShape

`Autodesk.Revit.DB.DirectShape` · Revit 2024 · 38 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddExternallyTaggedGeometry | 2022 | `public void AddExternallyTaggedGeometry ( ExternallyTaggedGeometryObject externallyTaggedGeometry )` |
| Method | AddReferenceCurve | — | `` |
| Method | AddReferencePlane | — | `` |
| Method | AddReferencePoint | — | `` |
| Method | AppendShape | — | `` |
| Method | AreOptionsValid | 2016 | `public bool AreOptionsValid ( DirectShapeOptions options )` |
| Method | AreOptionsValidForTransientDirectShape | 2016 | `public bool AreOptionsValidForTransientDirectShape ( DirectShapeOptions options )` |
| Method | AreValidDirectShapeReferenceOptions | 2024 | `public bool AreValidDirectShapeReferenceOptions ( DirectShapeReferenceOptions options )` |
| Method | CanCreateParts | 2020 | `public bool CanCreateParts ()` |
| Method | CreateElement | 2017 | `public static DirectShape CreateElement ( Document document , ElementId categoryId )` |
| Method | CreateElementInstance | 2017 | `public static DirectShape CreateElementInstance ( Document document , ElementId typeId , ElementId categoryId , string definitionId , Transform trf )` |
| Method | CreateGeometryInstance | 2015 | `public static IList < GeometryObject > CreateGeometryInstance ( Document document , string definition_id , Transform trf )` |
| Method | GetExternallyTaggedGeometry | 2022 | `public ExternallyTaggedGeometryObject GetExternallyTaggedGeometry ( ExternalGeometryId externalId )` |
| Method | GetExternallyTaggedReference | 2024 | `public Reference GetExternallyTaggedReference ( ExternalGeometryId externalId )` |
| Method | GetOptions | 2016 | `public DirectShapeOptions GetOptions ()` |
| Method | HasExternalGeometry | 2022 | `public bool HasExternalGeometry ( ExternalGeometryId externalId )` |
| Method | HasExternallyTaggedReference | 2024 | `public bool HasExternallyTaggedReference ( ExternalGeometryId externalId )` |
| Method | IsSupportedDocument | 2017 | `public static bool IsSupportedDocument ( Document document )` |
| Method | IsValidCategoryId | 2015 | `public static bool IsValidCategoryId ( ElementId categoryId , Document doc )` |
| Method | IsValidGeometry | 2015 | `public bool IsValidGeometry ( Solid Geom )` |
| Method | IsValidReferenceCurve | 2022 | `public static bool IsValidReferenceCurve ( Curve curve )` |
| Method | IsValidReferencePlaneBoundingBoxUV | 2022 | `public static bool IsValidReferencePlaneBoundingBoxUV ( BoundingBoxUV boundingBoxUV )` |
| Method | IsValidShape | — | `` |
| Method | IsValidTypeId | 2015 | `public bool IsValidTypeId ( ElementId typeId )` |
| Method | IsValidUsage | 2024 | `public bool IsValidUsage ( ExternallyTaggedGeometryObject externallyTaggedGeometry )` |
| Method | RemoveAllReferenceObjects | 2024 | `public void RemoveAllReferenceObjects ()` |
| Method | RemoveExternallyTaggedGeometry | 2022 | `public void RemoveExternallyTaggedGeometry ( ExternalGeometryId externalId )` |
| Method | RemoveReferenceObject | — | `` |
| Method | ResetExternallyTaggedGeometry | 2022 | `public void ResetExternallyTaggedGeometry ()` |
| Method | SetName | 2015 | `public void SetName ( string name )` |
| Method | SetOptions | 2016 | `public void SetOptions ( DirectShapeOptions options )` |
| Method | SetShape | — | `` |
| Method | SetTypeId | 2015 | `public void SetTypeId ( ElementId typeId )` |
| Method | UpdateExternallyTaggedGeometry | 2022 | `public void UpdateExternallyTaggedGeometry ( ExternallyTaggedGeometryObject externallyTaggedGeometry )` |
| Property | ApplicationDataId | 2017 | `public string ApplicationDataId { get ; set ; }` |
| Property | ApplicationId | 2017 | `public string ApplicationId { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | TypeId | 2015 | `public ElementId TypeId { get ; }` |