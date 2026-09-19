---
num: 1716
date: 2019-01-18
themes: [Geometry]
tags: [revit-api, tbc]
---

# New RevitLookup Snoops Edges, Faces and Links

<https://jeremytammik.github.io/tbc/a/1716_snoop_edge_face_link.html>

```csharp
optionsBtn.AddPushButton(&nbsp;new&nbsp;PushButtonData(&nbsp;&quot;Snoop&nbsp;Pick&nbsp;Face...&quot;,&nbsp;&quot;Snoop&nbsp;Pick&nbsp;Face...&quot;,&nbsp;ExecutingAssemblyPath,&nbsp;&quot;RevitLookup.CmdSnoopModScopePickSurface&quot;&nbsp;)&nbsp;); optionsBtn.AddPushButton(&nbsp;new&nbsp;PushButtonData(&nbsp;&quot;Snoop&nbsp;Pick&nbsp;Edge...&quot;,&nbsp;&quot;Snoop&nbsp;Pick&nbsp;Edge...&quot;,&nbsp;ExecutingAssemblyPath,&nbsp;&quot;RevitLookup.CmdSnoopModScopePickEdge&quot;&nbsp;)&nbsp;); optionsBtn.AddPushButton(&nbsp;new&nbsp;PushButtonData(&nbsp;&quot;Snoop&nbsp;Pick&nbsp;Linked&nbsp;Element...&quot;,&nbsp;&quot;Snoop&nbsp;Linked&nbsp;Element...&quot;,&nbsp;ExecutingAssemblyPath,&nbsp;&quot;RevitLookup.CmdSnoopModScopeLinkedElement&quot;&nbsp;)&nbsp;);
```

```csharp
&nbsp;&nbsp;Face&nbsp;face&nbsp;=&nbsp;cmdData.Application.ActiveUIDocument &nbsp;&nbsp;&nbsp;&nbsp;.Document.GetElement(&nbsp;refElem&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.GetGeometryObjectFromReference(&nbsp;refElem&nbsp;)&nbsp;as&nbsp;Face;
```

```csharp
&nbsp;&nbsp;string&nbsp;stableRef&nbsp;=&nbsp;refElem &nbsp;&nbsp;&nbsp;&nbsp;.ConvertToStableRepresentation(&nbsp;uidoc.Document&nbsp;);
```

```csharp
&nbsp;&nbsp;List&lt;Solid&gt;&nbsp;solidsInFamily&nbsp;=&nbsp;new&nbsp;List&lt;Solid&gt;(); &nbsp;&nbsp;IList&lt;Type&gt;&nbsp;geomTypes&nbsp;=&nbsp;new&nbsp;List&lt;Type&gt;()&nbsp;{&nbsp;typeof(&nbsp;GenericForm&nbsp;),&nbsp;typeof(&nbsp;GeomCombination&nbsp;)&nbsp;}; &nbsp;&nbsp;ElementMulticlassFilter&nbsp;emcf&nbsp;=&nbsp;new&nbsp;ElementMulticlassFilter(&nbsp;geomTypes&nbsp;); &nbsp;&nbsp;FilteredElementCollector&nbsp;colForms&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;.WherePasses(&nbsp;emcf&nbsp;); &nbsp;&nbsp;Options&nbsp;opt&nbsp;=&nbsp;new&nbsp;Options(); &nbsp;&nbsp;opt.ComputeReferences&nbsp;=&nbsp;true; &nbsp;&nbsp;foreach(&nbsp;CombinableElement&nbsp;combinable&nbsp;in&nbsp;colForms&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;combinable&nbsp;is&nbsp;GenericForm&nbsp;&amp;&amp;&nbsp;!(&nbsp;combinable&nbsp;as&nbsp;GenericForm&nbsp;).IsSolid&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue; &nbsp;&nbsp;&nbsp;&nbsp;GeometryElement&nbsp;geomElem&nbsp;=&nbsp;combinable.get_Geometry(&nbsp;opt&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;List&lt;Solid&gt;&nbsp;solids&nbsp;=&nbsp;Utils.GetElementSolids(&nbsp;geomElem&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;solidsInFamily.AddRange(&nbsp;solids&nbsp;); &nbsp;&nbsp;}
```

```csharp
&nbsp;&nbsp;foreach(&nbsp;Solid&nbsp;solid&nbsp;in&nbsp;solids&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;Face&nbsp;face&nbsp;in&nbsp;solid.Faces&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string&nbsp;stable&nbsp;=&nbsp;face.Reference.ConvertToStableRepresentation(&nbsp;doc&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;stable&nbsp;==&nbsp;stableRef&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;face&nbsp;as&nbsp;PlanarFace; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;}
```
