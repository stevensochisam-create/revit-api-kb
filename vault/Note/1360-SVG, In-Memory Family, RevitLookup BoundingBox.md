---
num: 1360
date: 2015-09-24
themes: [Geometry, Pitfall]
tags: [revit-api, tbc]
---

# SVG, In-Memory Family, RevitLookup BoundingBox

<https://jeremytammik.github.io/tbc/a/1360_revitlookup.html>

```csharp
&nbsp; BoundingBoxXYZ bb = elem.get_BoundingBox( null ); &nbsp; if( null != bb ) &nbsp; { &nbsp; &nbsp; data.Add( new Snoop.Data.Object( &quot;Bounding box&quot;, bb ) ); &nbsp; }
```
