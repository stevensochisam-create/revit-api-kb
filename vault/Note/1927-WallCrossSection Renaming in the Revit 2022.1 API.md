---
num: 1927
date: 2021-11-10
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# WallCrossSection Renaming in the Revit 2022.1 API

<https://jeremytammik.github.io/tbc/a/1927_wallcrosssection.html>

```csharp
var&nbsp;PG_WALL_CROSS_SECTION&nbsp;=&nbsp;(BuiltInParameterGroup)&nbsp;(-5000228);
```

```csharp
using&nbsp;System.Reflection; . . . ForgeTypeId&nbsp;id&nbsp;=&nbsp;new&nbsp;ForgeTypeId(); Type&nbsp;type&nbsp;=&nbsp;typeof(GroupTypeId); PropertyInfo&nbsp;propOld&nbsp;=&nbsp;type.GetProperty(&quot;WallCrossSection&quot;, BindingFlags.Public&nbsp;|&nbsp;BindingFlags.Static); if&nbsp;(null&nbsp;!=&nbsp;propOld) { id&nbsp;=&nbsp;(ForgeTypeId)&nbsp;propOld.GetValue(null,&nbsp;null); } else { PropertyInfo&nbsp;propNew&nbsp;=&nbsp;type.GetProperty(&quot;WallCrossSectionDefinition&quot;, BindingFlags.Public&nbsp;|&nbsp;BindingFlags.Static); id&nbsp;=&nbsp;(ForgeTypeId)&nbsp;propNew.GetValue(null,&nbsp;null); }
```

```csharp
&nbsp;&nbsp;Type&nbsp;type&nbsp;=&nbsp;typeof(GroupTypeId); &nbsp;&nbsp;PropertyInfo&nbsp;prop&nbsp;=&nbsp;type.GetProperty(&quot;WallCrossSection&quot;,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;BindingFlags.Public&nbsp;|&nbsp;BindingFlags.Static)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;??&nbsp;type.GetProperty(&quot;WallCrossSectionDefinition&quot;,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BindingFlags.Public&nbsp;|&nbsp;BindingFlags.Static); &nbsp;&nbsp;ForgeTypeId&nbsp;id&nbsp;=&nbsp;(ForgeTypeId)&nbsp;prop.GetValue(null,&nbsp;null);
```
