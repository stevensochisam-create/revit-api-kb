---
num: 1623
date: 2018-02-02
themes: [MEP]
tags: [revit-api, tbc]
---

# Rotation Adjusts Conduit End

<https://jeremytammik.github.io/tbc/a/1623_rotate_adjust_conduit.html>

```csharp
using(&nbsp;Transaction&nbsp;trans&nbsp;=&nbsp;new&nbsp;Transaction(&nbsp;doc&nbsp;)&nbsp;) { &nbsp;&nbsp;trans.Start(&nbsp;&quot;虚假旋转线管&quot;&nbsp;); &nbsp;&nbsp;var&nbsp;ids&nbsp;=&nbsp;conduits.Select(&nbsp;c&nbsp;=&gt;&nbsp;c.Id&nbsp;).ToList(); &nbsp;&nbsp;var&nbsp;axis&nbsp;=&nbsp;Line.CreateBound(&nbsp;XYZ.Zero,&nbsp;XYZ.BasisX&nbsp;); &nbsp;&nbsp;ElementTransformUtils.RotateElements(&nbsp;doc,&nbsp;ids,&nbsp;axis,&nbsp;0&nbsp;); &nbsp;&nbsp;trans.Commit(); }
```
