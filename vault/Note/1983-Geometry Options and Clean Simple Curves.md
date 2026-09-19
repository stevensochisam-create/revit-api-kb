---
num: 1983
date: 2023-02-24
themes: [Geometry]
tags: [revit-api, tbc]
---

# Geometry Options and Clean Simple Curves

<https://jeremytammik.github.io/tbc/a/1983_geo_opt_curve.html>

```csharp
Public timer1 As Timer Public timer_interval As Integer = 1000 'millisecondi Public timer_attempts As Integer 'not used Public Const diagTitle As String = "Aggiornamento del modello analitico strutturale" Public Const diagButton As String = "&Chiudi" Public Function EnumWindowsProc(ByVal hwnd As Integer, ByVal lParam As Integer) As Boolean Dim sbTitle As New StringBuilder(256) Dim test As Integer = User32.GetWindowText(hwnd, sbTitle, sbTitle.Capacity) Dim title As String = sbTitle.ToString() If title.Length &gt; 0 AndAlso title = diagTitle Then User32.EnumChildWindows(hwnd, New User32.EnumWindowsProc(AddressOf EnumChildProc), 0) Return False Else Return True End If End Function Public Function EnumChildProc(ByVal hwnd As Integer, ByVal lParam As Integer) As Boolean Dim sbTitle As New StringBuilder(256) User32.GetWindowText(hwnd, sbTitle, sbTitle.Capacity) Dim title As String = sbTitle.ToString() If title.Length &gt; 0 AndAlso title = diagButton Then User32.SendMessage(hwnd, User32.BM_SETSTATE, 1, 0) User32.SendMessage(hwnd, User32.WM_LBUTTONDOWN, 0, 0) User32.SendMessage(hwnd, User32.WM_LBUTTONUP, 0, 0) User32.SendMessage(hwnd, User32.BM_SETSTATE, 1, 0) If Not timer1 Is Nothing Then timer1.Stop() timer1 = Nothing End If Return False Else Return True End If End Function Public Sub timer1_Elapsed(ByVal sender As Object, ByVal e As EventArgs) 'If timer_attempts &lt; 3000 Then User32.EnumWindows(New User32.EnumWindowsProc(AddressOf EnumWindowsProc), 0) 'Else ' timer1.Stop() 'End If 'timer_attempts += 1 'Debug.Print(timer_attempts.ToString()) End Sub Public Sub closeOptionsDialog() timer_attempts = 0 If timer1 Is Nothing Then timer1 = New Timer() End If timer1.Interval = timer_interval AddHandler timer1.Elapsed, New ElapsedEventHandler(AddressOf timer1_Elapsed) timer1.Start() End Sub
```

```csharp
Imports System Imports System.Runtime.InteropServices Imports System.Text Module User32 Delegate Function EnumWindowsProc(ByVal hWnd As Integer, ByVal lParam As Integer) As Boolean &lt;DllImport("user32.dll", CharSet:=CharSet.Unicode)&gt; Function FindWindow(ByVal className As String, ByVal windowName As String) As Integer End Function &lt;DllImport("user32.dll", CharSet:=CharSet.Unicode)&gt; Function EnumWindows(ByVal callbackFunc As EnumWindowsProc, ByVal lParam As Integer) As Integer End Function &lt;DllImport("user32.dll", CharSet:=CharSet.Unicode)&gt; Function EnumChildWindows(ByVal hwnd As Integer, ByVal callbackFunc As EnumWindowsProc, ByVal lParam As Integer) As Integer End Function &lt;DllImport("user32.dll", CharSet:=CharSet.Unicode)&gt; Function GetWindowText(ByVal hwnd As Integer, ByVal buff As StringBuilder, ByVal maxCount As Integer) As Integer End Function &lt;DllImport("user32.dll", CharSet:=CharSet.Unicode)&gt; Function GetLastActivePopup(ByVal hwnd As Integer) As Integer End Function &lt;DllImport("user32.dll", CharSet:=CharSet.Unicode)&gt; Function SendMessage(ByVal hwnd As Integer, ByVal Msg As Integer, ByVal wParam As Integer, ByVal lParam As Integer) As Integer End Function Public BM_SETSTATE As Integer = 243 Public WM_LBUTTONDOWN As Integer = 513 Public WM_LBUTTONUP As Integer = 514 End Module
```
