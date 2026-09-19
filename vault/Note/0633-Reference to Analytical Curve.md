---
num: 633
date: 2011-08-18
themes: [Geometry]
tags: [revit-api, tbc]
---

# Reference to Analytical Curve

<https://jeremytammik.github.io/tbc/a/0633_analytical_reference.htm>

```csharp
&nbsp; AnalyticalModel analyticalModel = fiColumn &nbsp; &nbsp; .GetAnalyticalModel() as AnalyticalModel; &nbsp; &nbsp; Reference startReference = null; &nbsp; &nbsp; if( null != analyticalModel ) &nbsp; { &nbsp; &nbsp; Curve curveCol = analyticalModel.GetCurve(); &nbsp; &nbsp; if( null != curveCol ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; AnalyticalModelSelector amSelector &nbsp; &nbsp; &nbsp; &nbsp; = new AnalyticalModelSelector( curveCol ); &nbsp; &nbsp; &nbsp; &nbsp; amSelector.CurveSelector &nbsp; &nbsp; &nbsp; &nbsp; = AnalyticalCurveSelector.StartPoint; &nbsp; &nbsp; &nbsp; &nbsp; startReference = analyticalModel &nbsp; &nbsp; &nbsp; &nbsp; .GetReference( amSelector ); &nbsp; &nbsp; } &nbsp; }
```
