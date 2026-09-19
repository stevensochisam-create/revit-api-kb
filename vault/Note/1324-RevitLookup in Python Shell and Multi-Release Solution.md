---
num: 1324
date: 2015-05-27
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# RevitLookup in Python Shell and Multi-Release Solution

<https://jeremytammik.github.io/tbc/a/1324_revitlookup_python.htm>

```csharp
&lt;ItemGroup Condition="'$(Configuration)' == 'Debug 2014'"&gt; &lt;Reference Include="RevitAPI"&gt; &lt;HintPath&gt;..\RequiredLibraries\Revit2014\RevitAPI.dll&lt;/HintPath&gt; &lt;/Reference&gt; &lt;Reference Include="RevitAPIUI"&gt; &lt;HintPath&gt;..\RequiredLibraries\Revit2014\RevitAPIUI.dll&lt;/HintPath&gt; &lt;/Reference&gt; &lt;/ItemGroup&gt; &lt;ItemGroup Condition="'$(Configuration)' == 'Debug 2015'"&gt; &lt;Reference Include="RevitAPI"&gt; &lt;HintPath&gt;..\RequiredLibraries\Revit2015\RevitAPI.dll&lt;/HintPath&gt; &lt;/Reference&gt; &lt;Reference Include="RevitAPIUI"&gt; &lt;HintPath&gt;..\RequiredLibraries\Revit2015\RevitAPIUI.dll&lt;/HintPath&gt; &lt;/Reference&gt; &lt;/ItemGroup&gt; &lt;ItemGroup Condition="'$(Configuration)' == 'Debug 2016'"&gt; &lt;Reference Include="RevitAPI"&gt; &lt;HintPath&gt;..\RequiredLibraries\Revit2016\RevitAPI.dll&lt;/HintPath&gt; &lt;/Reference&gt; &lt;Reference Include="RevitAPIUI"&gt; &lt;HintPath&gt;..\RequiredLibraries\Revit2016\RevitAPIUI.dll&lt;/HintPath&gt; &lt;/Reference&gt; &lt;/ItemGroup&gt;
```
