---
num: 1307
date: 2015-04-10
themes: [Geometry]
tags: [revit-api, tbc]
---

# Curved Wall Elevation Profile and Creator Class Update

<https://jeremytammik.github.io/tbc/a/1307_wall_elevation_profile.htm>

```csharp
&nbsp; public ModelCurve CreateModelCurve( Curve curve ) &nbsp; { &nbsp; &nbsp; return _credoc.NewModelCurve( curve, &nbsp; &nbsp; &nbsp; NewSketchPlaneContainCurve( curve ) ); &nbsp; }
```

```csharp
&nbsp; if( ( (LocationCurve) wall.Location ).Curve &nbsp; &nbsp; is Line ) &nbsp; { &nbsp; &nbsp; Plane plane = creapp.NewPlane( curves ); &nbsp; &nbsp; &nbsp; SketchPlane sketchPlane &nbsp; &nbsp; &nbsp; = SketchPlane.Create( doc, plane ); &nbsp; &nbsp; &nbsp; ModelCurveArray curveElements &nbsp; &nbsp; &nbsp; = credoc.NewModelCurveArray( &nbsp; &nbsp; &nbsp; &nbsp; curves, sketchPlane ); &nbsp; &nbsp; &nbsp; if( isCounterClockwise ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( ModelCurve c in curveElements ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; SetModelCurveColor( c, view, colorRed ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; foreach( var curve in curves.Cast&lt;Curve&gt;() ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; var mc = creator.CreateModelCurve( curve ); &nbsp; &nbsp; &nbsp; &nbsp; if( isCounterClockwise ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; SetModelCurveColor( mc, view, colorRed ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; ModelCurve CreateModelCurve( &nbsp; &nbsp; Curve curve, &nbsp; &nbsp; XYZ origin, &nbsp; &nbsp; XYZ normal ) &nbsp; { &nbsp; &nbsp; Plane plane = _creapp.NewPlane( normal, origin ); &nbsp; &nbsp; &nbsp; SketchPlane sketchPlane = SketchPlane.Create( &nbsp; &nbsp; &nbsp; _doc, plane ); &nbsp; &nbsp; &nbsp; return _credoc.NewModelCurve( &nbsp; &nbsp; &nbsp; curve, sketchPlane ); &nbsp; } &nbsp; &nbsp; public ModelCurveArray CreateModelCurves( &nbsp; &nbsp; Curve curve ) &nbsp; { &nbsp; &nbsp; var array = new ModelCurveArray(); &nbsp; &nbsp; &nbsp; var line = curve as Line; &nbsp; &nbsp; if( line != null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; array.Append( CreateModelLine( _doc, &nbsp; &nbsp; &nbsp; &nbsp; curve.GetEndPoint( 0 ), &nbsp; &nbsp; &nbsp; &nbsp; curve.GetEndPoint( 1 ) ) ); &nbsp; &nbsp; &nbsp; &nbsp; return array; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; var arc = curve as Arc; &nbsp; &nbsp; if( arc != null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; var origin = arc.Center; &nbsp; &nbsp; &nbsp; var normal = arc.Normal; &nbsp; &nbsp; &nbsp; &nbsp; array.Append( CreateModelCurve( &nbsp; &nbsp; &nbsp; &nbsp; arc, origin, normal ) ); &nbsp; &nbsp; &nbsp; &nbsp; return array; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; var ellipse = curve as Ellipse; &nbsp; &nbsp; if( ellipse != null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; var origin = ellipse.Center; &nbsp; &nbsp; &nbsp; var normal = ellipse.Normal; &nbsp; &nbsp; &nbsp; &nbsp; array.Append( CreateModelCurve( &nbsp; &nbsp; &nbsp; &nbsp; ellipse, origin, normal ) ); &nbsp; &nbsp; &nbsp; &nbsp; return array; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; var points = curve.Tessellate(); &nbsp; &nbsp; var p = points.First(); &nbsp; &nbsp; &nbsp; foreach( var q in points.Skip( 1 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; array.Append( CreateModelLine( _doc, p, q ) ); &nbsp; &nbsp; &nbsp; p = q; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; return array; &nbsp; }
```

```csharp
t = Transaction(doc, 'wall elevation profile') t.Start() colorRed = Color( 255, 0, 0 ) view = doc.ActiveView for wall in selection: sideFaceReference = HostObjectUtils.GetSideFaces( wall, ShellLayerType.Exterior ) [0] face = wall.GetGeometryObjectFromReference( sideFaceReference) offset = Transform.CreateTranslation( 5 * wall.Orientation); for curveLoop in face.GetEdgesAsCurveLoops(): curves = doc.Application.Create.NewCurveArray() for curve in curveLoop: curves.Append(curve.CreateTransformed(offset)) plane = doc.Application.Create.NewPlane( curves ) sketchPlane = SketchPlane.Create( doc, plane ) curveElements = doc.Create.NewModelCurveArray( curves, sketchPlane ) if curveLoop.IsCounterclockwise(wall.Orientation): for mcurve in curveElements: overrides = view.GetElementOverrides(mcurve.Id) overrides.SetProjectionLineColor(colorRed) view.SetElementOverrides(mcurve.Id, overrides) t.Commit()
```
