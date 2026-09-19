---
num: 1605
date: 2017-11-28
themes: [Parameter]
tags: [revit-api, tbc]
---

# Cloud Model Predicate, and Set Parameter Regenerates

<https://jeremytammik.github.io/tbc/a/1605_param_regen_cloud_model.html>

```csharp
&nbsp;&nbsp;public&nbsp;static&nbsp;bool&nbsp;GetIsModelInCloud( &nbsp;&nbsp;&nbsp;&nbsp;Document&nbsp;document&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;PropertyInfo&nbsp;p&nbsp;=&nbsp;typeof(&nbsp;Document&nbsp;).GetProperty( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;IsModelInCloud&quot;, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BindingFlags.NonPublic&nbsp;|&nbsp;BindingFlags.Instance&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;(bool)&nbsp;p.GetValue(&nbsp;document&nbsp;); &nbsp;&nbsp;}
```
