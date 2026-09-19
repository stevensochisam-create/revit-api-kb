---
type: ViewSection
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# ViewSection

`Autodesk.Revit.DB.ViewSection` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateCallout | 2013 | `public static View CreateCallout ( Document document , ElementId parentViewId , ElementId viewFamilyTypeId , XYZ point1 , XYZ point2 )` |
| Method | CreateDetail | 2013 | `public static ViewSection CreateDetail ( Document document , ElementId viewFamilyTypeId , BoundingBoxXYZ sectionBox )` |
| Method | CreateReferenceCallout | 2013 | `public static void CreateReferenceCallout ( Document document , ElementId parentViewId , ElementId viewIdToReference , XYZ point1 , XYZ point2 )` |
| Method | CreateReferenceSection | 2013 | `public static void CreateReferenceSection ( Document document , ElementId parentViewId , ElementId viewIdToReference , XYZ headPoint , XYZ tailPoint )` |
| Method | CreateSection | 2013 | `public static ViewSection CreateSection ( Document document , ElementId viewFamilyTypeId , BoundingBoxXYZ sectionBox )` |
| Method | IsParentViewValidForCallout | — | `public static bool IsParentViewValidForCallout ( Document document , ElementId parentViewId )` |
| Method | IsSplitSection | 2021 | `public bool IsSplitSection ()` |
| Method | IsViewFamilyTypeValidForCallout | — | `public static bool IsViewFamilyTypeValidForCallout ( Document document , ElementId viewFamilyTypeId , ElementId parentViewId )` |
| Method | Print | — | `` |
| Property | Parameter | — | `` |