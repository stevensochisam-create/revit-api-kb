---
type: LinkLoadResult
namespace: Autodesk.Revit.DB
version: 2024
members: 16
tags: [revit-api, class]
---

# LinkLoadResult

`Autodesk.Revit.DB.LinkLoadResult` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | LinkLoadResult | — | `` |
| Constructor | LinkLoadResult | 2013 | `public LinkLoadResult ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetCentralModelName | 2013 | `public ModelPath GetCentralModelName ()` |
| Method | GetExternalResourceReference | 2015 | `public ExternalResourceReference GetExternalResourceReference ()` |
| Method | GetExternalResourceReferencesFromFailedLoads | 2015 | `public IList < ExternalResourceReference > GetExternalResourceReferencesFromFailedLoads ()` |
| Method | GetLinkLoadResult | 2015 | `public LinkLoadResult GetLinkLoadResult ( ExternalResourceReference matchExtResRef )` |
| Method | GetModelName | 2013 | `public ModelPath GetModelName ()` |
| Method | GetNestedLinkLoadResults | 2013 | `public IDictionary < string , LinkLoadResult > GetNestedLinkLoadResults ()` |
| Method | GetParentModelName | 2013 | `public ModelPath GetParentModelName ()` |
| Method | IsCodeSuccess | 2013 | `public static bool IsCodeSuccess ( LinkLoadResultType code )` |
| Property | ElementId | 2013 | `public ElementId ElementId { get ; }` |
| Property | IsCircularLink | 2013 | `public bool IsCircularLink { get ; }` |
| Property | IsNested | 2013 | `public bool IsNested { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | LoadResult | 2013 | `public LinkLoadResultType LoadResult { get ; }` |