---
type: AssetProperty
namespace: Autodesk.Revit.DB.Visual
version: 2024
members: 15
tags: [revit-api, class]
---

# AssetProperty

`Autodesk.Revit.DB.Visual.AssetProperty` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddConnectedAsset | 2018.1 | `public void AddConnectedAsset ( string schema )` |
| Method | AddCopyAsConnectedAsset | 2018.1 | `public void AddCopyAsConnectedAsset ( Asset pRenderingAsset )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAllConnectedProperties | 2014 | `public IList < AssetProperty > GetAllConnectedProperties ()` |
| Method | GetConnectedProperty | 2014 | `public AssetProperty GetConnectedProperty ( int index )` |
| Method | GetSingleConnectedAsset | 2018.1 | `public Asset GetSingleConnectedAsset ()` |
| Method | GetTypeName | — | `public static string GetTypeName ( AssetPropertyType type )` |
| Method | IsEditable | 2018.1 | `public bool IsEditable ()` |
| Method | IsValidSchemaIdentifier | 2018.1 | `public bool IsValidSchemaIdentifier ( string schemaID )` |
| Method | RemoveConnectedAsset | 2018.1 | `public void RemoveConnectedAsset ()` |
| Property | IsReadOnly | — | `public bool IsReadOnly { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Name | — | `public string Name { get ; }` |
| Property | NumberOfConnectedProperties | 2014 | `public int NumberOfConnectedProperties { get ; }` |
| Property | Type | — | `public AssetPropertyType Type { get ; }` |