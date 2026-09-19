---
num: 219
date: 2009-09-14
themes: [MEP]
tags: [revit-api, tbc]
---

# The Revit MEP API

<https://jeremytammik.github.io/tbc/a/0219_mep_api.htm>

```csharp
Document.Export( string folder, string name, GBXMLExportOptions );
```

```csharp
ElectricalSystem sys; ConnectorSet connectors = sys.ConnectorManager.Connectors;
```
