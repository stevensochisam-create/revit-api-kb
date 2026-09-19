---
num: 1900
date: 2021-04-14
themes: [Parameter, Pitfall]
tags: [revit-api, tbc]
---

# PDF Export, ForgeTypeId and Multi-Target Add-In

<https://jeremytammik.github.io/tbc/a/1900_forgetypeid.html>

```csharp
&nbsp;&nbsp;if(&nbsp;parameter.Definition.ParameterType&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;==&nbsp;ParameterType.Text&nbsp;)&nbsp;&nbsp;...
```

```csharp
&nbsp;&nbsp;if(&nbsp;parameter.Definition.GetDataType()&nbsp;==&nbsp;????)&nbsp;&nbsp;....
```

```csharp
>>> element.Parameter[BuiltInParameter.ALL_MODEL_MARK].Definition.GetSpecTypeId() == SpecTypeId.Number True
```

```csharp
&nbsp;&nbsp;var&nbsp;option&nbsp;=&nbsp;new&nbsp;ExternalDefinitionCreationOptions(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&quot;ExampleParamForge&quot;,&nbsp;SpecTypeId.XXX&nbsp;???); &nbsp;&nbsp;var&nbsp;definition&nbsp;=&nbsp;definitionGroup.Definitions.Create(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;option&nbsp;);
```

```csharp
&lt;Project&nbsp;Sdk=&quot;Microsoft.NET.Sdk.WindowsDesktop&quot;&nbsp;InitialTargets=&quot;Test&quot;&gt; &nbsp;&nbsp;... &nbsp;&nbsp;&lt;PropertyGroup&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;TargetFrameworks&gt;net461;net47;net472;net48&lt;/TargetFrameworks&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;Configurations&gt;Debug;Release&lt;/Configurations&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;OutputPath&gt;bin\$(Configuration)\&lt;/OutputPath&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;UseWindowsForms&gt;true&lt;/UseWindowsForms&gt; &nbsp;&nbsp;&nbsp;&nbsp;&lt;RevitVersion&nbsp;Condition=&quot;&nbsp;&#39;$(RevitVersion)&#39;&nbsp;==&nbsp;&#39;&#39;&nbsp;&quot;&gt;2022&lt;/RevitVersion&gt; &nbsp;&nbsp;&nbsp;&nbsp;... &nbsp;&nbsp;&lt;/PropertyGroup&gt;
```
