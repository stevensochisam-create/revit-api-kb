---
num: 1149
date: 2014-05-08
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Multithreading Throws Exceptions in Revit 2015

<https://jeremytammik.github.io/tbc/a/1149_exception_in_2015.htm>

```csharp
bw.ReportProgress(progress, notification);
```

```csharp
bw.ProgressChanged += new ProgressChangedEventHandler( delegate(object o, ProgressChangedEventArgs args) { bProg.Value = args.ProgressPercentage; labelPerc.Text = args.ProgressPercentage + "%"; labelLoading.Text = args.UserState.ToString(); }); void reportProgress(int progressvalue, string notification) { bProg.Value = progressvalue; labelPerc.Text = progressvalue + "%"; labelLoading.Text = notification; System.Windows.Forms.Application.DoEvents(); }
```
