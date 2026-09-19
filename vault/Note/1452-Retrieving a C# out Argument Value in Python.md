---
num: 1452
date: 2016-07-07
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# Retrieving a C# out Argument Value in Python

<https://jeremytammik.github.io/tbc/a/1452_py_out_arg.html>

```csharp
curveLoop = I.ExporterIFCUtils .GetInstanceCutoutFromWall( doc, wall, familyInstance, out basisY );
```

```csharp
for i in openingIds: try: bounding, orient = I.ExporterIFCUtils.GetInstanceCutoutFromWall(doc, element, doc.GetElement(i),) print "success" except: print (" failed for wall %s and opening %s" %(element.Id, i))
```
