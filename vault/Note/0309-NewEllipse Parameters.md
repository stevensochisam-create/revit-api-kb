---
num: 309
date: 2010-03-01
themes: [Parameter]
tags: [revit-api, tbc]
---

# NewEllipse Parameters

<https://jeremytammik.github.io/tbc/a/0309_newellipse.htm>

```csharp
Ellipse CreateEllipse( Application app ) { &nbsp; XYZ center = XYZ.Zero; &nbsp; &nbsp; double radX = 30; &nbsp; double radY = 50; &nbsp; &nbsp; XYZ xVec = XYZ.BasisX; &nbsp; XYZ yVec = XYZ.BasisY; &nbsp; &nbsp; double param0 = 0.0; &nbsp; double param1 = 2 * Math.PI; &nbsp; &nbsp; Ellipse e = app.Create.NewEllipse( center, &nbsp; &nbsp; radX, radY, xVec, yVec, param0, param1 ); &nbsp; &nbsp; // Create a line from ellipse center in &nbsp; // direction of target angle: &nbsp; &nbsp; double targetAngle = Math.PI / 3.0; &nbsp; &nbsp; XYZ direction = new XYZ( &nbsp; &nbsp; Math.Cos( targetAngle ), &nbsp; &nbsp; Math.Sin( targetAngle ), &nbsp; &nbsp; 0 ); &nbsp; &nbsp; Line line = app.Create.NewLineUnbound( &nbsp; &nbsp; center, direction ); &nbsp; &nbsp; // Find intersection between line and ellipse: &nbsp; &nbsp; IntersectionResultArray results; &nbsp; e.Intersect( line, out results ); &nbsp; &nbsp; // Find the shortest intersection segment: &nbsp; &nbsp; foreach( IntersectionResult result in results ) &nbsp; { &nbsp; &nbsp; double p = result.UVPoint.U; &nbsp; &nbsp; if( p &lt; param1 ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; param1 = p; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; // Apply parameter to the ellipse: &nbsp; &nbsp; e.MakeBound( param0, param1 ); &nbsp; &nbsp; return e; }
```
