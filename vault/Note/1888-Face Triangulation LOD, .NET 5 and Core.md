---
num: 1888
date: 2021-01-27
themes: [Geometry]
tags: [revit-api, tbc]
---

# Face Triangulation LOD, .NET 5 and Core

<https://jeremytammik.github.io/tbc/a/1888_net_5_core.html>

```csharp
public RenderNodeAction OnFaceBegin(FaceNode node) { Autodesk.Revit.DB.Face face = node.GetFace(); Autodesk.Revit.DB.Mesh m = face.Triangulate(0.1); int vertCount = m.Vertices.Count; return RenderNodeAction.Proceed; }
```
