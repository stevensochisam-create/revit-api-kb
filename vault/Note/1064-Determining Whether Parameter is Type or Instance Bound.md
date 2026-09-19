---
num: 1064
date: 2013-11-21
themes: [Parameter, Pitfall]
tags: [revit-api, tbc]
---

# Determining Whether Parameter is Type or Instance Bound

<https://jeremytammik.github.io/tbc/a/1064_param_type_or_inst.htm>

```csharp
[Transaction( TransactionMode.ReadOnly )] class CmdListSharedParams : IExternalCommand { &nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication app = commandData.Application; &nbsp; &nbsp; UIDocument uidoc = app.ActiveUIDocument; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; BindingMap bindings = doc.ParameterBindings; &nbsp; &nbsp; &nbsp; int n = bindings.Size; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;{0} shared parementer{1} defined{2}&quot;, &nbsp; &nbsp; &nbsp; n, Util.PluralSuffix( n ), Util.DotOrColon( n ) ); &nbsp; &nbsp; &nbsp; if( 0 &lt; n ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; DefinitionBindingMapIterator it &nbsp; &nbsp; &nbsp; &nbsp; = bindings.ForwardIterator(); &nbsp; &nbsp; &nbsp; &nbsp; while( it.MoveNext() ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; Definition d = it.Key as Definition; &nbsp; &nbsp; &nbsp; &nbsp; Binding b = it.Current as Binding; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Assert( b is ElementBinding, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;all Binding instances are ElementBinding instances&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Assert( b is InstanceBinding &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; || b is TypeBinding, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;all bindings are either instance or type&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // All definitions obtained in this manner &nbsp; &nbsp; &nbsp; &nbsp; // are InternalDefinition instances, even &nbsp; &nbsp; &nbsp; &nbsp; // if they are actually associated with &nbsp; &nbsp; &nbsp; &nbsp; // shared parameters, i.e. external. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Assert( d is InternalDefinition, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;all definitions obtained from BindingMap are internal&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; string sbinding = ( b is InstanceBinding ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ? &quot;instance&quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : &quot;type&quot;; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;{0}: {1}&quot;, d.Name, sbinding ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```
