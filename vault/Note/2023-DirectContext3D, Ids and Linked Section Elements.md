---
num: 2023
date: 2024-01-19
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# DirectContext3D, Ids and Linked Section Elements

<https://jeremytammik.github.io/tbc/a/2023_id.html>

```csharp
Reference reference = Reference.ParseFromStableRepresentation( document, element.UniqueId);
```

```csharp
Reference refe = new Reference(itemconex) .CreateLinkReference(docsVinculados); IndependentTag tagConexao = IndependentTag.Create( Doc.Document, TagConexSelecionada.Id, Doc.ActiveView.Id, refe, true, TagOrientation.Horizontal, PosicaoFinal);
```

```csharp
IndependentTag tagConexao = IndependentTag.Create( Config.doc, Config.doc.ActiveView.Id, refe, true, TagMode.TM_ADDBY_CATEGORY, TagOrientation.Horizontal, PosicaoFinal); if (null != tagConexao.get_BoundingBox(Config.doc.ActiveView)) { // The element is in the view }
```
