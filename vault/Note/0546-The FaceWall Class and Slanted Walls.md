---
num: 546
date: 2011-03-02
themes: [Geometry]
tags: [revit-api, tbc]
---

# The FaceWall Class and Slanted Walls

<https://jeremytammik.github.io/tbc/a/0546_slanted_wall.htm>

```csharp
&nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( FaceWall ) ) &nbsp; &nbsp; &nbsp; .OfCategory( BuiltInCategory.OST_Walls );
```
