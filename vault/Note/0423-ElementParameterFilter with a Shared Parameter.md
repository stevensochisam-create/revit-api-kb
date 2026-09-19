---
num: 423
date: 2010-08-10
themes: [Parameter]
tags: [revit-api, tbc]
---

# ElementParameterFilter with a Shared Parameter

<https://jeremytammik.github.io/tbc/a/0423_filter_shared_param.htm>

```csharp
public class ParamFilterTest : IExternalCommand { &nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication uiapp = commandData.Application; &nbsp; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; &nbsp; Application app = uiapp.Application; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; Wall wall = uidoc.Selection.PickObject( &nbsp; &nbsp; &nbsp; Autodesk.Revit.UI.Selection.ObjectType.Element ) &nbsp; &nbsp; &nbsp; .Element as Wall; &nbsp; &nbsp; &nbsp; Parameter parameter = wall.get_Parameter( &nbsp; &nbsp; &nbsp; &quot;Unconnected Height&quot; ); &nbsp; &nbsp; &nbsp; ParameterValueProvider pvp &nbsp; &nbsp; &nbsp; = new ParameterValueProvider( parameter.Id ); &nbsp; &nbsp; &nbsp; FilterNumericRuleEvaluator fnrv &nbsp; &nbsp; &nbsp; = new FilterNumericGreater(); &nbsp; &nbsp; &nbsp; FilterRule fRule &nbsp; &nbsp; &nbsp; = new FilterDoubleRule( pvp, fnrv, 20, 1E-6 ); &nbsp; &nbsp; &nbsp; ElementParameterFilter filter &nbsp; &nbsp; &nbsp; = new ElementParameterFilter( fRule ); &nbsp; &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; &nbsp; // Find walls with unconnected height &nbsp; &nbsp; // less than or equal to 20: &nbsp; &nbsp; &nbsp; ElementParameterFilter lessOrEqualFilter &nbsp; &nbsp; &nbsp; = new ElementParameterFilter( fRule, true ); &nbsp; &nbsp; &nbsp; IList&lt;Element&gt; lessOrEqualFounds &nbsp; &nbsp; &nbsp; = collector.WherePasses( lessOrEqualFilter ) &nbsp; &nbsp; &nbsp; &nbsp; .OfCategory( BuiltInCategory.OST_Walls ) &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( Wall ) ) &nbsp; &nbsp; &nbsp; &nbsp; .ToElements(); &nbsp; &nbsp; &nbsp; TaskDialog.Show( &quot;Revit&quot;, &quot;Walls found: &quot; &nbsp; &nbsp; &nbsp; + lessOrEqualFounds.Count ); &nbsp; &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```
