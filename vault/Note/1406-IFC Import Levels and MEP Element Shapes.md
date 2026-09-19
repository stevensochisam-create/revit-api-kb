---
num: 1406
date: 2016-02-24
themes: [MEP]
tags: [revit-api, tbc]
---

# IFC Import Levels and MEP Element Shapes

<https://jeremytammik.github.io/tbc/a/1406_mep_element_shape_4.html>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Determine element shape from its &nbsp; /// element type's family name property. &nbsp; /// &lt;/summary&gt; &nbsp; static public string GetElementShape4( &nbsp; &nbsp; Element e ) &nbsp; { &nbsp; &nbsp; string shape = &quot;unknown&quot;; &nbsp; &nbsp; &nbsp; ElementId tid = e.GetTypeId(); &nbsp; &nbsp; &nbsp; if( ElementId.InvalidElementId != tid ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Document doc = e.Document; &nbsp; &nbsp; &nbsp; &nbsp; ElementType etyp = doc.GetElement( tid ) &nbsp; &nbsp; &nbsp; &nbsp; as ElementType; &nbsp; &nbsp; &nbsp; &nbsp; if( null != etyp ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; shape = etyp.FamilyName; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return shape; &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Return shape of first end connector on given duct. &nbsp; /// &lt;/summary&gt; &nbsp; public ConnectorProfileType GetShape( Duct duct ) &nbsp; { &nbsp; &nbsp; ConnectorProfileType ductShape &nbsp; &nbsp; &nbsp; = ConnectorProfileType.Invalid; &nbsp; &nbsp; &nbsp; foreach( Connector c &nbsp; &nbsp; &nbsp; in duct.ConnectorManager.Connectors ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( c.ConnectorType == ConnectorType.End ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; ductShape = c.Shape; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return ductShape; &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Return shape of all duct connectors. &nbsp; /// &lt;/summary&gt; &nbsp; static ConnectorProfileType[] GetProfileTypes( &nbsp; &nbsp; Duct duct ) &nbsp; { &nbsp; &nbsp; ConnectorSet connectors &nbsp; &nbsp; &nbsp; = duct.ConnectorManager.Connectors; &nbsp; &nbsp; &nbsp; int n = connectors.Size; &nbsp; &nbsp; &nbsp; ConnectorProfileType[] profileTypes &nbsp; &nbsp; &nbsp; = new ConnectorProfileType[n]; &nbsp; &nbsp; &nbsp; int i = 0; &nbsp; &nbsp; &nbsp; foreach( Connector c in connectors ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; profileTypes[i++] = c.Shape; &nbsp; &nbsp; } &nbsp; &nbsp; return profileTypes; &nbsp; }
```
