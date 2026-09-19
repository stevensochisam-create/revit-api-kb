---
num: 902
date: 2013-02-25
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# What's New in the Revit 2011 API

<https://jeremytammik.github.io/tbc/a/0902_whats_new_2011.htm>

```csharp
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt; &lt;RevitAddIns&gt; &nbsp; &lt;AddIn Type=&quot;Command&quot;&gt; &nbsp; &nbsp; &lt;Assembly&gt;c:\MyProgram\MyProgram.dll&lt;/Assembly&gt; &nbsp; &nbsp; &lt;AddInId&gt;76eb700a-2c85-4888-a78d-31429ecae9ed&lt;/AddInId&gt; &nbsp; &nbsp; &lt;FullClassName&gt;Revit.Samples.SampleCommand&lt;/FullClassName&gt; &nbsp; &nbsp; &lt;Text&gt;Sample command&lt;/Text&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInFamily&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;VisibilityMode&gt;NotVisibleInMEP&lt;/VisibilityMode&gt; &nbsp; &nbsp; &lt;AvailabilityClassName&gt;Revit.Samples.SampleAccessibilityCheck&lt;/AvailabilityClassName&gt; &nbsp; &nbsp; &lt;LongDescription&gt; &nbsp; &nbsp; &nbsp; &lt;p&gt;This is the long description for my command.&lt;/p&gt; &nbsp; &nbsp; &nbsp; &lt;/p/&gt; &nbsp; &nbsp; &nbsp; &lt;p&gt;This is another descriptive paragraph, with notes about how to use the command properly.&lt;/p&gt; &nbsp; &nbsp; &lt;/LongDescription&gt; &nbsp; &nbsp; &lt;TooltipImage&gt;c:\MyProgram\Autodesk.jpg&lt;/TooltipImage&gt; &nbsp; &nbsp; &lt;LargeImage&gt;c:\MyProgram\MyProgramIcon.png&lt;/LargeImage&gt; &nbsp; &lt;/AddIn&gt; &lt;/RevitAddIns&gt;
```

```csharp
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt; &lt;RevitAddIns&gt; &nbsp; &lt;AddIn Type=&quot;Application&quot;&gt; &nbsp; &nbsp; &lt;Name&gt;SampleApplication&lt;/Name&gt; &nbsp; &nbsp; &lt;Assembly&gt;c:\MyProgram\MyProgram.dll&lt;/Assembly&gt; &nbsp; &nbsp; &lt;AddInId&gt;604B1052-F742-4951-8576-C261D1993107&lt;/AddInId&gt; &nbsp; &nbsp; &lt;FullClassName&gt;Revit.Samples.SampleApplication&lt;/FullClassName&gt; &nbsp; &lt;/AddIn&gt; &lt;/RevitAddIns&gt;
```

```csharp
&lt;Text&gt;Extension Manager&lt;/Text&gt;
```

```csharp
&lt;LanguageType&gt;English_USA&lt;/LanguageType&gt;
```

```csharp
public class SampleAccessibilityCheck : IExternalCommandAvailability { &nbsp; public bool IsCommandAvailable( &nbsp; &nbsp; Autodesk.Revit.ApplicationServices.Application data, &nbsp; &nbsp; CategorySet selectedCategories ) &nbsp; { &nbsp; &nbsp; // Allow button click if there is no active selection &nbsp; &nbsp; if( selectedCategories.IsEmpty ) &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; &nbsp; // Allow button click if there is at least one wall selected &nbsp; &nbsp; foreach( Category c in selectedCategories ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( c.Id.IntegerValue == (int)BuiltInCategory.OST_Walls ) &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; } &nbsp; &nbsp; return false; &nbsp; } }
```
