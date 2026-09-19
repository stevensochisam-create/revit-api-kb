---
type: InternalDefinition
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# InternalDefinition

`Autodesk.Revit.DB.InternalDefinition` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetGroupTypeId | — | `public override ForgeTypeId GetGroupTypeId ()` |
| Method | GetParameterTypeId | — | `public ForgeTypeId GetParameterTypeId ()` |
| Method | GetTypeId | — | `public ForgeTypeId GetTypeId ()` |
| Method | SetAllowVaryBetweenGroups | 2014 | `public ICollection < ElementId > SetAllowVaryBetweenGroups ( Document document , bool allowVaryBetweenGroups )` |
| Method | SetGroupTypeId | — | `public void SetGroupTypeId ( ForgeTypeId groupTypeId )` |
| Property | BuiltInParameter | — | `public BuiltInParameter BuiltInParameter { get ; }` |
| Property | Id | 2017 | `public ElementId Id { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Name | — | `public override string Name { get ; }` |
| Property | ParameterGroup | — | `[ ObsoleteAttribute ("This property is deprecated in Revit 2024 and may be removed in a future version of Revit. Please use the `GetGroupTypeId()` method instead.")] public override BuiltInParameterGroup ParameterGroup {` |
| Property | VariesAcrossGroups | 2014 | `public bool VariesAcrossGroups { get ; }` |
| Property | Visible | — | `public virtual bool Visible { get ; }` |