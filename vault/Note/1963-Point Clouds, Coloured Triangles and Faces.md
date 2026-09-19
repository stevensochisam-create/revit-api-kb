---
num: 1963
date: 2022-09-02
themes: [Geometry]
tags: [revit-api, tbc]
---

# Point Clouds, Coloured Triangles and Faces

<https://jeremytammik.github.io/tbc/a/1963_point_cloud.html>

```csharp
if any([ display_style == DB.DisplayStyle.Shading, display_style == DB.DisplayStyle.ShadingWithEdges ]): tri_effect_instance = dc.EffectInstance( dc.VertexFormatBits.PositionNormalColored ) else: tri_effect_instance = dc.EffectInstance( dc.VertexFormatBits.PositionColored )
```
