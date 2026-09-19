---
num: 1639
date: 2018-04-03
themes: [Geometry, LinkedModel]
tags: [revit-api, tbc]
---

# Using Intersection Filter with Linked File

<https://jeremytammik.github.io/tbc/a/1639_linked_inters_filt.html>

```csharp
Dim ElementParameters As ParameterSet = el.Parameters For Each elparam As Parameter In ElementParameters If elparam.Definition.Name = "OBJ-LOCATION-RDK" Then elparam.Set("") oWrite1.WriteLine(el.Category.Name) End If Next
```

```csharp
IList plist = e.GetParameters("OBJ-LOCATION-RDK") Parameter elparam = plist[0] elparam.Set("")
```
