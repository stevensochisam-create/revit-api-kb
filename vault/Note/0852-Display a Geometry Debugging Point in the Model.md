---
num: 852
date: 2012-10-31
themes: [Geometry]
tags: [revit-api, tbc]
---

# Display a Geometry Debugging Point in the Model

<https://jeremytammik.github.io/tbc/a/0852_create_marker.htm>

```csharp
transaction = Transaction(doc) transaction.Start('draw a line') c = XYZ(0, 0, 0) v0 = XYZ(a.X - b.X, a.Y - b.Y, a.Z - b.Z) v1 = XYZ(a.X - c.X, a.Y - c.Y, a.Z - c.Z) plane = Plane(v0.CrossProduct(v1), a) sketchPlane = doc.Create.NewSketchPlane(plane) line = doc.Application.Create.NewLineBound(a, b) doc.Create.NewModelCurve(line, sketchPlane) transaction.Commit()
```
