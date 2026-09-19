---
type: ExternalDefinition
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# ExternalDefinition

`Autodesk.Revit.DB.ExternalDefinition` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetGroupTypeId | — | `public override ForgeTypeId GetGroupTypeId ()` |
| Property | Description | 2015 | `public virtual string Description { get ; }` |
| Property | GUID | — | `public virtual Guid GUID { get ; }` |
| Property | HideWhenNoValue | 2020 | `public bool HideWhenNoValue { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Name | — | `public override string Name { get ; }` |
| Property | OwnerGroup | — | `public virtual DefinitionGroup OwnerGroup { get ; set ; }` |
| Property | ParameterGroup | — | `[ ObsoleteAttribute ("This property is deprecated in Revit 2024 and may be removed in a future version of Revit. Please use the `GetGroupTypeId()` method instead.")] public override BuiltInParameterGroup ParameterGroup {` |
| Property | UserModifiable | 2015 | `public bool UserModifiable { get ; }` |
| Property | Visible | — | `public virtual bool Visible { get ; }` |