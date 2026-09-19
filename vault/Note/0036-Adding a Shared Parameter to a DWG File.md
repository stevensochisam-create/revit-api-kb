---
num: 36
date: 2008-11-10
themes: [Parameter]
tags: [revit-api, tbc]
---

# Adding a Shared Parameter to a DWG File

<https://jeremytammik.github.io/tbc/a/0036_dwg_shared_param.htm>

```csharp
public virtual Category get_Item( string key ); public virtual Category get_Item( BuiltInCategory categoryId );
```

```csharp
&nbsp; static public BuiltInCategory Target &nbsp; &nbsp; = BuiltInCategory.OST_Doors; &nbsp; static public BuiltInCategory Target &nbsp; &nbsp; = BuiltInCategory.OST_Walls; &nbsp; static public string Target &nbsp; &nbsp; = "Drawing1.dwg";
```
