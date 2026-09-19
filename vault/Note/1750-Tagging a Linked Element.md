---
num: 1750
date: 2019-05-13
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# Tagging a Linked Element

<https://jeremytammik.github.io/tbc/a/1750_tag_linked_elem.html>

```csharp
&nbsp;&nbsp;RevitLinkInstance&nbsp;link&nbsp;=&nbsp;doc.GetElement( &nbsp;&nbsp;&nbsp;&nbsp;tag.TaggedElementId.LinkInstanceId&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as&nbsp;RevitLinkInstance; &nbsp;&nbsp;Reference&nbsp;refer&nbsp;=&nbsp;new&nbsp;Reference( &nbsp;&nbsp;&nbsp;&nbsp;link.GetLinkDocument() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.GetElement(&nbsp;tag.TaggedElementId.LinkedElementId&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.CreateLinkReference(&nbsp;link&nbsp;);
```

```csharp
&nbsp;&nbsp;FilteredElementCollector&nbsp;doors &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfCategory(&nbsp;BuiltInCategory.OST_Doors&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;FamilyInstance&nbsp;)&nbsp;); &nbsp;&nbsp;IEnumerable&lt;IndependentTag&gt;&nbsp;tags &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;IndependentTag&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;IndependentTag&gt;(); &nbsp;&nbsp;IList&lt;ElementId&gt;&nbsp;untagged_elements&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;List&lt;ElementId&gt;(); &nbsp;&nbsp;foreach(&nbsp;Element&nbsp;e&nbsp;in&nbsp;doors&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;!tags.Any(&nbsp;q&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&gt;&nbsp;q.TaggedLocalElementId&nbsp;==&nbsp;e.Id&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_elements.Add(&nbsp;e.Id&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;} &nbsp;&nbsp;uidoc.Selection.SetElementIds(&nbsp;untagged_elements&nbsp;); &nbsp;&nbsp;uidoc.RefreshActiveView();
```

```csharp
&nbsp;&nbsp;var&nbsp;collector&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;IndependentTag&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.OfCategory(&nbsp;BuiltInCategory.OST_DoorTags&nbsp;); &nbsp;&nbsp;var&nbsp;doorTagsIds &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;HashSet&lt;ElementId&gt;( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector.OfType&lt;IndependentTag&gt;() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Select(&nbsp;x&nbsp;=&gt;&nbsp;x.GetTaggedLocalElement()?.Id&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Where(&nbsp;x&nbsp;=&gt;&nbsp;x&nbsp;!=&nbsp;null&nbsp;)&nbsp;);
```
