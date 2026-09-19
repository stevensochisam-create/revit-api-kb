---
type: FilteredWorksetCollector
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# FilteredWorksetCollector

`Autodesk.Revit.DB.FilteredWorksetCollector` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | FilteredWorksetCollector | 2012 | `public FilteredWorksetCollector ( Document document )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | FirstWorkset | 2012 | `public Workset FirstWorkset ()` |
| Method | FirstWorksetId | 2012 | `public WorksetId FirstWorksetId ()` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetEnumerator | — | `public virtual IEnumerator < Workset > GetEnumerator ()` |
| Method | GetWorksetIdIterator | 2012 | `public FilteredWorksetIdIterator GetWorksetIdIterator ()` |
| Method | GetWorksetIterator | 2012 | `public FilteredWorksetIterator GetWorksetIterator ()` |
| Method | OfKind | 2012 | `public FilteredWorksetCollector OfKind ( WorksetKind worksetKind )` |
| Method | ToWorksetIds | 2012 | `public ICollection < WorksetId > ToWorksetIds ()` |
| Method | ToWorksets | 2012 | `public IList < Workset > ToWorksets ()` |
| Method | WherePasses | 2012 | `public FilteredWorksetCollector WherePasses ( WorksetFilter filter )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |