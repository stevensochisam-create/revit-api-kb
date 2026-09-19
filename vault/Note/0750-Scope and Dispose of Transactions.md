---
num: 750
date: 2012-04-18
themes: [Transaction]
tags: [revit-api, tbc]
---

# Scope and Dispose of Transactions

<https://jeremytammik.github.io/tbc/a/0750_dispose_transact.htm>

```csharp
&nbsp; using( TransactionGroup group &nbsp; &nbsp; = new TransactionGroup( doc ) ) &nbsp; { &nbsp; &nbsp; group.Start( &quot;Muda a fachada&quot; ); &nbsp; &nbsp; &nbsp; using( Transaction tran &nbsp; &nbsp; &nbsp; = new Transaction( doc ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; tran.Start( &quot;Step 1 &quot; ); &nbsp; &nbsp; &nbsp; Calcula_Padrao( doc, Paneis, 0.10 ); &nbsp; &nbsp; &nbsp; tran.Commit(); &nbsp; &nbsp; &nbsp; &nbsp; uidoc.RefreshActiveView(); &nbsp; &nbsp; &nbsp; &nbsp; Thread.Sleep( 2000 ); &nbsp; &nbsp; &nbsp; &nbsp; tran.Start( &quot;Step 2 &quot; ); &nbsp; &nbsp; &nbsp; Calcula_Padrao( doc, Paneis, 0.4 ); &nbsp; &nbsp; &nbsp; tran.Commit(); &nbsp; &nbsp; &nbsp; &nbsp; uidoc.RefreshActiveView(); &nbsp; &nbsp; &nbsp; &nbsp; Thread.Sleep( 2000 ); &nbsp; &nbsp; &nbsp; &nbsp; tran.Start( &quot;Step 3 &quot; ); &nbsp; &nbsp; &nbsp; Calcula_Padrao( doc, Paneis, 0.05 ); &nbsp; &nbsp; &nbsp; tran.Commit(); &nbsp; &nbsp; &nbsp; &nbsp; uidoc.RefreshActiveView(); &nbsp; &nbsp; &nbsp; &nbsp; Thread.Sleep( 2000 ); &nbsp; &nbsp; &nbsp; &nbsp; tran.Start( &quot;Step 4 &quot; ); &nbsp; &nbsp; &nbsp; Calcula_Padrao( doc, Paneis, 0.4 ); &nbsp; &nbsp; &nbsp; tran.Commit(); &nbsp; &nbsp; &nbsp; &nbsp; uidoc.RefreshActiveView(); &nbsp; &nbsp; } &nbsp; &nbsp; group.Assimilate(); &nbsp; }
```
