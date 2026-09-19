---
type: CurveByPointsUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 12
tags: [revit-api, class]
---

# CurveByPointsUtils

`Autodesk.Revit.DB.CurveByPointsUtils` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddCurvesToFaceRegion | 2012 | `public static void AddCurvesToFaceRegion ( Document document , IList < ElementId > curveElemIds )` |
| Method | CreateArcThroughPoints | 2014 | `public static CurveElement CreateArcThroughPoints ( Document document , ReferencePoint startPoint , ReferencePoint endPoint , ReferencePoint interiorPoint )` |
| Method | CreateRectangle | 2012 | `public static void CreateRectangle ( Document document , ReferencePoint startPoint , ReferencePoint endPoint , CurveProjectionType projectionType , bool boundaryReferenceLines , bool boundaryCurvesFollowSurface , out ILi` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetFaceRegions | 2012 | `public static IList < Reference > GetFaceRegions ( Document cda , Reference referenceOfFace )` |
| Method | GetHostFace | 2012 | `public static Reference GetHostFace ( CurveElement curveElem )` |
| Method | GetProjectionType | 2012 | `public static CurveProjectionType GetProjectionType ( CurveElement curveElem )` |
| Method | GetSketchOnSurface | 2012 | `public static bool GetSketchOnSurface ( CurveElement curveElem )` |
| Method | SetProjectionType | 2012 | `public static void SetProjectionType ( CurveElement curveElem , CurveProjectionType value )` |
| Method | SetSketchOnSurface | 2012 | `public static void SetSketchOnSurface ( CurveElement curveElem , bool sketchOnSurface )` |
| Method | ValidateCurveElementIdArrayForFaceRegions | 2012 | `public static bool ValidateCurveElementIdArrayForFaceRegions ( Document document , IList < ElementId > curveElemIds )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |