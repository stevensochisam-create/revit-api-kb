---
num: 1224
date: 2014-10-17
themes: [MEP]
tags: [revit-api, tbc]
---

# Brussels Hackathon, Pipe Wall Thickness and Voids

<https://jeremytammik.github.io/tbc/a/1224_pipe_wall_thickness.htm>

```csharp
&nbsp; const BuiltInParameter bipDiameterInner &nbsp; &nbsp; = BuiltInParameter.RBS_PIPE_INNER_DIAM_PARAM; &nbsp; &nbsp; const BuiltInParameter bipDiameterOuter &nbsp; &nbsp; = BuiltInParameter.RBS_PIPE_OUTER_DIAMETER; &nbsp; &nbsp; static double GetWallThickness( Pipe pipe ) &nbsp; { &nbsp; &nbsp; double dinner = pipe.get_Parameter( &nbsp; &nbsp; &nbsp; bipDiameterInner ).AsDouble(); &nbsp; &nbsp; &nbsp; double douter = pipe.get_Parameter( &nbsp; &nbsp; &nbsp; bipDiameterOuter ).AsDouble(); &nbsp; &nbsp; &nbsp; return 0.5 * ( douter - dinner ); &nbsp; }
```
