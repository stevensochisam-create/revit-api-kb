---
type: Group
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# Group

`Autodesk.Revit.DB.Group` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetAvailableAttachedDetailGroupTypeIds | 2019.1 | `public ISet < ElementId > GetAvailableAttachedDetailGroupTypeIds ()` |
| Method | GetMemberIds | 2013 | `public IList < ElementId > GetMemberIds ()` |
| Method | GetShownAttachedDetailGroupTypeIds | 2019.1 | `public ISet < ElementId > GetShownAttachedDetailGroupTypeIds ( View view )` |
| Method | HideAllAttachedDetailGroups | 2019.1 | `public void HideAllAttachedDetailGroups ( View view )` |
| Method | HideAttachedDetailGroups | 2019.1 | `public void HideAttachedDetailGroups ( View view , ElementId detailGroupTypeId )` |
| Method | IsCompatibleAttachedDetailGroupType | 2019.1 | `public bool IsCompatibleAttachedDetailGroupType ( View view , ElementId detailGroupTypeId )` |
| Method | ShowAllAttachedDetailGroups | 2019.1 | `public void ShowAllAttachedDetailGroups ( View view )` |
| Method | ShowAttachedDetailGroups | 2019.1 | `public void ShowAttachedDetailGroups ( View view , ElementId detailGroupTypeId )` |
| Method | UngroupMembers | — | `public ICollection < ElementId > UngroupMembers ()` |
| Property | AttachedParentId | 2019.1 | `public ElementId AttachedParentId { get ; }` |
| Property | GroupType | — | `public virtual GroupType GroupType { get ; set ; }` |
| Property | IsAttached | 2019.1 | `public bool IsAttached { get ; }` |
| Property | Location | — | `public override Location Location { get ; }` |
| Property | Parameter | — | `` |