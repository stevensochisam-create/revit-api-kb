---
num: 1809
date: 2020-01-08
themes: [Geometry]
tags: [revit-api, tbc]
---

# Extrusion Analyser and 2D Boolean Element Outline

<https://jeremytammik.github.io/tbc/a/1809_element_outline.html>

```csharp
{"name":"pt2+20+7", "id":"576786", "uid":"bc43ed2e-7e23-4f0e-9588-ab3c43f3d388-0008cd12", "svg_path":"M-56862 -9150 L-56572 -9150 -56572 -14186 -56862 -14186Z"} {"name":"pt70/210", "id":"576925", "uid":"bc43ed2e-7e23-4f0e-9588-ab3c43f3d388-0008cd9d", "svg_path":"M-55672 -11390 L-55672 -11290 -55656 -11290 -55656 -11278 -55087 -11278 -55087 -11270 -55076 -11270 -55076 -11242 -55182 -11242 -55182 -11214 -55048 -11214 -55048 -11270 -55037 -11270 -55037 -11278 -54988 -11278 -54988 -11290 -54972 -11290 -54972 -11390Z"} {"name":"pt80/115", "id":"576949", "uid":"bc43ed2e-7e23-4f0e-9588-ab3c43f3d388-0008cdb5", "svg_path":"M-56572 -10580 L-56572 -9430 -55772 -9430 -55772 -10580Z"} {"name":"מנוע מזגן מפוצל", "id":"576972", "uid":"bc43ed2e-7e23-4f0e-9588-ab3c43f3d388-0008cdcc", "svg_path":"M-56753 -8031 L-56713 -8031 -56713 -8018 -56276 -8018 -56276 -8031 -56265 -8031 -56265 -8109 -56276 -8109 -56276 -8911 -56252 -8911 -56252 -8989 -56276 -8989 -56276 -9020 -56277 -9020 -56278 -9020 -56711 -9020 -56713 -9020 -56713 -8989 -56753 -8989 -56753 -8911 -56713 -8911 -56713 -8109 -56753 -8109Z"}
```

```csharp
Options opt = new Options { IncludeNonVisibleObjects = true, DetailLevel = ViewDetailLevel.Fine }; GeometryElement geomElem = element.get_Geometry(opt);
```
