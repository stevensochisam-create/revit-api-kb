---
type: DisplacementElement
namespace: Autodesk.Revit.DB
version: 2024
members: 23
tags: [revit-api, class]
---

# DisplacementElement

`Autodesk.Revit.DB.DisplacementElement` · Revit 2024 · 23 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanCategoryBeDisplaced | 2014 | `public static bool CanCategoryBeDisplaced ( ElementId categoryId )` |
| Method | CanElementsBeAddedToDisplacementSet | 2014 | `public bool CanElementsBeAddedToDisplacementSet ( ICollection < ElementId > toDisplace )` |
| Method | CanElementsBeDisplaced | — | `` |
| Method | Create | 2014 | `public static DisplacementElement Create ( Document document , ICollection < ElementId > elementsToDisplace , XYZ displacement , View ownerDBView , DisplacementElement parentDisplacementElement )` |
| Method | GetAbsoluteDisplacement | 2014 | `public XYZ GetAbsoluteDisplacement ()` |
| Method | GetAdditionalElementsToDisplace | 2014 | `public static ICollection < ElementId > GetAdditionalElementsToDisplace ( Document document , View view , ElementId idToDisplace )` |
| Method | GetChildren | 2014 | `public IList < DisplacementElement > GetChildren ()` |
| Method | GetDisplacedElementIds | — | `` |
| Method | GetDisplacedElementIds | 2014 | `public ICollection < ElementId > GetDisplacedElementIds ()` |
| Method | GetDisplacedElementIdsFromAllChildren | 2014 | `public ICollection < ElementId > GetDisplacedElementIdsFromAllChildren ()` |
| Method | GetDisplacementElementId | 2014 | `public static ElementId GetDisplacementElementId ( View view , ElementId id )` |
| Method | GetDisplacementElementIds | 2014 | `public static ICollection < ElementId > GetDisplacementElementIds ( View view )` |
| Method | GetRelativeDisplacement | 2014 | `public XYZ GetRelativeDisplacement ()` |
| Method | IsAllowedAsDisplacedElement | 2014 | `public static bool IsAllowedAsDisplacedElement ( Element element )` |
| Method | IsElementDisplacedInView | 2014 | `public static bool IsElementDisplacedInView ( View view , ElementId id )` |
| Method | IsNotEmpty | 2014 | `public static bool IsNotEmpty ( ICollection < ElementId > elementIds )` |
| Method | IsValidAsParentInView | 2014 | `public static bool IsValidAsParentInView ( View view , DisplacementElement parent )` |
| Method | RemoveDisplacedElement | 2014 | `public void RemoveDisplacedElement ( Element ElemToRemove )` |
| Method | ResetDisplacedElements | 2014 | `public void ResetDisplacedElements ()` |
| Method | SetDisplacedElementIds | 2014 | `public void SetDisplacedElementIds ( ICollection < ElementId > displacedElemIds )` |
| Method | SetRelativeDisplacement | 2014 | `public void SetRelativeDisplacement ( XYZ displacement )` |
| Property | Parameter | — | `` |
| Property | ParentId | 2014 | `public ElementId ParentId { get ; }` |