---
num: 1008
date: 2013-08-28
themes: [MEP]
tags: [revit-api, tbc]
---

# Open MEP Connector Warning

<https://jeremytammik.github.io/tbc/a/1008_loose_connector.htm>

```csharp
&nbsp; ConnectorSet connectors &nbsp; &nbsp; = GetConnectorManager( e ).Connectors; &nbsp; &nbsp; int nUnconnected = connectors &nbsp; &nbsp; .Cast&lt;Connector&gt;() &nbsp; &nbsp; .Count&lt;Connector&gt;( c =&gt; !c.IsConnected ); &nbsp; &nbsp; bool hasOpenConnectors = 0 &lt; nUnconnected; &nbsp; &nbsp; string s = 0 == nUnconnected &nbsp; &nbsp; ? string.Empty &nbsp; &nbsp; : string.Format( &quot; with {0} open connector{1}&quot;, &nbsp; &nbsp; &nbsp; nUnconnected, Util.PluralSuffix( nUnconnected ) );
```

```csharp
Duct &lt;630420 Mitered Elbows&gt; has 2 connectors and max flow 22.08. . . . Duct &lt;630695 Short Radius&gt; has 2 connectors and max flow 4.58. Duct &lt;630991 Mitered Elbows&gt; has 2 connectors and max flow 0. Duct &lt;630992 Mitered Elbows&gt; has 2 connectors and max flow 0 with 1 open connector. Duct &lt;630995 Mitered Elbows&gt; has 2 connectors and max flow 4.58. . . . Duct &lt;631007 Short Radius&gt; has 2 connectors and max flow 4.58. Duct &lt;631074 Mitered Elbows&gt; has 2 connectors and max flow 0. Duct &lt;631075 Mitered Elbows&gt; has 6 connectors and max flow 8.33 with 1 open connector. Duct &lt;631077 Mitered Elbows&gt; has 2 connectors and max flow 4.58. . . . Duct &lt;632298 Mitered Elbows&gt; has 2 connectors and max flow 8.33. Set MEP Duct Flow Parameter: Set max flow parameter on 43 ducts, 2 of which have open connectors.
```
