---
num: 1280
date: 2015-02-11
themes: [Pitfall, Transaction]
tags: [revit-api, tbc]
---

# Using Transaction Groups

<https://jeremytammik.github.io/tbc/a/1280_transaction_group.htm>

```csharp
&nbsp; using( TransactionGroup transGroup = new TransactionGroup( document ) ) &nbsp; { &nbsp; &nbsp; transGroup.Start( &quot;Transaction Group&quot; ); &nbsp; &nbsp; &nbsp; using( Transaction firstTrans = new Transaction( document ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; try &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; firstTrans.Start( &quot;First Transaction&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // do some stuff &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; firstTrans.Commit(); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; catch &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; transGroup.Rollback(); // &lt;-- We do not have to roll back firstTrans? &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; using( Transaction secondTrans = new Transaction( document ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; try &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; secondTrans.Start( &quot;Second Transaction&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // do some stuff &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; secondTrans.Commit(); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; catch &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; transGroup.Rollback(); // &lt;-- We do not have to roll back secondTrans? &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; transGroup.Assimilate(); &nbsp; &nbsp; &nbsp; return Result.Succeeded; &nbsp; }
```

```csharp
&nbsp; using( TransactionGroup transGroup &nbsp; &nbsp; = new TransactionGroup( document ) ) &nbsp; { &nbsp; &nbsp; using( Transaction trans &nbsp; &nbsp; &nbsp; = new Transaction( document ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; try &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; transGroup.Start( &quot;Action&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; trans.Start( &quot;First Transaction&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // do some stuff &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( trans.Commit() != TransactionStatus.Committed ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; trans.Start( &quot;Second Transaction&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // do some more stuff &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; trans.Commit(); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if( trans.Commit() != TransactionStatus.Committed ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; transGroup.Assimilate(); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; catch &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return Result.Succeeded; &nbsp; }
```
