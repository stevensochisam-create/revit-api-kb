---
type: ImporterIFC
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 9
tags: [revit-api, class]
---

# ImporterIFC

`Autodesk.Revit.DB.IFC.ImporterIFC` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetOptions | 2015 | `public IDictionary < string , string > GetOptions ()` |
| Method | HybridCreateImportMap | — | `public IDictionary < string , ElementId > HybridCreateImportMap ( Document doc , IList < ElementId > elementIds )` |
| Method | HybridElementImport | 2024 | `public IList < ElementId > HybridElementImport ( Document doc , string file )` |
| Method | ProcessIFCProject | — | `` |
| Method | SetFile | 2014 | `public void SetFile ( IFCFile file )` |
| Property | Document | 2015 | `public Document Document { get ; }` |
| Property | FullFileName | 2014 | `public string FullFileName { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |