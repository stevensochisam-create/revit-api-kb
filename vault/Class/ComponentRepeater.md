---
type: ComponentRepeater
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# ComponentRepeater

`Autodesk.Revit.DB.ComponentRepeater` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanElementBeRepeated | 2015 Subscription Update | `public static bool CanElementBeRepeated ( Document ADoc , ElementId elementId )` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetEnumerator | — | `public virtual IEnumerator < ComponentRepeaterSlot > GetEnumerator ()` |
| Method | IsTypeValidForRepeater | 2014 | `public bool IsTypeValidForRepeater ( ElementId typeId )` |
| Method | RemoveRepeaters | 2015 Subscription Update | `public static ISet < ElementId > RemoveRepeaters ( Document document , ISet < ElementId > elementIds )` |
| Method | RepeatElements | 2014 | `public static IList < ComponentRepeater > RepeatElements ( Document document , ICollection < ElementId > elementIds )` |
| Property | DefaultFamilyType | 2014 | `public ElementId DefaultFamilyType { get ; set ; }` |
| Property | DimensionCount | 2014 | `public int DimensionCount { get ; }` |
| Property | Parameter | — | `` |