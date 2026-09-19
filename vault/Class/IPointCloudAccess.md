---
type: IPointCloudAccess
namespace: Autodesk.Revit.DB.PointClouds
version: 2024
members: 8
tags: [revit-api, class]
---

# IPointCloudAccess

`Autodesk.Revit.DB.PointClouds.IPointCloudAccess` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreatePointSetIterator | — | `` |
| Method | Free | 2012 | `void Free ()` |
| Method | GetColorEncoding | 2012 | `PointCloudColorEncoding GetColorEncoding ()` |
| Method | GetExtent | 2012 | `Outline GetExtent ()` |
| Method | GetName | 2012 | `string GetName ()` |
| Method | GetOffset | 2012 | `XYZ GetOffset ()` |
| Method | GetUnitsToFeetConversionFactor | 2012 | `double GetUnitsToFeetConversionFactor ()` |
| Method | ReadPoints | 2012 | `int ReadPoints ( PointCloudFilter rFilter , ElementId viewId , IntPtr buffer , int nBufferSize )` |