---
num: 1792
date: 2019-10-24
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# DevCon Invitation and Dynamo for Infrastructure

<https://jeremytammik.github.io/tbc/a/1792_dynamo_infrastructure.html>

```csharp
Edge selEdge = RevitActions.Instance .GetInstanceEdgeFromSymbolRef(LeftSideEdge); Curve refcurve = selEdge.AsCurve().CreateReversed();
```
