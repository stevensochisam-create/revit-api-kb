---
num: 1831
date: 2020-03-26
themes: [MEP]
tags: [revit-api, tbc]
---

# Autorouting and Reference for CreatePipeConnector

<https://jeremytammik.github.io/tbc/a/1831_createpipeconnector.html>

```csharp
Autodesk.Revit.DB.Plane plane = Reference_plane.GetPlane(); ConnectorElement connector = ConnectorElement .CreatePipeConnector( family_document, PipeSystemType.Global, plane );
```

```csharp
ConnectorElement connector = ConnectorElement .CreatePipeConnector( family_document, PipeSystemType.Global, Reference_plane.GetReference() );
```

```csharp
var srep = $"{rebar51.UniqueId}:2000000:{1002000+typ}:LINEAR"; var refr = Reference.ParseFromStableRepresentation( rebar51.Document, srep );
```
