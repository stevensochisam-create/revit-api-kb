---
num: 1388
date: 2015-12-18
themes: [Parameter]
tags: [revit-api, tbc]
---

# Shared Project Parameter GUID Reporter

<https://jeremytammik.github.io/tbc/a/1388_project_param_guid.html>

```csharp
public struct MyData { public Definition def; public ElementBinding binding; } while (it.MoveNext()) { MyData myData; myData.def = it.Key; myData.binding = it.Current as ElementBinding; myDatas.Add(myData); } foreach (MyData md in myDatas) { // do normal processing }
```
