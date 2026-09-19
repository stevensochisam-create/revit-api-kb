---
num: 1427
date: 2016-04-20
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# RvtSamples for Revit 2017

<https://jeremytammik.github.io/tbc/a/1427_rvtsamples.html>

```csharp
bool&nbsp;testClassName&nbsp;=&nbsp;true;&nbsp;//&nbsp;jeremy
```

```csharp
&gt; md "C:\Users\tammikj\Documents\Visual Studio 2015\Addins" &gt; copy "C:\Users\tammikj\Documents\Visual Studio 2012\Addins" "C:\Users\tammikj\Documents\Visual Studio 2015\Addins" C:\Users\tammikj\Documents\Visual Studio 2012\Addins\CopySourceAsHtml.AddIn 1 file(s) copied.
```

```csharp
&lt;?xml&nbsp;version=&quot;1.0&quot;&nbsp;encoding=&quot;utf-8&quot;?&gt; &lt;RevitAddIns&gt; &nbsp;&nbsp;&lt;AddIn&nbsp;Type=&quot;Application&quot;&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;Name&gt;External&nbsp;Tool&lt;/Name&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;Assembly&gt;C:\a\lib\revit\2017\SDK\Samples\RvtSamples\CS\bin\Debug\RvtSamples.dll&lt;/Assembly&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;ClientId&gt;42cb0a70-2ee7-4e64-a42d-87b9cdcc41c8&lt;/ClientId&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;FullClassName&gt;RvtSamples.Application&lt;/FullClassName&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;VendorId&gt;ADSK&lt;/VendorId&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;VendorDescription&gt;Autodesk,&nbsp;www.autodesk.com&lt;/VendorDescription&gt; &nbsp;&nbsp;&lt;/AddIn&gt; &lt;/RevitAddIns&gt;
```

```csharp
[Window Title] Security - Unsigned Add-In [Main Instruction] The publisher of this add-in could not be verified. What do you want to do? [Content] Name: External Tool Publisher: Unknown Publisher Location: C:\a\lib\revit\2017\SDK\Samples\RvtSamples\CS\bin\Debug\RvtSamples.dll Issuer: None Date: 2016-04-20 15:28:45 Make sure that this add-in comes from a trusted source. [Always Load] [Load Once] [Do Not Load] [Footer] What are the risks?
```

```csharp
C:\...\FabricationPartLayout\CS &gt; grep class.*IExtern *.cs ConvertToFabrication.cs: public class ConvertToFabrication : IExtern... FabricationPartLayout.cs: public class FabricationPartLayout : IExte... OptimizeStraights.cs: public class OptimizeStraights : IExternalCommand RenumberingPart.cs: public class RenumberingPart : IExternalCommand StretchAndFit.cs: public class StretchAndFit : IExternalCommand
```
