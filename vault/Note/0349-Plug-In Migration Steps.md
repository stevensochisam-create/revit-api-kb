---
num: 349
date: 2010-04-22
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Plug-In Migration Steps

<https://jeremytammik.github.io/tbc/a/0349_migration_steps.htm>

```csharp
//using Autodesk.Revit; //using Autodesk.Revit.Elements; //using Autodesk.Revit.Structural.Enums; using Autodesk.Revit.ApplicationServices; using Autodesk.Revit.Attributes; using Autodesk.Revit.DB; using Autodesk.Revit.UI;
```

```csharp
[Transaction( TransactionMode.ReadOnly )] [Regeneration( RegenerationOption.Manual )]
```

```csharp
UIApplication uiapp = commandData.Application; UIDocument uidoc = uiapp.ActiveUIDocument; Application app = uiapp.Application; Document doc = uidoc.Document;
```

```csharp
Transaction t = new Transaction( doc, "Test" ); t.Start(); . . . t.Commit();
```
