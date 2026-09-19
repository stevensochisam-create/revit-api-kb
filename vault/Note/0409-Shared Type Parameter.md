---
num: 409
date: 2010-07-16
themes: [Parameter]
tags: [revit-api, tbc]
---

# Shared Type Parameter

<https://jeremytammik.github.io/tbc/a/0409_shared_type_param.htm>

```csharp
&nbsp; Binding binding = typeParameter &nbsp; &nbsp; ? ca.NewTypeBinding( catSet ) as Binding &nbsp; &nbsp; : ca.NewInstanceBinding( catSet ) as Binding;
```

```csharp
Created a shared instance parameter 'SP1' for the Doors category. Created a shared instance parameter 'SP2' for the Walls category. Please insert a model group. Created a shared instance parameter 'SP3' for the Lines category. Created a shared type parameter 'SP4' for the Walls category.
```
