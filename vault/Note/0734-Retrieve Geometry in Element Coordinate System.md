---
num: 734
date: 2012-03-16
themes: [Geometry]
tags: [revit-api, tbc]
---

# Retrieve Geometry in Element Coordinate System

<https://jeremytammik.github.io/tbc/a/0734_retrieve_ecs_geom.htm>

```csharp
coordSys = m_revElem ->endConnectors[0] ->CoordinateSystem; org = coordSys->Origin; dir = coordSys->BasisZ->Negate(); norm = coordSys->BasisY->Negate();
```

```csharp
Transform ^tf = Transform::Identity; tf->BasisX = coordSys->BasisZ->Negate(); tf->BasisY = coordSys->BasisX; tf->BasisZ = coordSys->BasisY->Negate(); tf->Origin = coordSys->Origin; tf = tf->Inverse;
```
