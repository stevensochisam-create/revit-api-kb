---
num: 1654
date: 2018-05-17
themes: [Parameter]
tags: [revit-api, tbc]
---

# Getting All Parameter Values

<https://jeremytammik.github.io/tbc/a/1654_get_all_param_val.html>

```csharp
&nbsp;&nbsp;///&nbsp;&lt;summary&gt; &nbsp;&nbsp;///&nbsp;List&nbsp;all&nbsp;built-in&nbsp;categories&nbsp;of&nbsp;interest &nbsp;&nbsp;///&nbsp;&lt;/summary&gt; &nbsp;&nbsp;static&nbsp;BuiltInCategory[]&nbsp;_cats&nbsp;= &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;BuiltInCategory.OST_Doors, &nbsp;&nbsp;&nbsp;&nbsp;BuiltInCategory.OST_Rooms, &nbsp;&nbsp;&nbsp;&nbsp;BuiltInCategory.OST_Windows &nbsp;&nbsp;};
```

```csharp
Dictionary&lt;string, &nbsp;&nbsp;Dictionary&lt;string, &nbsp;&nbsp;&nbsp;&nbsp;Dictionary&lt;string,&nbsp;string&gt;&gt;&gt; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;map_cat_to_uid_to_param_values;
```

```csharp
param_values.Add(&nbsp;string.Format(&nbsp;&quot;{0}={1}&quot;,&nbsp; &nbsp;&nbsp;p.Definition.Name,&nbsp;p.AsValueString()&nbsp;)&nbsp;);
```

```csharp
Dictionary&lt;string, &nbsp;&nbsp;Dictionary&lt;string, &nbsp;&nbsp;&nbsp;&nbsp;List&lt;string&gt;&gt;&gt; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;map_cat_to_uid_to_param_values;
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Return&nbsp;all&nbsp;the&nbsp;parameter&nbsp;values&nbsp;&nbsp; ///&nbsp;deemed&nbsp;relevant&nbsp;for&nbsp;the&nbsp;given&nbsp;element ///&nbsp;in&nbsp;string&nbsp;form. ///&nbsp;&lt;/summary&gt; List&lt;string&gt;&nbsp;GetParamValues(&nbsp;Element&nbsp;e&nbsp;) { &nbsp;&nbsp;//&nbsp;Two&nbsp;choices:&nbsp; &nbsp;&nbsp;//&nbsp;Element.Parameters&nbsp;property&nbsp;--&nbsp;Retrieves&nbsp; &nbsp;&nbsp;//&nbsp;a&nbsp;set&nbsp;containing&nbsp;all&nbsp;&nbsp;the&nbsp;parameters. &nbsp;&nbsp;//&nbsp;GetOrderedParameters&nbsp;method&nbsp;--&nbsp;Gets&nbsp;the&nbsp; &nbsp;&nbsp;//&nbsp;visible&nbsp;parameters&nbsp;in&nbsp;order. &nbsp;&nbsp;IList&lt;Parameter&gt;&nbsp;ps&nbsp;=&nbsp;e.GetOrderedParameters(); &nbsp;&nbsp;List&lt;string&gt;&nbsp;param_values&nbsp;=&nbsp;new&nbsp;List&lt;string&gt;(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;ps.Count&nbsp;); &nbsp;&nbsp;foreach(&nbsp;Parameter&nbsp;p&nbsp;in&nbsp;ps) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;AsValueString&nbsp;displays&nbsp;the&nbsp;value&nbsp;as&nbsp;the&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;user&nbsp;sees&nbsp;it.&nbsp;In&nbsp;some&nbsp;cases,&nbsp;the&nbsp;underlying &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;database&nbsp;value&nbsp;returned&nbsp;by&nbsp;AsInteger,&nbsp;AsDouble, &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;etc.,&nbsp;may&nbsp;be&nbsp;more&nbsp;relevant. &nbsp;&nbsp;&nbsp;&nbsp;param_values.Add(&nbsp;string.Format(&nbsp;&quot;{0}={1}&quot;,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p.Definition.Name,&nbsp;p.AsValueString()&nbsp;)&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;return&nbsp;param_values; }
```
