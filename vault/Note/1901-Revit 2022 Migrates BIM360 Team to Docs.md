---
num: 1901
date: 2021-04-15
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2022 Migrates BIM360 Team to Docs

<https://jeremytammik.github.io/tbc/a/1901_bim360_team_to_docs.html>

```csharp
Document.SaveAsCloudModel(Guid, Guid, String, String)
```

```csharp
#pragma&nbsp;warning&nbsp;disable&nbsp;CS0618 &nbsp;&nbsp;//&nbsp;warning&nbsp;CS0618:&nbsp;`DisplayUnitType`&nbsp;is&nbsp;obsolete:&nbsp; &nbsp;&nbsp;//&nbsp;This&nbsp;enumeration&nbsp;is&nbsp;deprecated&nbsp;in&nbsp;Revit&nbsp;2021&nbsp;and&nbsp;may&nbsp;be&nbsp;removed&nbsp;in&nbsp;a&nbsp;future&nbsp;version&nbsp;of&nbsp;Revit.&nbsp; &nbsp;&nbsp;//&nbsp;Please&nbsp;use&nbsp;the&nbsp;`ForgeTypeId`&nbsp;class&nbsp;instead.&nbsp; &nbsp;&nbsp;//&nbsp;Use&nbsp;constant&nbsp;members&nbsp;of&nbsp;the&nbsp;`UnitTypeId`&nbsp;class&nbsp;to&nbsp;replace&nbsp;uses&nbsp;of&nbsp;specific&nbsp;values&nbsp;of&nbsp;this&nbsp;enumeration. &nbsp;&nbsp;if(&nbsp;2&nbsp;==&nbsp;parameters.Length&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;ParameterInfo&nbsp;p1&nbsp;=&nbsp;parameters.First(); &nbsp;&nbsp;&nbsp;&nbsp;ParameterInfo&nbsp;p2&nbsp;=&nbsp;parameters.Last(); &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;p1.ParameterType&nbsp;==&nbsp;typeof(&nbsp;Field&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&amp;&amp;&nbsp;(p2.ParameterType&nbsp;==&nbsp;typeof(&nbsp;DisplayUnitType&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;||&nbsp;p2.ParameterType&nbsp;==&nbsp;typeof(&nbsp;ForgeTypeId&nbsp;)); &nbsp;&nbsp;} #pragma&nbsp;warning&nbsp;restore&nbsp;CS0618
```
