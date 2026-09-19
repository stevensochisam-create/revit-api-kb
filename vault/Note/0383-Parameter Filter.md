---
num: 383
date: 2010-06-07
themes: [Parameter]
tags: [revit-api, tbc]
---

# Parameter Filter

<https://jeremytammik.github.io/tbc/a/0383_param_filter.htm>

```csharp
&nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; ICollection&lt;Element&gt; levels &nbsp; &nbsp; = collector.OfClass( typeof( Level ) ) &nbsp; &nbsp; &nbsp; .ToElements(); &nbsp; &nbsp; for( int i = 0; i &lt; levels.Count; i++ ) &nbsp; { &nbsp; &nbsp; ElementId levelId = levels.ElementAt( i ).Id; &nbsp; &nbsp; &nbsp; ElementLevelFilter levelFilter &nbsp; &nbsp; &nbsp; = new ElementLevelFilter( levelId ); &nbsp; &nbsp; &nbsp; collector = new FilteredElementCollector( doc ); &nbsp; &nbsp; &nbsp; ICollection&lt;Element&gt; allOnLevel &nbsp; &nbsp; &nbsp; = collector.WherePasses( levelFilter ) &nbsp; &nbsp; &nbsp; &nbsp; .ToElements(); &nbsp; &nbsp; &nbsp; // . . . &nbsp; }
```

```csharp
&nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; collector.OfCategory( &nbsp; &nbsp; BuiltInCategory.OST_StructuralFraming ); &nbsp; &nbsp; collector.OfClass( typeof( FamilyInstance ) ); &nbsp; &nbsp; BuiltInParameter bip = BuiltInParameter &nbsp; &nbsp; .INSTANCE_REFERENCE_LEVEL_PARAM; &nbsp; &nbsp; ParameterValueProvider provider &nbsp; &nbsp; = new ParameterValueProvider( &nbsp; &nbsp; &nbsp; new ElementId( bip ) ); &nbsp; &nbsp; FilterNumericRuleEvaluator evaluator &nbsp; &nbsp; = new FilterNumericGreater(); &nbsp; &nbsp; ElementId idRuleValue = level.Id; &nbsp; &nbsp; FilterElementIdRule rule &nbsp; &nbsp; = new FilterElementIdRule( &nbsp; &nbsp; &nbsp; provider, evaluator, idRuleValue ); &nbsp; &nbsp; ElementParameterFilter filter &nbsp; &nbsp; = new ElementParameterFilter( rule ); &nbsp; &nbsp; collector.WherePasses( filter );
```

```csharp
[TransactionAttribute( TransactionMode.ReadOnly )] [RegenerationAttribute( RegenerationOption.Manual )] public class RevitCommand : IExternalCommand { &nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string messages, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication app = commandData.Application; &nbsp; &nbsp; Document doc = app.ActiveUIDocument.Document; &nbsp; &nbsp; &nbsp; ElementId id = new ElementId( &nbsp; &nbsp; &nbsp; BuiltInParameter.ELEM_ROOM_NUMBER ); &nbsp; &nbsp; &nbsp; ParameterValueProvider provider &nbsp; &nbsp; &nbsp; = new ParameterValueProvider( id ); &nbsp; &nbsp; &nbsp; FilterStringRuleEvaluator evaluator &nbsp; &nbsp; &nbsp; = new FilterStringEquals(); &nbsp; &nbsp; &nbsp; string sRoomNumber = &quot;1&quot;; &nbsp; &nbsp; &nbsp; FilterRule rule = new FilterStringRule( &nbsp; &nbsp; &nbsp; provider, evaluator, sRoomNumber, false ); &nbsp; &nbsp; &nbsp; ElementParameterFilter filter &nbsp; &nbsp; &nbsp; = new ElementParameterFilter( rule ); &nbsp; &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; &nbsp; .WherePasses( filter ); &nbsp; &nbsp; &nbsp; string s = string.Empty; &nbsp; &nbsp; &nbsp; foreach( Element elem in collector ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; s += elem.Name + elem.Category.Name.ToString() + &quot;\n&quot;; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; System.Windows.Forms.MessageBox.Show( s ); &nbsp; &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```

```csharp
&nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; collector.OfClass( typeof( Level ) ); &nbsp; ElementId id = new ElementId( &nbsp; &nbsp; BuiltInParameter.DATUM_TEXT ); &nbsp; &nbsp; ParameterValueProvider provider &nbsp; &nbsp; = new ParameterValueProvider( id ); &nbsp; &nbsp; FilterStringRuleEvaluator evaluator &nbsp; &nbsp; = new FilterStringContains(); &nbsp; &nbsp; FilterRule rule = new FilterStringRule( &nbsp; &nbsp; provider, evaluator, &quot;Level&quot;, false ); &nbsp; &nbsp; ElementParameterFilter filter &nbsp; &nbsp; = new ElementParameterFilter( rule );
```

```csharp
&nbsp; BuiltInParameter testParam &nbsp; &nbsp; = BuiltInParameter.ID_PARAM; &nbsp; &nbsp; ParameterValueProvider pvp &nbsp; &nbsp; = new ParameterValueProvider( &nbsp; &nbsp; &nbsp; new ElementId( ( int ) testParam ) ); &nbsp; &nbsp; FilterNumericRuleEvaluator fnrv &nbsp; &nbsp; = new FilterNumericGreater(); &nbsp; &nbsp; // filter elements whose Id is greater than 99 &nbsp; &nbsp; ElementId ruleValId = new ElementId( 99 ); &nbsp; &nbsp; FilterRule paramFr = new FilterElementIdRule( &nbsp; &nbsp; pvp, fnrv, ruleValId ); &nbsp; &nbsp; ElementParameterFilter epf &nbsp; &nbsp; = new ElementParameterFilter( paramFr ); &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector(&nbsp; doc ); &nbsp; &nbsp; collector.OfClass( typeof( ViewPlan ) ) &nbsp; &nbsp; .WherePasses( epf ); // only deal with ViewPlan
```
