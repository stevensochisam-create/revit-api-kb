---
num: 581
date: 2011-05-16
themes: [Parameter, Pitfall]
tags: [revit-api, tbc]
---

# New Room Computation Parameters

<https://jeremytammik.github.io/tbc/a/0581_room_computation_param.htm>

```csharp
&nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( App.Document ); &nbsp; &nbsp; IList elementos = collector &nbsp; &nbsp; .OfCategory( BuiltInCategory.OST_Levels ) &nbsp; &nbsp; .WhereElementIsElementType() &nbsp; &nbsp; .ToElements(); &nbsp; &nbsp; foreach( Element e in elementos ) &nbsp; { &nbsp; &nbsp; Parameter p = e.get_Parameter( BuiltInParameter &nbsp; &nbsp; &nbsp; .LEVEL_ATTR_ROOM_COMPUTATION_AUTOMATIC ); &nbsp; &nbsp; &nbsp; p.Set( 0 ); &nbsp; &nbsp; &nbsp; p = e.get_Parameter( BuiltInParameter &nbsp; &nbsp; &nbsp; .LEVEL_ATTR_ROOM_COMPUTATION_HEIGHT ); &nbsp; &nbsp; &nbsp; p.Set( 0 ); &nbsp; } &nbsp;
```

```csharp
&nbsp; &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; uidoc.Document ); &nbsp; &nbsp; &nbsp; &nbsp; IList&lt;Element&gt; elementos = collector &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( Level ) ) &nbsp; &nbsp; &nbsp; &nbsp; .ToElements(); &nbsp; &nbsp; &nbsp; &nbsp; foreach( Element e in elementos ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; Parameter p = e.get_Parameter( BuiltInParameter &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .LEVEL_ROOM_COMPUTATION_HEIGHT ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; p.Set( 2.5 ); &nbsp; &nbsp; &nbsp; } &nbsp;
```
