---
num: 2078
date: 2025-07-25
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Jeremy's Retirement, Continuation of the Blog, Revit SDK 2026.2

<https://jeremytammik.github.io/tbc/a/2078_jeremy_tammik_retirement.html>

```csharp
RevitAddInManifestSettings.UnifyInAddInManager
```

```csharp
&lt;?xml version="1.0" encoding="utf-8"?&gt; &lt;RevitAddIns&gt; &lt;AddIn Type="DBApplication"&gt; &lt;Name&gt;SampleApplication&lt;/Name&gt; &lt;FullClassName&gt;SampleApplication.Application&lt;/FullClassName&gt; &lt;Assembly&gt;SampleApplication.dll&lt;/Assembly&gt; &lt;ClientId&gt;C96B32A3-98C6-4B47-99DA-562E64689C6F&lt;/ClientId&gt; &lt;VendorId&gt;Autodesk&lt;/VendorId&gt; &lt;/AddIn&gt; &lt;ManifestSettings&gt; &lt;UnifyInAddInManager&gt;True&lt;/UnifyInAddInManager&gt; &lt;/ManifestSettings&gt; &lt;/RevitAddIns&gt;
```

```csharp
FabricationPartType.ResetAssemblyTypes(Document doc)
```
