---
type: LinearArray
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# LinearArray

`Autodesk.Revit.DB.LinearArray` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ArrayElementWithoutAssociation | — | `public static ICollection < ElementId > ArrayElementWithoutAssociation ( Document aDoc , View dBView , ElementId id , int count , XYZ translationToAnchorMember , ArrayAnchorMember anchorMember )` |
| Method | ArrayElementsWithoutAssociation | — | `public static ICollection < ElementId > ArrayElementsWithoutAssociation ( Document aDoc , View dBView , ICollection < ElementId > ids , int count , XYZ translationToAnchorMember , ArrayAnchorMember anchorMember )` |
| Method | Create | — | `` |
| Method | GetCopiedMemberIds | 2013 | `public override ICollection < ElementId > GetCopiedMemberIds ()` |
| Method | GetOriginalMemberIds | 2013 | `public override ICollection < ElementId > GetOriginalMemberIds ()` |
| Method | IsElementArrayable | — | `public static bool IsElementArrayable ( Document aDoc , ElementId id )` |
| Method | IsValidArraySize | — | `public static bool IsValidArraySize ( int count )` |
| Property | NumMembers | — | `public override int NumMembers { get ; set ; }` |
| Property | Parameter | — | `` |