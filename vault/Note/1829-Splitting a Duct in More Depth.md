---
num: 1829
date: 2020-03-17
themes: [MEP]
tags: [revit-api, tbc]
---

# Splitting a Duct in More Depth

<https://jeremytammik.github.io/tbc/a/1829_split_duct.html>

```csharp
&lt;Transaction(TransactionMode.Manual)&gt; &lt;Regeneration(RegenerationOption.Manual)&gt; &lt;Journaling(JournalingMode.UsingCommandData)&gt; Public&nbsp;Class&nbsp;TransactionCommand &nbsp;&nbsp;Implements&nbsp;UI.IExternalCommand &nbsp;&nbsp;Public&nbsp;Function&nbsp;Execute( &nbsp;&nbsp;&nbsp;&nbsp;ByVal&nbsp;commandData&nbsp;As&nbsp;UI.ExternalCommandData, &nbsp;&nbsp;&nbsp;&nbsp;ByRef&nbsp;message&nbsp;As&nbsp;String,&nbsp;ByVal&nbsp;elements&nbsp;As&nbsp;DB.ElementSet)&nbsp;_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;UI.Result&nbsp;Implements&nbsp;UI.IExternalCommand.Execute &nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;app&nbsp;As&nbsp;ApplicationServices.Application&nbsp;=&nbsp;commandData.Application.Application &nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;doc&nbsp;As&nbsp;DB.Document&nbsp;=&nbsp;commandData.Application.ActiveUIDocument.Document &nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;docUi&nbsp;As&nbsp;UI.UIDocument&nbsp;=&nbsp;commandData.Application.ActiveUIDocument &nbsp;&nbsp;&nbsp;&nbsp;Execute&nbsp;=&nbsp;UI.Result.Failed &nbsp;&nbsp;&nbsp;&nbsp;Using&nbsp;transaction&nbsp;As&nbsp;New&nbsp;DB.Transaction(doc,&nbsp;&quot;Break&nbsp;Duct&quot;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transaction.Start() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;duct&nbsp;As&nbsp;DB.Mechanical.Duct&nbsp;=&nbsp;TryCast(doc.GetElement( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New&nbsp;DB.ElementId(1789723)),&nbsp;DB.Mechanical.Duct) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;curve&nbsp;As&nbsp;DB.Curve&nbsp;=&nbsp;TryCast(duct.Location,&nbsp;DB.LocationCurve).Curve &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;pt0&nbsp;As&nbsp;DB.XYZ&nbsp;=&nbsp;curve.GetEndPoint(0) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;pt1&nbsp;As&nbsp;DB.XYZ&nbsp;=&nbsp;curve.GetEndPoint(1) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;vector&nbsp;As&nbsp;DB.XYZ&nbsp;=&nbsp;pt1.Subtract(pt0).Normalize &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;breakPt&nbsp;As&nbsp;DB.XYZ&nbsp;=&nbsp;pt0.Add(vector.Multiply(2.0)) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dim&nbsp;newDuctId&nbsp;As&nbsp;DB.ElementId&nbsp;=&nbsp;DB.Mechanical.MechanicalUtils.BreakCurve( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;doc,&nbsp;duct.Id,&nbsp;breakPt) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transaction.Commit() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#39;&nbsp;change&nbsp;our&nbsp;result&nbsp;to&nbsp;successful &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&
```

```csharp
Dim&nbsp;famInstance&nbsp;As&nbsp;DB.FamilyInstance&nbsp;_ =&nbsp;doc.Create.NewFamilyInstance( &nbsp;&nbsp;breakPt,&nbsp;FamilySymbol,&nbsp;vector,&nbsp;null, &nbsp;&nbsp;DB.Structure.StructuralType.NonStructural)
```
