---
num: 1954
date: 2022-06-07
themes: [Parameter]
tags: [revit-api, tbc]
---

# Parameters, Snippets, Batch Mode and Self-Signing

<https://jeremytammik.github.io/tbc/a/1954_batch_snip_selfsign.html>

```csharp
Private IntRegenCount As Integer = 0 Private Sub ProgressChanged(a As Object, e As Autodesk.Revit.DB.Events.ProgressChangedEventArgs) If e.Caption = "Regenerating" Then IntRegenCount += 1 End If If IntRegenCount > 2200 Then 'IntRegenCount = 0 e.Cancel() End If End Sub Public Function Obj_220516d(commandData As ExternalCommandData, ByRef message As String, elements As ElementSet) As Result Dim IntUIApp As UIApplication = commandData.Application Dim IntUIDoc As UIDocument = commandData.Application.ActiveUIDocument Dim IntDoc As Document = IntUIDoc.Document AddHandler commandData.Application.Application.ProgressChanged, AddressOf ProgressChanged Const NM As String = "Vantage Metro Series Hinged Door Jamb" Dim FEC As New FilteredElementCollector(IntDoc) Dim ECF As New ElementClassFilter(GetType(Family)) Dim F As Family = FEC.WherePasses(ECF) _ .Where(Function(x) x.Name = NM) _ .Cast(Of Family) _ .FirstOrDefault Dim FDoc As Document = Nothing Try FDoc = IntDoc.EditFamily(F) Catch ex As Exception Return Result.Cancelled Finally RemoveHandler commandData.Application.Application.ProgressChanged, AddressOf ProgressChanged End Try Return Result.Succeeded End Function
```

```csharp
Private IntProgressLog As Integer() = New Integer(20) {} Private Sub ProgressChanged(s As Object, e As Autodesk.Revit.DB.Events.ProgressChangedEventArgs) Dim ULim As Double = e.UpperRange Dim Pos As Double = e.Position Dim Perc As Integer = ((Pos / ULim) * 20) IntProgressLog(Perc) += 1 Dim N As Integer = IntProgressLog.Max Dim T As Integer = IntProgressLog.Sum If N > 2000 OrElse T > 15000 Then e.Cancel() End If End Sub Private Sub MsgBoxShowing(s As Object, e As Autodesk.Revit.UI.Events.DialogBoxShowingEventArgs) Dim IntUIApp As UIApplication = s IntProgressLog = New Integer(20) {} 'reset the variable for next family e.OverrideResult(2) End Sub Public Function Obj_220516d(commandData As ExternalCommandData, ByRef message As String, elements As ElementSet) As Result Dim IntUIApp As UIApplication = commandData.Application Dim IntUIDoc As UIDocument = commandData.Application.ActiveUIDocument Dim IntDoc As Document = IntUIDoc.Document AddHandler IntUIApp.Application.ProgressChanged, AddressOf ProgressChanged AddHandler IntUIApp.DialogBoxShowing, AddressOf MsgBoxShowing Dim NM As String() = New String(1) {"Vantage Metro Series Hinged Door Jamb", "_ Callout Head"} Dim FDoc As Document = Nothing For i = 0 To 1 Dim K As Integer = i Dim FEC As New FilteredElementCollector(IntDoc) Dim ECF As New ElementClassFilter(GetType(Family)) Dim F As Family = FEC.WherePasses(ECF) _ .Where(Function(x) x.Name = NM(K)) _ .Cast(Of Family) _ .FirstOrDefault Try FDoc = IntDoc.EditFamily(F) Catch ex As Exception End Try If FDoc IsNot Nothing Then Debug.WriteLine("Edit of: " & NM(i)) End If Next RemoveHandler IntUIApp.Application.ProgressChanged, AddressOf ProgressChanged RemoveHandler IntUIApp.DialogBoxShowing, AddressOf MsgBoxShowing Return Result.Succeeded End Function
```
