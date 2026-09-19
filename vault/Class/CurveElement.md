---
type: CurveElement
namespace: Autodesk.Revit.DB
version: 2024
members: 19
tags: [revit-api, class]
---

# CurveElement

`Autodesk.Revit.DB.CurveElement` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateAreaBasedLoadBoundaryLine | 2023 | `public static CurveElement CreateAreaBasedLoadBoundaryLine ( Document document , Curve curve , ElementId levelId )` |
| Method | CreateAreaBasedLoadBoundaryLines | 2023 | `public static IList < CurveElement > CreateAreaBasedLoadBoundaryLines ( Document document , IList < Curve > curves , ElementId levelId )` |
| Method | GetAdjoinedCurveElements | 2017 | `public ISet < ElementId > GetAdjoinedCurveElements ( int end )` |
| Method | GetAreaBasedLoadBoundaryLineData | 2023 | `public AreaBasedLoadBoundaryLineData GetAreaBasedLoadBoundaryLineData ()` |
| Method | GetLineStyleIds | — | `public ICollection < ElementId > GetLineStyleIds ()` |
| Method | GetTangentLock | 2017 | `public bool GetTangentLock ( int end , ElementId other )` |
| Method | HasTangentJoin | 2017 | `public bool HasTangentJoin ( int end , ElementId other )` |
| Method | HasTangentLocks | 2017 | `public bool HasTangentLocks ( int end )` |
| Method | IsAdjoinedCurveElement | 2017 | `public bool IsAdjoinedCurveElement ( int end , ElementId other )` |
| Method | SetGeometryCurve | 2015 | `public void SetGeometryCurve ( Curve curve , bool overrideJoins )` |
| Method | SetSketchPlaneAndCurve | 2015 | `public void SetSketchPlaneAndCurve ( SketchPlane sketchPlane , Curve curve )` |
| Method | SetTangentLock | 2017 | `public void SetTangentLock ( int end , ElementId other , bool state )` |
| Property | CenterPointReference | — | `public Reference CenterPointReference { get ; }` |
| Property | CurveElementType | — | `public CurveElementType CurveElementType { get ; }` |
| Property | GeometryCurve | — | `public Curve GeometryCurve { get ; set ; }` |
| Property | LineStyle | — | `public Element LineStyle { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | SketchPlane | — | `public virtual SketchPlane SketchPlane { get ; set ; }` |
| Property | SupportsTangentLocks | — | `public bool SupportsTangentLocks { get ; }` |