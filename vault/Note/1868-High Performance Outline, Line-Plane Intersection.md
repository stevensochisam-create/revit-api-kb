---
num: 1868
date: 2020-10-06
themes: [Geometry]
tags: [revit-api, tbc]
---

# High Performance Outline, Line-Plane Intersection

<https://jeremytammik.github.io/tbc/a/1868_outline_performance.html>

```csharp
&nbsp;&nbsp;double&nbsp;b&nbsp;=&nbsp;500000&nbsp;/&nbsp;304.8; &nbsp;&nbsp;XYZ&nbsp;min&nbsp;=&nbsp;new&nbsp;XYZ(&nbsp;-b,&nbsp;-b,&nbsp;-b&nbsp;); &nbsp;&nbsp;XYZ&nbsp;max&nbsp;=&nbsp;new&nbsp;XYZ(&nbsp;b,&nbsp;b,&nbsp;b&nbsp;);
```

```csharp
&nbsp;&nbsp;double&nbsp;precision&nbsp;=&nbsp;10e-6&nbsp;/&nbsp;304.8; &nbsp;&nbsp;var&nbsp;bb&nbsp;=&nbsp;new&nbsp;BinaryUpperLowerBoundsSearch(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;doc,&nbsp;precision&nbsp;); &nbsp;&nbsp;XYZ[]&nbsp;rx&nbsp;=&nbsp;bb.GetBoundaries(&nbsp;min,&nbsp;max,&nbsp;elems,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;BinaryUpperLowerBoundsSearch.Direction.X&nbsp;); &nbsp;&nbsp;rx&nbsp;=&nbsp;bb.GetBoundaries(&nbsp;rx[&nbsp;0&nbsp;],&nbsp;rx[&nbsp;1&nbsp;],&nbsp;elems,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;BinaryUpperLowerBoundsSearch.Direction.Y&nbsp;); &nbsp;&nbsp;rx&nbsp;=&nbsp;bb.GetBoundaries(&nbsp;rx[&nbsp;0&nbsp;],&nbsp;rx[&nbsp;1&nbsp;],&nbsp;elems,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;BinaryUpperLowerBoundsSearch.Direction.Z&nbsp;);
```

```csharp
public&nbsp;static&nbsp;class&nbsp;PointExt { &nbsp;&nbsp;public&nbsp;static&nbsp;double&nbsp;Projection( &nbsp;&nbsp;&nbsp;&nbsp;this&nbsp;XYZ&nbsp;vector,&nbsp;XYZ&nbsp;other&nbsp;)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&gt;&nbsp;vector.DotProduct(&nbsp;other&nbsp;)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;other.GetLength(); }
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Return&nbsp;the&nbsp;3D&nbsp;intersection&nbsp;point&nbsp;between ///&nbsp;a&nbsp;line&nbsp;and&nbsp;a&nbsp;plane. ///&nbsp;https://forums.autodesk.com/t5/revit-api-forum/how-can-we-calculate-the-intersection-between-the-plane-and-the/m-p/9785834 ///&nbsp;https://stackoverflow.com/questions/5666222/3d-line-plane-intersection ///&nbsp;Determine&nbsp;the&nbsp;point&nbsp;of&nbsp;intersection&nbsp;between&nbsp; ///&nbsp;a&nbsp;plane&nbsp;defined&nbsp;by&nbsp;a&nbsp;point&nbsp;and&nbsp;a&nbsp;normal&nbsp;vector&nbsp; ///&nbsp;and&nbsp;a&nbsp;line&nbsp;defined&nbsp;by&nbsp;a&nbsp;point&nbsp;and&nbsp;a&nbsp;direction&nbsp;vector. ///&nbsp;planePoint&nbsp;-&nbsp;A&nbsp;point&nbsp;on&nbsp;the&nbsp;plane. ///&nbsp;planeNormal&nbsp;-&nbsp;The&nbsp;normal&nbsp;vector&nbsp;of&nbsp;the&nbsp;plane. ///&nbsp;linePoint&nbsp;-&nbsp;A&nbsp;point&nbsp;on&nbsp;the&nbsp;line. ///&nbsp;lineDirection&nbsp;-&nbsp;The&nbsp;direction&nbsp;vector&nbsp;of&nbsp;the&nbsp;line. ///&nbsp;lineParameter&nbsp;-&nbsp;The&nbsp;intersection&nbsp;distance&nbsp;along&nbsp;the&nbsp;line. ///&nbsp;Return&nbsp;-&nbsp;The&nbsp;point&nbsp;of&nbsp;intersection&nbsp;between&nbsp;the&nbsp; ///&nbsp;line&nbsp;and&nbsp;the&nbsp;plane,&nbsp;null&nbsp;if&nbsp;the&nbsp;line&nbsp;is&nbsp;parallel&nbsp; ///&nbsp;to&nbsp;the&nbsp;plane. ///&nbsp;&lt;/summary&gt; public&nbsp;static&nbsp;XYZ&nbsp;LinePlaneIntersection( &nbsp;&nbsp;Line&nbsp;line, &nbsp;&nbsp;Plane&nbsp;plane, &nbsp;&nbsp;out&nbsp;double&nbsp;lineParameter&nbsp;) { &nbsp;&nbsp;XYZ&nbsp;planePoint&nbsp;=&nbsp;plane.Origin; &nbsp;&nbsp;XYZ&nbsp;planeNormal&nbsp;=&nbsp;plane.Normal; &nbsp;&nbsp;XYZ&nbsp;linePoint&nbsp;=&nbsp;line.GetEndPoint(&nbsp;0&nbsp;); &nbsp;&nbsp;XYZ&nbsp;lineDirection&nbsp;=&nbsp;(line.GetEndPoint(&nbsp;1&nbsp;)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;linePoint).Normalize(); &nbsp;&nbsp;//&nbsp;Is&nbsp;the&nbsp;line&nbsp;parallel&nbsp;to&nbsp;the&nbsp;plane,&nbsp;i.e., &nbsp;&nbsp;//&nbsp;perpendicular&nbsp;to&nbsp;the&nbsp;plane&nbsp;normal? &nbsp;&nbsp;if(&nbsp;IsZero(&nbsp;planeNormal.DotProduct(&nbsp;lineDirection&nbsp;)&nbsp;)&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;lineParameter&nbsp;=&nbsp;double.NaN; &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;null; &nbsp;&nbsp;} &nbsp;&nbsp;lineParameter&nbsp;=&nbsp;(planeNormal.DotProduct(&nbsp;planePoint&nbsp;)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;planeNorma
```
