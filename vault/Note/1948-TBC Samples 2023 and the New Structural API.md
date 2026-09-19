---
num: 1948
date: 2022-04-26
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# TBC Samples 2023 and the New Structural API

<https://jeremytammik.github.io/tbc/a/1948_tbc_rst_2023.html>

```csharp
var am = wall.GetAnalyticalModel(); foreach (var ct in CurveTypes) { var curves = am.GetCurves(ct); var n = curves.Count; Debug.Print("{0} {1} curve{2}.", n, ct, Util.PluralSuffix(n)); foreach (var curve in curves) creator.CreateModelCurve( curve.CreateTransformed(T)); }
```

```csharp
&nbsp;&nbsp;private&nbsp;static&nbsp;ElementId&nbsp;GetAnalyticalElementId(dynElement&nbsp;element) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;_document&nbsp;=&nbsp;iDocument.Current.WrappedType; &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Gets&nbsp;the&nbsp;AnalyticalToPhysicalAssociationManager&nbsp;for&nbsp;this&nbsp;document &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;analyticalToPhysicalManager&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;AnalyticalToPhysicalAssociationManager &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.GetAnalyticalToPhysicalAssociationManager(_document); &nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(analyticalToPhysicalManager&nbsp;==&nbsp;null) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;throw&nbsp;new&nbsp;System.Exception(OrchidBase.InvalidType); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;ElementId&nbsp;_elementId&nbsp;=&nbsp;GetDynamic(element).Id; &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;analyticalToPhysicalManager.GetAssociatedElementId(_elementId); &nbsp;&nbsp;} &nbsp;&nbsp;public&nbsp;static&nbsp;dynElement&nbsp;GetAnalytical(dynElement&nbsp;element) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;GetAnalyticalElementId(element).ToDynamoType(); &nbsp;&nbsp;}
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Return&nbsp;the&nbsp;associated&nbsp;analytical&nbsp;element&nbsp;id&nbsp; ///&nbsp;for&nbsp;the&nbsp;given&nbsp;element ///&nbsp;&lt;/summary&gt; ElementId&nbsp;GetAnalyticalElementId(Element&nbsp;e) { &nbsp;&nbsp;Document&nbsp;doc&nbsp;=&nbsp;e.Document; &nbsp;&nbsp;AnalyticalToPhysicalAssociationManager&nbsp;m&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;AnalyticalToPhysicalAssociationManager &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.GetAnalyticalToPhysicalAssociationManager( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;doc); &nbsp;&nbsp;if&nbsp;(null&nbsp;==&nbsp;m) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;throw&nbsp;new&nbsp;System.ArgumentException( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;No&nbsp;AnalyticalToPhysicalAssociationManager&nbsp;found&quot;); &nbsp;&nbsp;} &nbsp;&nbsp;return&nbsp;m.GetAssociatedElementId(e.Id); }
```
