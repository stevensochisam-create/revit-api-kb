---
num: 399
date: 2010-06-24
themes: [Geometry]
tags: [revit-api, tbc]
---

# Intersection Between Elements

<https://jeremytammik.github.io/tbc/a/0399_find_element_intersection.htm>

```csharp
&nbsp; private XYZ GetIntersection( &nbsp; &nbsp; Line line1, &nbsp; &nbsp; Line line2 ) &nbsp; { &nbsp; &nbsp; IntersectionResultArray results; &nbsp; &nbsp; &nbsp; SetComparisonResult result &nbsp; &nbsp; &nbsp; = line1.Intersect( line2, out results ); &nbsp; &nbsp; &nbsp; if( result != SetComparisonResult.Overlap ) &nbsp; &nbsp; &nbsp; throw new InvalidOperationException( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Input lines did not intersect.&quot; ); &nbsp; &nbsp; &nbsp; if( results == null || results.Size != 1 ) &nbsp; &nbsp; &nbsp; throw new InvalidOperationException( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Could not extract line intersection point.&quot; ); &nbsp; &nbsp; &nbsp; IntersectionResult iResult &nbsp; &nbsp; &nbsp; = results.get_Item( 0 ); &nbsp; &nbsp; &nbsp; return iResult.XYZPoint; &nbsp; }
```
