---
num: 1409
date: 2016-03-01
themes: [Geometry]
tags: [revit-api, tbc]
---

# API, SDK and View Section Box Element Intersection

<https://jeremytammik.github.io/tbc/a/1409_filter_section_view.html>

```csharp
&nbsp; if( startView.IsSectionBoxActive ) &nbsp; { &nbsp; &nbsp; Transform t = startView.GetSectionBox().Transform; &nbsp; &nbsp; &nbsp; Outline o = new Outline( &nbsp; &nbsp; &nbsp; t.OfPoint( startView.GetSectionBox().Min ), &nbsp; &nbsp; &nbsp; t.OfPoint( startView.GetSectionBox().Max ) ); &nbsp; &nbsp; &nbsp; intersectFilterStart &nbsp; &nbsp; &nbsp; = new BoundingBoxIntersectsFilter( o ); &nbsp; } &nbsp; if( targetView.IsSectionBoxActive ) &nbsp; { &nbsp; &nbsp; Transform t = targetView.GetSectionBox().Transform; &nbsp; &nbsp; &nbsp; Outline o = new Outline( &nbsp; &nbsp; &nbsp; t.OfPoint( targetView.GetSectionBox().Min ), &nbsp; &nbsp; &nbsp; t.OfPoint( targetView.GetSectionBox().Max ) ); &nbsp; &nbsp; &nbsp; intersectFilterTarget &nbsp; &nbsp; &nbsp; = new BoundingBoxIntersectsFilter( o ); &nbsp; }
```
