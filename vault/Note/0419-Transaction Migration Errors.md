---
num: 419
date: 2010-08-03
themes: [Transaction, VersionMigration]
tags: [revit-api, tbc]
---

# Transaction Migration Errors

<https://jeremytammik.github.io/tbc/a/0419_transaction_migration.htm>

```csharp
&nbsp; [Transaction( TransactionMode.Automatic )]
```

```csharp
&nbsp; SubTransaction t = new SubTransaction( doc ); &nbsp; ICollection&lt;ElementId&gt; delIds = null; &nbsp; try &nbsp; { &nbsp; &nbsp; t.Start(); &nbsp; &nbsp; delIds = doc.Delete( wall ); &nbsp; &nbsp; t.RollBack(); &nbsp; } &nbsp; catch ( Exception ex ) &nbsp; { &nbsp; &nbsp; message = &quot;Deletion failed: &quot; + ex.Message; &nbsp; &nbsp; t.RollBack(); &nbsp; &nbsp; return Result.Failed; &nbsp; }
```
