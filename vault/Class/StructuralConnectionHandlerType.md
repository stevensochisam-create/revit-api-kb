---
type: StructuralConnectionHandlerType
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 12
tags: [revit-api, class]
---

# StructuralConnectionHandlerType

`Autodesk.Revit.DB.Structure.StructuralConnectionHandlerType` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddElementsToCustomConnection | 2017 | `public static void AddElementsToCustomConnection ( StructuralConnectionHandler structuralConnectionHandler , IList < Reference > references )` |
| Method | Create | — | `` |
| Method | CreateDefaultStructuralConnectionHandlerType | 2017 | `public static ElementId CreateDefaultStructuralConnectionHandlerType ( Document pADoc )` |
| Method | FindGenericConnectionType | 2017 | `public static ElementId FindGenericConnectionType ( Document doc )` |
| Method | GetDefaultConnectionHandlerType | 2017 | `public static ElementId GetDefaultConnectionHandlerType ( Document pADoc )` |
| Method | IsCustom | 2019 | `public bool IsCustom ()` |
| Method | IsDetailed | 2019 | `public bool IsDetailed ()` |
| Method | IsGeneric | 2019 | `public bool IsGeneric ()` |
| Method | IsTypeNameValidForCustomConnection | 2017 | `public static bool IsTypeNameValidForCustomConnection ( Document document , string typeName )` |
| Method | RemoveMainSubelementsFromCustomConnection | 2017 | `public static void RemoveMainSubelementsFromCustomConnection ( StructuralConnectionHandler structuralConnectionHandler , IList < Subelement > subelements )` |
| Property | ConnectionGuid | 2017 | `public Guid ConnectionGuid { get ; }` |
| Property | Parameter | — | `` |