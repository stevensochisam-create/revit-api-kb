---
num: 384
date: 2010-06-07
themes: [Parameter]
tags: [revit-api, tbc]
---

# Element Name Parameter Filter Correction

<https://jeremytammik.github.io/tbc/a/0384_elem_name_param_filter.htm>

```csharp
Element GetFirstElementOfTypeWithBipString( &nbsp; Type type, &nbsp; BuiltInParameter bip, &nbsp; string name ) { &nbsp; FilteredElementCollector a &nbsp; &nbsp; = GetElementsOfType( type ); &nbsp; &nbsp; ParameterValueProvider provider &nbsp; &nbsp; = new ParameterValueProvider( &nbsp; &nbsp; &nbsp; new ElementId( bip ) ); &nbsp; &nbsp; FilterStringRuleEvaluator evaluator &nbsp; &nbsp; = new FilterStringEquals(); &nbsp; &nbsp; FilterRule rule = new FilterStringRule( &nbsp; &nbsp; provider, evaluator, name, true ); &nbsp; &nbsp; ElementParameterFilter filter &nbsp; &nbsp; = new ElementParameterFilter( rule ); &nbsp; &nbsp; return a.WherePasses( filter ).FirstElement(); }
```

```csharp
&nbsp; level = null; &nbsp; &nbsp; using( JtTimer pt = new JtTimer( &nbsp; &nbsp; &quot;Parameter filter&quot; ) ) &nbsp; { &nbsp; &nbsp; //level = GetFirstElementOfTypeWithBipString( &nbsp; &nbsp; //&nbsp; t, BuiltInParameter.ELEM_NAME_PARAM, name ); &nbsp; &nbsp; &nbsp; level = GetFirstElementOfTypeWithBipString( &nbsp; &nbsp; &nbsp; t, BuiltInParameter.DATUM_TEXT, name ); &nbsp; } &nbsp; &nbsp; Debug.Assert( null != level, &nbsp; &nbsp; &quot;expected to find a valid level&quot; );
```

```csharp
--------------------------------------------------------------- Retrieve specific named level: Percentage Seconds Calls Process --------------------------------------------------------------- 0.00% 0.00 1000 Empty method * 0.19% 0.11 1000 Collector with no name check * 9.19% 5.46 1000 Parameter filter 22.53% 13.37 1000 Explicit 22.57% 13.40 1000 Anonymous named 22.73% 13.49 1000 Anonymous 22.73% 13.49 1000 Linq 100.00% 59.35 1 TOTAL TIME ---------------------------------------------------------------
```
