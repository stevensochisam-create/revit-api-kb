---
num: 1643
date: 2018-04-13
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Compiling the Revit 2019 SDK Samples

<https://jeremytammik.github.io/tbc/a/1643_revit_2019_sdk.html>

```csharp
&nbsp;&nbsp;&lt;PropertyGroup&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;Configuration&nbsp;Condition=&quot;&nbsp;&#39;$(Configuration)&#39;&nbsp;==&nbsp;&#39;&#39;&nbsp;&quot;&gt;Debug&lt;/Configuration&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;Platform&nbsp;Condition=&quot;&nbsp;&#39;$(Platform)&#39;&nbsp;==&nbsp;&#39;&#39;&nbsp;&quot;&gt;AnyCPU&lt;/Platform&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;ProductVersion&gt;9.0.30729&lt;/ProductVersion&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;SchemaVersion&gt;2.0&lt;/SchemaVersion&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;ProjectGuid&gt;{4E3C160F-1FC8-4BD7-8E01-B62C58E79CD4}&lt;/ProjectGuid&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;OutputType&gt;Library&lt;/OutputType&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;AppDesignerFolder&gt;Properties&lt;/AppDesignerFolder&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;RootNamespace&gt;Revit.SDK.Samples.DimensionLeaderEnd.CS&lt;/RootNamespace&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;AssemblyName&gt;DimensionLeaderEnd&lt;/AssemblyName&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;StartupObject&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;/StartupObject&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;TargetFrameworkVersion&gt;v4.7&lt;/TargetFrameworkVersion&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;TargetFrameworkProfile&nbsp;/&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;OutputPath&gt;bin\x64\Debug\&lt;/OutputPath&gt; &nbsp;&nbsp;&lt;/PropertyGroup&gt;
```

```csharp
/v/C/Program Files/Autodesk/Revit 2019 $ find . | grep ASObjectsMgd ./AddIns/SteelConnections/ASObjectsMgd.dll
```
