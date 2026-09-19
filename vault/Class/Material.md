---
type: Material
namespace: Autodesk.Revit.DB
version: 2024
members: 25
tags: [revit-api, class]
---

# Material

`Autodesk.Revit.DB.Material` · Revit 2024 · 25 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ClearMaterialAspect | — | `public void ClearMaterialAspect ( MaterialAspect aspect )` |
| Method | Create | — | `public static ElementId Create ( Document document , string name )` |
| Method | Duplicate | — | `public Material Duplicate ( string name )` |
| Method | IsMaterialOrValidDefault | — | `public static bool IsMaterialOrValidDefault ( Element pElem , ElementId materialId )` |
| Method | IsNameUnique | 2015 | `public static bool IsNameUnique ( Document aDocument , string name )` |
| Method | SetMaterialAspectByPropertySet | — | `public void SetMaterialAspectByPropertySet ( MaterialAspect aspect , ElementId propertySetId )` |
| Property | AppearanceAssetId | 2014 | `public ElementId AppearanceAssetId { get ; set ; }` |
| Property | Color | — | `public Color Color { get ; set ; }` |
| Property | CutBackgroundPatternColor | 2019 | `public Color CutBackgroundPatternColor { get ; set ; }` |
| Property | CutBackgroundPatternId | 2019 | `public ElementId CutBackgroundPatternId { get ; set ; }` |
| Property | CutForegroundPatternColor | 2019 | `public Color CutForegroundPatternColor { get ; set ; }` |
| Property | CutForegroundPatternId | 2019 | `public ElementId CutForegroundPatternId { get ; set ; }` |
| Property | MaterialCategory | 2015 | `public string MaterialCategory { get ; set ; }` |
| Property | MaterialClass | — | `public string MaterialClass { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | Shininess | — | `public int Shininess { get ; set ; }` |
| Property | Smoothness | — | `public int Smoothness { get ; set ; }` |
| Property | StructuralAssetId | — | `public ElementId StructuralAssetId { get ; set ; }` |
| Property | SurfaceBackgroundPatternColor | 2019 | `public Color SurfaceBackgroundPatternColor { get ; set ; }` |
| Property | SurfaceBackgroundPatternId | 2019 | `public ElementId SurfaceBackgroundPatternId { get ; set ; }` |
| Property | SurfaceForegroundPatternColor | 2019 | `public Color SurfaceForegroundPatternColor { get ; set ; }` |
| Property | SurfaceForegroundPatternId | 2019 | `public ElementId SurfaceForegroundPatternId { get ; set ; }` |
| Property | ThermalAssetId | — | `public ElementId ThermalAssetId { get ; set ; }` |
| Property | Transparency | — | `public int Transparency { get ; set ; }` |
| Property | UseRenderAppearanceForShading | 2015 | `public bool UseRenderAppearanceForShading { get ; set ; }` |