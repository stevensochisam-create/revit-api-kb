---
num: 1366
date: 2015-10-21
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Filtering Samples and RAC 2016 Features

<https://jeremytammik.github.io/tbc/a/1366_filter_rac_2016.html>

```csharp
&nbsp; // Floors, Walls, Ceilings, Roofs etc... &nbsp; FilteredElementCollector FMFloorCollector &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; FMFloorCollector.OfClass( typeof( Floor ) ); &nbsp; &nbsp; foreach( Floor FMFloor in FMFloorCollector ) &nbsp; { &nbsp; &nbsp; // Type &nbsp; &nbsp; Element el = FMFloor as Element; &nbsp; &nbsp; ElementId typeid = el.GetTypeId(); &nbsp; &nbsp; Element floortype = doc.GetElement( typeid ); &nbsp; &nbsp; &nbsp; Parameter pKeynote = floortype.get_Parameter( &nbsp; &nbsp; &nbsp; BuiltInParameter.KEYNOTE_PARAM ); &nbsp; &nbsp; &nbsp; // Instance &nbsp; &nbsp; Parameter pArea = FMFloor.get_Parameter( &nbsp; &nbsp; &nbsp; BuiltInParameter.HOST_AREA_COMPUTED ); &nbsp; }
```
