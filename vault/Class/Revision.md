---
type: Revision
namespace: Autodesk.Revit.DB
version: 2024
members: 15
tags: [revit-api, class]
---

# Revision

`Autodesk.Revit.DB.Revision` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CombineWithNext | 2015 | `public static ISet < ElementId > CombineWithNext ( Document document , ElementId revisionId )` |
| Method | CombineWithPrevious | 2015 | `public static ISet < ElementId > CombineWithPrevious ( Document document , ElementId revisionId )` |
| Method | Create | 2015 | `public static Revision Create ( Document document )` |
| Method | GetAllRevisionIds | 2015 | `public static IList < ElementId > GetAllRevisionIds ( Document document )` |
| Method | ReorderRevisionSequence | 2015 | `public static void ReorderRevisionSequence ( Document document , IList < ElementId > newSequence )` |
| Property | Description | 2015 | `public string Description { get ; set ; }` |
| Property | Issued | 2015 | `public bool Issued { get ; set ; }` |
| Property | IssuedBy | 2015 | `public string IssuedBy { get ; set ; }` |
| Property | IssuedTo | 2015 | `public string IssuedTo { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | RevisionDate | 2015 | `public string RevisionDate { get ; set ; }` |
| Property | RevisionNumber | 2015 | `public string RevisionNumber { get ; }` |
| Property | RevisionNumberingSequenceId | 2022 | `public ElementId RevisionNumberingSequenceId { get ; set ; }` |
| Property | SequenceNumber | 2015 | `public int SequenceNumber { get ; }` |
| Property | Visibility | 2015 | `public RevisionVisibility Visibility { get ; set ; }` |