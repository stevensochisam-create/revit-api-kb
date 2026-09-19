---
type: MultiReferenceAnnotationOptions
namespace: Autodesk.Revit.DB
version: 2024
members: 17
tags: [revit-api, class]
---

# MultiReferenceAnnotationOptions

`Autodesk.Revit.DB.MultiReferenceAnnotationOptions` · Revit 2024 · 17 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | MultiReferenceAnnotationOptions | 2014 | `public MultiReferenceAnnotationOptions ( MultiReferenceAnnotationType multiReferenceAnnotationType )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | ElementsMatchReferenceCategory | 2014 | `public bool ElementsMatchReferenceCategory ( ICollection < ElementId > elements )` |
| Method | GetAdditionalReferencesToDimension | 2020 | `public IList < Reference > GetAdditionalReferencesToDimension ()` |
| Method | GetElementsToDimension | 2014 | `public ICollection < ElementId > GetElementsToDimension ()` |
| Method | IsAllowedDimensionStyleType | 2014 | `public bool IsAllowedDimensionStyleType ( DimensionStyleType dimensionStyleType )` |
| Method | ReferencesDontMatchReferenceCategory | 2020 | `public bool ReferencesDontMatchReferenceCategory ( IList < Reference > references )` |
| Method | SetAdditionalReferencesToDimension | 2020 | `public void SetAdditionalReferencesToDimension ( IList < Reference > referencesToDimension )` |
| Method | SetElementsToDimension | 2014 | `public void SetElementsToDimension ( ICollection < ElementId > elementsToDimension )` |
| Property | DimensionLineDirection | 2014 | `public XYZ DimensionLineDirection { get ; set ; }` |
| Property | DimensionLineOrigin | 2014 | `public XYZ DimensionLineOrigin { get ; set ; }` |
| Property | DimensionPlaneNormal | 2014 | `public XYZ DimensionPlaneNormal { get ; set ; }` |
| Property | DimensionStyleType | 2014 | `public DimensionStyleType DimensionStyleType { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | MultiReferenceAnnotationType | 2014 | `public MultiReferenceAnnotationType MultiReferenceAnnotationType { get ; }` |
| Property | TagHasLeader | 2014 | `public bool TagHasLeader { get ; set ; }` |
| Property | TagHeadPosition | 2014 | `public XYZ TagHeadPosition { get ; set ; }` |