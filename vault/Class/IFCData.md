---
type: IFCData
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 33
tags: [revit-api, class]
---

# IFCData

`Autodesk.Revit.DB.IFC.IFCData` · Revit 2024 · 33 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | IFCData | 2013 | `public IFCData ( IFCData from )` |
| Method | AsAggregate | 2013 | `public IFCAggregate AsAggregate ()` |
| Method | AsBoolean | 2013 | `public bool AsBoolean ()` |
| Method | AsDouble | 2013 | `public double AsDouble ()` |
| Method | AsInstance | 2013 | `public IFCAnyHandle AsInstance ()` |
| Method | AsInteger | 2013 | `public int AsInteger ()` |
| Method | AsLogical | 2013 | `public IFCLogical AsLogical ()` |
| Method | AsString | 2013 | `public string AsString ()` |
| Method | CreateBinary | 2013 | `public static IFCData CreateBinary ( string value )` |
| Method | CreateBoolean | 2013 | `public static IFCData CreateBoolean ( bool value )` |
| Method | CreateBooleanOfType | 2013 | `public static IFCData CreateBooleanOfType ( bool value , string typeName )` |
| Method | CreateDouble | 2013 | `public static IFCData CreateDouble ( double value )` |
| Method | CreateDoubleOfType | 2013 | `public static IFCData CreateDoubleOfType ( double value , string typeName )` |
| Method | CreateEnumeration | 2013 | `public static IFCData CreateEnumeration ( string value )` |
| Method | CreateIFCAggregate | 2013 | `public static IFCData CreateIFCAggregate ( IFCAggregate value )` |
| Method | CreateIFCAnyHandle | 2013 | `public static IFCData CreateIFCAnyHandle ( IFCAnyHandle value )` |
| Method | CreateInteger | 2013 | `public static IFCData CreateInteger ( int value )` |
| Method | CreateIntegerOfType | 2013 | `public static IFCData CreateIntegerOfType ( int value , string typeName )` |
| Method | CreateLogical | 2013 | `public static IFCData CreateLogical ( IFCLogical value )` |
| Method | CreateLogicalOfType | 2014 | `public static IFCData CreateLogicalOfType ( IFCLogical value , string typeName )` |
| Method | CreateString | 2013 | `public static IFCData CreateString ( string value )` |
| Method | CreateStringOfType | 2013 | `public static IFCData CreateStringOfType ( string value , string typeName )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | Equals | — | `public override bool Equals ( Object obj )` |
| Method | GetHashCode | — | `public override int GetHashCode ()` |
| Method | GetSimpleType | 2013 | `public string GetSimpleType ()` |
| Method | GetTypeList | 2013 | `public IList < string > GetTypeList ()` |
| Method | HasSimpleType | 2015 | `public bool HasSimpleType ()` |
| Method | SetSimpleType | 2013 | `public void SetSimpleType ( string typeName )` |
| Method | SetTypeList | — | `public void SetTypeList ( IList < string > typeList )` |
| Property | HasValue | 2013 | `public bool HasValue { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | PrimitiveType | 2013 | `public IFCDataPrimitiveType PrimitiveType { get ; set ; }` |