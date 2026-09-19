---
type: JoinGeometryUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 6
tags: [revit-api, class]
---

# JoinGeometryUtils

`Autodesk.Revit.DB.JoinGeometryUtils` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreElementsJoined | 2014 | `public static bool AreElementsJoined ( Document document , Element firstElement , Element secondElement )` |
| Method | GetJoinedElements | 2014 | `public static ICollection < ElementId > GetJoinedElements ( Document document , Element element )` |
| Method | IsCuttingElementInJoin | 2014 | `public static bool IsCuttingElementInJoin ( Document document , Element firstElement , Element secondElement )` |
| Method | JoinGeometry | 2014 | `public static void JoinGeometry ( Document document , Element firstElement , Element secondElement )` |
| Method | SwitchJoinOrder | 2014 | `public static void SwitchJoinOrder ( Document document , Element firstElement , Element secondElement )` |
| Method | UnjoinGeometry | 2014 | `public static void UnjoinGeometry ( Document document , Element firstElement , Element secondElement )` |