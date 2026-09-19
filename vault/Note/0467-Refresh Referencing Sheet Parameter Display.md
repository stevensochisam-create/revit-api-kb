---
num: 467
date: 2010-11-01
themes: [Parameter]
tags: [revit-api, tbc]
---

# Refresh Referencing Sheet Parameter Display

<https://jeremytammik.github.io/tbc/a/0467_refresh_referencing_sheet.htm>

```csharp
void UpdateReferencingSheet( &nbsp; ViewSection selectedViewport ) { &nbsp; BuiltInParameter bip &nbsp; &nbsp; = BuiltInParameter.VIEW_DISCIPLINE; &nbsp; &nbsp; Parameter discipline &nbsp; &nbsp; = selectedViewport.get_Parameter( bip ); &nbsp; &nbsp; int disciplineNo = discipline.AsInteger(); &nbsp; &nbsp; Document doc = selectedViewport.Document; &nbsp; &nbsp; Transaction transaction = new Transaction( doc ); &nbsp; &nbsp; if( TransactionStatus.Started &nbsp; &nbsp; == transaction.Start( &quot;Updating the model&quot; ) ) &nbsp; { &nbsp; &nbsp; switch( disciplineNo ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; case 1: &nbsp; &nbsp; &nbsp; &nbsp; discipline.Set( 2 ); &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; default: &nbsp; &nbsp; &nbsp; &nbsp; discipline.Set( 1 ); &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; } &nbsp; } &nbsp; discipline.Set( disciplineNo ); &nbsp; transaction.Commit(); }
```
