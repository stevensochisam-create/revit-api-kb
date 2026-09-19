---
num: 1700
date: 2018-11-10
themes: [Transaction]
tags: [revit-api, tbc]
---

# More on Transaction Groups and Assimilation

<https://jeremytammik.github.io/tbc/a/1700_transaction_group.html>

```csharp
&nbsp;&nbsp;public&nbsp;void&nbsp;Execute(&nbsp;RvtUiApplication&nbsp;app&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;WpfTarget.Transactions.ContainsKey(&nbsp;this.GetName()&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transaction&nbsp;=&nbsp;WpfTarget.Transactions[GetName()]; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;Transaction&nbsp;==&nbsp;null&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transaction&nbsp;=&nbsp;new&nbsp;Transaction(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WpfTarget.CmdVars.DbDoc,&nbsp;GetName()&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WpfTarget.Transactions[GetName()]&nbsp;=&nbsp;this.Transaction; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;else &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WpfTarget.Transactions.Add(&nbsp;GetName(),&nbsp;new&nbsp;Transaction(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WpfTarget.CmdVars.DbDoc,&nbsp;GetName()&nbsp;)&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;WpfTarget.TransGroup.Start(); &nbsp;&nbsp;&nbsp;&nbsp;Transaction.Start(); &nbsp;&nbsp;&nbsp;&nbsp;Level.Create(&nbsp;WpfTarget.CmdVars.DbDoc,&nbsp;30&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;Transaction.Commit(); &nbsp;&nbsp;&nbsp;&nbsp;WpfTarget.TransGroup.Assimilate(); &nbsp;&nbsp;}
```
