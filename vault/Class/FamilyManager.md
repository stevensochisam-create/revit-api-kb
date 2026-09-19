---
type: FamilyManager
namespace: Autodesk.Revit.DB
version: 2024
members: 30
tags: [revit-api, class]
---

# FamilyManager

`Autodesk.Revit.DB.FamilyManager` · Revit 2024 · 30 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddParameter | — | `` |
| Method | AssociateElementParameterToFamilyParameter | — | `public void AssociateElementParameterToFamilyParameter ( Parameter elementParameter , FamilyParameter familyParameter )` |
| Method | CanElementParameterBeAssociated | — | `public bool CanElementParameterBeAssociated ( Parameter elementParameter )` |
| Method | DeleteCurrentType | — | `public void DeleteCurrentType ()` |
| Method | GetAssociatedFamilyParameter | — | `public FamilyParameter GetAssociatedFamilyParameter ( Parameter elementParameter )` |
| Method | GetParameter | 2022 | `public FamilyParameter GetParameter ( ForgeTypeId parameterTypeId )` |
| Method | GetParameters | 2015 | `public IList < FamilyParameter > GetParameters ()` |
| Method | IsParameterLockable | — | `public bool IsParameterLockable ( FamilyParameter familyParameter )` |
| Method | IsParameterLocked | — | `public bool IsParameterLocked ( FamilyParameter familyParameter )` |
| Method | IsUserAssignableParameterGroup | — | `` |
| Method | MakeInstance | — | `public void MakeInstance ( FamilyParameter familyParameter )` |
| Method | MakeNonReporting | 2011 | `public void MakeNonReporting ( FamilyParameter familyParameter )` |
| Method | MakeReporting | 2011 | `public void MakeReporting ( FamilyParameter familyParameter )` |
| Method | MakeType | — | `public void MakeType ( FamilyParameter familyParameter )` |
| Method | NewType | — | `public FamilyType NewType ( string typeName )` |
| Method | RemoveParameter | — | `public void RemoveParameter ( FamilyParameter familyParameter )` |
| Method | RenameCurrentType | — | `public void RenameCurrentType ( string typeName )` |
| Method | RenameParameter | — | `public void RenameParameter ( FamilyParameter familyParameter , string name )` |
| Method | ReorderParameters | 2015 | `public void ReorderParameters ( IList < FamilyParameter > parameters )` |
| Method | ReplaceParameter | — | `` |
| Method | Set | — | `` |
| Method | SetDescription | 2015 | `public void SetDescription ( FamilyParameter familyParameter , string description )` |
| Method | SetFormula | — | `public void SetFormula ( FamilyParameter familyParameter , string formula )` |
| Method | SetParameterLocked | — | `public void SetParameterLocked ( FamilyParameter familyParameter , bool locked )` |
| Method | SetValueString | — | `public void SetValueString ( FamilyParameter familyParameter , string value )` |
| Method | SortParameters | 2015 | `public void SortParameters ( ParametersOrder order )` |
| Property | CurrentType | — | `public FamilyType CurrentType { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | Parameters | — | `public FamilyParameterSet Parameters { get ; }` |
| Property | Types | — | `public FamilyTypeSet Types { get ; }` |