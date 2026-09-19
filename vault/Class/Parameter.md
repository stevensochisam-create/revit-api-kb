---
type: Parameter
namespace: Autodesk.Revit.DB
version: 2024
members: 25
tags: [revit-api, class]
---

# Parameter

`Autodesk.Revit.DB.Parameter` · Revit 2024 · 25 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AsDouble | — | `public double AsDouble ()` |
| Method | AsElementId | — | `public ElementId AsElementId ()` |
| Method | AsInteger | — | `public int AsInteger ()` |
| Method | AsString | — | `public string AsString ()` |
| Method | AsValueString | — | `` |
| Method | AsValueString | — | `public string AsValueString ()` |
| Method | AssociateWithGlobalParameter | 2016 Subscription Update | `public void AssociateWithGlobalParameter ( ElementId gpId )` |
| Method | CanBeAssociatedWithGlobalParameter | 2016 Subscription Update | `public bool CanBeAssociatedWithGlobalParameter ( ElementId gpId )` |
| Method | CanBeAssociatedWithGlobalParameters | 2016 Subscription Update | `public bool CanBeAssociatedWithGlobalParameters ()` |
| Method | ClearValue | 2020 | `public bool ClearValue ()` |
| Method | DissociateFromGlobalParameter | 2016 Subscription Update | `public void DissociateFromGlobalParameter ()` |
| Method | GetAssociatedGlobalParameter | 2016 Subscription Update | `public ElementId GetAssociatedGlobalParameter ()` |
| Method | GetTypeId | 2022 | `public ForgeTypeId GetTypeId ()` |
| Method | GetUnitTypeId | — | `public ForgeTypeId GetUnitTypeId ()` |
| Method | Set | — | `` |
| Method | SetValueString | — | `public bool SetValueString ( string valueString )` |
| Property | Definition | — | `public Definition Definition { get ; }` |
| Property | Element | — | `public Element Element { get ; }` |
| Property | GUID | 2011 | `public Guid GUID { get ; }` |
| Property | HasValue | 2012 | `public bool HasValue { get ; }` |
| Property | Id | 2011 | `public ElementId Id { get ; }` |
| Property | IsReadOnly | — | `public override bool IsReadOnly { get ; }` |
| Property | IsShared | 2011 | `public bool IsShared { get ; }` |
| Property | StorageType | — | `public StorageType StorageType { get ; }` |
| Property | UserModifiable | 2015 | `public bool UserModifiable { get ; }` |