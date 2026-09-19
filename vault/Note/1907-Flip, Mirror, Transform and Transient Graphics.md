---
num: 1907
date: 2021-05-26
themes: [Geometry]
tags: [revit-api, tbc]
---

# Flip, Mirror, Transform and Transient Graphics

<https://jeremytammik.github.io/tbc/a/1907_reflect_transform.html>

```csharp
import sys import clr clr.AddReference('ProtoGeometry') from Autodesk.DesignScript.Geometry import * data= UnwrapElement(IN[0]) output=[] for i in data: output.append(i.Location.Point) output.append(i.GetTransform().BasisX) output.append(i.GetTransform().BasisY) output.append(i.GetTransform().BasisZ) output.append("") OUT = output
```
