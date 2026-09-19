---
num: 366
date: 2010-05-17
themes: [MEP]
tags: [revit-api, tbc]
---

# Cable Tray Orientation and Fittings

<https://jeremytammik.github.io/tbc/a/0366_cable_tray_fitting.htm>

```csharp
&nbsp; ElementId idType = new ElementId( 411325 ); &nbsp; ElementId idLevel = new ElementId( 311 ); &nbsp; &nbsp; XYZ start1 = new XYZ( -30.49, 38.42, 10.05 ); &nbsp; XYZ end1 = new XYZ( -20.43, 30.83, 10.05 ); &nbsp; CableTray tray1 = CableTray.Create( &nbsp; &nbsp; doc, idType, start1, end1, idLevel ); &nbsp; &nbsp; XYZ start2 = new XYZ( -20.43, 30.83, 10.05 ); &nbsp; XYZ end2 = new XYZ( -20.43, 30.83, 13.33 ); &nbsp; CableTray tray2 = CableTray.Create( &nbsp; &nbsp; doc, idType, start2, end2, idLevel ); &nbsp; &nbsp; Connector c1start, c1end = null; &nbsp; &nbsp; foreach( Connector c in &nbsp; &nbsp; tray1.MEPSystem.ConnectorManager.Connectors ) &nbsp; { &nbsp; &nbsp; if( c.Origin.IsAlmostEqualTo( start1 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c1start = c; &nbsp; &nbsp; } &nbsp; &nbsp; else if( c.Origin.IsAlmostEqualTo( end1 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c1end = c; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; Connector c2start = null, c2end; &nbsp; &nbsp; foreach( Connector c in &nbsp; &nbsp; tray2.MEPSystem.ConnectorManager.Connectors ) &nbsp; { &nbsp; &nbsp; if( c.Origin.IsAlmostEqualTo( start2 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c2start = c; &nbsp; &nbsp; } &nbsp; &nbsp; else if( c.Origin.IsAlmostEqualTo( end2 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c2end = c; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; if( null != c1end &amp;&amp; null != c2start ) &nbsp; { &nbsp; &nbsp; doc.Create.NewElbowFitting( c1end, c2start ); &nbsp; }
```

```csharp
&nbsp; Connector c1start, c1end = null; &nbsp; &nbsp; foreach( Connector c in &nbsp; &nbsp; tray1.ConnectorManager.Connectors ) &nbsp; { &nbsp; &nbsp; if( c.Origin.IsAlmostEqualTo( start1 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c1start = c; &nbsp; &nbsp; } &nbsp; &nbsp; else if( c.Origin.IsAlmostEqualTo( end1 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c1end = c; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; Connector c2start = null, c2end; &nbsp; &nbsp; foreach( Connector c in &nbsp; &nbsp; tray2.ConnectorManager.Connectors ) &nbsp; { &nbsp; &nbsp; if( c.Origin.IsAlmostEqualTo( start2 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c2start = c; &nbsp; &nbsp; } &nbsp; &nbsp; else if( c.Origin.IsAlmostEqualTo( end2 ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; c2end = c; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; if( null != c1end &amp;&amp; null != c2start ) &nbsp; { &nbsp; &nbsp; c1end.ConnectTo( c2start ); &nbsp; &nbsp; &nbsp; // this throws &nbsp; &nbsp; // Autodesk.Revit.Exceptions &nbsp; &nbsp; // .InvalidOperationException: &nbsp; &nbsp; // &quot;failed to insert elbow&quot;. &nbsp; &nbsp; &nbsp; doc.Create.NewElbowFitting( c1end, c2start ); &nbsp; }
```

```csharp
m_document.Create.NewElbowFitting( connectors[2], baseConn2 );
```

```csharp
Autodesk.Revit.Exceptions.InvalidOperationException: "failed to insert elbow".
```

```csharp
&nbsp; private const double min1FittingLength = 1;
```
