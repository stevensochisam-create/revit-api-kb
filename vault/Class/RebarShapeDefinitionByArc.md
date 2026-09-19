---
type: RebarShapeDefinitionByArc
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 11
tags: [revit-api, class]
---

# RebarShapeDefinitionByArc

`Autodesk.Revit.DB.Structure.RebarShapeDefinitionByArc` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | RebarShapeDefinitionByArc | — | `` |
| Method | AddConstraintArcLength | 2009 | `public void AddConstraintArcLength ( ElementId paramId )` |
| Method | AddConstraintChordLength | 2009 | `public void AddConstraintChordLength ( ElementId paramId )` |
| Method | AddConstraintCircumference | 2009 | `public void AddConstraintCircumference ( ElementId paramId , RebarShapeArcReferenceType arcRefType )` |
| Method | AddConstraintDiameter | 2009 | `public void AddConstraintDiameter ( ElementId paramId , RebarShapeArcReferenceType arcRefType )` |
| Method | AddConstraintRadius | 2009 | `public void AddConstraintRadius ( ElementId paramId , RebarShapeArcReferenceType arcRefType )` |
| Method | AddConstraintSagittaLength | 2009 | `public void AddConstraintSagittaLength ( ElementId paramId )` |
| Method | GetConstraints | 2012 | `public IList < RebarShapeConstraint > GetConstraints ()` |
| Method | SetArcTypeSpiral | 2011 | `public void SetArcTypeSpiral ( double height , double pitch , int baseFinishingTurns , int topFinishingTurns )` |
| Method | SetConstraints | 2012 | `public void SetConstraints ( IList < RebarShapeConstraint > constraints )` |
| Property | Type | 2009 | `public RebarShapeDefinitionByArcType Type { get ; set ; }` |