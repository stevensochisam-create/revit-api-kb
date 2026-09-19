---
num: 1131
date: 2014-04-09
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2015 API News &ndash; DevDays Online Recording

<https://jeremytammik.github.io/tbc/a/1131_revit_2015_api_news.htm>

```csharp
&nbsp; Public CommandToIssue As RevitCommandId
```

```csharp
&nbsp; Private Sub PictureBox2_Click( _ &nbsp; &nbsp; ByVal sender As Object, _ &nbsp; &nbsp; ByVal e As EventArgs) _ &nbsp; Handles PictureBox2.Click &nbsp; &nbsp; CommandToIssue _ &nbsp; &nbsp; &nbsp; = RevitCommandId.LookupPostableCommandId( _ &nbsp; &nbsp; &nbsp; &nbsp; PostableCommand.StructuralColumn) &nbsp; &nbsp; Close() &nbsp; End Sub
```

```csharp
&nbsp; Private Sub WheelForm_Shown( _ &nbsp; &nbsp; ByVal sender As Object, _ &nbsp; &nbsp; ByVal e As EventArgs) _ &nbsp; Handles Me.Shown &nbsp; &nbsp; Location = New System.Drawing.Point( _ &nbsp; &nbsp; &nbsp; CInt(MousePosition.X - (Me.Width / 2)), _ &nbsp; &nbsp; &nbsp; CInt(MousePosition.Y - (Me.Width / 2))) &nbsp; End Sub
```

```csharp
Option Strict On Option Explicit On &nbsp; Imports Autodesk.Revit.Attributes Imports Autodesk.Revit.UI &nbsp; Imports BrevitTools.UI.Wheel &nbsp; &lt;Transaction(TransactionMode.Manual)&gt; _ Public Class Wheel &nbsp; Implements IExternalCommand &nbsp; &nbsp; Public Function Execute( _ &nbsp; &nbsp; ByVal cmdData As ExternalCommandData, _ &nbsp; &nbsp; ByRef message As String, _ &nbsp; &nbsp; ByVal elements As Autodesk.Revit.DB.ElementSet) _ &nbsp; As Result Implements IExternalCommand.Execute &nbsp; &nbsp; &nbsp; Dim form As New WheelForm &nbsp; &nbsp; form.ShowDialog() &nbsp; &nbsp; &nbsp; If form.CommandToIssue IsNot Nothing Then &nbsp; &nbsp; &nbsp; cmdData.Application.PostCommand( &nbsp; &nbsp; &nbsp; &nbsp; form.CommandToIssue) &nbsp; &nbsp; End If &nbsp; &nbsp; &nbsp; Return Result.Succeeded &nbsp; &nbsp; End Function &nbsp; End Class
```
