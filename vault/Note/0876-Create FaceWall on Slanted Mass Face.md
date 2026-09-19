---
num: 876
date: 2013-01-03
themes: [Geometry]
tags: [revit-api, tbc]
---

# Create FaceWall on Slanted Mass Face

<https://jeremytammik.github.io/tbc/a/0876_facewall_create.htm>

```csharp
Reference r1 = doc.Selection.PickObject( ObjectType.Element, "Please pick a wall: " ); Element e1 = doc.GetElement( r1 ); FaceWall faceWall = e1 as FaceWall; LocationCurve theCurve = faceWall.Location as LocationCurve; LocationPoint thePoint = faceWall.Location as LocationPoint;
```
