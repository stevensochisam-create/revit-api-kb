---
type: SchemaBuilder
namespace: Autodesk.Revit.DB.ExtensibleStorage
version: 2024
members: 17
tags: [revit-api, class]
---

# SchemaBuilder

`Autodesk.Revit.DB.ExtensibleStorage.SchemaBuilder` · Revit 2024 · 17 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | SchemaBuilder | 2012 | `public SchemaBuilder ( Guid guid )` |
| Method | AcceptableName | 2012 | `public bool AcceptableName ( string name )` |
| Method | AddArrayField | 2012 | `public FieldBuilder AddArrayField ( string fieldName , Type fieldType )` |
| Method | AddMapField | 2012 | `public FieldBuilder AddMapField ( string fieldName , Type keyType , Type valueType )` |
| Method | AddSimpleField | 2012 | `public FieldBuilder AddSimpleField ( string fieldName , Type fieldType )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | Finish | 2012 | `public Schema Finish ()` |
| Method | GUIDIsValid | 2012 | `public static bool GUIDIsValid ( Guid guid )` |
| Method | Ready | 2012 | `public bool Ready ()` |
| Method | SetApplicationGUID | 2012 | `public SchemaBuilder SetApplicationGUID ( Guid applicationGUID )` |
| Method | SetDocumentation | 2012 | `public SchemaBuilder SetDocumentation ( string documentation )` |
| Method | SetReadAccessLevel | 2012 | `public SchemaBuilder SetReadAccessLevel ( AccessLevel readAccessLevel )` |
| Method | SetSchemaName | 2012 | `public SchemaBuilder SetSchemaName ( string schemaName )` |
| Method | SetVendorId | 2012 | `public SchemaBuilder SetVendorId ( string vendorId )` |
| Method | SetWriteAccessLevel | 2012 | `public SchemaBuilder SetWriteAccessLevel ( AccessLevel writeAccessLevel )` |
| Method | VendorIdIsValid | 2012 | `public static bool VendorIdIsValid ( string vendorId )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |