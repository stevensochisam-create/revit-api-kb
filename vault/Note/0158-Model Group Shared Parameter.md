---
num: 158
date: 2009-06-24
themes: [Parameter]
tags: [revit-api, tbc]
---

# Model Group Shared Parameter

<https://jeremytammik.github.io/tbc/a/0158_model_group_shared_param.htm>

```csharp
static public BuiltInCategory Target = BuiltInCategory.OST_IOSModelGroups;
```

```csharp
doc.ParameterBindings.Insert( fireRatingParamDef, binding );
```

```csharp
doc.Settings.Categories.get_Item( BuiltInCategory.OST_IOSModelGroups );
```

```csharp
Category GetCategory( Application app, BuiltInCategory target ) { &nbsp; Document doc = app.ActiveDocument; &nbsp; Category cat = null; &nbsp; &nbsp; if( target.Equals( BuiltInCategory.OST_IOSModelGroups ) ) &nbsp; { &nbsp; &nbsp; // &nbsp; &nbsp; // determine model group category: &nbsp; &nbsp; // &nbsp; &nbsp; Autodesk.Revit.Creation.Filter cf &nbsp; &nbsp; &nbsp; = app.Create.Filter; &nbsp; &nbsp; &nbsp; List&lt;Element&gt; modelGroups &nbsp; &nbsp; &nbsp; = new List&lt;Element&gt;(); &nbsp; &nbsp; &nbsp; Filter fType = cf.NewTypeFilter( &nbsp; &nbsp; &nbsp; typeof( Group ) ); &nbsp; &nbsp; &nbsp; //Filter fType = cf.NewTypeFilter( // this works as well &nbsp; &nbsp; //&nbsp; typeof( GroupType ) ); &nbsp; &nbsp; &nbsp; Filter fCategory = cf.NewCategoryFilter( &nbsp; &nbsp; &nbsp; BuiltInCategory.OST_IOSModelGroups ); &nbsp; &nbsp; &nbsp; Filter f = cf.NewLogicAndFilter( &nbsp; &nbsp; &nbsp; fType, fCategory ); &nbsp; &nbsp; &nbsp; if( 0 == doc.get_Elements( f, modelGroups ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Util.ErrorMsg( &quot;Please insert a model group.&quot; ); &nbsp; &nbsp; &nbsp; return cat; &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; cat = modelGroups[0].Category; &nbsp; &nbsp; } &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; try &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; cat = doc.Settings.Categories.get_Item( target ); &nbsp; &nbsp; } &nbsp; &nbsp; catch( Exception ex ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Util.ErrorMsg( string.Format( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Error obtaining document {0} category: {1}&quot;, &nbsp; &nbsp; &nbsp; &nbsp; target.ToString(), ex.Message ) ); &nbsp; &nbsp; &nbsp; return cat; &nbsp; &nbsp; } &nbsp; } &nbsp; if( null == cat ) &nbsp; { &nbsp; &nbsp; Util.ErrorMsg( string.Format( &nbsp; &nbsp; &nbsp; &quot;Unable to obtain the document {0} category.&quot;, &nbsp; &nbsp; &nbsp; target.ToString() ) ); &nbsp; } &nbsp; return cat; }
```

```csharp
bool CreateSharedParameter( &nbsp; Application app, &nbsp; Category cat, &nbsp; int nameSuffix ) { &nbsp; Document doc = app.ActiveDocument; &nbsp; // &nbsp; // get or set the current shared params filename: &nbsp; // &nbsp; string filename &nbsp; &nbsp; = app.Options.SharedParametersFilename; &nbsp; &nbsp; if( 0 == filename.Length ) &nbsp; { &nbsp; &nbsp; string path = _filename; &nbsp; &nbsp; StreamWriter stream; &nbsp; &nbsp; stream = new StreamWriter( path ); &nbsp; &nbsp; stream.Close(); &nbsp; &nbsp; app.Options.SharedParametersFilename = path; &nbsp; &nbsp; filename = app.Options.SharedParametersFilename; &nbsp; } &nbsp; // &nbsp; // get the current shared params file object: &nbsp; // &nbsp; DefinitionFile file &nbsp; &nbsp; = app.OpenSharedParameterFile(); &nbsp; &nbsp; if( null == file ) &nbsp; { &nbsp; &nbsp; Util.ErrorMsg( &nbsp; &nbsp; &nbsp; &quot;Error getting the shared params file.&quot; ); &nbsp; &nbsp; &nbsp; return false; &nbsp; } &nbsp; // &nbsp; // get or create the shared params group: &nbsp; // &nbsp; DefinitionGroup group &nbsp; &nbsp; = file.Groups.get_Item( _groupname ); &nbsp; &nbsp; if( null == group ) &nbsp; { &nbsp; &nbsp; group = file.Groups.Create( _groupname ); &nbsp; } &nbsp; &nbsp; if( null == group ) &nbsp; { &nbsp; &nbsp; Util.ErrorMsg( &nbsp; &nbsp; &nbsp; &quot;Error getting the shared params group.&quot; ); &nbsp; &nbsp; &nbsp; return false; &nbsp; } &nbsp; // &nbsp; // set visibility of the new parameter: &nbsp; // &nbsp; bool visible = cat.AllowsBoundParameters; &nbsp; // &nbsp; // get or create the shared params definition: &nbsp; // &nbsp; string defname = _defname + nameSuffix.ToString(); &nbsp; &nbsp; Definition definition = group.Definitions.get_Item( &nbsp; &nbsp; defname ); &nbsp; &nbsp; if( null == definition ) &nbsp; { &nbsp; &nbsp; definition = group.Definitions.Create( &nbsp; &nbsp; &nbsp; defname, _deftype, visible ); &nbsp; } &nbsp; if( null == definition ) &nbsp; { &nbsp; &nbsp; Util.ErrorMsg( &nbsp; &nbsp; &nbsp; &quot;Error in creating shared parameter.&quot; ); &nbsp; &nbsp; &nbsp; return false; &nbsp; } &nbsp; // &nbsp; // create the category set containing our category for binding: &nbsp; // &nbsp; CategorySet catSet = app.Create.NewCategorySet(); &nbsp; catSet.Insert( cat ); &nbsp; // &nbsp; // bind the param: &nbsp; // &nbsp; try &nbsp; { &nbsp; &nbsp; Binding binding = app.Create.NewInstanceBin
```
