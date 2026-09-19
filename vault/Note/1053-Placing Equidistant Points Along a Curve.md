---
num: 1053
date: 2013-11-07
themes: [Geometry]
tags: [revit-api, tbc]
---

# Placing Equidistant Points Along a Curve

<https://jeremytammik.github.io/tbc/a/1053_equi_distant_pts.htm>

```csharp
&nbsp; double param1 = curve.GetEndParameter(0); &nbsp; double param2 = curve.GetEndParameter(1); &nbsp; &nbsp; double paramCalc = param1 + ((param2 - param1) &nbsp; &nbsp; * requiredDist / curveLength); &nbsp; &nbsp; XYZ evaluatedPoint = null; &nbsp; &nbsp; if (curve.IsInside(paramCalc)) &nbsp; { &nbsp; &nbsp; double normParam = curve &nbsp; &nbsp; &nbsp; .ComputeNormalizedParameter(paramCalc); &nbsp; &nbsp; &nbsp; evaluatedPoint = curve.Evaluate( &nbsp; &nbsp; &nbsp; normParam, true))); &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Create a horizontal detail curve circle of &nbsp; /// the given radius at the specified point. &nbsp; /// &lt;/summary&gt; &nbsp; DetailArc CreateCircle( &nbsp; &nbsp; Document doc, &nbsp; &nbsp; XYZ location, &nbsp; &nbsp; double radius ) &nbsp; { &nbsp; &nbsp; XYZ norm = XYZ.BasisZ; &nbsp; &nbsp; &nbsp; double startAngle = 0; &nbsp; &nbsp; double endAngle = 2 * Math.PI; &nbsp; &nbsp; &nbsp; Plane plane = new Plane( norm, location ); &nbsp; &nbsp; &nbsp; Arc arc = Arc.Create( plane, &nbsp; &nbsp; &nbsp; radius, startAngle, endAngle ); &nbsp; &nbsp; &nbsp; return doc.Create.NewDetailCurve( &nbsp; &nbsp; &nbsp; doc.ActiveView, arc ) as DetailArc; &nbsp; }
```

```csharp
public Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; UIApplication uiapp = commandData.Application; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; Reference r = null; &nbsp; &nbsp; try &nbsp; { &nbsp; &nbsp; r = uidoc.Selection.PickObject( &nbsp; &nbsp; &nbsp; ObjectType.Element, &nbsp; &nbsp; &nbsp; new CurveSelectionFilter(), &nbsp; &nbsp; &nbsp; &quot;Please pick an arc or spline to select path&quot; ); &nbsp; } &nbsp; catch( Autodesk.Revit.Exceptions &nbsp; &nbsp; .OperationCanceledException ) &nbsp; { &nbsp; &nbsp; return Result.Cancelled; &nbsp; } &nbsp; &nbsp; if( null == r ) &nbsp; { &nbsp; &nbsp; message = &quot;Null pick object reference.&quot;; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; &nbsp; Element e = doc.GetElement( r ); &nbsp; &nbsp; if( null == e || !( e is CurveElement ) ) &nbsp; { &nbsp; &nbsp; message = &quot;Not a curve element.&quot;; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; &nbsp; // Extract data from the selected curve. &nbsp; &nbsp; Curve curve = ( e as CurveElement ).GeometryCurve; &nbsp; &nbsp; IList&lt;XYZ&gt; tessellation = curve.Tessellate(); &nbsp; &nbsp; // Create a list of equi-distant points. &nbsp; &nbsp; List&lt;XYZ&gt; pts = new List&lt;XYZ&gt;( 1 ); &nbsp; &nbsp; double stepsize = 5.0; &nbsp; double dist = 0.0; &nbsp; &nbsp; XYZ p = curve.GetEndPoint( 0 ); &nbsp; &nbsp; foreach( XYZ q in tessellation ) &nbsp; { &nbsp; &nbsp; if( 0 == pts.Count ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; pts.Add( p ); &nbsp; &nbsp; &nbsp; dist = 0.0; &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; dist += p.DistanceTo( q ); &nbsp; &nbsp; &nbsp; &nbsp; if( dist &gt;= stepsize ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; pts.Add( q ); &nbsp; &nbsp; &nbsp; &nbsp; dist = 0; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; p = q; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; // Place a marker circle at each point. &nbsp; &nbsp; using( Transaction tx = new Transaction( doc ) ) &nbsp; { &nbsp; &nbsp; tx.Start( &quot;Draw Curves at Points&quot; ); &nbsp; &nbsp; &nbsp; foreach( XYZ pt in pts ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; CreateCircle( doc, pt, 1 ); &nbsp; &nbsp; } &nbsp; &nbsp; tx.Commit(); &nbsp; } &nbsp; return Result.Succeeded; }
```
