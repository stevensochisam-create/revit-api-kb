---
num: 375
date: 2010-05-27
themes: [Geometry]
tags: [revit-api, tbc]
---

# Model Curve Creator

<https://jeremytammik.github.io/tbc/a/0375_model_curve_creator.htm>

```csharp
SketchPlane NewSketchPlaneContainCurve( &nbsp; Curve curve ) { &nbsp; XYZ p = curve.get_EndPoint( 0 ); &nbsp; XYZ normal = GetCurveNormal( curve ); &nbsp; Plane plane = _app.NewPlane( normal, p ); &nbsp; &nbsp; return _doc.NewSketchPlane( plane ); }
```

```csharp
public void CreateModelCurve( Curve curve ) { &nbsp; _doc.NewModelCurve( curve, &nbsp; &nbsp; NewSketchPlaneContainCurve( curve ) ); }
```

```csharp
[Transaction( TransactionMode.Automatic )] [Regeneration( RegenerationOption.Manual )] class CmdCurtainWallGeom : IExternalCommand { &nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication uiapp = commandData.Application; &nbsp; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; &nbsp; Application app = uiapp.Application; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; Wall wall = Util.SelectSingleElementOfType( &nbsp; &nbsp; &nbsp; uidoc, typeof( Wall ), &quot;a curtain wall&quot; ) &nbsp; &nbsp; &nbsp; as Wall; &nbsp; &nbsp; &nbsp; if( null == wall ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; message = &quot;Please select a single &quot; &nbsp; &nbsp; &nbsp; &nbsp; + &quot;curtain wall element.&quot;; &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; LocationCurve locationcurve &nbsp; &nbsp; &nbsp; &nbsp; = wall.Location as LocationCurve; &nbsp; &nbsp; &nbsp; &nbsp; Curve curve = locationcurve.Curve; &nbsp; &nbsp; &nbsp; &nbsp; // move whole geometry over by length of wall: &nbsp; &nbsp; &nbsp; &nbsp; XYZ p = curve.get_EndPoint( 0 ); &nbsp; &nbsp; &nbsp; XYZ q = curve.get_EndPoint( 1 ); &nbsp; &nbsp; &nbsp; XYZ v = q - p; &nbsp; &nbsp; &nbsp; &nbsp; Transform tv = Transform.get_Translation( v ); &nbsp; &nbsp; &nbsp; &nbsp; curve = curve.get_Transformed( tv ); &nbsp; &nbsp; &nbsp; &nbsp; Creator creator = new Creator( doc ); &nbsp; &nbsp; &nbsp; creator.CreateModelCurve( curve ); &nbsp; &nbsp; &nbsp; &nbsp; Options opt = app.Create.NewGeometryOptions(); &nbsp; &nbsp; &nbsp; opt.IncludeNonVisibleObjects = true; &nbsp; &nbsp; &nbsp; &nbsp; GeometryElement e = wall.get_Geometry( opt ); &nbsp; &nbsp; &nbsp; &nbsp; foreach( GeometryObject obj in e.Objects ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; curve = obj as Curve; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( null != curve ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; curve = curve.get_Transformed( tv ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; creator.CreateModelCurve( curve ); &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```
