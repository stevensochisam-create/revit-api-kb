---
num: 515
date: 2011-01-13
themes: [Parameter]
tags: [revit-api, tbc]
---

# Access to Shared Family Parameter GUID

<https://jeremytammik.github.io/tbc/a/0515_fam_param_guid.htm>

```csharp
&nbsp; FamilyParameter parameter &nbsp; &nbsp; = &lt;get a family parameter &nbsp; &nbsp; &nbsp; &nbsp; ref from the FamilyManager&gt; &nbsp; &nbsp; ExternalDefinition externalDef &nbsp; &nbsp; = parameter.Definition as ExternalDefinition; &nbsp; &nbsp; InternalDefinition internalDef &nbsp; &nbsp; = parameter.Definition as InternalDefinition;
```

```csharp
bool GetFamilyParamGuid( &nbsp; FamilyParameter fp, &nbsp; out string guid ) { &nbsp; guid = string.Empty; &nbsp; &nbsp; bool isShared = false; &nbsp; &nbsp; System.Reflection.FieldInfo fi &nbsp; &nbsp; = fp.GetType().GetField( &quot;m_Parameter&quot;, &nbsp; &nbsp; &nbsp; System.Reflection.BindingFlags.Instance &nbsp; &nbsp; &nbsp; | System.Reflection.BindingFlags.NonPublic ); &nbsp; &nbsp; if( null != fi ) &nbsp; { &nbsp; &nbsp; Parameter p = fi.GetValue( fp ) as Parameter; &nbsp; &nbsp; &nbsp; isShared = p.IsShared; &nbsp; &nbsp; &nbsp; if( isShared &amp;&amp; null != p.GUID ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; guid = p.GUID.ToString(); &nbsp; &nbsp; } &nbsp; } &nbsp; return isShared; }
```

```csharp
public Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; UIApplication app = commandData.Application; &nbsp; Document doc = app.ActiveUIDocument.Document; &nbsp; &nbsp; if( !doc.IsFamilyDocument ) &nbsp; { &nbsp; &nbsp; message = &nbsp; &nbsp; &nbsp; &quot;Please run this command in a family document.&quot;; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; bool isShared; &nbsp; &nbsp; string guid; &nbsp; &nbsp; &nbsp; FamilyManager mgr = doc.FamilyManager; &nbsp; &nbsp; &nbsp; foreach( FamilyParameter fp in mgr.Parameters ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; isShared = GetFamilyParamGuid( fp, out guid ); &nbsp; &nbsp; } &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```
