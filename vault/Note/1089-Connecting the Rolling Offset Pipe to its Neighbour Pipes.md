---
num: 1089
date: 2014-01-14
themes: [MEP]
tags: [revit-api, tbc]
---

# Connecting the Rolling Offset Pipe to its Neighbour Pipes

<https://jeremytammik.github.io/tbc/a/1089_rolling_offset_connect.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Return the given element's connector manager, &nbsp; /// using either the family instance MEPModel or &nbsp; /// directly from the MEPCurve connector manager &nbsp; /// for ducts and pipes. &nbsp; /// &lt;/summary&gt; &nbsp; static ConnectorManager GetConnectorManager( &nbsp; &nbsp; Element e ) &nbsp; { &nbsp; &nbsp; MEPCurve mc = e as MEPCurve; &nbsp; &nbsp; FamilyInstance fi = e as FamilyInstance; &nbsp; &nbsp; &nbsp; if( null == mc &amp;&amp; null == fi ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; throw new ArgumentException( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Element is neither an MEP curve nor a fitting.&quot; ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; return null == mc &nbsp; &nbsp; &nbsp; ? fi.MEPModel.ConnectorManager &nbsp; &nbsp; &nbsp; : mc.ConnectorManager; &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Return the connector in the set &nbsp; /// closest to the given point. &nbsp; /// &lt;/summary&gt; &nbsp; static Connector GetConnectorClosestTo( &nbsp; &nbsp; ConnectorSet connectors, &nbsp; &nbsp; XYZ p ) &nbsp; { &nbsp; &nbsp; Connector targetConnector = null; &nbsp; &nbsp; double minDist = double.MaxValue; &nbsp; &nbsp; &nbsp; foreach( Connector c in connectors ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; double d = c.Origin.DistanceTo( p ); &nbsp; &nbsp; &nbsp; &nbsp; if( d &lt; minDist ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; targetConnector = c; &nbsp; &nbsp; &nbsp; &nbsp; minDist = d; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return targetConnector; &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Connect the two given elements at point p. &nbsp; /// &lt;/summary&gt; &nbsp; /// &lt;exception cref=&quot;ArgumentException&quot;&gt;Thrown if &nbsp; /// one of the given elements lacks connectors. &nbsp; /// &lt;/exception&gt; &nbsp; public static void Connect( &nbsp; &nbsp; XYZ p, &nbsp; &nbsp; Element a, &nbsp; &nbsp; Element b ) &nbsp; { &nbsp; &nbsp; ConnectorManager cm = GetConnectorManager( a ); &nbsp; &nbsp; &nbsp; if( null == cm ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; throw new ArgumentException( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Element a has no connectors.&quot; ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; Connector ca = GetConnectorClosestTo( &nbsp; &nbsp; &nbsp; cm.Connectors, p ); &nbsp; &nbsp; &nbsp; cm = GetConnectorManager( b ); &nbsp; &nbsp; &nbsp; if( null == cm ) &nbsp; &nbsp
```

```csharp
&nbsp; if( null != pipe ) &nbsp; { &nbsp; &nbsp; // Connect rolling offset pipe segment &nbsp; &nbsp; // with its neighbours &nbsp; &nbsp; &nbsp; Util.Connect( q0, pipes[0], pipe ); &nbsp; &nbsp; Util.Connect( q1, pipe, pipes[1] ); &nbsp; }
```
