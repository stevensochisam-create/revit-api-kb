---
num: 1785
date: 2019-10-01
themes: [Parameter]
tags: [revit-api, tbc]
---

# Get Project Parameter Id and Prevent Updater Loop

<https://jeremytammik.github.io/tbc/a/1785_dmu_loop_project_param.html>

```csharp
ElementId&nbsp;GetProjectParameterId( &nbsp;&nbsp;Document&nbsp;doc,&nbsp; &nbsp;&nbsp;string&nbsp;name&nbsp;) { &nbsp;&nbsp;ParameterElement&nbsp;pElem&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;ParameterElement&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;ParameterElement&gt;() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Where(&nbsp;e&nbsp;=&gt;&nbsp;e.Name.Equals(name)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.FirstOrDefault(); &nbsp;&nbsp;return&nbsp;pElem&nbsp;?.Id; }
```

```csharp
&nbsp;&nbsp;string&nbsp;newValue&nbsp;=&nbsp;&quot;4&quot;; &nbsp;&nbsp;if(&nbsp;param.AsValueString()&nbsp;!=&nbsp;newValue&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;param.SetValueString(&nbsp;newValue&nbsp;); &nbsp;&nbsp;}
```
