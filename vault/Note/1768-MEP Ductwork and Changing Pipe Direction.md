---
num: 1768
date: 2019-08-15
themes: [MEP]
tags: [revit-api, tbc]
---

# MEP Ductwork and Changing Pipe Direction

<https://jeremytammik.github.io/tbc/a/1768_pipe_direction.html>

```csharp
Pipe dummyPipe = doc.GetElement( ElementTransformUtils.CopyElement( doc, branchPipe.Id, XYZ.Zero).First()) as Pipe; (dummyPipe.Location as LocationCurve).Curve = Line.CreateBound( intersectionPoint, intersectionPoint + perpendicularDirection );
```

```csharp
pipeDirection = X.CrossProduct(Y).CrossProduct(X)
```
