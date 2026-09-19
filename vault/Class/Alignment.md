---
type: Alignment
namespace: Autodesk.Revit.DB.Infrastructure
version: 2024
members: 21
tags: [revit-api, class]
---

# Alignment

`Autodesk.Revit.DB.Infrastructure.Alignment` · Revit 2024 · 21 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Get | — | `` |
| Method | GetAlignments | — | `` |
| Method | GetClosestPoint | 2021.1 | `public XYZ GetClosestPoint ( XYZ point )` |
| Method | GetClosestStation | 2021.1 | `public double GetClosestStation ( XYZ point )` |
| Method | GetDisplayedHorizontalCurveEndpoints | 2021.1 | `public IList < HorizontalCurveEndpoint > GetDisplayedHorizontalCurveEndpoints ()` |
| Method | GetDistance | 2021.1 | `public double GetDistance ( double fromStation , double toStation )` |
| Method | GetHCurveNormalAtStation | 2021.1 | `public XYZ GetHCurveNormalAtStation ( double station )` |
| Method | GetHCurveTangentAtStation | 2021.1 | `public XYZ GetHCurveTangentAtStation ( double station )` |
| Method | GetPointAtStation | 2021.1 | `public XYZ GetPointAtStation ( double station )` |
| Method | GetVCurveNormalAtStation | 2021.1 | `public XYZ GetVCurveNormalAtStation ( double station )` |
| Method | GetVCurveTangentAtStation | 2021.1 | `public XYZ GetVCurveTangentAtStation ( double station )` |
| Method | IsValid | — | `` |
| Method | IsValid | 2021.1 | `public bool IsValid ()` |
| Property | Description | 2021.1 | `public string Description { get ; }` |
| Property | DisplayedEndStation | 2021.1 | `public double DisplayedEndStation { get ; }` |
| Property | DisplayedStartStation | 2021.1 | `public double DisplayedStartStation { get ; }` |
| Property | Element | 2021.1 | `public Element Element { get ; }` |
| Property | EndStation | 2022 | `public double EndStation { get ; }` |
| Property | GUID | 2021.1 | `public Guid GUID { get ; }` |
| Property | Name | 2021.1 | `public string Name { get ; }` |
| Property | StartStation | 2022 | `public double StartStation { get ; }` |