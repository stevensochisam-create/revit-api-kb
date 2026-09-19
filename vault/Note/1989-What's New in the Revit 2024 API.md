---
num: 1989
date: 2023-04-11
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# What's New in the Revit 2024 API

<https://jeremytammik.github.io/tbc/a/1989_whats_new_2024.html>

```csharp
AssetPropertyInteger decalElementIdProp = (asset.FindByName("decalelementId") as AssetPropertyInteger); if (decalElementIdProp.Type == AssetPropertyType.Integer)
```

```csharp
AssetPropertyInt64 decalElementIdProp = (asset.FindByName("decalelementId") as AssetPropertyInt64); if (decalElementIdProp.Type == AssetPropertyType.Longlong)
```
