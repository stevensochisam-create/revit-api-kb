---
num: 1748
date: 2019-05-07
themes: [Geometry]
tags: [revit-api, tbc]
---

# Spatial Geometry, Add-In Manager and Show Reels

<https://jeremytammik.github.io/tbc/a/1748_spatial_geo_2020.html>

```csharp
Room 7; Wall3(308817): net 28; opening 2; gross 30
```

```csharp
Room 7; Wall3(308817): net 30; opening 2; gross 32
```

```csharp
spatialData.dblNetArea&nbsp;=&nbsp;Util.sqFootToSquareM( &nbsp;&nbsp;spatialSubFace.GetSubface().Area&nbsp;-&nbsp;openingArea&nbsp;);&nbsp;
```

```csharp
&nbsp;&nbsp;///&nbsp;&lt;summary&gt; &nbsp;&nbsp;///&nbsp;Return&nbsp;wall&nbsp;openings&nbsp;using&nbsp;GetDependentElements &nbsp;&nbsp;///&nbsp;&lt;/summary&gt; &nbsp;&nbsp;static&nbsp;IList&lt;ElementId&gt;&nbsp;GetOpenings(&nbsp;Wall&nbsp;wall&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;ElementMulticategoryFilter&nbsp;emcf &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;ElementMulticategoryFilter( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;List&lt;ElementId&gt;()&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;ElementId(BuiltInCategory.OST_Windows), &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;ElementId(BuiltInCategory.OST_Doors)&nbsp;}&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;wall.GetDependentElements(&nbsp;emcf&nbsp;); &nbsp;&nbsp;}
```
