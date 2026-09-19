---
num: 1318
date: 2015-05-15
themes: [DynamoPython, VersionMigration]
tags: [revit-api, tbc]
---

# CopyElements, Revit 2016 Scalability, Python and Ruby

<https://jeremytammik.github.io/tbc/a/1318_2016_scalability.htm>

```csharp
&nbsp; ElementTransformUtils.CopyElements( view3DInLink, &nbsp; &nbsp; ids, view3DInHost, null, new CopyPasteOptions() );
```

```csharp
&nbsp; ElementTransformUtils.CopyElements( linkedDoc, ids, &nbsp; &nbsp; thisDoc, null, new CopyPasteOptions() );
```
