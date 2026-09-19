---
type: StructuralConnectionType
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 7
tags: [revit-api, class]
---

# StructuralConnectionType

`Autodesk.Revit.DB.Structure.StructuralConnectionType` · Revit 2024 · 7 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2011 | `public static StructuralConnectionType Create ( Document doc , StructuralConnectionApplyTo applyTo , string name , ElementId familySymbolId )` |
| Method | GetAllStructuralConnectionTypeIds | 2011 | `public static void GetAllStructuralConnectionTypeIds ( Document cda , out ICollection < ElementId > ids )` |
| Method | GetFamilySymbolId | 2011 | `public ElementId GetFamilySymbolId ()` |
| Method | SetFamilySymbolId | 2011 | `public void SetFamilySymbolId ( ElementId familySymbolId )` |
| Method | ValidFamilySymbolId | 2011 | `public static bool ValidFamilySymbolId ( Document doc , StructuralConnectionApplyTo applyTo , ElementId familySymbolId )` |
| Property | ApplyTo | 2011 | `public StructuralConnectionApplyTo ApplyTo { get ; }` |
| Property | Parameter | — | `` |