---
num: 1845
date: 2020-05-19
themes: [Geometry, LinkedModel]
tags: [revit-api, tbc]
---

# Using ReferenceIntersector with a Linked File

<https://jeremytammik.github.io/tbc/a/1845_raycast_linked.html>

```csharp
public&nbsp;string&nbsp;GetFaceRefRepresentation(&nbsp; &nbsp;&nbsp;Wall&nbsp;wall,&nbsp; &nbsp;&nbsp;Document&nbsp;doc,&nbsp; &nbsp;&nbsp;RevitLinkInstance&nbsp;instance&nbsp;) { &nbsp;&nbsp;Reference&nbsp;faceRef&nbsp;=&nbsp;HostObjectUtils.GetSideFaces(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;wall,&nbsp;ShellLayerType.Exterior&nbsp;).FirstOrDefault(); &nbsp;&nbsp;Reference&nbsp;stRef&nbsp;=&nbsp;faceRef.CreateLinkReference(&nbsp;instance&nbsp;); &nbsp;&nbsp;string&nbsp;stable&nbsp;=&nbsp;stRef.ConvertToStableRepresentation(&nbsp;doc&nbsp;); &nbsp;&nbsp;return&nbsp;stable; }
```
