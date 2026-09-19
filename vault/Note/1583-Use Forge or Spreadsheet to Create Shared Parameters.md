---
num: 1583
date: 2017-09-11
themes: [Parameter]
tags: [revit-api, tbc]
---

# Use Forge or Spreadsheet to Create Shared Parameters

<https://jeremytammik.github.io/tbc/a/1583_rvtmetaprop.html>

```csharp
"externalId","component","displayCategory","categoryId","displayName","displayValue","metaType","filelink","filename","link" "7df7740a-9736-4a3e-81ec-45e05b0d2ad2-0000c28d","Basic Wall [49805]","General","PG_GENERAL","test_text","this is a text added in forge","Text",,, "7df7740a-9736-4a3e-81ec-45e05b0d2ad2-0000c28d","Basic Wall [49805]","General","PG_GENERAL","test_real","0.12","Double",,, "7df7740a-9736-4a3e-81ec-45e05b0d2ad2-0000c28d","Basic Wall [49805]","General","PG_GENERAL","test_int","12","Int",,,
```

```csharp
[ { "displayCategory": "General", "displayValue": "this is a text added in forge", "displayName": "test_text", "categoryId": "PG_GENERAL", "externalId": "7df7740a-9736-4a3e-81ec-45e05b0d2ad2-0000c28d", "component": "Basic Wall [49805]", "metaType": "Text" }, { "displayCategory": "General", "displayValue": "0.12", "displayName": "test_real", "categoryId": "PG_GENERAL", "externalId": "7df7740a-9736-4a3e-81ec-45e05b0d2ad2-0000c28d", "component": "Basic Wall [49805]", "metaType": "Double" }, { "displayCategory": "General", "displayValue": "12", "displayName": "test_int", "categoryId": "PG_GENERAL", "externalId": "7df7740a-9736-4a3e-81ec-45e05b0d2ad2-0000c28d", "component": "Basic Wall [49805]", "metaType": "Int" } ]
```
