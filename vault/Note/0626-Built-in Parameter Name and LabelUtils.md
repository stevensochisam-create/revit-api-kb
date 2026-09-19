---
num: 626
date: 2011-08-08
themes: [Parameter]
tags: [revit-api, tbc]
---

# Built-in Parameter Name and LabelUtils

<https://jeremytammik.github.io/tbc/a/0626_label_utils.htm>

```csharp
&nbsp; string s = string.Empty; &nbsp; &nbsp; foreach( BuiltInParameter bip in &nbsp; &nbsp; Enum.GetValues( typeof( BuiltInParameter ) ) ) &nbsp; { &nbsp; &nbsp; s += &quot;\r\n&quot; + bip.ToString(); &nbsp; } &nbsp; TaskDialog.Show( &quot;Parameter Names&quot;, s );
```

```csharp
&nbsp; Element e; &nbsp; &nbsp; Dictionary&lt;BuiltInParameter, string&gt; mapBipToName &nbsp; &nbsp; = new Dictionary&lt;BuiltInParameter, string&gt;(); &nbsp; &nbsp; foreach( BuiltInParameter bip in &nbsp; &nbsp; Enum.GetValues( typeof( BuiltInParameter ) ) ) &nbsp; { &nbsp; &nbsp; // translate built-in enum to parameter name &nbsp; &nbsp; &nbsp; Parameter p = e.get_Parameter( bip ); &nbsp; &nbsp; &nbsp; if( null != p ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; mapBipToName.Add( bip, p.Definition.Name ); &nbsp; &nbsp; } &nbsp; }
```
