---
num: 1601
date: 2017-11-13
themes: [DynamoPython, Parameter]
tags: [revit-api, tbc]
---

# Deleting a Global Parameter and RevitPythonShell

<https://jeremytammik.github.io/tbc/a/1601_delete_global_param.html>

```csharp
from Autodesk.Revit.DB import * doc = __revit__.ActiveUIDocument.Document id = GlobalParametersManager.FindByName(doc,'Test') t = Transaction(doc) t.Start('delete gp') doc.Delete(id) t.Commit()
```
