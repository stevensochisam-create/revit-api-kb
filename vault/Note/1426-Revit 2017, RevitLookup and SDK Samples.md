---
num: 1426
date: 2016-04-19
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2017, RevitLookup and SDK Samples

<https://jeremytammik.github.io/tbc/a/1426_revit_2017.html>

```csharp
01/20/2016 23:28 43,680 RevitAddInUtility.dll 01/20/2016 23:39 26,252,328 RevitAPI.dll 01/20/2016 23:40 81,568 RevitAPIBrowserUtils.dll 01/20/2016 23:30 1,255,584 RevitAPIFoundation.dll 01/20/2016 23:39 384,040 RevitAPIIFC.dll 01/20/2016 23:39 33,952 RevitAPILink.dll 01/20/2016 23:40 103,584 RevitAPIMacros.dll 01/20/2016 23:39 550,952 RevitAPIMacrosInterop.dll 01/20/2016 23:39 559,144 RevitAPIMacrosInteropAPI.dll 01/20/2016 23:40 2,695,720 RevitAPIUI.dll 01/20/2016 23:40 69,792 RevitAPIUILink.dll 01/20/2016 23:40 83,616 RevitAPIUIMacros.dll 01/20/2016 23:39 263,208 RevitAPIUIMacrosInterop.dll 01/20/2016 23:40 463,520 RevitAPIUIMacrosInteropAPI.dll 01/20/2016 23:32 12,464,168 RevitDBAPI.dll 01/20/2016 23:32 658,984 RevitMFCAPI.dll 01/20/2016 23:40 1,454,632 RevitUIAPI.dll 17 File(s) 47,418,472 bytes
```

```csharp
02/26/2016 03:23 42,968 RevitAddInUtility.dll 02/26/2016 03:34 26,252,760 RevitAPI.dll 02/26/2016 03:36 81,928 RevitAPIBrowserUtils.dll 02/26/2016 03:26 1,254,872 RevitAPIFoundation.dll 02/26/2016 03:35 385,544 RevitAPIIFC.dll 02/26/2016 03:35 34,312 RevitAPILink.dll 02/26/2016 03:35 103,944 RevitAPIMacros.dll 02/26/2016 03:35 551,384 RevitAPIMacrosInterop.dll 02/26/2016 03:35 559,576 RevitAPIMacrosInteropAPI.dll 02/26/2016 03:36 2,696,152 RevitAPIUI.dll 02/26/2016 03:36 70,152 RevitAPIUILink.dll 02/26/2016 03:36 83,976 RevitAPIUIMacros.dll 02/26/2016 03:35 264,712 RevitAPIUIMacrosInterop.dll 02/26/2016 03:35 462,808 RevitAPIUIMacrosInteropAPI.dll 02/26/2016 03:28 12,464,600 RevitDBAPI.dll 02/26/2016 03:28 660,488 RevitMFCAPI.dll 02/26/2016 03:35 1,455,576 RevitUIAPI.dll 17 File(s) 47,425,752 bytes
```

```csharp
04/15/2016 11:29 307,387,758 REVIT_2017_SDK.msi
```

```csharp
&lt;Reference Include=&quot;RevitAPI&quot;&gt; &nbsp; &lt;HintPath&gt;..\..\..\..\..\..\..\..\Releasex64\RevitAPI.dll&lt;/HintPath&gt; &lt;/Reference&gt; &lt;Reference Include=&quot;RevitAPIUI&quot;&gt; &nbsp; &lt;HintPath&gt;..\..\..\..\..\..\..\..\Releasex64\RevitAPIUI.dll&lt;/HintPath&gt; &lt;/Reference&gt;
```

```csharp
&gt; copy "C:\Program Files\Autodesk\Revit Kepler\RevitAddInUtility.dll" "..\Revit 2017"
```
