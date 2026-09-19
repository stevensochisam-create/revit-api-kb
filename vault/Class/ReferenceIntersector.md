---
type: ReferenceIntersector
namespace: Autodesk.Revit.DB
version: 2024
members: 12
tags: [revit-api, class]
---

# ReferenceIntersector

`Autodesk.Revit.DB.ReferenceIntersector` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ReferenceIntersector | — | `` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | Find | 2013 | `public IList < ReferenceWithContext > Find ( XYZ origin , XYZ direction )` |
| Method | FindNearest | 2013 | `public ReferenceWithContext FindNearest ( XYZ origin , XYZ direction )` |
| Method | GetFilter | 2013 | `public ElementFilter GetFilter ()` |
| Method | GetTargetElementIds | 2013 | `public ICollection < ElementId > GetTargetElementIds ()` |
| Method | SetFilter | 2013 | `public void SetFilter ( ElementFilter filter )` |
| Method | SetTargetElementIds | 2013 | `public void SetTargetElementIds ( ICollection < ElementId > elementIds )` |
| Property | FindReferencesInRevitLinks | 2014 | `public bool FindReferencesInRevitLinks { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | TargetType | 2013 | `public FindReferenceTarget TargetType { get ; set ; }` |
| Property | ViewId | 2013 | `public ElementId ViewId { get ; set ; }` |