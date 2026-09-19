---
type: ImageInstance
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# ImageInstance

`Autodesk.Revit.DB.ImageInstance` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2020 | `public static ImageInstance Create ( Document document , View view , ElementId imageTypeId , ImagePlacementOptions placementOptions )` |
| Method | GetLocation | 2020 | `public XYZ GetLocation ( BoxPlacement placementPoint )` |
| Method | IsValidView | 2020 | `public static bool IsValidView ( View view )` |
| Method | SetLocation | 2020 | `public void SetLocation ( XYZ newLocation , BoxPlacement placementPoint )` |
| Property | CanHaveSnaps | 2020 | `public bool CanHaveSnaps { get ; }` |
| Property | DrawLayer | 2020 | `public DrawLayer DrawLayer { get ; set ; }` |
| Property | EnableSnaps | 2020 | `public bool EnableSnaps { get ; set ; }` |
| Property | Height | 2020 | `public double Height { get ; set ; }` |
| Property | HeightScale | 2020 | `public double HeightScale { get ; set ; }` |
| Property | LockProportions | 2020 | `public bool LockProportions { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | Width | 2020 | `public double Width { get ; set ; }` |
| Property | WidthScale | 2020 | `public double WidthScale { get ; set ; }` |