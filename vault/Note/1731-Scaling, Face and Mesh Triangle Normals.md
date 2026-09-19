---
num: 1731
date: 2019-03-20
themes: [Geometry]
tags: [revit-api, tbc]
---

# Scaling, Face and Mesh Triangle Normals

<https://jeremytammik.github.io/tbc/a/1731_scaling.html>

```csharp
&nbsp;&nbsp;Face&nbsp;f; &nbsp;&nbsp;XYZ&nbsp;MeshPt;&nbsp;//&nbsp;x1,&nbsp;x2&nbsp;or&nbsp;x3 &nbsp;&nbsp;XYZ&nbsp;NormalFromPoints;&nbsp;//&nbsp;(x3-x1).CrossProduct(x2-x1) &nbsp;&nbsp;UV&nbsp;UVpt&nbsp;=&nbsp;f.Project(&nbsp;MeshPt&nbsp;).UVPoint; &nbsp;&nbsp;XYZ&nbsp;face_normal&nbsp;=&nbsp;f.ComputeNormal(&nbsp;UVpt&nbsp;); &nbsp;&nbsp;XYZ&nbsp;surface_normal&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;f.OrientationMatchesSurfaceOrientation&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?&nbsp;face_normal&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;face_normal.Negate(); &nbsp;&nbsp;XYZ&nbsp;MeshNormal&nbsp;=&nbsp;surface_normal &nbsp;&nbsp;&nbsp;&nbsp;.DotProduct(&nbsp;NormalFromPoints&nbsp;)&nbsp;&gt;&nbsp;0&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?&nbsp;NormalFromPoints&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;NormalFromPoints.Negate();
```

```csharp
&nbsp;&nbsp;var&nbsp;tri&nbsp;=&nbsp;mesh.get_Triangle(&nbsp;I&nbsp;); &nbsp;&nbsp;XYZ&nbsp;pt0&nbsp;=&nbsp;tri.get_Vertex(&nbsp;0&nbsp;); &nbsp;&nbsp;XYZ&nbsp;pt1&nbsp;=&nbsp;tri.get_Vertex(&nbsp;1&nbsp;); &nbsp;&nbsp;XYZ&nbsp;pt2&nbsp;=&nbsp;tri.get_Vertex(&nbsp;2&nbsp;); &nbsp;&nbsp;XYZ&nbsp;vec1&nbsp;=&nbsp;pt1&nbsp;-&nbsp;pt0; &nbsp;&nbsp;XYZ&nbsp;vec2&nbsp;=&nbsp;pt2&nbsp;-&nbsp;pt0; &nbsp;&nbsp;XYZ&nbsp;normal&nbsp;=&nbsp;vec1.CrossProduct(&nbsp;vec2&nbsp;);
```
