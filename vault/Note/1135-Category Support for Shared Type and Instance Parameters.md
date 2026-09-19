---
num: 1135
date: 2014-04-14
themes: [Parameter, Pitfall]
tags: [revit-api, tbc]
---

# Category Support for Shared Type and Instance Parameters

<https://jeremytammik.github.io/tbc/a/1135_categ_type_inst_param.htm>

```csharp
&nbsp; SortedList&lt;string, Category&gt; CatList &nbsp; &nbsp; = new SortedList&lt;string, Category&gt;(); &nbsp; &nbsp; Categories cats = doc.Settings.Categories; &nbsp; &nbsp; foreach( Category cat in cats ) &nbsp; { &nbsp; &nbsp; if( cat.AllowsBoundParameters ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; CatList.Add( cat.Name, cat ); &nbsp; &nbsp; } &nbsp; }&nbsp; &nbsp;
```

```csharp
&nbsp; // Create a Category Set containing only &nbsp; // categories that allow Type bound parameters &nbsp; &nbsp; Categories cats = doc.Settings.Categories; &nbsp; &nbsp; Autodesk.Revit.DB.CategorySet catSetTypeOnly &nbsp; &nbsp; = doc.Application.Create.NewCategorySet(); &nbsp; &nbsp; foreach( Category cat in cats ) &nbsp; { &nbsp; &nbsp; // This property exists. &nbsp; &nbsp; &nbsp; if( cat.AllowsBoundParameters ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // This property is needed. &nbsp; &nbsp; &nbsp; &nbsp; if( cat.AllowsTypeBoundParameters ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; catSetTypeOnly.Insert( cat ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; BuiltInCategory bic = ...; &nbsp; &nbsp; bool bType = BicSupportsTypeParameters( bic ); &nbsp; bool bInstance = BicSupportsInstanceParameters( bic );
```

```csharp
&nbsp; #region Built-in categories supporting type parameters &nbsp; static public BuiltInCategory[] &nbsp; &nbsp; _bicAllowsBoundParametersAsType &nbsp; &nbsp; &nbsp; = new BuiltInCategory[] &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Analytical Links&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_LinksAnalytical, &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Structural Connections&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_StructConnections, &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Structural Fabric Areas&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_FabricAreas, . . . &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Walls&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_Walls &nbsp; &nbsp; &nbsp; }; &nbsp; #endregion // Built-in categories supporting type parameters &nbsp; #region Built-in categories supporting instance parameters &nbsp; static public BuiltInCategory[] &nbsp; &nbsp; _bicAllowsBoundParametersAsInstance &nbsp; &nbsp; &nbsp; = new BuiltInCategory[] &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Analytical Links&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_LinksAnalytical, &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Analytical Nodes&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_AnalyticalNodes, &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Analytical Foundation Slabs&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_FoundationSlabAnalytical, . . . &nbsp; &nbsp; &nbsp; &nbsp; ///&lt;summary&gt;Walls&lt;/summary&gt; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_Walls &nbsp; &nbsp; &nbsp; }; &nbsp; #endregion // Built-in categories supporting instance parameters
```

```csharp
&nbsp; static readonly Dictionary&lt;BuiltInCategory, BuiltInCategory&gt; &nbsp; &nbsp; _bicSupportsTypeParameters &nbsp; &nbsp; &nbsp; = _bicAllowsBoundParametersAsType &nbsp; &nbsp; &nbsp; &nbsp; .ToDictionary&lt;BuiltInCategory, BuiltInCategory&gt;( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; c =&gt; c ); &nbsp; &nbsp; static readonly Dictionary&lt;BuiltInCategory, BuiltInCategory&gt; &nbsp; &nbsp; _bicSupportsInstanceParameters &nbsp; &nbsp; &nbsp; = _bicAllowsBoundParametersAsInstance &nbsp; &nbsp; &nbsp; &nbsp; .ToDictionary&lt;BuiltInCategory, BuiltInCategory&gt;( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; c =&gt; c );
```
