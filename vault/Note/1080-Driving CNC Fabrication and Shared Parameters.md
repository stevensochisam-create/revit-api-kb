---
num: 1080
date: 2013-12-19
themes: [Parameter]
tags: [revit-api, tbc]
---

# Driving CNC Fabrication and Shared Parameters

<https://jeremytammik.github.io/tbc/a/1080_exportcncfab.htm>

```csharp
&nbsp; [Transaction( TransactionMode.Manual )] &nbsp; public class CmdSat : IExternalCommand &nbsp; { &nbsp; &nbsp; public Result Execute( &nbsp; &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; &nbsp; ref string message, &nbsp; &nbsp; &nbsp; ElementSet elements ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return CmdDxf.Execute2( commandData, true ); &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; static void OnDialogBoxShowing( &nbsp; &nbsp; object sender, &nbsp; &nbsp; DialogBoxShowingEventArgs e ) &nbsp; { &nbsp; &nbsp; TaskDialogShowingEventArgs e2 &nbsp; &nbsp; &nbsp; = e as TaskDialogShowingEventArgs; &nbsp; &nbsp; &nbsp; if( null != e2 &amp;&amp; e2.DialogId.Equals( &nbsp; &nbsp; &nbsp; &quot;TaskDialog_Really_Print_Or_Export_Temp_View_Modes&quot; ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; int cmdLink &nbsp; &nbsp; &nbsp; &nbsp; = (int) TaskDialogResult.CommandLink2; &nbsp; &nbsp; &nbsp; &nbsp; e.OverrideResult( cmdLink ); &nbsp; &nbsp; } &nbsp; }
```
