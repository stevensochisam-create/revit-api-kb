---
num: 875
date: 2012-12-21
themes: [Geometry]
tags: [revit-api, tbc]
---

# GetInstanceGeometry Overhead and Invalid References

<https://jeremytammik.github.io/tbc/a/0875_inst_geom_overhead.htm>

```csharp
int idx = sfm.AddSpatialFieldPrimitive( face, Transform.Identity );
```

```csharp
int idx = sfm.AddSpatialFieldPrimitive( face.Reference );
```

```csharp
AddSpatialFieldPrimitive( Reference, SpatialFieldPrimitiveHideMode )
```
