---
num: 1754
date: 2019-05-23
themes: [Geometry]
tags: [revit-api, tbc]
---

# Retrieving Section View Intersection Cut Geometry

<https://jeremytammik.github.io/tbc/a/1754_section_intersect_geo.html>

```csharp
Options&nbsp;option&nbsp;=&nbsp;new&nbsp;Options(); option.View&nbsp;=&nbsp;viewSection; GeometryElement&nbsp;geometryElement&nbsp;=&nbsp;familyInstance &nbsp;&nbsp;.get_Geometry(&nbsp;option&nbsp;); GeometryInstance?&nbsp;gInst&nbsp;=&nbsp;geometryElement.First()&nbsp; &nbsp;&nbsp;as&nbsp;GeometryInstance; GeometryElement&nbsp;gSymbol&nbsp;=&nbsp;gInst.GetInstanceGeometry();
```

```csharp
viewSection.get_Parameter(&nbsp; &nbsp;&nbsp;BuiltInParameter.VIEWER_BOUND_FAR_CLIPPING&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.Set(&nbsp;1&nbsp;); viewSection.DetailLevel&nbsp;=&nbsp;ViewDetailLevel.Fine;
```

```csharp
3 Element 2 FamilyInstance 7 GeometryElement 2 GeometryInstance 261 Line 2 null 9 Solid 2 Wall
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Predicate&nbsp;returning&nbsp;true&nbsp;if&nbsp;the&nbsp;given&nbsp;line ///&nbsp;lies&nbsp;in&nbsp;the&nbsp;given&nbsp;plane ///&nbsp;&lt;/summary&gt; static&nbsp;bool&nbsp;IsLineInPlane( &nbsp;&nbsp;Line&nbsp;line, &nbsp;&nbsp;Plane&nbsp;plane&nbsp;) { &nbsp;&nbsp;XYZ&nbsp;p0&nbsp;=&nbsp;line.GetEndPoint(&nbsp;0&nbsp;); &nbsp;&nbsp;XYZ&nbsp;p1&nbsp;=&nbsp;line.GetEndPoint(&nbsp;1&nbsp;); &nbsp;&nbsp;UV&nbsp;uv0,&nbsp;uv1; &nbsp;&nbsp;double&nbsp;d0,&nbsp;d1; &nbsp;&nbsp;plane.Project(&nbsp;p0,&nbsp;out&nbsp;uv0,&nbsp;out&nbsp;d0&nbsp;); &nbsp;&nbsp;plane.Project(&nbsp;p1,&nbsp;out&nbsp;uv1,&nbsp;out&nbsp;d1&nbsp;); &nbsp;&nbsp;return&nbsp;_eps&nbsp;&gt;&nbsp;Math.Abs(&nbsp;d0&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&amp;&amp;&nbsp;_eps&nbsp;&gt;&nbsp;Math.Abs(&nbsp;d1&nbsp;); }
```

```csharp
Object analysed: 3 Element 2 FamilyInstance 7 GeometryElement 2 GeometryInstance 261 Line 2 null 9 Solid 2 Wall 77 cut geometry lines found in section plane.
```
