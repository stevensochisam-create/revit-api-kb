---
num: 1677
date: 2018-08-27
themes: [Parameter]
tags: [revit-api, tbc]
---

# Colleagues Deleting Non-Shared Project Parameter

<https://jeremytammik.github.io/tbc/a/1677_del_non_shared_param.html>

```csharp
&nbsp;&nbsp;void&nbsp;DeleteNonSharedProjectParam(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;Document&nbsp;doc,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;string&nbsp;parametername&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;FilteredElementCollector&nbsp;ps &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.WhereElementIsNotElementType() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;ParameterElement&nbsp;)&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;ParameterElement&nbsp;projectparameter&nbsp;=&nbsp;null; &nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;ParameterElement&nbsp;pe&nbsp;in&nbsp;ps&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;pe.GetDefinition().Name.Equals(&nbsp;parametername&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;projectparameter&nbsp;=&nbsp;pe; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;projectparameter&nbsp;!=&nbsp;null&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;doc.Delete(&nbsp;projectparameter.Id&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;}
```

```csharp
&nbsp;&nbsp;ParameterElement&nbsp;projectparameter &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.WhereElementIsNotElementType() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;ParameterElement&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;ParameterElement&gt;() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Where(&nbsp;e&nbsp;=&gt;&nbsp;e.GetDefinition() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Name.Equals(&nbsp;parametername&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.FirstOrDefault(); &nbsp;&nbsp;if(&nbsp;projectparameter&nbsp;!=&nbsp;null&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;doc.Delete(&nbsp;projectparameter.Id&nbsp;); &nbsp;&nbsp;}
```
