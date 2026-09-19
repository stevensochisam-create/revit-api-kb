---
type: ExportLayerTable
namespace: Autodesk.Revit.DB
version: 2024
members: 16
tags: [revit-api, class]
---

# ExportLayerTable

`Autodesk.Revit.DB.ExportLayerTable` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ExportLayerTable | 2014 | `public ExportLayerTable ()` |
| Method | Add | 2014 | `public void Add ( ExportLayerKey exportLayerKey , ExportLayerInfo exportLayerInfo )` |
| Method | Clear | 2014 | `public void Clear ()` |
| Method | ContainsKey | 2014 | `public bool ContainsKey ( ExportLayerKey exportlayerKey )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAvaliableLayerModifierTypes | 2014 | `public static IList < ModifierType > GetAvaliableLayerModifierTypes ( Document document , ExportLayerKey exportLayerKey )` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetEnumerator | — | `public virtual IEnumerator < KeyValuePair < ExportLayerKey , ExportLayerInfo >> GetEnumerator ()` |
| Method | GetExportLayerInfo | 2014 | `public ExportLayerInfo GetExportLayerInfo ( ExportLayerKey exportLayerKey )` |
| Method | GetKeys | 2014 | `public IList < ExportLayerKey > GetKeys ()` |
| Method | GetLayerTableIterator | — | `public ExportLayerTableIterator GetLayerTableIterator ()` |
| Method | GetValues | 2014 | `public IList < ExportLayerInfo > GetValues ()` |
| Method | Remove | 2014 | `public void Remove ( ExportLayerKey exportLayerKey )` |
| Property | Count | 2014 | `public int Count { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Item | 2014 | `public ExportLayerInfo this [ ExportLayerKey layerKey ] { get ; set ; }` |