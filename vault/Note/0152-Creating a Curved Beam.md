---
num: 152
date: 2009-06-15
themes: [Geometry]
tags: [revit-api, tbc]
---

# Creating a Curved Beam

<https://jeremytammik.github.io/tbc/a/0152_curved_beam.htm>

```csharp
Application app = commandData.Application; Document doc = app.ActiveDocument; &nbsp; Level level = doc.ActiveView.Level; &nbsp; FamilySymbol symbol = null; &nbsp; string path = &quot;C:/Documents and Settings&quot; &nbsp; + &quot;/All Users/Application Data/Autodesk&quot; &nbsp; + &quot;/RST 2009/Metric Library/Structural&quot; &nbsp; + &quot;/Framing/Steel/&quot;; &nbsp; string family = &quot;M_WWF-Welded Wide Flange&quot;; &nbsp; string ext = &quot;.rfa&quot;; &nbsp; string filename = path + family + ext; &nbsp; string symbolName = &quot;WWF600x460&quot;; &nbsp; if ( doc.LoadFamilySymbol( filename, symbolName, out symbol ) ) { &nbsp; Curve c = CreateNurbSpline( app ); &nbsp; &nbsp; FamilyInstance inst &nbsp; &nbsp; = doc.Create.NewFamilyInstance( &nbsp; &nbsp; &nbsp; c, symbol, level, StructuralType.Beam ); &nbsp; &nbsp; return IExternalCommand.Result.Succeeded; } else { &nbsp; message = &quot;Couldn't load &quot; + filename; &nbsp; return IExternalCommand.Result.Failed; }
```

```csharp
NurbSpline CreateNurbSpline( Application app ) { &nbsp; XYZArray ctrPoints = app.Create.NewXYZArray(); &nbsp; &nbsp; XYZ xyz1 = new XYZ( -41.8 * 1, 0, -9.02 * 1 ); &nbsp; XYZ xyz2 = new XYZ( -9.2 * 2, 0, 0.82 * 50 ); &nbsp; XYZ xyz3 = new XYZ( 9.2 * 2, 0, -0.82 * 50 ); &nbsp; XYZ xyz4 = new XYZ( 41.8 * 1, 0, 9.02 * 1 ); &nbsp; &nbsp; ctrPoints.Append( xyz1 ); &nbsp; ctrPoints.Append( xyz2 ); &nbsp; ctrPoints.Append( xyz3 ); &nbsp; ctrPoints.Append( xyz4 ); &nbsp; &nbsp; DoubleArray weights = new DoubleArray(); &nbsp; &nbsp; double w1 = 1, w2 = 1, w3 = 1, w4 = 1; &nbsp; &nbsp; weights.Append( ref w1 ); &nbsp; weights.Append( ref w2 ); &nbsp; weights.Append( ref w3 ); &nbsp; weights.Append( ref w4 ); &nbsp; &nbsp; DoubleArray knots = new DoubleArray(); &nbsp; &nbsp; double k0 = 0, k1 = 0, k2 = 0, k3 = 0, &nbsp; &nbsp; k4 = 34.425128, k5 = 34.425128, &nbsp; &nbsp; k6 = 34.425128, k7 = 34.425128; &nbsp; &nbsp; knots.Append( ref k0 ); &nbsp; knots.Append( ref k1 ); &nbsp; knots.Append( ref k2 ); &nbsp; knots.Append( ref k3 ); &nbsp; knots.Append( ref k4 ); &nbsp; knots.Append( ref k5 ); &nbsp; knots.Append( ref k6 ); &nbsp; knots.Append( ref k7 ); &nbsp; &nbsp; NurbSpline detailNurbSpline &nbsp; &nbsp; = app.Create.NewNurbSpline( &nbsp; &nbsp; ctrPoints, weights, knots, 3, false, true ); &nbsp; &nbsp; return detailNurbSpline; }
```
