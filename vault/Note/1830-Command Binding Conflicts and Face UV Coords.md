---
num: 1830
date: 2020-03-20
themes: [Geometry]
tags: [revit-api, tbc]
---

# Command Binding Conflicts and Face UV Coords

<https://jeremytammik.github.io/tbc/a/1830_face_bounding_box_uv.html>

```csharp
&nbsp;&nbsp;BoundingBoxUV&nbsp;bb&nbsp;=&nbsp;face.GetBoundingBox(); &nbsp;&nbsp;UV&nbsp;pmid&nbsp;=&nbsp;0.5&nbsp;*&nbsp;(bb.Min&nbsp;+&nbsp;bb.Max);
```
