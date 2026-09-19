---
num: 1093
date: 2014-01-27
themes: [MEP]
tags: [revit-api, tbc]
---

# Final Rolling Offset Using Pipe.Create

<https://jeremytammik.github.io/tbc/a/1093_pipe_create.htm>

```csharp
&nbsp; // Extract all pipe system types &nbsp; &nbsp; var mepSystemTypes &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( PipingSystemType ) ) &nbsp; &nbsp; &nbsp; .OfType&lt;PipingSystemType&gt;() &nbsp; &nbsp; &nbsp; .ToList(); &nbsp; &nbsp; // Get the Domestic hot water type &nbsp; &nbsp; var domesticHotWaterSystemType = &nbsp; &nbsp; mepSystemTypes.FirstOrDefault( &nbsp; &nbsp; &nbsp; st =&gt; st.SystemClassification == &nbsp; &nbsp; &nbsp; &nbsp; MEPSystemClassification.DomesticHotWater ); &nbsp; &nbsp; if( domesticHotWaterSystemType == null ) &nbsp; { &nbsp; &nbsp; message = &quot;Could not found Domestic Hot Water System Type&quot;; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; &nbsp; // Looking for the PipeType &nbsp; &nbsp; var pipeTypes = &nbsp; &nbsp; new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( PipeType ) ) &nbsp; &nbsp; &nbsp; .OfType&lt;PipeType&gt;() &nbsp; &nbsp; &nbsp; .ToList(); &nbsp; &nbsp; // Get the first type from the collection &nbsp; &nbsp; var firstPipeType = &nbsp; &nbsp; &nbsp; pipeTypes.FirstOrDefault(); &nbsp; &nbsp; if( firstPipeType == null ) &nbsp; { &nbsp; &nbsp; message = &quot;Could not found Pipe Type&quot;; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; &nbsp; var level = uidoc.ActiveView.GenLevel; &nbsp; &nbsp; if( level == null ) &nbsp; { &nbsp; &nbsp; message = &quot;Wrong Active View&quot;; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; &nbsp; var startPoint = XYZ.Zero; &nbsp; &nbsp; var endPoint = new XYZ( 100, 0, 0 ); &nbsp; &nbsp; using( var t = new Transaction( doc ) ) &nbsp; { &nbsp; &nbsp; t.Start( &quot;Create pipe using Pipe.Create&quot; ); &nbsp; &nbsp; &nbsp; var pipe = Pipe.Create( doc, &nbsp; &nbsp; &nbsp; domesticHotWaterSystemType.Id, &nbsp; &nbsp; &nbsp; firstPipeType.Id, &nbsp; &nbsp; &nbsp; level.Id, &nbsp; &nbsp; &nbsp; startPoint, &nbsp; &nbsp; &nbsp; endPoint ); &nbsp; &nbsp; &nbsp; t.Commit(); &nbsp; }
```

```csharp
&nbsp; ElementId idSystem = pipe.MEPSystem.Id;
```

```csharp
&nbsp; ElementId systemIdTypeId &nbsp; &nbsp; = pipe.MEPSystem.GetTypeId();
```

```csharp
&nbsp; ElementId systemIdTypeId; &nbsp; &nbsp; if( pipe.MEPSystem != null ) &nbsp; { &nbsp; &nbsp; systemIdTypeId = pipe.MEPSystem.GetTypeId(); &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; // Select some default systemTypeId &nbsp; &nbsp; // Extract all pipe system types &nbsp; &nbsp; var mepSystemTypes &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( PipingSystemType ) ) &nbsp; &nbsp; &nbsp; &nbsp; .OfType&lt;PipingSystemType&gt;() &nbsp; &nbsp; &nbsp; &nbsp; .ToList(); &nbsp; &nbsp; &nbsp; // Get the Domestic hot water type &nbsp; &nbsp; systemIdTypeId = mepSystemTypes.FirstOrDefault( &nbsp; &nbsp; &nbsp; st =&gt; st.SystemClassification == &nbsp; &nbsp; &nbsp; &nbsp; MEPSystemClassification.DomesticHotWater ); &nbsp; }
```
