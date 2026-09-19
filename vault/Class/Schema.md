---
type: Schema
namespace: Autodesk.Revit.DB.ExtensibleStorage
version: 2024
members: 15
tags: [revit-api, class]
---

# Schema

`Autodesk.Revit.DB.ExtensibleStorage.Schema` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetField | 2012 | `public Field GetField ( string name )` |
| Method | ListFields | 2012 | `public IList < Field > ListFields ()` |
| Method | ListSchemas | 2012 | `public static IList < Schema > ListSchemas ()` |
| Method | Lookup | 2012 | `public static Schema Lookup ( Guid guid )` |
| Method | ReadAccessGranted | 2012 | `public bool ReadAccessGranted ()` |
| Method | WriteAccessGranted | 2012 | `public bool WriteAccessGranted ()` |
| Property | ApplicationGUID | 2012 | `public Guid ApplicationGUID { get ; }` |
| Property | Documentation | 2012 | `public string Documentation { get ; }` |
| Property | GUID | 2012 | `public Guid GUID { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | ReadAccessLevel | 2012 | `public AccessLevel ReadAccessLevel { get ; }` |
| Property | SchemaName | 2012 | `public string SchemaName { get ; }` |
| Property | VendorId | 2012 | `public string VendorId { get ; }` |
| Property | WriteAccessLevel | 2012 | `public AccessLevel WriteAccessLevel { get ; }` |