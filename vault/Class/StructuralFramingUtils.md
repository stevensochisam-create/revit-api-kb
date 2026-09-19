---
type: StructuralFramingUtils
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 10
tags: [revit-api, class]
---

# StructuralFramingUtils

`Autodesk.Revit.DB.Structure.StructuralFramingUtils` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AllowJoinAtEnd | 2015 | `public static void AllowJoinAtEnd ( FamilyInstance familyInstance , int end )` |
| Method | CanFlipEnds | 2015 Subscription Update | `public static bool CanFlipEnds ( FamilyInstance familyInstance )` |
| Method | CanSetEndReference | 2015 | `public static bool CanSetEndReference ( FamilyInstance familyInstance , int end )` |
| Method | DisallowJoinAtEnd | 2015 | `public static void DisallowJoinAtEnd ( FamilyInstance familyInstance , int end )` |
| Method | FlipEnds | 2015 Subscription Update | `public static void FlipEnds ( FamilyInstance familyInstance )` |
| Method | GetEndReference | 2015 | `public static Reference GetEndReference ( FamilyInstance familyInstance , int end )` |
| Method | IsEndReferenceValid | 2015 | `public static bool IsEndReferenceValid ( FamilyInstance familyInstance , int end , Reference pick )` |
| Method | IsJoinAllowedAtEnd | 2015 | `public static bool IsJoinAllowedAtEnd ( FamilyInstance familyInstance , int end )` |
| Method | RemoveEndReference | 2015 | `public static void RemoveEndReference ( FamilyInstance familyInstance , int end )` |
| Method | SetEndReference | 2015 | `public static void SetEndReference ( FamilyInstance familyInstance , int end , Reference pick )` |