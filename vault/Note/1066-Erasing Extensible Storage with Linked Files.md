---
num: 1066
date: 2013-11-25
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# Erasing Extensible Storage with Linked Files

<https://jeremytammik.github.io/tbc/a/1066_erase_estore_link.htm>

```csharp
&nbsp; public void DeleteSchema() &nbsp; { &nbsp; &nbsp; using( Transaction trans = new Transaction( _doc ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; trans.Start( &quot;Delete Schema&quot; ); &nbsp; &nbsp; &nbsp; Schema schema = Schema.Lookup( _schemaGuid ); &nbsp; &nbsp; &nbsp; Schema.EraseSchemaAndAllEntities( schema, false ); &nbsp; &nbsp; &nbsp; trans.Commit(); &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; collector = new FilteredElementCollector( famDoc ); &nbsp; collector.OfClass( typeof( ConnectorElement ) ); &nbsp; &nbsp; ICollection&lt;ElementId&gt; connectors &nbsp; &nbsp; = collector.ToElementIds(); &nbsp; &nbsp; if( connectors.Count &gt; 0 ) &nbsp; &nbsp; view.HideElements( connectors );
```

```csharp
&nbsp; view = View3D.CreateIsometric( famDoc, &nbsp; &nbsp; viewFamilyType.Id );
```

```csharp
&nbsp; // Hide connectors &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector(view.Document); &nbsp; &nbsp; collector.OfClass(typeof(ConnectorElement)); &nbsp; &nbsp; ICollection&lt;ElementId&gt; connectors &nbsp; &nbsp; = collector.ToElementIds(); &nbsp; &nbsp; if (connectors.Count &gt; 0) &nbsp; &nbsp; view.HideElements(connectors); &nbsp; &nbsp; view.Document.Regenerate(); // &lt;---- Add this! ------ &nbsp; &nbsp; // Export view
```
