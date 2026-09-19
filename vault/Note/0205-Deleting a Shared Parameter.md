---
num: 205
date: 2009-08-19
themes: [Parameter]
tags: [revit-api, tbc]
---

# Deleting a Shared Parameter

<https://jeremytammik.github.io/tbc/a/0205_delete_shared_param.htm>

```csharp
public IExternalCommand.Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string messages, &nbsp; ElementSet elements ) { &nbsp; Application app = commandData.Application; &nbsp; Document doc = app.ActiveDocument; &nbsp; &nbsp; doc.Selection.StatusbarTip &nbsp; &nbsp; = &quot;Please select a wall to remove &quot; &nbsp; &nbsp; &nbsp; + &quot;the shared parameter bound to it.&quot;; &nbsp; &nbsp; doc.Selection.PickOne(); &nbsp; &nbsp; Element wall = null; &nbsp; &nbsp; foreach( Element e in doc.Selection.Elements ) &nbsp; { &nbsp; &nbsp; wall = e; &nbsp; &nbsp; break; &nbsp; } &nbsp; &nbsp; if( wall != null ) &nbsp; { &nbsp; &nbsp; Parameter par = wall.get_Parameter( &nbsp; &nbsp; &nbsp; &quot;APIParameter&quot; ); &nbsp; &nbsp; &nbsp; Definition def = par.Definition; &nbsp; &nbsp; &nbsp; doc.ParameterBindings.Remove( def ); &nbsp; } &nbsp; return IExternalCommand.Result.Succeeded; }
```

```csharp
public IExternalCommand.Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string messages, &nbsp; ElementSet elements ) { &nbsp; Application app = commandData.Application; &nbsp; Document doc = app.ActiveDocument; &nbsp; &nbsp; BindingMap bm = doc.ParameterBindings; &nbsp; &nbsp; DefinitionBindingMapIterator it &nbsp; &nbsp; = bm.ForwardIterator(); &nbsp; &nbsp; while( it.MoveNext() ) &nbsp; { &nbsp; &nbsp; Definition def = it.Key; &nbsp; &nbsp; &nbsp; if( def.Name.Equals( &quot;APIParameter&quot; ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; bm.Remove( def ); &nbsp; &nbsp; } &nbsp; } &nbsp; return IExternalCommand.Result.Succeeded; }
```
