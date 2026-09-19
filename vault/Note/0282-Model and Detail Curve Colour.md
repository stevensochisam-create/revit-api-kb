---
num: 282
date: 2010-01-14
themes: [Geometry]
tags: [revit-api, tbc]
---

# Model and Detail Curve Colour

<https://jeremytammik.github.io/tbc/a/0282_change_detail_curve_colour.htm>

```csharp
Application app = commandData.Application; Document doc = app.ActiveDocument; View view = doc.ActiveView; &nbsp; // Create a geometry line &nbsp; XYZ startPoint = new XYZ( 0, 0, 0 ); XYZ endPoint = new XYZ( 10, 10, 0 ); &nbsp; Line geomLine = app.Create.NewLine( &nbsp; startPoint, endPoint, true ); &nbsp; // Create a geometry arc &nbsp; XYZ end0 = new XYZ( 1, 0, 0 ); XYZ end1 = new XYZ( 10, 10, 10 ); XYZ pointOnCurve = new XYZ( 10, 0, 0 ); &nbsp; Arc geomArc = app.Create.NewArc( &nbsp; end0, end1, pointOnCurve ); &nbsp; // Create a geometry plane &nbsp; XYZ origin = new XYZ( 0, 0, 0 ); XYZ normal = new XYZ( 1, 1, 0 ); &nbsp; Plane geomPlane = app.Create.NewPlane( &nbsp; normal, origin ); &nbsp; // Create a sketch plane in current document &nbsp; SketchPlane sketch = doc.Create.NewSketchPlane( &nbsp; geomPlane ); &nbsp; // Create a DetailLine element using the // newly created geometry line and sketch plane &nbsp; DetailLine line = doc.Create.NewDetailCurve( &nbsp; view, geomLine ) as DetailLine; &nbsp; // Create a DetailArc element using the // newly created geometry arc and sketch plane &nbsp; DetailArc arc = doc.Create.NewDetailCurve( &nbsp; view, geomArc ) as DetailArc; &nbsp; // Change detail curve colour. // Initially, this only affects the newly // created curves. However, when the view // is refreshed, all detail curves will // be updated. &nbsp; GraphicsStyle gs = arc.LineStyle as GraphicsStyle; &nbsp; gs.GraphicsStyleCategory.LineColor &nbsp; = new Color( 250, 10, 10 ); &nbsp; return CmdResult.Succeeded;
```
