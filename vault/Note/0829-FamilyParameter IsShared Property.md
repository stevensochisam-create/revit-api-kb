---
num: 829
date: 2012-09-21
themes: [Parameter]
tags: [revit-api, tbc]
---

# FamilyParameter IsShared Property

<https://jeremytammik.github.io/tbc/a/0829_family_param_shared.htm>

```csharp
&nbsp; public bool IsShared &nbsp; { &nbsp; &nbsp; get { return getParameter().IsShared; } &nbsp; }
```

```csharp
&nbsp; public static bool IsShared( &nbsp; &nbsp; this FamilyParameter familyParameter ) &nbsp; { &nbsp; &nbsp; MethodInfo mi = familyParameter &nbsp; &nbsp; &nbsp; .GetType() &nbsp; &nbsp; &nbsp; .GetMethod( &quot;getParameter&quot;, &nbsp; &nbsp; &nbsp; &nbsp; BindingFlags.Instance &nbsp; &nbsp; &nbsp; &nbsp; | BindingFlags.NonPublic ); &nbsp; &nbsp; &nbsp; if( null == mi ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; throw new InvalidOperationException( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Could not find getParameter method&quot; ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; var parameter = mi.Invoke( familyParameter, &nbsp; &nbsp; &nbsp; new object[] { } ) as Parameter; &nbsp; &nbsp; &nbsp; return parameter.IsShared; &nbsp; }
```

```csharp
&nbsp; foreach( FamilyParameter fp in mgr.Parameters ) &nbsp; { &nbsp; &nbsp; if( fp.IsShared() ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; familyTypeParameter.Guid = fp.GUID; &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; try { var guid = parameter.GUID; } &nbsp; catch() {}
```
