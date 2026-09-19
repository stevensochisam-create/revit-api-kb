---
num: 1714
date: 2019-01-08
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# pyRevit Keynote Manager and Becker Forge Blog

<https://jeremytammik.github.io/tbc/a/1714_keynote_becker.html>

```csharp
&nbsp;&nbsp;var&nbsp;symbolId&nbsp;=&nbsp;document.GetDefaultFamilyTypeId(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;ElementId(&nbsp;BuiltInCategory.OST_Walls&nbsp;)&nbsp;);
```

```csharp
&nbsp;&nbsp;WallType&nbsp;wType&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;WallType&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;WallType&gt;().FirstOrDefault(&nbsp;q &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&gt;&nbsp;q.Name&nbsp;==&nbsp;&quot;Generic&nbsp;-&nbsp;6\&quot;&nbsp;Masonry&quot;&nbsp;);
```
