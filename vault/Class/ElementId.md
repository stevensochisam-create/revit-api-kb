---
type: ElementId
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# ElementId

`Autodesk.Revit.DB.ElementId` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ElementId | — | `` |
| Method | Compare | — | `public int Compare ( ElementId id )` |
| Method | Equals | — | `public override bool Equals ( Object obj )` |
| Method | GetHashCode | — | `public override int GetHashCode ()` |
| Method | Parse | 2023 | `public static ElementId Parse ( string idStr )` |
| Method | ToString | — | `public override string ToString ()` |
| Method | TryParse | 2023 | `public static bool TryParse ( string idStr , out ElementId id )` |
| Property | IntegerValue | — | `[ ObsoleteAttribute ("This property is deprecated in Revit 2024 and may be removed in a future version of Revit. Please use the Value property instead.")] public int IntegerValue { get ; }` |
| Property | InvalidElementId | — | `public static ElementId InvalidElementId { get ; }` |
| Property | Value | 2024 | `public long Value { get ; }` |