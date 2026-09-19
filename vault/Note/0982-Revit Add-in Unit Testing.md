---
num: 982
date: 2013-07-12
themes: [Units]
tags: [revit-api, tbc]
---

# Revit Add-in Unit Testing

<https://jeremytammik.github.io/tbc/a/0982_rvtunit.htm>

```csharp
&lt;ItemGroup Condition=&quot;'$(Configuration)|$(Platform)' == 'Debug|AnyCPU'&quot;&gt; &nbsp; &lt;Reference Include=&quot;Moq&quot;&gt; &nbsp; &nbsp; &lt;HintPath&gt;..\rvtUnit\Lib\Moq.dll&lt;/HintPath&gt; &nbsp; &lt;/Reference&gt; &nbsp; . . . &nbsp; &lt;Compile Include=&quot;Tests\UnitTests\HasParameter_Tests.cs&quot; /&gt; &nbsp; &lt;None Include=&quot;Tests\Features\SetParameter.feature&quot;&gt; &nbsp; &nbsp; &lt;Generator&gt;SpecFlowSingleFileGenerator&lt;/Generator&gt; &nbsp; &nbsp; &lt;LastGenOutput&gt;SetParameter.feature.cs&lt;/LastGenOutput&gt; &nbsp; &lt;/None&gt; &lt;/ItemGroup&gt;
```
