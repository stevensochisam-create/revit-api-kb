---
num: 221
date: 2009-09-18
themes: [Parameter]
tags: [revit-api, tbc]
---

# Adding a Category to a Parameter Binding

<https://jeremytammik.github.io/tbc/a/0221_add_category_to_binding.htm>

```csharp
Dim extDef an ExternalBinding Dim b As InstanceBinding _ = doc.ParameterBindings.Item(extDef) For Each c As Category In categorySet If Not b.Categories.Contains(c) Then b.Categories.Insert(c) End If Next
```

```csharp
&nbsp; For Each extDef As ExternalDefinition In Binding.ParametersCol &nbsp; &nbsp; If doc.ParameterBindings.Contains(extDef) Then &nbsp; &nbsp; &nbsp; Dim Added As Boolean = False &nbsp; &nbsp; &nbsp; Dim b As ElementBinding = doc.ParameterBindings.Item(extDef) &nbsp; &nbsp; &nbsp; For Each c As Category In categorySet &nbsp; &nbsp; &nbsp; &nbsp; If Not b.Categories.Contains(c) Then &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; b.Categories.Insert(c) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 'Added = True&nbsp; ' HB &nbsp; &nbsp; &nbsp; &nbsp; End If &nbsp; &nbsp; &nbsp; Next &nbsp; &nbsp; &nbsp; 'If Added = True Then&nbsp; ' HB &nbsp; &nbsp; &nbsp; ' doc.ParameterBindings.ReInsert(extDef, b)&nbsp; ' HB &nbsp; &nbsp; &nbsp; 'End If&nbsp; ' HB &nbsp; &nbsp; Else &nbsp; &nbsp; &nbsp; doc.ParameterBindings.Insert(extDef, elementBinding) &nbsp; &nbsp; End If &nbsp; Next
```
