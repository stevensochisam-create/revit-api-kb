---
num: 607
date: 2011-06-30
themes: [MEP]
tags: [revit-api, tbc]
---

# Modifying Cable Tray Shape

<https://jeremytammik.github.io/tbc/a/0607_cable_tray_shape.htm>

```csharp
&nbsp; Document doc = commandData.Application &nbsp; &nbsp; .ActiveUIDocument.Document; &nbsp; &nbsp; // Get the trays &nbsp; &nbsp; FilteredElementCollector trays &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfCategory( BuiltInCategory.OST_CableTray ) &nbsp; &nbsp; &nbsp; .WhereElementIsNotElementType(); &nbsp; &nbsp; // Get the ladder tray type &nbsp; &nbsp; FilteredElementCollector trayTypes &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( CableTrayType ) ); &nbsp; &nbsp; Element ladderType = trayTypes.First&lt;Element&gt;( &nbsp; &nbsp; e =&gt; e.Name.Equals( &quot;Ladder Cable Tray&quot; ) ); &nbsp; &nbsp; // Set all trays type to ladder &nbsp; &nbsp; foreach( Element tray in trays ) &nbsp; { &nbsp; &nbsp; Transaction trans = new Transaction( doc, &quot;Edit Type&quot; ); &nbsp; &nbsp; trans.Start(); &nbsp; &nbsp; tray.ChangeTypeId( ladderType.Id ); &nbsp; &nbsp; trans.Commit(); &nbsp; } &nbsp; return Result.Succeeded;
```
