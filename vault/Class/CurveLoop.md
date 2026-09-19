---
type: CurveLoop
namespace: Autodesk.Revit.DB
version: 2024
members: 23
tags: [revit-api, class]
---

# CurveLoop

`Autodesk.Revit.DB.CurveLoop` · Revit 2024 · 23 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | CurveLoop | 2012 | `public CurveLoop ()` |
| Method | Append | 2012 | `public void Append ( Curve curve )` |
| Method | Create | 2012 | `public static CurveLoop Create ( IList < Curve > curves )` |
| Method | CreateViaCopy | 2012 | `public static CurveLoop CreateViaCopy ( CurveLoop original )` |
| Method | CreateViaOffset | — | `` |
| Method | CreateViaThicken | — | `` |
| Method | CreateViaTransform | 2016 | `public static CurveLoop CreateViaTransform ( CurveLoop curveLoop , Transform transform )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | Flip | 2012 | `public void Flip ()` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetCurveLoopIterator | 2013 | `public CurveLoopIterator GetCurveLoopIterator ()` |
| Method | GetEnumerator | — | `public virtual IEnumerator < Curve > GetEnumerator ()` |
| Method | GetExactLength | 2012 | `public double GetExactLength ()` |
| Method | GetPlane | 2012 | `public Plane GetPlane ()` |
| Method | GetRectangularHeight | 2012 | `public double GetRectangularHeight ( Plane plane )` |
| Method | GetRectangularWidth | 2012 | `public double GetRectangularWidth ( Plane plane )` |
| Method | HasPlane | 2013 | `public bool HasPlane ()` |
| Method | IsCounterclockwise | 2012 | `public bool IsCounterclockwise ( XYZ normal )` |
| Method | IsOpen | 2012 | `public bool IsOpen ()` |
| Method | IsRectangular | 2012 | `public bool IsRectangular ( Plane plane )` |
| Method | NumberOfCurves | 2019.1 | `public int NumberOfCurves ()` |
| Method | Transform | 2016 | `public void Transform ( Transform transform )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |