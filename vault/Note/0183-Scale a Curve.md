---
num: 183
date: 2009-07-22
themes: [Geometry]
tags: [revit-api, tbc]
---

# Scale a Curve

<https://jeremytammik.github.io/tbc/a/0183_scale_curve.htm>

```csharp
public void ScaleCurves() { &nbsp; CurveArray cArray = PrepareCurveArray(); &nbsp; &nbsp; Transform x = Transform.Identity; &nbsp; x = x.ScaleBasis( 1.0 / 12.0 ); &nbsp; &nbsp; int numCurves = cArray.Size; &nbsp; for( int i = 0; i &lt; numCurves; ++i ) &nbsp; { &nbsp; &nbsp; Curve curve = cArray.get_Item( i ); &nbsp; &nbsp; &nbsp; Curve newCurve = curve.get_Transformed( x ); &nbsp; &nbsp; &nbsp; cArray.set_Item( i, newCurve ); &nbsp; } &nbsp; &nbsp; WriteProfile( &quot;After transformation&quot;, cArray ); }
```
