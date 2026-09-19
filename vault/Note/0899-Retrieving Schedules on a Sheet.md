---
num: 899
date: 2013-02-15
themes: [Schedule]
tags: [revit-api, tbc]
---

# Retrieving Schedules on a Sheet

<https://jeremytammik.github.io/tbc/a/0899_schedules_on_sheet.htm>

```csharp
&nbsp; public static class ViewSheetExtensions &nbsp; { &nbsp; &nbsp; public static IEnumerable&lt;ViewSchedule&gt; &nbsp; &nbsp; &nbsp; GetSchedules( this ViewSheet viewSheet )&nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; var doc = viewSheet.Document; &nbsp; &nbsp; &nbsp; &nbsp; FilteredElementCollector collector = &nbsp; &nbsp; &nbsp; &nbsp; new FilteredElementCollector( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; doc, viewSheet.Id ); &nbsp; &nbsp; &nbsp; &nbsp; var scheduleSheetInstances = &nbsp; &nbsp; &nbsp; &nbsp; collector &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( ScheduleSheetInstance ) ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .ToElements() &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .OfType&lt;ScheduleSheetInstance&gt;(); &nbsp; &nbsp; &nbsp; &nbsp; foreach( var scheduleSheetInstance in &nbsp; &nbsp; &nbsp; &nbsp; scheduleSheetInstances ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; var scheduleId = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; scheduleSheetInstance &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .ScheduleId; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( scheduleId == ElementId.InvalidElementId ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; var viewSchedule = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; doc.GetElement( scheduleId ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; as ViewSchedule; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( viewSchedule != null ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; yield return viewSchedule; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; var schedules = viewSheet &nbsp; &nbsp; .GetSchedules() &nbsp; &nbsp; .ToList(); &nbsp; foreach( var viewSchedule in schedules ) &nbsp; { &nbsp; &nbsp; // Do something &nbsp; }
```

```csharp
&nbsp; public static class ViewScheduleExtensions &nbsp; { &nbsp; &nbsp; public static IEnumerable&lt;ElementId&gt; &nbsp; &nbsp; &nbsp; GetElementIdsInSchedule( &nbsp; &nbsp; &nbsp; &nbsp; this ViewSchedule viewSchedule ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; var doc = viewSchedule.Document; &nbsp; &nbsp; &nbsp; &nbsp; FilteredElementCollector collector = &nbsp; &nbsp; &nbsp; &nbsp; new FilteredElementCollector( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; doc, viewSchedule.Id ); &nbsp; &nbsp; &nbsp; &nbsp; var elementIds = collector &nbsp; &nbsp; &nbsp; &nbsp; .WhereElementIsNotElementType() &nbsp; &nbsp; &nbsp; &nbsp; .ToElementIds(); &nbsp; &nbsp; &nbsp; &nbsp; return elementIds; &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; foreach( var id in elementIds ) &nbsp; { &nbsp; &nbsp; var element = doc.GetElement( id ); &nbsp; &nbsp; &nbsp; if( element is Material ) &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; &nbsp; // Do something &nbsp; }
```
