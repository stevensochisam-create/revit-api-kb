---
num: 2041
date: 2024-06-05
themes: [LinkedModel, Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2025 API Video and Hiding Linked Elements

<https://jeremytammik.github.io/tbc/a/2041_hide_linked.html>

```csharp
// Select elements using UIDocument // then use PostCommand "HideElements" // elemsFromRevitLinkInstance is "List&lt;Element&gt;" // these are the elements you want to hide in the link var refs = elemsFromRevitLinkInstance.Select( x => new Reference(x).CreateLinkReference(revitLinkInstance)) .ToList(); uidoc.Selection.SetReferences(refs); uidoc.Application.PostCommand( RevitCommandId.LookupPostableCommandId( PostableCommand.HideElements));
```

```csharp
// Get a link var filter = new ElementClassFilter(typeof(RevitLinkInstance)); var firstInstanceLink = (RevitLinkInstance) new FilteredElementCollector(doc) .WherePasses(filter) .FirstElement(); // Get its floors filter = new ElementClassFilter(typeof(Floor)); var elemsFromRevitLinkInstance = new FilteredElementCollector( firstInstanceLink.GetLinkDocument()) .WherePasses(filter) .ToElements(); // Isolate them var refs = elemsFromRevitLinkInstance.Select( x => new Reference(x).CreateLinkReference(firstInstanceLink)) .ToList(); uidoc.Selection.SetReferences(refs); uidoc.Application.PostCommand( RevitCommandId.LookupPostableCommandId( PostableCommand.HideElements));
```
