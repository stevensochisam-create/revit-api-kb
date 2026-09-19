---
num: 301
date: 2010-02-10
themes: [Geometry]
tags: [revit-api, tbc]
---

# Detail Curve on Level

<https://jeremytammik.github.io/tbc/a/0301_detail_curve_level.htm>

```csharp
&nbsp; XYZ p = XYZ.Zero; &nbsp; XYZ norm = XYZ.BasisZ; &nbsp; double startAngle = 0; &nbsp; double endAngle = 2 * Math.PI; &nbsp; double radius = 1.23; &nbsp; &nbsp; Plane plane = new Plane( norm, p ); &nbsp; &nbsp; Arc arc = app.Create.NewArc( &nbsp; &nbsp; plane, radius, startAngle, endAngle ); &nbsp; &nbsp; DetailArc detailArc &nbsp; &nbsp; = doc.Create.NewDetailCurve( &nbsp; &nbsp; &nbsp; doc.ActiveView, arc ) as DetailArc;
```

```csharp
using System; using Autodesk.Revit; using Autodesk.Revit.Elements; using Autodesk.Revit.Geometry; &nbsp; public class RevitCommand : IExternalCommand { &nbsp; public IExternalCommand.Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string messages, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; Application app = commandData.Application; &nbsp; &nbsp; Document doc = app.ActiveDocument; &nbsp; &nbsp; &nbsp; // Create an arc on the plane whose &nbsp; &nbsp; // center is at the plane origin: &nbsp; &nbsp; &nbsp; XYZ end0 = new XYZ( 0, 0, 1 ); &nbsp; &nbsp; XYZ end1 = new XYZ( 1, 3, 2 ); &nbsp; &nbsp; XYZ norm; &nbsp; &nbsp; &nbsp; if( end0.X == end1.X ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; norm = XYZ.BasisZ; &nbsp; &nbsp; } &nbsp; &nbsp; else if ( end0.Y == end1.Y ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; norm = XYZ.BasisZ; &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; norm = XYZ.BasisZ; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; double startAngle = 0; &nbsp; &nbsp; double endAngle = 2 * Math.PI; &nbsp; &nbsp; double radius = 5; &nbsp; &nbsp; &nbsp; Plane objPlane &nbsp; &nbsp; &nbsp; = app.Create.NewPlane( norm, XYZ.Zero ); &nbsp; &nbsp; &nbsp; // ViewPlan of &quot;Level 2&quot; &nbsp; &nbsp; &nbsp; ViewPlan vp2 = null; &nbsp; &nbsp; &nbsp; ElementIterator ei &nbsp; &nbsp; &nbsp; = doc.get_Elements( typeof( ViewPlan ) ); &nbsp; &nbsp; &nbsp; while( ei.MoveNext() ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; ViewPlan vp = ei.Current as ViewPlan; &nbsp; &nbsp; &nbsp; &nbsp; if( vp.GenLevel.Name.Equals( &quot;Level 2&quot; ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; vp2 = vp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; if( null == vp2 ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; vp2 = doc.ActiveView as ViewPlan; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; if( null != vp2 ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // draw the circle: &nbsp; &nbsp; &nbsp; &nbsp; Arc arc = app.Create.NewArc( objPlane, &nbsp; &nbsp; &nbsp; &nbsp; radius, startAngle, endAngle ); &nbsp; &nbsp; &nbsp; &nbsp; DetailArc detailArc &nbsp; &nbsp; &nbsp; &nbsp; = doc.Create.NewDetailCurve( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; vp2, arc ) as DetailArc; &nbsp; &nbsp; } &nbsp; &nbsp; return (null == vp2) &nbsp; &nbsp; &nbsp; ? IExternalCommand.Result.Failed &nbsp; &nbsp; &nbsp; : IExternalCommand.Resul
```
