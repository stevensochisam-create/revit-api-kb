---
num: 2018
date: 2023-11-29
themes: [Geometry, Pitfall, Toposolid]
tags: [revit-api, tbc]
---

# Camera Target and Toposolid Subdivision Material

<https://jeremytammik.github.io/tbc/a/2018_topo_mat_came_targ.html>

```csharp
&lt;Window x:Class="RevitTestProject.TestWindow" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:d="http://schemas.microsoft.com/expression/blend/2008" xmlns:local="clr-namespace:RevitTestProject" xmlns:cef="clr-namespace:CefSharp.Wpf;assembly=CefSharp.Wpf" mc:Ignorable="d" Width="1000" Height="500"&gt; &lt;Grid Background="PapayaWhip"&gt; &lt;cef:ChromiumWebBrowser Name="ChromiumBrowser" Address="http://www.google.com" Width="900" Height="450"/&gt; &lt;/Grid&gt; &lt;/Window&gt;
```

```csharp
[Transaction(TransactionMode.Manual)] public class ChangeSubdivisionMaterial : IExternalCommand { public Result Execute(ExternalCommandData commandData, ref string message, ElementSet elements) { var uidoc = commandData.Application.ActiveUIDocument; var doc = uidoc.Document; var sel = uidoc.Selection; Toposolid topo = doc.GetElement(sel.PickObject( ObjectType.Element, new ToposolidFilter())) as Toposolid; ToposolidType topoType = doc.GetElement(topo.GetTypeId()) as ToposolidType; ElementId materialId = topoType.GetCompoundStructure().GetLayers().First().MaterialId; List&lt;Toposolid&gt; subdivisions = new FilteredElementCollector(doc) .OfClass(typeof(Toposolid)) .OfType&lt;Toposolid&gt;() .Where(t =&gt; t.HostTopoId == topo.Id) .ToList(); Transaction trans = new Transaction(doc, "change material"); trans.Start(); subdivisions.ForEach(t =&gt; t.get_Parameter( BuiltInParameter.TOPOSOLID_SUBDIVIDE_MATERIAL) .Set(materialId)); trans.Commit(); return Result.Succeeded; } }
```
