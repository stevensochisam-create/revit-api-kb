---
type: ParameterFilterUtilities
namespace: Autodesk.Revit.DB
version: 2024
members: 5
tags: [revit-api, class]
---

# ParameterFilterUtilities

`Autodesk.Revit.DB.ParameterFilterUtilities` · Revit 2024 · 5 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetAllFilterableCategories | 2011 | `public static ICollection < ElementId > GetAllFilterableCategories ()` |
| Method | GetFilterableParametersInCommon | 2011 | `public static ICollection < ElementId > GetFilterableParametersInCommon ( Document aDoc , ICollection < ElementId > categories )` |
| Method | GetInapplicableParameters | 2011 | `public static IList < ElementId > GetInapplicableParameters ( Document aDoc , ICollection < ElementId > categories , IList < ElementId > parameters )` |
| Method | IsParameterApplicable | 2011 | `public static bool IsParameterApplicable ( Element element , ElementId parameter )` |
| Method | RemoveUnfilterableCategories | 2011 | `public static ICollection < ElementId > RemoveUnfilterableCategories ( ICollection < ElementId > categories )` |