---
num: 435
date: 2010-08-31
themes: [Parameter]
tags: [revit-api, tbc]
---

# Modeless Form and Shared Parameter Disappearance

<https://jeremytammik.github.io/tbc/a/0435_shared_params_disappear.htm>

```csharp
&nbsp; // create an instance definition in &nbsp; // definition group MyParameters &nbsp; Definition myDefinition_ProductDate &nbsp; &nbsp; = myGroup.Definitions.Create( &nbsp; &nbsp; &nbsp; &quot;Instance_ProductDate&quot;, &nbsp; &nbsp; &nbsp; ParameterType.Text );
```

```csharp
&nbsp; // set visibility of the new parameter: &nbsp; &nbsp; // Category.AllowsBoundParameters property &nbsp; // indicates if a category can have shared &nbsp; // or project parameters. If it is false, &nbsp; // it may not be bound to shared parameters &nbsp; // using the BindingMap. Please note that &nbsp; // non-user-visible parameters can still be &nbsp; // bound to these categories. &nbsp; &nbsp; bool visible = cat.AllowsBoundParameters; &nbsp; &nbsp; // get or create the shared params definition: &nbsp; &nbsp; string defname = _defname + nameSuffix.ToString(); &nbsp; &nbsp; Definition definition = group.Definitions.get_Item( &nbsp; &nbsp; defname ); &nbsp; &nbsp; if( null == definition ) &nbsp; { &nbsp; &nbsp; definition = group.Definitions.Create( &nbsp; &nbsp; &nbsp; defname, _deftype, visible ); &nbsp; }
```
