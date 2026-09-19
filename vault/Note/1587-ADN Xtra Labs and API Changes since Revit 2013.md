---
num: 1587
date: 2017-09-20
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# ADN Xtra Labs and API Changes since Revit 2013

<https://jeremytammik.github.io/tbc/a/1587_changes_xtra.html>

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Event&nbsp;handler&nbsp;for&nbsp;the&nbsp;above&nbsp;combo&nbsp;box&nbsp; ///&nbsp;&lt;/summary&gt;&nbsp;&nbsp;&nbsp;&nbsp; void&nbsp;comboBx_CurrentChanged( &nbsp;&nbsp;object&nbsp;sender, &nbsp;&nbsp;ComboBoxCurrentChangedEventArgs&nbsp;e&nbsp;) { &nbsp;&nbsp;//&nbsp;Cast&nbsp;sender&nbsp;as&nbsp;TextBox&nbsp;to&nbsp;retrieve&nbsp;text&nbsp;value &nbsp;&nbsp;ComboBox&nbsp;combodata&nbsp;=&nbsp;sender&nbsp;as&nbsp;ComboBox; &nbsp;&nbsp;ComboBoxMember&nbsp;member&nbsp;=&nbsp;combodata.Current; &nbsp;&nbsp;TaskDialog.Show(&nbsp;&quot;Combobox&nbsp;Selection&quot;, &quot;Your&nbsp;new&nbsp;selection:&nbsp;&quot;&nbsp;+&nbsp;member.ItemText&nbsp;); }
```
