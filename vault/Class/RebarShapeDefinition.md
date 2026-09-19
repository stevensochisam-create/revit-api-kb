---
type: RebarShapeDefinition
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 14
tags: [revit-api, class]
---

# RebarShapeDefinition

`Autodesk.Revit.DB.Structure.RebarShapeDefinition` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddFormulaParameter | 2009 | `public void AddFormulaParameter ( ElementId paramId , string formula )` |
| Method | AddParameter | 2009 | `public void AddParameter ( ElementId paramId , double defaultValue )` |
| Method | CheckDefaultParameterValues | 2009 | `public bool CheckDefaultParameterValues ( double bendRadius , double barDiameter )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetParameterDefaultValue | 2009 | `public double GetParameterDefaultValue ( ElementId paramId )` |
| Method | GetParameterFormula | 2009 | `public string GetParameterFormula ( ElementId paramId )` |
| Method | GetParameters | 2009 | `public IList < ElementId > GetParameters ()` |
| Method | HasParameter | 2009 | `public bool HasParameter ( ElementId paramId )` |
| Method | RemoveParameter | 2009 | `public void RemoveParameter ( ElementId paramId )` |
| Method | SetParameterDefaultValue | 2009 | `public void SetParameterDefaultValue ( ElementId paramId , double value )` |
| Method | SetParameterFormula | 2009 | `public void SetParameterFormula ( ElementId paramId , string formula )` |
| Property | Complete | 2009 | `public bool Complete { get ; }` |
| Property | IsPlanar | 2012 | `public bool IsPlanar { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |