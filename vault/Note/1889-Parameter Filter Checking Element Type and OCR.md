---
num: 1889
date: 2021-01-29
themes: [Parameter]
tags: [revit-api, tbc]
---

# Parameter Filter Checking Element Type and OCR

<https://jeremytammik.github.io/tbc/a/1889_param_filter_type.html>

```csharp
&nbsp;&nbsp;BuiltInParameter&nbsp;bip&nbsp;=&nbsp;BuiltInParameter.FIRE_RATING; &nbsp;&nbsp;ElementId&nbsp;pid&nbsp;=&nbsp;new&nbsp;ElementId(&nbsp;bip&nbsp;); &nbsp;&nbsp;ParameterValueProvider&nbsp;provider &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;ParameterValueProvider(&nbsp;pid&nbsp;); &nbsp;&nbsp;FilterStringRuleEvaluator&nbsp;evaluator&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilterStringContains(); &nbsp;&nbsp;FilterStringRule&nbsp;rule&nbsp;=&nbsp;new&nbsp;FilterStringRule(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;provider,&nbsp;evaluator,&nbsp;&quot;/&quot;,&nbsp;false&nbsp;); &nbsp;&nbsp;ElementParameterFilter&nbsp;filter&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;ElementParameterFilter(&nbsp;rule&nbsp;); &nbsp;&nbsp;var&nbsp;myWalls&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.OfCategory(&nbsp;BuiltInCategory.OST_Walls&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.WherePasses(&nbsp;filter&nbsp;); &nbsp;&nbsp;List&lt;ElementId&gt;&nbsp;false_positive_ids&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;List&lt;ElementId&gt;(); &nbsp;&nbsp;foreach(&nbsp;Element&nbsp;wall&nbsp;in&nbsp;myWalls&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;Parameter&nbsp;param&nbsp;=&nbsp;wall.get_Parameter(&nbsp;bip&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;null&nbsp;==&nbsp;param&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;false_positive_ids.Add(&nbsp;wall.Id&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;} &nbsp;&nbsp;string&nbsp;s&nbsp;=&nbsp;string.Join(&nbsp;&quot;,&nbsp;&quot;,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;false_positive_ids.Select&lt;ElementId,&nbsp;string&gt;(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id&nbsp;=&gt;&nbsp;id.IntegerValue.ToString()&nbsp;)&nbsp;); &nbsp;&nbsp;TaskDialog&nbsp;dlg&nbsp;=&nbsp;new&nbsp;TaskDialog(&nbsp;&quot;False&nbsp;Positives&quot;&nbsp;); &nbsp;&nbsp;dlg.MainInstruction&nbsp;=&nbsp;&quot;False&nbsp;filtered&nbsp;walls&nbsp;ids:&nbsp;&quot;; &nbsp;&nbsp;dlg.MainContent&nbsp;=&nbsp;s; &nbsp;&nbsp;dlg.Show();
```

```csharp
if (m_elemOrSymbol == EOS_Symbol || err != ERR_SUCCESS || !oParameterValue) { ElementId typeId = pElement-&gt;getTypeId(); if (validElementId(typeId)) { const Element *pTypeElement = pElement-&gt;getDocument()-&gt;getElement(typeId); if (pTypeElement != NULL) { oParameterValue = pTypeElement-&gt;getParameterValue( m_parameter); err = getErrFromParameterValue(oParameterValue); if (err != ERR_SUCCESS) { return nullptr; } } } }
```
