---
num: 1506
date: 2016-12-09
themes: [Parameter]
tags: [revit-api, tbc]
---

# Need for Regen and Duplicate Parameter Access

<https://jeremytammik.github.io/tbc/a/1506_need_for_regen.html>

```csharp
# <---- Make unique numbers t = Transaction(doc, 'Rename Detail Numbers') t.Start() for i, viewport in enumerate(viewports): setParam(viewport, "Detail Number",getParam(viewport,"Detail Number")+"x") t.Commit() # <---- Do the thang t2 = Transaction(doc, 'Rename Detail Numbers') t2.Start() for i, viewport in enumerate(viewports): setParam(viewport, "Detail Number",detailViewNumberData[i]) t2.Commit()
```
