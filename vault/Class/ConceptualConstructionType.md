---
type: ConceptualConstructionType
namespace: Autodesk.Revit.DB.Analysis
version: 2024
members: 15
tags: [revit-api, class]
---

# ConceptualConstructionType

`Autodesk.Revit.DB.Analysis.ConceptualConstructionType` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetAllConceptualConstructionsForCategory | 2012 | `public static ICollection < ElementId > GetAllConceptualConstructionsForCategory ( Document ccda , ElementId massSubCategoryId )` |
| Method | GetFloorOrSlabConstructionType | 2012 | `public static ElementId GetFloorOrSlabConstructionType ( Document ccda , ConceptualConstructionFloorSlabType typeEnum )` |
| Method | GetGBSId | 2012 | `public int GetGBSId ( ElementId massSurfaceSubCategoryId )` |
| Method | GetOpeningConstructionType | 2012 | `public static ElementId GetOpeningConstructionType ( Document ccda , ConceptualConstructionOpeningType typeEnum )` |
| Method | GetRoofConstructionType | 2012 | `public static ElementId GetRoofConstructionType ( Document ccda , ConceptualConstructionRoofType typeEnum )` |
| Method | GetShadeConstructionType | 2012 | `public static ElementId GetShadeConstructionType ( Document ccda , ConceptualConstructionShadeType typeEnum )` |
| Method | GetWallConstructionType | 2012 | `public static ElementId GetWallConstructionType ( Document ccda , ConceptualConstructionWallType typeEnum )` |
| Method | GetWindowOrSkylightConstructionType | 2012 | `public static ElementId GetWindowOrSkylightConstructionType ( Document ccda , ConceptualConstructionWindowSkylightType typeEnum )` |
| Method | IsValidConceptualConstructionId | 2012 | `public static bool IsValidConceptualConstructionId ( Document ccda , ElementId constructionTypeId )` |
| Method | IsValidConceptualConstructionIdForCategory | 2012 | `public static bool IsValidConceptualConstructionIdForCategory ( Document ccda , ElementId constructionTypeId , ElementId massSubcategoryId )` |
| Method | IsValidSubcategoryForMassSurfaceDatas | 2012 | `public static bool IsValidSubcategoryForMassSurfaceDatas ( ElementId massSubCategoryId )` |
| Method | IsValidSurfaceSubcategoryForConstruction | 2012 | `public bool IsValidSurfaceSubcategoryForConstruction ( ElementId massSurfaceSubcategoryId )` |
| Property | MassSurfaceSubCategoryId | 2012 | `public ElementId MassSurfaceSubCategoryId { get ; }` |
| Property | MaterialId | 2012 | `public ElementId MaterialId { get ; set ; }` |
| Property | Parameter | — | `` |