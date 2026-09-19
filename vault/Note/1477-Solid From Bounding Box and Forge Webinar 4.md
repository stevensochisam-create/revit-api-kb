---
num: 1477
date: 2016-09-30
themes: [Geometry]
tags: [revit-api, tbc]
---

# Solid From Bounding Box and Forge Webinar 4

<https://jeremytammik.github.io/tbc/a/1477_solid_bbox_forge.html>

```csharp
&nbsp;&lt;summary&gt; ///&nbsp;Create&nbsp;and&nbsp;return&nbsp;a&nbsp;solid&nbsp;representing&nbsp; ///&nbsp;the&nbsp;bounding&nbsp;box&nbsp;of&nbsp;the&nbsp;input&nbsp;solid. ///&nbsp;Assumption:&nbsp;aligned&nbsp;with&nbsp;Z&nbsp;axis. ///&nbsp;Written,&nbsp;described&nbsp;and&nbsp;tested&nbsp;by&nbsp;Owen&nbsp;Merrick&nbsp;for&nbsp; ///&nbsp;http://forums.autodesk.com/t5/revit-api-forum/create-solid-from-boundingbox/m-p/6592486 ///&nbsp;&lt;/summary&gt; public&nbsp;static&nbsp;Solid&nbsp;CreateSolidFromBoundingBox(&nbsp; &nbsp;&nbsp;Solid&nbsp;inputSolid&nbsp;) { &nbsp;&nbsp;BoundingBoxXYZ&nbsp;bbox&nbsp;=&nbsp;inputSolid.GetBoundingBox(); &nbsp;&nbsp;//&nbsp;Corners&nbsp;in&nbsp;BBox&nbsp;coords &nbsp;&nbsp;XYZ&nbsp;pt0&nbsp;=&nbsp;new&nbsp;XYZ(&nbsp;bbox.Min.X,&nbsp;bbox.Min.Y,&nbsp;bbox.Min.Z&nbsp;); &nbsp;&nbsp;XYZ&nbsp;pt1&nbsp;=&nbsp;new&nbsp;XYZ(&nbsp;bbox.Max.X,&nbsp;bbox.Min.Y,&nbsp;bbox.Min.Z&nbsp;); &nbsp;&nbsp;XYZ&nbsp;pt2&nbsp;=&nbsp;new&nbsp;XYZ(&nbsp;bbox.Max.X,&nbsp;bbox.Max.Y,&nbsp;bbox.Min.Z&nbsp;); &nbsp;&nbsp;XYZ&nbsp;pt3&nbsp;=&nbsp;new&nbsp;XYZ(&nbsp;bbox.Min.X,&nbsp;bbox.Max.Y,&nbsp;bbox.Min.Z&nbsp;); &nbsp;&nbsp;//&nbsp;Edges&nbsp;in&nbsp;BBox&nbsp;coords &nbsp;&nbsp;Line&nbsp;edge0&nbsp;=&nbsp;Line.CreateBound(&nbsp;pt0,&nbsp;pt1&nbsp;); &nbsp;&nbsp;Line&nbsp;edge1&nbsp;=&nbsp;Line.CreateBound(&nbsp;pt1,&nbsp;pt2&nbsp;); &nbsp;&nbsp;Line&nbsp;edge2&nbsp;=&nbsp;Line.CreateBound(&nbsp;pt2,&nbsp;pt3&nbsp;); &nbsp;&nbsp;Line&nbsp;edge3&nbsp;=&nbsp;Line.CreateBound(&nbsp;pt3,&nbsp;pt0&nbsp;); &nbsp;&nbsp; &nbsp;&nbsp;//&nbsp;Create&nbsp;loop,&nbsp;still&nbsp;in&nbsp;BBox&nbsp;coords &nbsp;&nbsp;List&lt;Curve&gt;&nbsp;edges&nbsp;=&nbsp;new&nbsp;List&lt;Curve&gt;(); &nbsp;&nbsp;edges.Add(&nbsp;edge0&nbsp;); &nbsp;&nbsp;edges.Add(&nbsp;edge1&nbsp;); &nbsp;&nbsp;edges.Add(&nbsp;edge2&nbsp;); &nbsp;&nbsp;edges.Add(&nbsp;edge3&nbsp;); &nbsp;&nbsp;double&nbsp;height&nbsp;=&nbsp;bbox.Max.Z&nbsp;-&nbsp;bbox.Min.Z; &nbsp;&nbsp;CurveLoop&nbsp;baseLoop&nbsp;=&nbsp;CurveLoop.Create(&nbsp;edges&nbsp;); &nbsp;&nbsp;List&lt;CurveLoop&gt;&nbsp;loopList&nbsp;=&nbsp;new&nbsp;List&lt;CurveLoop&gt;(); &nbsp;&nbsp;loopList.Add(&nbsp;baseLoop&nbsp;); &nbsp;&nbsp;Solid&nbsp;preTransformBox&nbsp;=&nbsp;GeometryCreationUtilities &nbsp;&nbsp;&nbsp;&nbsp;.CreateExtrusionGeometry(&nbsp;loopList,&nbsp;XYZ.BasisZ,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;height&nb
```
