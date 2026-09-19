---
type: ExportPatternTable
namespace: Autodesk.Revit.DB
version: 2024
members: 15
tags: [revit-api, class]
---

# ExportPatternTable

`Autodesk.Revit.DB.ExportPatternTable` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ExportPatternTable | 2014 | `public ExportPatternTable ()` |
| Method | Add | 2014 | `public void Add ( ExportPatternKey exportPatternKey , ExportPatternInfo exportPatternInfo )` |
| Method | Clear | 2014 | `public void Clear ()` |
| Method | ContainsKey | 2014 | `public bool ContainsKey ( ExportPatternKey exportpatternKey )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetEnumerator | — | `public virtual IEnumerator < KeyValuePair < ExportPatternKey , ExportPatternInfo >> GetEnumerator ()` |
| Method | GetExportPatternInfo | 2014 | `public ExportPatternInfo GetExportPatternInfo ( ExportPatternKey exportPatternKey )` |
| Method | GetKeys | 2014 | `public IList < ExportPatternKey > GetKeys ()` |
| Method | GetPatternTableIterator | — | `public ExportPatternTableIterator GetPatternTableIterator ()` |
| Method | GetValues | 2014 | `public IList < ExportPatternInfo > GetValues ()` |
| Method | Remove | 2014 | `public void Remove ( ExportPatternKey exportPatternKey )` |
| Property | Count | 2014 | `public int Count { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Item | 2014 | `public ExportPatternInfo this [ ExportPatternKey patternKey ] { get ; set ; }` |