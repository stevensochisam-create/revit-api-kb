---
num: 298
date: 2010-02-05
themes: [Geometry]
tags: [revit-api, tbc]
---

# Retrieving Column and Stair Geometry

<https://jeremytammik.github.io/tbc/a/0298_column_stair_geometry.htm>

```csharp
void generateSingleElement( RvtElement e ) { &nbsp; GeoElement geo = e.get_Geometry( geomOption ); &nbsp; &nbsp; if( geo != null ) &nbsp; { &nbsp; &nbsp; GeometryObjectArray arr = geo.Objects; &nbsp; &nbsp; &nbsp; foreach( GeometryObject obj in arr ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Solid geomSolid = obj as Solid; &nbsp; &nbsp; &nbsp; &nbsp; if( null != geomSolid ) //+ &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; // get geometry from this solid &nbsp; &nbsp; &nbsp; &nbsp; // ... &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; else if( obj is GeoInstance ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; GeoInstance geoInst = obj as GeoInstance; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; GeoElement geoElem = geoInst.SymbolGeometry; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Transform transform = geoInst.Transform; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; GeometryObjectArray arr2 = geoElem.Objects; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // use the same method as above to obtain &nbsp; &nbsp; &nbsp; &nbsp; // the nested geometry. please don't &nbsp; &nbsp; &nbsp; &nbsp; // forget to convert with the transform. &nbsp; &nbsp; &nbsp; &nbsp; // ... &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } }
```
