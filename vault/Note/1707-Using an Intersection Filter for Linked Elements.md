---
num: 1707
date: 2018-12-07
themes: [Geometry, LinkedModel]
tags: [revit-api, tbc]
---

# Using an Intersection Filter for Linked Elements

<https://jeremytammik.github.io/tbc/a/1707_filter_intersect.html>

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Collect&nbsp;the&nbsp;element&nbsp;ids&nbsp;of&nbsp;all&nbsp;elements&nbsp;in&nbsp;the&nbsp; ///&nbsp;linked&nbsp;documents&nbsp;intersecting&nbsp;the&nbsp;given&nbsp;element. ///&nbsp;&lt;/summary&gt; ///&nbsp;&lt;param&nbsp;name=&quot;e&quot;&gt;Target&nbsp;element&lt;/param&gt; ///&nbsp;&lt;param&nbsp;name=&quot;links&quot;&gt;Linked&nbsp;documents&lt;/param&gt; ///&nbsp;&lt;param&nbsp;name=&quot;ids&quot;&gt;Return&nbsp;intersecting&nbsp;element&nbsp;ids&lt;/param&gt; ///&nbsp;&lt;returns&gt;Number&nbsp;of&nbsp;intersecting&nbsp;elements&nbsp;found&lt;/returns&gt; int&nbsp;GetIntersectingLinkedElementIds(&nbsp; &nbsp;&nbsp;Element&nbsp;e, &nbsp;&nbsp;IList&lt;RevitLinkInstance&gt;&nbsp;links, &nbsp;&nbsp;List&lt;ElementId&gt;&nbsp;ids&nbsp;) { &nbsp;&nbsp;int&nbsp;count&nbsp;=&nbsp;ids.Count(); &nbsp;&nbsp;Solid&nbsp;solid&nbsp;=&nbsp;GetSolid(&nbsp;e&nbsp;); &nbsp;&nbsp;foreach(&nbsp;RevitLinkInstance&nbsp;i&nbsp;in&nbsp;links&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;GetTransform&nbsp;or&nbsp;GetTotalTransform&nbsp;or&nbsp;what? &nbsp;&nbsp;&nbsp;&nbsp;Transform&nbsp;transform&nbsp;=&nbsp;i.GetTransform();&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;!transform.AlmostEqual(&nbsp;Transform.Identity)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;solid&nbsp;=&nbsp;SolidUtils.CreateTransformed(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;solid,&nbsp;transform.Inverse&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;ElementIntersectsSolidFilter&nbsp;filter&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;ElementIntersectsSolidFilter(&nbsp;solid&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;FilteredElementCollector&nbsp;intersecting&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;i.GetLinkDocument()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.WherePasses(&nbsp;filter&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;ids.AddRange(&nbsp;intersecting.ToElementIds()&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;return&nbsp;ids.Count&nbsp;-&nbsp;count; }
```
