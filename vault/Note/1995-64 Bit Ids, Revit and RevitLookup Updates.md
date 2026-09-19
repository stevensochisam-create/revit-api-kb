---
num: 1995
date: 2023-05-23
themes: [ElementId, Pitfall]
tags: [revit-api, tbc]
---

# 64 Bit Ids, Revit and RevitLookup Updates

<https://jeremytammik.github.io/tbc/a/1995_lookup.html>

```csharp
Category.GetCategory(); Document.GetDocumentVersion() UIDocument.GetRevitUIFamilyLoadOptions() Application.MinimumThickness
```

```csharp
Module RT_ElementIdExtensionModule #If RvtVer &gt;= 2024 Then &lt;Extension&gt; Public Function NewElementId(L As Long) As ElementId Return New ElementId(L) End Function #Else &lt;Extension&gt; Public Function Value(ID As ElementId) As Long Return ID.IntegerValue End Function &lt;Extension&gt; Public Function NewElementId(L As Long) As ElementId If L &gt; Int32.MaxValue OrElse L &lt; Int32.MinValue Then Throw New OverflowException("Value for ElementId out of range.") End If Return New ElementId(CInt(L)) End Function #End If End Module
```
