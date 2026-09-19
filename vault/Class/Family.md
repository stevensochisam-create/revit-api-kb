---
type: Family
namespace: Autodesk.Revit.DB
version: 2024
members: 26
tags: [revit-api, class]
---

# Family

`Autodesk.Revit.DB.Family` · Revit 2024 · 26 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanHaveStructuralSection | 2016 | `public bool CanHaveStructuralSection ()` |
| Method | CanLoadFamilies | 2020.1 | `public static bool CanLoadFamilies ( Document document )` |
| Method | ExtractPartAtom | 2011 | `public void ExtractPartAtom ( string xmlFilePath )` |
| Method | GetFamilySymbolIds | 2015 | `public ISet < ElementId > GetFamilySymbolIds ()` |
| Method | GetFamilyTypeParameterValues | 2016 | `public ISet < ElementId > GetFamilyTypeParameterValues ( ElementId parameterId )` |
| Method | HasLargeSketches | 2017 | `public bool HasLargeSketches ()` |
| Method | IsAppropriateCategoryId | 2015 | `public bool IsAppropriateCategoryId ( ElementId categoryId )` |
| Property | CurtainPanelHorizontalSpacing | — | `public double CurtainPanelHorizontalSpacing { get ; set ; }` |
| Property | CurtainPanelTilePattern | — | `public TilePatternsBuiltIn CurtainPanelTilePattern { get ; }` |
| Property | CurtainPanelVerticalSpacing | — | `public double CurtainPanelVerticalSpacing { get ; set ; }` |
| Property | FamilyCategory | — | `public Category FamilyCategory { get ; set ; }` |
| Property | FamilyCategoryId | 2015 | `public ElementId FamilyCategoryId { get ; set ; }` |
| Property | FamilyPlacementType | 2013 | `public FamilyPlacementType FamilyPlacementType { get ; }` |
| Property | IsConceptualMassFamily | — | `public bool IsConceptualMassFamily { get ; }` |
| Property | IsCurtainPanelFamily | — | `public bool IsCurtainPanelFamily { get ; }` |
| Property | IsEditable | — | `public bool IsEditable { get ; }` |
| Property | IsInPlace | — | `public bool IsInPlace { get ; }` |
| Property | IsOwnerFamily | 2015 | `public bool IsOwnerFamily { get ; }` |
| Property | IsParametric | 2017 | `public bool IsParametric { get ; }` |
| Property | IsUserCreated | 2015 | `public bool IsUserCreated { get ; }` |
| Property | Parameter | — | `` |
| Property | ShowSpatialElementCalculationPoint | 2013 | `public bool ShowSpatialElementCalculationPoint { get ; set ; }` |
| Property | StructuralCodeName | 2016 | `public string StructuralCodeName { get ; set ; }` |
| Property | StructuralFamilyNameKey | 2016 | `public string StructuralFamilyNameKey { get ; set ; }` |
| Property | StructuralMaterialType | — | `public StructuralMaterialType StructuralMaterialType { get ; }` |
| Property | StructuralSectionShape | 2015 | `public StructuralSectionShape StructuralSectionShape { get ; set ; }` |