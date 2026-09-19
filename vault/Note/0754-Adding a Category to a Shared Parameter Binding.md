---
num: 754
date: 2012-04-25
themes: [Parameter]
tags: [revit-api, tbc]
---

# Adding a Category to a Shared Parameter Binding

<https://jeremytammik.github.io/tbc/a/0754_shared_param_add_categ.htm>

```csharp
&nbsp; 'create a category set with the Element category in it &nbsp; Dim categories As Autodesk.Revit.DB.CategorySet &nbsp; categories = app.Create.NewCategorySet &nbsp; Dim LCategory As Autodesk.Revit.DB.Category &nbsp; LCategory = doc.Settings.Categories.Item( _ &nbsp; &nbsp; iCategory.Name.ToString) &nbsp; categories.Insert(LCategory) &nbsp; 'create a new Type binding for the Symbol categories &nbsp; Dim TypeBinding As Autodesk.Revit.DB.TypeBinding &nbsp; TypeBinding = app.Create.NewTypeBinding(categories) &nbsp; 'Bind the parameter &nbsp; doc.ParameterBindings.Insert( _ &nbsp; &nbsp; sharedParameterDefinition, TypeBinding)
```
