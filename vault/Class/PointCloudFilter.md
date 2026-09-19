---
type: PointCloudFilter
namespace: Autodesk.Revit.DB.PointClouds
version: 2024
members: 6
tags: [revit-api, class]
---

# PointCloudFilter

`Autodesk.Revit.DB.PointClouds.PointCloudFilter` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Clone | 2012 | `public PointCloudFilter Clone ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | PrepareForCell | 2012 | `public void PrepareForCell ( XYZ min , XYZ max , int numTests )` |
| Method | TestCell | 2012 | `public int TestCell ( XYZ min , XYZ max )` |
| Method | TestPoint | — | `public virtual bool TestPoint ( CloudPoint point )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |