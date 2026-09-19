---
type: Subelement
namespace: Autodesk.Revit.DB
version: 2024
members: 21
tags: [revit-api, class]
---

# Subelement

`Autodesk.Revit.DB.Subelement` · Revit 2024 · 21 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanHaveTypeAssigned | 2018 | `public bool CanHaveTypeAssigned ()` |
| Method | ChangeTypeId | 2018 | `public void ChangeTypeId ( ElementId typeId )` |
| Method | Create | 2018 | `public static Subelement Create ( Document aDoc , Reference reference )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAllParameters | 2018 | `public IList < ElementId > GetAllParameters ()` |
| Method | GetBoundingBox | 2018 | `public BoundingBoxXYZ GetBoundingBox ( View dbView )` |
| Method | GetGeometryObject | 2018 | `public GeometryObject GetGeometryObject ( View dbView )` |
| Method | GetParameterValue | 2018 | `public ParameterValue GetParameterValue ( ElementId parameterId )` |
| Method | GetReference | 2018 | `public Reference GetReference ()` |
| Method | GetValidTypes | 2018 | `public ISet < ElementId > GetValidTypes ()` |
| Method | HasParameter | 2018 | `public bool HasParameter ( ElementId parameterId )` |
| Method | IsParameterModifiable | 2018 | `public bool IsParameterModifiable ( ElementId parameterId )` |
| Method | IsValidSubelementReference | 2018 | `public static bool IsValidSubelementReference ( Document aDoc , Reference reference )` |
| Method | IsValidType | 2018 | `public bool IsValidType ( ElementId typeId )` |
| Method | SetParameterValue | 2018 | `public void SetParameterValue ( ElementId parameterId , ParameterValue pValue )` |
| Property | Category | — | `public Category Category { get ; }` |
| Property | Document | 2018 | `public Document Document { get ; }` |
| Property | Element | 2018 | `public Element Element { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | TypeId | 2018 | `public ElementId TypeId { get ; }` |
| Property | UniqueId | 2018 | `public string UniqueId { get ; }` |