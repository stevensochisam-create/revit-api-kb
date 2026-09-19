---
num: 1052
date: 2013-11-06
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# Determining Host Document Location of a Linked Element

<https://jeremytammik.github.io/tbc/a/1052_linked_elem_location.htm>

```csharp
&nbsp; Document d = rvtlink.GetLinkDocument(); &nbsp; Element e = d.GetElement( id ); &nbsp; LocationCurve curve = e.Location as LocationCurve; &nbsp; XYZ p = curve.Curve.GetEndPoint( 0 ); &nbsp; XYZ q = curve.Curve.GetEndPoint( 1 );
```

```csharp
&nbsp; UIApplication uiapp = commandData.Application; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; Document doc = uidoc.Document; &nbsp; Selection sel = uidoc.Selection; &nbsp; &nbsp; Reference r = sel.PickObject( &nbsp; &nbsp; ObjectType.Element, &nbsp; &nbsp; new LinkSelectionFilter(), &nbsp; &nbsp; &quot;Please pick an import instance&quot; ); &nbsp; &nbsp; RevitLinkInstance rvtlink = doc.GetElement( r ) &nbsp; &nbsp; as RevitLinkInstance; &nbsp; &nbsp; if( rvtlink == null ) &nbsp; { &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; &nbsp; // For this example, just focus on &nbsp; // the blue and red walls &nbsp; &nbsp; var walls = new FilteredElementCollector( &nbsp; &nbsp; &nbsp; rvtlink.GetLinkDocument() ) &nbsp; &nbsp; .OfClass( typeof( Wall ) ) &nbsp; &nbsp; .Where( c =&gt; c.Id.IntegerValue == 179910 &nbsp; &nbsp; &nbsp; || c.Id.IntegerValue == 179980 ); &nbsp; &nbsp; foreach( Wall wall in walls ) &nbsp; { &nbsp; &nbsp; // Ask Revit for coordinates; these are &nbsp; &nbsp; // related to the linked file (Document A). &nbsp; &nbsp; &nbsp; LocationCurve curve = wall.Location &nbsp; &nbsp; &nbsp; as LocationCurve; &nbsp; &nbsp; &nbsp; XYZ p = curve.Curve.GetEndPoint( 0 ); &nbsp; &nbsp; XYZ q = curve.Curve.GetEndPoint( 1 ); &nbsp; &nbsp; &nbsp; if( wall.Id.IntegerValue == 179910 ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; TaskDialog.Show( &quot;The Red wall&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &quot;The red wall is situated at &quot; &nbsp; &nbsp; &nbsp; &nbsp; + PointString( p ) ); &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; TaskDialog.Show( &quot;The Blue wall&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &quot;The blue wall is situated at: &quot; &nbsp; &nbsp; &nbsp; &nbsp; + PointString( p ) ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; // So, how can I determine where the red and &nbsp; &nbsp; // blue walls are in the coordinate system of &nbsp; &nbsp; // the document B file ? &nbsp; } &nbsp; return Result.Succeeded;
```

```csharp
&nbsp; const double _inch_to_mm = 25.4; &nbsp; const double _foot_to_mm = 12 * _inch_to_mm; &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Return a string for a real number &nbsp; /// formatted to two decimal places. &nbsp; /// &lt;/summary&gt; &nbsp; public static string RealString( double a ) &nbsp; { &nbsp; &nbsp; return a.ToString( &quot;0.##&quot; ); &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Return a string for an XYZ point &nbsp; /// or vector with its coordinates &nbsp; /// converted from feet to millimetres &nbsp; /// and formatted to two decimal places. &nbsp; /// &lt;/summary&gt; &nbsp; public static string PointStringMm( XYZ p ) &nbsp; { &nbsp; &nbsp; return string.Format( &quot;({0},{1},{2})&quot;, &nbsp; &nbsp; &nbsp; RealString( p.X * _foot_to_mm ), &nbsp; &nbsp; &nbsp; RealString( p.Y * _foot_to_mm ), &nbsp; &nbsp; &nbsp; RealString( p.Z * _foot_to_mm ) ); &nbsp; }
```

```csharp
&nbsp; // Transformation from linked file to host &nbsp; &nbsp; Transform t = rvtlink.GetTotalTransform(); &nbsp; &nbsp; foreach( Wall wall in walls ) &nbsp; { &nbsp; &nbsp; // Ask Revit for coordinates; these are &nbsp; &nbsp; // related to the linked file (Document A). &nbsp; &nbsp; &nbsp; LocationCurve curve = wall.Location &nbsp; &nbsp; &nbsp; as LocationCurve; &nbsp; &nbsp; &nbsp; XYZ p = curve.Curve.GetEndPoint( 0 ); &nbsp; &nbsp; XYZ q = curve.Curve.GetEndPoint( 1 ); &nbsp; &nbsp; &nbsp; string title = &quot;The {0} Wall&quot;; &nbsp; &nbsp; &nbsp; string msg = &quot;The {0} wall is situated at {1} &quot; &nbsp; &nbsp; &nbsp; + &quot;in the source document and at {2} in the &quot; &nbsp; &nbsp; &nbsp; + &quot;target one.&quot;; &nbsp; &nbsp; &nbsp; bool red = ( wall.Id.IntegerValue == 179910 ); &nbsp; &nbsp; &nbsp; TaskDialog.Show( &nbsp; &nbsp; &nbsp; string.Format( title, red ? &quot;Red&quot; : &quot;Blue&quot; ), &nbsp; &nbsp; &nbsp; string.Format( msg, &nbsp; &nbsp; &nbsp; &nbsp; red ? &quot;red&quot; : &quot;blue&quot;, &nbsp; &nbsp; &nbsp; &nbsp; PointStringMm( q ), &nbsp; &nbsp; &nbsp; &nbsp; PointStringMm( t.OfPoint( q ) ) ) ); &nbsp; }
```
