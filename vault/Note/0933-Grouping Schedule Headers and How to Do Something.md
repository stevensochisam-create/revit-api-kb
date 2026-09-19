---
num: 933
date: 2013-04-22
themes: [Schedule]
tags: [revit-api, tbc]
---

# Grouping Schedule Headers and How to Do Something

<https://jeremytammik.github.io/tbc/a/0933_group_headers.htm>

```csharp
public Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; try &nbsp; { &nbsp; &nbsp; UIDocument uidoc = commandData.Application &nbsp; &nbsp; &nbsp; .ActiveUIDocument; &nbsp; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; // Create the schedule &nbsp; &nbsp; &nbsp; Transaction tran = new Transaction( doc ); &nbsp; &nbsp; tran.Start( &quot;Create schedule&quot; ); &nbsp; &nbsp; &nbsp; ViewSchedule sampleSchedule &nbsp; &nbsp; &nbsp; = ViewSchedule.CreateSchedule( doc, new &nbsp; &nbsp; &nbsp; &nbsp; ElementId( BuiltInCategory.OST_Windows ) ); &nbsp; &nbsp; &nbsp; foreach( ElementId id in &nbsp; &nbsp; &nbsp; ViewSchedule.GetAvailableParameters( doc, new &nbsp; &nbsp; &nbsp; &nbsp; ElementId( BuiltInCategory.OST_Windows ) ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; try &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; sampleSchedule.Definition.AddField( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; new SchedulableField( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ScheduleFieldType.Instance, id ) ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; catch( Exception ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; ScheduleDefinition sampleDefinition &nbsp; &nbsp; &nbsp; = sampleSchedule.Definition; &nbsp; &nbsp; &nbsp; // Hide two columns in the schedule &nbsp; &nbsp; &nbsp; sampleDefinition.GetField( 0 ).IsHidden = true; &nbsp; &nbsp; sampleDefinition.GetField( 1 ).IsHidden = true; &nbsp; &nbsp; &nbsp; // Commit the schedule. This is important so &nbsp; &nbsp; // you can set the active view. &nbsp; &nbsp; &nbsp; tran.Commit(); &nbsp; &nbsp; &nbsp; // Change the active view to the schedule. &nbsp; &nbsp; // This is required before the GroupHeaders &nbsp; &nbsp; // function will work. &nbsp; &nbsp; &nbsp; uidoc.ActiveView = sampleSchedule; &nbsp; &nbsp; &nbsp; // Group the last three headers. &nbsp; &nbsp; // Hidden fields are not counted in the left &nbsp; &nbsp; // and right values, so make sure to account &nbsp; &nbsp; // for that. &nbsp; &nbsp; &nbsp; tran.Start( &quot;Group headers&quot; ); &nbsp; &nbsp; &nbsp; int iFieldCount = sampleDefinition &nbsp; &nbsp; &nbsp; .GetFieldCount(); &nbsp; &nbsp; &nbsp; sampleSchedule.GroupHeaders( 0, &nbsp; &nbsp; &nbsp; iFieldCount - 5, 0, &nbsp; &nbsp; &nbsp; iFieldCount - 3, &quot;Group Header&quot; ); &nbsp; &nbsp; &nbsp; t
```
