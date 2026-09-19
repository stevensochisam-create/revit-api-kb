---
type: ViewCropRegionShapeManager
namespace: Autodesk.Revit.DB
version: 2024
members: 26
tags: [revit-api, class]
---

# ViewCropRegionShapeManager

`Autodesk.Revit.DB.ViewCropRegionShapeManager` · Revit 2024 · 26 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAnnotationCropShape | 2016 | `public CurveLoop GetAnnotationCropShape ()` |
| Method | GetCropShape | 2016 | `public IList < CurveLoop > GetCropShape ()` |
| Method | GetSplitRegionMaximum | 2016 | `public double GetSplitRegionMaximum ( int regionIndex )` |
| Method | GetSplitRegionMinimum | 2016 | `public double GetSplitRegionMinimum ( int regionIndex )` |
| Method | GetSplitRegionOffset | 2021 | `public XYZ GetSplitRegionOffset ( int regionIndex )` |
| Method | IsCropRegionShapeValid | 2014 | `public bool IsCropRegionShapeValid ( CurveLoop boundary )` |
| Method | RemoveCropRegionShape | 2014 | `public void RemoveCropRegionShape ()` |
| Method | RemoveSplit | 2014 | `public void RemoveSplit ()` |
| Method | RemoveSplitRegion | 2016 | `public void RemoveSplitRegion ( int regionIndex )` |
| Method | SetCropShape | 2014 | `public void SetCropShape ( CurveLoop boundary )` |
| Method | SplitRegionHorizontally | 2016 | `public void SplitRegionHorizontally ( int regionIndex , double leftPart , double rightPart )` |
| Method | SplitRegionVertically | 2016 | `public void SplitRegionVertically ( int regionIndex , double topPart , double bottomPart )` |
| Property | BottomAnnotationCropOffset | 2016 | `public double BottomAnnotationCropOffset { get ; set ; }` |
| Property | CanBeSplit | 2016 | `public bool CanBeSplit { get ; }` |
| Property | CanHaveAnnotationCrop | 2016 | `public bool CanHaveAnnotationCrop { get ; }` |
| Property | CanHaveShape | 2016 | `public bool CanHaveShape { get ; }` |
| Property | IsSplitHorizontally | 2016 | `public bool IsSplitHorizontally { get ; }` |
| Property | IsSplitVertically | 2016 | `public bool IsSplitVertically { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | LeftAnnotationCropOffset | 2016 | `public double LeftAnnotationCropOffset { get ; set ; }` |
| Property | NumberOfSplitRegions | 2016 | `public int NumberOfSplitRegions { get ; }` |
| Property | RightAnnotationCropOffset | 2016 | `public double RightAnnotationCropOffset { get ; set ; }` |
| Property | ShapeSet | 2014 | `public bool ShapeSet { get ; }` |
| Property | Split | 2014 | `public bool Split { get ; }` |
| Property | TopAnnotationCropOffset | 2016 | `public double TopAnnotationCropOffset { get ; set ; }` |