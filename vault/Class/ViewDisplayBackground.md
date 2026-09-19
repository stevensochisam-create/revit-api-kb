---
type: ViewDisplayBackground
namespace: Autodesk.Revit.DB
version: 2024
members: 15
tags: [revit-api, class]
---

# ViewDisplayBackground

`Autodesk.Revit.DB.ViewDisplayBackground` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateGradient | 2014 | `public static ViewDisplayBackground CreateGradient ( Color skyColor , Color horizonColor , Color groundColor )` |
| Method | CreateImage | 2014 | `public static ViewDisplayBackground CreateImage ( string imagePath , ViewDisplayBackgroundImageFlags flags , UV imageOffsets , UV imageScales )` |
| Method | CreateSky | 2014 | `public static ViewDisplayBackground CreateSky ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Property | BackgroundColor | 2014 | `public Color BackgroundColor { get ; }` |
| Property | GroundColor | 2014 | `public Color GroundColor { get ; }` |
| Property | HorizontalImageOffset | 2014 | `public double HorizontalImageOffset { get ; }` |
| Property | HorizontalImageScale | 2014 | `public double HorizontalImageScale { get ; }` |
| Property | ImageFlags | 2014 | `public ViewDisplayBackgroundImageFlags ImageFlags { get ; }` |
| Property | ImagePath | 2014 | `public string ImagePath { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | SkyColor | 2014 | `public Color SkyColor { get ; }` |
| Property | Type | 2014 | `public ViewDisplayBackgroundType Type { get ; }` |
| Property | VerticalImageOffset | 2014 | `public double VerticalImageOffset { get ; }` |
| Property | VerticalImageScale | 2014 | `public double VerticalImageScale { get ; }` |