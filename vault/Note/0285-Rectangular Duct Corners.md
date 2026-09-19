---
num: 285
date: 2010-01-18
themes: [MEP]
tags: [revit-api, tbc]
---

# Rectangular Duct Corners

<https://jeremytammik.github.io/tbc/a/0285_rectangular_duct_corners.htm>

```csharp
&nbsp; XYZ p = connector.CoordinateSystem.OfPoint( &nbsp; &nbsp; new XYZ( connector.Width / 2, &nbsp; &nbsp; &nbsp; connector.Height / 2, 0 ) );
```

```csharp
&nbsp; XYZ p = connector.CoordinateSystem.OfPoint( &nbsp; &nbsp; new XYZ( connector.Height / 2, &nbsp; &nbsp; &nbsp; connector.Width / 2, 0 ) );
```

```csharp
static bool GetFirstRectangularConnector( &nbsp; Duct duct, &nbsp; out Connector c1 ) { &nbsp; c1 = null; &nbsp; &nbsp; ConnectorSet connectors &nbsp; &nbsp; = duct.ConnectorManager.Connectors; &nbsp; &nbsp; if( 0 &lt; connectors.Size ) &nbsp; { &nbsp; &nbsp; foreach( Connector c in connectors ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( ConnectorProfileType.RectProfile &nbsp; &nbsp; &nbsp; &nbsp; == c.Shape ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; c1 = c; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; else &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; Trace.WriteLine( &quot;Connector shape: &quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + c.Shape ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; return null != c1; }
```

```csharp
static bool FaceContainsConnector( &nbsp; Face face, &nbsp; Connector c ) { &nbsp; XYZ p = c.Origin; &nbsp; &nbsp; IntersectionResult result = face.Project( p ); &nbsp; &nbsp; return null != result &nbsp; &nbsp; &amp;&amp; Math.Abs( result.Distance ) &lt; 1e-9; }
```

```csharp
Application app = commandData.Application; &nbsp; if( ProductType.MEP != app.Product ) { &nbsp; message = &quot;Please run this command in Revit MEP.&quot;; &nbsp; return CmdResult.Failed; } &nbsp; Document doc = app.ActiveDocument; SelElementSet sel = doc.Selection.Elements; &nbsp; if( 0 == sel.Size ) { &nbsp; message = &quot;Please select some rectangular ducts.&quot;; &nbsp; return CmdResult.Failed; } &nbsp; // set up log file: &nbsp; string log = Assembly.GetExecutingAssembly().Location &nbsp; + &quot;.&quot; + DateTime.Now.ToString( &quot;yyyyMMdd&quot; ) &nbsp; + &quot;.log&quot;; &nbsp; if( File.Exists( log ) ) { &nbsp; File.Delete( log ); } &nbsp; TraceListener listener &nbsp; = new TextWriterTraceListener( log ); &nbsp; Trace.Listeners.Add( listener ); &nbsp; try { &nbsp; Trace.WriteLine( &quot;Begin&quot; ); &nbsp; &nbsp; // loop over all selected ducts: &nbsp; &nbsp; foreach( Duct duct in sel ) &nbsp; { &nbsp; &nbsp; if( null == duct ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Trace.TraceError( &quot;The selection is not a duct!&quot; ); &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // process each duct: &nbsp; &nbsp; &nbsp; &nbsp; Trace.WriteLine( &quot;========================&quot; ); &nbsp; &nbsp; &nbsp; Trace.WriteLine( &quot;Duct: Id = &quot; + duct.Id.Value ); &nbsp; &nbsp; &nbsp; &nbsp; AnalyseDuct( duct ); &nbsp; &nbsp; } &nbsp; } } catch( Exception ex ) { &nbsp; Trace.WriteLine( ex.ToString() ); } finally { &nbsp; Trace.Flush(); &nbsp; listener.Close(); &nbsp; Trace.Close(); &nbsp; Trace.Listeners.Remove( listener ); } return CmdResult.Failed;
```
