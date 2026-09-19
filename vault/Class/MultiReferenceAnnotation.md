---
type: MultiReferenceAnnotation
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# MultiReferenceAnnotation

`Autodesk.Revit.DB.MultiReferenceAnnotation` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreElementsValidForMultiReferenceAnnotation | 2020 | `public static bool AreElementsValidForMultiReferenceAnnotation ( Document document , MultiReferenceAnnotationOptions options )` |
| Method | AreReferencesValidForLinearDimension | 2014 | `public static bool AreReferencesValidForLinearDimension ( Document document , ElementId ownerViewId , MultiReferenceAnnotationOptions options )` |
| Method | AreReferencesValidForLinearFixedDimension | 2014 | `public static bool AreReferencesValidForLinearFixedDimension ( Document document , ElementId ownerViewId , MultiReferenceAnnotationOptions options )` |
| Method | Create | 2014 | `public static MultiReferenceAnnotation Create ( Document document , ElementId ownerViewId , MultiReferenceAnnotationOptions options )` |
| Method | Is3DViewValidForDimension | 2020 | `public static bool Is3DViewValidForDimension ( Document document , ElementId ownerViewId , MultiReferenceAnnotationOptions options )` |
| Method | IsLinearFixedDimensionDirectionValid | 2014 | `public static bool IsLinearFixedDimensionDirectionValid ( Document document , ElementId viewId , MultiReferenceAnnotationOptions options )` |
| Property | DimensionId | 2014 | `public ElementId DimensionId { get ; }` |
| Property | Parameter | — | `` |
| Property | TagId | 2014 | `public ElementId TagId { get ; }` |