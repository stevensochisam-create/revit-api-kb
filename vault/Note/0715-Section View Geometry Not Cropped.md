---
num: 715
date: 2012-02-02
themes: [Geometry]
tags: [revit-api, tbc]
---

# Section View Geometry Not Cropped

<https://jeremytammik.github.io/tbc/a/0715_section_view_geom_crop.htm>

```csharp
&nbsp; // Create the 'Details 0' view &nbsp; &nbsp; BoundingBoxXYZ boundingBox &nbsp; &nbsp; = GetFrontBoundingBox( slab, doc ); &nbsp; &nbsp; ViewSection viewSection &nbsp; &nbsp; = doc.Create.NewViewSection( boundingBox ); &nbsp; &nbsp; // Retrieve the element geometry within the view; &nbsp; // this returns the whole slab (floor) &nbsp; &nbsp; Options options = application.Create &nbsp; &nbsp; .NewGeometryOptions(); &nbsp; &nbsp; options.View = viewSection; &nbsp; &nbsp; GeometryElement geo1 = slab.get_Geometry( &nbsp; &nbsp; options ); &nbsp; &nbsp; DumpLines( geo1 ); &nbsp; &nbsp; // Retrieve the geometry of the whole slab; &nbsp; // this returns the same result &nbsp; &nbsp; GeometryElement geo2 = slab.get_Geometry( &nbsp; &nbsp; new Options() ); &nbsp; &nbsp; DumpLines( geo2 );
```

```csharp
&nbsp; BoundingBoxXYZ boundingBox &nbsp; &nbsp; = GetFrontBoundingBox( slab, doc ); &nbsp; &nbsp; ViewSection viewSection &nbsp; &nbsp; = doc.Create.NewViewSection( boundingBox ); &nbsp; &nbsp; //viewSection.CropBox = boundingBox; &nbsp; &nbsp; Options options &nbsp; &nbsp; = doc.Application.Create.NewGeometryOptions(); &nbsp; &nbsp; options.View = viewSection; &nbsp; &nbsp; doc.Regenerate(); &nbsp; &nbsp; GeometryElement geo1 = slab.get_Geometry( &nbsp; &nbsp; options ); &nbsp; &nbsp; DumpLines( geo1 ); &nbsp; &nbsp; GeometryElement geo2 = slab.get_Geometry( &nbsp; &nbsp; new Options() ); &nbsp; &nbsp; DumpLines( geo2 );
```
