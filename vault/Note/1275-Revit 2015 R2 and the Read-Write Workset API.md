---
num: 1275
date: 2015-02-03
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2015 R2 and the Read-Write Workset API

<https://jeremytammik.github.io/tbc/a/1275_r2_workset_api.htm>

```csharp
&nbsp; Private Sub CreateWorkset(name As String) &nbsp; &nbsp; Using t As New Transaction(m_Doc) &nbsp; &nbsp; &nbsp; t.Start(&quot;Create Workset&quot;) &nbsp; &nbsp; &nbsp; Workset.Create(m_Doc, name) &nbsp; &nbsp; &nbsp; t.Commit() &nbsp; &nbsp; End Using &nbsp; End Sub
```
