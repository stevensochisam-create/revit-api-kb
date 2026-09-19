---
num: 1935
date: 2022-01-19
themes: [Geometry]
tags: [revit-api, tbc]
---

# Detailed 2D Text and Other Element Geometry

<https://jeremytammik.github.io/tbc/a/1935_text_2d_geo.html>

```csharp
Public Sub OnText(node As TextNode) Implements IExportContextBase.OnText If FilterEIDs IsNot Nothing Then If FilterEIDs.Contains(IntCurrentEID) = False Then Exit Sub End If End If OnText_Overridable(node) End Sub
```
