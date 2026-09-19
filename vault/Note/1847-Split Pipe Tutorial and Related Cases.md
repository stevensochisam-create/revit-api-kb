---
num: 1847
date: 2020-06-02
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# Split Pipe Tutorial and Related Cases

<https://jeremytammik.github.io/tbc/a/1847_split_pipe.html>

```csharp
using(&nbsp;Transaction&nbsp;tx&nbsp;=&nbsp;new&nbsp;Transaction(&nbsp;activeDoc.Document&nbsp;)&nbsp;) { &nbsp;&nbsp;tx.Start(&nbsp;&quot;split&nbsp;pipe&quot;&nbsp;); &nbsp;&nbsp;ElementId&nbsp;systemtype&nbsp;=&nbsp;system.GetTypeId(); &nbsp;&nbsp;SplitPipe(&nbsp;pipes[&nbsp;0&nbsp;],&nbsp;system,&nbsp;activeDoc,&nbsp;systemtype,&nbsp;pipeType&nbsp;); &nbsp;&nbsp;tx.Commit(); }
```

```csharp
&nbsp;&nbsp;ElementId&nbsp;levelId&nbsp;=&nbsp;segment.get_Parameter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;BuiltInParameter.RBS_START_LEVEL_PARAM&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp; .AsElementId(); &nbsp;&nbsp;//&nbsp;system.LevelId; &nbsp;&nbsp;ElementId&nbsp;systemtype&nbsp;=&nbsp;_system.GetTypeId(); &nbsp;&nbsp;//&nbsp;selecting&nbsp;one&nbsp;pipe&nbsp;and&nbsp;taking&nbsp;its&nbsp;location. &nbsp;&nbsp;Curve&nbsp;c1&nbsp;=&nbsp;(segment.Location&nbsp;as&nbsp;LocationCurve).Curve;&nbsp; &nbsp;&nbsp;//Pipe&nbsp;diameter &nbsp;&nbsp;double&nbsp;pipeDia&nbsp;=&nbsp;UnitUtils.ConvertFromInternalUnits(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;segment.get_Parameter(&nbsp;BuiltInParameter.RBS_PIPE_DIAMETER_PARAM&nbsp;).AsDouble(), &nbsp;&nbsp;&nbsp;&nbsp;DisplayUnitType.DUT_MILLIMETERS&nbsp;);
```

```csharp
//Standard&nbsp;length double&nbsp;l&nbsp;=&nbsp;6000; //Coupling&nbsp;length double&nbsp;fittinglength&nbsp;=&nbsp;(1.1&nbsp;*&nbsp;pipeDia&nbsp;+&nbsp;14.4); //&nbsp;finding&nbsp;the&nbsp;length&nbsp;of&nbsp;the&nbsp;selected&nbsp;pipe. double&nbsp;len&nbsp;=&nbsp;UnitUtils.ConvertFromInternalUnits(&nbsp;segment.get_Parameter(&nbsp;BuiltInParameter.CURVE_ELEM_LENGTH&nbsp;).AsDouble(),&nbsp;DisplayUnitType.DUT_MILLIMETERS&nbsp;); if(&nbsp;len&nbsp;&lt;=&nbsp;l&nbsp;) &nbsp;&nbsp;return;
```

```csharp
var&nbsp;startPoint&nbsp;=&nbsp;c1.GetEndPoint(&nbsp;0&nbsp;); var&nbsp;endPoint&nbsp;=&nbsp;c1.GetEndPoint(&nbsp;1&nbsp;); XYZ&nbsp;splitpoint&nbsp;=&nbsp;(endPoint&nbsp;-&nbsp;startPoint)&nbsp;*&nbsp;(l&nbsp;/&nbsp;len); var&nbsp;newpoint&nbsp;=&nbsp;startPoint&nbsp;+&nbsp;splitpoint; Pipe&nbsp;pp&nbsp;=&nbsp;segment&nbsp;as&nbsp;Pipe; //&nbsp;Find&nbsp;two&nbsp;connectors&nbsp;which&nbsp;pipe&#39;s&nbsp;two&nbsp;ends&nbsp;connector&nbsp;connected&nbsp;to.&nbsp; Connector&nbsp;startConn&nbsp;=&nbsp;FindConnectedTo(&nbsp;pp,&nbsp;startPoint&nbsp;); Connector&nbsp;endConn&nbsp;=&nbsp;FindConnectedTo(&nbsp;pp,&nbsp;endPoint&nbsp;);
```

```csharp
//&nbsp;creating&nbsp;first&nbsp;pipe&nbsp; Pipe&nbsp;pipe&nbsp;=&nbsp;null; if(&nbsp;null&nbsp;!=&nbsp;_pipeType&nbsp;) { &nbsp;&nbsp;pipe&nbsp;=&nbsp;Pipe.Create(&nbsp;_activeDoc.Document,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;_pipeType.Id,&nbsp;levelId,&nbsp;startConn,&nbsp;newpoint&nbsp;); } Connector&nbsp;conn1&nbsp;=&nbsp;FindConnector(&nbsp;pipe,&nbsp;newpoint&nbsp;); //Check&nbsp;+&nbsp;fitting XYZ&nbsp;fittingend&nbsp;=&nbsp;(endPoint&nbsp;-&nbsp;startPoint)&nbsp; &nbsp;&nbsp;*&nbsp;((l&nbsp;+&nbsp;(fittinglength&nbsp;/&nbsp;2))&nbsp;/&nbsp;len); //New&nbsp;point&nbsp;after&nbsp;the&nbsp;fitting&nbsp;gap var&nbsp;endOfFitting&nbsp;=&nbsp;startPoint&nbsp;+&nbsp;fittingend; Pipe&nbsp;pipe1&nbsp;=&nbsp;Pipe.Create(&nbsp;_activeDoc.Document,&nbsp; &nbsp;&nbsp;systemtype,&nbsp;_pipeType.Id,&nbsp;levelId,&nbsp;endOfFitting,&nbsp; &nbsp;&nbsp;endPoint&nbsp;); //&nbsp;Copy&nbsp;parameters&nbsp;from&nbsp;previous&nbsp;pipe&nbsp;to&nbsp;the&nbsp;following&nbsp;Pipe.&nbsp; CopyParameters(&nbsp;pipe,&nbsp;pipe1&nbsp;); Connector&nbsp;conn2&nbsp;=&nbsp;FindConnector(&nbsp;pipe1,&nbsp;endOfFitting&nbsp;); _&nbsp;=&nbsp;_activeDoc.Document.Create.NewUnionFitting(&nbsp;conn1,&nbsp;conn2&nbsp;); if(&nbsp;null&nbsp;!=&nbsp;endConn&nbsp;) { &nbsp;&nbsp;Connector&nbsp;pipeEndConn&nbsp;=&nbsp;FindConnector(&nbsp;pipe1,&nbsp;endPoint&nbsp;); &nbsp;&nbsp;pipeEndConn.ConnectTo(&nbsp;endConn&nbsp;); }
```
