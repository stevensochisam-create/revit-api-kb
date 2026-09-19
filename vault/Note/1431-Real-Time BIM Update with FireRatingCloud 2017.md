---
num: 1431
date: 2016-04-26
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Real-Time BIM Update with FireRatingCloud 2017

<https://jeremytammik.github.io/tbc/a/1431_firerating_2017.html>

```csharp
[Transaction(&nbsp;TransactionMode.ReadOnly&nbsp;)] class&nbsp;Cmd_4_Subscribe&nbsp;:&nbsp;IExternalCommand { &nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;Result&nbsp;Execute( &nbsp;&nbsp;&nbsp;&nbsp;ExternalCommandData&nbsp;commandData, &nbsp;&nbsp;&nbsp;&nbsp;ref&nbsp;string&nbsp;message, &nbsp;&nbsp;&nbsp;&nbsp;ElementSet&nbsp;elements&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;UIApplication&nbsp;uiapp&nbsp;=&nbsp;commandData.Application; &nbsp;&nbsp;&nbsp;&nbsp;Document&nbsp;doc&nbsp;=&nbsp;uiapp.ActiveUIDocument.Document; &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Determine&nbsp;custom&nbsp;project&nbsp;identifier. &nbsp;&nbsp;&nbsp;&nbsp;string&nbsp;project_id&nbsp;=&nbsp;Util.GetProjectIdentifier(&nbsp;doc&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(&nbsp;!App.Subscribed&nbsp;&amp;&amp;&nbsp;0&nbsp;==&nbsp;DbAccessor.Timestamp&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DbAccessor.Init(&nbsp;project_id&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;DbAccessor.ToggleSubscription(&nbsp;uiapp&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;Result.Succeeded; &nbsp;&nbsp;} }
```
