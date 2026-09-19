---
num: 1747
date: 2019-05-06
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# AI, Boundaries, Loops and RevitApiDocs 2020

<https://jeremytammik.github.io/tbc/a/1747_apidocs_2020.html>

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Expand&nbsp;the&nbsp;given&nbsp;bounding&nbsp;box&nbsp;to&nbsp;include&nbsp; ///&nbsp;and&nbsp;contain&nbsp;the&nbsp;given&nbsp;points. ///&nbsp;&lt;/summary&gt; public&nbsp;static&nbsp;void&nbsp;ExpandToContain( &nbsp;&nbsp;this&nbsp;BoundingBoxXYZ&nbsp;bb, &nbsp;&nbsp;IEnumerable&lt;XYZ&gt;&nbsp;pts&nbsp;) { &nbsp;&nbsp;bb.ExpandToContain(&nbsp;new&nbsp;XYZ( &nbsp;&nbsp;&nbsp;&nbsp;pts.Min&lt;XYZ,&nbsp;double&gt;(&nbsp;p&nbsp;=&gt;&nbsp;p.X&nbsp;), &nbsp;&nbsp;&nbsp;&nbsp;pts.Min&lt;XYZ,&nbsp;double&gt;(&nbsp;p&nbsp;=&gt;&nbsp;p.Y&nbsp;), &nbsp;&nbsp;&nbsp;&nbsp;pts.Min&lt;XYZ,&nbsp;double&gt;(&nbsp;p&nbsp;=&gt;&nbsp;p.Z&nbsp;)&nbsp;)&nbsp;); &nbsp;&nbsp;bb.ExpandToContain(&nbsp;new&nbsp;XYZ( &nbsp;&nbsp;&nbsp;&nbsp;pts.Max&lt;XYZ,&nbsp;double&gt;(&nbsp;p&nbsp;=&gt;&nbsp;p.X&nbsp;), &nbsp;&nbsp;&nbsp;&nbsp;pts.Max&lt;XYZ,&nbsp;double&gt;(&nbsp;p&nbsp;=&gt;&nbsp;p.Y&nbsp;), &nbsp;&nbsp;&nbsp;&nbsp;pts.Max&lt;XYZ,&nbsp;double&gt;(&nbsp;p&nbsp;=&gt;&nbsp;p.Z&nbsp;)&nbsp;)&nbsp;); } ///&nbsp;&lt;summary&gt; ///&nbsp;Return&nbsp;the&nbsp;bounding&nbsp;box&nbsp;of&nbsp;a&nbsp;curve&nbsp;loop. ///&nbsp;&lt;/summary&gt; public&nbsp;static&nbsp;BoundingBoxXYZ&nbsp;GetBoundingBox( &nbsp;&nbsp;CurveLoop&nbsp;curveLoop&nbsp;) { &nbsp;&nbsp;List&lt;XYZ&gt;&nbsp;pts&nbsp;=&nbsp;new&nbsp;List&lt;XYZ&gt;(); &nbsp;&nbsp;foreach(&nbsp;Curve&nbsp;c&nbsp;in&nbsp;curveLoop&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;pts.AddRange(&nbsp;c.Tessellate()&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;BoundingBoxXYZ&nbsp;bb&nbsp;=&nbsp;new&nbsp;BoundingBoxXYZ(); &nbsp;&nbsp;bb.Clear(); &nbsp;&nbsp;bb.ExpandToContain(&nbsp;pts&nbsp;); &nbsp;&nbsp;return&nbsp;bb; }
```
