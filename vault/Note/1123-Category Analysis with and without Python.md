---
num: 1123
date: 2014-03-31
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# Category Analysis with and without Python

<https://jeremytammik.github.io/tbc/a/1123_category_analysis.htm>

```csharp
from System import * bindings = doc.ParameterBindings it = bindings.ForwardIterator() while it.MoveNext(): if it.Key.Name == 'my': # project parameter name for cat in it.Current.Categories: print Enum.ToObject(BuiltInCategory, cat.Id.IntegerValue)
```
