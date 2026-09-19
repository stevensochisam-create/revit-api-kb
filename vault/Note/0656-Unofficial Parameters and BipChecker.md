---
num: 656
date: 2011-09-28
themes: [Parameter, Pitfall]
tags: [revit-api, tbc]
---

# Unofficial Parameters and BipChecker

<https://jeremytammik.github.io/tbc/a/0656_unofficial_param.htm>

```csharp
private Double? GetElementLength( Element element ) { &nbsp; var lengthParam &nbsp; &nbsp; = Enum.GetValues( typeof( BuiltInParameter ) ) &nbsp; &nbsp; &nbsp; .OfType&lt;BuiltInParameter&gt;() &nbsp; &nbsp; &nbsp; .Where( p =&gt; p.ToString().Contains( &quot;LENGTH&quot; ) ) &nbsp; &nbsp; &nbsp; .Select( param =&gt; element.get_Parameter( param ) ) &nbsp; &nbsp; &nbsp; .Where( param =&gt; param != null ) &nbsp; &nbsp; &nbsp; .FirstOrDefault(); &nbsp; &nbsp; if( lengthParam != null ) &nbsp; { &nbsp; &nbsp; var lengthValue = lengthParam.AsDouble(); &nbsp; &nbsp; return lengthValue; &nbsp; } &nbsp; &nbsp; return null; }
```

```csharp
Array bips = Enum.GetValues(typeof(BuiltInParameter)); Parameter p; foreach (BuiltInParameter a in bips) { try { p = elem.get_Parameter(a); } catch { } }
```

```csharp
bool IsParameterInCollection( Parameter parameter ) { &nbsp; foreach( Parameter p &nbsp; &nbsp; in parameter.Element.Parameters ) &nbsp; { &nbsp; &nbsp; if( p.IsShared &nbsp; &nbsp; &nbsp; != _parameter.IsShared ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return false; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; if( ( p.Definition as &nbsp; &nbsp; &nbsp; &nbsp; InternalDefinition ).BuiltInParameter &nbsp; &nbsp; &nbsp; == ( _parameter.Definition as &nbsp; &nbsp; &nbsp; &nbsp; InternalDefinition ).BuiltInParameter ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; _parameterInElementParametersCollection = true; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; } &nbsp; } &nbsp; return false; }
```

```csharp
#if USE_LIST_VIEW &nbsp; using( BuiltInParamsCheckerFormListView form &nbsp; &nbsp; = new BuiltInParamsCheckerFormListView( &nbsp; &nbsp; &nbsp; description, data ) ) #else &nbsp; using (BuiltInParamsCheckerForm form &nbsp; &nbsp; = new BuiltInParamsCheckerForm( &nbsp; &nbsp; &nbsp; description, data)) #endif // USE_LIST_VIEW &nbsp; { &nbsp; &nbsp; form.ShowDialog(); &nbsp; }
```

```csharp
&nbsp; wall.Parameters.Contains( &nbsp; &nbsp; wall.get_Parameter( &nbsp; &nbsp; &nbsp; BuiltInParameter.CURVE_ELEM_LENGTH ) )
```
