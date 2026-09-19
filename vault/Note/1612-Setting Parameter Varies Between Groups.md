---
num: 1612
date: 2017-12-20
themes: [Parameter]
tags: [revit-api, tbc]
---

# Setting Parameter Varies Between Groups

<https://jeremytammik.github.io/tbc/a/1612_param_vary_group.html>

```csharp
&nbsp;&nbsp;&nbsp;&nbsp;///&nbsp;&lt;summary&gt; &nbsp;&nbsp;///&nbsp;Helper&nbsp;method&nbsp;to&nbsp;control&nbsp;`SetAllowVaryBetweenGroups`&nbsp; &nbsp;&nbsp;///&nbsp;option&nbsp;for&nbsp;instance&nbsp;binding&nbsp;param &nbsp;&nbsp;///&nbsp;&lt;/summary&gt; &nbsp;&nbsp;static&nbsp;void&nbsp;SetInstanceParamVaryBetweenGroupsBehaviour( &nbsp;&nbsp;&nbsp;&nbsp;Document&nbsp;doc,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;Guid&nbsp;guid,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;bool&nbsp;allowVaryBetweenGroups&nbsp;=&nbsp;true&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;try&nbsp;//&nbsp;last&nbsp;resort &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SharedParameterElement&nbsp;sp&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;SharedParameterElement.Lookup(&nbsp;doc,&nbsp;guid&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Should&nbsp;never&nbsp;happen&nbsp;as&nbsp;we&nbsp;will&nbsp;call&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;this&nbsp;only&nbsp;for&nbsp;*existing*&nbsp;shared&nbsp;param. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;null&nbsp;==&nbsp;sp&nbsp;)&nbsp;return;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;InternalDefinition&nbsp;def&nbsp;=&nbsp;sp.GetDefinition(); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;def.VariesAcrossGroups&nbsp;!=&nbsp;allowVaryBetweenGroups&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Must&nbsp;be&nbsp;within&nbsp;an&nbsp;outer&nbsp;transaction! &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;def.SetAllowVaryBetweenGroups(&nbsp;doc,&nbsp;allowVaryBetweenGroups&nbsp;);&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;catch&nbsp;{&nbsp;}&nbsp;//&nbsp;ideally,&nbsp;should&nbsp;report&nbsp;something&nbsp;to&nbsp;log... &nbsp;&nbsp;}
```
