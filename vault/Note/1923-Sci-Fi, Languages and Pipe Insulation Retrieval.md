---
num: 1923
date: 2021-10-14
themes: [MEP]
tags: [revit-api, tbc]
---

# Sci-Fi, Languages and Pipe Insulation Retrieval

<https://jeremytammik.github.io/tbc/a/1923_mep_insulation.html>

```csharp
&nbsp;&nbsp;var&nbsp;pipeInsulation&nbsp;=&nbsp;pipe &nbsp;&nbsp;&nbsp;&nbsp;.GetDependentElements(&nbsp;new&nbsp;ElementClassFilter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;typeof(&nbsp;PipeInsulation&nbsp;)&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.Select(&nbsp;pipe.Document.GetElement&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;PipeInsulation&gt;() &nbsp;&nbsp;&nbsp;&nbsp;.FirstOrDefault();
```

```csharp
&nbsp;&nbsp;var&nbsp;pipeInsulation&nbsp;=&nbsp;InsulationLiningBase &nbsp;&nbsp;&nbsp;&nbsp;.GetInsulationIds(&nbsp;pipe.Document,&nbsp;pipe.Id&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.Select(&nbsp;pipe.Document.GetElement&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.OfType&lt;PipeInsulation&gt;() &nbsp;&nbsp;&nbsp;&nbsp;.FirstOrDefault();
```
