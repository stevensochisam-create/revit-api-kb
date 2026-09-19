---
num: 1951
date: 2022-05-09
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2023 API Docs and Disabling an Error Failure

<https://jeremytammik.github.io/tbc/a/1951_disable_error_failure.html>

```csharp
&nbsp;&nbsp;if&nbsp;(failureAccessor.HasResolutionOfType( &nbsp;&nbsp;&nbsp;&nbsp;FailureResolutionType.DeleteElements)) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;failureAccessor.SetCurrentResolutionType( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FailureResolutionType.DeleteElements); &nbsp;&nbsp;&nbsp;&nbsp;failuresAccessor.ResolveFailure(failureAccessor); &nbsp;&nbsp;}
```

```csharp
&nbsp;&nbsp;public&nbsp;class&nbsp;AutoDetachOrDeleteFailurePreprocessor&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;IFailuresPreprocessor &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;FailureProcessingResult&nbsp;PreprocessFailures( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FailuresAccessor&nbsp;failuresAccessor) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;preprocessorMessages &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;failuresAccessor.GetFailureMessages(FailureSeverity.Error) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Union(failuresAccessor.GetFailureMessages(FailureSeverity.Warning)) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Where(x&nbsp;=&gt;&nbsp;x.HasResolutionOfType(FailureResolutionType.DeleteElements) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;x.HasResolutionOfType(FailureResolutionType.DetachElements)) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.ToList(); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(preprocessorMessages.Count&nbsp;==&nbsp;0) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;FailureProcessingResult.Continue; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;foreach&nbsp;(var&nbsp;failureAccessor&nbsp;in&nbsp;preprocessorMessages) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failureAccessor.SetCurrentResolutionType( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failureAccessor.HasResolutionOfType(FailureResolutionType.DetachElements)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?&nbsp;FailureResolutionType.DetachElements&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;FailureResolutionType.DeleteElements); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failuresAccessor.ResolveFailure(failureAccessor); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;FailureProcessingResult.ProceedWithCommit; &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;}
```

```csharp
failureOptions.SetClearAfterRollback(true);
```

```csharp
public FailureProcessingResult PreprocessFailures(FailuresAccessor failuresAccessor) { IList failList = new List(); failList = failuresAccessor.GetFailureMessages(); // Inside event handler, get all warnings foreach (FailureMessageAccessor failure in failList) { FailureDefinitionId failID = failure.GetFailureDefinitionId(); if (failID == BuiltInFailures.DPartFailures.DeletingDPartWillDeleteMorePartsError) { failure.SetCurrentResolutionType(FailureResolutionType.Default); failuresAccessor.ResolveFailure(failure); failuresAccessor.GetFailureHandlingOptions().SetClearAfterRollback(true); return FailureProcessingResult.ProceedWithRollBack; } } return FailureProcessingResult.Continue; }
```

```csharp
&nbsp;&nbsp;var&nbsp;failureOptions&nbsp;=&nbsp;transaction.GetFailureHandlingOptions(); &nbsp;&nbsp;failureOptions.SetClearAfterRollback(true); &nbsp;&nbsp;//... &nbsp;&nbsp;transaction.SetFailureHandlingOptions(failureOptions); &nbsp;&nbsp;transaction.Start();
```
