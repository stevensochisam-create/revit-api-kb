---
num: 1023
date: 2013-09-17
themes: [Geometry]
tags: [revit-api, tbc]
---

# How to Save a Solid to a File

<https://jeremytammik.github.io/tbc/a/1023_save_solid_to_file.htm>

```csharp
FreeFormElement/CS/FreeFormElementUtils.cs(66): Document familyDoc = app.NewFamilyDocument( familyTemplate);
```

```csharp
FreeFormElement/CS/FreeFormElementUtils.cs(113): RevitFreeFormElement element = Autodesk.Revit.DB .FreeFormElement.Create(familyDoc, block);
```

```csharp
GeometryAPI/SlaveSymbolGeometry/CS/SlaveSymbolGeometry.cs(82): View3D instanceView = View3D.CreateIsometric( RevitDoc, View3DId);
```

```csharp
ImportExport/CS/Export/ExportSATData.cs(164): exported = m_activeDoc.Export(m_exportFolder, m_exportFileName, viewIds, satExportOptions);
```
