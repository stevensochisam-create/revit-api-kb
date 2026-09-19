---
num: 663
date: 2011-10-11
themes: [MEP]
tags: [revit-api, tbc]
---

# Set New Pipe Type Properties

<https://jeremytammik.github.io/tbc/a/0663_set_new_pipe_type_prop.htm>

```csharp
&nbsp; &nbsp; newType.get_Parameter( &nbsp; &nbsp; &nbsp; BuiltInParameter.RBS_CURVETYPE_DEFAULT_ELBOW_PARAM ) &nbsp; &nbsp; &nbsp; &nbsp; .Set( ElementId.InvalidElementId );
```
