---
type: AssemblyInstance
namespace: Autodesk.Revit.DB
version: 2024
members: 20
tags: [revit-api, class]
---

# AssemblyInstance

`Autodesk.Revit.DB.AssemblyInstance` · Revit 2024 · 20 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddMemberIds | 2012 | `public void AddMemberIds ( ICollection < ElementId > memberIds )` |
| Method | AllowsAssemblyViewCreation | 2012 | `public bool AllowsAssemblyViewCreation ()` |
| Method | AreElementsValidForAssembly | 2012 | `public static bool AreElementsValidForAssembly ( Document document , ICollection < ElementId > assemblyMemberIds , ElementId assemblyId )` |
| Method | CanRemoveElementsFromAssembly | 2012 | `public static bool CanRemoveElementsFromAssembly ( AssemblyInstance assemblyInstance , ICollection < ElementId > memberIds )` |
| Method | CompareAssemblyInstances | 2012 | `public static AssemblyDifference CompareAssemblyInstances ( AssemblyInstance instance1 , AssemblyInstance instance2 )` |
| Method | Create | 2012 | `public static AssemblyInstance Create ( Document document , ICollection < ElementId > assemblyMemberIds , ElementId namingCategoryId )` |
| Method | Disassemble | 2012 | `public ICollection < ElementId > Disassemble ()` |
| Method | GetCenter | 2012 | `public XYZ GetCenter ()` |
| Method | GetMemberIds | 2012 | `public ICollection < ElementId > GetMemberIds ()` |
| Method | GetTransform | 2013 | `public Transform GetTransform ()` |
| Method | IsMember | 2022 | `public bool IsMember ( ElementId id )` |
| Method | IsValidNamingCategory | 2012 | `public static bool IsValidNamingCategory ( Document document , ElementId namingCategoryId , ICollection < ElementId > assemblyMemberIds )` |
| Method | PlaceInstance | 2012 | `public static AssemblyInstance PlaceInstance ( Document document , ElementId assemblyTypeId , XYZ location )` |
| Method | RemoveMemberIds | 2012 | `public void RemoveMemberIds ( ICollection < ElementId > memberIds )` |
| Method | SetMemberIds | 2012 | `public void SetMemberIds ( ICollection < ElementId > memberIds )` |
| Method | SetTransform | 2013 | `public void SetTransform ( Transform trf )` |
| Property | AssemblyTypeName | 2012 | `public string AssemblyTypeName { get ; set ; }` |
| Property | Location | 2013 | `public override Location Location { get ; }` |
| Property | NamingCategoryId | 2012 | `public ElementId NamingCategoryId { get ; set ; }` |
| Property | Parameter | — | `` |