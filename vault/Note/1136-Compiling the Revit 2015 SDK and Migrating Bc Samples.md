---
num: 1136
date: 2014-04-15
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Compiling the Revit 2015 SDK and Migrating Bc Samples

<https://jeremytammik.github.io/tbc/a/1136_tbc_sdk_2015.htm>

```csharp
cd C:\a\lib\revit\2015\SDK\Samples jhint -v -r *proj | sort | uniq cd C:\Program Files\Autodesk\Revit Architecture 2015 cp RevitAddInUtility.dll RevitAPI.dll RevitAPIIFC.dll RevitAPIUI.dll "..\Revit 2015"
```

```csharp
C:\Revit 2015 SDK\ --&gt; C:\a\lib\revit\2015\SDK\
```

```csharp
#include C:\a\lib\revit\2015\bc\BcSamples.txt
```

```csharp
C:\a\lib\revit\2014\bc\ --&gt; C:\a\lib\revit\2015\bc\
```
