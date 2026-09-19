---
type: ShapeImporter
namespace: Autodesk.Revit.DB
version: 2024
members: 8
tags: [revit-api, class]
---

# ShapeImporter

`Autodesk.Revit.DB.ShapeImporter` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ShapeImporter | 2017 | `public ShapeImporter ()` |
| Method | Convert | 2017 | `public IList < GeometryObject > Convert ( Document document , string filename )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | IsServiceAvailable | 2017 | `public static bool IsServiceAvailable ()` |
| Method | SetDefaultLengthUnit | 2017_subscription_update | `public ShapeImporter SetDefaultLengthUnit ( ImportUnit defaultLengthUnit )` |
| Property | DefaultLengthUnit | 2017 | `public ImportUnit DefaultLengthUnit { get ; }` |
| Property | InputFormat | 2017 | `public ShapeImporterSourceFormat InputFormat { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |