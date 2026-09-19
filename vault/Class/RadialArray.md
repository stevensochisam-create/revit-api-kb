---
type: RadialArray
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# RadialArray

`Autodesk.Revit.DB.RadialArray` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ArrayElementWithoutAssociation | — | `public static ICollection < ElementId > ArrayElementWithoutAssociation ( Document aDoc , View dBView , ElementId id , int count , Line axis , double angle , ArrayAnchorMember anchorMember )` |
| Method | ArrayElementsWithoutAssociation | — | `public static ICollection < ElementId > ArrayElementsWithoutAssociation ( Document aDoc , View dBView , ICollection < ElementId > ids , int count , Line axis , double angle , ArrayAnchorMember anchorMember )` |
| Method | Create | — | `` |
| Method | GetCopiedMemberIds | 2013 | `public override ICollection < ElementId > GetCopiedMemberIds ()` |
| Method | GetOriginalMemberIds | 2013 | `public override ICollection < ElementId > GetOriginalMemberIds ()` |
| Method | IsRotationAngleValid | — | `public static bool IsRotationAngleValid ( double angle )` |
| Method | IsValidArraySize | — | `public static bool IsValidArraySize ( int count )` |
| Property | NumMembers | — | `public override int NumMembers { get ; set ; }` |
| Property | Parameter | — | `` |