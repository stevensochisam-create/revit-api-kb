---
num: 1250
date: 2014-11-29
themes: [Transaction]
tags: [revit-api, tbc]
---

# Handling Transaction Status and Errors

<https://jeremytammik.github.io/tbc/a/1250_transaction.htm>

```csharp
&nbsp; try &nbsp; { &nbsp; &nbsp; using (var trans = new Transaction(doc, &quot;Transaction Name&quot;)) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; trans.Start(); &nbsp; &nbsp; &nbsp; &nbsp; ///////////DO SOMETHING TO THE MODEL/////////////////// &nbsp; &nbsp; &nbsp; &nbsp; trans.Commit(); &nbsp; &nbsp; } &nbsp; } &nbsp; catch (Exception exp) &nbsp; { &nbsp; &nbsp; logger.Error( &quot;Exception occurred during transaction&quot;, exp ); &nbsp; }
```

```csharp
&nbsp; try &nbsp; { &nbsp; &nbsp; using( var trans = new Transaction( doc, &quot;Transaction Name&quot; ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; trans.Start(); &nbsp; &nbsp; &nbsp; &nbsp; /////////////////////////////////////////////////////// &nbsp; &nbsp; &nbsp; ///////////DO SOMETHING TO THE MODEL/////////////////// &nbsp; &nbsp; &nbsp; /////////////////////////////////////////////////////// &nbsp; &nbsp; &nbsp; &nbsp; var commitStatus = trans.Commit(); &nbsp; &nbsp; &nbsp; &nbsp; if( commitStatus != TransactionStatus.Committed ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; logger.Warn( &quot;Transaction &quot; + trans.GetName() &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + &quot; did not commit. Status = &quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + commitStatus.ToString() ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; catch( Exception exp ) &nbsp; { &nbsp; &nbsp; logger.Error( &quot;Exception occured durring transaction&quot;, exp ); &nbsp; }
```

```csharp
&nbsp; using(TransactionGroup tgroup = new TransactionGroup(document)) &nbsp; { &nbsp; &nbsp; tgroup.Start(); &nbsp; &nbsp; using(Transaction trans = new Transaction(document)) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; trans.Start(&quot;Change 1&quot;); &nbsp; &nbsp; &nbsp; &nbsp; MakeMyChanges(document); &nbsp; &nbsp; &nbsp; &nbsp; if(trans.Commit() != TransactionStatus.Commited) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; tgroup.RollBack(); &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; return err_code; // or throw an exception &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; trans.Start(&quot;Change 2&quot;); &nbsp; &nbsp; &nbsp; &nbsp; MakeMyOtherChanges(document); &nbsp; &nbsp; &nbsp; &nbsp; if(trans.Commit() != TransactionStatus.Commited) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; tgroup.RollBack() &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; return err_code; // or throw an exception &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; tgroup.Commit(); &nbsp; }
```
