---
num: 1556
date: 2017-05-11
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Prompt Cancel Throws Exception in Revit 2018

<https://jeremytammik.github.io/tbc/a/1556_prompt_exception.html>

```csharp
Try &nbsp;&nbsp;docUi.PromptForFamilyInstancePlacement(FamilySymbol) Catch&nbsp;ex&nbsp;As&nbsp;Exceptions.OperationCanceledException &nbsp;&nbsp;&#39;&nbsp;The&nbsp;user&nbsp;cancelled&nbsp;placement. &nbsp;&nbsp;&#39;&nbsp;This&nbsp;should&nbsp;only&nbsp;trigger&nbsp;in&nbsp;Revit&nbsp;2018. &nbsp;&nbsp;&#39;&nbsp;Do&nbsp;something&nbsp;if&nbsp;you&nbsp;like End&nbsp;Try
```

```csharp
try { &nbsp;&nbsp;uidoc.PromptForFamilyInstancePlacement(&nbsp;symbol&nbsp;); } catch(&nbsp;Autodesk.Revit.Exceptions.OperationCanceledException&nbsp;ex&nbsp;) { &nbsp;&nbsp;Debug.Print(&nbsp;ex.Message&nbsp;); }
```
