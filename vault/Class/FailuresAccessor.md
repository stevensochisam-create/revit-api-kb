---
type: FailuresAccessor
namespace: Autodesk.Revit.DB
version: 2024
members: 30
tags: [revit-api, class]
---

# FailuresAccessor

`Autodesk.Revit.DB.FailuresAccessor` · Revit 2024 · 30 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanCommitPendingTransaction | 2011 | `public bool CanCommitPendingTransaction ()` |
| Method | CanRollBackPendingTransaction | 2011 | `public bool CanRollBackPendingTransaction ()` |
| Method | CommitPendingTransaction | 2011 | `public TransactionStatus CommitPendingTransaction ()` |
| Method | DeleteAllWarnings | 2011 | `public void DeleteAllWarnings ()` |
| Method | DeleteElements | 2011 | `public void DeleteElements ( IList < ElementId > idsToDelete )` |
| Method | DeleteWarning | 2011 | `public void DeleteWarning ( FailureMessageAccessor failure )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAttemptedResolutionTypes | 2011 | `public IList < FailureResolutionType > GetAttemptedResolutionTypes ( FailureMessageAccessor failure )` |
| Method | GetDocument | 2011 | `public Document GetDocument ()` |
| Method | GetFailureHandlingOptions | 2011 | `public FailureHandlingOptions GetFailureHandlingOptions ()` |
| Method | GetFailureMessages | — | `` |
| Method | GetFailureMessages | 2011 | `public IList < FailureMessageAccessor > GetFailureMessages ()` |
| Method | GetSeverity | 2011 | `public FailureSeverity GetSeverity ()` |
| Method | GetTransactionName | 2011 | `public string GetTransactionName ()` |
| Method | IsActive | 2011 | `public bool IsActive ()` |
| Method | IsElementsDeletionPermitted | — | `` |
| Method | IsElementsDeletionPermitted | 2011 | `public bool IsElementsDeletionPermitted ()` |
| Method | IsFailureResolutionPermitted | — | `` |
| Method | IsFailureResolutionPermitted | 2011 | `public bool IsFailureResolutionPermitted ()` |
| Method | IsPending | 2011 | `public bool IsPending ()` |
| Method | IsTransactionBeingCommitted | 2011 | `public bool IsTransactionBeingCommitted ()` |
| Method | JournalFailures | 2011 | `public void JournalFailures ( IList < FailureMessageAccessor > failures )` |
| Method | PostFailure | 2011 | `public void PostFailure ( FailureMessage failure )` |
| Method | ReplaceFailures | 2011 | `public void ReplaceFailures ( FailureMessage failure )` |
| Method | ResolveFailure | 2011 | `public void ResolveFailure ( FailureMessageAccessor failure )` |
| Method | ResolveFailures | 2011 | `public void ResolveFailures ( IList < FailureMessageAccessor > failures )` |
| Method | RollBackPendingTransaction | 2011 | `public TransactionStatus RollBackPendingTransaction ()` |
| Method | SetFailureHandlingOptions | 2011 | `public void SetFailureHandlingOptions ( FailureHandlingOptions options )` |
| Method | SetTransactionName | 2011 | `public void SetTransactionName ( string transactionName )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |