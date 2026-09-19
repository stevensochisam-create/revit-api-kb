---
num: 1653
date: 2018-05-16
themes: [Geometry]
tags: [revit-api, tbc]
---

# Foreground Image Import and Visible DWG Geometry

<https://jeremytammik.github.io/tbc/a/1653_dwg_layer_visible.html>

```csharp
(curDoc.GetElement(curObj.GraphicsStyleId) as GraphicsStyle).Name;
```

```csharp
&nbsp;&nbsp;foreach(&nbsp;GeometryObject&nbsp;gObject&nbsp;in&nbsp;gElement&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;gInstance&nbsp;=&nbsp;(GeometryInstance)&nbsp;gObject; &nbsp;&nbsp;&nbsp;&nbsp;gElement2&nbsp;=&nbsp;gInstance.GetInstanceGeometry(); &nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;GeometryObject&nbsp;obj&nbsp;in&nbsp;gElement2&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;gStyle&nbsp;=&nbsp;curDoc.GetElement(&nbsp;obj.GraphicsStyleId&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as&nbsp;GraphicsStyle; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Try&nbsp;Catch&nbsp;because&nbsp;i&nbsp;was&nbsp;getting&nbsp;some&nbsp;Object &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Instance&nbsp;errors&nbsp;with&nbsp;the&nbsp;graphics&nbsp;style&nbsp;object. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;try &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Add&nbsp;object&nbsp;to&nbsp;list &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;!view.GetCategoryHidden(&nbsp;gStyle.GraphicsStyleCategory.Id&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list.Add(&nbsp;obj&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;catch&nbsp;{&nbsp;continue;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;}
```
