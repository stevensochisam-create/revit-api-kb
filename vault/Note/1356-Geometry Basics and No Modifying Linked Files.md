---
num: 1356
date: 2015-09-09
themes: [Geometry, LinkedModel]
tags: [revit-api, tbc]
---

# Geometry Basics and No Modifying Linked Files

<https://jeremytammik.github.io/tbc/a/1356_geom_transact_link.html>

```csharp
&nbsp; UIApplication uiapp = commandData.Application; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; Application app = uiapp.Application; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; foreach (Document d in app.Documents) &nbsp; { &nbsp; &nbsp; using (Transaction t = new Transaction(doc)) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; t.Start(&quot;New Space&quot;); &nbsp; &nbsp; &nbsp; Space sp = d.Create.NewSpace( ... ); &nbsp; &nbsp; &nbsp; t.Commit(); &nbsp; &nbsp; }&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }
```
