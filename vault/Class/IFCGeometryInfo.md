---
type: IFCGeometryInfo
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 9
tags: [revit-api, class]
---

# IFCGeometryInfo

`Autodesk.Revit.DB.IFC.IFCGeometryInfo` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateCurveGeometryInfo | 2017 | `public static IFCGeometryInfo CreateCurveGeometryInfo ( ExporterIFC ExporterIFC , Transform lcs , XYZ projectionDir , bool planViewOnly )` |
| Method | CreateFaceGeometryInfo | — | `` |
| Method | CreateSurfaceGeometryInfo | 2012 | `public static IFCGeometryInfo CreateSurfaceGeometryInfo ( double epsilon )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCurves | 2012 | `public IList < IFCAnyHandle > GetCurves ()` |
| Method | GetFaces | 2012 | `public IList < ICollection < IFCAnyHandle >> GetFaces ()` |
| Method | GetRepresentations | 2013 | `public ICollection < IFCAnyHandle > GetRepresentations ()` |
| Method | GetSurfaces | 2012 | `public ICollection < IFCAnyHandle > GetSurfaces ()` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |