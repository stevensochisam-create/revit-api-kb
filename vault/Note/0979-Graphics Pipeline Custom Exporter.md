---
num: 979
date: 2013-07-08
themes: [MEP]
tags: [revit-api, tbc]
---

# Graphics Pipeline Custom Exporter

<https://jeremytammik.github.io/tbc/a/0979_custom_exporter.htm>

```csharp
&nbsp; // Instantiate custom context &nbsp; &nbsp; MyExportContext context = new MyExportContext( &nbsp; &nbsp; document ); &nbsp; &nbsp; // Instantiate custom exporter &nbsp; &nbsp; CustomExporter exporter = new CustomExporter( &nbsp; &nbsp; document, context ); &nbsp; &nbsp; // Specify exporter settings &nbsp; &nbsp; exporter.IncludeFaces = false; &nbsp; &nbsp; exporter.ShouldStopOnError = false; &nbsp; &nbsp; // Launch export process &nbsp; &nbsp; exporter.Export( view3D );
```

```csharp
&nbsp; MyExportContext context = new MyExportContext( &nbsp; &nbsp; document ); &nbsp; &nbsp; // Create an instance of a custom exporter by &nbsp; // giving it a document and the context. &nbsp; &nbsp; CustomExporter exporter = new CustomExporter( &nbsp; &nbsp; document, context ); &nbsp; &nbsp; // Note: Excluding faces just excludes the calls, &nbsp; // not the actual processing of face tessellation. &nbsp; // Meshes of the faces will still be received by &nbsp; // the context. &nbsp; &nbsp; exporter.IncludeFaces = false; &nbsp; &nbsp; exporter.ShouldStopOnError = false; &nbsp; &nbsp; exporter.Export( view3D );
```
