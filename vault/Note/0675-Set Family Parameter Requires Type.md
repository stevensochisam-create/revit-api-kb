---
num: 675
date: 2011-11-14
themes: [Parameter]
tags: [revit-api, tbc]
---

# Set Family Parameter Requires Type

<https://jeremytammik.github.io/tbc/a/0675_set_family_param.htm>

```csharp
public class Command : IExternalCommand { &nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication uiapp = commandData.Application; &nbsp; &nbsp; &nbsp; uiapp.OpenAndActivateDocument( &nbsp; &nbsp; &nbsp; &quot;C:\\Projects\\FY12\\GE Revit\\SWBD-AV2.rfa&quot; ); &nbsp; &nbsp; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; &nbsp; Application app = uiapp.Application; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; FamilyManager familyMgr = doc.FamilyManager; &nbsp; &nbsp; &nbsp; FamilyParameter param = familyMgr.get_Parameter( &nbsp; &nbsp; &nbsp; &quot;Width&quot; ); &nbsp; &nbsp; &nbsp; if( null == param ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; param = doc.FamilyManager.AddParameter( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Width&quot;, BuiltInParameterGroup.PG_GEOMETRY, &nbsp; &nbsp; &nbsp; &nbsp; ParameterType.Length, true ); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; familyMgr.Set( param, 0.2 ); // set the value &nbsp; &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```

```csharp
&nbsp; if( doc.FamilyManager.Types.Size == 0 ) &nbsp; &nbsp; doc.FamilyManager.NewType( &quot;Type 1&quot; ); &nbsp; familyMgr.Set( param, 0.2 );
```
