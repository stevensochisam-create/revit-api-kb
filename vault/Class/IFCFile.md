---
type: IFCFile
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 11
tags: [revit-api, class]
---

# IFCFile

`Autodesk.Revit.DB.IFC.IFCFile` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Close | 2013 | `public void Close ()` |
| Method | Create | 2013 | `public static IFCFile Create ( IFCFileModelOptions modelOptions )` |
| Method | CreateHeaderInstance | 2013 | `public IFCAnyHandle CreateHeaderInstance ( string name )` |
| Method | CreateInstance | 2013 | `public IFCAnyHandle CreateInstance ( string name )` |
| Method | CreateStyle | — | `` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetInstanceCount | 2014 | `public int GetInstanceCount ( string entityName , bool includeSubTypes )` |
| Method | GetInstances | 2014 | `public IList < IFCAnyHandle > GetInstances ( string entityName , bool includeSubTypes )` |
| Method | Read | — | `` |
| Method | Write | 2013 | `public void Write ( IFCFileWriteOptions writeOptions )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |