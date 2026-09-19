---
num: 1832
date: 2020-03-30
themes: [Geometry]
tags: [revit-api, tbc]
---

# Satellite Images and Instance Transforms

<https://jeremytammik.github.io/tbc/a/1832_xform_inst_sat_img.html>

```csharp
&nbsp;&nbsp;Reference&nbsp;faceRef&nbsp;=&nbsp;sel.PickObject(&nbsp;ObjectType.Face&nbsp;); &nbsp;&nbsp;GeometryObject&nbsp;geoObj&nbsp;=&nbsp;doc.GetElement(&nbsp;faceRef&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.GetGeometryObjectFromReference(&nbsp;faceRef&nbsp;); &nbsp;&nbsp;PlanarFace&nbsp;moduleFace&nbsp;=&nbsp;geoObj&nbsp;as&nbsp;PlanarFace; &nbsp;&nbsp;IList&lt;CurveLoop&gt;&nbsp;faceEdges&nbsp;=&nbsp;moduleFace.GetEdgesAsCurveLoops(); &nbsp;&nbsp;FilledRegion&nbsp;fillRegion&nbsp;=&nbsp;FilledRegion.Create(&nbsp;doc,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;stringFillType.Id,&nbsp;currentView.Id,&nbsp;faceEdges&nbsp;);
```

```csharp
&nbsp;&nbsp;Reference&nbsp;faceRef&nbsp;=&nbsp;sel.PickObject(&nbsp;ObjectType.Face&nbsp;); &nbsp;&nbsp;GeometryObject&nbsp;geoObj&nbsp;=&nbsp;doc.GetElement(&nbsp;faceRef&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.GetGeometryObjectFromReference(&nbsp;faceRef&nbsp;); &nbsp;&nbsp;Instance&nbsp;moduleInstance&nbsp;=&nbsp;doc.GetElement(&nbsp;faceRef&nbsp;)&nbsp;as&nbsp;Instance; &nbsp;&nbsp;Transform&nbsp;moduleTransform&nbsp;=&nbsp;moduleInstance.GetTotalTransform(); &nbsp;&nbsp;PlanarFace&nbsp;moduleFace&nbsp;=&nbsp;geoObj&nbsp;as&nbsp;PlanarFace; &nbsp;&nbsp;IList&lt;CurveLoop&gt;&nbsp;faceEdges&nbsp;=&nbsp;moduleFace.GetEdgesAsCurveLoops(); &nbsp;&nbsp;foreach(&nbsp;CurveLoop&nbsp;loop&nbsp;in&nbsp;faceEdges&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;loop.Transform(&nbsp;moduleTransform&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;FilledRegion&nbsp;fillRegion&nbsp;=&nbsp;FilledRegion.Create(&nbsp;doc,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;stringFillType.Id,&nbsp;currentView.Id,&nbsp;faceEdges&nbsp;);
```
