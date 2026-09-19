---
num: 75
date: 2009-01-19
themes: [Transaction]
tags: [revit-api, tbc]
---

# Transaction Responsibility

<https://jeremytammik.github.io/tbc/a/0075_transaction_responsibility.htm>

```csharp
void application_OnDocumentNewed( Document doc ) { &nbsp; // we cannot modify the document &nbsp; // unless a transaction is started &nbsp; &nbsp; if( doc.BeginTransaction() ) &nbsp; { &nbsp; &nbsp; // once a new transaction is started &nbsp; &nbsp; // we are responsible for ending or &nbsp; &nbsp; // aborting it, so we have to put &nbsp; &nbsp; // everything in a try-catch block &nbsp; &nbsp; &nbsp; try &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; CreateUserDefinedParameters( doc ); &nbsp; &nbsp; &nbsp; &nbsp; // we are responsible for ending &nbsp; &nbsp; &nbsp; // the transaction we started &nbsp; &nbsp; &nbsp; &nbsp; doc.EndTransaction(); &nbsp; &nbsp; } &nbsp; &nbsp; catch( Exception ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // if we cannot finish what we wanted &nbsp; &nbsp; &nbsp; // we should probably abort the whole thing &nbsp; &nbsp; &nbsp; &nbsp; doc.AbortTransaction(); &nbsp; &nbsp; &nbsp; throw; // re-throw the exception &nbsp; &nbsp; } &nbsp; } }
```
