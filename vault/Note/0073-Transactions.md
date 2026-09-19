---
num: 73
date: 2009-01-18
themes: [Transaction]
tags: [revit-api, tbc]
---

# Transactions

<https://jeremytammik.github.io/tbc/a/0073_transaction.htm>

```csharp
void application_OnDocumentNewed( Document doc ) { &nbsp; bool rc = doc.BeginTransaction(); &nbsp; Debug.Assert( rc, "begin transaction failed" ); &nbsp; if( rc ) &nbsp; { &nbsp; &nbsp; CreateUserDefinedParameters( doc ); &nbsp; &nbsp; rc = doc.EndTransaction(); &nbsp; &nbsp; Debug.Assert( rc, "end transaction failed" ); &nbsp; } }
```
