---
type: DocumentChangedEventArgs
namespace: Autodesk.Revit.DB.Events
version: 2024
members: 8
tags: [revit-api, class]
---

# DocumentChangedEventArgs

`Autodesk.Revit.DB.Events.DocumentChangedEventArgs` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetAddedElementIds | — | `` |
| Method | GetAddedElementIds | 2011 | `public ICollection < ElementId > GetAddedElementIds ()` |
| Method | GetDeletedElementIds | 2011 | `public ICollection < ElementId > GetDeletedElementIds ()` |
| Method | GetDocument | 2011 | `public Document GetDocument ()` |
| Method | GetModifiedElementIds | — | `` |
| Method | GetModifiedElementIds | 2011 | `public ICollection < ElementId > GetModifiedElementIds ()` |
| Method | GetTransactionNames | 2011 | `public IList < string > GetTransactionNames ()` |
| Property | Operation | 2011 | `public UndoOperation Operation { get ; }` |