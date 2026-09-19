---
num: 1904
date: 2021-05-04
themes: [Geometry]
tags: [revit-api, tbc]
---

# Roadmap Today and Sorting Non-Planar Curve Loops

<https://jeremytammik.github.io/tbc/a/1904_sort_loops.html>

```csharp
&nbsp;&nbsp;var&nbsp;loops&nbsp;=&nbsp;face.GetEdgesAsCurveLoops(); &nbsp;&nbsp;var&nbsp;sortedLoops&nbsp;=&nbsp;ExporterIFCUtils.SortCurveLoops(&nbsp;loops&nbsp;); &nbsp;&nbsp;for(&nbsp;var&nbsp;i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;sortedLoops.Count;&nbsp;i++&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;for(&nbsp;var&nbsp;j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;sortedLoops[&nbsp;i&nbsp;].Count;&nbsp;j++&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CreateTextNote(&nbsp;$&quot;[{i}][{j}]&quot;,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sortedLoops[&nbsp;i&nbsp;][&nbsp;j&nbsp;].First().Evaluate(&nbsp;0.33,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;true&nbsp;),&nbsp;doc&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;} &nbsp;&nbsp;TextNote&nbsp;CreateTextNote(&nbsp;string&nbsp;text,&nbsp;XYZ&nbsp;origin,&nbsp;Document&nbsp;doc&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;options&nbsp;=&nbsp;new&nbsp;TextNoteOptions &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HorizontalAlignment&nbsp;=&nbsp;HorizontalTextAlignment.Center, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VerticalAlignment&nbsp;=&nbsp;VerticalTextAlignment.Middle, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TypeId&nbsp;=&nbsp;doc.GetDefaultElementTypeId(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ElementTypeGroup.TextNoteType&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;}; &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;TextNote.Create(&nbsp;doc,&nbsp;doc.ActiveView.Id,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;origin,&nbsp;text,&nbsp;options&nbsp;); &nbsp;&nbsp;}
```
