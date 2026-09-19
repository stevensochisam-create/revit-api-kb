---
num: 1597
date: 2017-10-25
themes: [Geometry]
tags: [revit-api, tbc]
---

# Curtain Wall Panel Geometry with Basic Wall Panel

<https://jeremytammik.github.io/tbc/a/1597_curtain_wall_panel.html>

```csharp
&nbsp;&nbsp;//&nbsp;First,&nbsp;find&nbsp;solid&nbsp;geometry&nbsp;from&nbsp;panel&nbsp;ids. &nbsp;&nbsp;//&nbsp;Note&nbsp;that&nbsp;the&nbsp;panel&nbsp;which&nbsp;contains&nbsp;a&nbsp;basic &nbsp;&nbsp;//&nbsp;wall&nbsp;has&nbsp;NO&nbsp;geometry! &nbsp;&nbsp;Wall&nbsp;wall&nbsp;=&nbsp;doc.GetElement(&nbsp;curtainWallId&nbsp;)&nbsp;as&nbsp;Wall; &nbsp;&nbsp;var&nbsp;grid&nbsp;=&nbsp;wall.CurtainGrid; &nbsp;&nbsp;foreach(&nbsp;ElementId&nbsp;id&nbsp;in&nbsp;grid.GetPanelIds()&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;Element&nbsp;e&nbsp;=&nbsp;doc.GetElement(&nbsp;id&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;solids.AddRange(&nbsp;GetElementSolids(&nbsp;e&nbsp;)&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;//&nbsp;Secondly,&nbsp;find&nbsp;corresponding&nbsp;panel&nbsp;wall &nbsp;&nbsp;//&nbsp;for&nbsp;the&nbsp;curtain&nbsp;wall&nbsp;and&nbsp;retrieve&nbsp;the&nbsp;actual &nbsp;&nbsp;//&nbsp;geometry&nbsp;from&nbsp;that. &nbsp;&nbsp;FilteredElementCollector&nbsp;cwPanels &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfCategory(&nbsp;BuiltInCategory.OST_CurtainWallPanels&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;Wall&nbsp;)&nbsp;); &nbsp;&nbsp;foreach(&nbsp;Wall&nbsp;cwp&nbsp;in&nbsp;cwPanels&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Find&nbsp;panel&nbsp;wall&nbsp;belonging&nbsp;to&nbsp;this&nbsp;curtain&nbsp;wall &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;and&nbsp;retrieve&nbsp;its&nbsp;geometry &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;cwp.StackedWallOwnerId&nbsp;==&nbsp;curtainWallId&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;solids.AddRange(&nbsp;GetElementSolids(&nbsp;cwp&nbsp;)&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;}
```
