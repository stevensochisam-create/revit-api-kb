---
type: DatumPlane
namespace: Autodesk.Revit.DB
version: 2024
members: 18
tags: [revit-api, class]
---

# DatumPlane

`Autodesk.Revit.DB.DatumPlane` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddLeader | 2016 | `public Leader AddLeader ( DatumEnds datumEnd , View view )` |
| Method | CanBeVisibleInView | 2016 | `public bool CanBeVisibleInView ( View view )` |
| Method | GetCurvesInView | 2016 | `public IList < Curve > GetCurvesInView ( DatumExtentType extentMode , View view )` |
| Method | GetDatumExtentTypeInView | 2016 | `public DatumExtentType GetDatumExtentTypeInView ( DatumEnds datumEnd , View view )` |
| Method | GetLeader | 2016 | `public Leader GetLeader ( DatumEnds datumEnd , View view )` |
| Method | GetPropagationViews | 2016 | `public ISet < ElementId > GetPropagationViews ( View view )` |
| Method | HasBubbleInView | 2016 | `public bool HasBubbleInView ( DatumEnds datumEnd , View view )` |
| Method | HideBubbleInView | 2016 | `public void HideBubbleInView ( DatumEnds datumEnd , View view )` |
| Method | IsBubbleVisibleInView | 2016 | `public bool IsBubbleVisibleInView ( DatumEnds datumEnd , View view )` |
| Method | IsCurveValidInView | 2016 | `public bool IsCurveValidInView ( DatumExtentType extentMode , View view , Curve curve )` |
| Method | IsLeaderValid | 2016 | `public bool IsLeaderValid ( DatumEnds datumEnd , View view , Leader leader )` |
| Method | Maximize3DExtents | 2016 | `public void Maximize3DExtents ()` |
| Method | PropagateToViews | 2016 | `public void PropagateToViews ( View view , ISet < ElementId > parallelViews )` |
| Method | SetCurveInView | 2016 | `public void SetCurveInView ( DatumExtentType extentMode , View view , Curve curve )` |
| Method | SetDatumExtentType | 2016 | `public void SetDatumExtentType ( DatumEnds datumEnd , View view , DatumExtentType extentMode )` |
| Method | SetLeader | 2016 | `public void SetLeader ( DatumEnds datumEnd , View view , Leader pLeader )` |
| Method | ShowBubbleInView | 2016 | `public void ShowBubbleInView ( DatumEnds datumEnd , View view )` |
| Property | Parameter | — | `` |