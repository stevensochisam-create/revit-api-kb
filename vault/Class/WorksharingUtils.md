---
type: WorksharingUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 10
tags: [revit-api, class]
---

# WorksharingUtils

`Autodesk.Revit.DB.WorksharingUtils` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CheckoutElements | — | `` |
| Method | CheckoutWorksets | — | `` |
| Method | CreateNewLocal | 2014 | `public static void CreateNewLocal ( ModelPath sourcePath , ModelPath targetPath )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCheckoutStatus | — | `` |
| Method | GetModelUpdatesStatus | 2012 | `public static ModelUpdatesStatus GetModelUpdatesStatus ( Document document , ElementId elementId )` |
| Method | GetUserWorksetInfo | 2012 | `public static IList < WorksetPreview > GetUserWorksetInfo ( ModelPath path )` |
| Method | GetWorksharingTooltipInfo | 2012 | `public static WorksharingTooltipInfo GetWorksharingTooltipInfo ( Document document , ElementId elementId )` |
| Method | RelinquishOwnership | 2014 | `public static RelinquishedItems RelinquishOwnership ( Document document , RelinquishOptions generalCategories , TransactWithCentralOptions options )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |