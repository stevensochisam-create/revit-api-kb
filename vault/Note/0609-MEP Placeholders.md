---
num: 609
date: 2011-07-04
themes: [MEP]
tags: [revit-api, tbc]
---

# MEP Placeholders

<https://jeremytammik.github.io/tbc/a/0609_mep_placeholder.htm>

```csharp
class EquipmentElement { &nbsp; public FamilyInstance FamilyInstance; &nbsp; public Connector SupplyAirConnector; &nbsp; public XYZ ConnectionPoint; &nbsp; public XYZ ConnectionDirection; &nbsp; &nbsp; public EquipmentElement( &nbsp; &nbsp; FamilyInstance familyInstance, &nbsp; &nbsp; Connector supplyAirConnector, &nbsp; &nbsp; XYZ connectionPoint, &nbsp; &nbsp; XYZ connectionDirection ) &nbsp; { &nbsp; &nbsp; FamilyInstance = familyInstance; &nbsp; &nbsp; SupplyAirConnector = supplyAirConnector; &nbsp; &nbsp; ConnectionPoint = connectionPoint; &nbsp; &nbsp; ConnectionDirection = connectionDirection; &nbsp; } }
```

```csharp
static Connector GetDuctConnectorAt( &nbsp; Duct duct, &nbsp; XYZ location, &nbsp; out Connector otherConnector ) { &nbsp; otherConnector = null; &nbsp; &nbsp; Connector targetConnector = null; &nbsp; &nbsp; ConnectorManager cm = duct.ConnectorManager; &nbsp; &nbsp; foreach( Connector c in cm.Connectors ) &nbsp; { &nbsp; &nbsp; if( c.Origin.IsAlmostEqualTo( location ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; targetConnector = c; &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; otherConnector = c; &nbsp; &nbsp; } &nbsp; } &nbsp; return targetConnector; }
```

```csharp
public Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; Document doc = commandData.View.Document; &nbsp; &nbsp; Transaction t = new Transaction( doc ); &nbsp; t.Start( &quot;Convert placeholder network&quot; ); &nbsp; &nbsp; FilteredElementCollector ductCollector &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( Duct ) ); &nbsp; &nbsp; Func&lt;Duct, bool&gt; isPlaceholder &nbsp; &nbsp; = duct =&gt; duct.IsPlaceholder; &nbsp; &nbsp; IEnumerable&lt;Duct&gt; ducts = ductCollector &nbsp; &nbsp; .OfType&lt;Duct&gt;() &nbsp; &nbsp; .Where&lt;Duct&gt;( isPlaceholder ); &nbsp; &nbsp; ICollection&lt;ElementId&gt; ductIds = ducts &nbsp; &nbsp; .Select&lt;Duct, ElementId&gt;( duct =&gt; duct.Id ) &nbsp; &nbsp; .ToList&lt;ElementId&gt;(); &nbsp; &nbsp; MechanicalUtils.ConvertDuctPlaceholders( &nbsp; &nbsp; doc, ductIds ); &nbsp; &nbsp; t.Commit(); &nbsp; &nbsp; return Result.Succeeded; }
```

```csharp
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt; &lt;RevitAddIns&gt; &nbsp; &lt;AddIn Type=&quot;Command&quot;&gt; &nbsp; &nbsp; &lt;Text&gt;Create MEP Placeholders&lt;/Text&gt; &nbsp; &nbsp; &lt;Description&gt;Create MEP placeholder elements&lt;/Description&gt; &nbsp; &nbsp; &lt;Assembly&gt;C:\a\lib\revit\2012\adn\webcast\src\MepPlaceholders\MepPlaceholders\bin\Debug\MepPlaceholders.dll&lt;/Assembly&gt; &nbsp; &nbsp; &lt;FullClassName&gt;MepPlaceholders.CreatePlaceholders&lt;/FullClassName&gt; &nbsp; &nbsp; &lt;ClientId&gt;54b7cf02-64bd-4af5-a701-030a81e6c0d5&lt;/ClientId&gt; &nbsp; &nbsp; &lt;VendorId&gt;ADNP&lt;/VendorId&gt; &nbsp; &nbsp; &lt;VendorDescription&gt;Autodesk, Inc. www.autodesk.com&lt;/VendorDescription&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInArchitecture&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInFamily&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInStructure&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleWhenNoActiveDocument&lt;/VisibilityMode&gt;&nbsp; &lt;/AddIn&gt; &nbsp; &lt;AddIn Type=&quot;Command&quot;&gt; &nbsp; &nbsp; &lt;Text&gt;Convert MEP Placeholders&lt;/Text&gt; &nbsp; &nbsp; &lt;Description&gt;Convert MEP placeholder elements&lt;/Description&gt; &nbsp; &nbsp; &lt;Assembly&gt;C:\a\lib\revit\2012\adn\webcast\src\MepPlaceholders\MepPlaceholders\bin\Debug\MepPlaceholders.dll&lt;/Assembly&gt; &nbsp; &nbsp; &lt;FullClassName&gt;MepPlaceholders.ConvertPlaceholders&lt;/FullClassName&gt; &nbsp; &nbsp; &lt;ClientId&gt;2c834e62-3d55-4aae-95d9-5646a74dmaroon6&lt;/ClientId&gt; &nbsp; &nbsp; &lt;VendorId&gt;ADNP&lt;/VendorId&gt; &nbsp; &nbsp; &lt;VendorDescription&gt;Autodesk, Inc. www.autodesk.com&lt;/VendorDescription&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInArchitecture&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInFamily&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInStructure&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleWhenNoActiveDocument&lt;/VisibilityMode&gt; &nbsp; &lt;/AddIn&gt; &lt;/RevitAddIns&gt;
```
