---
type: PointCloudInstance
namespace: Autodesk.Revit.DB
version: 2024
members: 12
tags: [revit-api, class]
---

# PointCloudInstance

`Autodesk.Revit.DB.PointCloudInstance` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ContainsScan | 2014 | `public bool ContainsScan ( string scanName )` |
| Method | Create | — | `public static PointCloudInstance Create ( Document document , ElementId typeId , Transform transform )` |
| Method | GetPoints | 2014 | `public PointCollection GetPoints ( PointCloudFilter filter , double averageDistance , int numPoints )` |
| Method | GetRegions | 2017 | `public IList < string > GetRegions ()` |
| Method | GetScanOrigin | 2014 | `public XYZ GetScanOrigin ( string scanName )` |
| Method | GetScans | 2014 | `public IList < string > GetScans ()` |
| Method | GetSelectionFilter | — | `public PointCloudFilter GetSelectionFilter ()` |
| Method | HasColor | 2014 | `public bool HasColor ()` |
| Method | SetSelectionFilter | — | `public void SetSelectionFilter ( PointCloudFilter pFilter )` |
| Property | FilterAction | — | `public SelectionFilterAction FilterAction { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | SupportsOverrides | 2014 | `public bool SupportsOverrides { get ; }` |