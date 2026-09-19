---
num: 2004
date: 2023-08-17
themes: [Schedule]
tags: [revit-api, tbc]
---

# GasTools, Cmd Ids, Key Schedule et al

<https://jeremytammik.github.io/tbc/a/2004_cmd_id_key_schedule.html>

```csharp
elements = FilteredElementCollector(doc, viewSchedule.Id).ToElements()
```

```csharp
params = [] for i in elements: params.append(i.Parameters)
```

```csharp
Category category = Category.GetCategory(doc, BuiltInCategory.OST_Rooms); viewSchedule = ViewSchedule.CreateKeySchedule(doc, category.Id); FilteredElementCollector elementCollector = new FilteredElementCollector(doc, viewSchedule.Id); IList&lt;Element&gt; rows = elementCollector.ToElements();
```
