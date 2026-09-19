---
num: 208
date: 2009-08-24
themes: [Parameter]
tags: [revit-api, tbc]
---

# Shared Parameter Visibility

<https://jeremytammik.github.io/tbc/a/0208_shared_param_visibility.htm>

```csharp
ExternalDefinition externalDef = param.Definition as ExternalDefinition; if( externalDef == null || externalDef.Visible ) { // show the parameter }
```

```csharp
public static bool isParameterVisible( Parameter p ) { &nbsp; bool bParameterIsVisible = true; &nbsp; &nbsp; try &nbsp; { &nbsp; &nbsp; BindingFlags flags &nbsp; &nbsp; &nbsp; = BindingFlags.Instance &nbsp; &nbsp; &nbsp; | BindingFlags.FlattenHierarchy &nbsp; &nbsp; &nbsp; | BindingFlags.Public &nbsp; &nbsp; &nbsp; | BindingFlags.NonPublic &nbsp; &nbsp; &nbsp; | BindingFlags.InvokeMethod; &nbsp; &nbsp; &nbsp; Type t = typeof( Definition ); &nbsp; &nbsp; object result = t.InvokeMember( &nbsp; &nbsp; &nbsp; &quot;get_Visible&quot;, flags, null, p.Definition, null ); &nbsp; &nbsp; &nbsp; if( null != result &amp;&amp; result is Boolean ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; bParameterIsVisible = (Boolean) result; &nbsp; &nbsp; } &nbsp; } &nbsp; catch( System.Exception ) &nbsp; { &nbsp; &nbsp; // in case of any problems, assume parameter is visible &nbsp; } &nbsp; return bParameterIsVisible; }
```
