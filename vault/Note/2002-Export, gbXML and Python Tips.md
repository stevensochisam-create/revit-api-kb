---
num: 2002
date: 2023-07-27
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# Export, gbXML and Python Tips

<https://jeremytammik.github.io/tbc/a/2002_dll_hell_gbxml.html>

```csharp
### Setting Energy Analysis parameters ### opt=Analysis.EnergyAnalysisDetailModelOptions() opt.EnergyModelType=Analysis.EnergyModelType.BuildingElement opt.ExportMullions=False opt.IncludeShadingSurfaces=False opt.SimplifyCurtainSystems=True opt.Tier=Analysis.EnergyAnalysisDetailModelTier.SecondLevelBoundaries ### loop over all R-value combinations and create models ### t=Transaction(doc,"R change") c=Transaction(doc,"model creation") for i in range(len(FloorR)): for j in range(len(WallsR)): for k in range(len(RoofR)): t.Start() Floor.Set(FloorR[i]/0.3048) #R-value change for floor Wall.Set(WallsR[j]/0.3048)#R-value change for Walls Roof.Set(RoofR[k]/0.3048)#R-value change for roof t.Commit() t.Dispose() c.Start() model=Analysis.EnergyAnalysisDetailModel.Create(doc, opt) model.TransformModel() GBopt=GBXMLExportOptions() GBopt.ExportEnergyModelType=ExportEnergyModelType.BuildingElement doc.Export("C:\Users\Миша\Desktop\ASD","0"+","+str(0.2/FloorR[i])+","+str(0.3/WallsR[j])+","+str(0.3/RoofR[k]), GBopt) c.Commit()
```

```csharp
EnergyAnalysisDetailModelOptions.ExportMullions = False Traceback (most recent call last): File "&lt;stdin&gt;", line 1, in &lt;module&gt; AttributeError: static property 'ExportMullions' of 'EnergyAnalysisDetailModelOptions' can only be assigned to through a type, not an instance
```

```csharp
### Setting Energy Analysis parameters ### opt=Analysis.EnergyAnalysisDetailModelOptions() opt.EnergyModelType=Analysis.EnergyModelType.BuildingElement opt.ExportMullions=False opt.IncludeShadingSurfaces=False opt.SimplifyCurtainSystems=True opt.Tier=Analysis.EnergyAnalysisDetailModelTier.SecondLevelBoundaries
```

```csharp
using System.Threading.Tasks; using Autodesk.Revit.UI; using System.Windows.Forms; using Autodesk.Revit.UI.Events; namespace YourNamespaceHere { public class Class2 : IExternalApplication { UIControlledApplication UIControlledApplication; public Result OnStartup(UIControlledApplication Application) { UIControlledApplication = Application; UIControlledApplication.Idling += Application_Idling; return Result.Succeeded; } public Result OnShutdown(UIControlledApplication Application) => Result.Succeeded; void Application_Idling(object Sender, IdlingEventArgs E) { UIControlledApplication.Idling -= Application_Idling; var UIApplication = (UIApplication)Sender; MyMacro(UIApplication); //TaskDialog.Show("Application_Idling", Sender.GetType().FullName); } void OnDialogBoxShowing(object Sender, DialogBoxShowingEventArgs Args) => ((TaskDialogShowingEventArgs)Args).OverrideResult((int)TaskDialogResult.Ok); static async void RunCommands(UIApplication UIapp, RevitCommandId Id_Addin) { UIapp.PostCommand(Id_Addin); await Task.Delay(400); SendKeys.Send("{ENTER}"); await Task.Delay(400); SendKeys.Send("{ENTER}"); await Task.Delay(400); SendKeys.Send("{ENTER}"); await Task.Delay(400); SendKeys.Send("{ESCAPE}"); await Task.Delay(400); SendKeys.Send("{ESCAPE}"); } void MyMacro(UIApplication UIapp) { try { var Name = "CustomCtrl_%CustomCtrl_%Twinmotion 2020%Twinmotion Direct Link%ExportButton"; var Id_Addin = RevitCommandId.LookupCommandId(Name); if (Id_Addin != null) { UIapp.DialogBoxShowing += OnDialogBoxShowing; RunCommands(UIapp, Id_Addin); } } catch { TaskDialog.Show("Test", "error"); } finally { UIapp.DialogBoxShowing -= OnDialogBoxShowing; } } } }
```
