---
type: RebarTrimExtendData
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 10
tags: [revit-api, class]
---

# RebarTrimExtendData

`Autodesk.Revit.DB.Structure.RebarTrimExtendData` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddBarGeometry | — | `` |
| Method | CanAddBarGeometry | 2018 | `public bool CanAddBarGeometry ()` |
| Method | ClearAllAddedBarGeometry | 2018 | `public void ClearAllAddedBarGeometry ()` |
| Method | CreateEndConstraint | 2018 | `public bool CreateEndConstraint ( IList < Reference > targetReferences , bool isConstraintToCover , double offsetValue )` |
| Method | CreateStartConstraint | 2018 | `public bool CreateStartConstraint ( IList < Reference > targetReferences , bool isConstraintToCover , double offsetValue )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAddedBarGeometry | 2018 | `public IList < Curve > GetAddedBarGeometry ( int barIndex )` |
| Method | GetNumberOfBarGeometry | 2018 | `public int GetNumberOfBarGeometry ()` |
| Method | GetRebarUpdateCurvesData | 2018 | `public RebarUpdateCurvesData GetRebarUpdateCurvesData ()` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |