---
num: 1343
date: 2015-07-13
themes: [Geometry]
tags: [revit-api, tbc]
---

# Clicks, DMU, Surfaces, FireRating Feedback, Vacation

<https://jeremytammik.github.io/tbc/a/1343_vacation.htm>

```csharp
&nbsp; UIApplication uiapp = commandData.Application; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; using( Transaction tx = new Transaction( doc ) ) &nbsp; { &nbsp; &nbsp; tx.Start( &quot;Create a Floor&quot; ); &nbsp; &nbsp; &nbsp; int n = 4; &nbsp; &nbsp; XYZ[] points = new XYZ[n]; &nbsp; &nbsp; points[0] = XYZ.Zero; &nbsp; &nbsp; points[1] = new XYZ( 10.0, 0.0, 0.0 ); &nbsp; &nbsp; points[2] = new XYZ( 10.0, 10.0, 0.0 ); &nbsp; &nbsp; points[3] = new XYZ( 0.0, 10.0, 0.0 ); &nbsp; &nbsp; &nbsp; CurveArray curve = new CurveArray(); &nbsp; &nbsp; &nbsp; for( int i = 0; i &lt; n; i++ ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Line line = Line.CreateBound( points[i], &nbsp; &nbsp; &nbsp; &nbsp; points[(i &lt; n-1) ? i + 1 : 0] ); &nbsp; &nbsp; &nbsp; &nbsp; curve.Append( line ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; doc.Create.NewFloor( curve, true ); &nbsp; &nbsp; &nbsp; tx.Commit(); &nbsp; } &nbsp; return Result.Succeeded;
```
